#!/usr/bin/env python3
"""
🔍 ANALYSE DÉTAILLÉE PUZZLE 4: 00dbd492
Identifier les positions exactes des nouvelles couleurs
"""

import json

def analyser_positions_detaillees():
    """Analyser les positions exactes des nouvelles couleurs"""
    print("🔍 ANALYSE DÉTAILLÉE PUZZLE 4: 00dbd492")
    print("=" * 50)

    with open("data/training/00dbd492.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n📐 EXEMPLE {i} - POSITIONS DÉTAILLÉES")

        input_grid = exemple['input']
        output_grid = exemple['output']

        # Identifier toutes les positions où de nouvelles couleurs apparaissent
        nouvelles_couleurs = {
            'bleu': [],      # Couleur 3
            'noir': []       # Couleur 8
        }

        for x in range(len(output_grid)):
            for y in range(len(output_grid[0])):
                if input_grid[x][y] == 0 and output_grid[x][y] != 0:
                    if output_grid[x][y] == 3:
                        nouvelles_couleurs['bleu'].append((x, y))
                    elif output_grid[x][y] == 8:
                        nouvelles_couleurs['noir'].append((x, y))

        print(f"   🔵 Pixels bleus ajoutés: {len(nouvelles_couleurs['bleu'])}")
        print(f"   ⚫ Pixels noirs ajoutés: {len(nouvelles_couleurs['noir'])}")

        if nouvelles_couleurs['bleu']:
            print(f"   Positions bleues: {nouvelles_couleurs['bleu']}")

        if nouvelles_couleurs['noir']:
            print(f"   Positions noires: {nouvelles_couleurs['noir']}")

        # Analyser les patterns
        analyser_pattern_exemple(nouvelles_couleurs, i)

def analyser_pattern_exemple(nouvelles_couleurs, exemple_num):
    """Analyser le pattern spécifique d'un exemple"""
    print("   🎯 ANALYSE DU PATTERN:")

    if exemple_num == 1:
        bleus = nouvelles_couleurs['bleu']
        if bleus:
            x_coords = [x for x, y in bleus]
            y_coords = [y for x, y in bleus]

            print(f"      Zone couverte: x[{min(x_coords)}-{max(x_coords)}], y[{min(y_coords)}-{max(y_coords)}]")
            print("      Type: Remplissage rectangle avec trou central")
    elif exemple_num == 2:
        print("      Type: Remplissage partiel")
    elif exemple_num == 3:
        print("      Type: Remplissage avec motif")
    elif exemple_num == 4:
        bleus = nouvelles_couleurs['bleu']
        noirs = nouvelles_couleurs['noir']

        print(f"      Remplissage bleu: {len(bleus)} pixels")
        print(f"      Points noirs: {len(noirs)} pixels")
        print("      Type: Remplissage + points spécifiques")

def visualiser_avec_nouvelles_couleurs():
    """Visualiser chaque exemple avec les nouvelles couleurs surlignées"""
    print("
🎨 VISUALISATION AVEC NOUVELLES COULEURS:"    print("=" * 50)

    with open("data/training/00dbd492.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🖼️ EXEMPLE {i} AVEC NOUVELLES COULEURS:")

        input_grid = exemple['input']
        output_grid = exemple['output']

        for x in range(len(input_grid)):
            row_str = ""
            for y in range(len(input_grid[0])):
                if input_grid[x][y] == 2:  # Vert original
                    row_str += "🟢"
                elif output_grid[x][y] == 3 and input_grid[x][y] == 0:  # Bleu ajouté
                    row_str += "🔵"
                elif output_grid[x][y] == 8 and input_grid[x][y] == 0:  # Noir ajouté
                    row_str += "⚫"
                elif input_grid[x][y] == 0:
                    row_str += "⬜"
                else:
                    row_str += "⬜"
            print(f"      {row_str}")

def identifier_regles_generales():
    """Identifier les règles générales du puzzle"""
    print("
🎯 RÈGLES GÉNÉRALES IDENTIFIÉES:"    print("=" * 50)

    with open("data/training/00dbd492.json", 'r') as f:
        puzzle_data = json.load(f)

    print("   📋 Observations:")
    print("   1. Les pixels 🟢 (2) restent toujours à leur place")
    print("   2. De nouveaux pixels 🔵 (3) remplissent des zones fermées")
    print("   3. Quelques pixels ⚫ (8) apparaissent à des positions spécifiques")
    print("   4. Les zones remplies sont des 'enclos' fermés par des pixels 🟢")
    print("   5. Le pattern ressemble au puzzle 3 mais avec couleur différente")

    print("
   🔍 HYPOTHÈSE:"    print("   Les pixels 🔵 remplissent les espaces vides complètement")
    print("   entourés par des pixels 🟢 (comme dans puzzle 3)")
    print("   Les pixels ⚫ pourraient être des marqueurs spéciaux")

def comparer_avec_puzzle_3():
    """Comparer avec le pattern du puzzle 3"""
    print("
🔄 COMPARAISON AVEC PUZZLE 3:"    print("=" * 50)

    print("   📊 Puzzle 3 (00d62c1b):")
    print("      - Couleur de remplissage: 🟡 (4)")
    print("      - Pattern: Zones fermées remplies")

    print("   📊 Puzzle 4 (00dbd492):")
    print("      - Couleur de remplissage: 🔵 (3)")
    print("      - Pattern: Zones fermées remplies")
    print("      - Plus: Quelques pixels ⚫ (8)")

    print("
   💡 CONCLUSION:"    print("   Les deux puzzles utilisent le même concept de base:")
    print("   'REMPLIR LES ZONES FERMÉES' mais avec des couleurs différentes")
    print("   Puzzle 3: Zones fermées → 🟡")
    print("   Puzzle 4: Zones fermées → 🔵 + quelques ⚫")

if __name__ == "__main__":
    analyser_positions_detaillees()
    visualiser_avec_nouvelles_couleurs()
    identifier_regles_generales()
    comparer_avec_puzzle_3()
