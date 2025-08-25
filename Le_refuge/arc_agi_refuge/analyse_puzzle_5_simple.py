#!/usr/bin/env python3
"""
🎨 ANALYSE PUZZLE 5: 017c7c7b
"""

import json

def analyser():
    print("🎨 ANALYSE PUZZLE 5: 017c7c7b")
    print("=" * 50)

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"Exemples: {len(puzzle_data['train'])}")

    # Premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print(f"Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_grid)}x{len(output_grid[0])}")

    print("INPUT:")
    for row in input_grid:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
            elif cell == 2:
                row_str += "🟢"
            elif cell == 3:
                row_str += "🔵"
            else:
                row_str += "💎"
        print(f"  {row_str}")

    print("OUTPUT:")
    for row in output_grid:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
            elif cell == 2:
                row_str += "🟢"
            elif cell == 3:
                row_str += "🔵"
            else:
                row_str += "💎"
        print(f"  {row_str}")

    # Analyse
    pixels_input = compter_pixels(input_grid)
    pixels_output = compter_pixels(output_grid)

    print(f"Input pixels: {pixels_input}")
    print(f"Output pixels: {pixels_output}")

    couleurs_input = set()
    couleurs_output = set()

    for row in input_grid:
        for cell in row:
            if cell != 0:
                couleurs_input.add(cell)

    for row in output_grid:
        for cell in row:
            if cell != 0:
                couleurs_output.add(cell)

    print(f"Couleurs input: {sorted(couleurs_input)}")
    print(f"Couleurs output: {sorted(couleurs_output)}")

def compter_pixels(grille):
    compte = {}
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            couleur = grille[i][j]
            if couleur != 0:
                compte[couleur] = compte.get(couleur, 0) + 1
    return compte

if __name__ == "__main__":
    analyser()
