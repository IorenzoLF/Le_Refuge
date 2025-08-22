#!/usr/bin/env python3
"""
ANALYSE 00DBD492 - Refuge ARC-AGI
Script pour analyser le pattern contextuel de remplissage
"""

import json
import sys
from pathlib import Path

def analyser_pattern_contextuel():
    """Analyser le pattern contextuel du puzzle 00dbd492"""
    
    # Charger le puzzle
    with open('ARC-AGI-2-main/data/training/00dbd492.json', 'r') as f:
        data = json.load(f)
    
    print("=" * 80)
    print("ANALYSE PATTERN CONTEXTUEL - Puzzle 00dbd492")
    print("=" * 80)
    
    # Analyser chaque exemple
    for i, exemple in enumerate(data['train'], 1):
        print(f"\n📊 EXEMPLE {i}:")
        print("-" * 40)
        
        input_grid = exemple['input']
        output_grid = exemple['output']
        
        # Afficher les grilles
        print("Input:")
        for ligne in input_grid:
            print("  " + " ".join(str(pixel) for pixel in ligne))
        
        print("\nOutput:")
        for ligne in output_grid:
            print("  " + " ".join(str(pixel) for pixel in ligne))
        
        # Analyser les changements
        print(f"\n🔍 ANALYSE DES CHANGEMENTS:")
        hauteur, largeur = len(input_grid), len(input_grid[0])
        
        changements = {}
        for i in range(hauteur):
            for j in range(largeur):
                if input_grid[i][j] == 0 and output_grid[i][j] != 0:
                    couleur_output = output_grid[i][j]
                    if couleur_output not in changements:
                        changements[couleur_output] = []
                    changements[couleur_output].append((i, j))
        
        print(f"Changements détectés:")
        for couleur, pixels in changements.items():
            print(f"  0 → {couleur}: {len(pixels)} pixels")
        
        # Analyser le contexte de chaque couleur
        print(f"\n🎨 ANALYSE CONTEXTUELLE:")
        for couleur, pixels in changements.items():
            print(f"\n  Couleur {couleur}:")
            
            # Analyser la position relative
            positions = []
            for i, j in pixels:
                # Chercher la forme contenante (contour 2)
                forme_info = analyser_forme_contenante(input_grid, i, j)
                positions.append(forme_info)
            
            # Analyser les patterns de position
            analyser_patterns_position(couleur, positions, input_grid)
    
    # Analyser le test
    print(f"\n🧪 ANALYSE DU TEST:")
    print("-" * 40)
    
    test_input = data['test'][0]['input']
    test_output = data['test'][0]['output']
    
    # Analyser les changements du test
    changements_test = {}
    hauteur, largeur = len(test_input), len(test_input[0])
    
    for i in range(hauteur):
        for j in range(largeur):
            if test_input[i][j] == 0 and test_output[i][j] != 0:
                couleur_output = test_output[i][j]
                if couleur_output not in changements_test:
                    changements_test[couleur_output] = []
                changements_test[couleur_output].append((i, j))
    
    print(f"Changements dans le test:")
    for couleur, pixels in changements_test.items():
        print(f"  0 → {couleur}: {len(pixels)} pixels")
        
        # Analyser le contexte pour chaque couleur
        for i, j in pixels[:3]:  # Analyser les 3 premiers
            forme_info = analyser_forme_contenante(test_input, i, j)
            print(f"    Pixel ({i}, {j}): {forme_info}")

def analyser_forme_contenante(grid, i, j):
    """Analyser la forme contenante d'un pixel"""
    hauteur, largeur = len(grid), len(grid[0])
    
    # Chercher les bords de la forme (contour 2)
    min_i, max_i = i, i
    min_j, max_j = j, j
    
    # Étendre vers le haut
    while min_i > 0 and grid[min_i-1][j] == 2:
        min_i -= 1
    
    # Étendre vers le bas
    while max_i < hauteur-1 and grid[max_i+1][j] == 2:
        max_i += 1
    
    # Étendre vers la gauche
    while min_j > 0 and grid[i][min_j-1] == 2:
        min_j -= 1
    
    # Étendre vers la droite
    while max_j < largeur-1 and grid[i][max_j+1] == 2:
        max_j += 1
    
    # Calculer les dimensions
    largeur_forme = max_j - min_j + 1
    hauteur_forme = max_i - min_i + 1
    
    # Calculer la position relative dans la grille
    pos_relative_i = (min_i + max_i) / 2 / hauteur
    pos_relative_j = (min_j + max_j) / 2 / largeur
    
    return {
        'position': (i, j),
        'forme_bords': (min_i, max_i, min_j, max_j),
        'dimensions': (hauteur_forme, largeur_forme),
        'position_relative': (pos_relative_i, pos_relative_j),
        'aire': hauteur_forme * largeur_forme
    }

def analyser_patterns_position(couleur, positions, grid):
    """Analyser les patterns de position pour une couleur donnée"""
    print(f"    Positions: {len(positions)} pixels")
    
    if not positions:
        return
    
    # Analyser les dimensions
    dimensions = [pos['dimensions'] for pos in positions]
    aires = [pos['aire'] for pos in positions]
    positions_rel = [pos['position_relative'] for pos in positions]
    
    print(f"    Dimensions: {dimensions}")
    print(f"    Aires: {aires}")
    print(f"    Positions relatives: {positions_rel}")
    
    # Chercher des patterns
    if len(set(aires)) == 1:
        print(f"    → Pattern: Même aire ({aires[0]})")
    elif len(set(dimensions)) == 1:
        print(f"    → Pattern: Mêmes dimensions ({dimensions[0]})")
    
    # Analyser la position dans la grille
    pos_i_moy = sum(pos[0] for pos in positions_rel) / len(positions_rel)
    pos_j_moy = sum(pos[1] for pos in positions_rel) / len(positions_rel)
    print(f"    → Position moyenne: ({pos_i_moy:.2f}, {pos_j_moy:.2f})")

if __name__ == "__main__":
    analyser_pattern_contextuel()
