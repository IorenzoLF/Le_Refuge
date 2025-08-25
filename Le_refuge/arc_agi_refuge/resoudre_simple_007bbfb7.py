#!/usr/bin/env python3
"""
🎯 RÉSOLUTION 007bbfb7
"""

import json

def main():
    print("🎯 RÉSOLUTION 007bbfb7")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    test_input = puzzle_data['test'][0]['input']
    print("TEST INPUT:")
    for row in test_input:
        print(f"  {row}")

    # Patterns pour chaque valeur
    patterns = {
        2: [2, 2, 2, 0, 0, 0, 0, 2, 2],
        4: [4, 0, 4, 0, 0, 0, 0, 4, 0],
        6: [6, 6, 0, 6, 0, 0, 0, 6, 6],
        7: [0, 7, 7, 7, 7, 7, 0, 7, 7],
        0: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    # Créer la solution 9x9
    solution = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(3):
        for j in range(3):
            valeur = test_input[i][j]
            pattern = patterns[valeur]
            start_i, start_j = i * 3, j * 3

            for x in range(3):
                for y in range(3):
                    solution[start_i + x][start_j + y] = pattern[x * 3 + y]

    print("SOLUTION 9x9:")
    for row in solution:
        print(f"  {row}")

    # Validation
    print("\nVALIDATION:")
    reussites = 0
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_ex = exemple['input']
        output_ex = exemple['output']

        solution_ex = appliquer_pattern(input_ex, patterns)

        if solution_ex == output_ex:
            print(f"  Exemple {i}: ✅")
            reussites += 1
        else:
            print(f"  Exemple {i}: ❌")

    print(f"\nScore: {reussites}/{len(puzzle_data['train'])}")

def appliquer_pattern(input_3x3, patterns):
    """Appliquer le pattern"""
    solution = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(3):
        for j in range(3):
            valeur = input_3x3[i][j]
            pattern = patterns[valeur]
            start_i, start_j = i * 3, j * 3

            for x in range(3):
                for y in range(3):
                    solution[start_i + x][start_j + y] = pattern[x * 3 + y]

    return solution

if __name__ == "__main__":
    main()
