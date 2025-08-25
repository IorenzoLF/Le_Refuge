#!/usr/bin/env python3
"""
Audit de 200 puzzles représentatifs pour recadrage réaliste
"""

import json
import random
import os
from collections import defaultdict, Counter
from typing import List, Dict, Tuple, Set

class Auditeur200Puzzles:
    def __init__(self):
        self.puzzles_selectionnes = []
        self.analyse_resultats = {}
        self.patterns_manquants = defaultdict(int)

    def selectionner_200_puzzles(self) -> List[str]:
        """Sélectionner 200 puzzles représentatifs"""
        print("=== SELECTION DE 200 PUZZLES REPRÉSENTATIFS ===")

        # Lister tous les puzzles disponibles
        puzzles_disponibles = []
        for file in os.listdir('ARC-AGI-2-main/data/training'):
            if file.endswith('.json'):
                puzzles_disponibles.append(file[:-5])  # Enlever .json

        print(f"Total puzzles disponibles: {len(puzzles_disponibles)}")

        # Sélection stratifiée pour représentativité
        # 1. Prendre les 50 premiers (pour patterns basiques)
        premiers = puzzles_disponibles[:50]

        # 2. Prendre 50 du milieu (patterns intermédiaires)
        milieu_start = len(puzzles_disponibles) // 2 - 25
        milieu_end = len(puzzles_disponibles) // 2 + 25
        milieu = puzzles_disponibles[milieu_start:milieu_end]

        # 3. Prendre 50 de la fin (patterns complexes)
        derniers = puzzles_disponibles[-50:]

        # 4. Prendre 50 aléatoires pour diversité
        restants = puzzles_disponibles[50:-50]
        aleatoires = random.sample(restants, min(50, len(restants)))

        # Combiner et dédupliquer
        selection = list(set(premiers + milieu + derniers + aleatoires))
        # S'assurer d'avoir exactement 200 puzzles
        if len(selection) > 200:
            selection = selection[:200]
        elif len(selection) < 200:
            # Ajouter des puzzles restants si nécessaire
            restants_non_selectionnes = list(set(puzzles_disponibles) - set(selection))
            selection.extend(restants_non_selectionnes[:200-len(selection)])

        self.puzzles_selectionnes = selection
        print(f"Selection finale: {len(selection)} puzzles")

        # Distribution
        print("\nDistribution:")
        print(f"  Premiers: {len([p for p in selection if p in premiers])}")
        print(f"  Milieu: {len([p for p in selection if p in milieu])}")
        print(f"  Derniers: {len([p for p in selection if p in derniers])}")
        print(f"  Aleatoires: {len([p for p in selection if p in aleatoires])}")

        return selection

    def analyser_puzzle(self, puzzle_id: str) -> Dict:
        """Analyser un puzzle individuel"""
        try:
            with open(f'ARC-AGI-2-main/data/training/{puzzle_id}.json', 'r') as f:
                data = json.load(f)
        except Exception as e:
            return {'erreur': str(e)}

        analyse = {
            'puzzle_id': puzzle_id,
            'nb_examples': len(data['train']),
            'dimensions_input': [],
            'dimensions_output': [],
            'couleurs_input': set(),
            'couleurs_output': set(),
            'changement_dimensions': False,
            'changement_couleurs': False,
            'complexite_estimee': 0
        }

        # Analyser chaque exemple
        for exemple in data['train']:
            input_h, input_w = len(exemple['input']), len(exemple['input'][0]) if exemple['input'] else (0, 0)
            output_h, output_w = len(exemple['output']), len(exemple['output'][0]) if exemple['output'] else (0, 0)

            analyse['dimensions_input'].append((input_h, input_w))
            analyse['dimensions_output'].append((output_h, output_w))

            # Couleurs
            for row in exemple['input']:
                analyse['couleurs_input'].update(row)
            for row in exemple['output']:
                analyse['couleurs_output'].update(row)

        # Détecter changements
        if any(in_dim != out_dim for in_dim, out_dim in zip(analyse['dimensions_input'], analyse['dimensions_output'])):
            analyse['changement_dimensions'] = True

        if analyse['couleurs_output'] != analyse['couleurs_input']:
            analyse['changement_couleurs'] = True

        # Complexité estimée (facteur composite)
        nb_couleurs = len(analyse['couleurs_input'])
        taille_moyenne = sum(h*w for h,w in analyse['dimensions_input']) / len(analyse['dimensions_input'])
        analyse['complexite_estimee'] = nb_couleurs * taille_moyenne

        return analyse

    def classifier_patterns_manquants(self, analyse: Dict) -> List[str]:
        """Classifier les patterns potentiellement manquants"""
        patterns = []

        # Patterns de changement de dimensions
        if analyse['changement_dimensions']:
            dim_changes = []
            for in_dim, out_dim in zip(analyse['dimensions_input'], analyse['dimensions_output']):
                if in_dim != out_dim:
                    ratio_h = out_dim[0] / in_dim[0] if in_dim[0] > 0 else 0
                    ratio_w = out_dim[1] / in_dim[1] if in_dim[1] > 0 else 0
                    dim_changes.append((ratio_h, ratio_w))

            # Identifier type de changement
            if all(r[0] == r[1] for r in dim_changes):  # Même ratio H/W
                if dim_changes[0][0] < 1:  # Réduction
                    patterns.append('reduction_symetrique')
                else:  # Agrandissement
                    patterns.append('agrandissement_symetrique')
            else:
                patterns.append('changement_dimensions_asymetrique')

        # Patterns de transformation de couleurs
        if analyse['changement_couleurs']:
            couleurs_ajoutees = analyse['couleurs_output'] - analyse['couleurs_input']
            couleurs_enlevees = analyse['couleurs_input'] - analyse['couleurs_output']

            if couleurs_ajoutees and not couleurs_enlevees:
                patterns.append('ajout_couleurs')
            elif couleurs_enlevees and not couleurs_ajoutees:
                patterns.append('suppression_couleurs')
            else:
                patterns.append('remplacement_couleurs')

        # Patterns spatiaux complexes
        if not analyse['changement_dimensions'] and not analyse['changement_couleurs']:
            # Même dimensions, même couleurs = transformation spatiale pure
            patterns.append('transformation_spatiale_complexe')

        # Patterns de symétrie et rotation
        if analyse['nb_examples'] >= 3:  # Assez d'exemples pour détecter patterns
            patterns.extend(self.detecter_symetries_rotations(analyse))

        return patterns

    def detecter_symetries_rotations(self, analyse: Dict) -> List[str]:
        """Détecter patterns de symétrie et rotation (simplifié)"""
        # Version simplifiée - dans un vrai audit, on analyserais les grilles
        patterns = []

        # Patterns potentiels basés sur la complexité
        if analyse['complexite_estimee'] > 100:
            patterns.append('pattern_complexe_non_couvert')

        if len(analyse['couleurs_input']) > 5:
            patterns.append('gestion_couleurs_complexe')

        return patterns

    def executer_audit_complet(self):
        """Exécuter l'audit complet des 200 puzzles"""
        print("\n=== DÉBUT AUDIT 200 PUZZLES ===\n")

        # Sélection des puzzles
        puzzles = self.selectionner_200_puzzles()

        # Analyser chaque puzzle
        analyses = {}
        for i, puzzle_id in enumerate(puzzles, 1):
            print(f"Analyse {i:3d}/200: {puzzle_id}")
            analyse = self.analyser_puzzle(puzzle_id)
            analyses[puzzle_id] = analyse

            # Classifier patterns manquants
            patterns_manquants = self.classifier_patterns_manquants(analyse)
            for pattern in patterns_manquants:
                self.patterns_manquants[pattern] += 1

        self.analyse_resultats = analyses

        # Générer rapport
        self.generer_rapport_audit()

        return analyses

    def generer_rapport_audit(self):
        """Générer le rapport d'audit détaillé"""
        print("\n=== RAPPORT AUDIT 200 PUZZLES ===\n")

        # Statistiques générales
        total_analyses = len(self.analyse_resultats)
        changements_dimensions = sum(1 for a in self.analyse_resultats.values()
                                   if a.get('changement_dimensions', False))
        changements_couleurs = sum(1 for a in self.analyse_resultats.values()
                                 if a.get('changement_couleurs', False))

        print("STATISTIQUES GÉNÉRALES:")
        print(f"  Puzzles analysés: {total_analyses}")
        print(f"  Changements de dimensions: {changements_dimensions} ({changements_dimensions/total_analyses*100:.1f}%)")
        print(f"  Changements de couleurs: {changements_couleurs} ({changements_couleurs/total_analyses*100:.1f}%)")

        # Patterns manquants identifiés
        print(f"\nPATTERNS MANQUANTS IDENTIFIÉS ({len(self.patterns_manquants)} types):")
        print("-" * 50)

        for pattern, count in sorted(self.patterns_manquants.items(), key=lambda x: x[1], reverse=True):
            pourcentage = count / total_analyses * 100
            print("30")

        # Analyse par complexité
        print("\nANALYSE PAR COMPLEXITÉ:")
        complexites = [a['complexite_estimee'] for a in self.analyse_resultats.values() if 'complexite_estimee' in a]
        if complexites:
            print(".1f")
            print(".1f")
            print(".1f")

        # Recommandations
        print("\nRECOMMANDATIONS POUR RECADRAGE:")
        print("-" * 40)

        recommandations = []

        if changements_dimensions > total_analyses * 0.3:
            recommandations.append("PRIORITE: Implementer patterns de changement de dimensions")

        if changements_couleurs > total_analyses * 0.2:
            recommandations.append("PRIORITE: Ameliorer gestion des transformations de couleurs")

        if self.patterns_manquants['transformation_spatiale_complexe'] > total_analyses * 0.1:
            recommandations.append("PRIORITE: Developper patterns spatiaux complexes")

        for rec in recommandations:
            print(f"  • {rec}")

        # Plan d'action
        print("\nPLAN D'ACTION PROPOSÉ:")
        print("1. Phase 1 (Semaine 1): Implementer patterns de dimensions")
        print("2. Phase 2 (Semaine 2): Robustifier gestion couleurs")
        print("3. Phase 3 (Semaine 3): Developper patterns spatiaux")
        print("4. Phase 4 (Semaine 4): Tests et validation")

        # Sauvegarder résultats
        self.sauvegarder_resultats()

    def sauvegarder_resultats(self):
        """Sauvegarder les résultats de l'audit"""
        resultats = {
            'puzzles_analyses': self.analyse_resultats,
            'patterns_manquants': dict(self.patterns_manquants),
            'resume': {
                'total_analyses': len(self.analyse_resultats),
                'changements_dimensions': sum(1 for a in self.analyse_resultats.values() if a.get('changement_dimensions', False)),
                'changements_couleurs': sum(1 for a in self.analyse_resultats.values() if a.get('changement_couleurs', False))
            }
        }

        with open('resultats_audit_200_puzzles.json', 'w') as f:
            json.dump(resultats, f, indent=2)

        print("\nResultats sauvegardes: resultats_audit_200_puzzles.json")

if __name__ == "__main__":
    # Fixer la seed pour reproductibilité
    random.seed(42)

    auditeur = Auditeur200Puzzles()
    resultats = auditeur.executer_audit_complet()
