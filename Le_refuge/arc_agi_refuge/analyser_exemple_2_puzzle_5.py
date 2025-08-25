#!/usr/bin/env python3
"""
🔍 ANALYSE DÉTAILLÉE EXEMPLE 2 PUZZLE 5
Comprendre pourquoi l'exemple 2 échoue
"""

import json

def analyser_exemple_2():
    """Analyser en détail l'exemple 2 qui pose problème"""
    print("🔍 ANALYSE EXEMPLE 2 PUZZLE 5")
    print("=" * 50)

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser l'exemple 2 spécifiquement
    exemple = puzzle_data['train'][1]  # Index 1 = exemple 2
    input_grid = exemple['input']
    output_attendu = exemple['output']

    print("📐 EXEMPLE 2 - ANALYSE DÉTAILLÉE")
    print(f"Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_attendu)}x{len(output_attendu[0])}")

    print("\nINPUT:")
    for i, row in enumerate(input_grid):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
        print(f"  {i}: {row_str}")

    print("\nOUTPUT ATTENDU:")
    for i, row in enumerate(output_attendu):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 2:
                row_str += "🟢"
        print(f"  {i}: {row_str}")

    # Appliquer notre pattern actuel
    solution_actuelle = appliquer_pattern_actuel(input_grid)

    print("\nSOLUTION ACTUELLE:")
    for i, row in enumerate(solution_actuelle):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 2:
                row_str += "🟢"
        print(f"  {i}: {row_str}")

    # Comparer
    print("\n🔍 COMPARAISON:")
    for i in range(len(output_attendu)):
        attendu = output_attendu[i]
        actuel = solution_actuelle[i] if i < len(solution_actuelle) else [0] * len(attendu)

        if attendu != actuel:
            print(f"  Ligne {i}:")
            print(f"    Attendu:  {attendu}")
            print(f"    Actuel:   {actuel}")
            print("    ❌ DIFFÉRENCE"

    # Analyser les pixels
    pixels_input = compter_pixels(input_grid)
    pixels_attendu = compter_pixels(output_attendu)
    pixels_actuel = compter_pixels(solution_actuelle)

    print("
📊 ANALYSE DES PIXELS:"    print(f"  Input: {pixels_input}")
    print(f"  Attendu: {pixels_attendu}")
    print(f"  Actuel: {pixels_actuel}")

def appliquer_pattern_actuel(grid):
    """Appliquer le pattern actuel (celui qui échoue)"""
    rows_input = len(grid)
    cols = len(grid[0])
    rows_output = 9  # D'après l'exemple 1

    solution = [[0 for _ in range(cols)] for _ in range(rows_output)]

    for i in range(rows_output):
        for j in range(cols):
            input_i = i % rows_input
            if grid[input_i][j] != 0:
                solution[i][j] = 2

    return solution

def compter_pixels(grille):
    """Compter les pixels par couleur"""
    compte = {}
    for row in grille:
        for cell in row:
            if cell != 0:
                compte[cell] = compte.get(cell, 0) + 1
    return compte

def analyser_tous_exemples():
    """Analyser tous les exemples pour voir les différences"""
    print("
📋 ANALYSE COMPARATIVE DES EXEMPLES:"    print("=" * 50)

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        pixels_input = compter_pixels(input_grid)
        pixels_output = compter_pixels(output_grid)

        ratio_extension = len(output_grid) / len(input_grid)

        print(f"  Exemple {i}:")
        print(f"    Input: {len(input_grid)}x{len(input_grid[0])}, pixels: {pixels_input}")
        print(f"    Output: {len(output_grid)}x{len(output_grid[0])}, pixels: {pixels_output}")
        print(".1f")

if __name__ == "__main__":
    analyser_exemple_2()
    analyser_tous_exemples()
