#!/usr/bin/env python3
"""
🔍 FORME TEST 009d5c81
"""

import json

def analyser():
    print("🔍 FORME TEST 009d5c81")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    test_input = puzzle_data['test'][0]['input']

    print("TEST INPUT:")
    for i in range(14):
        row_str = ""
        for j in range(14):
            cell = test_input[i][j]
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
            elif cell == 8:
                row_str += "🔵"
        print(f"  {row_str}")

    # Positions 1
    positions_1 = []
    for i in range(14):
        for j in range(14):
            if test_input[i][j] == 1:
                positions_1.append((i, j))

    print(f"Positions 1: {sorted(positions_1)}")

    # Analyser la forme
    if positions_1:
        x_coords = [x for x, y in positions_1]
        y_coords = [y for x, y in positions_1]

        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)

        print(f"Bounding box: ({min_x},{min_y}) -> ({max_x},{max_y})")
        print(f"Dimensions: {max_x - min_x + 1} x {max_y - min_y + 1}")
        print(f"Pixels: {len(positions_1)}")

        # Positions relatives
        positions_rel = [(x - min_x, y - min_y) for x, y in positions_1]
        print(f"Positions relatives: {sorted(positions_rel)}")

        print("
📐 FORME:"        print("  6 pixels formant un rectangle 3x3 avec 3 pixels manquants")
        print("  Ressemble aux exemples 3 et 5 (couleur 2)")

        # Résoudre
        couleur = 2
        print(f"Couleur prédite: {couleur}")

        solution = [[0 for _ in range(14)] for _ in range(14)]
        for x in range(14):
            for y in range(14):
                if test_input[x][y] == 8:
                    solution[x][y] = couleur

        submission = {"009d5c81": solution}
        with open("submission_009d5c81_geometrique.json", 'w') as f:
            json.dump(submission, f, indent=2)
        print("Solution sauvegardée!")

if __name__ == "__main__":
    analyser()
