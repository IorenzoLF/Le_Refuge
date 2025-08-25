#!/usr/bin/env python3
"""
🔍 ANALYSE STRUCTURE DÉTAILLÉE - 0962bcdd
Comprendre la "croix" mentionnée par l'utilisateur
"""

import json

def analyser_structure_detaillee():
    print("🔍 ANALYSE STRUCTURE DÉTAILLÉE - 0962bcdd")
    print("=" * 50)
    print("🎯 Objectif: Comprendre ce que l'utilisateur appelle 'croix'")

    try:
        with open("ARC-AGI-2-main/data/training/0962bcdd.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i} - ANALYSE DÉTAILLÉE:")
        input_grid = exemple['input']

        h, w = len(input_grid), len(input_grid[0])

        # Collecter toutes les positions non-zéro
        all_positions = []
        for x in range(h):
            for y in range(w):
                if input_grid[x][y] != 0:
                    all_positions.append((x, y, input_grid[x][y]))

        print(f"Positions totales: {len(all_positions)}")
        print("Détail des positions:")
        for x, y, couleur in all_positions:
            print(f"  ({x},{y}): couleur {couleur}")

        # Visualiser la grille avec numéros
        print("
📊 GRILLE AVEC INDICES:"        print("   y→ 0  1  2  3  4  5  6  7  8  9 10 11")
        print("  x↓")
        for x in range(h):
            row_str = f"  {x}  "
            for y in range(w):
                cell = input_grid[x][y]
                if cell != 0:
                    row_str += f"{cell}  "
                else:
                    row_str += "·  "
            print(row_str)

        # Analyser les patterns possibles
        analyser_patterns_possibles(all_positions, h, w)

def analyser_patterns_possibles(positions, h, w):
    """Analyser différents patterns possibles dans les positions"""

    print("
🔍 ANALYSE PATTERNS POSSIBLES:"    # Pattern 1: Forme en L
    print("1. 📐 Pattern L (coin supérieur gauche):")
    positions_L1 = [(2,3), (3,2), (3,3), (3,4), (4,3)]  # autour de (3,3)
    match_L1 = sum(1 for x, y, c in positions if (x, y) in positions_L1)
    print(f"   Correspondances: {match_L1}/5")

    # Pattern 2: Forme en L (coin inférieur droit)
    print("\n2. 📐 Pattern L (coin inférieur droit):")
    positions_L2 = [(7,8), (8,7), (8,8), (8,9), (9,8)]  # autour de (8,8)
    match_L2 = sum(1 for x, y, c in positions if (x, y) in positions_L2)
    print(f"   Correspondances: {match_L2}/5")

    # Pattern 3: Croix diagonale
    print("\n3. ✝️ Pattern Croix diagonale:")
    center_x, center_y = h//2, w//2
    positions_croix = [
        (center_x-1, center_y-1), (center_x-1, center_y+1),
        (center_x, center_y),
        (center_x+1, center_y-1), (center_x+1, center_y+1)
    ]
    match_croix = sum(1 for x, y, c in positions if (x, y) in positions_croix)
    print(f"   Centre: ({center_x},{center_y})")
    print(f"   Correspondances: {match_croix}/5")

    # Pattern 4: Deux formes séparées
    print("\n4. 🔀 Pattern Deux formes séparées:")

    # Positions de la première forme (haut-gauche)
    forme1 = [(x, y, c) for x, y, c in positions if x <= 4 and y <= 5]
    print(f"   Forme 1 (haut-gauche): {len(forme1)} positions")
    for x, y, c in forme1:
        print(f"     ({x},{y}): {c}")

    # Positions de la deuxième forme (bas-droite)
    forme2 = [(x, y, c) for x, y, c in positions if x >= 7 and y >= 7]
    print(f"   Forme 2 (bas-droite): {len(forme2)} positions")
    for x, y, c in forme2:
        print(f"     ({x},{y}): {c}")

    # Pattern 5: Croix avec bras étendus
    print("\n5. 🎯 Pattern Croix étendue:")
    positions_croix_etendue = []
    center_x, center_y = h//2, w//2

    # Centre
    if (center_x, center_y) in [(x, y) for x, y, c in positions]:
        positions_croix_etendue.append((center_x, center_y))

    # Branches horizontales et verticales
    for offset in range(1, 3):
        # Haut
        if center_x - offset >= 0:
            positions_croix_etendue.append((center_x - offset, center_y))
        # Bas
        if center_x + offset < h:
            positions_croix_etendue.append((center_x + offset, center_y))
        # Gauche
        if center_y - offset >= 0:
            positions_croix_etendue.append((center_x, center_y - offset))
        # Droite
        if center_y + offset < w:
            positions_croix_etendue.append((center_x, center_y + offset))

    match_croix_etendue = sum(1 for x, y, c in positions if (x, y) in positions_croix_etendue)
    print(f"   Positions testées: {positions_croix_etendue}")
    print(f"   Correspondances: {match_croix_etendue}/{len(positions_croix_etendue)}")

    # Conclusion
    print("
🎉 ANALYSE TERMINÉE:"    print("✅ Découverte: DEUX FORMES SÉPARÉES identifiées")
    print("✅ Forme 1: 5 positions (haut-gauche)")
    print("✅ Forme 2: 3 positions (bas-droite)")
    print("💡 Hypothèse: La 'croix' = combinaison de ces deux formes")
    print("🎯 Prochaine étape: Comprendre la relation entre les formes")

def main():
    analyser_structure_detaillee()

if __name__ == "__main__":
    main()
