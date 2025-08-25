#!/usr/bin/env python3
"""
🔍 ANALYSE POSITIONS PUZZLE 4
"""

import json

def analyser():
    print("🔍 ANALYSE POSITIONS PUZZLE 4")

    with open("data/training/00dbd492.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n📐 EXEMPLE {i}")

        input_grid = exemple['input']
        output_grid = exemple['output']

        nouvelles_bleu = []
        nouvelles_noir = []

        for x in range(len(output_grid)):
            for y in range(len(output_grid[0])):
                if input_grid[x][y] == 0 and output_grid[x][y] != 0:
                    if output_grid[x][y] == 3:
                        nouvelles_bleu.append((x, y))
                    elif output_grid[x][y] == 8:
                        nouvelles_noir.append((x, y))

        print(f"   🔵 Pixels bleus: {len(nouvelles_bleu)}")
        print(f"   ⚫ Pixels noirs: {len(nouvelles_noir)}")

        if nouvelles_bleu:
            print(f"   Positions bleues: {nouvelles_bleu}")

        if nouvelles_noir:
            print(f"   Positions noires: {nouvelles_noir}")

if __name__ == "__main__":
    analyser()
