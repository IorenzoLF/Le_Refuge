#!/usr/bin/env python3
"""
🎯 RÉSOLUTION 00576224
"""

import json

def resoudre_00576224():
    print("🎯 RÉSOLUTION 00576224")

    with open("data/training/00576224.json", 'r') as f:
        puzzle_data = json.load(f)

    test_input = puzzle_data['test'][0]['input']
    print("TEST INPUT:")
    for row in test_input:
        print(f"  {row}")

    # Appliquer pattern expansion diagonale
    a, b = test_input[0][0], test_input[0][1]
    c, d = test_input[1][0], test_input[1][1]

    print(f"Valeurs: a={a}, b={b}, c={c}, d={d}")

    solution = [
        [a, b, a, b, a, b],
        [c, d, c, d, c, d],
        [b, a, b, a, b, a],
        [d, c, d, c, d, c],
        [a, b, a, b, a, b],
        [c, d, c, d, c, d]
    ]

    print("SOLUTION 6x6:")
    for row in solution:
        print(f"  {row}")

    # Validation avec exemples
    print("\nVALIDATION:")

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_ex = exemple['input']
        output_ex = exemple['output']

        solution_ex = appliquer_expansion(input_ex)

        if solution_ex == output_ex:
            print(f"  Exemple {i}: ✅")
        else:
            print(f"  Exemple {i}: ❌")

def appliquer_expansion(input_2x2):
    """Applique l'expansion diagonale"""
    a, b = input_2x2[0][0], input_2x2[0][1]
    c, d = input_2x2[1][0], input_2x2[1][1]

    return [
        [a, b, a, b, a, b],
        [c, d, c, d, c, d],
        [b, a, b, a, b, a],
        [d, c, d, c, d, c],
        [a, b, a, b, a, b],
        [c, d, c, d, c, d]
    ]

if __name__ == "__main__":
    resoudre_00576224()
