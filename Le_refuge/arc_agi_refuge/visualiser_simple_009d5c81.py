#!/usr/bin/env python3
"""
🎨 VISUALISATION SIMPLE 009d5c81
Penser comme un humain
"""

import json

def visualiser():
    print("🎨 VISUALISATION 009d5c81")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i}:")

        input_grid = exemple['input']
        output_grid = exemple['output']

        print("INPUT:")
        for row in input_grid:
            row_str = ""
            for cell in row:
                if cell == 0:
                    row_str += "⬜"
                elif cell == 1:
                    row_str += "🔴"
                elif cell == 8:
                    row_str += "🔵"
            print(f"  {row_str}")

        print("OUTPUT:")
        for row in output_grid:
            row_str = ""
            for cell in row:
                if cell == 0:
                    row_str += "⬜"
                elif cell == 1:
                    row_str += "🔴"
                elif cell == 8:
                    row_str += "🔵"
                else:
                    row_str += "🟢"
            print(f"  {row_str}")

        # Analyser changements
        groupe_1_input = sum(1 for row in input_grid for cell in row if cell == 1)
        groupe_8_input = sum(1 for row in input_grid for cell in row if cell == 8)
        groupe_1_output = sum(1 for row in output_grid for cell in row if cell == 1)
        groupe_8_output = sum(1 for row in output_grid for cell in row if cell == 8)

        print(f"Groupe 🔴: {groupe_1_input} -> {groupe_1_output}")
        print(f"Groupe 🔵: {groupe_8_input} -> {groupe_8_output}")

        if groupe_1_input > 0 and groupe_1_output == 0:
            print("  → 🔴 DISPARAÎT COMPLETEMENT")
        if groupe_8_input > 0 and groupe_8_output > 0:
            couleur_sortie = None
            for row in output_grid:
                for cell in row:
                    if cell != 0 and cell != 1:
                        couleur_sortie = cell
                        break
                if couleur_sortie:
                    break
            print(f"  → 🔵 CHANGE DE COULEUR VERS {couleur_sortie}")

if __name__ == "__main__":
    visualiser()
