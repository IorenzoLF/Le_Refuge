#!/usr/bin/env python3
"""
ANALYSE INTERACTIONS PUZZLE 15
Comprendre les regles de groupe
"""

import json

def analyse_interactions():
    print("ANALYSE INTERACTIONS PUZZLE 15")
    print("Comprendre les regles de groupe")
    
    with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
        puzzle_data = json.load(f)
    
    # Analyser chaque exemple
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"EXEMPLE {i} - ANALYSE INTERACTIONS:")
        
        input_grid = exemple['input']
        output_grid = exemple['output']
        
        # Positions colorées
        positions_input = []
        for x in range(3):
            for y in range(3):
                if input_grid[x][y] != 0:
                    positions_input.append((x, y))
        
        print(f"  Positions input: {positions_input}")
        
        # Grouper par lignes et colonnes
        lignes = {}
        colonnes = {}
        
        for x, y in positions_input:
            if x not in lignes:
                lignes[x] = []
            lignes[x].append((x, y))
            
            if y not in colonnes:
                colonnes[y] = []
            colonnes[y].append((x, y))
        
        print(f"  Groupes par ligne: {lignes}")
        print(f"  Groupes par colonne: {colonnes}")
        
        # Analyser les patterns par groupe
        if len(positions_input) > 1:
            print("  INTERACTIONS DETECTEES !")
            if len(lignes[1]) == 3:  # Ligne 1 a 3 pixels
                print("  Ligne 1 complete -> meme pattern pour tous")
        
        print()

if __name__ == "__main__":
    analyse_interactions()
