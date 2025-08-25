#!/usr/bin/env python3
"""
🔍 ANALYSE EXEMPLE 4 007bbfb7
Trouver le pattern correct
"""

import json

def analyser_exemple4():
    print("🔍 ANALYSE EXEMPLE 4 007bbfb7")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    exemple4 = puzzle_data['train'][3]
    input4 = exemple4['input']
    output4 = exemple4['output']

    print("EXEMPLE 4:")
    print("INPUT:")
    for row in input4:
        print(f"  {row}")

    print("\nZONES 3x3 DÉTAILLÉES:")
    for x in range(3):
        for y in range(3):
            valeur = input4[x][y]
            start_i, start_j = x * 3, y * 3
            zone = []
            print(f"\nPos ({x},{y}) = {valeur}:")

            for i in range(3):
                row_zone = []
                for j in range(3):
                    val = output4[start_i + i][start_j + j]
                    row_zone.append(val)
                zone.extend(row_zone)
                print(f"  Row {i}: {row_zone}")

            print(f"  Pattern complet: {zone}")

    # Comparer avec mes patterns actuels
    patterns_actuels = {
        2: [0, 0, 0, 0, 0, 2, 2, 0, 2],  # Corrigé
        4: [4, 0, 4, 0, 0, 0, 0, 4, 0],
        6: [6, 6, 0, 6, 0, 0, 0, 6, 6],
        7: [0, 7, 7, 7, 7, 7, 0, 7, 7],
        0: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    print("\nCOMPARAISON AVEC PATTERNS ACTUELS:")

    # Tester chaque position
    for x in range(3):
        for y in range(3):
            valeur = input4[x][y]
            start_i, start_j = x * 3, y * 3

            # Zone réelle
            zone_reelle = []
            for i in range(3):
                for j in range(3):
                    zone_reelle.append(output4[start_i + i][start_j + j])

            # Zone avec mon pattern
            pattern_actuel = patterns_actuels[valeur]

            print(f"\nPos ({x},{y}) = {valeur}:")
            print(f"  Réel:      {zone_reelle}")
            print(f"  Mon pattern: {pattern_actuel}")
            print(f"  Match: {'✅' if zone_reelle == pattern_actuel else '❌'}")

            if zone_reelle != pattern_actuel:
                print("  ❌ DIFFERENCES:"                for i in range(9):
                    if zone_reelle[i] != pattern_actuel[i]:
                        print(f"     Pos {i}: {pattern_actuel[i]} -> {zone_reelle[i]}")

    # Vérifier si le pattern pour 2 change selon le contexte
    print("\n🔍 ANALYSE SPÉCIFIQUE VALEUR 2:")
    positions_2 = [(x, y) for x in range(3) for y in range(3) if input4[x][y] == 2]

    for x, y in positions_2:
        start_i, start_j = x * 3, y * 3
        zone = []
        for i in range(3):
            for j in range(3):
                zone.append(output4[start_i + i][start_j + j])

        print(f"  Pos ({x},{y})=2 -> {zone}")

if __name__ == "__main__":
    analyser_exemple4()
