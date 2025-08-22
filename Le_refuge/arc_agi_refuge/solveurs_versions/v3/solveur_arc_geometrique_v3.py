#!/usr/bin/env python3
"""
🔧 SOLVEUR ARC GÉOMÉTRIQUE V3 - Refuge ARC-AGI
Version avec intégration des patterns géométriques (symétries, rotations, répétitions)
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

class DetecteurGeometrique:
    """🔍 Détecteur de patterns géométriques"""
    
    def __init__(self):
        self.seuil_similarite = 0.8
    
    def detecter_symetries(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, float]:
        """Détecter les types de symétries"""
        symetries = {}
        
        # Symétrie horizontale
        if len(input_grille) == len(output_grille):
            input_flip = np.flipud(input_grille)
            similarite_h = self._calculer_similarite(input_flip, output_grille)
            if similarite_h > self.seuil_similarite:
                symetries['horizontale'] = similarite_h
        
        # Symétrie verticale
        if len(input_grille[0]) == len(output_grille[0]):
            input_flip = np.fliplr(input_grille)
            similarite_v = self._calculer_similarite(input_flip, output_grille)
            if similarite_v > self.seuil_similarite:
                symetries['verticale'] = similarite_v
        
        # Symétrie diagonale
        if len(input_grille) == len(output_grille) and len(input_grille[0]) == len(output_grille[0]):
            input_flip = np.fliplr(np.flipud(input_grille))
            similarite_d = self._calculer_similarite(input_flip, output_grille)
            if similarite_d > self.seuil_similarite:
                symetries['diagonale'] = similarite_d
        
        return symetries
    
    def detecter_rotations(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, float]:
        """Détecter les rotations"""
        rotations = {}
        
        if len(input_grille) == len(output_grille) and len(input_grille[0]) == len(output_grille[0]):
            # Rotation 90°
            input_rot90 = np.rot90(input_grille, 1)
            similarite_90 = self._calculer_similarite(input_rot90, output_grille)
            if similarite_90 > self.seuil_similarite:
                rotations['rotation_90'] = similarite_90
            
            # Rotation 180°
            input_rot180 = np.rot90(input_grille, 2)
            similarite_180 = self._calculer_similarite(input_rot180, output_grille)
            if similarite_180 > self.seuil_similarite:
                rotations['rotation_180'] = similarite_180
            
            # Rotation 270°
            input_rot270 = np.rot90(input_grille, 3)
            similarite_270 = self._calculer_similarite(input_rot270, output_grille)
            if similarite_270 > self.seuil_similarite:
                rotations['rotation_270'] = similarite_270
        
        return rotations
    
    def detecter_repetitions(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter les patterns répétitifs"""
        repetitions = {}
        
        # Répétition horizontale
        facteur_h = self._detecter_facteur_repetition(len(input_grille), len(output_grille))
        if facteur_h > 1:
            repetitions['repetition_horizontale'] = {
                'facteur': facteur_h,
                'confiance': 0.9
            }
        
        # Répétition verticale
        facteur_v = self._detecter_facteur_repetition(len(input_grille[0]), len(output_grille[0]))
        if facteur_v > 1:
            repetitions['repetition_verticale'] = {
                'facteur': facteur_v,
                'confiance': 0.9
            }
        
        # Pattern répétitif dans les valeurs
        pattern_valeurs = self._detecter_pattern_valeurs(input_grille, output_grille)
        if pattern_valeurs:
            repetitions['pattern_valeurs'] = pattern_valeurs
        
        return repetitions
    
    def detecter_translations(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter les translations de motifs"""
        translations = {}
        
        # Chercher des motifs qui se déplacent
        motifs = self._extraire_motifs(input_grille)
        for motif in motifs:
            nouvelle_position = self._chercher_motif(motif, output_grille)
            if nouvelle_position:
                dx = nouvelle_position[0] - motif['position'][0]
                dy = nouvelle_position[1] - motif['position'][1]
                if dx != 0 or dy != 0:
                    translations[f"translation_{len(translations)}"] = {
                        'motif': motif['valeurs'],
                        'deplacement': (dx, dy),
                        'confiance': 0.8
                    }
        
        return translations
    
    def _calculer_similarite(self, grille1: np.ndarray, grille2: List[List[int]]) -> float:
        """Calculer la similarité entre deux grilles"""
        if grille1.shape != (len(grille2), len(grille2[0])):
            return 0.0
        
        grille2_array = np.array(grille2)
        differences = np.sum(grille1 != grille2_array)
        total_elements = grille1.size
        
        return 1.0 - (differences / total_elements)
    
    def _detecter_facteur_repetition(self, taille_in: int, taille_out: int) -> int:
        """Détecter le facteur de répétition"""
        if taille_in == 0:
            return 1
        
        facteur = taille_out / taille_in
        if facteur.is_integer() and facteur > 1:
            return int(facteur)
        return 1
    
    def _detecter_pattern_valeurs(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Optional[Dict]:
        """Détecter des patterns dans les valeurs"""
        input_flat = [val for ligne in input_grille for val in ligne]
        output_flat = [val for ligne in output_grille for val in ligne]
        
        # Chercher des séquences répétitives
        for longueur in range(1, min(len(input_flat), len(output_flat)) // 2 + 1):
            for debut in range(len(input_flat) - longueur + 1):
                sequence = input_flat[debut:debut + longueur]
                if self._sequence_repetee(sequence, output_flat):
                    return {
                        'sequence': sequence,
                        'longueur': longueur,
                        'confiance': 0.85
                    }
        
        return None
    
    def _sequence_repetee(self, sequence: List[int], grille_flat: List[int]) -> bool:
        """Vérifier si une séquence est répétée"""
        if len(sequence) == 0:
            return False
        
        for i in range(0, len(grille_flat) - len(sequence) + 1, len(sequence)):
            if grille_flat[i:i + len(sequence)] == sequence:
                return True
        
        return False
    
    def _extraire_motifs(self, grille: List[List[int]]) -> List[Dict]:
        """Extraire les motifs de la grille"""
        motifs = []
        h, w = len(grille), len(grille[0])
        
        # Chercher des motifs 2x2
        for y in range(h - 1):
            for x in range(w - 1):
                motif = [
                    [grille[y][x], grille[y][x+1]],
                    [grille[y+1][x], grille[y+1][x+1]]
                ]
                motifs.append({
                    'valeurs': motif,
                    'position': (y, x),
                    'taille': (2, 2)
                })
        
        return motifs
    
    def _chercher_motif(self, motif: Dict, grille: List[List[int]]) -> Optional[Tuple[int, int]]:
        """Chercher un motif dans une grille"""
        motif_vals = motif['valeurs']
        h_motif, w_motif = len(motif_vals), len(motif_vals[0])
        h_grille, w_grille = len(grille), len(grille[0])
        
        for y in range(h_grille - h_motif + 1):
            for x in range(w_grille - w_motif + 1):
                trouve = True
                for dy in range(h_motif):
                    for dx in range(w_motif):
                        if grille[y + dy][x + dx] != motif_vals[dy][dx]:
                            trouve = False
                            break
                    if not trouve:
                        break
                if trouve:
                    return (y, x)
        
        return None

class SolveurARCGeometriqueV3:
    """🔧 Solveur ARC géométrique V3 - Avec patterns géométriques"""
    
    def __init__(self):
        self.detecteur = PatternDetector()
        self.detecteur_geo = DetecteurGeometrique()
        self.resultats = {'succes': 0, 'total': 0}

    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Résoudre une tâche avec patterns géométriques"""
        print(f"🔧 RÉSOLUTION TÂCHE GÉOMÉTRIQUE: {tache.tache_id}")
        
        if not tache.test:
            return {'solution': [[0]], 'confiance': 0.0, 'methode': 'erreur'}
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return {'solution': [[0]], 'confiance': 0.0, 'methode': 'erreur'}
        
        # 1. Analyser les patterns géométriques
        patterns_geometriques = self._analyser_patterns_geometriques(tache)
        
        # 2. Analyser les transformations de valeurs
        transformations_valeurs = self._analyser_transformations_valeurs(tache)
        
        # 3. Identifier le pattern principal
        pattern_principal = self._identifier_pattern_principal(patterns_geometriques, transformations_valeurs)
        
        # 4. Appliquer le pattern au test
        solution = self._appliquer_pattern_geometrique(test_input, pattern_principal, tache)
        
        # 5. Calculer la confiance
        confiance = self._calculer_confiance_geometrique(pattern_principal, patterns_geometriques, transformations_valeurs)
        
        return {
            'solution': solution,
            'confiance': confiance,
            'methode': pattern_principal.get('type', 'inconnue'),
            'patterns_geometriques': len(patterns_geometriques),
            'transformations_valeurs': len(transformations_valeurs),
            'pattern_detecte': pattern_principal
        }

    def _analyser_patterns_geometriques(self, tache: TacheARC) -> List[Dict]:
        """Analyser les patterns géométriques dans les exemples d'entraînement"""
        patterns = []
        
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            pattern = {
                'symetries': self.detecteur_geo.detecter_symetries(input_grille, output_grille),
                'rotations': self.detecteur_geo.detecter_rotations(input_grille, output_grille),
                'repetitions': self.detecteur_geo.detecter_repetitions(input_grille, output_grille),
                'translations': self.detecteur_geo.detecter_translations(input_grille, output_grille)
            }
            
            patterns.append(pattern)
        
        return patterns

    def _analyser_transformations_valeurs(self, tache: TacheARC) -> List[Dict]:
        """Analyser les transformations de valeurs"""
        transformations = []
        
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
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

    def _identifier_pattern_principal(self, patterns_geo: List[Dict], transformations: List[Dict]) -> Dict:
        """Identifier le pattern principal"""
        if not patterns_geo and not transformations:
            return {'type': 'fallback', 'confiance': 0.0}
        
        # Analyser les patterns géométriques
        symetries_totales = defaultdict(int)
        rotations_totales = defaultdict(int)
        repetitions_totales = defaultdict(int)
        
        for pattern in patterns_geo:
            for sym_type, conf in pattern['symetries'].items():
                symetries_totales[sym_type] += 1
            for rot_type, conf in pattern['rotations'].items():
                rotations_totales[rot_type] += 1
            for rep_type, details in pattern['repetitions'].items():
                repetitions_totales[rep_type] += 1
        
        # Identifier le pattern dominant
        if symetries_totales:
            sym_principale = max(symetries_totales.items(), key=lambda x: x[1])
            return {
                'type': 'symetrie',
                'symetrie': sym_principale[0],
                'confiance': sym_principale[1] / len(patterns_geo),
                'details': dict(symetries_totales)
            }
        
        elif rotations_totales:
            rot_principale = max(rotations_totales.items(), key=lambda x: x[1])
            return {
                'type': 'rotation',
                'rotation': rot_principale[0],
                'confiance': rot_principale[1] / len(patterns_geo),
                'details': dict(rotations_totales)
            }
        
        elif repetitions_totales:
            rep_principale = max(repetitions_totales.items(), key=lambda x: x[1])
            return {
                'type': 'repetition',
                'repetition': rep_principale[0],
                'confiance': rep_principale[1] / len(patterns_geo),
                'details': dict(repetitions_totales)
            }
        
        # Fallback sur les transformations de valeurs
        elif transformations:
            patterns_valeurs = defaultdict(int)
            for trans in transformations:
                for val_in, val_out in trans['mapping_valeurs'].items():
                    patterns_valeurs[(val_in, val_out)] += 1
            
            if patterns_valeurs:
                mapping_principal = max(patterns_valeurs.items(), key=lambda x: x[1])
                return {
                    'type': 'transformation_valeurs',
                    'mapping': mapping_principal[0],
                    'confiance': mapping_principal[1] / len(transformations),
                    'details': dict(patterns_valeurs)
                }
        
        return {'type': 'fallback', 'confiance': 0.0}

    def _appliquer_pattern_geometrique(self, test_input: List[List[int]], pattern: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer le pattern géométrique détecté"""
        
        if pattern['type'] == 'symetrie':
            return self._appliquer_symetrie(test_input, pattern)
        
        elif pattern['type'] == 'rotation':
            return self._appliquer_rotation(test_input, pattern)
        
        elif pattern['type'] == 'repetition':
            return self._appliquer_repetition(test_input, pattern, tache)
        
        elif pattern['type'] == 'transformation_valeurs':
            return self._appliquer_transformation_valeurs(test_input, pattern)
        
        else:
            # Fallback
            return test_input

    def _appliquer_symetrie(self, test_input: List[List[int]], pattern: Dict) -> List[List[int]]:
        """Appliquer une symétrie"""
        symetrie = pattern['symetrie']
        test_array = np.array(test_input)
        
        if symetrie == 'horizontale':
            return np.flipud(test_array).tolist()
        elif symetrie == 'verticale':
            return np.fliplr(test_array).tolist()
        elif symetrie == 'diagonale':
            return np.fliplr(np.flipud(test_array)).tolist()
        
        return test_input

    def _appliquer_rotation(self, test_input: List[List[int]], pattern: Dict) -> List[List[int]]:
        """Appliquer une rotation"""
        rotation = pattern['rotation']
        test_array = np.array(test_input)
        
        if rotation == 'rotation_90':
            return np.rot90(test_array, 1).tolist()
        elif rotation == 'rotation_180':
            return np.rot90(test_array, 2).tolist()
        elif rotation == 'rotation_270':
            return np.rot90(test_array, 3).tolist()
        
        return test_input

    def _appliquer_repetition(self, test_input: List[List[int]], pattern: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer une répétition"""
        repetition = pattern['repetition']
        
        # Analyser la taille de sortie attendue depuis les exemples d'entraînement
        if tache.train:
            exemple = tache.train[0]
            output_grille = exemple.get('output', [])
            if output_grille:
                h_out, w_out = len(output_grille), len(output_grille[0])
                
                if repetition == 'repetition_horizontale':
                    return self._repetition_horizontale(test_input, h_out)
                elif repetition == 'repetition_verticale':
                    return self._repetition_verticale(test_input, w_out)
                elif repetition == 'pattern_valeurs':
                    return self._repetition_pattern_valeurs(test_input, pattern, h_out, w_out)
        
        return test_input

    def _repetition_horizontale(self, grille: List[List[int]], h_out: int) -> List[List[int]]:
        """Répétition horizontale"""
        h_in = len(grille)
        if h_in == 0:
            return grille
        
        facteur = h_out // h_in
        reste = h_out % h_in
        
        resultat = []
        for _ in range(facteur):
            resultat.extend(grille)
        
        if reste > 0:
            resultat.extend(grille[:reste])
        
        return resultat

    def _repetition_verticale(self, grille: List[List[int]], w_out: int) -> List[List[int]]:
        """Répétition verticale"""
        if not grille:
            return grille
        
        w_in = len(grille[0])
        if w_in == 0:
            return grille
        
        facteur = w_out // w_in
        reste = w_out % w_in
        
        resultat = []
        for ligne in grille:
            nouvelle_ligne = ligne * facteur
            if reste > 0:
                nouvelle_ligne.extend(ligne[:reste])
            resultat.append(nouvelle_ligne)
        
        return resultat

    def _repetition_pattern_valeurs(self, grille: List[List[int]], pattern: Dict, h_out: int, w_out: int) -> List[List[int]]:
        """Répétition de pattern de valeurs"""
        sequence = pattern.get('details', {}).get('sequence', [])
        if not sequence:
            return grille
        
        # Créer une grille avec le pattern répété
        resultat = []
        for y in range(h_out):
            ligne = []
            for x in range(w_out):
                index = (y * w_out + x) % len(sequence)
                ligne.append(sequence[index])
            resultat.append(ligne)
        
        return resultat

    def _appliquer_transformation_valeurs(self, test_input: List[List[int]], pattern: Dict) -> List[List[int]]:
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

    def _calculer_confiance_geometrique(self, pattern: Dict, patterns_geo: List[Dict], transformations: List[Dict]) -> float:
        """Calculer la confiance avec les patterns géométriques"""
        confiance_base = pattern.get('confiance', 0.0)
        
        # Bonus pour la cohérence géométrique
        if patterns_geo:
            coherence_geo = self._calculer_coherence_geometrique(patterns_geo)
            confiance_base += coherence_geo * 0.3
        
        # Bonus pour la cohérence des transformations
        if transformations:
            coherence_trans = self._calculer_coherence_transformations(transformations)
            confiance_base += coherence_trans * 0.2
        
        return min(1.0, confiance_base)

    def _calculer_coherence_geometrique(self, patterns_geo: List[Dict]) -> float:
        """Calculer la cohérence entre les patterns géométriques"""
        if len(patterns_geo) < 2:
            return 0.5
        
        # Comparer les types de patterns
        types_patterns = []
        for pattern in patterns_geo:
            types = []
            if pattern['symetries']:
                types.append('symetrie')
            if pattern['rotations']:
                types.append('rotation')
            if pattern['repetitions']:
                types.append('repetition')
            types_patterns.append(set(types))
        
        # Calculer la similarité
        similarites = []
        for i in range(len(types_patterns)):
            for j in range(i + 1, len(types_patterns)):
                intersection = len(types_patterns[i] & types_patterns[j])
                union = len(types_patterns[i] | types_patterns[j])
                if union > 0:
                    similarites.append(intersection / union)
        
        return np.mean(similarites) if similarites else 0.0

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

def main():
    """Test du solveur géométrique V3"""
    print("🔧 TEST SOLVEUR ARC GÉOMÉTRIQUE V3")
    print("=" * 50)
    
    # Créer une tâche de test avec symétrie
    tache_test = TacheARC(
        tache_id="test_symetrie",
        train=[
            {
                'input': [[1, 2, 3], [4, 5, 6]],
                'output': [[6, 5, 4], [3, 2, 1]]
            },
            {
                'input': [[0, 1], [2, 3]],
                'output': [[3, 2], [1, 0]]
            }
        ],
        test=[
            {
                'input': [[7, 8, 9], [10, 11, 12]],
                'output': None
            }
        ]
    )
    
    # Tester le solveur
    solveur = SolveurARCGeometriqueV3()
    resultat = solveur.resoudre_tache(tache_test)
    
    print(f"Solution: {resultat['solution']}")
    print(f"Confiance: {resultat['confiance']:.2f}")
    print(f"Méthode: {resultat['methode']}")

if __name__ == "__main__":
    main()
