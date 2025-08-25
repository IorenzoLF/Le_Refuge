#!/usr/bin/env python3
"""
DECOUVRIR REGLES DE GROUPE PUZZLE 15
"""

import json

def decouvre_regles_groupe():
    print("DECOUVRIR REGLES DE GROUPE PUZZLE 15")
    
    with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
        puzzle_data = json.load(f)
    
    # Analyser exemple 2 (lignes et colonnes completes)
    exemple2 = puzzle_data['train'][1]
    input_grid2 = exemple2['input']
    output_grid2 = exemple2['output']
    
    print("EXEMPLE 2 - LIGNE ET COLONNE COMPLETES:")
    print("Input positions: [(0,1), (1,0), (1,1), (1,2), (2,1)]")
    print("Ligne 1 complete: (1,0), (1,1), (1,2)")
    print("Colonne 1 complete: (0,1), (1,1), (2,1)")
    
    # Pattern pour ligne complete
    positions_ligne1 = []
    for dx in range(3):
        for dy in range(3):
            out_x = 1 * 3 + dx
            out_y = 1 * 3 + dy
            if output_grid2[out_x][out_y] != 0:
                positions_ligne1.append((dx, dy))
    print(f"Pattern ligne complete: {positions_ligne1}")
    
    # Pattern pour colonne complete
    positions_colonne1 = []
    for dx in range(3):
        for dy in range(3):
            out_x = dx
            out_y = 1 * 3 + dy
            if output_grid2[out_x][out_y] != 0:
                positions_colonne1.append((dx, dy))
    print(f"Pattern colonne complete: {positions_colonne1}")
    
    # Sont-ils les memes ?
    if set(positions_ligne1) == set(positions_colonne1):
        print("PATTERN IDENTIQUE POUR LIGNE ET COLONNE COMPLETES !")
    else:
        print("PATTERNS DIFFERENTS")
    
    # Chercher d'autres exemples avec groupes
    print("ANALYSE EXEMPLE 3:")
    exemple3 = puzzle_data['train'][2]
    input_grid3 = exemple3['input']
    output_grid3 = exemple3['output']
    
    positions_input3 = []
    for x in range(3):
        for y in range(3):
            if input_grid3[x][y] != 0:
                positions_input3.append((x, y))
    
    print(f"Input positions: {positions_input3}")
    
    # Verifier groupes
    lignes = {}
    colonnes = {}
    for x, y in positions_input3:
        if x not in lignes:
            lignes[x] = []
        lignes[x].append((x, y))
        if y not in colonnes:
            colonnes[y] = []
        colonnes[y].append((x, y))
    
    print(f"Groupes lignes: {lignes}")
    print(f"Groupes colonnes: {colonnes}")
    
    # Pas de ligne ou colonne complete dans exemple 3
    print("Aucun groupe complet dans exemple 3")

if __name__ == "__main__":
    decouvre_regles_groupe()
