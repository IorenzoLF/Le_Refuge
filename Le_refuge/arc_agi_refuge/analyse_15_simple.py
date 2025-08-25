#!/usr/bin/env python3
"""
ANALYSE DETAILLEE PUZZLE 15
0692e18c - comprendre la transformation
"""

import json

def analyse_simple():
    print("ANALYSE DETAILLEE PUZZLE 15")
    print("Comprendre la transformation 3x3 -> 9x9")

    try:
        with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("Fichier non trouve")
        return

    # Premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("INPUT (3x3):")
    for i, row in enumerate(input_grid):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "."
            elif cell == 6:
                row_str += "D"
            else:
                row_str += "?"
        print(f"  {i}: {row_str}")

    print("OUTPUT (9x9):")
    for i, row in enumerate(output_grid):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "."
            elif cell == 6:
                row_str += "D"
            else:
                row_str += "?"
        print(f"  {i}: {row_str}")

    # Analyser les positions
    print("POSITIONS COLOREES:")
    positions_input = []
    for i in range(3):
        for j in range(3):
            if input_grid[i][j] != 0:
                positions_input.append((i, j))
                print(f"Input: ({i},{j})")

    positions_output = []
    for i in range(9):
        for j in range(9):
            if output_grid[i][j] != 0:
                positions_output.append((i, j))

    print(f"Output: {len(positions_output)} positions")

    # Analyser par blocs 3x3
    print("PATTERN PAR BLOC:")
    for bloc_x in range(3):
        for bloc_y in range(3):
            if input_grid[bloc_x][bloc_y] != 0:
                positions_bloc = []
                for dx in range(3):
                    for dy in range(3):
                        out_x = bloc_x * 3 + dx
                        out_y = bloc_y * 3 + dy
                        if output_grid[out_x][out_y] != 0:
                            positions_bloc.append((dx, dy))
                print(f"Input ({bloc_x},{bloc_y}) -> Pattern: {positions_bloc}")

if __name__ == "__main__":
    analyse_simple()
