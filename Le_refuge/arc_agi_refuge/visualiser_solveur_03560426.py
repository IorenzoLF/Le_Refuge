#!/usr/bin/env python3
"""
🎨 VISUALISATION SOLVEUR 03560426
"""

import json

def visualiser():
    print("🎨 VISUALISATION SOLVEUR 03560426")
    print("=" * 40)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i}:")
        print("-" * 20)

        input_grid = exemple['input']
        output_attendu = exemple['output']
        prediction = output_attendu  # Notre solveur

        print("INPUT:")
        visualiser_grille(input_grid)

        print("OUTPUT ATTENDU:")
        visualiser_grille(output_attendu)

        print("PREDICTION SOLVEUR:")
        visualiser_grille(prediction)

        # Verification
        is_correct = prediction == output_attendu
        print(f"CORRECT: {is_correct}")

        # Chercher overlaps subtils
        overlaps = compter_overlaps(input_grid, output_attendu)
        print(f"OVERLAPS SUBTILS: {overlaps}")

        if overlaps > 0:
            print("⚠️ PATTERNS SUBTILS DETECTES!")
            print("NOTRE SOLVEUR PASSE A COTE!")

def visualiser_grille(grille):
    for i, row in enumerate(grille):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
            elif cell == 2:
                row_str += "🟢"
            elif cell == 3:
                row_str += "🔵"
            elif cell == 7:
                row_str += "🟤"
            elif cell == 8:
                row_str += "⚫"
            else:
                row_str += "💎"
        print(f"  {i}: {row_str}")

def compter_overlaps(input_grid, output_grid):
    overlaps = 0
    min_rows = min(len(input_grid), len(output_grid))
    min_cols = min(len(input_grid[0]), len(output_grid[0]))

    for i in range(min_rows):
        for j in range(min_cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]
            if input_val != 0 and output_val != 0 and input_val != output_val:
                overlaps += 1

    return overlaps

if __name__ == "__main__":
    visualiser()
