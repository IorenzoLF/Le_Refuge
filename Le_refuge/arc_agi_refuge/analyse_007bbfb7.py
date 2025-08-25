#!/usr/bin/env python3
"""
🎯 ANALYSE PUZZLE 2 - 007bbfb7
Objectif: comprendre et résoudre à 100%
"""

import json

def analyser_007bbfb7():
    print("🎯 ANALYSE PUZZLE 2 - 007bbfb7")
    print("=" * 40)

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"Training examples: {len(puzzle_data['train'])}")
    print(f"Test examples: {len(puzzle_data['test'])}")

    # Analyser les exemples d'entraînement
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i} D'ENTRAÎNEMENT:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_grid)}x{len(output_grid[0])}")

        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        print("OUTPUT:")
        for row in output_grid:
            print(f"  {row}")

        # Analyser les changements
        changements = 0
        for x in range(len(input_grid)):
            for y in range(len(input_grid[0])):
                if input_grid[x][y] != output_grid[x][y]:
                    changements += 1
                    print(f"  Change ({x},{y}): {input_grid[x][y]} -> {output_grid[x][y]}")

        print(f"Changements: {changements}")

    # Analyser l'exemple de test
    print("\nTEST À RÉSOUDRE:")
    test_input = puzzle_data['test'][0]['input']
    print(f"Test dimensions: {len(test_input)}x{len(test_input[0])}")

    print("TEST INPUT:")
    for row in test_input:
        print(f"  {row}")

    # Analyser le pattern
    comprendre_pattern_007bbfb7(puzzle_data)

def comprendre_pattern_007bbfb7(puzzle_data):
    """Tente de comprendre le pattern du puzzle"""
    print("\n🧠 ANALYSE DU PATTERN:")

    exemples = puzzle_data['train']

    # Analyser les types de transformation
    transformations = []
    for exemple in exemples:
        h_in, w_in = len(exemple['input']), len(exemple['input'][0])
        h_out, w_out = len(exemple['output']), len(exemple['output'][0])

        if h_in == h_out and w_in == w_out:
            transformations.append("meme_dimensions")
        else:
            transformations.append("changement_dimensions")

    print(f"  📊 Types de transformations: {set(transformations)}")

    # Analyser les couleurs
    toutes_couleurs = set()
    for exemple in exemples:
        for grid in [exemple['input'], exemple['output']]:
            for row in grid:
                for cell in row:
                    if cell != 0:
                        toutes_couleurs.add(cell)

    print(f"  🎨 Couleurs utilisées: {sorted(toutes_couleurs)}")

    # Proposition d'hypothèses
    print("\n💡 HYPOTHÈSES DE PATTERN:")

    if len(set(transformations)) == 1 and transformations[0] == "meme_dimensions":
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

    print("\n🎯 PROCHAINE ÉTAPE:")
    print("  🔍 Analyse manuelle des exemples")
    print("  💡 Proposition d'une solution")
    print("  🧪 Test de la solution")
    print("  📊 Validation à 100%")

if __name__ == "__main__":
    analyser_007bbfb7()
