#!/usr/bin/env python3
"""
🔍 ANALYSE DES POSITIONS JAUNES PUZZLE 3
Identifier exactement où les pixels 🟡 apparaissent
"""

import json

def analyser_positions_jaunes():
    """Analyser les positions exactes des pixels jaunes"""
    print("🔍 ANALYSE POSITIONS JAUNES 00d62c1b")
    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🖼️ EXEMPLE {i} - POSITIONS JAUNES:")

        input_grid = exemple['input']
        output_grid = exemple['output']

        positions_jaunes = []

        for x in range(len(output_grid)):
            for y in range(len(output_grid[0])):
                if output_grid[x][y] == 4 and input_grid[x][y] != 4:
                    positions_jaunes.append((x, y))

        print(f"   Nombre de pixels jaunes: {len(positions_jaunes)}")
        print(f"   Positions: {positions_jaunes}")

        # Analyser le pattern
        if positions_jaunes:
            analyser_pattern_positions(positions_jaunes, i)

def analyser_pattern_positions(positions, exemple_num):
    """Analyser le pattern des positions"""
    print("   📐 ANALYSE DU PATTERN:")

    x_coords = [x for x, y in positions]
    y_coords = [y for x, y in positions]

    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    print(f"      Bounding box: ({min_x},{min_y}) -> ({max_x},{max_y})")
    print(f"      Largeur: {max_y - min_y + 1}, Hauteur: {max_x - min_x + 1}")

    # Regrouper par lignes
    positions_par_ligne = {}
    for x, y in positions:
        if x not in positions_par_ligne:
            positions_par_ligne[x] = []
        positions_par_ligne[x].append(y)

    print("      Répartition par ligne:")
    for ligne in sorted(positions_par_ligne.keys()):
        cols = sorted(positions_par_ligne[ligne])
        print(f"         Ligne {ligne}: colonnes {cols}")

    # Identifier le type de pattern
    if exemple_num == 1:
        print("      Type: Remplissage interne dispersé")
    elif exemple_num == 2:
        print("      Type: Point isolé")
    elif exemple_num == 3:
        print("      Type: Ligne horizontale avec extensions")
    elif exemple_num == 4:
        print("      Type: Pattern complexe multi-zones")
    elif exemple_num == 5:
        print("      Type: Points symétriques")

def visualiser_avec_jaunes():
    """Visualiser chaque exemple avec les pixels jaunes surlignés"""
    print("
🎨 VISUALISATION AVEC JAUNES:"    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🖼️ EXEMPLE {i} AVEC JAUNES:")

        input_grid = exemple['input']
        output_grid = exemple['output']

        for x in range(len(input_grid)):
            row_str = ""
            for y in range(len(input_grid[0])):
                if output_grid[x][y] == 4 and input_grid[x][y] != 4:
                    row_str += "🟡"  # Pixel jaune ajouté
                elif input_grid[x][y] == 3:
                    row_str += "🔵"  # Pixel bleu original
                elif input_grid[x][y] == 0:
                    row_str += "⬜"  # Case vide
                else:
                    row_str += "⚪"  # Autre
            print(f"      {row_str}")

def identifier_regles_generales():
    """Identifier les règles générales du pattern"""
    print("
🎯 RÈGLES GÉNÉRALES IDENTIFIÉES:"    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    print("   📋 Observations:")
    print("   1. Les pixels 🟡 (4) n'apparaissent que sur des cases vides (0)")
    print("   2. Les pixels 🔵 (3) restent toujours à leur place")
    print("   3. Le nombre de pixels 🟡 varie selon la taille de la grille:")
    print("      - 6x6: ~2 pixels")
    print("      - 10x10: 1 à 9 pixels")
    print("      - 20x20: ~31 pixels")
    print("   4. Les pixels 🟡 remplissent des 'trous' ou espaces internes")
    print("   5. Pas de pixels 🟡 aux bords ou dans les grandes zones vides")

    print("
   🔍 HYPOTHÈSE:"    print("   Les pixels 🟡 apparaissent dans les espaces complètement")
    print("   entourés par des pixels 🔵, créant des formes 'remplies'")

if __name__ == "__main__":
    analyser_positions_jaunes()
    visualiser_avec_jaunes()
    identifier_regles_generales()
