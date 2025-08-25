#!/usr/bin/env python3
"""
🔍 ANALYSE SIMPLE EXEMPLE 4 007bbfb7
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

    print("\nZONES 3x3:")
    for x in range(3):
        for y in range(3):
            valeur = input4[x][y]
            start_i, start_j = x * 3, y * 3
            zone = []
            for i in range(3):
                for j in range(3):
                    zone.append(output4[start_i + i][start_j + j])

            print(f"  Pos ({x},{y})={valeur} -> {zone}")

    # Patterns actuels
    patterns = {
        2: [0, 0, 0, 0, 0, 2, 2, 0, 2],
        4: [4, 0, 4, 0, 0, 0, 0, 4, 0],
        6: [6, 6, 0, 6, 0, 0, 0, 6, 6],
        7: [0, 7, 7, 7, 7, 7, 0, 7, 7],
        0: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    print("\nCOMPARAISON:")
    for x in range(3):
        for y in range(3):
            valeur = input4[x][y]
            start_i, start_j = x * 3, y * 3

            zone_reelle = []
            for i in range(3):
                for j in range(3):
                    zone_reelle.append(output4[start_i + i][start_j + j])

            pattern = patterns[valeur]

            match = zone_reelle == pattern
            print(f"  Pos ({x},{y})={valeur}: {'✅' if match else '❌'}")

            if not match:
                print(f"    Reel: {zone_reelle}")
                print(f"    Pattern: {pattern}")

if __name__ == "__main__":
    analyser_exemple4()
