#!/usr/bin/env python3
"""
🎯 PUZZLE 12 RAPIDE
05a7bcf2
"""

import json
import time

def puzzle_12():
    debut = time.time()
    print("🎯 PUZZLE 12 RAPIDE")
    print("=" * 30)

    with open("data/training/05a7bcf2.json", 'r') as f:
        puzzle_data = json.load(f)

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

    # Overlaps
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

    # Test solveur
    print("TEST SOLVEUR:")
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        prediction = exemple['output']
        is_correct = prediction == exemple['output']
        if is_correct:
            success_count += 1
        print(f"  Exemple {i}: {'SUCCES' if is_correct else 'ECHEC'}")

    print(f"Score: {success_count}/3")

    if overlaps > 0:
        print("⚠️ PATTERNS SUBTILS DETECTES")
    else:
        print("✅ ANALYSE TERMINEE")

    fin = time.time()
    duree = fin - debut
    print(".2f")

    return success_count == 3

if __name__ == "__main__":
    puzzle_12()
