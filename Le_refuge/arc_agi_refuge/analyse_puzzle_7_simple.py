#!/usr/bin/env python3
"""
🎨 ANALYSE PUZZLE 7: 03560426
Copulation de formes
"""

import json

def analyser():
    print("🎨 ANALYSE PUZZLE 7: 03560426")
    print("=" * 50)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"Exemples: {len(puzzle_data['train'])}")

    # Premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print(f"Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_grid)}x{len(output_grid[0])}")

    print("INPUT:")
    for row in input_grid:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
            elif cell == 2:
                row_str += "🟢"
            elif cell == 3:
                row_str += "🔵"
            else:
                row_str += "💎"
        print(f"  {row_str}")

    print("OUTPUT:")
    for row in output_grid:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
            elif cell == 2:
                row_str += "🟢"
            elif cell == 3:
                row_str += "🔵"
            else:
                row_str += "💎"
        print(f"  {row_str}")

    # Analyse des formes
    formes_input = identifier_formes(input_grid)
    formes_output = identifier_formes(output_grid)

    print(f"Formes input: {len(formes_input)}")
    print(f"Formes output: {len(formes_output)}")

    # Analyse copulation
    if len(formes_input) > len(formes_output):
        print("PATTERN: FUSION - copulation de formes")
    elif len(formes_input) < len(formes_output):
        print("PATTERN: DIVISION - séparation de formes")
    else:
        print("PATTERN: MODIFICATION - même nombre de formes")

    # Couleurs
    couleurs_input = set()
    couleurs_output = set()

    for row in input_grid:
        for cell in row:
            if cell != 0:
                couleurs_input.add(cell)

    for row in output_grid:
        for cell in row:
            if cell != 0:
                couleurs_output.add(cell)

    print(f"Couleurs input: {sorted(couleurs_input)}")
    print(f"Couleurs output: {sorted(couleurs_output)}")

def identifier_formes(grille):
    """Identifier les formes connectées"""
    rows = len(grille)
    cols = len(grille[0])
    visited = set()
    formes = []

    for i in range(rows):
        for j in range(cols):
            if grille[i][j] != 0 and (i, j) not in visited:
                forme = flood_fill_forme(grille, i, j, visited)
                formes.append(forme)

    return formes

def flood_fill_forme(grille, start_i, start_j, visited):
    """Identifier une forme connectée"""
    rows = len(grille)
    cols = len(grille[0])
    forme = set()
    pile = [(start_i, start_j)]

    couleur = grille[start_i][start_j]

    while pile:
        i, j = pile.pop()
        if (i < 0 or i >= rows or j < 0 or j >= cols or
            (i, j) in visited or grille[i][j] != couleur):
            continue

        visited.add((i, j))
        forme.add((i, j))

        pile.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])

    return forme

if __name__ == "__main__":
    analyser()
