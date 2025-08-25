#!/usr/bin/env python3
"""
🎯 PUZZLE 9 - ANALYSE INITIALE RAPIDE
Test de rythme sur 1 semaine terrienne
"""

import json
import time

def analyse_puzzle_9_rapide():
    """Analyse initiale du puzzle 9 avec mesure de temps"""
    debut = time.time()

    print("🚀 PUZZLE 9 - ANALYSE INITIALE RAPIDE")
    print("=" * 50)
    print("⏱️ DÉBUT ANALYSE:", time.strftime("%H:%M:%S"))

    # Récupération des données
    with open("data/training/046d8d7a.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"📊 {len(puzzle_data['train'])} exemples d'entraînement")

    # Analyse rapide du premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    # Dimensions
    dim_input = f"{len(input_grid)}x{len(input_grid[0])}"
    dim_output = f"{len(output_grid)}x{len(output_grid[0])}"
    print(f"📐 Dimensions: {dim_input} → {dim_output}")

    # Visualisation rapide
    print("📥 INPUT:")
    visualiser_rapide(input_grid)

    print("📤 OUTPUT:")
    visualiser_rapide(output_grid)

    # Analyse des couleurs
    couleurs_input = set()
    couleurs_output = set()

    for row in input_grid:
        for cell in row:
            if cell != 0:
                couleurs_input.add(cell)

    for row in output_grid:
        for cell in row:
            if cell != 0:
                couleurs_output.add(cell)

    print(f"🎨 Couleurs input: {sorted(couleurs_input)}")
    print(f"🎨 Couleurs output: {sorted(couleurs_output)}")

    # Analyse des pixels
    pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
    pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)

    print(f"🔢 Pixels: {pixels_input} → {pixels_output}")

    # Validation d'overlap rapide
    overlaps = valider_overlaps_rapide(input_grid, output_grid)
    print(f"🔄 Overlaps détectés: {overlaps}")

    fin = time.time()
    duree = fin - debut

    print("
⏱️ FIN ANALYSE:"    print(".2f"    print("
🎯 ANALYSE TERMINÉE - PRÊT POUR RÉSOLUTION!"    return duree

def visualiser_rapide(grille):
    """Visualisation rapide sans détails"""
    for i, row in enumerate(grille):
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
                row_str += "💎"
        print(f"  {i}: {row_str}")

def valider_overlaps_rapide(input_grid, output_grid):
    """Validation d'overlap rapide"""
    overlaps = 0
    rows = len(input_grid)
    cols = len(input_grid[0])

    for i in range(rows):
        for j in range(cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]

            if input_val != 0 and output_val != 0 and input_val != output_val:
                overlaps += 1

    return overlaps

if __name__ == "__main__":
    duree_analyse = analyse_puzzle_9_rapide()
