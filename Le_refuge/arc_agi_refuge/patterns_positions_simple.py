#!/usr/bin/env python3
"""
PATTERNS PAR POSITION PUZZLE 15
0692e18c - chaque position a son pattern
"""

import json

def patterns_positions_simple():
    print("PATTERNS PAR POSITION PUZZLE 15")
    print("Chaque position (x,y) a son propre pattern !")

    try:
        with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("Fichier non trouve")
        return

    # Analyser chaque position possible
    for pos_x in range(3):
        for pos_y in range(3):
            print(f"POSITION ({pos_x},{pos_y}):")

            patterns_trouves = []

            for i, exemple in enumerate(puzzle_data['train'], 1):
                input_grid = exemple['input']
                output_grid = exemple['output']

                # Verifier si cette position est coloree
                if input_grid[pos_x][pos_y] != 0:
                    pattern_bloc = []
                    for dx in range(3):
                        for dy in range(3):
                            out_x = pos_x * 3 + dx
                            out_y = pos_y * 3 + dy
                            if output_grid[out_x][out_y] != 0:
                                pattern_bloc.append((dx, dy))

                    patterns_trouves.append({
                        'exemple': i,
                        'pattern': pattern_bloc
                    })

                    print(f"  Exemple {i}: {pattern_bloc}")

            if not patterns_trouves:
                print("  Jamais utilisee")

if __name__ == "__main__":
    patterns_positions_simple()
