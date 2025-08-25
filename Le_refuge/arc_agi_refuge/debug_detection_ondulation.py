#!/usr/bin/env python3
"""
🔍 DEBUG DÉTECTION PATTERN ONDULATION DIAGONALE
"""

import json
from pattern_ondulation_diagonale import PatternOndulationDiagonale

def debug_detection():
    print("🔍 DEBUG DÉTECTION ONDULATION DIAGONALE")
    print("=" * 50)

    # Charger le puzzle
    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    pattern_ondulation = PatternOndulationDiagonale()

    # Tester l'exemple 2 qui marchait bien dans notre analyse précédente
    exemple = puzzle_data['train'][1]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("📊 DONNÉES DE TEST:")
    print(f"Input: {len(input_grid)}x{len(input_grid[0])}")
    print(f"Output: {len(output_grid)}x{len(output_grid[0])}")

    # Extraire couleurs input
    couleurs_sequence = []
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] != 0 and input_grid[i][j] not in couleurs_sequence:
                couleurs_sequence.append(input_grid[i][j])

    print(f"Couleurs sequence: {couleurs_sequence}")

    # Analyser output_grid
    h, w = len(output_grid), len(output_grid[0])

    print("\n🔍 ANALYSE OUTPUT_GRID:")
    lignes_paires = []
    lignes_impaires = []

    for i in range(h):
        if i % 2 == 0:
            lignes_paires.append(output_grid[i])
            print(f"Ligne {i} (paire): {output_grid[i]}")
        else:
            lignes_impaires.append(output_grid[i])
            print(f"Ligne {i} (impaire): {output_grid[i]}")

    # Vérifier si lignes paires sont identiques
    if len(lignes_paires) > 1:
        toutes_paires_identiques = all(row == lignes_paires[0] for row in lignes_paires)
        print(f"\nLignes paires identiques: {toutes_paires_identiques}")
        print(f"Pattern paire: {lignes_paires[0]}")

    # Vérifier si lignes impaires sont identiques
    if len(lignes_impaires) > 1:
        toutes_impaires_identiques = all(row == lignes_impaires[0] for row in lignes_impaires)
        print(f"Lignes impaires identiques: {toutes_impaires_identiques}")
        print(f"Pattern impaire: {lignes_impaires[0]}")

    # Tester la détection
    print("\n🔍 TEST DÉTECTION:")
    detection = pattern_ondulation.detecter(input_grid, output_grid)
    print(f"Détecté: {detection['detecte']}")
    print(".1f")

    if not detection['detecte']:
        print("❌ DIAGNOSTIC - POURQUOI PAS DÉTECTÉ:")

        # Vérifier chaque condition
        print("1. Couleurs sequence:", "✅" if couleurs_sequence else "❌")
        print("2. Longueur couleurs:", "✅" if len(couleurs_sequence) >= 2 else "❌")
        print("3. Grille carrée:", "✅" if h == w else "❌")
        print("4. Lignes paires identiques:", "✅" if len(lignes_paires) > 1 and all(row == lignes_paires[0] for row in lignes_paires) else "❌")
        print("5. Lignes impaires identiques:", "✅" if len(lignes_impaires) > 1 and all(row == lignes_impaires[0] for row in lignes_impaires) else "❌")

        # Tester propagation diagonale
        if len(lignes_paires) > 0:
            confiance_diagonale = pattern_ondulation._verifier_propagation_diagonale(lignes_paires[0], couleurs_sequence)
            print(".1f")

        # Tester relation patterns
        if len(lignes_paires) > 0 and len(lignes_impaires) > 0:
            confiance_relation = pattern_ondulation._verifier_relation_patterns(lignes_paires[0], lignes_impaires[0], couleurs_sequence)
            print(".1f")

def main():
    debug_detection()

if __name__ == "__main__":
    main()
