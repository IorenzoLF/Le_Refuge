#!/usr/bin/env python3
"""
SOLVEUR ARC ZONES V11 SIMPLE - Refuge ARC-AGI
Version simplifiee du solveur avec detection de remplissage de zones
"""

import json
import sys
import os
import numpy as np
from typing import List, Dict, Any, Tuple, Optional, Set
from dataclasses import dataclass, field
from pathlib import Path
from collections import deque

# Ajouter src au path
sys.path.insert(0, '../../../src')
sys.path.insert(0, 'src')

try:
    from pattern_detector_simple import PatternDetector
except ImportError as e:
    print(f"Erreur d'import: {e}")
    PatternDetector = None

@dataclass
class TacheARC:
    """Tache ARC avec donnees d'entrainement et de test"""
    tache_id: str
    train: List[Dict[str, Any]]
    test: List[Dict[str, Any]]

class ZoneAnalyzer:
    """Analyseur de zones et de remplissage"""
    
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, Bas, Gauche, Droite
    
    def detecter_zones_fermees(self, grid: List[List[int]], couleur_contour: int) -> Set[Tuple[int, int]]:
        """Detecter les zones fermees (pixels vides entoures par des contours)"""
        hauteur, largeur = len(grid), len(grid[0])
        zones_fermees = set()
        
        # Pour chaque pixel vide, verifier s'il est dans une zone fermee
        for i in range(hauteur):
            for j in range(largeur):
                if grid[i][j] == 0:  # Pixel vide
                    if self._est_zone_fermee(grid, i, j, couleur_contour):
                        zones_fermees.add((i, j))
        
        return zones_fermees
    
    def _est_zone_fermee(self, grid: List[List[int]], start_i: int, start_j: int, couleur_contour: int) -> bool:
        """Verifier si un pixel est dans une zone fermee (pas de chemin vers l'exterieur)"""
        hauteur, largeur = len(grid), len(grid[0])
        visite = set()
        queue = deque([(start_i, start_j)])
        peut_atteindre_exterieur = False
        
        while queue:
            i, j = queue.popleft()
            
            # Si on atteint une bordure de la grille, la zone n'est pas fermee
            if i < 0 or i >= hauteur or j < 0 or j >= largeur:
                peut_atteindre_exterieur = True
                break
            
            # Si on a deja visite ce pixel
            if (i, j) in visite:
                continue
            
            visite.add((i, j))
            
            # Si c'est un contour, on ne peut pas passer
            if grid[i][j] == couleur_contour:
                continue
            
            # Si c'est vide, on peut continuer l'exploration
            if grid[i][j] == 0:
                # Explorer dans toutes les directions
                for di, dj in self.directions:
                    ni, nj = i + di, j + dj
                    if (ni, nj) not in visite:
                        queue.append((ni, nj))
        
        # Une zone est fermee si on ne peut pas atteindre l'exterieur
        return not peut_atteindre_exterieur

class SolveurZonesV11Simple:
    """Solveur simplifie avec detection de remplissage de zones"""
    
    def __init__(self):
        self.zone_analyzer = ZoneAnalyzer()
    
    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Resoudre une tache avec detection de zones"""
        print(f"SOLVEUR V11 SIMPLE - Analyse de zones de la tache {tache.tache_id}")
        
        # 1. Analyser les exemples pour detecter le pattern
        pattern_info = self._detecter_pattern_depuis_exemples(tache)
        
        if pattern_info['detecte']:
            print(f"   Pattern detecte: remplissage de zones avec contour {pattern_info['couleur_contour']} -> remplissage {pattern_info['couleur_remplissage']}")
            
            # 2. Appliquer le pattern au test input
            test_input = tache.test[0]['input']
            zones_fermees = self.zone_analyzer.detecter_zones_fermees(test_input, pattern_info['couleur_contour'])
            
            # 3. Appliquer le remplissage
            output = [ligne[:] for ligne in test_input]  # Copie
            for i, j in zones_fermees:
                output[i][j] = pattern_info['couleur_remplissage']
            
            # 4. Validation croisee
            validation = self._valider_solution_croisee(tache, output, pattern_info)
            
            return {
                'solution': output,
                'confiance': 0.9,
                'methode': 'remplissage_zones_simple',
                'validation': validation,
                'pattern_info': pattern_info,
                'zones_fermees': list(zones_fermees)
            }
        else:
            print("   Aucun pattern de remplissage de zones detecte")
            return {
                'solution': tache.test[0]['input'],
                'confiance': 0.1,
                'methode': 'fallback',
                'validation': {'valide': False, 'erreurs': 1, 'total_tests': 1, 'taux_erreur': 1.0},
                'pattern_info': pattern_info
            }
    
    def _detecter_pattern_depuis_exemples(self, tache: TacheARC) -> Dict[str, Any]:
        """Detecter le pattern de remplissage de zones depuis les exemples"""
        
        # Analyser le premier exemple pour detecter le pattern
        exemple = tache.train[0]
        input_grid = exemple['input']
        output_grid = exemple['output']
        
        # Chercher les changements de 0 vers une autre couleur
        changements = {}
        hauteur, largeur = len(input_grid), len(input_grid[0])
        
        for i in range(hauteur):
            for j in range(largeur):
                if i < len(output_grid) and j < len(output_grid[0]):
                    if input_grid[i][j] == 0 and output_grid[i][j] != 0:
                        couleur_output = output_grid[i][j]
                        if couleur_output not in changements:
                            changements[couleur_output] = []
                        changements[couleur_output].append((i, j))
        
        # Si on a des changements, essayer de detecter le pattern
        for couleur_remplissage, pixels in changements.items():
            # Chercher la couleur de contour
            for couleur_contour in set(pixel for ligne in input_grid for pixel in ligne if pixel != 0):
                # Detector les zones fermees
                zones_fermees = self.zone_analyzer.detecter_zones_fermees(input_grid, couleur_contour)
                
                # Verifier si les changements correspondent aux zones fermees
                pixels_set = set(pixels)
                if pixels_set.issubset(zones_fermees):
                    return {
                        'detecte': True,
                        'couleur_contour': couleur_contour,
                        'couleur_remplissage': couleur_remplissage,
                        'zones_fermees': list(zones_fermees),
                        'changements_reels': list(pixels_set)
                    }
        
        return {'detecte': False}
    
    def _valider_solution_croisee(self, tache: TacheARC, solution: List[List[int]], 
                                pattern_info: Dict) -> Dict[str, Any]:
        """Validation croisee complete"""
        erreurs = 0
        total_tests = 0
        
        for exemple in tache.train:
            input_exemple = exemple['input']
            output_attendu = exemple['output']
            
            try:
                # Appliquer le meme pattern sur l'exemple
                zones_fermees = self.zone_analyzer.detecter_zones_fermees(input_exemple, pattern_info['couleur_contour'])
                output_calcule = [ligne[:] for ligne in input_exemple]
                for i, j in zones_fermees:
                    output_calcule[i][j] = pattern_info['couleur_remplissage']
                
                if output_calcule != output_attendu:
                    erreurs += 1
                    print(f"     ERREUR: Input {input_exemple} -> Attendu {output_attendu}, Calculé {output_calcule}")
                else:
                    print(f"     SUCCES: Input {input_exemple} -> Correct!")
                
            except Exception as e:
                erreurs += 1
                print(f"     ERREUR: Exception: {e}")
            
            total_tests += 1
        
        valide = erreurs == 0
        taux_erreur = erreurs / total_tests if total_tests > 0 else 1.0
        
        return {
            'valide': valide,
            'erreurs': erreurs,
            'total_tests': total_tests,
            'taux_erreur': taux_erreur,
            'approche': 'remplissage_zones_simple'
        }

def main():
    """Test du solveur zones V11 simple"""
    print("SOLVEUR ARC ZONES V11 SIMPLE - Refuge ARC-AGI")
    
    # Test sur 00d62c1b
    with open('ARC-AGI-2-main/data/training/00d62c1b.json', 'r') as f:
        data = json.load(f)
    
    tache = TacheARC('00d62c1b', data['train'], data['test'])
    solveur = SolveurZonesV11Simple()
    
    resultat = solveur.resoudre_tache(tache)
    
    print(f"\nRESULTAT:")
    print(f"   Solution: {resultat['solution']}")
    print(f"   Confiance: {resultat['confiance']:.2f}")
    print(f"   Methode: {resultat['methode']}")
    print(f"   Validation: {resultat['validation']}")

if __name__ == "__main__":
    main()
