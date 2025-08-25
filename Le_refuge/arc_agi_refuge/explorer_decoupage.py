#!/usr/bin/env python3
"""
🎨 EXPLORATION DÉCOUPAGE GÉOMÉTRIQUE
Ligne grise = découpage, superposition de zones
"""

import json

def explorer_decoupage():
    print("🎨 EXPLORATION DÉCOUPAGE GÉOMÉTRIQUE")
    print("=" * 50)
    print("Ton idée: ligne grise = découpage")
    print("Superposition de 2 zones")

    with open("data/training/0520fde7.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser le premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("EXEMPLE 1:")
    print("INPUT AVEC LIGNES GRISES:")
    visualiser(input_grid)

    print("OUTPUT:")
    visualiser(output_grid)

    # Identifier les lignes grises
    lignes_grises = detecter_lignes_grises(input_grid)
    print(f"LIGNES GRISES DETECTEES: {lignes_grises}")

    # Analyser selon ton interprétation
    print("ANALYSE SELON TON IDEE:")
    print("- Ligne grise = marquage de decoupage")
    print("- Enlever la ligne grise")
    print("- Creer 2 zones separees")
    print("- Superposer les zones")
    print("- Determiner conditions de placement")

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
            elif cell == 5:
                row_str += "⚫"  # Ligne grise
            else:
                row_str += "💎"
        print(f"  {i}: {row_str}")

def detecter_lignes_grises(grille):
    lignes_grises = []

    # Lignes horizontales
    for i in range(len(grille)):
        if all(cell == 5 for cell in grille[i]):
            lignes_grises.append(f"Ligne horiz {i}")

    # Colonnes verticales
    for j in range(len(grille[0])):
        if all(grille[i][j] == 5 for i in range(len(grille))):
            lignes_grises.append(f"Colonne vert {j}")

    return lignes_grises

if __name__ == "__main__":
    explorer_decoupage()
