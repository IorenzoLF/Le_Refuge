#!/usr/bin/env python3
"""
DEBUG EXEMPLE 3 PUZZLE 15
Comprendre pourquoi il echoue encore
"""

import json

def debug_exemple3():
    print("DEBUG EXEMPLE 3 PUZZLE 15")
    
    with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
        puzzle_data = json.load(f)
    
    exemple = puzzle_data['train'][2]  # Exemple 3
    input_grid = exemple['input']
    output_attendu = exemple['output']
    
    print("EXEMPLE 3 - ANALYSE DETAILLEE")
    print("Input:")
    for i, row in enumerate(input_grid):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "."
            elif cell == 6:
                row_str += "D"
            else:
                row_str += "?"
        print(f"  {i}: {row_str}")
    
    print("Output attendu:")
    for i, row in enumerate(output_attendu):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "."
            elif cell == 6:
                row_str += "D"
            else:
                row_str += "?"
        print(f"  {i}: {row_str}")
    
    # Positions input
    positions_input = []
    for i in range(3):
        for j in range(3):
            if input_grid[i][j] != 0:
                positions_input.append((i, j))
    
    print(f"Positions input: {positions_input}")
    
    # Groupes
    lignes = {}
    colonnes = {}
    for x, y in positions_input:
        if x not in lignes:
            lignes[x] = []
        lignes[x].append((x, y))
        if y not in colonnes:
            colonnes[y] = []
        colonnes[y].append((x, y))
    
    print(f"Groupes lignes: {lignes}")
    print(f"Groupes colonnes: {colonnes}")
    
    # Aucun groupe complet - utiliser patterns individuels
    patterns_individuels = {
        (0, 0): [(0, 2), (1, 0), (1, 1), (2, 0), (2, 1)],
        (0, 1): [(0, 0), (0, 2), (2, 0), (2, 2)],
        (1, 2): [(0, 0), (0, 2), (2, 0), (2, 2)],
        (2, 2): [(0, 2), (1, 0), (1, 1), (2, 0), (2, 1)]
    }
    
    print("PATTERNS INDIVIDUELS A APPLIQUER:")
    for pos in positions_input:
        pattern = patterns_individuels.get(pos, [])
        print(f"  {pos} -> {pattern}")
    
    # Verifier si les patterns se chevauchent
    print("VERIFICATION CHEVAUCHEMENTS:")
    
    # Simuler l'application
    output_simule = [[0 for _ in range(9)] for _ in range(9)]
    
    for pos in positions_input:
        pattern = patterns_individuels.get(pos, [])
        x, y = pos
        
        for rel_x, rel_y in pattern:
            abs_x = x * 3 + rel_x
            abs_y = y * 3 + rel_y
            output_simule[abs_x][abs_y] = 6  # Couleur
    
    # Comparer avec attendu
    print("COMPARAISON OUTPUT:")
    differences = []
    for i in range(9):
        for j in range(9):
            if output_simule[i][j] != output_attendu[i][j]:
                differences.append(((i, j), output_simule[i][j], output_attendu[i][j]))
    
    print(f"Differences trouvees: {len(differences)}")
    if len(differences) <= 20:
        for pos, simule, attendu in differences:
            print(f"  Position {pos}: {simule} -> {attendu}")

if __name__ == "__main__":
    debug_exemple3()
