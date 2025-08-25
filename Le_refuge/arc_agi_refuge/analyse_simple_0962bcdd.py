#!/usr/bin/env python3
"""
📊 ANALYSE SIMPLE 0962bcdd
"""

import json

def main():
    print("📊 ANALYSE 0962bcdd")

    try:
        with open("ARC-AGI-2-main/data/training/0962bcdd.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"EXEMPLE {i}:")
        input_grid = exemple['input']

        # Positions
        positions = []
        for x in range(len(input_grid)):
            for y in range(len(input_grid[0])):
                if input_grid[x][y] != 0:
                    positions.append((x, y, input_grid[x][y]))

        print(f"Positions: {len(positions)}")
        for x, y, c in positions:
            print(f"  ({x},{y}): {c}")

        # Séparation en deux formes
        forme1 = [(x, y, c) for x, y, c in positions if x <= 4 and y <= 5]
        forme2 = [(x, y, c) for x, y, c in positions if x >= 7 and y >= 7]

        print(f"Forme 1 (haut-gauche): {len(forme1)}")
        print(f"Forme 2 (bas-droite): {len(forme2)}")

        if len(forme1) >= 3 and len(forme2) >= 3:
            print("✅ CROIX EN DEUX PARTIES IDENTIFIEE!")
        else:
            print("❌ Pas de séparation claire")

if __name__ == "__main__":
    main()
