#!/usr/bin/env python3
"""
🔧 SOLVEUR ARC ULTIME V6 - Refuge ARC-AGI
Version avec amélioration spécifique des répétitions et symétries
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
    from pattern_detector_simple import PatternDetector
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

class AnalyseurUltime:
    """🧠 Analyseur ultime pour patterns complexes"""
    
    def __init__(self):
        self.seuil_similarite = 0.5  # Très permissif pour capturer plus de patterns
    
    def analyser_pattern_complet(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, Any]:
        """Analyse complète d'un pattern input→output"""
        analyse = {
            'symetries': self._detecter_symetries_ultimes(input_grille, output_grille),
            'rotations': self._detecter_rotations_ultimes(input_grille, output_grille),
            'repetitions': self._detecter_repetitions_ultimes(input_grille, output_grille),
            'transformations_valeurs': self._detecter_transformations_ultimes(input_grille, output_grille),
            'patterns_imbriques': self._detecter_patterns_imbriques_ultimes(input_grille, output_grille),
            'logique_conditionnelle': self._detecter_logique_conditionnelle_ultime(input_grille, output_grille)
        }
        
        # Calculer le pattern dominant
        pattern_dominant = self._identifier_pattern_dominant_ultime(analyse)
        analyse['pattern_dominant'] = pattern_dominant
        
        return analyse
    
    def _detecter_repetitions_ultimes(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détection ultime des répétitions - AMÉLIORÉE"""
        repetitions = {}
        
        # Analyser les dimensions
        h_in, w_in = len(input_grille), len(input_grille[0])
        h_out, w_out = len(output_grille), len(output_grille[0])
        
        # Répétition horizontale (lignes) - AMÉLIORÉE
        if h_out > h_in and h_out % h_in == 0:
            facteur_h = h_out // h_in
            repetitions['repetition_horizontale'] = {
                'facteur': facteur_h,
                'confiance': 0.95,
                'type': 'lignes_completes',
                'motif_source': input_grille
            }
        
        # Répétition verticale (colonnes) - AMÉLIORÉE
        if w_out > w_in and w_out % w_in == 0:
            facteur_w = w_out // w_in
            repetitions['repetition_verticale'] = {
                'facteur': facteur_w,
                'confiance': 0.95,
                'type': 'colonnes_completes',
                'motif_source': input_grille
            }
        
        # Détecter les motifs répétitifs dans la grille de sortie
        motifs_repetitifs = self._detecter_motifs_repetitifs_ultimes(output_grille)
        if motifs_repetitifs:
            repetitions['motifs_repetitifs'] = motifs_repetitifs
        
        return repetitions
    
    def _detecter_motifs_repetitifs_ultimes(self, grille: List[List[int]]) -> Optional[Dict]:
        """Détecter des motifs répétitifs dans une grille - AMÉLIORÉE"""
        h, w = len(grille), len(grille[0])
        
        # Chercher des motifs 2x2, 3x3, etc.
        for taille in [2, 3, 4]:
            motifs = self._extraire_motifs_taille_ultime(grille, taille)
            for motif in motifs:
                occurrences = self._compter_occurrences_motif_ultime(motif, grille)
                if occurrences >= 2:  # Au moins 2 occurrences
                    return {
                        'motif': motif,
                        'taille': taille,
                        'occurrences': occurrences,
                        'confiance': 0.9
                    }
        
        return None
    
    def _extraire_motifs_taille_ultime(self, grille: List[List[int]], taille: int) -> List[List[List[int]]]:
        """Extraire des motifs d'une taille donnée - AMÉLIORÉE"""
        motifs = []
        h, w = len(grille), len(grille[0])
        
        for y in range(h - taille + 1):
            for x in range(w - taille + 1):
                motif = []
                for dy in range(taille):
                    ligne = []
                    for dx in range(taille):
                        ligne.append(grille[y + dy][x + dx])
                    motif.append(ligne)
                motifs.append(motif)
        
        return motifs
    
    def _compter_occurrences_motif_ultime(self, motif: List[List[int]], grille: List[List[int]]) -> int:
        """Compter les occurrences d'un motif dans une grille - AMÉLIORÉE"""
        h_motif, w_motif = len(motif), len(motif[0])
        h_grille, w_grille = len(grille), len(grille[0])
        
        occurrences = 0
        for y in range(h_grille - h_motif + 1):
            for x in range(w_grille - w_motif + 1):
                if self._motif_egal_ultime(motif, grille, y, x):
                    occurrences += 1
        
        return occurrences
    
    def _motif_egal_ultime(self, motif: List[List[int]], grille: List[List[int]], y: int, x: int) -> bool:
        """Vérifier si un motif est égal à une portion de grille - AMÉLIORÉE"""
        h_motif, w_motif = len(motif), len(motif[0])
        
        for dy in range(h_motif):
            for dx in range(w_motif):
                if motif[dy][dx] != grille[y + dy][x + dx]:
                    return False
        return True
    
    def _detecter_symetries_ultimes(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, float]:
        """Détection ultime des symétries - AMÉLIORÉE"""
        symetries = {}
        
        # Symétrie horizontale - AMÉLIORÉE
        if len(input_grille) == len(output_grille):
            input_flip = np.flipud(input_grille)
            similarite_h = self._calculer_similarite_ultime(input_flip, output_grille)
            if similarite_h > self.seuil_similarite:
                symetries['horizontale'] = similarite_h
        
        # Symétrie verticale - AMÉLIORÉE
        if len(input_grille[0]) == len(output_grille[0]):
            input_flip = np.fliplr(input_grille)
            similarite_v = self._calculer_similarite_ultime(input_flip, output_grille)
            if similarite_v > self.seuil_similarite:
                symetries['verticale'] = similarite_v
        
        # Symétrie diagonale - AMÉLIORÉE
        if len(input_grille) == len(output_grille) and len(input_grille[0]) == len(output_grille[0]):
            input_flip = np.fliplr(np.flipud(input_grille))
            similarite_d = self._calculer_similarite_ultime(input_flip, output_grille)
            if similarite_d > self.seuil_similarite:
                symetries['diagonale'] = similarite_d
        
        return symetries
    
    def _detecter_transformations_ultimes(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détection ultime des transformations de valeurs - AMÉLIORÉE"""
        transformations = {
            'mappings': {},
            'valeurs_ajoutees': set(),
            'valeurs_supprimees': set(),
            'valeurs_conservees': set()
        }
        
        # Collecter toutes les valeurs
        valeurs_input = set()
        valeurs_output = set()
        
        for ligne in input_grille:
            valeurs_input.update(ligne)
        for ligne in output_grille:
            valeurs_output.update(ligne)
        
        # Analyser les mappings - AMÉLIORÉE
        mappings_coherents = {}
        for y in range(min(len(input_grille), len(output_grille))):
            for x in range(min(len(input_grille[0]), len(output_grille[0]))):
                val_in = input_grille[y][x]
                val_out = output_grille[y][x]
                
                if val_in != val_out:
                    if val_in not in mappings_coherents:
                        mappings_coherents[val_in] = val_out
                    elif mappings_coherents[val_in] != val_out:
                        # Mapping incohérent - on l'ignore
                        continue
        
        # N'ajouter que les mappings cohérents
        transformations['mappings'] = mappings_coherents
        
        # Analyser les valeurs ajoutées/supprimées
        transformations['valeurs_ajoutees'] = valeurs_output - valeurs_input
        transformations['valeurs_supprimees'] = valeurs_input - valeurs_output
        transformations['valeurs_conservees'] = valeurs_input & valeurs_output
        
        return transformations
    
    def _detecter_rotations_ultimes(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, float]:
        """Détection ultime des rotations - AMÉLIORÉE"""
        rotations = {}
        
        if len(input_grille) == len(output_grille) and len(input_grille[0]) == len(output_grille[0]):
            # Rotation 90°
            input_rot90 = np.rot90(input_grille, 1)
            similarite_90 = self._calculer_similarite_ultime(input_rot90, output_grille)
            if similarite_90 > self.seuil_similarite:
                rotations['rotation_90'] = similarite_90
            
            # Rotation 180°
            input_rot180 = np.rot90(input_grille, 2)
            similarite_180 = self._calculer_similarite_ultime(input_rot180, output_grille)
            if similarite_180 > self.seuil_similarite:
                rotations['rotation_180'] = similarite_180
            
            # Rotation 270°
            input_rot270 = np.rot90(input_grille, 3)
            similarite_270 = self._calculer_similarite_ultime(input_rot270, output_grille)
            if similarite_270 > self.seuil_similarite:
                rotations['rotation_270'] = similarite_270
        
        return rotations
    
    def _detecter_patterns_imbriques_ultimes(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter des patterns imbriqués - AMÉLIORÉE"""
        patterns = {}
        
        # Chercher des patterns de remplissage
        pattern_remplissage = self._detecter_pattern_remplissage_ultime(input_grille, output_grille)
        if pattern_remplissage:
            patterns['remplissage'] = pattern_remplissage
        
        return patterns
    
    def _detecter_logique_conditionnelle_ultime(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter une logique conditionnelle - AMÉLIORÉE"""
        logique = {}
        
        # Analyser les conditions basées sur la position
        conditions_position = self._analyser_conditions_position_ultime(input_grille, output_grille)
        if conditions_position:
            logique['conditions_position'] = conditions_position
        
        return logique
    
    def _calculer_similarite_ultime(self, grille1: np.ndarray, grille2: List[List[int]]) -> float:
        """Calculer la similarité de manière ultime - AMÉLIORÉE"""
        if grille1.shape != (len(grille2), len(grille2[0])):
            return 0.0
        
        grille2_array = np.array(grille2)
        differences = np.sum(grille1 != grille2_array)
        total_elements = grille1.size
        
        return 1.0 - (differences / total_elements)
    
    def _detecter_pattern_remplissage_ultime(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Optional[Dict]:
        """Détecter un pattern de remplissage - AMÉLIORÉE"""
        zones_remplies = []
        
        for y in range(min(len(input_grille), len(output_grille))):
            for x in range(min(len(input_grille[0]), len(output_grille[0]))):
                if input_grille[y][x] == 0 and output_grille[y][x] != 0:
                    zones_remplies.append((y, x, output_grille[y][x]))
        
        if zones_remplies:
            return {
                'zones_remplies': zones_remplies,
                'confiance': 0.8
            }
        
        return None
    
    def _analyser_conditions_position_ultime(self, input_grille: List[List[int]], output_grille: List[List[int]]) -> Optional[Dict]:
        """Analyser les conditions basées sur la position - AMÉLIORÉE"""
        conditions = {}
        
        # Analyser les bords
        h_in, w_in = len(input_grille), len(input_grille[0])
        h_out, w_out = len(output_grille), len(output_grille[0])
        
        # Condition sur les bords
        if h_out > h_in or w_out > w_in:
            conditions['expansion_bords'] = {
                'h_ajout': max(0, h_out - h_in),
                'w_ajout': max(0, w_out - w_in)
            }
        
        return conditions if conditions else None
    
    def _identifier_pattern_dominant_ultime(self, analyse: Dict[str, Any]) -> Dict[str, Any]:
        """Identifier le pattern dominant - AMÉLIORÉE"""
        scores = {
            'symetrie': len(analyse['symetries']) * 0.3,
            'rotation': len(analyse['rotations']) * 0.3,
            'repetition': len(analyse['repetitions']) * 0.4,
            'transformation': len(analyse['transformations_valeurs']['mappings']) * 0.2,
            'imbrique': len(analyse['patterns_imbriques']) * 0.3,
            'logique': len(analyse['logique_conditionnelle']) * 0.4
        }
        
        pattern_max = max(scores.items(), key=lambda x: x[1])
        
        return {
            'type': pattern_max[0],
            'score': pattern_max[1],
            'details': analyse
        }

class SolveurARCUltimeV6:
    """🔧 Solveur ARC ultime V6 - Avec améliorations spécifiques"""
    
    def __init__(self):
        self.detecteur = PatternDetector()
        self.analyseur = AnalyseurUltime()
        self.resultats = {'succes': 0, 'total': 0}

    def resoudre_tache(self, tache: TacheARC) -> Dict[str, Any]:
        """Résoudre une tâche avec perfection ultime"""
        print(f"🔧 RÉSOLUTION TÂCHE ULTIME: {tache.tache_id}")
        
        if not tache.test:
            return {'solution': [[0]], 'confiance': 0.0, 'methode': 'erreur'}
        
        test_input = tache.test[0].get('input', [])
        if not test_input:
            return {'solution': [[0]], 'confiance': 0.0, 'methode': 'erreur'}
        
        # 1. Analyser tous les patterns des exemples d'entraînement
        analyses = self._analyser_exemples_entrainement_ultime(tache)
        
        # 2. Identifier le pattern principal
        pattern_principal = self._identifier_pattern_principal_ultime(analyses)
        
        # 3. Appliquer le pattern avec validation ultime
        solution = self._appliquer_pattern_ultime(test_input, pattern_principal, tache)
        
        # 4. Calculer la confiance
        confiance = self._calculer_confiance_ultime(pattern_principal, analyses)
        
        return {
            'solution': solution,
            'confiance': confiance,
            'methode': pattern_principal.get('type', 'inconnue'),
            'analyses_effectuees': len(analyses),
            'pattern_detecte': pattern_principal
        }

    def _analyser_exemples_entrainement_ultime(self, tache: TacheARC) -> List[Dict[str, Any]]:
        """Analyser tous les exemples d'entraînement - AMÉLIORÉE"""
        analyses = []
        
        for exemple in tache.train:
            input_grille = exemple.get('input', [])
            output_grille = exemple.get('output', [])
            
            if not input_grille or not output_grille:
                continue
            
            analyse = self.analyseur.analyser_pattern_complet(input_grille, output_grille)
            analyses.append(analyse)
        
        return analyses

    def _identifier_pattern_principal_ultime(self, analyses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Identifier le pattern principal de manière ultime - AMÉLIORÉE"""
        if not analyses:
            return {'type': 'fallback', 'confiance': 0.0}
        
        # Compter les types de patterns
        types_patterns = defaultdict(int)
        scores_patterns = defaultdict(float)
        
        for analyse in analyses:
            pattern_dominant = analyse.get('pattern_dominant', {})
            pattern_type = pattern_dominant.get('type', 'inconnu')
            score = pattern_dominant.get('score', 0.0)
            
            types_patterns[pattern_type] += 1
            scores_patterns[pattern_type] += score
        
        # Identifier le pattern le plus fréquent et avec le meilleur score
        if types_patterns:
            pattern_frequent = max(types_patterns.items(), key=lambda x: x[1])
            pattern_score = max(scores_patterns.items(), key=lambda x: x[1])
            
            # Prioriser le pattern avec le meilleur score
            pattern_choisi = pattern_score[0]
            confiance = pattern_score[1] / len(analyses)
            
            return {
                'type': pattern_choisi,
                'confiance': confiance,
                'frequence': types_patterns[pattern_choisi],
                'score_total': scores_patterns[pattern_choisi]
            }
        
        return {'type': 'fallback', 'confiance': 0.0}

    def _appliquer_pattern_ultime(self, test_input: List[List[int]], pattern: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer le pattern de manière ultime - AMÉLIORÉE"""
        pattern_type = pattern.get('type', 'fallback')
        
        if pattern_type == 'symetrie':
            return self._appliquer_symetrie_ultime(test_input, pattern, tache)
        
        elif pattern_type == 'rotation':
            return self._appliquer_rotation_ultime(test_input, pattern, tache)
        
        elif pattern_type == 'repetition':
            return self._appliquer_repetition_ultime(test_input, pattern, tache)
        
        elif pattern_type == 'transformation':
            return self._appliquer_transformation_ultime(test_input, pattern, tache)
        
        elif pattern_type == 'imbrique':
            return self._appliquer_pattern_imbrique_ultime(test_input, pattern, tache)
        
        elif pattern_type == 'logique':
            return self._appliquer_logique_conditionnelle_ultime(test_input, pattern, tache)
        
        else:
            # Fallback ultime
            return self._appliquer_fallback_ultime(test_input, tache)

    def _appliquer_repetition_ultime(self, test_input: List[List[int]], pattern: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer une répétition de manière ultime - AMÉLIORÉE"""
        analyses = self._analyser_exemples_entrainement_ultime(tache)
        
        for analyse in analyses:
            repetitions = analyse.get('repetitions', {})
            
            # Répétition horizontale - AMÉLIORÉE
            if 'repetition_horizontale' in repetitions:
                details = repetitions['repetition_horizontale']
                facteur = details.get('facteur', 2)
                motif_source = details.get('motif_source', test_input)
                return self._repetition_horizontale_ultime(test_input, facteur, tache, motif_source)
            
            # Répétition verticale - AMÉLIORÉE
            elif 'repetition_verticale' in repetitions:
                details = repetitions['repetition_verticale']
                facteur = details.get('facteur', 2)
                motif_source = details.get('motif_source', test_input)
                return self._repetition_verticale_ultime(test_input, facteur, tache, motif_source)
            
            # Motifs répétitifs - AMÉLIORÉE
            elif 'motifs_repetitifs' in repetitions:
                return self._appliquer_motifs_repetitifs_ultime(test_input, repetitions['motifs_repetitifs'], tache)
        
        return test_input

    def _repetition_horizontale_ultime(self, grille: List[List[int]], facteur: int, tache: TacheARC, motif_source: List[List[int]]) -> List[List[int]]:
        """Répétition horizontale ultime - AMÉLIORÉE"""
        # Analyser la taille de sortie attendue
        if tache.train:
            exemple = tache.train[0]
            output_grille = exemple.get('output', [])
            if output_grille:
                h_out = len(output_grille)
                
                # Utiliser le motif source pour la répétition
                resultat = []
                for _ in range(facteur):
                    resultat.extend(motif_source)
                
                # Ajuster à la taille exacte
                if len(resultat) > h_out:
                    resultat = resultat[:h_out]
                elif len(resultat) < h_out:
                    # Compléter avec des lignes vides
                    while len(resultat) < h_out:
                        resultat.append([0] * len(motif_source[0]) if motif_source else [0])
                
                return resultat
        
        return grille

    def _repetition_verticale_ultime(self, grille: List[List[int]], facteur: int, tache: TacheARC, motif_source: List[List[int]]) -> List[List[int]]:
        """Répétition verticale ultime - AMÉLIORÉE"""
        if not grille:
            return grille
        
        # Analyser la taille de sortie attendue
        if tache.train:
            exemple = tache.train[0]
            output_grille = exemple.get('output', [])
            if output_grille:
                w_out = len(output_grille[0])
                
                # Utiliser le motif source pour la répétition
                resultat = []
                for ligne in motif_source:
                    nouvelle_ligne = ligne * facteur
                    if len(nouvelle_ligne) > w_out:
                        nouvelle_ligne = nouvelle_ligne[:w_out]
                    elif len(nouvelle_ligne) < w_out:
                        nouvelle_ligne.extend([0] * (w_out - len(nouvelle_ligne)))
                    resultat.append(nouvelle_ligne)
                
                return resultat
        
        return grille

    def _appliquer_motifs_repetitifs_ultime(self, test_input: List[List[int]], motifs_info: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer des motifs répétitifs - AMÉLIORÉE"""
        motif = motifs_info.get('motif', [])
        if not motif:
            return test_input
        
        # Analyser la taille de sortie attendue
        if tache.train:
            exemple = tache.train[0]
            output_grille = exemple.get('output', [])
            if output_grille:
                h_out, w_out = len(output_grille), len(output_grille[0])
                
                # Créer une grille avec le motif répété
                resultat = []
                for y in range(h_out):
                    ligne = []
                    for x in range(w_out):
                        # Calculer la position dans le motif
                        motif_y = y % len(motif)
                        motif_x = x % len(motif[0])
                        ligne.append(motif[motif_y][motif_x])
                    resultat.append(ligne)
                
                return resultat
        
        return test_input

    def _appliquer_symetrie_ultime(self, test_input: List[List[int]], pattern: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer une symétrie de manière ultime - AMÉLIORÉE"""
        analyses = self._analyser_exemples_entrainement_ultime(tache)
        
        for analyse in analyses:
            symetries = analyse.get('symetries', {})
            if symetries:
                # Prendre la symétrie avec la plus haute confiance
                symetrie_principale = max(symetries.items(), key=lambda x: x[1])
                symetrie_type = symetrie_principale[0]
                
                test_array = np.array(test_input)
                
                if symetrie_type == 'horizontale':
                    return np.flipud(test_array).tolist()
                elif symetrie_type == 'verticale':
                    return np.fliplr(test_array).tolist()
                elif symetrie_type == 'diagonale':
                    return np.fliplr(np.flipud(test_array)).tolist()
        
        return test_input

    def _appliquer_transformation_ultime(self, test_input: List[List[int]], pattern: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer une transformation de manière ultime - AMÉLIORÉE"""
        analyses = self._analyser_exemples_entrainement_ultime(tache)
        
        for analyse in analyses:
            transformations = analyse.get('transformations_valeurs', {})
            mappings = transformations.get('mappings', {})
            
            if mappings:
                # Appliquer tous les mappings cohérents
                resultat = []
                for ligne in test_input:
                    nouvelle_ligne = []
                    for val in ligne:
                        nouvelle_val = mappings.get(val, val)
                        nouvelle_ligne.append(nouvelle_val)
                    resultat.append(nouvelle_ligne)
                
                return resultat
        
        return test_input

    def _appliquer_rotation_ultime(self, test_input: List[List[int]], pattern: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer une rotation de manière ultime - AMÉLIORÉE"""
        analyses = self._analyser_exemples_entrainement_ultime(tache)
        
        for analyse in analyses:
            rotations = analyse.get('rotations', {})
            if rotations:
                rotation_principale = max(rotations.items(), key=lambda x: x[1])
                rotation_type = rotation_principale[0]
                
                test_array = np.array(test_input)
                
                if rotation_type == 'rotation_90':
                    return np.rot90(test_array, 1).tolist()
                elif rotation_type == 'rotation_180':
                    return np.rot90(test_array, 2).tolist()
                elif rotation_type == 'rotation_270':
                    return np.rot90(test_array, 3).tolist()
        
        return test_input

    def _appliquer_pattern_imbrique_ultime(self, test_input: List[List[int]], pattern: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer un pattern imbriqué de manière ultime - AMÉLIORÉE"""
        analyses = self._analyser_exemples_entrainement_ultime(tache)
        
        for analyse in analyses:
            patterns_imbriques = analyse.get('patterns_imbriques', {})
            
            if 'remplissage' in patterns_imbriques:
                return self._appliquer_remplissage_ultime(test_input, patterns_imbriques['remplissage'], tache)
        
        return test_input

    def _appliquer_remplissage_ultime(self, test_input: List[List[int]], remplissage_info: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer un remplissage de manière ultime - AMÉLIORÉE"""
        zones_remplies = remplissage_info.get('zones_remplies', [])
        
        if not zones_remplies:
            return test_input
        
        # Analyser la taille de sortie attendue
        if tache.train:
            exemple = tache.train[0]
            output_grille = exemple.get('output', [])
            if output_grille:
                h_out, w_out = len(output_grille), len(output_grille[0])
                
                # Créer une grille de la taille attendue
                resultat = [[0 for _ in range(w_out)] for _ in range(h_out)]
                
                # Copier le test_input
                for y in range(min(len(test_input), h_out)):
                    for x in range(min(len(test_input[0]), w_out)):
                        resultat[y][x] = test_input[y][x]
                
                # Appliquer le remplissage
                for y, x, val in zones_remplies:
                    if y < h_out and x < w_out:
                        resultat[y][x] = val
                
                return resultat
        
        return test_input

    def _appliquer_logique_conditionnelle_ultime(self, test_input: List[List[int]], pattern: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer une logique conditionnelle de manière ultime - AMÉLIORÉE"""
        analyses = self._analyser_exemples_entrainement_ultime(tache)
        
        for analyse in analyses:
            logique = analyse.get('logique_conditionnelle', {})
            
            if 'conditions_position' in logique:
                return self._appliquer_conditions_position_ultime(test_input, logique['conditions_position'], tache)
        
        return test_input

    def _appliquer_conditions_position_ultime(self, test_input: List[List[int]], conditions: Dict, tache: TacheARC) -> List[List[int]]:
        """Appliquer des conditions de position de manière ultime - AMÉLIORÉE"""
        # Analyser la taille de sortie attendue
        if tache.train:
            exemple = tache.train[0]
            output_grille = exemple.get('output', [])
            if output_grille:
                h_out, w_out = len(output_grille), len(output_grille[0])
                
                # Créer une grille de la taille attendue
                resultat = [[0 for _ in range(w_out)] for _ in range(h_out)]
                
                # Copier le test_input
                for y in range(min(len(test_input), h_out)):
                    for x in range(min(len(test_input[0]), w_out)):
                        resultat[y][x] = test_input[y][x]
                
                return resultat
        
        return test_input

    def _appliquer_fallback_ultime(self, test_input: List[List[int]], tache: TacheARC) -> List[List[int]]:
        """Fallback ultime - AMÉLIORÉE"""
        # Analyser les transformations de valeurs même si pas de pattern dominant
        analyses = self._analyser_exemples_entrainement_ultime(tache)
        
        for analyse in analyses:
            transformations = analyse.get('transformations_valeurs', {})
            mappings = transformations.get('mappings', {})
            
            if mappings:
                # Appliquer les transformations
                resultat = []
                for ligne in test_input:
                    nouvelle_ligne = []
                    for val in ligne:
                        nouvelle_val = mappings.get(val, val)
                        nouvelle_ligne.append(nouvelle_val)
                    resultat.append(nouvelle_ligne)
                
                return resultat
        
        return test_input

    def _calculer_confiance_ultime(self, pattern: Dict, analyses: List[Dict[str, Any]]) -> float:
        """Calculer la confiance de manière ultime - AMÉLIORÉE"""
        confiance_base = pattern.get('confiance', 0.0)
        
        # Bonus pour la cohérence entre les analyses
        if len(analyses) > 1:
            coherence = self._calculer_coherence_analyses_ultime(analyses)
            confiance_base += coherence * 0.3
        
        # Bonus pour la complexité du pattern
        complexite = self._calculer_complexite_pattern_ultime(pattern)
        confiance_base += complexite * 0.2
        
        return min(1.0, confiance_base)

    def _calculer_coherence_analyses_ultime(self, analyses: List[Dict[str, Any]]) -> float:
        """Calculer la cohérence entre les analyses - AMÉLIORÉE"""
        if len(analyses) < 2:
            return 0.5
        
        # Comparer les types de patterns dominants
        types_patterns = []
        for analyse in analyses:
            pattern_dominant = analyse.get('pattern_dominant', {})
            pattern_type = pattern_dominant.get('type', 'inconnu')
            types_patterns.append(pattern_type)
        
        # Calculer la similarité
        similarites = []
        for i in range(len(types_patterns)):
            for j in range(i + 1, len(types_patterns)):
                if types_patterns[i] == types_patterns[j]:
                    similarites.append(1.0)
                else:
                    similarites.append(0.0)
        
        return np.mean(similarites) if similarites else 0.0

    def _calculer_complexite_pattern_ultime(self, pattern: Dict) -> float:
        """Calculer la complexité du pattern - AMÉLIORÉE"""
        pattern_type = pattern.get('type', 'fallback')
        
        complexites = {
            'fallback': 0.1,
            'symetrie': 0.3,
            'rotation': 0.4,
            'repetition': 0.5,
            'transformation': 0.6,
            'imbrique': 0.7,
            'logique': 0.8
        }
        
        return complexites.get(pattern_type, 0.1)

def main():
    """Test du solveur ultime V6"""
    print("🔧 TEST SOLVEUR ARC ULTIME V6")
    print("=" * 50)
    
    # Créer une tâche de test complexe
    tache_test = TacheARC(
        tache_id="test_complexe",
        train=[
            {
                'input': [[1, 2], [3, 4]],
                'output': [[2, 1], [4, 3]]
            },
            {
                'input': [[0, 1], [2, 3]],
                'output': [[1, 0], [3, 2]]
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
    solveur = SolveurARCUltimeV6()
    resultat = solveur.resoudre_tache(tache_test)
    
    print(f"Solution: {resultat['solution']}")
    print(f"Confiance: {resultat['confiance']:.2f}")
    print(f"Méthode: {resultat['methode']}")

if __name__ == "__main__":
    main()
