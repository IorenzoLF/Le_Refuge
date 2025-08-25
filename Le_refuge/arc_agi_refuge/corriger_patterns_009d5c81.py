#!/usr/bin/env python3
"""
🔧 CORRIGER PATTERNS 009d5c81
Utiliser les vraies positions des pixels 1
"""

import json

def corriger_patterns():
    print("🔧 CORRIGER PATTERNS 009d5c81")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    # Extraire les vraies positions des 1 et leurs couleurs correspondantes
    vrai_mapping = {}

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Positions des 1
        positions_1 = frozenset([(x, y) for x in range(14) for y in range(14) if input_grid[x][y] == 1])

        # Couleur de sortie
        couleur_sortie = None
        for x in range(14):
            for y in range(14):
                if output_grid[x][y] != 0:
                    couleur_sortie = output_grid[x][y]
                    break
            if couleur_sortie is not None:
                break

        vrai_mapping[positions_1] = couleur_sortie
        print(f"Exemple {i}: {sorted(positions_1)} -> {couleur_sortie}")

    print("
🎨 VRAI MAPPING:"    for positions, couleur in vrai_mapping.items():
        print(f"  {sorted(positions)} -> {couleur}")

    # Maintenant tester avec les vraies positions
    reussites = 0
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        positions_1 = frozenset([(x, y) for x in range(14) for y in range(14) if input_grid[x][y] == 1])

        couleur_predite = vrai_mapping.get(positions_1)

        if couleur_predite:
            # Vérifier
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
            print(f"Exemple {i}: Pattern non trouvé")

    print(f"Score: {reussites}/5")

    if reussites == 5:
        print("🎉 SUCCÈS AVEC VRAIES POSITIONS!")

        # Test
        test_input = puzzle_data['test'][0]['input']
        positions_1_test = frozenset([(x, y) for x in range(14) for y in range(14) if test_input[x][y] == 1])

        print(f"Test positions: {sorted(positions_1_test)}")

        couleur_test = vrai_mapping.get(positions_1_test)

        if couleur_test:
            print(f"Couleur test: {couleur_test}")

            # Créer solution
            solution = [[0 for _ in range(14)] for _ in range(14)]
            for x in range(14):
                for y in range(14):
                    if test_input[x][y] == 8:
                        solution[x][y] = couleur_test

            print("SOLUTION TEST (premières lignes):")
            for i in range(5):
                print(f"  {solution[i]}")

            # Sauvegarder
            submission = {"009d5c81": solution}
            with open("submission_009d5c81_vrai.json", 'w') as f:
                json.dump(submission, f, indent=2)
            print("Sauvegardé!")

if __name__ == "__main__":
    corriger_patterns()
