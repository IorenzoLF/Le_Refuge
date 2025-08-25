#!/usr/bin/env python3
"""
🏗️ EXPLORATION ESCALIERS PUZZLE 11 (05269061)
Ton intuition : construire des escaliers de couleur
"""

import json

def explorer_escaliers():
    print("🏗️ EXPLORATION ESCALIERS PUZZLE 11")
    print("=" * 50)
    print("Ton idee: construire des escaliers de couleur")

    with open("data/training/05269061.json", 'r') as f:
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

    # Analyser selon ton idee
    print("ANALYSE SELON TON IDEE D'ESCALIERS:")

    # Chercher patterns d'escaliers
    escaliers_input = chercher_escaliers(input_grid)
    escaliers_output = chercher_escaliers(output_grid)

    print(f"Escaliers input: {len(escaliers_input)}")
    print(f"Escaliers output: {len(escaliers_output)}")

    if escaliers_input or escaliers_output:
        print("✅ PATTERNS D'ESCALIERS DETECTES !")
        print("🎯 Ton intuition pourrait etre JUSTE !")
    else:
        print("❓ Pas d'escaliers evidents")
        print("🔍 Peut-etre un pattern different d'escaliers")

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

def chercher_escaliers(grille):
    """Chercher des patterns d'escaliers"""
    escaliers = []

    # Escalier horizontal simple
    for i in range(len(grille)):
        row = grille[i]
        if est_escalier_horizontal(row):
            escaliers.append(f"Escalier horizontal ligne {i}")

    # Escalier vertical simple
    for j in range(len(grille[0])):
        col = [grille[i][j] for i in range(len(grille))]
        if est_escalier_vertical(col):
            escaliers.append(f"Escalier vertical colonne {j}")

    return escaliers

def est_escalier_horizontal(ligne):
    """Verifie si une ligne forme un escalier"""
    couleurs = [c for c in ligne if c != 0]
    if len(couleurs) < 2:
        return False

    # Vérifier s'il y a une progression
    changements = 0
    for i in range(1, len(couleurs)):
        if couleurs[i] != couleurs[i-1]:
            changements += 1

    return changements >= 1  # Au moins un changement

def est_escalier_vertical(colonne):
    """Verifie si une colonne forme un escalier"""
    couleurs = [c for c in colonne if c != 0]
    if len(couleurs) < 2:
        return False

    # Vérifier s'il y a une progression
    changements = 0
    for i in range(1, len(couleurs)):
        if couleurs[i] != couleurs[i-1]:
            changements += 1

    return changements >= 1  # Au moins un changement

if __name__ == "__main__":
    explorer_escaliers()
