#!/usr/bin/env python3
"""
🔍 ANALYSE OVERLAP PUZZLE 03560426
"""

import json

def analyser():
    print("🔍 ANALYSE OVERLAP PUZZLE 03560426")
    print("=" * 50)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser le premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("EXEMPLE 1:")
    print("INPUT:")
    visualiser(input_grid)

    print("OUTPUT:")
    visualiser(output_grid)

    # Analyser les différences
    print("DIFFERENCES:")
    analyser_differences(input_grid, output_grid)

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

def analyser_differences(input_grid, output_grid):
    zones_overlap = []
    zones_ajoutees = []

    rows = len(input_grid)
    cols = len(input_grid[0])

    for i in range(rows):
        for j in range(cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]

            if input_val != output_val:
                if input_val == 0 and output_val != 0:
                    zones_ajoutees.append((i, j, output_val))
                    print(f"  AJOUT: ({i},{j}) = {output_val}")
                elif input_val != 0 and output_val == 0:
                    print(f"  SUPPR: ({i},{j}) = {input_val}")
                else:
                    zones_overlap.append((i, j, input_val, output_val))
                    print(f"  OVERLAP: ({i},{j}) = {input_val}->{output_val}")

    print(f"\nZones d'overlap: {len(zones_overlap)}")
    print(f"Zones ajoutées: {len(zones_ajoutees)}")

if __name__ == "__main__":
    analyser()