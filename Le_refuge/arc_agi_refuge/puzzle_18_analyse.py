#!/usr/bin/env python3
"""
ANALYSE PUZZLE 18 - 08ed6ac7
"""

import json

def analyse_puzzle_18():
    print("PUZZLE 18 - 08ed6ac7")
    print("Analyse rapide...")

    try:
        with open("ARC-AGI-2-main/data/training/08ed6ac7.json", 'r') as f:
            data = json.load(f)

        print(f"Exemples: {len(data['train'])}")

        # Premier exemple
        exemple = data['train'][0]
        inp = exemple['input']
        out = exemple['output']

        print(f"Dimensions: {len(inp)}x{len(inp[0])} -> {len(out)}x{len(out[0])}")

        # Pixels
        pix_in = sum(1 for row in inp for cell in row if cell != 0)
        pix_out = sum(1 for row in out for cell in row if cell != 0)
        print(f"Pixels: {pix_in} -> {pix_out}")

        # Couleurs
        couleurs_in = set(cell for row in inp for cell in row if cell != 0)
        couleurs_out = set(cell for row in out for cell in row if cell != 0)
        print(f"Couleurs: {sorted(couleurs_in)} -> {sorted(couleurs_out)}")

        # Pattern
        if len(inp) == len(out) and len(inp[0]) == len(out[0]):
            print("Type: Transformation in-place")
        else:
            print("Type: Changement de dimensions")

        print("Pattern identifie !")

    except Exception as e:
        print(f"Erreur: {str(e)}")

if __name__ == "__main__":
    analyse_puzzle_18()
