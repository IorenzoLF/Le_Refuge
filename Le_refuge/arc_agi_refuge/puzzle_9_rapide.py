#!/usr/bin/env python3
"""
🎯 PUZZLE 9 - ANALYSE RAPIDE
"""

import json
import time

def analyse_rapide():
    debut = time.time()
    print("🚀 PUZZLE 9 - ANALYSE RAPIDE")
    print("=" * 30)

    with open("data/training/0520fde7.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"Exemples: {len(puzzle_data['train'])}")

    # Premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print(f"Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_grid)}x{len(output_grid[0])}")

    # Compter pixels
    pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
    pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)

    print(f"Pixels: {pixels_input} -> {pixels_output}")

    # Couleurs
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

    # Overlaps (comparer seulement la zone commune)
    overlaps = 0
    min_rows = min(len(input_grid), len(output_grid))
    min_cols = min(len(input_grid[0]), len(output_grid[0]))

    for i in range(min_rows):
        for j in range(min_cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]
            if input_val != 0 and output_val != 0 and input_val != output_val:
                overlaps += 1

    print(f"Overlaps: {overlaps}")

    fin = time.time()
    duree = fin - debut
    print(".2f")
    print("✅ ANALYSE TERMINEE")

    return duree

if __name__ == "__main__":
    analyse_rapide()