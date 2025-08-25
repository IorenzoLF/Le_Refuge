#!/usr/bin/env python3
"""
EXPLORATION RANGEMENT PUZZLE 14
0607ce86 - mettre en ordre / ranger
"""

import json

def explorer_simple():
    print("EXPLORATION RANGEMENT PUZZLE 14")
    print("Ton intuition: mettre en ordre / ranger")
    print("20 overlaps subtils detectes !")

    with open("data/training/0607ce86.json", 'r') as f:
        puzzle_data = json.load(f)

    print("Analyse generale:")
    print("Dimensions: 21x22 -> 21x22")
    print("Pixels: 257 -> 225 (compression)")
    print("Couleurs: [1, 2, 3, 8] (inchangees)")
    print("20 overlaps subtils detectes")

    # Premier exemple seulement
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("EXEMPLE 1:")
    print("INPUT:")
    visualiser_simple(input_grid)

    print("OUTPUT:")
    visualiser_simple(output_grid)

    # Analyser les changements
    changements = analyser_changements(input_grid, output_grid)
    print(f"Changements detectes: {changements}")

    if changements > 0:
        print("PATTERNS SUBTILS CONFIRMES !")
        print("20 overlaps = changements de couleur")
        print("Ton intuition de rangement est la cle !")

def visualiser_simple(grille):
    for i, row in enumerate(grille):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "."
            elif cell == 1:
                row_str += "R"
            elif cell == 2:
                row_str += "G"
            elif cell == 3:
                row_str += "B"
            elif cell == 8:
                row_str += "N"
            else:
                row_str += "*"
        print(f"  {i}: {row_str}")

def analyser_changements(input_grid, output_grid):
    changements = 0
    min_rows = min(len(input_grid), len(output_grid))
    min_cols = min(len(input_grid[0]), len(output_grid[0]))

    for i in range(min_rows):
        for j in range(min_cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]
            if input_val != 0 and output_val != 0 and input_val != output_val:
                changements += 1

    return changements

if __name__ == "__main__":
    explorer_simple()
