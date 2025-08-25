#!/usr/bin/env python3
"""
📋 ANALYSE SIMPLE DU CADRE DES PUZZLES
"""

import json
from collections import Counter

def analyser_cadre():
    print("📋 ANALYSE CADRE PUZZLES ARC")

    # Analyser quelques puzzles
    puzzles = ["00576224", "007bbfb7", "009d5c81"]

    for puzzle_id in puzzles:
        print(f"\n🧩 PUZZLE {puzzle_id}")

        try:
            with open(f"data/training/{puzzle_id}.json", 'r') as f:
                puzzle_data = json.load(f)

            print(f"  Training: {len(puzzle_data['train'])} exemples")
            print(f"  Test: {len(puzzle_data['test'])} exemples")

            # Analyser dimensions
            for i, exemple in enumerate(puzzle_data['train'][:1]):
                h_in, w_in = len(exemple['input']), len(exemple['input'][0])
                h_out, w_out = len(exemple['output']), len(exemple['output'][0])
                print(f"  Dimensions: {h_in}x{w_in} -> {h_out}x{w_out}")

            # Analyser couleurs
            couleurs = set()
            for exemple in puzzle_data['train']:
                for grid in [exemple['input'], exemple['output']]:
                    for row in grid:
                        for cell in row:
                            if cell != 0:
                                couleurs.add(cell)
            print(f"  Couleurs: {sorted(couleurs)}")

        except Exception as e:
            print(f"  Erreur: {e}")

def explorer_nouvelle_perspective():
    print("\n🆕 NOUVELLE PERSPECTIVE 007bbfb7")

    try:
        with open("data/training/007bbfb7.json", 'r') as f:
            puzzle_data = json.load(f)

        exemple = puzzle_data['train'][0]
        input_grid = exemple['input']
        output_grid = exemple['output']

        print("INPUT 3x3:")
        for row in input_grid:
            print(f"  {row}")

        print("\nIDEE: Chaque pixel input determine si le bloc est repete")
        print("0 = pas de repetition, couleur = oui repetition")

        for i in range(3):
            for j in range(3):
                valeur = input_grid[i][j]
                start_i, start_j = i * 3, j * 3

                print(f"\nPos ({i},{j}) = {valeur}")
                if valeur == 0:
                    print("  -> Devrait etre vide")
                else:
                    print(f"  -> Devrait repeter bloc avec {valeur}")

                # Zone correspondante
                zone = []
                for x in range(3):
                    for y in range(3):
                        zone.append(output_grid[start_i + x][start_j + y])
                print(f"  -> Zone reelle: {zone}")

    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    analyser_cadre()
    explorer_nouvelle_perspective()
