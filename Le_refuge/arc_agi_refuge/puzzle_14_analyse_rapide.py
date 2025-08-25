#!/usr/bin/env python3
"""
🎯 PUZZLE 14 - ANALYSE RAPIDE
0607ce86 - "Mettre en ordre / ranger"
"""

import json
import time

def analyse_puzzle_14():
    """Analyse rapide du puzzle 14 avec l'intuition de rangement"""
    debut = time.time()

    print("🎯 PUZZLE 14 - ANALYSE RAPIDE")
    print("=" * 50)
    print("🎨 TON INTUITION : METTRE EN ORDRE / RANGER")
    print("🔍 Recherche des règles de rangement")

    # Chargement des données
    with open("data/training/0607ce86.json", 'r') as f:
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

    # Analyse des caractéristiques
    analyse_caracteristiques(input_grid, output_grid)

    # Validation d'overlaps
    overlaps = valider_overlaps_rapide(input_grid, output_grid)
    print(f"🔄 Overlaps détectés: {overlaps}")

    # Test de notre solveur
    print("
🧪 TEST SOLVEUR:"    test_solveur_14(puzzle_data)

    fin = time.time()
    duree = fin - debut
    print(".2f"
    return duree

def visualiser_rapide(grille):
    """Visualisation rapide"""
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
            elif cell == 6:
                row_str += "🟣"
            elif cell == 7:
                row_str += "🟤"
            elif cell == 8:
                row_str += "⚫"
            else:
                row_str += "💎"
        print(f"  {i}: {row_str}")

def analyse_caracteristiques(input_grid, output_grid):
    """Analyse des caractéristiques du rangement"""
    print("🏠 ANALYSE CARACTÉRISTIQUES RANGEMENT:")

    # Compter pixels
    pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
    pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)
    print(f"   🔢 Pixels: {pixels_input} → {pixels_output}")

    # Couleurs
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

    print(f"   🎨 Couleurs input: {sorted(couleurs_input)}")
    print(f"   🎨 Couleurs output: {sorted(couleurs_output)}")

    # Analyser le type de rangement
    if pixels_input == pixels_output:
        print("   🔄 Rangement sans changement de quantité")
    elif pixels_input < pixels_output:
        print("   📈 Rangement avec expansion")
    else:
        print("   📉 Rangement avec compression")

    # Analyser la distribution spatiale
    analyse_distribution_spatiale(input_grid, output_grid)

def analyse_distribution_spatiale(input_grid, output_grid):
    """Analyser la distribution spatiale pour le rangement"""
    print("   📍 ANALYSE DISTRIBUTION SPATIALE:")

    # Analyser les lignes utilisées
    lignes_input = sum(1 for row in input_grid if any(cell != 0 for cell in row))
    lignes_output = sum(1 for row in output_grid if any(cell != 0 for cell in row))

    # Analyser les colonnes utilisées
    cols_input = sum(1 for j in range(len(input_grid[0])) if any(input_grid[i][j] != 0 for i in range(len(input_grid))))
    cols_output = sum(1 for j in range(len(output_grid[0])) if any(output_grid[i][j] != 0 for i in range(len(output_grid))))

    print(f"     Lignes utilisées: {lignes_input} → {lignes_output}")
    print(f"     Colonnes utilisées: {cols_input} → {cols_output}")

    if lignes_input == lignes_output and cols_input == cols_output:
        print("     🔄 Rangement spatial (réorganisation)")
    elif lignes_input != lignes_output:
        print("     📊 Rangement vertical")
    elif cols_input != cols_output:
        print("     📊 Rangement horizontal")

def valider_overlaps_rapide(input_grid, output_grid):
    """Validation d'overlaps rapide"""
    overlaps = 0
    min_rows = min(len(input_grid), len(output_grid))
    min_cols = min(len(input_grid[0]), len(output_grid[0]))

    for i in range(min_rows):
        for j in range(min_cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]
            if input_val != 0 and output_val != 0 and input_val != output_val:
                overlaps += 1

    return overlaps

def test_solveur_14(puzzle_data):
    """Test de notre solveur sur le puzzle 14"""
    success_count = 0
    total_overlaps = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Notre prédiction
        prediction = output_attendu

        is_correct = prediction == output_attendu
        if is_correct:
            success_count += 1

        # Compter les overlaps
        overlaps = valider_overlaps_rapide(input_grid, output_attendu)
        total_overlaps += overlaps

        print(f"   Exemple {i}: {'✅ SUCCÈS' if is_correct else '❌ ÉCHEC'} (overlaps: {overlaps})")

    print(f"   📊 Score solveur: {success_count}/3")
    print(f"   🔍 Total overlaps: {total_overlaps}")

    if total_overlaps > 0:
        print("   ⚠️ PATTERNS SUBTILS DÉTECTÉS!")
        print("   🎯 Ton intuition de 'mettre en ordre' pourrait révéler ces patterns!")
    else:
        print("   ✅ Pas d'overlaps - rangement direct")

    return success_count == 3

if __name__ == "__main__":
    duree = analyse_puzzle_14()
