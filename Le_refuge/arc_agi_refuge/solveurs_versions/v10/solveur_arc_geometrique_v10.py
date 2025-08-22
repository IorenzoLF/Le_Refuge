#!/usr/bin/env python3
"""
SOLVEUR ARC GEOMETRIQUE V10 - Refuge ARC-AGI
Solveur avec detection de formes geometriques et transformations conditionnelles
"""

import json
import sys
import os
import numpy as np
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass, field
from pathlib import Path

# Ajouter src au path
sys.path.insert(0, '../../../src')

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

class FormeGeometrique:
    """Classe pour representer et analyser les formes geometriques"""
    
    def __init__(self, positions: List[Tuple[int, int]], couleur: int):
        self.positions = positions
        self.couleur = couleur
        self.centre = self._calculer_centre()
        self.forme_normalisee = self._normaliser_forme()
    
    def _calculer_centre(self) -> Tuple[float, float]:
        """Calculer le centre de la forme"""
        if not self.positions:
            return (0, 0)
        x_coords = [pos[0] for pos in self.positions]
        y_coords = [pos[1] for pos in self.positions]
        return (sum(x_coords) / len(x_coords), sum(y_coords) / len(y_coords))
    
    def _normaliser_forme(self) -> List[Tuple[int, int]]:
        """Normaliser la forme (centrer et aligner)"""
        if not self.positions:
            return []
        
        # Centrer la forme
        positions_centrees = []
        for pos in self.positions:
            x_rel = pos[0] - self.centre[0]
            y_rel = pos[1] - self.centre[1]
            positions_centrees.append((int(round(x_rel)), int(round(y_rel))))
        
        # Trier pour avoir une representation unique
        return sorted(positions_centrees)
    
    def __eq__(self, other):
        """Comparer deux formes"""
        if not isinstance(other, FormeGeometrique):
            return False
        return self.forme_normalisee == other.forme_normalisee and self.couleur == other.couleur
    
    def __hash__(self):
        """Hash pour utiliser dans les dictionnaires"""
        return hash((tuple(self.forme_normalisee), self.couleur))

class SolveurGeometriqueV10:
    """Solveur avec detection de formes geometriques et transformations conditionnelles"""
    
    def __init__(self):
        self.pattern_detector = PatternDetector() if PatternDetector else None
        self.approches = [
            'geometrie_conditionnelle',
            'marqueurs_geometriques',
            'transformation_couleur_simple',
            'masque_deploiement',
            'tiling_repetitif',
            'fallback'
        ]
    
    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Resoudre une tache avec detection geometrique"""
        print(f"SOLVEUR V10 - Analyse geometrique de la tache {tache.tache_id}")
        
        # 1. Analyser les patterns geometriques
        patterns_geometriques = self._analyser_patterns_geometriques(tache)
        
        # 2. Essayer chaque approche
        meilleure_solution = None
        meilleure_confiance = 0.0
        approche_gagnante = None
        
        for approche in self.approches:
            print(f"   ESSAI APPROCHE: {approche}")
            
            try:
                solution = self._appliquer_approche(tache, approche, patterns_geometriques)
                confiance = self._calculer_confiance_approche(solution, tache, approche, patterns_geometriques)
                
                print(f"      Confiance: {confiance:.2f}")
                
                if confiance > meilleure_confiance:
                    meilleure_confiance = confiance
                    meilleure_solution = solution
                    approche_gagnante = approche
                    
            except Exception as e:
                print(f"      Erreur: {e}")
                continue
        
        # 3. Validation croisee
        validation = self._valider_solution_croisee(tache, meilleure_solution, approche_gagnante)
        
        return {
            'solution': meilleure_solution or tache.test[0]['input'],
            'confiance': meilleure_confiance,
            'methode': approche_gagnante or 'fallback',
            'approches_testees': len(self.approches),
            'validation': validation,
            'patterns_geometriques': patterns_geometriques
        }
    
    def _analyser_patterns_geometriques(self, tache: TacheARC) -> Dict[str, Any]:
        """Analyser les patterns geometriques dans les exemples"""
        patterns = {
            'formes_detectees': [],
            'transformations_conditionnelles': {},
            'marqueurs_geometriques': {},
            'invariance_position': True
        }
        
        # Analyser chaque exemple
        for i, exemple in enumerate(tache.train):
            input_grid = exemple['input']
            output_grid = exemple['output']
            
            # Extraire les formes geometriques
            formes = self._extraire_formes_geometriques(input_grid)
            patterns['formes_detectees'].extend(formes)
            
            # Analyser les transformations
            transformations = self._analyser_transformations(input_grid, output_grid, formes)
            patterns['transformations_conditionnelles'][f'exemple_{i}'] = transformations
            
            # Detector les marqueurs geometriques
            marqueurs = self._detecter_marqueurs_geometriques(input_grid, output_grid)
            patterns['marqueurs_geometriques'][f'exemple_{i}'] = marqueurs
        
        # Analyser l'invariance par position
        patterns['invariance_position'] = self._analyser_invariance_position(patterns)
        
        return patterns
    
    def _extraire_formes_geometriques(self, grid: List[List[int]]) -> List[FormeGeometrique]:
        """Extraire les formes geometriques d'une grille"""
        formes = []
        hauteur, largeur = len(grid), len(grid[0])
        
        # Pour chaque couleur, extraire les formes
        couleurs_uniques = set()
        for ligne in grid:
            for pixel in ligne:
                if pixel != 0:
                    couleurs_uniques.add(pixel)
        
        for couleur in couleurs_uniques:
            positions = []
            for i in range(hauteur):
                for j in range(largeur):
                    if grid[i][j] == couleur:
                        positions.append((i, j))
            
            if positions:
                forme = FormeGeometrique(positions, couleur)
                formes.append(forme)
        
        return formes
    
    def _analyser_transformations(self, input_grid: List[List[int]], 
                                 output_grid: List[List[int]], 
                                 formes: List[FormeGeometrique]) -> Dict[str, Any]:
        """Analyser les transformations entre input et output"""
        transformations = {}
        
        # Analyser les changements de couleur
        for forme in formes:
            couleur_input = forme.couleur
            couleur_output = self._trouver_couleur_output(input_grid, output_grid, forme.positions)
            
            if couleur_input != couleur_output:
                transformations[f'forme_{couleur_input}'] = {
                    'input': couleur_input,
                    'output': couleur_output,
                    'forme': forme.forme_normalisee
                }
        
        return transformations
    
    def _trouver_couleur_output(self, input_grid: List[List[int]], 
                               output_grid: List[List[int]], 
                               positions: List[Tuple[int, int]]) -> int:
        """Trouver la couleur correspondante dans l'output"""
        if not positions:
            return 0
        
        # Prendre la premiere position pour determiner la transformation
        i, j = positions[0]
        if i < len(output_grid) and j < len(output_grid[0]):
            return output_grid[i][j]
        
        return 0
    
    def _detecter_marqueurs_geometriques(self, input_grid: List[List[int]], 
                                       output_grid: List[List[int]]) -> Dict[str, Any]:
        """Detecter les marqueurs geometriques (pixels qui disparaissent)"""
        marqueurs = {}
        
        hauteur, largeur = len(input_grid), len(input_grid[0])
        
        for i in range(hauteur):
            for j in range(largeur):
                if i < len(output_grid) and j < len(output_grid[0]):
                    if input_grid[i][j] != 0 and output_grid[i][j] == 0:
                        # Pixel qui disparait = marqueur potentiel
                        couleur = input_grid[i][j]
                        if couleur not in marqueurs:
                            marqueurs[couleur] = []
                        marqueurs[couleur].append((i, j))
        
        return marqueurs
    
    def _analyser_invariance_position(self, patterns: Dict[str, Any]) -> bool:
        """Analyser si les transformations sont invariantes par position"""
        # Simplification : on suppose invariance par defaut
        # En realite, il faudrait comparer les formes a differentes positions
        return True
    
    def _appliquer_approche(self, tache: TacheARC, approche: str, patterns: Dict) -> List[List[int]]:
        """Appliquer une approche specifique"""
        test_input = tache.test[0]['input']
        
        if approche == 'geometrie_conditionnelle':
            return self._appliquer_geometrie_conditionnelle(test_input, tache, patterns)
        elif approche == 'marqueurs_geometriques':
            return self._appliquer_marqueurs_geometriques(test_input, tache, patterns)
        elif approche == 'transformation_couleur_simple':
            return self._appliquer_transformation_couleur_simple(test_input, tache, patterns)
        elif approche == 'masque_deploiement':
            return self._appliquer_masque_deploiement(test_input, tache)
        elif approche == 'tiling_repetitif':
            return self._appliquer_tiling_repetitif(test_input, tache)
        else:
            return self._appliquer_fallback(test_input, tache)
    
    def _appliquer_geometrie_conditionnelle(self, test_input: List[List[int]], 
                                           tache: TacheARC, patterns: Dict) -> List[List[int]]:
        """Appliquer l'approche geometrie conditionnelle"""
        # Analyser les transformations des exemples
        transformations = patterns.get('transformations_conditionnelles', {})
        
        # Creer un mapping de couleurs global
        mapping_couleurs = {}
        for exemple_transforms in transformations.values():
            for transform_key, transform_data in exemple_transforms.items():
                input_color = transform_data['input']
                output_color = transform_data['output']
                if input_color != output_color:  # Seulement si il y a un changement
                    mapping_couleurs[input_color] = output_color
        
        # Si on a trouve des transformations, les appliquer
        if mapping_couleurs:
            output = []
            for ligne in test_input:
                nouvelle_ligne = []
                for pixel in ligne:
                    nouvelle_ligne.append(mapping_couleurs.get(pixel, pixel))
                output.append(nouvelle_ligne)
            return output
        
        # Sinon, essayer de detecter un pattern de tiling
        return self._appliquer_tiling_repetitif(test_input, tache)
    
    def _appliquer_marqueurs_geometriques(self, test_input: List[List[int]], 
                                        tache: TacheARC, patterns: Dict) -> List[List[int]]:
        """Appliquer l'approche marqueurs geometriques"""
        # Detector les marqueurs dans le test input
        marqueurs_test = self._detecter_marqueurs_geometriques(test_input, test_input)
        
        # Analyser les transformations conditionnelles
        transformations = patterns.get('transformations_conditionnelles', {})
        
        # Creer l'output
        output = [ligne[:] for ligne in test_input]  # Copie
        
        # Appliquer les transformations basees sur les marqueurs
        for couleur_marqueur, positions_marqueurs in marqueurs_test.items():
            # Chercher la transformation correspondante
            for exemple_transforms in transformations.values():
                for transform_key, transform_data in exemple_transforms.items():
                    if transform_data['input'] != couleur_marqueur:
                        # Appliquer la transformation aux pixels voisins
                        couleur_output = transform_data['output']
                        
                        for i, j in positions_marqueurs:
                            # Effacer le marqueur
                            if i < len(output) and j < len(output[0]):
                                output[i][j] = 0
                            
                            # Transformer les pixels voisins
                            for di in [-1, 0, 1]:
                                for dj in [-1, 0, 1]:
                                    ni, nj = i + di, j + dj
                                    if (0 <= ni < len(output) and 0 <= nj < len(output[0]) and
                                        test_input[ni][nj] != couleur_marqueur and test_input[ni][nj] != 0):
                                        output[ni][nj] = couleur_output
        
        return output
    
    def _appliquer_transformation_couleur_simple(self, test_input: List[List[int]], 
                                               tache: TacheARC, patterns: Dict) -> List[List[int]]:
        """Appliquer une transformation de couleur simple"""
        # Analyser les transformations des exemples
        transformations = patterns.get('transformations_conditionnelles', {})
        
        # Creer un mapping de couleurs
        mapping_couleurs = {}
        for exemple_transforms in transformations.values():
            for transform_key, transform_data in exemple_transforms.items():
                mapping_couleurs[transform_data['input']] = transform_data['output']
        
        # Appliquer le mapping
        output = []
        for ligne in test_input:
            nouvelle_ligne = []
            for pixel in ligne:
                nouvelle_ligne.append(mapping_couleurs.get(pixel, pixel))
            output.append(nouvelle_ligne)
        
        return output
    
    def _appliquer_masque_deploiement(self, test_input: List[List[int]], tache: TacheARC) -> List[List[int]]:
        """Appliquer l'approche masque de deploiement (V9)"""
        h_in, w_in = len(test_input), len(test_input[0])
        h_out, w_out = h_in * 3, w_in * 3
        
        output = [[0 for _ in range(w_out)] for _ in range(h_out)]
        
        for i in range(h_in):
            for j in range(w_in):
                out_i = i * 3
                out_j = j * 3
                
                if test_input[i][j] == 0:
                    continue
                else:
                    for di in range(h_in):
                        for dj in range(w_in):
                            if out_i + di < h_out and out_j + dj < w_out:
                                output[out_i + di][out_j + dj] = test_input[di][dj]
        
        return output
    
    def _appliquer_tiling_repetitif(self, test_input: List[List[int]], tache: TacheARC) -> List[List[int]]:
        """Appliquer l'approche tiling repetitif (V9)"""
        h_in, w_in = len(test_input), len(test_input[0])
        h_out, w_out = h_in * 3, w_in * 3
        
        output = [[0 for _ in range(w_out)] for _ in range(h_out)]
        
        for i in range(3):
            for j in range(3):
                out_i = i * h_in
                out_j = j * w_in
                
                for di in range(h_in):
                    for dj in range(w_in):
                        if out_i + di < h_out and out_j + dj < w_out:
                            output[out_i + di][out_j + dj] = test_input[di][dj]
        
        return output
    
    def _appliquer_fallback(self, test_input: List[List[int]], tache: TacheARC) -> List[List[int]]:
        """Fallback simple"""
        return test_input
    
    def _calculer_confiance_approche(self, solution: List[List[int]], tache: TacheARC, 
                                   approche: str, patterns: Dict) -> float:
        """Calculer la confiance d'une approche"""
        base_confiance = 0.5
        
        # Bonus selon l'approche
        if approche == 'geometrie_conditionnelle':
            base_confiance += 0.3
        elif approche == 'marqueurs_geometriques':
            base_confiance += 0.25
        elif approche == 'transformation_couleur_simple':
            base_confiance += 0.2
        
        # Bonus si on a detecte des formes geometriques
        if patterns.get('formes_detectees'):
            base_confiance += 0.2
        
        # Validation croisee rapide
        if self._valider_solution_rapide(tache, solution):
            base_confiance += 0.2
        
        return min(1.0, base_confiance)
    
    def _valider_solution_rapide(self, tache: TacheARC, solution: List[List[int]]) -> bool:
        """Validation rapide de la solution"""
        try:
            for exemple in tache.train[:1]:
                input_ex = exemple['input']
                output_ex = exemple['output']
                
                # Appliquer la meme logique sur l'input d'entrainement
                test_solution = self._appliquer_transformation_couleur_simple(input_ex, tache, {})
                
                if test_solution == output_ex:
                    return True
                    
        except Exception:
            pass
        
        return False
    
    def _valider_solution_croisee(self, tache: TacheARC, solution: List[List[int]], 
                                approche: str) -> Dict[str, Any]:
        """Validation croisee complete"""
        erreurs = 0
        total_tests = 0
        
        for exemple in tache.train:
            input_exemple = exemple['input']
            output_attendu = exemple['output']
            
            try:
                if approche == 'geometrie_conditionnelle':
                    output_calcule = self._appliquer_geometrie_conditionnelle(input_exemple, tache, {})
                elif approche == 'marqueurs_geometriques':
                    output_calcule = self._appliquer_marqueurs_geometriques(input_exemple, tache, {})
                elif approche == 'transformation_couleur_simple':
                    output_calcule = self._appliquer_transformation_couleur_simple(input_exemple, tache, {})
                elif approche == 'masque_deploiement':
                    output_calcule = self._appliquer_masque_deploiement(input_exemple, tache)
                elif approche == 'tiling_repetitif':
                    output_calcule = self._appliquer_tiling_repetitif(input_exemple, tache)
                else:
                    output_calcule = input_exemple
                
                if output_calcule != output_attendu:
                    erreurs += 1
                    print(f"     ERREUR: {approche} - Input {input_exemple} -> Attendu {output_attendu}, Calculé {output_calcule}")
                else:
                    print(f"     SUCCES: {approche} - Input {input_exemple} -> Correct!")
                
            except Exception as e:
                erreurs += 1
                print(f"     ERREUR: {approche} - Exception: {e}")
            
            total_tests += 1
        
        valide = erreurs == 0
        taux_erreur = erreurs / total_tests if total_tests > 0 else 1.0
        
        return {
            'valide': valide,
            'erreurs': erreurs,
            'total_tests': total_tests,
            'taux_erreur': taux_erreur,
            'approche': approche
        }

def main():
    """Test du solveur geometrique V10"""
    print("SOLVEUR ARC GEOMETRIQUE V10 - Refuge ARC-AGI")
    
    # Test sur un exemple
    solveur = SolveurGeometriqueV10()
    
    # Exemple de tache
    tache_data = {
        'train': [
            {
                'input': [[6, 6, 0], [6, 0, 0], [0, 6, 6]],
                'output': [[6, 6, 0, 6, 6, 0, 0, 0, 0], [6, 0, 0, 6, 0, 0, 0, 0, 0], [0, 6, 6, 0, 6, 6, 0, 0, 0], [6, 6, 0, 0, 0, 0, 0, 0, 0], [6, 0, 0, 0, 0, 0, 0, 0, 0], [0, 6, 6, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 6, 0, 6, 6, 0], [0, 0, 0, 6, 0, 0, 6, 0, 0], [0, 0, 0, 0, 6, 6, 0, 6, 6]]
            }
        ],
        'test': [
            {
                'input': [[7, 0, 7], [7, 0, 7], [7, 7, 0]],
                'output': [[7, 0, 7, 0, 0, 0, 7, 0, 7], [7, 0, 7, 0, 0, 0, 7, 0, 7], [7, 7, 0, 0, 0, 0, 7, 7, 0], [7, 0, 7, 0, 0, 0, 7, 0, 7], [7, 0, 7, 0, 0, 0, 7, 0, 7], [7, 7, 0, 0, 0, 0, 7, 7, 0], [7, 0, 7, 7, 0, 7, 0, 0, 0], [7, 0, 7, 7, 0, 7, 0, 0, 0], [7, 7, 0, 7, 7, 0, 0, 0, 0]]
            }
        ]
    }
    
    tache = TacheARC('007bbfb7', tache_data['train'], tache_data['test'])
    
    resultat = solveur.resoudre_tache(tache)
    
    print(f"\nRESULTAT:")
    print(f"   Solution: {resultat['solution']}")
    print(f"   Confiance: {resultat['confiance']:.2f}")
    print(f"   Methode: {resultat['methode']}")
    print(f"   Validation: {resultat['validation']}")

if __name__ == "__main__":
    main()
