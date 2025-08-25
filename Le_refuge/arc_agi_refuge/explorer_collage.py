#!/usr/bin/env python3
"""
🔗 EXPLORATION COLLAGE PUZZLE 13
Ta correction : "comment coller les formes ensemble"
"""

import json

def explorer_collage():
    print("🔗 EXPLORATION COLLAGE PUZZLE 13")
    print("=" * 50)
    print("Ta correction: comment coller les formes ensemble")

    with open("data/training/05f2a901.json", 'r') as f:
        puzzle_data = json.load(f)

    # Premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("EXEMPLE 1:")
    print("FORMES SEPAREES (input):")
    visualiser(input_grid)

    print("FORMES COLLEES (output):")
    visualiser(output_grid)

    # Analyser le collage
    print("ANALYSE COLLAGE:")

    formes_input = identifier_formes(input_grid)
    formes_output = identifier_formes(output_grid)

    print(f"Formes input: {len(formes_input)}")
    print(f"Formes output: {len(formes_output)}")

    isoles_input = compter_pixels_isoles(input_grid)
    isoles_output = compter_pixels_isoles(output_grid)

    print(f"Pixels isoles input: {isoles_input}")
    print(f"Pixels isoles output: {isoles_output}")

    if isoles_input > isoles_output:
        print("COLLAGE CONFIRME: Reduction des pixels isoles")
        print("Ta vision du collage est PARFAITE!")
    else:
        print("Pattern different de collage")

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

def identifier_formes(grille):
    rows = len(grille)
    cols = len(grille[0])
    visite = [[False for _ in range(cols)] for _ in range(rows)]
    formes = []

    for i in range(rows):
        for j in range(cols):
            if grille[i][j] != 0 and not visite[i][j]:
                forme = []
                pile = [(i, j)]

                while pile:
                    x, y = pile.pop()
                    if (0 <= x < rows and 0 <= y < cols and
                        grille[x][y] != 0 and not visite[x][y]):
                        visite[x][y] = True
                        forme.append((x, y))

                        pile.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

                if forme:
                    formes.append(forme)

    return formes

def compter_pixels_isoles(grille):
    rows = len(grille)
    cols = len(grille[0])
    pixels_isoles = 0

    for i in range(rows):
        for j in range(cols):
            if grille[i][j] != 0:
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

if __name__ == "__main__":
    explorer_collage()
