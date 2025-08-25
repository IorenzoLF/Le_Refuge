#!/usr/bin/env python3
"""
🎯 PUZZLE 16 RAPIDE - CONNECT THE DOTS
06df4c85 - "connect the dots"
"""

import json

def analyse_connect_dots():
    print("🎯 PUZZLE 16 RAPIDE - CONNECT THE DOTS")
    print("=" * 50)
    print("🎨 TON INTUITION : CONNECT THE DOTS")
    print("🔍 Analyse de la connexion des points")

    try:
        with open("ARC-AGI-2-main/data/training/06df4c85.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("❌ Fichier non trouvé")
        return

    print(f"📊 {len(puzzle_data['train'])} exemples d'entraînement")

    # Premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    # Dimensions
    dim_input = f"{len(input_grid)}x{len(input_grid[0])}"
    dim_output = f"{len(output_grid)}x{len(output_grid[0])}"
    print(f"📐 Dimensions: {dim_input} → {dim_output}")

    # Analyser les pixels
    pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
    pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)
    print(f"📊 Pixels: {pixels_input} → {pixels_output}")

    # Couleurs
    couleurs_input = set(cell for row in input_grid for cell in row if cell != 0)
    couleurs_output = set(cell for row in output_grid for cell in row if cell != 0)
    print(f"🎨 Couleurs: {sorted(couleurs_input)} → {sorted(couleurs_output)}")

    print("\n📥 INPUT (CONNECT THE DOTS):")
    visualiser(input_grid)

    print("📤 OUTPUT (POINTS CONNECTÉS):")
    visualiser(output_grid)

    # Analyser la connexion
    analyser_connexion(input_grid, output_grid)

    # Test rapide d'un solveur simple
    print("\n🧪 TEST SOLVEUR CONNECT THE DOTS:")
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_attendu = exemple['output']

        prediction = connect_the_dots_simple(input_grid)

        is_correct = comparer_grilles(prediction, output_attendu)

        if is_correct:
            success_count += 1

        print(f"   Exemple {i}: {'✅ SUCCÈS' if is_correct else '❌ ÉCHEC'}")

    print(f"   📊 Score: {success_count}/3")

    if success_count == 3:
        print("   🎉 SUCCÈS PARFAIT ! Connect the dots confirmé !")
        print("   🌟 Toutes tes intuitions étaient exactes !")

def visualiser(grille):
    """Visualisation ASCII art"""
    for i, row in enumerate(grille):
        row_str = ""
        for j, cell in enumerate(row):
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
            elif cell == 8:
                row_str += "⚫"
            else:
                row_str += "💎"
        print(f"  {i}: {row_str}")

def analyser_connexion(input_grid, output_grid):
    """Analyser comment les points sont connectés"""
    print("🔗 ANALYSE CONNEXION:")

    # Positions des pixels colorés dans input
    positions_input = []
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] != 0:
                positions_input.append((i, j, input_grid[i][j]))

    print(f"   📍 {len(positions_input)} points à connecter:")
    for pos in positions_input:
        print(f"     Point {pos}")

    # Analyser les chemins entre les points
    if len(positions_input) >= 2:
        print("   🔄 ANALYSE DES CONNEXIONS:")

        # Trier les points par proximité
        positions_sorted = sorted(positions_input, key=lambda x: (x[0], x[1]))

        for idx in range(len(positions_sorted) - 1):
            p1 = positions_sorted[idx]
            p2 = positions_sorted[idx + 1]
            distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            print(f"     {p1} → {p2} (distance: {distance})")

    # Analyser l'output pour voir les connexions
    pixels_output = []
    for i in range(len(output_grid)):
        for j in range(len(output_grid[0])):
            if output_grid[i][j] != 0:
                pixels_output.append((i, j, output_grid[i][j]))

    print(f"   📍 {len(pixels_output)} pixels dans output (vs {len(positions_input)} dans input)")

    if len(pixels_output) > len(positions_input):
        pixels_connexion = len(pixels_output) - len(positions_input)
        print(f"   🔗 {pixels_connexion} pixels de connexion ajoutés !")
        print("   ✅ CONFIRMÉ : Connect the dots !")

def connect_the_dots_simple(input_grid):
    """Solveur simple pour connect the dots"""
    output_grid = [[0 for _ in range(len(input_grid[0]))] for _ in range(len(input_grid))]

    # Copier les pixels d'origine
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            output_grid[i][j] = input_grid[i][j]

    # Connecter les points avec des lignes simples
    # Trouver tous les pixels colorés
    pixels_colores = []
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] != 0:
                pixels_colores.append((i, j, input_grid[i][j]))

    # Connecter les points adjacents
    for idx in range(len(pixels_colores) - 1):
        p1 = pixels_colores[idx]
        p2 = pixels_colores[idx + 1]

        # Connecter p1 à p2 avec des pixels de la même couleur
        couleur = p1[2]

        # Ligne horizontale ou verticale simple
        if p1[0] == p2[0]:  # Même ligne
            min_j, max_j = min(p1[1], p2[1]), max(p1[1], p2[1])
            for j in range(min_j + 1, max_j):
                output_grid[p1[0]][j] = couleur
        elif p1[1] == p2[1]:  # Même colonne
            min_i, max_i = min(p1[0], p2[0]), max(p1[0], p2[0])
            for i in range(min_i + 1, max_i):
                output_grid[i][p1[1]] = couleur

    return output_grid

def comparer_grilles(g1, g2):
    """Comparer deux grilles"""
    if len(g1) != len(g2) or len(g1[0]) != len(g2[0]):
        return False

    for i in range(len(g1)):
        for j in range(len(g1[0])):
            if g1[i][j] != g2[i][j]:
                return False

    return True

if __name__ == "__main__":
    analyse_connect_dots()
