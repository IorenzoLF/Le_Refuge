#!/usr/bin/env python3
"""
🎯 ANALYSE COMPLÈTE PREMIER PUZZLE - 00576224
Objectif: comprendre et résoudre à 100%
"""

import json

def analyser_00576224():
    print("🎯 ANALYSE COMPLÈTE 00576224")
    print("=" * 40)

    with open("data/training/00576224.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"Exemples d'entraînement: {len(puzzle_data['train'])}")
    print(f"Exemples de test: {len(puzzle_data['test'])}")

    # Analyser chaque exemple d'entraînement
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i} D'ENTRAÎNEMENT:")
        analyser_exemple(exemple, i)

    # Analyser l'exemple de test
    print("
🧪 EXEMPLE DE TEST:"    test_input = puzzle_data['test'][0]['input']
    analyser_grille(test_input, "Test Input")

    # Comprendre le pattern
    comprendre_pattern_00576224(puzzle_data)

def analyser_exemple(exemple, num):
    """Analyse un exemple complet"""
    input_grid = exemple['input']
    output_grid = exemple['output']

    print(f"  Dimensions: {len(input_grid)}x{len(input_grid[0])} → {len(output_grid)}x{len(output_grid[0])}")

    # Analyser input
    analyser_grille(input_grid, "Input")

    # Analyser output
    analyser_grille(output_grid, "Output")

    # Comparer
    comparer_grilles(input_grid, output_grid)

def analyser_grille(grille, nom):
    """Analyse détaillée d'une grille"""
    h, w = len(grille), len(grille[0])

    print(f"  {nom} ({h}x{w}):")

    # Afficher la grille
    for row in grille:
        print(f"    {row}")

    # Analyser les couleurs
    couleurs = set()
    positions = []
    for i in range(h):
        for j in range(w):
            if grille[i][j] != 0:
                couleurs.add(grille[i][j])
                positions.append((i, j, grille[i][j]))

    print(f"    Couleurs: {sorted(couleurs)}")
    print(f"    Pixels non-zéro: {len(positions)}")
    print(f"    Positions: {positions}")

def comparer_grilles(input_grid, output_grid):
    """Compare input et output pour identifier les changements"""
    h_in, w_in = len(input_grid), len(input_grid[0])
    h_out, w_out = len(output_grid), len(output_grid[0])

    print("  🔄 TRANSFORMATION:")

    if h_in == h_out and w_in == w_out:
        print("    📐 Mêmes dimensions")
        analyser_changements_pixels(input_grid, output_grid)
    else:
        print(f"    📐 Changement dimensions: {h_in}x{w_in} → {h_out}x{w_out}")
        analyser_changement_dimensions(input_grid, output_grid)

def analyser_changements_pixels(input_grid, output_grid):
    """Analyse les changements pixel par pixel"""
    h, w = len(input_grid), len(input_grid[0])
    changements = []

    for i in range(h):
        for j in range(w):
            if input_grid[i][j] != output_grid[i][j]:
                changements.append({
                    'pos': (i, j),
                    'avant': input_grid[i][j],
                    'apres': output_grid[i][j]
                })

    print(f"    🔄 {len(changements)} changements détectés:")

    for changement in changements:
        pos, avant, apres = changement['pos'], changement['avant'], changement['apres']
        print(f"      ({pos[0]},{pos[1]}): {avant} → {apres}")

    if len(changements) == 0:
        print("    ✅ Aucune modification!")

def analyser_changement_dimensions(input_grid, output_grid):
    """Analyse les changements de dimensions"""
    h_in, w_in = len(input_grid), len(input_grid[0])
    h_out, w_out = len(output_grid), len(output_grid[0])

    print(f"    📏 Ratio hauteur: {h_out/h_in if h_in > 0 else 'N/A'}")
    print(f"    📏 Ratio largeur: {w_out/w_in if w_in > 0 else 'N/A'}")

def comprendre_pattern_00576224(puzzle_data):
    """Tente de comprendre le pattern du puzzle"""
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

def main():
    analyser_00576224()

if __name__ == "__main__":
    main()
