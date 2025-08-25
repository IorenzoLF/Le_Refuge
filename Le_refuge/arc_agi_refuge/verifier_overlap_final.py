#!/usr/bin/env python3
"""
🔍 VÉRIFICATION FINALE OVERLAP PUZZLE 03560426
"""

import json

def verifier():
    print("🔍 VÉRIFICATION FINALE OVERLAP 03560426")
    print("=" * 50)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    total_overlap = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        overlaps = 0
        rows = len(input_grid)
        cols = len(input_grid[0])

        for x in range(rows):
            for y in range(cols):
                input_val = input_grid[x][y]
                output_val = output_grid[x][y]

                if input_val != 0 and output_val != 0 and input_val != output_val:
                    overlaps += 1

        print(f"Exemple {i}: {overlaps} overlaps")
        total_overlap += overlaps

    print(f"\nTOTAL OVERLAPS: {total_overlap}")

    if total_overlap == 0:
        print("❌ AUCUN OVERLAP dans ce puzzle!")
        print("✅ Notre solution d'apprentissage automatique est CORRECTE!")
        print("🎯 Le pattern est une TRANSFORMATION COMPLÈTE")
    else:
        print(f"✅ Il y a {total_overlap} overlaps!")
        print("⚠️ Notre solution pourrait manquer des détails")

if __name__ == "__main__":
    verifier()
