#!/usr/bin/env python3
"""
🎯 RÉSOLUTION FINALE 007bbfb7 - APPROCHE BLOC
"""

import json

def resoudre_007bbfb7():
    print("🎯 RÉSOLUTION 007bbfb7 - APPROCHE BLOC")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    # Extraire patterns
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

    print("PATTERNS:")
    for couleur in sorted(patterns.keys()):
        print(f"  {couleur}: {patterns[couleur]}")

    # Test
    test_input = puzzle_data['test'][0]['input']
    print("\nTEST INPUT:")
    for row in test_input:
        print(f"  {row}")

    # Solution
    solution = appliquer_bloc(test_input, patterns)
    print("\nSOLUTION:")
    for row in solution:
        print(f"  {row}")

    # Validation
    print("\nVALIDATION:")
    reussites = 0
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_ex = exemple['input']
        output_ex = exemple['output']
        solution_ex = appliquer_bloc(input_ex, patterns)

        if solution_ex == output_ex:
            print(f"  Exemple {i}: ✅")
            reussites += 1
        else:
            print(f"  Exemple {i}: ❌")

    print(f"Score: {reussites}/5")

    if reussites == 5:
        print("🎉 SUCCÈS! 100%")

        # Sauvegarder
        submission = {"007bbfb7": solution}
        with open("submission_007bbfb7_finale.json", 'w') as f:
            json.dump(submission, f, indent=2)
        print("Sauvegardé!")

def appliquer_bloc(input_3x3, patterns):
    """Appliquer l'approche bloc"""
    solution = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(3):
        for j in range(3):
            valeur = input_3x3[i][j]
            start_i, start_j = i * 3, j * 3

            if valeur == 0:
                pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            else:
                pattern = patterns.get(valeur, [valeur] * 9)

            for x in range(3):
                for y in range(3):
                    solution[start_i + x][start_j + y] = pattern[x * 3 + y]

    return solution

if __name__ == "__main__":
    resoudre_007bbfb7()
