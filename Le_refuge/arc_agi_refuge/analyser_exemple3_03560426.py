#!/usr/bin/env python3
"""
🔍 ANALYSE DÉTAILLÉE EXEMPLE 3 - LES 3 OVERLAPS
"""

import json

def analyser_exemple3():
    print("🔍 ANALYSE EXEMPLE 3 - LES 3 OVERLAPS")
    print("=" * 50)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser l'exemple 3
    exemple = puzzle_data['train'][2]  # Index 2 = exemple 3
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("EXEMPLE 3:")
    print("INPUT:")
    visualiser(input_grid)

    print("OUTPUT:")
    visualiser(output_grid)

    print("ANALYSE DES OVERLAPS:")
    analyser_overlaps(input_grid, output_grid)

def visualiser(grille):
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

def analyser_overlaps(input_grid, output_grid):
    overlaps = []
    rows = len(input_grid)
    cols = len(input_grid[0])

    for i in range(rows):
        for j in range(cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]

            if input_val != 0 and output_val != 0 and input_val != output_val:
                overlaps.append((i, j, input_val, output_val))

    print(f"Nombre d'overlaps: {len(overlaps)}")

    for i, j, old_color, new_color in overlaps:
        print(f"  OVERLAP ({i},{j}): {old_color} → {new_color}")

        # Analyser le contexte autour
        print("  Contexte 3x3:")
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    input_ctx = input_grid[ni][nj]
                    output_ctx = output_grid[ni][nj]
                    marker = "🎯" if di == 0 and dj == 0 else "   "
                    print(f"    {marker} ({ni},{nj}): {input_ctx} → {output_ctx}")

if __name__ == "__main__":
    analyser_exemple3()
