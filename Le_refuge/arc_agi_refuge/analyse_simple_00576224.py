#!/usr/bin/env python3
"""
🎯 ANALYSE PREMIER PUZZLE - 00576224
"""

import json

def analyser_00576224():
    print("🎯 ANALYSE 00576224")

    try:
        with open("data/training/00576224.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    print(f"Exemples entrainement: {len(puzzle_data['train'])}")
    print(f"Exemples test: {len(puzzle_data['test'])}")

    # Analyser exemples
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        print(f"\nExemple {i}: {h_in}x{w_in} -> {h_out}x{w_out}")

        # Couleurs
        couleurs_in = set()
        couleurs_out = set()
        for row in input_grid:
            for cell in row:
                if cell != 0:
                    couleurs_in.add(cell)
        for row in output_grid:
            for cell in row:
                if cell != 0:
                    couleurs_out.add(cell)

        print(f"Couleurs: {sorted(couleurs_in)} -> {sorted(couleurs_out)}")

        # Afficher grilles
        print("Input:")
        for row in input_grid:
            print(f"  {row}")

        print("Output:")
        for row in output_grid:
            print(f"  {row}")

    # Analyser test
    print("\nTEST:")
    test_input = puzzle_data['test'][0]['input']
    h_test, w_test = len(test_input), len(test_input[0])

    print(f"Test: {h_test}x{w_test}")

    couleurs_test = set()
    for row in test_input:
        for cell in row:
            if cell != 0:
                couleurs_test.add(cell)

    print(f"Couleurs test: {sorted(couleurs_test)}")

    print("Test input:")
    for row in test_input:
        print(f"  {row}")

    print("\n🎯 ANALYSE TERMINEE")
    print("Prochaine etape: comprendre le pattern")

if __name__ == "__main__":
    analyser_00576224()
