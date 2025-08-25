#!/usr/bin/env python3
"""
🔍 ANALYSE SIMPLE PATTERN 007bbfb7
"""

import json

def analyser_007bbfb7():
    print("🔍 ANALYSE PATTERN 007bbfb7")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser chaque exemple
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i}:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        print("OUTPUT (premières lignes):")
        for j in range(min(3, len(output_grid))):
            print(f"  {output_grid[j]}")

        # Analyser les zones 3x3
        print("ZONES 3x3:")
        for x in range(3):
            for y in range(3):
                input_val = input_grid[x][y]
                start_i, start_j = x * 3, y * 3
                zone = []
                for i in range(3):
                    for j in range(3):
                        zone.append(output_grid[start_i + i][start_j + j])

                print(f"  Pos ({x},{y})={input_val} -> {zone}")

    # Analyser test
    print("\nTEST:")
    test_input = puzzle_data['test'][0]['input']
    print("TEST INPUT:")
    for row in test_input:
        print(f"  {row}")

if __name__ == "__main__":
    analyser_007bbfb7()
