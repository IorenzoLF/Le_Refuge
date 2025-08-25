#!/usr/bin/env python3
"""
🎯 ANALYSE FINALE PREMIER PUZZLE - 00576224
"""

import json

def main():
    print("🎯 ANALYSE FINALE 00576224")

    with open("data/training/00576224.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"Training examples: {len(puzzle_data['train'])}")
    print(f"Test examples: {len(puzzle_data['test'])}")

    # Analyser les exemples
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i}:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_grid)}x{len(output_grid[0])}")

        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        print("OUTPUT:")
        for row in output_grid:
            print(f"  {row}")

        # Analyser les changements
        changements = 0
        for x in range(len(input_grid)):
            for y in range(len(input_grid[0])):
                if input_grid[x][y] != output_grid[x][y]:
                    changements += 1
                    print(f"  Change ({x},{y}): {input_grid[x][y]} -> {output_grid[x][y]}")

        print(f"Changements: {changements}")

    # Analyser le test
    print("\nTEST:")
    test_input = puzzle_data['test'][0]['input']
    print(f"Test dimensions: {len(test_input)}x{len(test_input[0])}")

    print("TEST INPUT:")
    for row in test_input:
        print(f"  {row}")

    print("\n🎯 ANALYSE TERMINEE")
    print("Le pattern semble etre: changement de valeurs specifiques")

if __name__ == "__main__":
    main()
