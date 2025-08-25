#!/usr/bin/env python3
"""
🎯 EXPLORATION DES COINS DE FORMES
Ton idée : coin bas-droite remplacé par coin haut-gauche
"""

import json

def explorer_coins():
    print("🎯 EXPLORATION DES COINS DE FORMES")
    print("=" * 50)
    print("Ton idée: coin bas-droite -> coin haut-gauche")

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser l'exemple 3 où il y a des overlaps
    exemple = puzzle_data['train'][2]  # Exemple 3
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("EXEMPLE 3:")
    print("INPUT:")
    visualiser(input_grid)

    print("OUTPUT:")
    visualiser(output_grid)

    # Identifier les formes
    formes_input = identifier_formes(input_grid)
    formes_output = identifier_formes(output_grid)

    print(f"Formes input: {len(formes_input)}")
    print(f"Formes output: {len(formes_output)}")

    # Analyser les coins selon ton idée
    analyser_coins_geometriques(formes_input, formes_output)

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

def analyser_coins_geometriques(formes_input, formes_output):
    print("ANALYSE GÉOMÉTRIQUE DES COINS:")

    if len(formes_input) >= 2 and len(formes_output) >= 2:
        # Analyser les deux premières formes
        forme1_input = formes_input[0]
        forme2_input = formes_input[1]

        forme1_output = formes_output[0]
        forme2_output = formes_output[1]

        # Coins de la première forme input
        coin_bd_forme1_input = trouver_coin_bas_droite(forme1_input)
        print(f"  Coin bas-droite forme 1 input: {coin_bd_forme1_input}")

        # Coin de la deuxième forme output (celle qui vient remplacer)
        coin_hg_forme2_output = trouver_coin_haut_gauche(forme2_output)
        print(f"  Coin haut-gauche forme 2 output: {coin_hg_forme2_output}")

        # Vérifier s'il y a correspondance
        if coin_bd_forme1_input and coin_hg_forme2_output:
            print("  🎯 CORRESPONDANCE POTENTIELLE TROUVÉE!")
            print("  🔄 Remplacement de coin détecté selon ton idée")

def trouver_coin_bas_droite(forme):
    if not forme:
        return None
    max_x = max(x for x, y in forme)
    max_y = max(y for x, y in forme)
    return (max_x, max_y) if (max_x, max_y) in forme else None

def trouver_coin_haut_gauche(forme):
    if not forme:
        return None
    min_x = min(x for x, y in forme)
    min_y = min(y for x, y in forme)
    return (min_x, min_y) if (min_x, min_y) in forme else None

if __name__ == "__main__":
    explorer_coins()
