#!/usr/bin/env python3
"""
PUZZLE 17 RAPIDE - 070dd51e
Analyse simple pour identifier le pattern
"""

import json

def puzzle_17_simple():
    print("PUZZLE 17 RAPIDE - 070dd51e")

    try:
        with open("ARC-AGI-2-main/data/training/070dd51e.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("Fichier non trouve")
        return

    print(f"Exemples: {len(puzzle_data['train'])}")

    # Premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print(f"Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_grid)}x{len(output_grid[0])}")

    # Pixels
    pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
    pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)
    print(f"Pixels: {pixels_input} -> {pixels_output}")

    # Couleurs
    couleurs_input = set(cell for row in input_grid for cell in row if cell != 0)
    couleurs_output = set(cell for row in output_grid for cell in row if cell != 0)
    print(f"Couleurs: {sorted(couleurs_input)} -> {sorted(couleurs_output)}")

    print("INPUT:")
    for i, row in enumerate(input_grid):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "."
            elif cell == 1:
                row_str += "R"
            elif cell == 2:
                row_str += "G"
            elif cell == 3:
                row_str += "B"
            elif cell == 4:
                row_str += "Y"
            else:
                row_str += "?"
        print(f"  {i}: {row_str}")

    print("OUTPUT:")
    for i, row in enumerate(output_grid):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "."
            elif cell == 1:
                row_str += "R"
            elif cell == 2:
                row_str += "G"
            elif cell == 3:
                row_str += "B"
            elif cell == 4:
                row_str += "Y"
            else:
                row_str += "?"
        print(f"  {i}: {row_str}")

    # Analyser tous les exemples
    print("ANALYSE TOUS EXEMPLES:")
    for i, exemple in enumerate(puzzle_data['train'], 1):
        inp = exemple['input']
        out = exemple['output']

        pix_in = sum(1 for row in inp for cell in row if cell != 0)
        pix_out = sum(1 for row in out for cell in row if cell != 0)

        print(f"  Exemple {i}: {pix_in} -> {pix_out} pixels")

if __name__ == "__main__":
    puzzle_17_simple()
