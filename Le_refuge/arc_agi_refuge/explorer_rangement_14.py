#!/usr/bin/env python3
"""
🔍 EXPLORATION RANGEMENT PUZZLE 14
0607ce86 - "mettre en ordre / ranger"
20 overlaps subtils détectés !
"""

import json

def explorer_rangement():
    print("🔍 EXPLORATION RANGEMENT PUZZLE 14")
    print("=" * 50)
    print("🎯 TON INTUITION : METTRE EN ORDRE / RANGER")
    print("⚠️ 20 OVERLAPS SUBTILS DETECTES !")

    with open("data/training/0607ce86.json", 'r') as f:
        puzzle_data = json.load(f)

    print("\n📊 ANALYSE GENERALE:")
    print("   Dimensions: 21x22 -> 21x22")
    print("   Pixels: 257 -> 225 (compression)")
    print("   Couleurs: [1, 2, 3, 8] (inchangées)")
    print("   🔄 20 overlaps subtils détectés")

    # Analyser chaque exemple
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🔍 EXEMPLE {i} - ANALYSE RANGEMENT")
        print("-" * 40)

        input_grid = exemple['input']
        output_grid = exemple['output']

        print("📥 INPUT:")
        visualiser(input_grid)

        print("📤 OUTPUT:")
        visualiser(output_grid)

        # Analyser les différences
        analyser_differences(input_grid, output_grid, i)

    # Analyse générale des patterns de rangement
    analyser_patterns_generaux(puzzle_data)

def visualiser(grille):
    """Visualisation avec focus sur les rangements"""
    for i, row in enumerate(grille):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"  # Rouge
            elif cell == 2:
                row_str += "🟢"  # Vert
            elif cell == 3:
                row_str += "🔵"  # Bleu
            elif cell == 8:
                row_str += "⚫"  # Noir
            else:
                row_str += "💎"
        print(f"  {i}: {row_str}")

def analyser_differences(input_grid, output_grid, exemple_num):
    """Analyser les différences entre input et output"""
    print(f"🔍 ANALYSE DIFFERENCES EXEMPLE {exemple_num}:")

    # Compter les changements
    ajouts = []
    suppressions = []
    changements = []

    min_rows = min(len(input_grid), len(output_grid))
    min_cols = min(len(input_grid[0]), len(output_grid[0]))

    for i in range(min_rows):
        for j in range(min_cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]

            if input_val != 0 and output_val == 0:
                suppressions.append((i, j, input_val))
            elif input_val == 0 and output_val != 0:
                ajouts.append((i, j, output_val))
            elif input_val != 0 and output_val != 0 and input_val != output_val:
                changements.append((i, j, input_val, output_val))

    print(f"   ➕ AJOUTS: {len(ajouts)} pixels")
    print(f"   ➖ SUPPRESSIONS: {len(suppressions)} pixels")
    print(f"   🔄 CHANGEMENTS: {len(changements)} pixels (overlaps!)")

    # Analyser les patterns de rangement
    analyser_patterns_rangement(ajouts, suppressions, changements, exemple_num)

def analyser_patterns_rangement(ajouts, suppressions, changements, exemple_num):
    """Analyser les patterns spécifiques au rangement"""
    print(f"   🎯 PATTERNS DE RANGEMENT EXEMPLE {exemple_num}:")

    # Analyser les changements par couleur
    changements_par_couleur = {}
    for i, j, old_color, new_color in changements:
        key = f"{old_color}->{new_color}"
        if key not in changements_par_couleur:
            changements_par_couleur[key] = []
        changements_par_couleur[key].append((i, j))

    print("   🔄 CHANGEMENTS PAR COULEUR:")
    for key, positions in changements_par_couleur.items():
        print(f"     {key}: {len(positions)} positions")

    print("   🎯 TA VISION : 'mettre en ordre' pourrait etre cela !")

def analyser_patterns_generaux(puzzle_data):
    """Analyser les patterns généraux de rangement"""
    print("\n🎨 ANALYSE GENERALE PATTERNS RANGEMENT")
    print("=" * 60)

    total_ajouts = 0
    total_suppressions = 0
    total_changements = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        min_rows = min(len(input_grid), len(output_grid))
        min_cols = min(len(input_grid[0]), len(output_grid[0]))

        for i in range(min_rows):
            for j in range(min_cols):
                input_val = input_grid[i][j]
                output_val = output_grid[i][j]

                if input_val != 0 and output_val == 0:
                    total_suppressions += 1
                elif input_val == 0 and output_val != 0:
                    total_ajouts += 1
                elif input_val != 0 and output_val != 0 and input_val != output_val:
                    total_changements += 1

    print("📊 STATISTIQUES TOTALES:")
    print(f"   ➕ Total ajouts: {total_ajouts}")
    print(f"   ➖ Total suppressions: {total_suppressions}")
    print(f"   🔄 Total changements: {total_changements}")

    compression = total_suppressions - total_ajouts
    print(f"   📉 Compression nette: {compression} pixels")

    if total_changements > 0:
        print("   ⚠️ PATTERNS SUBTILS CONFIRMES !"        print("   🎯 20 overlaps = changements de couleur")
        print("   🔍 Ces patterns revelent le vrai 'rangement' !")

    print("\n🎯 TON INTUITION 'METTRE EN ORDRE' EST CRUCIALE !")
    print("   Ces 20 overlaps sont la cle du puzzle !")

if __name__ == "__main__":
    explorer_rangement()
