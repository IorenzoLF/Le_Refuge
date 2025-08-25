#!/usr/bin/env python3
"""
🔗 ANALYSE COLLAGE DES FORMES PUZZLE 13 (05f2a901)
Ta correction : "comment coller les formes ensemble"
"""

import json

def analyser_collage_formes():
    """Analyser le collage des formes selon ta correction"""
    print("🔗 ANALYSE COLLAGE DES FORMES")
    print("=" * 50)
    print("🎯 TA CORRECTION : COMMENT COLLER LES FORMES ENSEMBLE")
    print("🔄 Perspective différente : assemblage plutôt que rangement")

    with open("data/training/05f2a901.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser chaque exemple sous l'angle du collage
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🔗 EXEMPLE {i} - ANALYSE COLLAGE")
        print("-" * 40)

        input_grid = exemple['input']
        output_grid = exemple['output']

        print("📥 FORMES SÉPARÉES (input):")
        visualiser(input_grid)

        print("📤 FORMES COLLÉES (output):")
        visualiser(output_grid)

        # Analyser le collage des formes
        analyser_collage(input_grid, output_grid, i)

def visualiser(grille):
    """Visualisation avec focus sur les formes"""
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

def analyser_collage(input_grid, output_grid, exemple_num):
    """Analyser le collage des formes selon ta perspective"""
    print("🔗 ANALYSE DU COLLAGE:")

    # Identifier les formes dans l'input
    formes_input = identifier_formes(input_grid)
    print(f"   📥 Formes input identifiées: {len(formes_input)}")

    # Identifier les formes dans l'output
    formes_output = identifier_formes(output_grid)
    print(f"   📤 Formes output identifiées: {len(formes_output)}")

    # Analyser comment les formes se collent
    if len(formes_input) > len(formes_output):
        print("   🔄 COLLAGE : Plusieurs formes → Une forme fusionnée")
        print("   🎯 Ta vision du 'collage' est PARFAITE !")
    elif len(formes_input) == len(formes_output):
        print("   🔄 RÉORGANISATION : Formes redéployées spatialement")
        print("   🎯 'Collage' par repositionnement")
    else:
        print("   ❓ Pattern de collage différent")

    # Analyser la connectivité
    analyser_connectivite(input_grid, output_grid)

def identifier_formes(grille):
    """Identifier les formes connectées"""
    rows = len(grille)
    cols = len(grille[0])
    visite = [[False for _ in range(cols)] for _ in range(rows)]
    formes = []

    for i in range(rows):
        for j in range(cols):
            if grille[i][j] != 0 and not visite[i][j]:
                # Nouvelle forme
                forme = []
                pile = [(i, j)]

                while pile:
                    x, y = pile.pop()
                    if (0 <= x < rows and 0 <= y < cols and
                        grille[x][y] != 0 and not visite[x][y]):
                        visite[x][y] = True
                        forme.append((x, y))

                        # Voisins
                        pile.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

                if forme:
                    formes.append(forme)

    return formes

def analyser_connectivite(input_grid, output_grid):
    """Analyser la connectivité des formes"""
    print("   🔗 ANALYSE CONNECTIVITÉ:")

    # Analyser les pixels isolés vs connectés
    pixels_isoles_input = compter_pixels_isoles(input_grid)
    pixels_isoles_output = compter_pixels_isoles(output_grid)

    print(f"     Pixels isolés input: {pixels_isoles_input}")
    print(f"     Pixels isolés output: {pixels_isoles_output}")

    if pixels_isoles_input > pixels_isoles_output:
        print("     🎯 COLLAGE : Réduction des pixels isolés")
        print("     🔗 Les formes se 'collent' ensemble")

def compter_pixels_isoles(grille):
    """Compter les pixels isolés (sans voisins de même couleur)"""
    rows = len(grille)
    cols = len(grille[0])
    pixels_isoles = 0

    for i in range(rows):
        for j in range(cols):
            if grille[i][j] != 0:
                # Vérifier les voisins
                couleur = grille[i][j]
                a_des_voisins = False

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < rows and 0 <= nj < cols and
                        grille[ni][nj] == couleur):
                        a_des_voisins = True
                        break

                if not a_des_voisins:
                    pixels_isoles += 1

    return pixels_isoles

def analyse_generale_collage():
    """Analyse générale du collage des formes"""
    print("
🎨 ANALYSE GÉNÉRALE COLLAGE"    print("=" * 60)

    with open("data/training/05f2a901.json", 'r') as f:
        puzzle_data = json.load(f)

    total_formes_input = 0
    total_formes_output = 0
    total_isoles_input = 0
    total_isoles_output = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        formes_input = identifier_formes(exemple['input'])
        formes_output = identifier_formes(exemple['output'])

        total_formes_input += len(formes_input)
        total_formes_output += len(formes_output)

        isoles_input = compter_pixels_isoles(exemple['input'])
        isoles_output = compter_pixels_isoles(exemple['output'])

        total_isoles_input += isoles_input
        total_isoles_output += isoles_output

    print("📊 STATISTIQUES COLLAGE:")
    print(f"   Formes totales: {total_formes_input} → {total_formes_output}")
    print(f"   Pixels isolés: {total_isoles_input} → {total_isoles_output}")

    if total_isoles_input > total_isoles_output:
        print("✅ COLLAGE CONFIRMÉ : Réduction des pixels isolés")
        print("🎯 Ta vision du 'collage' est parfaitement exacte !")
    else:
        print("🔍 Pattern de collage différent")

if __name__ == "__main__":
    analyser_collage_formes()
    analyse_generale_collage()
