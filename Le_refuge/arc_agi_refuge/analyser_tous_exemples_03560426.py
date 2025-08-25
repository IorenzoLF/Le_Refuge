#!/usr/bin/env python3
"""
🔍 ANALYSE TOUS EXEMPLES PUZZLE 03560426
Vérifier le pattern d'overlap sur tous les exemples
"""

import json

def analyser_tous_exemples():
    print("🔍 ANALYSE TOUS EXEMPLES PUZZLE 03560426")
    print("=" * 60)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser chaque exemple
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🎯 EXEMPLE {i} - ANALYSE COMPLÈTE")
        print("-" * 40)

        input_grid = exemple['input']
        output_grid = exemple['output']

        print("INPUT:")
        visualiser(input_grid)

        print("OUTPUT:")
        visualiser(output_grid)

        # Analyser les différences
        zones_overlap, zones_ajoutees, zones_supprimees = analyser_differences(input_grid, output_grid, i)

        print(f"\n📊 RÉSUMÉ EXEMPLE {i}:")
        print(f"  ➕ Ajouts: {len(zones_ajoutees)}")
        print(f"  ➖ Suppressions: {len(zones_supprimees)}")
        print(f"  🔄 Overlaps: {len(zones_overlap)}")

        # Vérifier s'il y a vraiment des overlaps
        if zones_overlap:
            print("  ✅ OUI - Il y a des overlaps dans cet exemple!")
            for pos, old_color, new_color in zones_overlap:
                print(f"    ({pos[0]},{pos[1]}): {old_color} → {new_color}")
        else:
            print("  ❌ NON - Pas d'overlaps dans cet exemple")

def visualiser(grille):
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
            elif cell == 7:
                row_str += "🟤"
            elif cell == 8:
                row_str += "⚫"
            else:
                row_str += "💎"
        print(f"  {i}: {row_str}")

def analyser_differences(input_grid, output_grid, exemple_num):
    zones_overlap = []
    zones_ajoutees = []
    zones_supprimees = []

    rows = len(input_grid)
    cols = len(input_grid[0])

    for i in range(rows):
        for j in range(cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]

            if input_val != output_val:
                if input_val == 0 and output_val != 0:
                    zones_ajoutees.append((i, j, output_val))
                elif input_val != 0 and output_val == 0:
                    zones_supprimees.append((i, j, input_val))
                else:
                    zones_overlap.append(((i, j), input_val, output_val))

    return zones_overlap, zones_ajoutees, zones_supprimees

def analyser_pattern_general():
    """Analyser le pattern général du puzzle"""
    print("
🎯 ANALYSE PATTERN GÉNÉRAL"    print("=" * 60)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    total_overlap = 0
    total_ajouts = 0
    total_suppressions = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        zones_overlap, zones_ajoutees, zones_supprimees = analyser_differences(input_grid, output_grid, i)

        total_overlap += len(zones_overlap)
        total_ajouts += len(zones_ajoutees)
        total_suppressions += len(zones_supprimees)

    print(f"📊 STATISTIQUES GLOBALES:")
    print(f"  🔄 Total overlaps: {total_overlap}")
    print(f"  ➕ Total ajouts: {total_ajouts}")
    print(f"  ➖ Total suppressions: {total_suppressions}")

    if total_overlap == 0:
        print("
❌ CONCLUSION: AUCUN OVERLAP dans ce puzzle!"        print("   Le pattern est une TRANSFORMATION COMPLÈTE, pas un overlap")
        print("   Notre solution d'apprentissage automatique est CORRECTE!")
    else:
        print("
✅ CONCLUSION: Il y a des overlaps!"        print(f"   {total_overlap} pixels changent de couleur (overlaps réels)")

if __name__ == "__main__":
    analyser_tous_exemples()
    analyser_pattern_general()
