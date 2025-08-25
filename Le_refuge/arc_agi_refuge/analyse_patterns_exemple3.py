#!/usr/bin/env python3
"""
ANALYSE PATTERNS REELS EXEMPLE 3 PUZZLE 15
Decouvrir les vrais patterns pour l'exemple 3
"""

import json

def analyse_patterns_exemple3():
    print("ANALYSE PATTERNS REELS EXEMPLE 3")
    
    with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
        puzzle_data = json.load(f)
    
    exemple = puzzle_data['train'][2]
    input_grid = exemple['input']
    output_grid = exemple['output']
    
    positions_input = [(0, 0), (0, 1), (1, 2), (2, 2)]
    
    print("PATTERNS REELS POUR EXEMPLE 3:")
    
    for pos_x, pos_y in positions_input:
        positions_bloc = []
        for dx in range(3):
            for dy in range(3):
                out_x = pos_x * 3 + dx
                out_y = pos_y * 3 + dy
                if output_grid[out_x][out_y] != 0:
                    positions_bloc.append((dx, dy))
        
        print(f"Position ({pos_x},{pos_y}) -> Pattern reel: {positions_bloc}")
    
    # Comparer avec les patterns que j'utilise
    patterns_utilises = {
        (0, 0): [(0, 2), (1, 0), (1, 1), (2, 0), (2, 1)],
        (0, 1): [(0, 0), (0, 2), (2, 0), (2, 2)],
        (1, 2): [(0, 0), (0, 2), (2, 0), (2, 2)],
        (2, 2): [(0, 2), (1, 0), (1, 1), (2, 0), (2, 1)]
    }
    
    print("COMPARAISON AVEC PATTERNS UTILISES:")
    for pos in positions_input:
        pattern_reel = []
        for dx in range(3):
            for dy in range(3):
                out_x = pos[0] * 3 + dx
                out_y = pos[1] * 3 + dy
                if output_grid[out_x][out_y] != 0:
                    pattern_reel.append((dx, dy))
        
        pattern_utilise = patterns_utilises.get(pos, [])
        correspondance = set(pattern_reel) == set(pattern_utilise)
        
        print(f"  {pos}:")
        print(f"    Reel: {pattern_reel}")
        print(f"    Utilise: {pattern_utilise}")
        print(f"    Correspondance: {correspondance}")
    
    # Identifier les vrais patterns
    print("VRAIS PATTERNS POUR EXEMPLE 3:")
    vrais_patterns = {}
    
    for pos in positions_input:
        pattern_reel = []
        for dx in range(3):
            for dy in range(3):
                out_x = pos[0] * 3 + dx
                out_y = pos[1] * 3 + dy
                if output_grid[out_x][out_y] != 0:
                    pattern_reel.append((dx, dy))
        vrais_patterns[pos] = pattern_reel
        print(f"  {pos} -> {pattern_reel}")

if __name__ == "__main__":
    analyse_patterns_exemple3()
