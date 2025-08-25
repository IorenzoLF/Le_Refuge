#!/usr/bin/env python3
"""
Analyse du puzzle 00576224 que nous avons oublie
"""

import json

def analyser_puzzle_oubli():
    print("Analyse du puzzle 00576224 (oublie)")
    print("=" * 40)

    try:
        with open("ARC-AGI-2-main/data/training/00576224.json", 'r') as f:
            puzzle_data = json.load(f)

        print(f"Nombre d'exemples: {len(puzzle_data['train'])}")

        for i, exemple in enumerate(puzzle_data['train'], 1):
            inp = exemple['input']
            out = exemple['output']

            print(f"\nEXEMPLE {i}:")
            print(f"  Input: {len(inp)}x{len(inp[0])}")
            print(f"  Output: {len(out)}x{len(out[0])}")

            # Compter les couleurs
            couleurs_input = set()
            couleurs_output = set()
            for row in inp:
                for cell in row:
                    couleurs_input.add(cell)
            for row in out:
                for cell in row:
                    couleurs_output.add(cell)

            print(f"  Couleurs input: {sorted(couleurs_input)}")
            print(f"  Couleurs output: {sorted(couleurs_output)}")

            # Visualisation simple
            print("  Input:")
            for row in inp:
                print("  " + "".join([str(cell) for cell in row]))

            print("  Output:")
            for row in out:
                print("  " + "".join([str(cell) for cell in row]))

    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    analyser_puzzle_oubli()
