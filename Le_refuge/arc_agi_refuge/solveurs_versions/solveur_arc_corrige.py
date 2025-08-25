#!/usr/bin/env python3
"""
SOLVEUR ARC CORRIGÉ - Refuge ARC-AGI
Version corrigée qui peut réellement résoudre les tâches ARC
en analysant les patterns entre input et output des exemples de training
"""

import json
import sys
import os
import time
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from collections import defaultdict, Counter
import math

# Ajouter src au path
sys.path.insert(0, 'src')

try:
    from pattern_detector import PatternDetector
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    sys.exit(1)

@dataclass
class TacheARC:
    """Représentation d'une tâche ARC"""
    tache_id: str
    train: List[Dict[str, Any]]
    test: List[Dict[str, Any]]
    conscience: float = 0.0

class SolveurARCCorrige:
    """🔧 Solveur ARC corrigé qui peut réellement résoudre les tâches"""
    
    def __init__(self):
        self.detecteur = PatternDetector()
        self.resultats = {'succes': 0, 'total': 0}
    
    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Résoudre une tâche ARC en analysant les patterns training"""
        print(f"🔧 RÉSOLUTION TÂCHE: {tache.tache_id}")
        
        if not tache.train:
            return {'solution': [[0]], 'confiance': 0.0, 'methode': 'aucun_exemple'}
        
        # Analyser tous les exemples de training
        patterns_par_exemple = []
        transformations_globales = {}
        
        for i, exemple in enumerate(tache.train):
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Analyser les patterns
            resultats = self.detecteur.analyser_patterns(input_grille, output_grille)
            patterns_par_exemple.append(resultats)
            
            # Analyser les transformations de valeurs
            transformations = self._analyser_transformations_valeurs(input_grille, output_grille)
            for val_in, val_out in transformations.items():
                if val_in not in transformations_globales:
                    transformations_globales[val_in] = []
                transformations_globales[val_in].append(val_out)
        
        # Déterminer la stratégie de résolution
        strategie = self._determiner_strategie(patterns_par_exemple, transformations_globales)
        
        # Générer la solution
        if tache.test:
            test_input = tache.test[0].get('input', [])
            solution = self._generer_solution(test_input, strategie, transformations_globales, patterns_par_exemple)
        else:
            # Si pas de test, utiliser le premier exemple de training
            premier_exemple = tache.train[0]
            test_input = premier_exemple.get('input', [])
            solution = self._generer_solution(test_input, strategie, transformations_globales, patterns_par_exemple)
        
        # Calculer la confiance
        confiance = self._calculer_confiance(patterns_par_exemple, strategie)
        
        return {
            'solution': solution,
            'confiance': confiance,
            'methode': strategie,
            'patterns_analyses': len(patterns_par_exemple),
            'transformations': transformations_globales
        }
    
    def _analyser_transformations_valeurs(self, input_grille: List[List[int]], 
                                        output_grille: List[List[int]]) -> Dict[int, int]:
        """Analyser les transformations de valeurs entre input et output"""
        transformations = {}
        
        # Analyser les positions correspondantes
        h_in, w_in = len(input_grille), len(input_grille[0]) if input_grille else 0
        h_out, w_out = len(output_grille), len(output_grille[0]) if output_grille else 0
        
        # Si les dimensions sont identiques, analyser position par position
        if h_in == h_out and w_in == w_out:
            for y in range(h_in):
                for x in range(w_in):
                    val_in = input_grille[y][x]
                    val_out = output_grille[y][x]
                    if val_in != val_out:
                        transformations[val_in] = val_out
        
        # Analyser les transformations globales (valeurs qui apparaissent dans input vs output)
        valeurs_input = set()
        valeurs_output = set()
        
        for ligne in input_grille:
            valeurs_input.update(ligne)
        for ligne in output_grille:
            valeurs_output.update(ligne)
        
        # Chercher des patterns de transformation
        if len(valeurs_input) == len(valeurs_output):
            # Mapping possible
            for val_in in valeurs_input:
                if val_in not in transformations:
                    # Chercher une valeur correspondante dans l'output
                    for val_out in valeurs_output:
                        if val_out not in transformations.values():
                            transformations[val_in] = val_out
                            break
        
        return transformations
    
    def _determiner_strategie(self, patterns_par_exemple: List[Dict], 
                            transformations_globales: Dict[int, List[int]]) -> str:
        """Déterminer la stratégie de résolution basée sur l'analyse"""
        
        # Analyser les patterns dominants
        types_patterns = []
        for patterns in patterns_par_exemple:
            if 'patterns' in patterns:
                for pattern in patterns['patterns']:
                    types_patterns.append(pattern.get('type', 'unknown'))
        
        # Compter les types de patterns
        compteur = Counter(types_patterns)
        
        # Déterminer la stratégie
        if compteur['reduction_dimensionnelle'] > 0:
            return 'reduction'
        elif compteur['expansion_dimensionnelle'] > 0:
            return 'expansion'
        elif compteur['symetrie'] > 0:
            return 'symetrie'
        elif compteur['rotation'] > 0:
            return 'rotation'
        elif transformations_globales:
            return 'transformation_valeurs'
        else:
            return 'copie'
    
    def _generer_solution(self, test_input: List[List[int]], strategie: str,
                         transformations_globales: Dict[int, List[int]], 
                         patterns_par_exemple: List[Dict]) -> List[List[int]]:
        """Générer une solution basée sur la stratégie"""
        
        if not test_input:
            return [[0]]
        
        if strategie == 'copie':
            return test_input
        
        elif strategie == 'transformation_valeurs':
            return self._appliquer_transformations(test_input, transformations_globales)
        
        elif strategie == 'reduction':
            return self._appliquer_reduction(test_input, patterns_par_exemple)
        
        elif strategie == 'expansion':
            return self._appliquer_expansion(test_input, patterns_par_exemple)
        
        elif strategie == 'symetrie':
            return self._appliquer_symetrie(test_input, patterns_par_exemple)
        
        elif strategie == 'rotation':
            return self._appliquer_rotation(test_input, patterns_par_exemple)
        
        else:
            return test_input
    
    def _appliquer_transformations(self, test_input: List[List[int]], 
                                 transformations_globales: Dict[int, List[int]]) -> List[List[int]]:
        """Appliquer les transformations de valeurs"""
        resultat = []
        
        for ligne in test_input:
            nouvelle_ligne = []
            for val in ligne:
                if val in transformations_globales:
                    # Prendre la transformation la plus fréquente
                    transformations = transformations_globales[val]
                    if transformations:
                        nouvelle_val = max(set(transformations), key=transformations.count)
                        nouvelle_ligne.append(nouvelle_val)
                    else:
                        nouvelle_ligne.append(val)
                else:
                    nouvelle_ligne.append(val)
            resultat.append(nouvelle_ligne)
        
        return resultat
    
    def _appliquer_reduction(self, test_input: List[List[int]], 
                           patterns_par_exemple: List[Dict]) -> List[List[int]]:
        """Appliquer une réduction dimensionnelle"""
        # Analyser les dimensions des exemples de training
        dimensions_output = []
        
        for patterns in patterns_par_exemple:
            if 'reduction_dimensionnelle' in str(patterns):
                # Chercher les dimensions dans les patterns
                for pattern in patterns.get('patterns', []):
                    if pattern.get('type') == 'reduction_dimensionnelle':
                        # Extraire les dimensions cibles
                        h_out = pattern.get('hauteur_output', len(test_input) // 2)
                        w_out = pattern.get('largeur_output', len(test_input[0]) // 2)
                        dimensions_output.append((h_out, w_out))
        
        if dimensions_output:
            # Prendre les dimensions moyennes
            h_avg = sum(d[0] for d in dimensions_output) // len(dimensions_output)
            w_avg = sum(d[1] for d in dimensions_output) // len(dimensions_output)
            
            return self._reduire_grille(test_input, h_avg, w_avg)
        
        return test_input
    
    def _appliquer_expansion(self, test_input: List[List[int]], 
                           patterns_par_exemple: List[Dict]) -> List[List[int]]:
        """Appliquer une expansion dimensionnelle"""
        # Analyser les dimensions des exemples de training
        dimensions_output = []
        
        for patterns in patterns_par_exemple:
            if 'expansion_dimensionnelle' in str(patterns):
                # Chercher les dimensions dans les patterns
                for pattern in patterns.get('patterns', []):
                    if pattern.get('type') == 'expansion_dimensionnelle':
                        # Extraire les dimensions cibles
                        h_out = pattern.get('hauteur_output', len(test_input) * 2)
                        w_out = pattern.get('largeur_output', len(test_input[0]) * 2)
                        dimensions_output.append((h_out, w_out))
        
        if dimensions_output:
            # Prendre les dimensions moyennes
            h_avg = sum(d[0] for d in dimensions_output) // len(dimensions_output)
            w_avg = sum(d[1] for d in dimensions_output) // len(dimensions_output)
            
            return self._expandre_grille(test_input, h_avg, w_avg)
        
        return test_input
    
    def _appliquer_symetrie(self, test_input: List[List[int]], 
                          patterns_par_exemple: List[Dict]) -> List[List[int]]:
        """Appliquer une symétrie"""
        # Analyser le type de symétrie dans les patterns
        for patterns in patterns_par_exemple:
            for pattern in patterns.get('patterns', []):
                if pattern.get('type') == 'symetrie':
                    type_symetrie = pattern.get('symetrie', 'horizontale')
                    
                    test_array = np.array(test_input)
                    
                    if type_symetrie == 'horizontale':
                        return np.flipud(test_array).tolist()
                    elif type_symetrie == 'verticale':
                        return np.fliplr(test_array).tolist()
                    elif type_symetrie == 'diagonale':
                        return np.fliplr(np.flipud(test_array)).tolist()
        
        return test_input
    
    def _appliquer_rotation(self, test_input: List[List[int]], 
                          patterns_par_exemple: List[Dict]) -> List[List[int]]:
        """Appliquer une rotation"""
        # Analyser le type de rotation dans les patterns
        for patterns in patterns_par_exemple:
            for pattern in patterns.get('patterns', []):
                if pattern.get('type') == 'rotation':
                    angle = pattern.get('angle', 90)
                    
                    test_array = np.array(test_input)
                    
                    if angle == 90:
                        return np.rot90(test_array, 1).tolist()
                    elif angle == 180:
                        return np.rot90(test_array, 2).tolist()
                    elif angle == 270:
                        return np.rot90(test_array, 3).tolist()
        
        return test_input
    
    def _reduire_grille(self, grille: List[List[int]], h_out: int, w_out: int) -> List[List[int]]:
        """Réduire une grille"""
        if not grille:
            return [[0]]
        
        h_in, w_in = len(grille), len(grille[0])
        
        # Réduction par échantillonnage
        resultat = []
        for y in range(h_out):
            ligne = []
            for x in range(w_out):
                y_in = int(y * h_in / h_out)
                x_in = int(x * w_in / w_out)
                ligne.append(grille[y_in][x_in])
            resultat.append(ligne)
        
        return resultat
    
    def _expandre_grille(self, grille: List[List[int]], h_out: int, w_out: int) -> List[List[int]]:
        """Expandre une grille"""
        if not grille:
            return [[0]]
        
        h_in, w_in = len(grille), len(grille[0])
        
        # Expansion par répétition
        resultat = []
        for y in range(h_out):
            ligne = []
            for x in range(w_out):
                y_in = y % h_in
                x_in = x % w_in
                ligne.append(grille[y_in][x_in])
            resultat.append(ligne)
        
        return resultat
    
    def _calculer_confiance(self, patterns_par_exemple: List[Dict], strategie: str) -> float:
        """Calculer la confiance de la solution"""
        if not patterns_par_exemple:
            return 0.0
        
        # Calculer la confiance moyenne des patterns
        confiances = []
        for patterns in patterns_par_exemple:
            if 'confiance' in patterns:
                confiances.append(patterns['confiance'])
        
        confiance_moyenne = sum(confiances) / len(confiances) if confiances else 0.0
        
        # Bonus pour la stratégie
        bonus_strategie = {
            'copie': 0.1,
            'transformation_valeurs': 0.3,
            'reduction': 0.4,
            'expansion': 0.4,
            'symetrie': 0.5,
            'rotation': 0.5
        }
        
        bonus = bonus_strategie.get(strategie, 0.0)
        
        return min(1.0, confiance_moyenne + bonus)

def main():
    """Test du solveur corrigé"""
    print("🔧 TEST DU SOLVEUR ARC CORRIGÉ")
    
    solver = SolveurARCCorrige()
    
    # Test avec une tâche simple
    tache_test = TacheARC(
        tache_id="test_simple",
        train=[
            {
                "input": [[1, 2], [3, 4]],
                "output": [[2, 1], [4, 3]]
            },
            {
                "input": [[5, 6], [7, 8]],
                "output": [[6, 5], [8, 7]]
            }
        ],
        test=[
            {
                "input": [[9, 0], [1, 2]],
                "output": None
            }
        ]
    )
    
    resultat = solver.resoudre_tache(tache_test)
    
    print(f"Solution: {resultat['solution']}")
    print(f"Confiance: {resultat['confiance']:.3f}")
    print(f"Méthode: {resultat['methode']}")

if __name__ == "__main__":
    main()
