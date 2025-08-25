#!/usr/bin/env python3
"""
🔍 DEBUG EXEMPLE 4 APPROCHE BLOC
Trouver pourquoi l'exemple 4 échoue
"""

import json

def debug_exemple4():
    print("🔍 DEBUG EXEMPLE 4 BLOC")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    exemple4 = puzzle_data['train'][3]
    input4 = exemple4['input']
    output4 = exemple4['output']

    print("EXEMPLE 4:")
    print("INPUT:")
    for row in input4:
        print(f"  {row}")

    # Extraire patterns depuis TOUS les exemples
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
                    elif patterns[valeur] != pattern:
                        print(f"⚠️  Pattern différent pour {valeur}:")
                        print(f"   Ancien: {patterns[valeur]}")
                        print(f"   Nouveau: {pattern}")

    print("\nPATTERNS DISPONIBLES:")
    for couleur in sorted(patterns.keys()):
        print(f"  {couleur}: {patterns[couleur]}")

    # Simuler la reconstruction de l'exemple 4
    print("\nSIMULATION RECONSTRUCTION EXEMPLE 4:")
    solution = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(3):
        for j in range(3):
            valeur = input4[i][j]
            start_i, start_j = i * 3, j * 3

            if valeur == 0:
                pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            else:
                pattern = patterns.get(valeur, [valeur] * 9)

            print(f"Pos ({i},{j})={valeur} -> {pattern}")

            for x in range(3):
                for y in range(3):
                    solution[start_i + x][start_j + y] = pattern[x * 3 + y]

    print("\nSOLUTION GÉNÉRÉE:")
    for row in solution:
        print(f"  {row}")

    print("\nSOLUTION ATTENDUE:")
    for row in output4:
        print(f"  {row}")

    # Comparer
    print("\nCOMPARAISON:")
    differences = []
    for x in range(9):
        for y in range(9):
            if solution[x][y] != output4[x][y]:
                differences.append((x, y, solution[x][y], output4[x][y]))

    if differences:
        print(f"❌ {len(differences)} différences:")
        for x, y, gen, att in differences[:10]:  # Montrer les 10 premières
            print(f"  ({x},{y}): {gen} -> {att}")
    else:
        print("✅ Parfait!")

if __name__ == "__main__":
    debug_exemple4()
