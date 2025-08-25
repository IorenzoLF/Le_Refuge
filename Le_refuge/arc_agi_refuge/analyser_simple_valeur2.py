#!/usr/bin/env python3
"""
🔍 ANALYSE SIMPLE VALEUR 2
"""

import json

def analyser_valeur2():
    print("🔍 ANALYSE VALEUR 2")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"\nEXEMPLE {i}:")
        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        # Positions avec 2
        positions_2 = []
        for x in range(3):
            for y in range(3):
                if input_grid[x][y] == 2:
                    start_i, start_j = x * 3, y * 3
                    zone = []
                    for a in range(3):
                        for b in range(3):
                            zone.append(output_grid[start_i + a][start_j + b])
                    positions_2.append((x, y, zone))

        if positions_2:
            print("POSITIONS 2:")
            for x, y, zone in positions_2:
                print(f"  ({x},{y}): {zone}")

            # Vérifier cohérence
            zones = [z for _, _, z in positions_2]
            unique_zones = []
            for z in zones:
                if z not in unique_zones:
                    unique_zones.append(z)

            if len(unique_zones) == 1:
                print("  ✅ Pattern cohérent")
            else:
                print(f"  ⚠️  {len(unique_zones)} patterns différents")
        else:
            print("  Aucun 2")

if __name__ == "__main__":
    analyser_valeur2()
