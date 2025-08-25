#!/usr/bin/env python3
"""
SOLVEUR ARC MULTI-APPROCHES V9 - Refuge ARC-AGI
Solveur avec plusieurs approches pour patterns complexes
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

class SolveurMultiApprochesV9:
    """Solveur avec plusieurs approches pour patterns complexes"""
    
    def __init__(self):
        self.pattern_detector = PatternDetector() if PatternDetector else None
        self.approches = [
            'masque_deploiement',
            'tiling_repetitif', 
            'template_mapping',
            'pattern_geometrique',
            'fallback'
        ]
    
    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Resoudre une tache avec plusieurs approches"""
        print(f"SOLVEUR V9 - Analyse de la tache {tache.tache_id}")
        
        # 1. Analyser les patterns
        patterns = self._analyser_patterns_complets(tache)
        
        # 2. Essayer chaque approche
        meilleure_solution = None
        meilleure_confiance = 0.0
        approche_gagnante = None
        
        for approche in self.approches:
            print(f"   ESSAI APPROCHE: {approche}")
            
            try:
                solution = self._appliquer_approche(tache, approche, patterns)
                confiance = self._calculer_confiance_approche(solution, tache, approche)
                
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
            'patterns_detectes': patterns
        }
    
    def _analyser_patterns_complets(self, tache: TacheARC) -> Dict[str, Any]:
        """Analyser tous les patterns possibles"""
        patterns = {}
        
        # Analyser les dimensions
        input_exemple = tache.train[0]['input']
        output_exemple = tache.train[0]['output']
        
        h_in, w_in = len(input_exemple), len(input_exemple[0])
        h_out, w_out = len(output_exemple), len(output_exemple[0])
        
        patterns['dimensions'] = {
            'input': f"{h_in}x{w_in}",
            'output': f"{h_out}x{w_out}",
            'rapport': f"{h_out/h_in:.1f}x{w_out/w_in:.1f}"
        }
        
        # Detector si c'est un pattern de deploiement
        if h_out == h_in * 3 and w_out == w_in * 3:
            patterns['deploiement_3x3'] = True
            patterns['type_deploiement'] = self._detecter_type_deploiement(tache)
        
        return patterns
    
    def _detecter_type_deploiement(self, tache: TacheARC) -> str:
        """Detecter le type de deploiement"""
        for exemple in tache.train:
            input_grid = exemple['input']
            output_grid = exemple['output']
            
            # Verifier si c'est un masque de deploiement
            if self._est_masque_deploiement(input_grid, output_grid):
                return 'masque_deploiement'
            
            # Verifier si c'est un tiling simple
            if self._est_tiling_simple(input_grid, output_grid):
                return 'tiling_simple'
        
        return 'inconnu'
    
    def _est_masque_deploiement(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Verifier si c'est un pattern de masque de deploiement"""
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])
        
        if h_out != h_in * 3 or w_out != w_in * 3:
            return False
        
        # Verifier le pattern de masque
        for i in range(h_in):
            for j in range(w_in):
                # Position dans l'output
                out_i = i * 3
                out_j = j * 3
                
                if input_grid[i][j] == 0:  # Masque = 0 (non)
                    # Zone devrait etre vide
                    zone = [row[out_j:out_j+3] for row in output_grid[out_i:out_i+3]]
                    if not self._est_zone_vide(zone):
                        return False
                else:  # Masque = couleur (oui)
                    # Zone devrait contenir le pattern
                    zone = [row[out_j:out_j+3] for row in output_grid[out_i:out_i+3]]
                    if not self._correspond_au_pattern(zone, input_grid):
                        return False
        
        return True
    
    def _est_tiling_simple(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Verifier si c'est un tiling simple"""
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])
        
        if h_out != h_in * 3 or w_out != w_in * 3:
            return False
        
        # Verifier si l'output est juste une repetition 3x3 de l'input
        for i in range(3):
            for j in range(3):
                out_i = i * h_in
                out_j = j * w_in
                
                zone = [row[out_j:out_j+w_in] for row in output_grid[out_i:out_i+h_in]]
                if zone != input_grid:
                    return False
        
        return True
    
    def _est_zone_vide(self, zone: List[List[int]]) -> bool:
        """Verifier si une zone est vide (tous 0)"""
        return all(all(cell == 0 for cell in row) for row in zone)
    
    def _correspond_au_pattern(self, zone: List[List[int]], pattern: List[List[int]]) -> bool:
        """Verifier si une zone correspond au pattern"""
        return zone == pattern
    
    def _appliquer_approche(self, tache: TacheARC, approche: str, patterns: Dict) -> List[List[int]]:
        """Appliquer une approche specifique"""
        test_input = tache.test[0]['input']
        
        if approche == 'masque_deploiement':
            return self._appliquer_masque_deploiement(test_input, tache)
        elif approche == 'tiling_repetitif':
            return self._appliquer_tiling_repetitif(test_input, tache)
        elif approche == 'template_mapping':
            return self._appliquer_template_mapping(test_input, tache)
        elif approche == 'pattern_geometrique':
            return self._appliquer_pattern_geometrique(test_input, tache)
        else:
            return self._appliquer_fallback(test_input, tache)
    
    def _appliquer_masque_deploiement(self, test_input: List[List[int]], tache: TacheARC) -> List[List[int]]:
        """Appliquer l'approche masque de deploiement"""
        h_in, w_in = len(test_input), len(test_input[0])
        h_out, w_out = h_in * 3, w_in * 3
        
        # Creer la grille de sortie
        output = [[0 for _ in range(w_out)] for _ in range(h_out)]
        
        # Appliquer le masque
        for i in range(h_in):
            for j in range(w_in):
                out_i = i * 3
                out_j = j * 3
                
                if test_input[i][j] == 0:  # Masque = 0 (non)
                    # Laisser vide
                    continue
                else:  # Masque = couleur (oui)
                    # Copier le pattern complet
                    for di in range(h_in):
                        for dj in range(w_in):
                            if out_i + di < h_out and out_j + dj < w_out:
                                output[out_i + di][out_j + dj] = test_input[di][dj]
        
        return output
    
    def _appliquer_tiling_repetitif(self, test_input: List[List[int]], tache: TacheARC) -> List[List[int]]:
        """Appliquer l'approche tiling repetitif"""
        h_in, w_in = len(test_input), len(test_input[0])
        h_out, w_out = h_in * 3, w_in * 3
        
        # Creer la grille de sortie
        output = [[0 for _ in range(w_out)] for _ in range(h_out)]
        
        # Repeter le pattern 3x3
        for i in range(3):
            for j in range(3):
                out_i = i * h_in
                out_j = j * w_in
                
                for di in range(h_in):
                    for dj in range(w_in):
                        if out_i + di < h_out and out_j + dj < w_out:
                            output[out_i + di][out_j + dj] = test_input[di][dj]
        
        return output
    
    def _appliquer_template_mapping(self, test_input: List[List[int]], tache: TacheARC) -> List[List[int]]:
        """Appliquer l'approche template mapping (plus sophistiquee)"""
        # Analyser les exemples pour extraire le template
        template = self._extraire_template(tache)
        
        if template:
            return self._appliquer_template(test_input, template)
        else:
            return self._appliquer_masque_deploiement(test_input, tache)
    
    def _extraire_template(self, tache: TacheARC) -> Optional[Dict]:
        """Extraire le template des exemples"""
        if len(tache.train) < 2:
            return None
        
        # Analyser les patterns communs
        templates = []
        
        for exemple in tache.train:
            input_grid = exemple['input']
            output_grid = exemple['output']
            
            template = self._analyser_template_exemple(input_grid, output_grid)
            if template:
                templates.append(template)
        
        # Retourner le template le plus frequent
        if templates:
            return templates[0]  # Simplification
        
        return None
    
    def _analyser_template_exemple(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Optional[Dict]:
        """Analyser le template d'un exemple"""
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])
        
        if h_out != h_in * 3 or w_out != w_in * 3:
            return None
        
        template = {
            'masque': [[0 for _ in range(w_in)] for _ in range(h_in)],
            'pattern': input_grid
        }
        
        # Analyser le masque
        for i in range(h_in):
            for j in range(w_in):
                out_i = i * 3
                out_j = j * 3
                
                zone = [row[out_j:out_j+3] for row in output_grid[out_i:out_i+3]]
                
                if self._est_zone_vide(zone):
                    template['masque'][i][j] = 0
                else:
                    template['masque'][i][j] = 1
        
        return template
    
    def _appliquer_template(self, test_input: List[List[int]], template: Dict) -> List[List[int]]:
        """Appliquer un template"""
        h_in, w_in = len(test_input), len(test_input[0])
        h_out, w_out = h_in * 3, w_in * 3
        
        output = [[0 for _ in range(w_out)] for _ in range(h_out)]
        masque = template['masque']
        
        for i in range(h_in):
            for j in range(w_in):
                out_i = i * 3
                out_j = j * 3
                
                if masque[i][j] == 1:  # Appliquer le pattern
                    for di in range(h_in):
                        for dj in range(w_in):
                            if out_i + di < h_out and out_j + dj < w_out:
                                output[out_i + di][out_j + dj] = test_input[di][dj]
        
        return output
    
    def _appliquer_pattern_geometrique(self, test_input: List[List[int]], tache: TacheARC) -> List[List[int]]:
        """Appliquer l'approche pattern geometrique"""
        # Essayer des transformations geometriques
        transformations = [
            lambda x: x,  # Identite
            lambda x: np.flipud(x).tolist(),  # Vertical flip
            lambda x: np.fliplr(x).tolist(),  # Horizontal flip
            lambda x: np.rot90(x, 1).tolist(),  # Rotation 90
            lambda x: np.rot90(x, 2).tolist(),  # Rotation 180
            lambda x: np.rot90(x, 3).tolist(),  # Rotation 270
        ]
        
        for transform in transformations:
            try:
                transformed = transform(test_input)
                solution = self._appliquer_masque_deploiement(transformed, tache)
                
                # Valider rapidement
                if self._valider_solution_rapide(tache, solution):
                    return solution
                    
            except Exception:
                continue
        
        return self._appliquer_masque_deploiement(test_input, tache)
    
    def _valider_solution_rapide(self, tache: TacheARC, solution: List[List[int]]) -> bool:
        """Validation rapide de la solution"""
        try:
            for exemple in tache.train[:1]:  # Juste le premier exemple
                input_ex = exemple['input']
                output_ex = exemple['output']
                
                # Appliquer la meme logique sur l'input d'entrainement
                test_solution = self._appliquer_masque_deploiement(input_ex, tache)
                
                if test_solution == output_ex:
                    return True
                    
        except Exception:
            pass
        
        return False
    
    def _appliquer_fallback(self, test_input: List[List[int]], tache: TacheARC) -> List[List[int]]:
        """Fallback simple"""
        return test_input
    
    def _calculer_confiance_approche(self, solution: List[List[int]], tache: TacheARC, approche: str) -> float:
        """Calculer la confiance d'une approche"""
        base_confiance = 0.5
        
        # Bonus selon l'approche
        if approche == 'masque_deploiement':
            base_confiance += 0.3
        elif approche == 'template_mapping':
            base_confiance += 0.2
        elif approche == 'pattern_geometrique':
            base_confiance += 0.1
        
        # Validation croisee rapide
        if self._valider_solution_rapide(tache, solution):
            base_confiance += 0.2
        
        return min(1.0, base_confiance)
    
    def _valider_solution_croisee(self, tache: TacheARC, solution: List[List[int]], approche: str) -> Dict[str, Any]:
        """Validation croisee complete"""
        erreurs = 0
        total_tests = 0
        
        for exemple in tache.train:
            input_exemple = exemple['input']
            output_attendu = exemple['output']
            
            # Appliquer l'approche sur l'input d'entrainement
            try:
                if approche == 'masque_deploiement':
                    output_calcule = self._appliquer_masque_deploiement(input_exemple, tache)
                elif approche == 'tiling_repetitif':
                    output_calcule = self._appliquer_tiling_repetitif(input_exemple, tache)
                elif approche == 'template_mapping':
                    output_calcule = self._appliquer_template_mapping(input_exemple, tache)
                elif approche == 'pattern_geometrique':
                    output_calcule = self._appliquer_pattern_geometrique(input_exemple, tache)
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
    """Test du solveur multi-approches V9"""
    print("SOLVEUR ARC MULTI-APPROCHES V9 - Refuge ARC-AGI")
    
    # Test sur un exemple
    solveur = SolveurMultiApprochesV9()
    
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
