#!/usr/bin/env python3
"""
🎯 ANALYSE FINALE - 05269061
Découverte: Pattern d'alternance lignes paires/impaires
"""

import json

def analyse_finale():
    print("🎯 ANALYSE FINALE - 05269061")
    print("=" * 40)
    print("✅ Découverte: Alternance régulière")
    print("✅ Lignes paires: pattern identique")
    print("✅ Lignes impaires: pattern différent")

    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\nEXEMPLE {i}:")
        output_grid = exemple['output']

        print("PATTERN ALTERNANCE:")
        for j, row in enumerate(output_grid):
            parite = "paire" if j % 2 == 0 else "impaire"
            print(f"  Ligne {j} ({parite}): {row}")

        # Analyser l'alternance
        lignes_paires = [output_grid[k] for k in range(0, len(output_grid), 2)]
        lignes_impaires = [output_grid[k] for k in range(1, len(output_grid), 2)]

        pattern_paire = lignes_paires[0] if lignes_paires else None
        pattern_impaire = lignes_impaires[0] if lignes_impaires else None

        print("
ANALYSE:"        if pattern_paire:
            print(f"  Pattern paires: {pattern_paire}")
        if pattern_impaire:
            print(f"  Pattern impairs: {pattern_impaire}")

        # Vérifier relation
        if pattern_paire and pattern_impaire:
            decalages = []
            for decalage in range(-7, 8):
                match = True
                for j in range(len(pattern_paire)):
                    pos = j + decalage
                    if 0 <= pos < len(pattern_impaire):
                        if pattern_paire[j] != pattern_impaire[pos]:
                            match = False
                            break
                    else:
                        match = False
                        break
                if match:
                    decalages.append(decalage)

            if decalages:
                print(f"  Décalages trouvés: {decalages}")

def main():
    analyse_finale()

if __name__ == "__main__":
    main()
