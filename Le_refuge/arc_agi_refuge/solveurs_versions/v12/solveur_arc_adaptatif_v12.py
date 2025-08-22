#!/usr/bin/env python3
"""
SOLVEUR ARC ADAPTATIF V12 - Refuge ARC-AGI
Solveur qui apprend de ses erreurs et détecte les paramètres manquants
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

@dataclass
class ParametreZone:
    """Paramètres d'une zone pour déterminer la couleur de remplissage"""
    aire: int
    perimetre: int
    largeur: int
    hauteur: int
    position_relative_i: float
    position_relative_j: float
    forme_complexite: float  # Ratio aire/perimètre

class ZoneAnalyzerAvance:
    """Analyseur de zones avancé avec détection de paramètres"""

    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def detecter_zones_fermees(self, grid: List[List[int]], couleur_contour: int) -> Set[Tuple[int, int]]:
        """Detecter les zones fermees"""
        hauteur, largeur = len(grid), len(grid[0])
        zones_fermees = set()

        for i in range(hauteur):
            for j in range(largeur):
                if grid[i][j] == 0:
                    if self._est_zone_fermee(grid, i, j, couleur_contour):
                        zones_fermees.add((i, j))

        return zones_fermees

    def _est_zone_fermee(self, grid: List[List[int]], start_i: int, start_j: int, couleur_contour: int) -> bool:
        """Verifier si un pixel est dans une zone fermee"""
        hauteur, largeur = len(grid), len(grid[0])
        visite = set()
        queue = deque([(start_i, start_j)])
        peut_atteindre_exterieur = False

        while queue:
            i, j = queue.popleft()

            if i < 0 or i >= hauteur or j < 0 or j >= largeur:
                peut_atteindre_exterieur = True
                break

            if (i, j) in visite:
                continue

            visite.add((i, j))

            if grid[i][j] == couleur_contour:
                continue

            if grid[i][j] == 0:
                for di, dj in self.directions:
                    ni, nj = i + di, j + dj
                    if (ni, nj) not in visite:
                        queue.append((ni, nj))

        return not peut_atteindre_exterieur

    def analyser_parametres_zone(self, grid: List[List[int]], zone_pixels: Set[Tuple[int, int]], couleur_contour: int) -> ParametreZone:
        """Analyser les paramètres d'une zone pour déterminer la couleur de remplissage"""
        if not zone_pixels:
            return ParametreZone(0, 0, 0, 0, 0.0, 0.0, 0.0)

        hauteur, largeur = len(grid), len(grid[0])
        
        # Calculer les bords de la zone
        min_i = min(i for i, j in zone_pixels)
        max_i = max(i for i, j in zone_pixels)
        min_j = min(j for i, j in zone_pixels)
        max_j = max(j for i, j in zone_pixels)

        # Dimensions
        zone_largeur = max_j - min_j + 1
        zone_hauteur = max_i - min_i + 1
        aire = len(zone_pixels)

        # Calculer le périmètre (pixels de contour)
        perimetre = 0
        for i, j in zone_pixels:
            for di, dj in self.directions:
                ni, nj = i + di, j + dj
                if (ni, nj) not in zone_pixels and 0 <= ni < hauteur and 0 <= nj < largeur:
                    if grid[ni][nj] == couleur_contour:
                        perimetre += 1

        # Position relative
        pos_relative_i = (min_i + max_i) / 2 / hauteur
        pos_relative_j = (min_j + max_j) / 2 / largeur

        # Complexité de forme (ratio aire/périmètre)
        forme_complexite = aire / perimetre if perimetre > 0 else 0

        return ParametreZone(
            aire=aire,
            perimetre=perimetre,
            largeur=zone_largeur,
            hauteur=zone_hauteur,
            position_relative_i=pos_relative_i,
            position_relative_j=pos_relative_j,
            forme_complexite=forme_complexite
        )

class SolveurAdaptatifV12:
    """Solveur qui apprend de ses erreurs et détecte les paramètres manquants"""

    def __init__(self):
        self.zone_analyzer = ZoneAnalyzerAvance()
        self.regles_apprises = []

    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Resoudre une tache avec apprentissage adaptatif"""
        print(f"SOLVEUR V12 ADAPTATIF - Analyse de la tache {tache.tache_id}")

        # 1. Détecter le pattern de base
        pattern_base = self._detecter_pattern_base(tache)
        
        if not pattern_base['detecte']:
            return self._solution_fallback(tache)

        print(f"   Pattern de base detecte: {pattern_base['type']}")

        # 2. Tester la solution simple
        solution_simple = self._appliquer_solution_simple(tache, pattern_base)
        validation_simple = self._valider_solution_croisee(tache, solution_simple, pattern_base)

        if validation_simple['valide']:
            print("   ✅ Solution simple valide!")
            return {
                'solution': solution_simple,
                'confiance': 0.9,
                'methode': 'solution_simple',
                'validation': validation_simple,
                'pattern_info': pattern_base
            }

        # 3. La solution simple échoue - chercher les paramètres manquants
        print("   ❌ Solution simple echoue - recherche de parametres manquants...")
        
        parametres_manquants = self._detecter_parametres_manquants(tache, pattern_base, solution_simple)
        
        if parametres_manquants:
            print(f"   🔍 Parametres detectes: {parametres_manquants}")
            
            # 4. Appliquer la solution avec paramètres
            solution_avancee = self._appliquer_solution_avancee(tache, pattern_base, parametres_manquants)
            validation_avancee = self._valider_solution_croisee(tache, solution_avancee, pattern_base)
            
            if validation_avancee['valide']:
                print("   ✅ Solution avancee valide!")
                return {
                    'solution': solution_avancee,
                    'confiance': 0.95,
                    'methode': 'solution_avancee',
                    'validation': validation_avancee,
                    'pattern_info': pattern_base,
                    'parametres': parametres_manquants
                }

        # 5. Échec - retourner la meilleure solution trouvée
        print("   ⚠️  Impossible de trouver une solution valide")
        return {
            'solution': solution_simple,
            'confiance': 0.3,
            'methode': 'fallback_avance',
            'validation': validation_simple,
            'pattern_info': pattern_base
        }

    def _detecter_pattern_base(self, tache: TacheARC) -> Dict[str, Any]:
        """Détecter le pattern de base"""
        # Analyser le premier exemple
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

        # Détecter le pattern de remplissage de zones
        for couleur_contour in set(pixel for ligne in input_grid for pixel in ligne if pixel != 0):
            zones_fermees = self.zone_analyzer.detecter_zones_fermees(input_grid, couleur_contour)
            
            for couleur_remplissage, pixels in changements.items():
                pixels_set = set(pixels)
                if pixels_set.issubset(zones_fermees):
                    return {
                        'detecte': True,
                        'type': 'remplissage_zones',
                        'couleur_contour': couleur_contour,
                        'couleur_remplissage': couleur_remplissage,
                        'zones_fermees': list(zones_fermees),
                        'changements_reels': list(pixels_set)
                    }

        return {'detecte': False}

    def _appliquer_solution_simple(self, tache: TacheARC, pattern_base: Dict) -> List[List[int]]:
        """Appliquer la solution simple (couleur fixe)"""
        test_input = tache.test[0]['input']
        zones_fermees = self.zone_analyzer.detecter_zones_fermees(test_input, pattern_base['couleur_contour'])
        
        output = [ligne[:] for ligne in test_input]
        for i, j in zones_fermees:
            output[i][j] = pattern_base['couleur_remplissage']
        
        return output

    def _detecter_parametres_manquants(self, tache: TacheARC, pattern_base: Dict, solution_simple: List[List[int]]) -> Optional[Dict[str, Any]]:
        """Détecter les paramètres manquants en analysant les erreurs"""
        
        # Analyser chaque exemple pour comprendre les variations
        parametres_zones = []
        
        for exemple in tache.train:
            input_grid = exemple['input']
            output_grid = exemple['output']
            
            # Détecter les zones fermées
            zones_fermees = self.zone_analyzer.detecter_zones_fermees(input_grid, pattern_base['couleur_contour'])
            
            # Analyser les changements réels
            changements_reels = {}
            hauteur, largeur = len(input_grid), len(input_grid[0])
            
            for i in range(hauteur):
                for j in range(largeur):
                    if i < len(output_grid) and j < len(output_grid[0]):
                        if input_grid[i][j] == 0 and output_grid[i][j] != 0:
                            couleur_output = output_grid[i][j]
                            if couleur_output not in changements_reels:
                                changements_reels[couleur_output] = []
                            changements_reels[couleur_output].append((i, j))
            
            # Analyser les paramètres pour chaque couleur
            for couleur_remplissage, pixels in changements_reels.items():
                pixels_set = set(pixels)
                if pixels_set.issubset(zones_fermees):
                    # Analyser les paramètres de cette zone
                    parametres = self.zone_analyzer.analyser_parametres_zone(input_grid, pixels_set, pattern_base['couleur_contour'])
                    parametres_zones.append({
                        'couleur': couleur_remplissage,
                        'parametres': parametres,
                        'pixels': pixels_set
                    })
        
        # Chercher des corrélations entre paramètres et couleurs
        if len(parametres_zones) > 1:
            return self._analyser_correlations(parametres_zones)
        
        return None

    def _analyser_correlations(self, parametres_zones: List[Dict]) -> Dict[str, Any]:
        """Analyser les corrélations entre paramètres et couleurs"""
        
        # Grouper par couleur
        groupes_couleurs = {}
        for item in parametres_zones:
            couleur = item['couleur']
            if couleur not in groupes_couleurs:
                groupes_couleurs[couleur] = []
            groupes_couleurs[couleur].append(item['parametres'])
        
        # Analyser les patterns
        regles = {}
        
        for couleur, parametres_list in groupes_couleurs.items():
            if len(parametres_list) > 1:
                # Chercher des patterns dans les paramètres
                aires = [p.aire for p in parametres_list]
                largeurs = [p.largeur for p in parametres_list]
                hauteurs = [p.hauteur for p in parametres_list]
                
                # Si toutes les zones ont la même aire, c'est un pattern
                if len(set(aires)) == 1:
                    regles[couleur] = {'type': 'aire_fixe', 'valeur': aires[0]}
                elif len(set(largeurs)) == 1:
                    regles[couleur] = {'type': 'largeur_fixe', 'valeur': largeurs[0]}
                elif len(set(hauteurs)) == 1:
                    regles[couleur] = {'type': 'hauteur_fixe', 'valeur': hauteurs[0]}
                else:
                    # Pattern plus complexe - utiliser l'aire comme critère principal
                    aire_moyenne = sum(aires) / len(aires)
                    regles[couleur] = {'type': 'aire_moyenne', 'valeur': aire_moyenne}
            else:
                # Une seule occurrence - utiliser les paramètres directs
                p = parametres_list[0]
                regles[couleur] = {'type': 'parametres_directs', 'aire': p.aire, 'largeur': p.largeur, 'hauteur': p.hauteur}
        
        return {
            'type': 'correlation_parametres',
            'regles': regles,
            'parametres_zones': parametres_zones
        }

    def _appliquer_solution_avancee(self, tache: TacheARC, pattern_base: Dict, parametres_manquants: Dict) -> List[List[int]]:
        """Appliquer la solution avec paramètres avancés"""
        test_input = tache.test[0]['input']
        zones_fermees = self.zone_analyzer.detecter_zones_fermees(test_input, pattern_base['couleur_contour'])
        
        output = [ligne[:] for ligne in test_input]
        
        # Grouper les zones par paramètres
        zones_groupes = {}
        for i, j in zones_fermees:
            zone_pixels = self._trouver_zone_complete(test_input, i, j, pattern_base['couleur_contour'])
            parametres = self.zone_analyzer.analyser_parametres_zone(test_input, zone_pixels, pattern_base['couleur_contour'])
            
            # Déterminer la couleur selon les règles
            couleur = self._determiner_couleur_par_parametres(parametres, parametres_manquants['regles'])
            
            for zi, zj in zone_pixels:
                output[zi][zj] = couleur
        
        return output

    def _trouver_zone_complete(self, grid: List[List[int]], start_i: int, start_j: int, couleur_contour: int) -> Set[Tuple[int, int]]:
        """Trouver tous les pixels d'une zone connectée"""
        hauteur, largeur = len(grid), len(grid[0])
        zone = set()
        queue = deque([(start_i, start_j)])
        
        while queue:
            i, j = queue.popleft()
            
            if (i, j) in zone:
                continue
                
            zone.add((i, j))
            
            for di, dj in self.directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < hauteur and 0 <= nj < largeur and 
                    grid[ni][nj] == 0 and (ni, nj) not in zone):
                    queue.append((ni, nj))
        
        return zone

    def _determiner_couleur_par_parametres(self, parametres: ParametreZone, regles: Dict) -> int:
        """Déterminer la couleur selon les paramètres et règles"""
        
        for couleur, regle in regles.items():
            if regle['type'] == 'aire_fixe' and parametres.aire == regle['valeur']:
                return couleur
            elif regle['type'] == 'largeur_fixe' and parametres.largeur == regle['valeur']:
                return couleur
            elif regle['type'] == 'hauteur_fixe' and parametres.hauteur == regle['valeur']:
                return couleur
            elif regle['type'] == 'aire_moyenne':
                # Utiliser la couleur la plus proche en aire
                if abs(parametres.aire - regle['valeur']) < 5:  # Tolérance
                    return couleur
        
        # Fallback: utiliser la première couleur disponible
        return list(regles.keys())[0] if regles else 1

    def _valider_solution_croisee(self, tache: TacheARC, solution: List[List[int]], pattern_info: Dict) -> Dict[str, Any]:
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

            except Exception as e:
                erreurs += 1

            total_tests += 1

        valide = erreurs == 0
        taux_erreur = erreurs / total_tests if total_tests > 0 else 1.0

        return {
            'valide': valide,
            'erreurs': erreurs,
            'total_tests': total_tests,
            'taux_erreur': taux_erreur
        }

    def _solution_fallback(self, tache: TacheARC) -> Dict[str, Any]:
        """Solution de fallback"""
        return {
            'solution': tache.test[0]['input'],
            'confiance': 0.1,
            'methode': 'fallback',
            'validation': {'valide': False, 'erreurs': 1, 'total_tests': 1, 'taux_erreur': 1.0},
            'pattern_info': {'detecte': False}
        }

def main():
    """Test du solveur adaptatif V12"""
    print("SOLVEUR ARC ADAPTATIF V12 - Refuge ARC-AGI")

    # Test sur 00dbd492
    with open('ARC-AGI-2-main/data/training/00dbd492.json', 'r') as f:
        data = json.load(f)

    tache = TacheARC('00dbd492', data['train'], data['test'])
    solveur = SolveurAdaptatifV12()

    resultat = solveur.resoudre_tache(tache)

    print(f"\nRESULTAT:")
    print(f"   Solution: {resultat['solution']}")
    print(f"   Confiance: {resultat['confiance']:.2f}")
    print(f"   Methode: {resultat['methode']}")
    print(f"   Validation: {resultat['validation']}")
    
    if 'parametres' in resultat:
        print(f"   Parametres detectes: {resultat['parametres']}")

if __name__ == "__main__":
    main()
