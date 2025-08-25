#!/usr/bin/env python3
"""
🔍 ANALYSE SIMPLE PUZZLE 3 - 009d5c81
"""

import json

def analyser_009d5c81():
    print("🔍 ANALYSE PUZZLE 3 - 009d5c81")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"Training: {len(puzzle_data['train'])} examples")
    print(f"Test: {len(puzzle_data['test'])} examples")

    # Analyser les exemples
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i}:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        print(f"Dimensions: {h_in}x{w_in} -> {h_out}x{w_out}")

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
        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        print("OUTPUT:")
        for row in output_grid:
            print(f"  {row}")

        # Compter changements
        changements = 0
        for x in range(h_in):
            for y in range(w_in):
                if input_grid[x][y] != output_grid[x][y]:
                    changements += 1

        print(f"Changements: {changements}")

    # Test
    print("\nTEST:")
    test_input = puzzle_data['test'][0]['input']
    h_test, w_test = len(test_input), len(test_input[0])

    print(f"Test dimensions: {h_test}x{w_test}")

    couleurs_test = set()
    for row in test_input:
        for cell in row:
            if cell != 0:
                couleurs_test.add(cell)

    print(f"Couleurs test: {sorted(couleurs_test)}")

    print("TEST INPUT:")
    for row in test_input:
        print(f"  {row}")

if __name__ == "__main__":
    analyser_009d5c81()
