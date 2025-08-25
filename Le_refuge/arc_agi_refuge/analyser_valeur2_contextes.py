#!/usr/bin/env python3
"""
🔍 ANALYSE VALEUR 2 DANS DIFFÉRENTS CONTEXTES
Trouver pourquoi le pattern change
"""

import json

def analyser_valeur2_contextes():
    print("🔍 ANALYSE VALEUR 2 DANS DIFFÉRENTS CONTEXTES")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    print("PATTERNS POUR VALEUR 2 SELON LES EXEMPLES:")

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"\nEXEMPLE {i}:")

        # Trouver toutes les positions avec 2
        positions_2 = []
        for x in range(3):
            for y in range(3):
                if input_grid[x][y] == 2:
                    start_i, start_j = x * 3, y * 3
                    zone = []
                    for a in range(3):
                        for b in range(3):
                            zone.append(output_grid[start_i + a][start_j + b])

                    positions_2.append({
                        'pos': (x, y),
                        'zone': zone
                    })

        if positions_2:
            print(f"  Positions avec 2: {len(positions_2)}")
            for pos_info in positions_2:
                print(f"    Pos {pos_info['pos']}: {pos_info['zone']}")

            # Vérifier si tous les patterns sont identiques
            zones = [p['zone'] for p in positions_2]
            unique_zones = []
            for zone in zones:
                if zone not in unique_zones:
                    unique_zones.append(zone)

            if len(unique_zones) == 1:
                print(f"  ✅ Pattern cohérent: {unique_zones[0]}")
            else:
                print(f"  ⚠️  Patterns différents: {len(unique_zones)} patterns")
                for j, zone in enumerate(unique_zones):
                    print(f"     Pattern {j+1}: {zone}")
        else:
            print("  Aucune position avec 2")

    # Analyser les contextes
    print("
🎯 ANALYSE DES CONTEXTES:"    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        print(f"\nEXEMPLE {i} - CONTEXTE:")
        print("  Input:")
        for row in input_grid:
            print(f"    {row}")

        # Compter les occurrences de chaque valeur
        valeurs_count = {}
        for row in input_grid:
            for cell in row:
                if cell != 0:
                    valeurs_count[cell] = valeurs_count.get(cell, 0) + 1

        print(f"  Distribution des valeurs: {valeurs_count}")

        # Voir les positions des 2
        positions_2 = [(x, y) for x in range(3) for y in range(3) if input_grid[x][y] == 2]
        if positions_2:
            print(f"  Positions des 2: {positions_2}")

    # Hypothèse: le pattern dépend du contexte
    print("
💡 HYPOTHÈSE:"    print("  Le pattern pour 2 pourrait dépendre:")
    print("  - Du nombre de 2 présents")
    print("  - De leur position relative")
    print("  - Des autres valeurs présentes")

if __name__ == "__main__":
    analyser_valeur2_contextes()
