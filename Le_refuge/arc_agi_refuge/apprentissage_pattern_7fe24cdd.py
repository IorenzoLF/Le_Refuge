#!/usr/bin/env python3
"""
Système d'apprentissage automatique simple pour le pattern 7fe24cdd
Analyse les exemples d'entraînement pour apprendre le mapping exact
"""

import json
from typing import Dict, List, Any, Tuple
from collections import defaultdict

class ApprentissagePattern7fe24cdd:
    """Apprentissage du mapping exact pour le pattern 7fe24cdd"""

    def __init__(self):
        self.mapping_positions = {}  # (i_input, j_input) -> [(i_output, j_output), ...]
        self.mapping_valeurs = defaultdict(list)  # valeur -> positions où elle apparaît
        self.exemples_analyses = 0

    def analyser_exemple(self, input_grid: List[List[int]], output_grid: List[List[int]]):
        """Analyse un exemple d'entraînement pour apprendre le mapping"""
        if len(input_grid) != 3 or len(input_grid[0]) != 3:
            return
        if len(output_grid) != 6 or len(output_grid[0]) != 6:
            return

        print(f"Analyse exemple {self.exemples_analyses + 1}...")

        # Pour chaque position non-zéro dans l'input
        for i in range(3):
            for j in range(3):
                valeur_input = input_grid[i][j]
                if valeur_input != 0:
                    # Trouver où cette valeur apparaît dans l'output
                    positions_output = []
                    for out_i in range(6):
                        for out_j in range(6):
                            if output_grid[out_i][out_j] == valeur_input:
                                positions_output.append((out_i, out_j))

                    # Enregistrer le mapping
                    key = (i, j)
                    if key not in self.mapping_positions:
                        self.mapping_positions[key] = []

                    # Ajouter les nouvelles positions (éviter les doublons)
                    for pos in positions_output:
                        if pos not in self.mapping_positions[key]:
                            self.mapping_positions[key].append(pos)

                    # Enregistrer les valeurs
                    self.mapping_valeurs[valeur_input].extend(positions_output)

        self.exemples_analyses += 1

    def apprendre_des_exemples(self, puzzle_data: Dict[str, Any]):
        """Apprendre de tous les exemples d'entraînement"""
        print("APPRENTISSAGE DU PATTERN 7fe24cdd")
        print("=" * 40)

        for i, exemple in enumerate(puzzle_data.get('train', [])):
            if 'input' in exemple and 'output' in exemple:
                self.analyser_exemple(exemple['input'], exemple['output'])

        print(f"Analyse terminée: {self.exemples_analyses} exemples traités")
        print(f"Mappings appris: {len(self.mapping_positions)} positions")

        # Afficher les mappings appris
        self.afficher_mappings()

    def afficher_mappings(self):
        """Affiche les mappings appris"""
        print("\nMAPPINGS APPRIS:")
        print("-" * 30)

        for (i, j), positions in sorted(self.mapping_positions.items()):
            valeur_typique = "?"
            # Trouver une valeur typique pour cette position
            for exemple in range(min(3, self.exemples_analyses)):
                try:
                    puzzle_path = f"ARC-AGI-2-main/data/training/7fe24cdd.json"
                    with open(puzzle_path, 'r') as f:
                        data = json.load(f)
                    if exemple < len(data['train']):
                        valeur_typique = str(data['train'][exemple]['input'][i][j])
                        break
                except:
                    pass

            positions_str = ", ".join([f"({x},{y})" for x, y in positions])
            print(f"Position ({i},{j}) [val:{valeur_typique}] → {positions_str}")

    def generer_prediction(self, input_grid: List[List[int]]) -> List[List[int]]:
        """Génère une prédiction basée sur les mappings appris"""
        if not self.mapping_positions:
            return input_grid  # Fallback

        output = [[0 for _ in range(6)] for _ in range(6)]

        # Appliquer les mappings
        for (i, j), positions_output in self.mapping_positions.items():
            if i < len(input_grid) and j < len(input_grid[0]):
                valeur = input_grid[i][j]
                if valeur != 0:
                    # Placer la valeur dans toutes les positions apprises
                    for out_i, out_j in positions_output:
                        if 0 <= out_i < 6 and 0 <= out_j < 6:
                            output[out_i][out_j] = valeur

        return output

    def evaluer_precision(self, puzzle_data: Dict[str, Any]):
        """Évalue la précision du modèle appris"""
        print("\nÉVALUATION DE PRÉCISION:")
        print("-" * 30)

        total_correct = 0
        total_positions = 0

        for exemple in puzzle_data.get('train', []):
            if 'input' in exemple and 'output' in exemple:
                prediction = self.generer_prediction(exemple['input'])
                expected = exemple['output']

                # Calculer la similarité
                correct = 0
                for i in range(6):
                    for j in range(6):
                        total_positions += 1
                        if prediction[i][j] == expected[i][j]:
                            correct += 1
                            total_correct += 1

                similarity = correct / (6 * 6) * 100
                print(f"Exemple: {similarity:.1f}% de précision")

        if total_positions > 0:
            precision_globale = total_correct / total_positions * 100
            print(f"Précision globale: {precision_globale:.1f}%")

        return total_correct / total_positions if total_positions > 0 else 0

def main():
    """Fonction principale d'apprentissage"""
    print("SYSTÈME D'APPRENTISSAGE POUR PATTERN 7fe24cdd")
    print("=" * 50)

    # Charger les données du puzzle
    puzzle_path = "ARC-AGI-2-main/data/training/7fe24cdd.json"

    try:
        with open(puzzle_path, 'r') as f:
            puzzle_data = json.load(f)

        # Créer et entraîner le modèle
        apprentissage = ApprentissagePattern7fe24cdd()
        apprentissage.apprendre_des_exemples(puzzle_data)

        # Évaluer la précision
        precision = apprentissage.evaluer_precision(puzzle_data)

        # Tester sur le test input
        if puzzle_data.get('test'):
            test_input = puzzle_data['test'][0]['input']
            print(f"\nTEST INPUT:")
            for row in test_input:
                print('  ' + ' '.join(map(str, row)))

            prediction = apprentissage.generer_prediction(test_input)
            print(f"\nPRÉDICTION APPRENTISSAGE:")
            for row in prediction:
                print('  ' + ' '.join(map(str, row)))

        print(f"\nRÉSULTAT FINAL:")
        if precision > 80:
            print("✅ MODÈLE APPRIS AVEC SUCCÈS!")
        elif precision > 50:
            print("🤔 MODÈLE PARTIELLEMENT APPRIS")
        else:
            print("❌ APPRENTISSAGE INSUFFISANT")

    except FileNotFoundError:
        print(f"❌ Fichier non trouvé: {puzzle_path}")
        print("Vérifiez que les données ARC-AGI sont présentes")
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()
