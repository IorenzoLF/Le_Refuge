#!/usr/bin/env python3
"""
📊 ANALYSE DÉCALAGE SIMPLE - 05269061
"""

import json

def analyser_decalage():
    print("📊 ANALYSE DÉCALAGE - 05269061")
    print("=" * 40)
    print("Description: lignes avec décalage diagonal")

    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i}:")

        input_grid = exemple['input']
        output_grid = exemple['output']

        print("OUTPUT:")
        for j, row in enumerate(output_grid):
            print(f"  Ligne {j}: {row}")

        # Analyser la dernière ligne
        derniere_ligne = output_grid[-1]
        print(f"\nDERNIÈRE LIGNE: {derniere_ligne}")

        # Extraire pattern
        pattern = []
        positions = []
        for j, cell in enumerate(derniere_ligne):
            if cell != 0:
                pattern.append(cell)
                positions.append(j)

        print(f"Pattern: {pattern}")
        print(f"Positions: {positions}")

        # Analyser décalage par ligne
        print("\nDÉCALAGE PAR LIGNE:")
        for k in range(len(output_grid)):
            ligne = output_grid[k]

            # Trouver position du pattern
            decalage_trouve = None
            for decalage in range(-7, 8):
                match = True
                for m, couleur in enumerate(pattern):
                    pos = positions[m] + decalage
                    if 0 <= pos < len(ligne):
                        if ligne[pos] != couleur:
                            match = False
                            break
                    else:
                        match = False
                        break

                if match:
                    decalage_trouve = decalage
                    break

            if decalage_trouve is not None:
                print(f"  Ligne {k}: décalage {decalage_trouve} ✅")
            else:
                print(f"  Ligne {k}: pas de correspondance ❌")

def main():
    analyser_decalage()

if __name__ == "__main__":
    main()
