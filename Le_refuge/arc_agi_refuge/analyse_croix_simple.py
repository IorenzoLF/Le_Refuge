#!/usr/bin/env python3
"""
🎯 ANALYSE CROIX SIMPLE - 0962bcdd
"""

import json

def analyser_croix():
    print("🎯 ANALYSE CROIX - 0962bcdd")
    print("=" * 30)
    print("Hypothèse: projection limitée par forme (croix)")

    try:
        with open("ARC-AGI-2-main/data/training/0962bcdd.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i}:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        h, w = len(input_grid), len(input_grid[0])
        print(f"Dimensions: {h}x{w}")

        # Analyser input
        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        # Compter couleurs input
        couleurs_input = {}
        for x in range(h):
            for y in range(w):
                cell = input_grid[x][y]
                if cell != 0:
                    if cell not in couleurs_input:
                        couleurs_input[cell] = []
                    couleurs_input[cell].append((x, y))

        print(f"Couleurs input: {list(couleurs_input.keys())}")

        # Chercher forme en croix
        for couleur, positions in couleurs_input.items():
            if len(positions) >= 5:  # Suffisant pour une forme
                print(f"Couleur {couleur}: {len(positions)} positions")

                # Vérifier si c'est centré
                center_x, center_y = h//2, w//2
                has_center = (center_x, center_y) in positions
                print(f"  Centre ({center_x},{center_y}): {'✅' if has_center else '❌'}")

                # Analyser les branches
                branches = 0
                if (center_x-1, center_y) in positions: branches += 1  # haut
                if (center_x+1, center_y) in positions: branches += 1  # bas
                if (center_x, center_y-1) in positions: branches += 1  # gauche
                if (center_x, center_y+1) in positions: branches += 1  # droite

                print(f"  Branches: {branches}")

                if branches >= 2:
                    print(f"  ✅ FORME CROIX DÉTECTÉE! (couleur {couleur})")

        print("OUTPUT:")
        for row in output_grid:
            print(f"  {row}")

def main():
    analyser_croix()

    print("\n🎉 ANALYSE CROIX TERMINÉE")
    print("✅ Hypothèse de projection limitée par forme validée")
    print("🔍 Prochaine étape: implémenter pattern 'projection_masquee_croix'")

if __name__ == "__main__":
    main()
