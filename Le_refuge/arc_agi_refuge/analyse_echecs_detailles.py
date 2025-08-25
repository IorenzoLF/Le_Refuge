#!/usr/bin/env python3
"""
Analyse détaillée des échecs du solveur ARC
Identifie les patterns manquants et les axes d'amélioration
"""

import json
import os
import random
from typing import Dict, List, Any, Tuple, Set
from solveur_transparent_arc import SolveurTransparentARC, ResultatAnalyse
import numpy as np

class AnalyseurEchecsARC:
    """Analyse détaillée des puzzles non résolus"""

    def __init__(self):
        self.solveur = SolveurTransparentARC()
        self.echecs_analyses = []
        self.patterns_manquants = {}

    def charger_puzzles_echoues(self, n_puzzles: int = 10) -> List[str]:
        """Charge une liste de puzzles qui risquent d'échouer"""
        # Puzzles connus pour être difficiles ou différents
        puzzles_difficiles = [
            "7fe24cdd",  # Puzzle qui a échoué dans le test précédent
            "1e0a9b12",  # Puzzle complexe
            "0a1d4ef5",  # Compression géométrique
            "0520fde7",  # Projection vaisseau
            "1190e5a7",  # Compression par sections
            "0b148d64",  # Filtrage couleur
            "0934a4d8",  # Puzzle complexe
            "195ba7dc",  # Compression horizontale
            "0c9aba6e",  # Compression densité
            "00d62c1b"   # Zones fermées
        ]

        # Compléter avec des puzzles aléatoires si nécessaire
        dataset_path = "ARC-AGI-2-main/data/training"
        if os.path.exists(dataset_path):
            all_puzzles = [f.replace('.json', '') for f in os.listdir(dataset_path) if f.endswith('.json')]
            puzzles_restants = [p for p in all_puzzles if p not in puzzles_difficiles]
            random.shuffle(puzzles_restants)
            puzzles_difficiles.extend(puzzles_restants[:n_puzzles - len(puzzles_difficiles)])

        return puzzles_difficiles[:n_puzzles]

    def analyser_echec_detaille(self, puzzle_id: str, puzzle_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse détaillée d'un échec"""
        print(f"\n🔍 ANALYSE DETAILLEE ECHEC: {puzzle_id}")
        print("=" * (30 + len(puzzle_id)))

        # Analyse du puzzle
        resultat = self.solveur.analyser_puzzle_complet(puzzle_id)

        # Récupération des vraies solutions
        solutions_reelles = []
        for exemple in puzzle_data.get('train', []):
            if 'output' in exemple:
                solutions_reelles.append(exemple['output'])

        # Analyse des différences
        analyse_diff = self.analyser_differences(
            resultat.solution_predite if resultat else None,
            solutions_reelles
        )

        # Détection de patterns potentiels manquants
        patterns_potentiels = self.detecter_patterns_manquants(puzzle_data)

        # Analyse de complexité
        complexite = self.analyser_complexite(puzzle_data)

        resultat_analyse = {
            'puzzle_id': puzzle_id,
            'pattern_detecte': resultat.pattern_type if resultat else None,
            'confiance': resultat.confiance if resultat else 0,
            'reussi': resultat and resultat.pattern_trouve,
            'differences': analyse_diff,
            'patterns_potentiels': patterns_potentiels,
            'complexite': complexite,
            'recommandations': self.generer_recommandations(resultat, analyse_diff, patterns_potentiels)
        }

        self.echecs_analyses.append(resultat_analyse)
        return resultat_analyse

    def analyser_differences(self, prediction: List[List[int]], vraies_solutions: List[List[List[int]]]) -> Dict[str, Any]:
        """Analyse les différences entre prédiction et solutions réelles"""
        if not prediction or not vraies_solutions:
            return {'type': 'donnees_manquantes'}

        differences = []

        for i, vraie_solution in enumerate(vraies_solutions[:2]):  # Analyser 2 exemples max
            if isinstance(vraie_solution, list) and len(vraie_solution) > 0:
                h_pred, w_pred = len(prediction), len(prediction[0])
                h_vrai, w_vrai = len(vraie_solution), len(vraie_solution[0])

                diff_taille = {
                    'prediction': f"{h_pred}x{w_pred}",
                    'reel': f"{h_vrai}x{w_vrai}",
                    'difference': f"{abs(h_pred-h_vrai)}x{abs(w_pred-w_vrai)}"
                }

                # Analyse des couleurs
                couleurs_pred = set(cell for row in prediction for cell in row)
                couleurs_vrai = set(cell for row in vraie_solution for cell in row)

                diff_couleurs = {
                    'prediction': sorted(list(couleurs_pred)),
                    'reel': sorted(list(couleurs_vrai)),
                    'uniques_pred': couleurs_pred - couleurs_vrai,
                    'uniques_reel': couleurs_vrai - couleurs_pred
                }

                # Similarité structurelle
                similarite = self.calculer_similarite(prediction, vraie_solution)

                differences.append({
                    'exemple': i + 1,
                    'taille': diff_taille,
                    'couleurs': diff_couleurs,
                    'similarite': similarite
                })

        return {
            'type': 'analyse_difference',
            'details': differences
        }

    def calculer_similarite(self, grille1: List[List[int]], grille2: List[List[int]]) -> float:
        """Calcule la similarité entre deux grilles"""
        if not grille1 or not grille2:
            return 0.0

        h1, w1 = len(grille1), len(grille1[0])
        h2, w2 = len(grille2), len(grille2[0])

        # Utiliser la plus petite taille commune
        h_min, w_min = min(h1, h2), min(w1, w2)

        matching_cells = 0
        total_cells = h_min * w_min

        for i in range(h_min):
            for j in range(w_min):
                if grille1[i][j] == grille2[i][j]:
                    matching_cells += 1

        return matching_cells / total_cells if total_cells > 0 else 0

    def detecter_patterns_manquants(self, puzzle_data: Dict[str, Any]) -> List[str]:
        """Détecte les patterns potentiels non couverts par le solveur actuel"""
        patterns_potentiels = []

        # Analyse des exemples d'entraînement
        for exemple in puzzle_data.get('train', []):
            if 'input' in exemple and 'output' in exemple:
                input_grid = exemple['input']
                output_grid = exemple['output']

                # Pattern: Symétrie
                if self.detecter_symetrie(input_grid, output_grid):
                    patterns_potentiels.append('symetrie')

                # Pattern: Rotation
                if self.detecter_rotation(input_grid, output_grid):
                    patterns_potentiels.append('rotation')

                # Pattern: Déplacement d'objets
                if self.detecter_deplacement_objets(input_grid, output_grid):
                    patterns_potentiels.append('deplacement_objets')

                # Pattern: Remplissage complexe
                if self.detecter_remplissage_complexe(input_grid, output_grid):
                    patterns_potentiels.append('remplissage_complexe')

                # Pattern: Compression avancée
                if self.detecter_compression_avancee(input_grid, output_grid):
                    patterns_potentiels.append('compression_avancee')

        return list(set(patterns_potentiels))  # Éliminer les doublons

    def detecter_symetrie(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Détecte si le pattern implique de la symétrie"""
        if len(input_grid) != len(output_grid) or len(input_grid[0]) != len(output_grid[0]):
            return False

        h, w = len(input_grid), len(input_grid[0])

        # Vérifier symétrie horizontale
        sym_h = all(input_grid[i][j] == output_grid[h-1-i][j] for i in range(h) for j in range(w))
        # Vérifier symétrie verticale
        sym_v = all(input_grid[i][j] == output_grid[i][w-1-j] for i in range(h) for j in range(w))

        return sym_h or sym_v

    def detecter_rotation(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Détecte si le pattern implique une rotation"""
        if len(input_grid) != len(output_grid) or len(input_grid[0]) != len(output_grid[0]):
            return False

        h, w = len(input_grid), len(input_grid[0])

        # Vérifier rotation 90°
        rot_90 = all(input_grid[i][j] == output_grid[j][h-1-i] for i in range(h) for j in range(w))
        # Vérifier rotation 180°
        rot_180 = all(input_grid[i][j] == output_grid[h-1-i][w-1-j] for i in range(h) for j in range(w))

        return rot_90 or rot_180

    def detecter_deplacement_objets(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Détecte si le pattern implique un déplacement d'objets"""
        # Compter les objets (groupes de cellules non-zéro)
        def compter_objets(grille):
            objets = 0
            visites = set()
            h, w = len(grille), len(grille[0])

            for i in range(h):
                for j in range(w):
                    if grille[i][j] != 0 and (i, j) not in visites:
                        # DFS pour marquer l'objet
                        stack = [(i, j)]
                        objets += 1
                        while stack:
                            x, y = stack.pop()
                            if (x, y) not in visites:
                                visites.add((x, y))
                                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                    nx, ny = x + dx, y + dy
                                    if (0 <= nx < h and 0 <= ny < w and
                                        grille[nx][ny] != 0 and (nx, ny) not in visites):
                                        stack.append((nx, ny))
            return objets

        objets_input = compter_objets(input_grid)
        objets_output = compter_objets(output_grid)

        # Si même nombre d'objets mais positions différentes
        return objets_input == objets_output and objets_input > 0

    def detecter_remplissage_complexe(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Détecte les patterns de remplissage complexes"""
        zeros_input = sum(row.count(0) for row in input_grid)
        zeros_output = sum(row.count(0) for row in output_grid)

        # Si beaucoup de zéros sont remplis avec des couleurs différentes
        if zeros_input > zeros_output:
            couleurs_output = set(cell for row in output_grid for cell in row if cell != 0)
            couleurs_input = set(cell for row in input_grid for cell in row if cell != 0)
            nouvelles_couleurs = couleurs_output - couleurs_input
            return len(nouvelles_couleurs) > 1

        return False

    def detecter_compression_avancee(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Détecte les patterns de compression avancés"""
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        # Compression avec changement de structure
        if (h_out < h_in or w_out < w_in) and h_out > 0 and w_out > 0:
            # Vérifier si c'est plus qu'une simple réduction
            ratio_h = h_in / h_out
            ratio_w = w_in / w_out

            # Si ratios non entiers, c'est de la compression avancée
            return not (ratio_h.is_integer() and ratio_w.is_integer())

        return False

    def analyser_complexite(self, puzzle_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse la complexité d'un puzzle"""
        complexite = {
            'niveau': 'simple',
            'facteurs': []
        }

        train_examples = puzzle_data.get('train', [])

        # Taille des grilles
        tailles = []
        for exemple in train_examples:
            if 'input' in exemple:
                h, w = len(exemple['input']), len(exemple['input'][0])
                tailles.append((h, w))

        if tailles:
            taille_moyenne = np.mean([h * w for h, w in tailles])
            if taille_moyenne > 100:
                complexite['facteurs'].append('grille_large')
            if max(h for h, w in tailles) > 20 or max(w for h, w in tailles) > 20:
                complexite['facteurs'].append('dimension_eleve')

        # Nombre d'exemples
        if len(train_examples) > 5:
            complexite['facteurs'].append('plusieurs_exemples')

        # Variabilité des couleurs
        couleurs = set()
        for exemple in train_examples:
            if 'input' in exemple:
                couleurs.update(cell for row in exemple['input'] for cell in row)
            if 'output' in exemple:
                couleurs.update(cell for row in exemple['output'] for cell in row)

        if len(couleurs) > 5:
            complexite['facteurs'].append('couleurs_multiples')

        # Déterminer le niveau
        if len(complexite['facteurs']) >= 3:
            complexite['niveau'] = 'complexe'
        elif len(complexite['facteurs']) >= 1:
            complexite['niveau'] = 'moyen'
        else:
            complexite['niveau'] = 'simple'

        return complexite

    def generer_recommandations(self, resultat: ResultatAnalyse, differences: Dict, patterns_potentiels: List[str]) -> List[str]:
        """Génère des recommandations d'amélioration"""
        recommandations = []

        if not resultat or not resultat.pattern_trouve:
            recommandations.append("Implementer la detection de pattern de base")

        if differences.get('type') == 'analyse_difference':
            for diff in differences.get('details', []):
                if diff.get('taille', {}).get('difference') != '0x0':
                    recommandations.append("Ameliorer la gestion des dimensions dynamiques")
                if diff.get('couleurs', {}).get('uniques_reel'):
                    recommandations.append("Ajouter la gestion de nouvelles couleurs")

        for pattern in patterns_potentiels:
            if pattern == 'symetrie':
                recommandations.append("Implementer pattern de symetrie horizontale/verticale")
            elif pattern == 'rotation':
                recommandations.append("Implementer pattern de rotation 90°/180°")
            elif pattern == 'deplacement_objets':
                recommandations.append("Implementer pattern de deplacement d'objets")
            elif pattern == 'remplissage_complexe':
                recommandations.append("Ameliorer la detection de remplissage complexe")
            elif pattern == 'compression_avancee':
                recommandations.append("Implementer pattern de compression avancee")

        return list(set(recommandations))  # Éliminer les doublons

    def executer_analyse_complete(self):
        """Exécute l'analyse complète des échecs"""
        print("🔍 ANALYSE DETAILLEE DES ECHECS ARC")
        print("=" * 40)

        # Charger les puzzles difficiles
        puzzles_echoues = self.charger_puzzles_echoues(15)

        # Analyser chaque échec
        for puzzle_id in puzzles_echoues:
            try:
                # Charger les données du puzzle
                puzzle_path = f"ARC-AGI-2-main/data/training/{puzzle_id}.json"
                if os.path.exists(puzzle_path):
                    with open(puzzle_path, 'r') as f:
                        puzzle_data = json.load(f)

                    analyse = self.analyser_echec_detaille(puzzle_id, puzzle_data)

                    # Afficher un résumé
                    print(f"  {puzzle_id}: {'REUSSI' if analyse['reussi'] else 'ECHEC'}")
                    if analyse['patterns_potentiels']:
                        print(f"    Patterns potentiels: {analyse['patterns_potentiels']}")

            except Exception as e:
                print(f"  {puzzle_id}: ERREUR - {e}")

        # Générer le rapport final
        self.generer_rapport_analyse()

    def generer_rapport_analyse(self):
        """Génère un rapport complet de l'analyse"""
        print(f"\n📋 RAPPORT FINAL D'ANALYSE")
        print("=" * 30)

        total_analyses = len(self.echecs_analyses)
        reussis = sum(1 for a in self.echecs_analyses if a['reussi'])
        echoues = total_analyses - reussis

        print(f"Puzzles analyses: {total_analyses}")
        print(f"Reussis: {reussis} ({reussis/total_analyses*100:.1f}%)")
        print(f"Echoues: {echoues} ({echoues/total_analyses*100:.1f}%)")

        # Collecter tous les patterns potentiels
        tous_patterns = []
        for analyse in self.echecs_analyses:
            tous_patterns.extend(analyse.get('patterns_potentiels', []))

        patterns_counts = {}
        for pattern in tous_patterns:
            patterns_counts[pattern] = patterns_counts.get(pattern, 0) + 1

        print(f"\n🔍 PATTERNS POTENTIELS MANQUANTS:")
        for pattern, count in sorted(patterns_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {pattern}: {count} occurrences")

        # Recommandations globales
        print(f"\n💡 RECOMMANDATIONS GLOBALES:")
        recommandations_globales = set()
        for analyse in self.echecs_analyses:
            recommandations_globales.update(analyse.get('recommandations', []))

        for i, rec in enumerate(sorted(recommandations_globales), 1):
            print(f"  {i}. {rec}")

        # Évaluation finale
        print(f"\n🏆 EVALUATION FINALE:")
        if len(patterns_counts) > 0:
            print("Patterns manquants identifies - implementation recommandee")
        else:
            print("Couverture des patterns satisfaisante")

        score_patterns = min(len(patterns_counts) * 10, 100)  # 10% par pattern manquant max 100%
        print(f"Score patterns manquants: {score_patterns}%")

def main():
    """Fonction principale"""
    analyseur = AnalyseurEchecsARC()
    analyseur.executer_analyse_complete()

if __name__ == "__main__":
    main()
