#!/usr/bin/env python3
"""
🖼️ ANALYSE PUZZLE 3: 00d62c1b
Visualisation géométrique simple
"""

import json

def visualiser_puzzle_3():
    """Visualiser le puzzle 3"""
    print("🖼️ ANALYSE PUZZLE 3: 00d62c1b")
    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"Nombre d'exemples: {len(puzzle_data['train'])}")

    # Analyser chaque exemple
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🖼️ EXEMPLE {i}")

        input_grid = exemple['input']
        output_grid = exemple['output']

        # Dimensions
        dim_input = f"{len(input_grid)}x{len(input_grid[0])}"
        dim_output = f"{len(output_grid)}x{len(output_grid[0])}"

        print(f"   📥 INPUT {dim_input} → 📤 OUTPUT {dim_output}")

        # Visualiser l'input
        print("   📥 INPUT:")
        visualiser_grille(input_grid)

        # Visualiser l'output
        print("   📤 OUTPUT:")
        visualiser_grille(output_grid)

        # Analyser les changements
        analyser_changements(input_grid, output_grid)

def visualiser_grille(grille):
    """Visualiser une grille"""
    for row in grille:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
            elif cell == 2:
                row_str += "🟢"
            elif cell == 3:
                row_str += "🔵"
            elif cell == 4:
                row_str += "🟡"
            elif cell == 5:
                row_str += "🟠"
            elif cell == 6:
                row_str += "🟣"
            elif cell == 7:
                row_str += "🟤"
            elif cell == 8:
                row_str += "⚫"
            else:
                row_str += "⚪"
        print(f"      {row_str}")

def analyser_changements(input_grid, output_grid):
    """Analyser les changements"""
    pixels_input = compter_pixels_couleur(input_grid)
    pixels_output = compter_pixels_couleur(output_grid)

    print("   🔄 CHANGEMENTS:")
    print(f"      Input: {pixels_input}")
    print(f"      Output: {pixels_output}")

    # Chercher les changements
    for couleur in set(pixels_input.keys()) | set(pixels_output.keys()):
        avant = pixels_input.get(couleur, 0)
        apres = pixels_output.get(couleur, 0)
        if avant != apres:
            emoji = get_emoji_couleur(couleur)
            if avant > apres:
                print(f"         {emoji} {couleur}: {avant} → {apres} (DISPARITION)")
            elif apres > avant:
                print(f"         {emoji} {couleur}: {avant} → {apres} (APPARITION)")

def get_emoji_couleur(couleur):
    """Obtenir l'emoji pour une couleur"""
    emojis = {
        1: "🔴", 2: "🟢", 3: "🔵", 4: "🟡",
        5: "🟠", 6: "🟣", 7: "🟤", 8: "⚫"
    }
    return emojis.get(couleur, "⚪")

def compter_pixels_couleur(grille):
    """Compter les pixels par couleur"""
    compte = {}
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            couleur = grille[i][j]
            if couleur != 0:
                compte[couleur] = compte.get(couleur, 0) + 1
    return compte

def analyser_patterns():
    """Analyser les patterns"""
    print("\n🎯 PATTERNS GÉNÉRAUX")
    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Vérifier dimensions
    dims_input = set()
    dims_output = set()

    for exemple in puzzle_data['train']:
        input_grid = exemple['input']
        output_grid = exemple['output']

        dims_input.add(f"{len(input_grid)}x{len(input_grid[0])}")
        dims_output.add(f"{len(output_grid)}x{len(output_grid[0])}")

    print(f"Dimensions d'entrée: {sorted(dims_input)}")
    print(f"Dimensions de sortie: {sorted(dims_output)}")

    # Analyser les couleurs
    couleurs_input = set()
    couleurs_output = set()

    for exemple in puzzle_data['train']:
        input_grid = exemple['input']
        output_grid = exemple['output']

        for row in input_grid:
            for cell in row:
                if cell != 0:
                    couleurs_input.add(cell)

        for row in output_grid:
            for cell in row:
                if cell != 0:
                    couleurs_output.add(cell)

    print(f"Couleurs en input: {sorted(couleurs_input)}")
    print(f"Couleurs en output: {sorted(couleurs_output)}")

if __name__ == "__main__":
    visualiser_puzzle_3()
    analyser_patterns()
