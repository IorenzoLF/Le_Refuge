#!/usr/bin/env python3
"""
🌊 ANALYSE ONDE - 05269061
"""

import json
from collections import Counter

def analyser_onde():
    print("🌊 ANALYSE ONDE - 05269061")
    print("=" * 40)
    print("Description: onde de 3 couleurs")
    print("Direction: haut-gauche → bas-droite")

    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i}:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        print("Input:")
        for row in input_grid:
            print(f"  {row}")

        print("Output:")
        for row in output_grid:
            print(f"  {row}")

        # Analyser couleurs
        couleurs_input = Counter()
        couleurs_output = Counter()

        for row in input_grid:
            for cell in row:
                if cell != 0:
                    couleurs_input[cell] += 1

        for row in output_grid:
            for cell in row:
                if cell != 0:
                    couleurs_output[cell] += 1

        print(f"Couleurs input: {dict(couleurs_input)}")
        print(f"Couleurs output: {dict(couleurs_output)}")

        # Analyser séquence d'onde
        couleurs_sequence = []
        for row in input_grid:
            for cell in row:
                if cell != 0 and cell not in couleurs_sequence:
                    couleurs_sequence.append(cell)

        print(f"Sequence couleurs: {couleurs_sequence}")

        # Vérifier pattern onde
        h, w = len(output_grid), len(output_grid[0])
        correspondances = 0
        total_positions = 0

        print("\nVERIFICATION PATTERN ONDE:")
        for i in range(h):
            for j in range(w):
                if output_grid[i][j] != 0:
                    total_positions += 1
                    distance = i + j
                    couleur_theorique = couleurs_sequence[distance % len(couleurs_sequence)]
                    couleur_reelle = output_grid[i][j]

                    match = "✅" if couleur_reelle == couleur_theorique else "❌"
                    if i <= 2 and j <= 2:  # Afficher seulement quelques positions
                        print(f"  ({i},{j}): {couleur_reelle} vs {couleur_theorique} {match}")

                    if couleur_reelle == couleur_theorique:
                        correspondances += 1

        if total_positions > 0:
            taux = correspondances / total_positions * 100
            print(".1f")

            if taux > 80:
                print("✅ HYPOTHESE ONDE CONFIRMEE")
            else:
                print("❌ HYPOTHESE ONDE NON CONFIRMEE")

def main():
    analyser_onde()

if __name__ == "__main__":
    main()
