#!/usr/bin/env python3
"""
🎯 ANALYSE PREMIER PUZZLE - 00576224
Approche systématique: comprendre puis résoudre à 100%
"""

import json

def analyser_premier_puzzle():
    print("🎯 ANALYSE PREMIER PUZZLE - 00576224")
    print("=" * 50)
    print("📊 Objectif: Compréhension complète → 100% de résolution")

    try:
        with open("data/training/00576224.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return

    # Analyse de la structure
    print("
📋 STRUCTURE DU PUZZLE:"    print(f"   📚 Nombre d'exemples d'entraînement: {len(puzzle_data['train'])}")
    print(f"   🧪 Nombre d'exemples de test: {len(puzzle_data['test'])}")

    # Analyse des exemples d'entraînement
    print("
🧪 ANALYSE EXEMPLES ENTRAÎNEMENT:"    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        print(f"\n   📝 Exemple {i}: {h_in}x{w_in} → {h_out}x{w_out}")

        # Analyse des couleurs
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

        print(f"   🎨 Couleurs: {sorted(couleurs_in)} → {sorted(couleurs_out)}")

        # Affichage des grilles
        print("   📥 Input:")
        for row in input_grid:
            print(f"      {row}")

        print("   📤 Output:")
        for row in output_grid:
            print(f"      {row}")

        # Analyse de la transformation
        analyse_transformation(input_grid, output_grid, i)

    # Analyse de l'exemple de test
    print("
🧪 ANALYSE EXEMPLE TEST:"    test_input = puzzle_data['test'][0]['input']
    h_test, w_test = len(test_input), len(test_input[0])

    print(f"   📝 Test: {h_test}x{w_test}")

    couleurs_test = set()
    for row in test_input:
        for cell in row:
            if cell != 0:
                couleurs_test.add(cell)

    print(f"   🎨 Couleurs: {sorted(couleurs_test)}")

    print("   📥 Test input:")
    for row in test_input:
        print(f"      {row}")

    # Tentative de compréhension du pattern
    comprendre_pattern(puzzle_data)

def analyse_transformation(input_grid, output_grid, exemple_num):
    """Analyse la transformation entre input et output"""

    h_in, w_in = len(input_grid), len(input_grid[0])
    h_out, w_out = len(output_grid), len(output_grid[0])

    print("   🔍 Analyse transformation:")

    # Compter les pixels non-zéro
    pixels_in = sum(1 for row in input_grid for cell in row if cell != 0)
    pixels_out = sum(1 for row in output_grid for cell in row if cell != 0)

    print(f"      📊 Pixels: {pixels_in} → {pixels_out}")

    # Analyse dimensionnelle
    if h_in == h_out and w_in == w_out:
        print("      📐 Même dimensions")
        analyse_meme_dimensions(input_grid, output_grid)
    else:
        print("      📐 Changement dimensions")
        analyse_changement_dimensions(input_grid, output_grid)

def analyse_meme_dimensions(input_grid, output_grid):
    """Analyse quand dimensions identiques"""

    h, w = len(input_grid), len(input_grid[0])
    differences = []

    for i in range(h):
        for j in range(w):
            if input_grid[i][j] != output_grid[i][j]:
                differences.append({
                    'position': (i, j),
                    'avant': input_grid[i][j],
                    'apres': output_grid[i][j]
                })

    print(f"      🔄 {len(differences)} positions modifiées")

    if len(differences) <= 10:  # Afficher si pas trop
        for diff in differences:
            print(f"         ({diff['position'][0]},{diff['position'][1]}): {diff['avant']} → {diff['apres']}")

def analyse_changement_dimensions(input_grid, output_grid):
    """Analyse quand dimensions changent"""

    h_in, w_in = len(input_grid), len(input_grid[0])
    h_out, w_out = len(output_grid), len(output_grid[0])

    print(f"      📏 {h_in}x{w_in} → {h_out}x{w_out}")

    # Analyse du ratio
    ratio_h = h_out / h_in if h_in > 0 else 0
    ratio_w = w_out / w_in if w_in > 0 else 0

    print(".2f"
def comprendre_pattern(puzzle_data):
    """Tente de comprendre le pattern général"""

    print("
🧠 TENTATIVE COMPRÉHENSION PATTERN:"    # Analyser tous les exemples
    exemples = puzzle_data['train']

    # Vérifier si c'est le même type de transformation
    types_transformation = []

    for exemple in exemples:
        input_grid = exemple['input']
        output_grid = exemple['output']

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        if h_in == h_out and w_in == w_out:
            types_transformation.append("meme_dimensions")
        else:
            types_transformation.append("changement_dimensions")

    print(f"   📊 Types de transformation: {set(types_transformation)}")

    # Analyser les couleurs utilisées
    toutes_couleurs = set()
    for exemple in exemples:
        for grid_type in ['input', 'output']:
            grid = exemple[grid_type]
            for row in grid:
                for cell in row:
                    if cell != 0:
                        toutes_couleurs.add(cell)

    print(f"   🎨 Toutes les couleurs utilisées: {sorted(toutes_couleurs)}")

    # Proposition de pattern
    print("
💡 HYPOTHÈSES DE PATTERN:"    if len(set(types_transformation)) == 1:
        if types_transformation[0] == "meme_dimensions":
            print("   📐 Pattern: Modification dans même dimensions")
            print("   💡 Possibilités: déplacement, remplissage, suppression")
        else:
            print("   📐 Pattern: Changement de dimensions")
            print("   💡 Possibilités: compression, expansion, reshape")
    else:
        print("   🔄 Patterns mixtes - plus complexe")

    print("
🎯 PROCHAINE ÉTAPE:"    print("   🔍 Analyse manuelle des exemples")
    print("   💡 Proposition d'hypothèse de pattern")
    print("   🧪 Test de l'hypothèse")
    print("   📊 Validation à 100%")

def main():
    analyser_premier_puzzle()

if __name__ == "__main__":
    main()
