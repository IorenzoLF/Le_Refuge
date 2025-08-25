#!/usr/bin/env python3
"""
🔍 EXPLORATION SIMPLE PERSPECTIVE BLOC
"""

import json

def explorer_bloc():
    print("🔍 EXPLORATION PERSPECTIVE BLOC")

    try:
        with open("data/training/007bbfb7.json", 'r') as f:
            puzzle_data = json.load(f)

        # Analyser premier exemple
        exemple = puzzle_data['train'][0]
        input_grid = exemple['input']
        output_grid = exemple['output']

        print("INPUT 3x3:")
        for row in input_grid:
            print(f"  {row}")

        print("\nANALYSE PAR ZONE:")
        for i in range(3):
            for j in range(3):
                valeur = input_grid[i][j]
                start_i, start_j = i * 3, j * 3

                zone = []
                for x in range(3):
                    for y in range(3):
                        zone.append(output_grid[start_i + x][start_j + y])

                print(f"Pos ({i},{j})={valeur} -> {zone}")

                if valeur == 0:
                    if all(cell == 0 for cell in zone):
                        print("  ✅ 0 -> zone vide")
                    else:
                        print("  ❌ 0 -> zone non vide")
                else:
                    print(f"  🎨 Pattern pour {valeur}")

        # Construire patterns
        print("\nPATTERNS PAR COULEUR:")
        patterns = {}

        for exemple in puzzle_data['train']:
            input_grid = exemple['input']
            output_grid = exemple['output']

            for i in range(3):
                for j in range(3):
                    valeur = input_grid[i][j]
                    if valeur != 0:
                        start_i, start_j = i * 3, j * 3
                        pattern = []
                        for x in range(3):
                            for y in range(3):
                                pattern.append(output_grid[start_i + x][start_j + y])

                        if valeur not in patterns:
                            patterns[valeur] = pattern

        for couleur in sorted(patterns.keys()):
            print(f"  {couleur}: {patterns[couleur]}")

    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    explorer_bloc()
