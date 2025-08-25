#!/usr/bin/env python3
"""
🔧 SOLVEUR ARC CORRIGÉ V2 - Refuge ARC-AGI
Version corrigée qui utilise réellement les patterns détectés
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

class SolveurARCCorrigeV2:
    """🔧 Solveur ARC corrigé V2 - Utilise réellement les patterns détectés"""

    def __init__(self):
        self.detecteur = PatternDetector()
        self.resultats = {'succes': 0, 'total': 0}

    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Résoudre une tâche en utilisant les patterns détectés"""
        print(f"🔧 RÉSOLUTION TÂCHE: {tache.tache_id}")
        
        if not tache.test:
            return {'solution': [[0]], 'confiance': 0.0, 'methode': 'erreur'}
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return {'solution': [[0]], 'confiance': 0.0, 'methode': 'erreur'}
        
        # 1. Analyser les patterns entre input et output des exemples d'entraînement
        transformations = self._analyser_transformations_entrainement(tache)
        
        # 2. Identifier le pattern principal
        pattern_principal = self._identifier_pattern_principal(transformations)
        
        # 3. Appliquer le pattern au test
        solution = self._appliquer_pattern(test_input, pattern_principal, transformations)
        
        # 4. Calculer la confiance
        confiance = self._calculer_confiance(pattern_principal, transformations)
        
        return {
            'solution': solution,
            'confiance': confiance,
            'methode': pattern_principal.get('type', 'inconnue'),
            'transformations_analysees': len(transformations),
            'pattern_detecte': pattern_principal
        }

    def _analyser_transformations_entrainement(self, tache: TacheARC) -> List[Dict]:
        """Analyser les transformations entre input et output des exemples d'entraînement"""
        transformations = []
        
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            # Analyser les transformations de valeurs
            transformation = {
                'input_shape': (len(input_grille), len(input_grille[0])),
                'output_shape': (len(output_grille), len(output_grille[0])),
                'valeurs_input': set(),
                'valeurs_output': set(),
                'mapping_valeurs': {},
                'positions_changees': []
            }
            
            # Collecter les valeurs
            for ligne in input_grille:
                transformation['valeurs_input'].update(ligne)
            for ligne in output_grille:
                transformation['valeurs_output'].update(ligne)
            
            # Analyser les changements de valeurs
            for y in range(min(len(input_grille), len(output_grille))):
                for x in range(min(len(input_grille[0]), len(output_grille[0]))):
                    val_in = input_grille[y][x]
                    val_out = output_grille[y][x]
                    
                    if val_in != val_out:
                        transformation['mapping_valeurs'][val_in] = val_out
                        transformation['positions_changees'].append((y, x, val_in, val_out))
            
            transformations.append(transformation)
        
        return transformations

    def _identifier_pattern_principal(self, transformations: List[Dict]) -> Dict:
        """Identifier le pattern principal parmi les transformations"""
        if not transformations:
            return {'type': 'fallback', 'confiance': 0.0}
        
        # Analyser les patterns récurrents
        patterns = {
            'mapping_valeurs': defaultdict(int),
            'shape_changes': defaultdict(int),
            'valeurs_ajoutees': set(),
            'valeurs_supprimees': set()
        }
        
        for trans in transformations:
            # Compter les mappings de valeurs
            for val_in, val_out in trans['mapping_valeurs'].items():
                patterns['mapping_valeurs'][(val_in, val_out)] += 1
            
            # Analyser les changements de forme
            shape_change = (trans['input_shape'], trans['output_shape'])
            patterns['shape_changes'][shape_change] += 1
            
            # Analyser les valeurs ajoutées/supprimées
            patterns['valeurs_ajoutees'].update(
                trans['valeurs_output'] - trans['valeurs_input']
            )
            patterns['valeurs_supprimees'].update(
                trans['valeurs_input'] - trans['valeurs_output']
            )
        
        # Identifier le pattern dominant
        if patterns['mapping_valeurs']:
            # Pattern de transformation de valeurs
            mapping_principal = max(patterns['mapping_valeurs'].items(), 
                                  key=lambda x: x[1])
            return {
                'type': 'transformation_valeurs',
                'mapping': mapping_principal[0],
                'confiance': mapping_principal[1] / len(transformations),
                'details': patterns
            }
        
        elif patterns['shape_changes']:
            # Pattern de changement de forme
            shape_principal = max(patterns['shape_changes'].items(), 
                                key=lambda x: x[1])
            return {
                'type': 'changement_forme',
                'shape_change': shape_principal[0],
                'confiance': shape_principal[1] / len(transformations),
                'details': patterns
            }
        
        elif patterns['valeurs_ajoutees'] or patterns['valeurs_supprimees']:
            # Pattern d'ajout/suppression de valeurs
            return {
                'type': 'modification_valeurs',
                'valeurs_ajoutees': list(patterns['valeurs_ajoutees']),
                'valeurs_supprimees': list(patterns['valeurs_supprimees']),
                'confiance': 0.8,
                'details': patterns
            }
        
        else:
            # Aucun pattern clair détecté
            return {'type': 'fallback', 'confiance': 0.0}

    def _appliquer_pattern(self, test_input: List[List[int]], pattern: Dict, 
                          transformations: List[Dict]) -> List[List[int]]:
        """Appliquer le pattern détecté au test input"""
        
        if pattern['type'] == 'transformation_valeurs':
            return self._appliquer_transformation_valeurs(test_input, pattern)
        
        elif pattern['type'] == 'changement_forme':
            return self._appliquer_changement_forme(test_input, pattern)
        
        elif pattern['type'] == 'modification_valeurs':
            return self._appliquer_modification_valeurs(test_input, pattern)
        
        else:
            # Fallback : analyser les transformations spécifiques
            return self._appliquer_transformations_specifiques(test_input, transformations)

    def _appliquer_transformation_valeurs(self, test_input: List[List[int]], 
                                        pattern: Dict) -> List[List[int]]:
        """Appliquer une transformation de valeurs"""
        mapping = pattern['mapping']
        val_in, val_out = mapping
        
        resultat = []
        for ligne in test_input:
            nouvelle_ligne = []
            for val in ligne:
                if val == val_in:
                    nouvelle_ligne.append(val_out)
                else:
                    nouvelle_ligne.append(val)
            resultat.append(nouvelle_ligne)
        
        return resultat

    def _appliquer_changement_forme(self, test_input: List[List[int]], 
                                   pattern: Dict) -> List[List[int]]:
        """Appliquer un changement de forme"""
        shape_change = pattern['shape_change']
        input_shape, output_shape = shape_change
        
        # Calculer les facteurs de changement
        h_in, w_in = input_shape
        h_out, w_out = output_shape
        
        if h_in > 0 and w_in > 0:
            facteur_h = h_out / h_in
            facteur_w = w_out / w_in
            
            if facteur_h > 1 or facteur_w > 1:
                # Expansion
                return self._expandre_grille(test_input, h_out, w_out)
            elif facteur_h < 1 or facteur_w < 1:
                # Réduction
                return self._reduire_grille(test_input, h_out, w_out)
        
        return test_input

    def _appliquer_modification_valeurs(self, test_input: List[List[int]], 
                                       pattern: Dict) -> List[List[int]]:
        """Appliquer une modification de valeurs (ajout/suppression)"""
        valeurs_ajoutees = pattern.get('valeurs_ajoutees', [])
        valeurs_supprimees = pattern.get('valeurs_supprimees', [])
        
        resultat = []
        for ligne in test_input:
            nouvelle_ligne = []
            for val in ligne:
                if val in valeurs_supprimees:
                    # Remplacer par une valeur par défaut
                    nouvelle_ligne.append(0)
                else:
                    nouvelle_ligne.append(val)
            resultat.append(nouvelle_ligne)
        
        # Ajouter des valeurs si nécessaire
        if valeurs_ajoutees and resultat:
            # Ajouter une nouvelle ligne avec les valeurs ajoutées
            nouvelle_ligne = [valeurs_ajoutees[0]] * len(resultat[0])
            resultat.append(nouvelle_ligne)
        
        return resultat

    def _appliquer_transformations_specifiques(self, test_input: List[List[int]], 
                                             transformations: List[Dict]) -> List[List[int]]:
        """Appliquer des transformations spécifiques basées sur les exemples"""
        if not transformations:
            return test_input
        
        # Prendre le premier exemple comme référence
        ref_trans = transformations[0]
        
        # Analyser les changements de position
        if ref_trans['positions_changees']:
            # Créer un mapping de positions
            mapping_positions = {}
            for y, x, val_in, val_out in ref_trans['positions_changees']:
                mapping_positions[(y, x)] = (val_in, val_out)
            
            # Appliquer les changements
            resultat = []
            for y, ligne in enumerate(test_input):
                nouvelle_ligne = []
                for x, val in enumerate(ligne):
                    if (y, x) in mapping_positions:
                        val_in, val_out = mapping_positions[(y, x)]
                        if val == val_in:
                            nouvelle_ligne.append(val_out)
                        else:
                            nouvelle_ligne.append(val)
                    else:
                        nouvelle_ligne.append(val)
                resultat.append(nouvelle_ligne)
            
            return resultat
        
        return test_input

    def _calculer_confiance(self, pattern: Dict, transformations: List[Dict]) -> float:
        """Calculer la confiance de la solution"""
        if not transformations:
            return 0.0
        
        # Confiance basée sur la cohérence du pattern
        confiance_base = pattern.get('confiance', 0.0)
        
        # Bonus pour la cohérence entre les transformations
        coherence = self._calculer_coherence_transformations(transformations)
        
        return min(1.0, confiance_base + coherence * 0.2)

    def _calculer_coherence_transformations(self, transformations: List[Dict]) -> float:
        """Calculer la cohérence entre les transformations"""
        if len(transformations) < 2:
            return 0.5
        
        # Comparer les mappings de valeurs
        mappings = []
        for trans in transformations:
            mappings.append(set(trans['mapping_valeurs'].items()))
        
        # Calculer la similarité
        similarites = []
        for i in range(len(mappings)):
            for j in range(i + 1, len(mappings)):
                intersection = len(mappings[i] & mappings[j])
                union = len(mappings[i] | mappings[j])
                if union > 0:
                    similarites.append(intersection / union)
        
        return np.mean(similarites) if similarites else 0.0

    def _expandre_grille(self, grille: List[List[int]], h_out: int, w_out: int) -> List[List[int]]:
        """Expandre une grille"""
        if not grille:
            return [[0]]
        
        h_in, w_in = len(grille), len(grille[0])
        
        resultat = []
        for y in range(h_out):
            ligne = []
            for x in range(w_out):
                y_in = y % h_in
                x_in = x % w_in
                ligne.append(grille[y_in][x_in])
            resultat.append(ligne)
        
        return resultat

    def _reduire_grille(self, grille: List[List[int]], h_out: int, w_out: int) -> List[List[int]]:
        """Réduire une grille"""
        if not grille:
            return [[0]]
        
        h_in, w_in = len(grille), len(grille[0])
        
        resultat = []
        for y in range(h_out):
            ligne = []
            for x in range(w_out):
                y_in = int(y * h_in / h_out)
                x_in = int(x * w_in / w_out)
                ligne.append(grille[y_in][x_in])
            resultat.append(ligne)
        
        return resultat

def main():
    """Test du solveur corrigé"""
    print("🔧 TEST SOLVEUR ARC CORRIGÉ V2")
    print("=" * 50)
    
    # Créer une tâche de test simple
    tache_test = TacheARC(
        tache_id="test_simple",
        train=[
            {
                'input': [[1, 2], [3, 4]],
                'output': [[2, 3], [4, 5]]
            },
            {
                'input': [[0, 1], [2, 3]],
                'output': [[1, 2], [3, 4]]
            }
        ],
        test=[
            {
                'input': [[5, 6], [7, 8]],
                'output': None
            }
        ]
    )
    
    # Tester le solveur
    solveur = SolveurARCCorrigeV2()
    resultat = solveur.resoudre_tache(tache_test)
    
    print(f"Solution: {resultat['solution']}")
    print(f"Confiance: {resultat['confiance']:.2f}")
    print(f"Méthode: {resultat['methode']}")

if __name__ == "__main__":
    main()
