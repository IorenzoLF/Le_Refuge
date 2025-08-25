#!/usr/bin/env python3
"""
🔍 ANALYSER TEST 009d5c81
Pourquoi la configuration du test n'est pas reconnue ?
"""

import json

def analyser_test():
    print("🔍 ANALYSER TEST 009d5c81")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    print("CONFIGURATIONS D'ENTRAÎNEMENT:")
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
TEST CONFIGURATION:"    test_input = puzzle_data['test'][0]['input']
    positions_1_test = frozenset([(x, y) for x in range(14) for y in range(14) if test_input[x][y] == 1])

    print(f"Test: {sorted(positions_1_test)}")

    # Chercher la correspondance la plus proche
    print("
🔍 ANALYSE DES DIFFÉRENCES:"    for i, config in enumerate(configurations.keys(), 1):
        difference = config.symmetric_difference(positions_1_test)
        intersection = config.intersection(positions_1_test)

        print(f"Exemple {i}:")
        print(f"  Intersection: {len(intersection)} positions communes")
        print(f"  Différence: {len(difference)} positions différentes")
        print(f"  Similitude: {len(intersection)}/{len(positions_1_test)}")

        if difference:
            print(f"  Positions manquantes dans test: {config - positions_1_test}")
            print(f"  Positions en trop dans test: {positions_1_test - config}")

    # Afficher la grille du test pour visualisation
    print("
🧪 GRILLE DU TEST:"    print("Pixels 1 (déterminent la couleur):")
    for x in range(14):
        for y in range(14):
            if test_input[x][y] == 1:
                print(f"  Position ({x},{y})")

    print("Pixels 8 (seront colorés):")
    for x in range(14):
        for y in range(14):
            if test_input[x][y] == 8:
                print(f"  Position ({x},{y})")

    # Analyser visuellement les positions
    print("
📊 VISUALISATION:"    print("Positions pixels 1 dans test:")
    positions_1_list = sorted(list(positions_1_test))
    for pos in positions_1_list:
        print(f"  {pos}")

    print("
💡 HYPOTHÈSES:"    print("1. Configuration similaire à exemple 3: rectangle vertical")
    print("2. Configuration similaire à exemple 5: rectangle vertical")
    print("3. Nouvelle configuration non vue en entraînement")
    print("4. Erreur dans l'identification des positions")

    # Comparer avec les exemples les plus similaires
    print("
🔍 COMPARAISON AVEC EXEMPLES SIMILAIRES:"    max_similarity = 0
    best_match = None

    for config, couleur in configurations.items():
        intersection = len(config.intersection(positions_1_test))
        similarity = intersection / len(positions_1_test)

        if similarity > max_similarity:
            max_similarity = similarity
            best_match = (config, couleur)

    if best_match:
        config, couleur = best_match
        print(f"Meilleure correspondance: {max_similarity:.2f} similarité")
        print(f"Configuration: {sorted(config)} -> {couleur}")
        print(f"Test: {sorted(positions_1_test)}")

if __name__ == "__main__":
    analyser_test()
