#!/usr/bin/env python3
"""
🔍 ANALYSE EXEMPLE 2 PUZZLE 5
"""

import json

def analyser():
    print("🔍 ANALYSE EXEMPLE 2 PUZZLE 5")

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    exemple = puzzle_data['train'][1]  # Exemple 2
    input_grid = exemple['input']
    output_attendu = exemple['output']

    print(f"Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_attendu)}x{len(output_attendu[0])}")

    print("\nINPUT:")
    for row in input_grid:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
        print(f"  {row_str}")

    print("\nOUTPUT ATTENDU:")
    for row in output_attendu:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 2:
                row_str += "🟢"
        print(f"  {row_str}")

    # Tester notre pattern
    solution = appliquer_pattern(input_grid)

    print("\nSOLUTION ACTUELLE:")
    for row in solution:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 2:
                row_str += "🟢"
        print(f"  {row_str}")

    # Comparer
    is_correct = solution == output_attendu
    print(f"\n✅ SUCCÈS: {is_correct}")

    if not is_correct:
        print("❌ ANALYSE DES DIFFÉRENCES:")
        for i in range(len(output_attendu)):
            if solution[i] != output_attendu[i]:
                print(f"  Ligne {i}: {solution[i]} != {output_attendu[i]}")

def appliquer_pattern(grid):
    """Appliquer le pattern actuel"""
    rows_input = len(grid)
    rows_output = 9
    cols = len(grid[0])

    solution = [[0 for _ in range(cols)] for _ in range(rows_output)]

    for i in range(rows_output):
        for j in range(cols):
            input_i = i % rows_input
            if grid[input_i][j] != 0:
                solution[i][j] = 2

    return solution

if __name__ == "__main__":
    analyser()
