#!/usr/bin/env python3
"""
🔍 MINIMAL TEST 009d5c81
"""

import json

def minimal():
    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    test_input = puzzle_data['test'][0]['input']

    # Positions 1
    positions_1 = []
    for i in range(14):
        for j in range(14):
            if test_input[i][j] == 1:
                positions_1.append((i, j))

    print(f"Positions 1: {sorted(positions_1)}")

    # Résoudre avec couleur 2 (comme exemples 3 et 5)
    solution = [[0 for _ in range(14)] for _ in range(14)]
    for x in range(14):
        for y in range(14):
            if test_input[x][y] == 8:
                solution[x][y] = 2

    submission = {"009d5c81": solution}
    with open("submission_009d5c81_minimal.json", 'w') as f:
        json.dump(submission, f, indent=2)
    print("Solution sauvegardée!")

if __name__ == "__main__":
    minimal()