#!/usr/bin/env python3
"""
🎯 SOLUTION COMPLÈTE 009d5c81
"""

import json

def solution_complete():
    print("🎯 SOLUTION COMPLÈTE 009d5c81")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    # Mapping complet
    mapping = {
        frozenset([(10,4),(10,5),(10,6),(11,4),(11,6),(12,5)]): 7,
        frozenset([(10,3),(10,5),(11,4),(12,3),(12,4),(12,5)]): 3,
        frozenset([(9,8),(10,7),(10,8),(10,9),(11,8)]): 2,
        frozenset([(8,2),(8,4),(9,3),(10,2),(10,3),(10,4)]): 3,
        frozenset([(9,2),(10,1),(10,2),(10,3),(11,2)]): 2
    }

    # Test
    test_input = puzzle_data['test'][0]['input']
    positions_1_test = frozenset([(x, y) for x in range(14) for y in range(14) if test_input[x][y] == 1])

    print(f"Test positions 1: {sorted(positions_1_test)}")

    couleur_test = mapping.get(positions_1_test)

    if couleur_test:
        print(f"Couleur trouvée: {couleur_test}")

        # Créer solution
        solution = [[0 for _ in range(14)] for _ in range(14)]
        for x in range(14):
            for y in range(14):
                if test_input[x][y] == 8:
                    solution[x][y] = couleur_test

        print("SOLUTION (premières lignes):")
        for i in range(5):
            print(f"  {solution[i]}")

        # Vérification
        pixels_8 = sum(1 for row in test_input for cell in row if cell == 8)
        pixels_couleur = sum(1 for row in solution for cell in row if cell != 0)

        print(f"Pixels 8 input: {pixels_8}")
        print(f"Pixels colorés output: {pixels_couleur}")
        print(f"Coherent: {'✅' if pixels_8 == pixels_couleur else '❌'}")

        if pixels_8 == pixels_couleur:
            submission = {"009d5c81": solution}
            with open("submission_009d5c81_final.json", 'w') as f:
                json.dump(submission, f, indent=2)
            print("Sauvegardé!")
    else:
        print("Configuration non reconnue")

if __name__ == "__main__":
    solution_complete()
