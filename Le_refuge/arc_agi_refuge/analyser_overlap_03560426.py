#!/usr/bin/env python3
"""
🔍 ANALYSE DÉTAILLÉE OVERLAP PUZZLE 03560426
Examiner les zones de superposition et les couleurs
"""

import json

def analyser_overlap():
    """Analyser les zones d'overlap dans le puzzle 03560426"""
    print("🔍 ANALYSE DÉTAILLÉE OVERLAP PUZZLE 03560426")
    print("=" * 60)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser chaque exemple pour les zones d'overlap
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🎯 EXEMPLE {i} - ANALYSE OVERLAP")
        print("-" * 40)

        input_grid = exemple['input']
        output_grid = exemple['output']

        # Visualiser l'input
        print("📥 INPUT:")
        visualiser_grille(input_grid)

        # Visualiser l'output
        print("📤 OUTPUT:")
        visualiser_grille(output_grid)

        # Analyser les différences pixel par pixel
        analyser_differences(input_grid, output_grid, i)

def visualiser_grille(grille):
    """Visualisation avec coordonnées"""
    for i, row in enumerate(grille):
        row_str = ""
        for j, cell in row:
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
    """Analyser les différences pixel par pixel"""
    print("🔄 DIFFÉRENCES DÉTAILLÉES:")

    rows = len(input_grid)
    cols = len(input_grid[0])

    zones_overlap = []
    zones_ajoutees = []
    zones_supprimees = []

    for i in range(rows):
        for j in range(cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]

            if input_val != output_val:
                position = (i, j)

                if input_val == 0 and output_val != 0:
                    zones_ajoutees.append((position, output_val))
                    print(f"  ➕ AJOUT: ({i},{j}) = {output_val} ({get_couleur_nom(output_val)})")

                elif input_val != 0 and output_val == 0:
                    zones_supprimees.append((position, input_val))
                    print(f"  ➖ SUPPR: ({i},{j}) = {input_val} ({get_couleur_nom(input_val)}) était là")

                else:
                    zones_overlap.append((position, input_val, output_val))
                    print(f"  🔄 OVERLAP: ({i},{j}) = {input_val}→{output_val} ({get_couleur_nom(input_val)}→{get_couleur_nom(output_val)})")

    # Analyser les patterns d'overlap
    analyser_patterns_overlap(zones_overlap, exemple_num)

def get_couleur_nom(couleur):
    """Nom des couleurs"""
    noms = {
        1: "🔴 rouge", 2: "🟢 vert", 3: "🔵 bleu",
        7: "🟤 marron", 8: "⚫ noir"
    }
    return noms.get(couleur, f"couleur_{couleur}")

def analyser_patterns_overlap(zones_overlap, exemple_num):
    """Analyser les patterns d'overlap"""
    print(f"\n🎨 PATTERNS OVERLAP EXEMPLE {exemple_num}:")

    if not zones_overlap:
        print("  ❌ Aucun overlap détecté")
        return

    print(f"  📊 {len(zones_overlap)} zones d'overlap trouvées:")

    # Grouper par type de transformation
    transformations = {}
    for pos, old_color, new_color in zones_overlap:
        key = (old_color, new_color)
        if key not in transformations:
            transformations[key] = []
        transformations[key].append(pos)

    for (old_color, new_color), positions in transformations.items():
        print(f"  🔄 {get_couleur_nom(old_color)} → {get_couleur_nom(new_color)}: {len(positions)} pixels")
        print(f"     Positions: {positions}")

    # Analyser la proximité
    analyser_proximite_overlap(zones_overlap)

def analyser_proximite_overlap(zones_overlap):
    """Analyser la proximité des zones d'overlap"""
    print("
📍 ANALYSE PROXIMITÉ:"    if len(zones_overlap) < 2:
        print("  📊 Pas assez de zones pour analyse de proximité")
        return

    # Calculer distances entre zones d'overlap
    positions = [pos for pos, _, _ in zones_overlap]

    print("  📏 Distances entre zones d'overlap:")
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            pos1 = positions[i]
            pos2 = positions[j]
            distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
            print(f"     ({pos1[0]},{pos1[1]}) ↔ ({pos2[0]},{pos2[1]}): {distance} cases")

def analyser_formes_separees(input_grid, output_grid):
    """Analyser les formes séparées"""
    print("
🔍 ANALYSE FORMES SÉPARÉES:"    # Identifier les formes dans l'input
    formes_input = identifier_formes(input_grid)
    formes_output = identifier_formes(output_grid)

    print(f"  📥 Formes input: {len(formes_input)}")
    for i, forme in enumerate(formes_input):
        pixels = len(forme)
        couleur = input_grid[forme[0][0]][forme[0][1]] if forme else 0
        print(f"     Forme {i+1}: {pixels} pixels, couleur {get_couleur_nom(couleur)}")

    print(f"  📤 Formes output: {len(formes_output)}")
    for i, forme in enumerate(formes_output):
        pixels = len(forme)
        couleur = output_grid[forme[0][0]][forme[0][1]] if forme else 0
        print(f"     Forme {i+1}: {pixels} pixels, couleur {get_couleur_nom(couleur)}")

def identifier_formes(grille):
    """Identifier les formes connectées"""
    rows = len(grille)
    cols = len(grille[0])
    visite = [[False for _ in range(cols)] for _ in range(rows)]
    formes = []

    for i in range(rows):
        for j in range(cols):
            if grille[i][j] != 0 and not visite[i][j]:
                # Trouver une nouvelle forme
                forme = []
                pile = [(i, j)]

                while pile:
                    x, y = pile.pop()
                    if (0 <= x < rows and 0 <= y < cols and
                        grille[x][y] != 0 and not visite[x][y]):
                        visite[x][y] = True
                        forme.append((x, y))

                        # Ajouter voisins
                        pile.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

                if forme:
                    formes.append(forme)

    return formes

if __name__ == "__main__":
    analyser_overlap()
