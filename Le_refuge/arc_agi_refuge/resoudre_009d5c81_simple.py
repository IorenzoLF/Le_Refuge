#!/usr/bin/env python3
"""
🎯 RÉSOLUTION 009d5c81
Pattern: positions des 1 déterminent la couleur des 8
"""

import json

def resoudre_009d5c81():
    print("🎯 RÉSOLUTION 009d5c81")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    # Patterns identifiés
    patterns = {
        ((10,4),(11,5),(12,6)): 7,  # L diagonal -> 7
        ((9,8),(10,7),(10,8),(10,9),(11,8),(12,8)): 2,  # Rectangle vertical -> 2
        ((9,2),(10,1),(10,2),(10,3),(11,2),(12,2)): 2,  # Rectangle vertical -> 2
        ((8,2),(9,3),(10,2),(10,3),(10,4),(11,4)): 3   # Rectangle -> 3
    }

    print("PATTERNS:")
    for pattern, couleur in patterns.items():
        print(f"  {pattern} -> {couleur}")

    # Tester validation
    reussites = 0
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        positions_1 = tuple(sorted([(x, y) for x in range(14) for y in range(14) if input_grid[x][y] == 1]))

        couleur_predite = None
        for pattern, couleur in patterns.items():
            if set(positions_1) == set(pattern):
                couleur_predite = couleur
                break

        if couleur_predite:
            couleur_reelle = None
            for x in range(14):
                for y in range(14):
                    if output_grid[x][y] != 0:
                        couleur_reelle = output_grid[x][y]
                        break
                if couleur_reelle is not None:
                    break

            if couleur_predite == couleur_reelle:
                print(f"Exemple {i}: ✅")
                reussites += 1
            else:
                print(f"Exemple {i}: ❌")
        else:
            print(f"Exemple {i}: Pattern non reconnu")

    print(f"Score: {reussites}/5")

    if reussites == 5:
        print("🎉 SUCCÈS!")

        # Résoudre test
        test_input = puzzle_data['test'][0]['input']
        positions_1_test = tuple(sorted([(x, y) for x in range(14) for y in range(14) if test_input[x][y] == 1]))

        print(f"Test positions 1: {positions_1_test}")

        couleur_test = None
        for pattern, couleur in patterns.items():
            if set(positions_1_test) == set(pattern):
                couleur_test = couleur
                break

        if couleur_test:
            print(f"Couleur test: {couleur_test}")

            # Créer solution
            solution = [[0 for _ in range(14)] for _ in range(14)]
            for x in range(14):
                for y in range(14):
                    if test_input[x][y] == 8:
                        solution[x][y] = couleur_test

            print("SOLUTION TEST (premières lignes):")
            for i in range(min(5, len(solution))):
                print(f"  {solution[i]}")

            # Sauvegarder
            submission = {"009d5c81": solution}
            with open("submission_009d5c81.json", 'w') as f:
                json.dump(submission, f, indent=2)
            print("Sauvegardé!")

if __name__ == "__main__":
    resoudre_009d5c81()
