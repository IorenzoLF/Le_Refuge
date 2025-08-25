#!/usr/bin/env python3
"""
COMPARAISON EXEMPLES PUZZLE 15
0692e18c - comprendre les variations
"""

import json

def comparer_simple():
    print("COMPARAISON EXEMPLES PUZZLE 15")
    print("Pourquoi 1/3 succes ? Variations du pattern")

    try:
        with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("Fichier non trouve")
        return

    # Comparer chaque exemple
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"EXEMPLE {i} - ANALYSE:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Positions input
        positions_input = []
        for x in range(3):
            for y in range(3):
                if input_grid[x][y] != 0:
                    positions_input.append((x, y))

        print(f"  Input positions: {positions_input}")

        # Patterns par bloc
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
                    print(f"  Bloc ({bloc_x},{bloc_y}) -> {positions_bloc}")

if __name__ == "__main__":
    comparer_simple()
