#!/usr/bin/env python3
"""
🔍 ANALYSE SIMPLE TEST 009d5c81
"""

import json

def analyser_test():
    print("🔍 ANALYSE TEST 009d5c81")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    print("CONFIGURATIONS ENTRAÎNEMENT:")
    configurations = {}

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        positions_1 = frozenset([(x, y) for x in range(14) for y in range(14) if input_grid[x][y] == 1])

        couleur_sortie = None
        for x in range(14):
            for y in range(14):
                if output_grid[x][y] != 0:
                    couleur_sortie = output_grid[x][y]
                    break
            if couleur_sortie is not None:
                break

        configurations[positions_1] = couleur_sortie
        print(f"Exemple {i}: {sorted(positions_1)} -> {couleur_sortie}")

    print("
TEST:"    test_input = puzzle_data['test'][0]['input']
    positions_1_test = frozenset([(x, y) for x in range(14) for y in range(14) if test_input[x][y] == 1])

    print(f"Test: {sorted(positions_1_test)}")

    # Chercher similarité
    print("
SIMILARITÉ:"    for i, config in enumerate(configurations.keys(), 1):
        intersection = len(config.intersection(positions_1_test))
        similarity = intersection / len(positions_1_test)
        print(f"Exemple {i}: {similarity:.2f} similarité")

        if similarity > 0.8:  # Plus de 80% similaire
            couleur = configurations[config]
            print(f"  → POTENTIELLEMENT {couleur}")

if __name__ == "__main__":
    analyser_test()
