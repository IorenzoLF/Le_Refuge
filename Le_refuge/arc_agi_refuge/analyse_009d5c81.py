#!/usr/bin/env python3
"""
🎯 ANALYSE PUZZLE 3 - 009d5c81
Objectif: comprendre et résoudre à 100%
"""

import json

def analyser_009d5c81():
    print("🎯 ANALYSE PUZZLE 3 - 009d5c81")
    print("=" * 40)

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"Training examples: {len(puzzle_data['train'])}")
    print(f"Test examples: {len(puzzle_data['test'])}")

    # Analyser chaque exemple d'entraînement
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i} D'ENTRAÎNEMENT:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        print(f"Dimensions: {h_in}x{w_in} -> {h_out}x{w_out}")

        # Analyser les couleurs
        couleurs_in = set()
        couleurs_out = set()
        for row in input_grid:
            for cell in row:
                if cell != 0:
                    couleurs_in.add(cell)
        for row in output_grid:
            for cell in row:
                if cell != 0:
                    couleurs_out.add(cell)

        print(f"Couleurs: {sorted(couleurs_in)} -> {sorted(couleurs_out)}")

        # Afficher les grilles
        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        print("OUTPUT:")
        for row in output_grid:
            print(f"  {row}")

        # Analyser les changements
        changements = 0
        for x in range(h_in):
            for y in range(w_in):
                if input_grid[x][y] != output_grid[x][y]:
                    changements += 1
                    print(f"  Change ({x},{y}): {input_grid[x][y]} -> {output_grid[x][y]}")

        print(f"Changements: {changements}")

    # Analyser l'exemple de test
    print("
🧪 EXEMPLE DE TEST:"    test_input = puzzle_data['test'][0]['input']
    h_test, w_test = len(test_input), len(test_input[0])

    print(f"Test dimensions: {h_test}x{w_test}")

    couleurs_test = set()
    for row in test_input:
        for cell in row:
            if cell != 0:
                couleurs_test.add(cell)

    print(f"Couleurs test: {sorted(couleurs_test)}")

    print("TEST INPUT:")
    for row in test_input:
        print(f"  {row}")

    # Analyser le pattern général
    analyser_pattern_009d5c81(puzzle_data)

def analyser_pattern_009d5c81(puzzle_data):
    """Analyser le pattern général du puzzle"""
    print("
🧠 ANALYSE DU PATTERN:"    exemples = puzzle_data['train']

    # Analyser les types de transformation
    transformations = []
    for exemple in exemples:
        h_in, w_in = len(exemple['input']), len(exemple['input'][0])
        h_out, w_out = len(exemple['output']), len(exemple['output'][0])

        if h_in == h_out and w_in == w_out:
            transformations.append("meme_dimensions")
        else:
            transformations.append("changement_dimensions")

    print(f"Types de transformations: {set(transformations)}")

    # Analyser les couleurs
    toutes_couleurs = set()
    for exemple in exemples:
        for grid in [exemple['input'], exemple['output']]:
            for row in grid:
                for cell in row:
                    if cell != 0:
                        toutes_couleurs.add(cell)

    print(f"Toutes les couleurs utilisées: {sorted(toutes_couleurs)}")

    # Proposition d'hypothèses
    print("
💡 HYPOTHÈSES DE PATTERN:"    if len(set(transformations)) == 1 and transformations[0] == "meme_dimensions":
        print("  📐 Pattern: modification dans même dimensions")
        print("  💡 Possibilités:")
        print("     - Déplacement de pixels")
        print("     - Changement de couleurs")
        print("     - Remplacement de valeurs")
    else:
        print("  📐 Pattern: changement de dimensions")
        print("  💡 Possibilités:")
        print("     - Compression/expansion")
        print("     - Reshape de la grille")

    print("
🎯 PROCHAINE ÉTAPE:"    print("  🔍 Analyse manuelle des exemples")
    print("  💡 Proposition d'une solution")
    print("  🧪 Test de la solution")
    print("  📊 Validation à 100%")

if __name__ == "__main__":
    analyser_009d5c81()
