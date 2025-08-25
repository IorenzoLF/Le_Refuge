#!/usr/bin/env python3
"""
Solveur pour le puzzle 00576224 - Expansion par motif en damier
Pattern : Chaque cellule est répétée 3 fois horizontalement et verticalement
"""

import json

def solveur_puzzle_00576224(input_grid):
    """
    Pattern: Alternance normale/inversée avec répétition
    - Lignes paires: version normale répétée 3x
    - Lignes impaires: version inversée répétée 3x
    """
    if not input_grid or len(input_grid) != 2 or len(input_grid[0]) != 2:
        return input_grid

    output_grid = []

    for output_row in range(6):  # 6 lignes de sortie
        # Déterminer quelle ligne d'input utiliser
        input_row_idx = output_row % 2  # 0, 1, 0, 1, 0, 1
        input_row = input_grid[input_row_idx]

        # Déterminer si on doit inverser
        should_invert = (output_row % 4 >= 2)  # Lignes 2,3,6,7,... mais dans 0-5: 2,3

        if should_invert:
            # Version inversée
            inverted_row = list(reversed(input_row))
            repeated_row = inverted_row * 3
        else:
            # Version normale
            repeated_row = input_row * 3

        output_grid.append(repeated_row)

    return output_grid

def tester_solveur():
    print("Test du solveur pour puzzle 00576224")
    print("=" * 40)

    try:
        with open("ARC-AGI-2-main/data/training/00576224.json", 'r') as f:
            puzzle_data = json.load(f)

        success_count = 0

        for i, exemple in enumerate(puzzle_data['train'], 1):
            input_grid = exemple['input']
            output_attendu = exemple['output']

            # Appliquer notre solveur
            prediction = solveur_puzzle_00576224(input_grid)

            # Debug: afficher les prédictions
            print(f"  Prediction {len(prediction)}x{len(prediction[0]) if prediction else 0}:")
            if prediction:
                for row in prediction:
                    print(f"    {''.join([str(x) for x in row])}")

            print(f"  Attendu {len(output_attendu)}x{len(output_attendu[0])}:")
            for row in output_attendu:
                print(f"    {''.join([str(x) for x in row])}")

            # Vérifier si c'est correct
            is_correct = (prediction == output_attendu)

            print(f"Exemple {i}: {'SUCCES' if is_correct else 'ECHEC'}")

            if is_correct:
                success_count += 1

        print(f"Score: {success_count}/{len(puzzle_data['train'])}")

        if success_count == len(puzzle_data['train']):
            print("Parfait ! Le pattern d'expansion par motif est valide.")
            return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

if __name__ == "__main__":
    tester_solveur()
