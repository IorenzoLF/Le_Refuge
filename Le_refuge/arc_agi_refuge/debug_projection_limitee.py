#!/usr/bin/env python3
"""
🔍 DEBUG PATTERN PROJECTION LIMITÉE
"""

import json
from pattern_projection_limitee_double_forme import PatternProjectionLimiteeDoubleForme

def debug_projection_limitee():
    print("🔍 DEBUG PROJECTION LIMITÉE")

    try:
        with open("ARC-AGI-2-main/data/training/0962bcdd.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    pattern = PatternProjectionLimiteeDoubleForme()

    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print(f"Input: {len(input_grid)}x{len(input_grid[0])}")
    print(f"Output: {len(output_grid)}x{len(output_grid[0])}")

    # Extraire couleurs
    couleurs_sequence = []
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] != 0 and input_grid[i][j] not in couleurs_sequence:
                couleurs_sequence.append(input_grid[i][j])

    print(f"Couleurs sequence: {couleurs_sequence}")

    # Test des conditions de base
    print("
CONDITIONS DE BASE:"    print(f"Grille carrée: {len(input_grid) == len(input_grid[0])}")
    print(f"2 couleurs: {len(couleurs_sequence) == 2}")

    # Test détection des formes
    formes = pattern._detecter_deux_formes(input_grid, couleurs_sequence)
    print(f"Formes détectées: {len(formes)}")

    if formes:
        for i, forme in enumerate(formes):
            print(f"  Forme {i}: couleur {forme['couleur']}")
            print(f"    Forme1: {len(forme['forme1'])} positions")
            print(f"    Forme2: {len(forme['forme2'])} positions")

    # Test rectangles
    if formes:
        rectangles = pattern._calculer_rectangles_englobants(formes)
        print(f"Rectangles: {len(rectangles)}")
        for rect in rectangles:
            print(f"  {rect}")

    # Test projection
    if formes:
        confiance = pattern._verifier_projection_limitee(output_grid, couleurs_sequence, rectangles)
        print(".1f")

    # Test complet
    detection = pattern.detecter(input_grid, output_grid)
    print("
DETECTION COMPLETE:"    print(f"Detecte: {detection['detecte']}")
    print(".1f")

    if not detection['detecte']:
        print("DIAGNOSTIC:")
        print(f"  - Couleurs OK: {len(couleurs_sequence) == 2}")
        print(f"  - Grille carrée: {len(input_grid) == len(input_grid[0])}")
        print(f"  - Formes détectées: {len(formes) if 'formes' in locals() else 0}")
        print(f"  - Confiance projection: {confiance if 'confiance' in locals() else 'N/A'}")

if __name__ == "__main__":
    debug_projection_limitee()
