#!/usr/bin/env python3
"""
🏠 EXPLORATION RANGEMENT PUZZLE 13
05f2a901 - Ton intuition "ranger" ou "ordre"
"""

import json

def explorer_rangement():
    print("🏠 EXPLORATION RANGEMENT PUZZLE 13")
    print("=" * 50)
    print("Ton idee: ranger ou ordre")

    with open("data/training/05f2a901.json", 'r') as f:
        puzzle_data = json.load(f)

    # Premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("EXEMPLE 1:")
    print("INPUT:")
    visualiser(input_grid)

    print("OUTPUT:")
    visualiser(output_grid)

    # Analyser selon ton idee de rangement
    print("ANALYSE SELON TON IDEE DE RANGEMENT:")

    # Comparer les organisations
    org_input = analyser_organisation(input_grid)
    org_output = analyser_organisation(output_grid)

    print(f"Input: {org_input}")
    print(f"Output: {org_output}")

    if org_input != org_output:
        print("CHANGEMENT D'ORGANISATION DETECTE!")
        print("Ton intuition de RANGEMENT pourrait etre JUSTE!")

        # Analyser le type de rangement
        if org_output['lignes_utilisees'] < org_input['lignes_utilisees']:
            print("RANGEMENT VERTICAL (compression)")
        elif org_output['lignes_utilisees'] > org_input['lignes_utilisees']:
            print("DEPLIEMENT VERTICAL")
        else:
            print("RANGEMENT HORIZONTAL")

    else:
        print("Meme organisation - peut-etre un autre type de rangement")

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

def analyser_organisation(grille):
    pixels_par_ligne = [sum(1 for cell in row if cell != 0) for row in grille]
    lignes_avec_pixels = sum(1 for count in pixels_par_ligne if count > 0)
    total_pixels = sum(pixels_par_ligne)

    return {
        'lignes_utilisees': lignes_avec_pixels,
        'total_pixels': total_pixels
    }

if __name__ == "__main__":
    explorer_rangement()
