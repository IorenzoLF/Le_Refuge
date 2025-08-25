#!/usr/bin/env python3
"""
🔍 COMPARAISON DES EXEMPLES PUZZLE 15
0692e18c - comprendre les variations du pattern
"""

import json

def comparer_exemples():
    print("🔍 COMPARAISON DES EXEMPLES PUZZLE 15")
    print("=" * 45)
    print("🎯 Pourquoi 1/3 succès ? Variations du pattern")

    try:
        with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("❌ Fichier non trouvé")
        return

    # Comparer chaque exemple
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🔍 EXEMPLE {i} - ANALYSE DÉTAILLÉE")
        print("-" * 35)

        input_grid = exemple['input']
        output_grid = exemple['output']

        print("📥 INPUT:")
        visualiser(input_grid)

        print("📤 OUTPUT:")
        visualiser(output_grid)

        # Analyser le pattern spécifique à cet exemple
        analyser_pattern_exemple(input_grid, output_grid, i)

def visualiser(grille):
    """Visualisation simple"""
    for i, row in enumerate(grille):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "."
            elif cell == 6:
                row_str += "D"
            else:
                row_str += "?"
        print(f"  {i}: {row_str}")

def analyser_pattern_exemple(input_grid, output_grid, exemple_num):
    """Analyser le pattern spécifique à cet exemple"""
    print(f"🎯 PATTERN SPÉCIFIQUE EXEMPLE {exemple_num}:")

    # Positions colorées input
    positions_input = []
    for i in range(3):
        for j in range(3):
            if input_grid[i][j] != 0:
                positions_input.append((i, j))

    print(f"   📍 Positions input colorées: {positions_input}")

    # Analyser chaque bloc 3x3 de l'output
    print("   📊 PATTERNS PAR BLOC:")

    for bloc_x in range(3):
        for bloc_y in range(3):
            # Vérifier si ce bloc doit avoir un pattern
            has_input_pixel = input_grid[bloc_x][bloc_y] != 0

            # Compter les pixels dans ce bloc de l'output
            pixel_count = 0
            positions_bloc = []

            for dx in range(3):
                for dy in range(3):
                    out_x = bloc_x * 3 + dx
                    out_y = bloc_y * 3 + dy
                    if output_grid[out_x][out_y] != 0:
                        pixel_count += 1
                        positions_bloc.append((dx, dy))

            if has_input_pixel:
                print(f"     Bloc ({bloc_x},{bloc_y}): {pixel_count} pixels → {positions_bloc}")
            elif pixel_count > 0:
                print(f"     ⚠️ Bloc ({bloc_x},{bloc_y}): {pixel_count} pixels mais pas d'input !")

    # Comparer avec le pattern attendu
    pattern_attendu = [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1), (2, 2)]
    print(f"   🎨 Pattern attendu: {pattern_attendu}")

    # Vérifier si les patterns correspondent
    for bloc_x, bloc_y in positions_input:
        positions_attendues = []
        for dx, dy in pattern_attendu:
            out_x = bloc_x * 3 + dx
            out_y = bloc_y * 3 + dy
            if output_grid[out_x][out_y] != 0:
                positions_attendues.append((dx, dy))

        positions_reelles = []
        for dx in range(3):
            for dy in range(3):
                out_x = bloc_x * 3 + dx
                out_y = bloc_y * 3 + dy
                if output_grid[out_x][out_y] != 0:
                    positions_reelles.append((dx, dy))

        correspondance = set(positions_attendues) == set(positions_reelles)
        print(f"     ✅ Correspondance bloc ({bloc_x},{bloc_y}): {correspondance}")

        if not correspondance:
            print(f"        Attendu: {positions_attendues}")
            print(f"        Réel: {positions_reelles}")

def analyser_variations_globales():
    """Analyser les variations globales entre exemples"""
    print("
🎨 ANALYSE VARIATIONS GLOBALES"    print("=" * 40)

    try:
        with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        return

    print("🔍 PATTERNS OBSERVÉS PAR EXEMPLE:")

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Positions input
        positions_input = []
        for x in range(3):
            for y in range(3):
                if input_grid[x][y] != 0:
                    positions_input.append((x, y))

        # Patterns par bloc
        patterns_exemple = {}
        for bloc_x in range(3):
            for bloc_y in range(3):
                if input_grid[bloc_x][bloc_y] != 0:
                    positions_bloc = []
                    for dx in range(3):
                        for dy in range(3):
                            out_x = bloc_x * 3 + dx
                            out_y = bloc_y * 3 + dy
                            if output_grid[out_x][out_y] != 0:
                                positions_bloc.append((dx, dy))
                    patterns_exemple[(bloc_x, bloc_y)] = positions_bloc

        print(f"   Exemple {i} (input: {positions_input}):")
        for pos, pattern in patterns_exemple.items():
            print(f"     {pos} → {pattern}")

    print("
🎯 CONCLUSION:"    print("   📊 Le pattern de base est cohérent")
    print("   🔍 Mais il y a des variations subtiles")
    print("   🎨 Chaque position input a son propre sous-pattern")
    print("   🌟 C'est un système de règles plus complexe !")

if __name__ == "__main__":
    comparer_exemples()
    analyser_variations_globales()
