#!/usr/bin/env python3
"""
SOLVEUR ARC AMÉLIORÉ - Refuge ARC-AGI
Version améliorée basée sur l'analyse des erreurs réelles
- Analyse position par position des transformations
- Détection des patterns géométriques (symétrie, rotation)
- Compréhension des patterns de remplissage
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

class SolveurARCAmeliore:
    """🔧 Solveur ARC amélioré basé sur l'analyse des erreurs"""
    
    def __init__(self):
        self.detecteur = PatternDetector()
        self.resultats = {'succes': 0, 'total': 0}
    
    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Résoudre une tâche ARC avec analyse améliorée"""
        print(f"🔧 RÉSOLUTION TÂCHE AMÉLIORÉE: {tache.tache_id}")
        
        if not tache.train:
            return {'solution': [[0]], 'confiance': 0.0, 'methode': 'aucun_exemple'}
        
        # Analyser tous les exemples de training
        transformations_positionnelles = []
        patterns_geometriques = []
        
        for i, exemple in enumerate(tache.train):
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Analyser les transformations position par position
            transformations = self._analyser_transformations_positionnelles(input_grille, output_grille)
            transformations_positionnelles.append(transformations)
            
            # Analyser les patterns géométriques
            patterns_geo = self._analyser_patterns_geometriques(input_grille, output_grille)
            if patterns_geo:
                patterns_geometriques.append(patterns_geo)
        
        # Déterminer la stratégie de résolution
        strategie = self._determiner_strategie_amelioree(transformations_positionnelles, patterns_geometriques)
        
        # Générer la solution
        if tache.test:
            test_input = tache.test[0].get('input', [])
            solution = self._generer_solution_amelioree(test_input, strategie, transformations_positionnelles, patterns_geometriques)
        else:
            # Si pas de test, utiliser le premier exemple de training
            premier_exemple = tache.train[0]
            test_input = premier_exemple.get('input', [])
            solution = self._generer_solution_amelioree(test_input, strategie, transformations_positionnelles, patterns_geometriques)
        
        # Calculer la confiance
        confiance = self._calculer_confiance_amelioree(transformations_positionnelles, patterns_geometriques, strategie)
        
        return {
            'solution': solution,
            'confiance': confiance,
            'methode': strategie,
            'transformations_analysees': len(transformations_positionnelles),
            'patterns_geometriques': len(patterns_geometriques)
        }
    
    def _analyser_transformations_positionnelles(self, input_grille: List[List[int]], 
                                               output_grille: List[List[int]]) -> Dict[str, Any]:
        """Analyser les transformations position par position"""
        transformations = {}
        
        h_in, w_in = len(input_grille), len(input_grille[0]) if input_grille else 0
        h_out, w_out = len(output_grille), len(output_grille[0]) if output_grille else 0
        
        # Si les dimensions sont identiques, analyser position par position
        if h_in == h_out and w_in == w_out:
            for y in range(h_in):
                for x in range(w_in):
                    val_in = input_grille[y][x]
                    val_out = output_grille[y][x]
                    if val_in != val_out:
                        key = f"{y},{x}"
                        transformations[key] = {'input': val_in, 'output': val_out}
        
        # Analyser les patterns de transformation
        patterns_transformation = self._identifier_patterns_transformation(transformations)
        
        return {
            'transformations': transformations,
            'patterns': patterns_transformation,
            'dimensions': (h_in, w_in, h_out, w_out)
        }
    
    def _identifier_patterns_transformation(self, transformations: Dict[str, Dict]) -> Dict[str, Any]:
        """Identifier les patterns de transformation"""
        patterns = {}
        
        # Analyser les transformations par valeur d'entrée
        transformations_par_valeur = defaultdict(list)
        for pos, trans in transformations.items():
            val_in = trans['input']
            val_out = trans['output']
            transformations_par_valeur[val_in].append(val_out)
        
        # Identifier les patterns
        for val_in, val_outs in transformations_par_valeur.items():
            if len(set(val_outs)) == 1:
                # Transformation constante
                patterns[f'constante_{val_in}'] = val_outs[0]
            else:
                # Transformation variable
                patterns[f'variable_{val_in}'] = val_outs
        
        # Analyser les positions
        positions_par_valeur = defaultdict(list)
        for pos, trans in transformations.items():
            val_in = trans['input']
            positions_par_valeur[val_in].append(pos)
        
        patterns['positions'] = dict(positions_par_valeur)
        
        return patterns
    
    def _analyser_patterns_geometriques(self, input_grille: List[List[int]], 
                                      output_grille: List[List[int]]) -> Optional[Dict[str, Any]]:
        """Analyser les patterns géométriques"""
        h_in, w_in = len(input_grille), len(input_grille[0]) if input_grille else 0
        h_out, w_out = len(output_grille), len(output_grille[0]) if output_grille else 0
        
        # Vérifier les symétries
        symetries = self._detecter_symetries(input_grille, output_grille)
        
        # Vérifier les rotations
        rotations = self._detecter_rotations(input_grille, output_grille)
        
        # Vérifier les patterns de remplissage
        remplissage = self._detecter_patterns_remplissage(input_grille, output_grille)
        
        if symetries or rotations or remplissage:
            return {
                'symetries': symetries,
                'rotations': rotations,
                'remplissage': remplissage
            }
        
        return None
    
    def _detecter_symetries(self, input_grille: List[List[int]], 
                          output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter les symétries"""
        if len(input_grille) != len(output_grille) or len(input_grille[0]) != len(output_grille[0]):
            return {}
        
        input_array = np.array(input_grille)
        output_array = np.array(output_grille)
        
        symetries = {}
        
        # Symétrie horizontale
        if np.array_equal(np.flipud(input_array), output_array):
            symetries['horizontale'] = True
        
        # Symétrie verticale
        if np.array_equal(np.fliplr(input_array), output_array):
            symetries['verticale'] = True
        
        # Symétrie diagonale
        if np.array_equal(np.fliplr(np.flipud(input_array)), output_array):
            symetries['diagonale'] = True
        
        return symetries
    
    def _detecter_rotations(self, input_grille: List[List[int]], 
                          output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter les rotations"""
        if len(input_grille) != len(output_grille) or len(input_grille[0]) != len(output_grille[0]):
            return {}
        
        input_array = np.array(input_grille)
        output_array = np.array(output_grille)
        
        rotations = {}
        
        # Rotation 90°
        if np.array_equal(np.rot90(input_array, 1), output_array):
            rotations['90'] = True
        
        # Rotation 180°
        if np.array_equal(np.rot90(input_array, 2), output_array):
            rotations['180'] = True
        
        # Rotation 270°
        if np.array_equal(np.rot90(input_array, 3), output_array):
            rotations['270'] = True
        
        return rotations
    
    def _detecter_patterns_remplissage(self, input_grille: List[List[int]], 
                                     output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter les patterns de remplissage"""
        remplissage = {}
        
        # Analyser les valeurs qui apparaissent dans l'output mais pas dans l'input
        valeurs_input = set()
        valeurs_output = set()
        
        for ligne in input_grille:
            valeurs_input.update(ligne)
        for ligne in output_grille:
            valeurs_output.update(ligne)
        
        nouvelles_valeurs = valeurs_output - valeurs_input
        
        if nouvelles_valeurs:
            remplissage['nouvelles_valeurs'] = list(nouvelles_valeurs)
            
            # Analyser où ces nouvelles valeurs apparaissent
            positions_nouvelles = {}
            for y, ligne in enumerate(output_grille):
                for x, val in enumerate(ligne):
                    if val in nouvelles_valeurs:
                        if val not in positions_nouvelles:
                            positions_nouvelles[val] = []
                        positions_nouvelles[val].append((y, x))
            
            remplissage['positions_nouvelles'] = positions_nouvelles
        
        return remplissage
    
    def _determiner_strategie_amelioree(self, transformations_positionnelles: List[Dict], 
                                      patterns_geometriques: List[Dict]) -> str:
        """Déterminer la stratégie de résolution améliorée"""
        
        # Priorité aux patterns géométriques
        if patterns_geometriques:
            for pattern in patterns_geometriques:
                if pattern.get('symetries'):
                    return 'symetrie'
                if pattern.get('rotations'):
                    return 'rotation'
                if pattern.get('remplissage'):
                    return 'remplissage'
        
        # Analyser les transformations positionnelles
        if transformations_positionnelles:
            # Chercher des patterns de transformation
            for trans in transformations_positionnelles:
                patterns = trans.get('patterns', {})
                if any(key.startswith('constante_') for key in patterns):
                    return 'transformation_constante'
                if any(key.startswith('variable_') for key in patterns):
                    return 'transformation_variable'
        
        return 'copie'
    
    def _generer_solution_amelioree(self, test_input: List[List[int]], strategie: str,
                                  transformations_positionnelles: List[Dict], 
                                  patterns_geometriques: List[Dict]) -> List[List[int]]:
        """Générer une solution basée sur la stratégie améliorée"""
        
        if not test_input:
            return [[0]]
        
        if strategie == 'copie':
            return test_input
        
        elif strategie == 'symetrie':
            return self._appliquer_symetrie_amelioree(test_input, patterns_geometriques)
        
        elif strategie == 'rotation':
            return self._appliquer_rotation_amelioree(test_input, patterns_geometriques)
        
        elif strategie == 'remplissage':
            return self._appliquer_remplissage_amelioree(test_input, patterns_geometriques)
        
        elif strategie == 'transformation_constante':
            return self._appliquer_transformation_constante(test_input, transformations_positionnelles)
        
        elif strategie == 'transformation_variable':
            return self._appliquer_transformation_variable(test_input, transformations_positionnelles)
        
        else:
            return test_input
    
    def _appliquer_symetrie_amelioree(self, test_input: List[List[int]], 
                                    patterns_geometriques: List[Dict]) -> List[List[int]]:
        """Appliquer une symétrie améliorée"""
        for pattern in patterns_geometriques:
            symetries = pattern.get('symetries', {})
            
            test_array = np.array(test_input)
            
            if symetries.get('horizontale'):
                return np.flipud(test_array).tolist()
            elif symetries.get('verticale'):
                return np.fliplr(test_array).tolist()
            elif symetries.get('diagonale'):
                return np.fliplr(np.flipud(test_array)).tolist()
        
        return test_input
    
    def _appliquer_rotation_amelioree(self, test_input: List[List[int]], 
                                    patterns_geometriques: List[Dict]) -> List[List[int]]:
        """Appliquer une rotation améliorée"""
        for pattern in patterns_geometriques:
            rotations = pattern.get('rotations', {})
            
            test_array = np.array(test_input)
            
            if rotations.get('90'):
                return np.rot90(test_array, 1).tolist()
            elif rotations.get('180'):
                return np.rot90(test_array, 2).tolist()
            elif rotations.get('270'):
                return np.rot90(test_array, 3).tolist()
        
        return test_input
    
    def _appliquer_remplissage_amelioree(self, test_input: List[List[int]], 
                                       patterns_geometriques: List[Dict]) -> List[List[int]]:
        """Appliquer un remplissage amélioré"""
        for pattern in patterns_geometriques:
            remplissage = pattern.get('remplissage', {})
            
            if 'nouvelles_valeurs' in remplissage:
                nouvelles_valeurs = remplissage['nouvelles_valeurs']
                positions_nouvelles = remplissage.get('positions_nouvelles', {})
                
                # Créer une copie du test input
                resultat = [ligne[:] for ligne in test_input]
                
                # Appliquer les remplissages basés sur les patterns détectés
                for val, positions in positions_nouvelles.items():
                    # Analyser le pattern de remplissage
                    if len(positions) > 0:
                        # Remplir les positions correspondantes
                        for y, x in positions:
                            if y < len(resultat) and x < len(resultat[0]):
                                resultat[y][x] = val
                
                return resultat
        
        return test_input
    
    def _appliquer_transformation_constante(self, test_input: List[List[int]], 
                                          transformations_positionnelles: List[Dict]) -> List[List[int]]:
        """Appliquer une transformation constante"""
        resultat = [ligne[:] for ligne in test_input]
        
        for trans in transformations_positionnelles:
            patterns = trans.get('patterns', {})
            
            for key, value in patterns.items():
                if key.startswith('constante_'):
                    val_in = int(key.split('_')[1])
                    val_out = value
                    
                    # Appliquer la transformation
                    for y, ligne in enumerate(resultat):
                        for x, val in enumerate(ligne):
                            if val == val_in:
                                resultat[y][x] = val_out
        
        return resultat
    
    def _appliquer_transformation_variable(self, test_input: List[List[int]], 
                                         transformations_positionnelles: List[Dict]) -> List[List[int]]:
        """Appliquer une transformation variable"""
        resultat = [ligne[:] for ligne in test_input]
        
        for trans in transformations_positionnelles:
            patterns = trans.get('patterns', {})
            positions = patterns.get('positions', {})
            
            for val_in_str, pos_list in positions.items():
                val_in = int(val_in_str)
                val_outs = patterns.get(f'variable_{val_in}', [])
                
                if val_outs:
                    # Prendre la transformation la plus fréquente
                    val_out = max(set(val_outs), key=val_outs.count)
                    
                    # Appliquer la transformation
                    for y, ligne in enumerate(resultat):
                        for x, val in enumerate(ligne):
                            if val == val_in:
                                resultat[y][x] = val_out
        
        return resultat
    
    def _calculer_confiance_amelioree(self, transformations_positionnelles: List[Dict], 
                                    patterns_geometriques: List[Dict], strategie: str) -> float:
        """Calculer la confiance améliorée"""
        
        # Base de confiance
        confiance_base = 0.3
        
        # Bonus pour les transformations positionnelles
        if transformations_positionnelles:
            confiance_base += 0.2
        
        # Bonus pour les patterns géométriques
        if patterns_geometriques:
            confiance_base += 0.3
        
        # Bonus pour la stratégie
        bonus_strategie = {
            'copie': 0.1,
            'transformation_constante': 0.4,
            'transformation_variable': 0.3,
            'remplissage': 0.5,
            'symetrie': 0.6,
            'rotation': 0.6
        }
        
        bonus = bonus_strategie.get(strategie, 0.0)
        
        return min(1.0, confiance_base + bonus)

def main():
    """Test du solveur amélioré"""
    print("🔧 TEST DU SOLVEUR ARC AMÉLIORÉ")
    
    solver = SolveurARCAmeliore()
    
    # Test avec une tâche simple
    tache_test = TacheARC(
        tache_id="test_remplissage",
        train=[
            {
                "input": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                "output": [[3, 3, 3], [3, 1, 3], [3, 3, 3]]
            },
            {
                "input": [[0, 0], [0, 2], [0, 0]],
                "output": [[4, 4], [4, 2], [4, 4]]
            }
        ],
        test=[
            {
                "input": [[0, 1, 0], [0, 0, 0], [0, 2, 0]],
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
