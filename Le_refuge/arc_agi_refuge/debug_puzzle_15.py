#!/usr/bin/env python3
"""
DEBUG PUZZLE 15 - comprendre les echecs
"""

import json

def debug_puzzle_15():
    print("DEBUG PUZZLE 15")
    print("Analyser les echecs en detail")
    
    with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
        puzzle_data = json.load(f)
    
    # Analyser exemple 2 en detail
    exemple = puzzle_data['train'][1]  # Exemple 2 (index 1)
    input_grid = exemple['input']
    output_attendu = exemple['output']
    
    print("EXEMPLE 2 - ANALYSE DETAILLEE")
    print("Input:")
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
    
    print("Output attendu:")
    for i, row in enumerate(output_attendu):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "."
            elif cell == 6:
                row_str += "D"
            else:
                row_str += "?"
        print(f"  {i}: {row_str}")
    
    # Positions input colorées
    positions_input = []
    for i in range(3):
        for j in range(3):
            if input_grid[i][j] != 0:
                positions_input.append((i, j))
    
    print(f"Positions input colorées: {positions_input}")
    
    # Analyser chaque bloc
    for bloc_x in range(3):
        for bloc_y in range(3):
            if input_grid[bloc_x][bloc_y] != 0:
                positions_attendues = []
                for dx in range(3):
                    for dy in range(3):
                        out_x = bloc_x * 3 + dx
                        out_y = bloc_y * 3 + dy
                        if output_attendu[out_x][out_y] != 0:
                            positions_attendues.append((dx, dy))
                print(f"Bloc ({bloc_x},{bloc_y}) -> attendu: {positions_attendues}")

if __name__ == "__main__":
    debug_puzzle_15()
