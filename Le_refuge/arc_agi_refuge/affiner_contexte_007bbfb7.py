#!/usr/bin/env python3
"""
🔧 AFFINAGE CONTEXTE 007bbfb7
Améliorer la détection de contexte
"""

import json

def analyser_contexte_detaille():
    print("🔧 ANALYSE DÉTAILLÉE DES CONTEXTES")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']

        print(f"\nEXEMPLE {i}:")
        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        # Analyser les positions des 2
        positions_2 = []
        for x in range(3):
            for y in range(3):
                if input_grid[x][y] == 2:
                    positions_2.append((x, y))

        print(f"Positions 2: {positions_2}")

        # Analyser le contexte
        if positions_2:
            # Vérifier si sur même ligne
            lignes = set(x for x, y in positions_2)
            colonnes = set(y for x, y in positions_2)

            print(f"  Lignes utilisées: {sorted(lignes)}")
            print(f"  Colonnes utilisées: {sorted(colonnes)}")

            # Critères de groupement
            meme_ligne = len(lignes) == 1
            meme_colonne = len(colonnes) == 1
            ligne_complete = meme_ligne and len(positions_2) == 3
            colonne_complete = meme_colonne and len(positions_2) == 3
            adjacent = sont_adjacents(positions_2)

            print(f"  Même ligne: {meme_ligne}")
            print(f"  Même colonne: {meme_colonne}")
            print(f"  Ligne complète: {ligne_complete}")
            print(f"  Colonne complète: {colonne_complete}")
            print(f"  Sont adjacents: {adjacent}")

            # Déterminer le contexte
            if ligne_complete or colonne_complete:
                contexte = "groupe"
            elif adjacent and len(positions_2) >= 2:
                contexte = "groupe"
            else:
                contexte = "isole"

            print(f"  → CONTEXTE: {contexte}")

def sont_adjacents(positions):
    """Vérifier si les positions sont adjacentes"""
    if len(positions) < 2:
        return True

    for i, pos1 in enumerate(positions):
        for pos2 in positions[i+1:]:
            x1, y1 = pos1
            x2, y2 = pos2
            # Distance de Manhattan
            distance = abs(x1 - x2) + abs(y1 - y2)
            if distance > 2:  # Pas adjacent
                return False
    return True

def tester_contexte_ameliore():
    print("\n🧪 TEST CONTEXTE AMÉLIORÉ:")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    patterns = {
        '2_isole': [0, 0, 0, 0, 0, 2, 2, 0, 2],
        '2_groupe': [2, 2, 2, 0, 0, 0, 0, 2, 2],
        4: [4, 0, 4, 0, 0, 0, 0, 4, 0],
        6: [6, 6, 0, 6, 0, 0, 0, 6, 6],
        7: [0, 7, 7, 7, 7, 7, 0, 7, 7],
        0: [0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    reussites = 0
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_ex = exemple['input']
        output_ex = exemple['output']

        solution_ex = appliquer_pattern_contexte_ameliore(input_ex, patterns)

        if solution_ex == output_ex:
            print(f"  Exemple {i}: ✅")
            reussites += 1
        else:
            print(f"  Exemple {i}: ❌")

    print(f"\nScore avec contexte amélioré: {reussites}/5")

def appliquer_pattern_contexte_ameliore(input_3x3, patterns):
    """Appliquer avec contexte amélioré"""
    solution = [[0 for _ in range(9)] for _ in range(9)]

    # Détecter le contexte pour la valeur 2
    contexte_2 = detecter_contexte_ameliore(input_3x3)

    for i in range(3):
        for j in range(3):
            valeur = input_3x3[i][j]

            if valeur == 2:
                pattern = patterns[f'2_{contexte_2}']
            else:
                pattern = patterns[valeur]

            start_i, start_j = i * 3, j * 3

            for x in range(3):
                for y in range(3):
                    solution[start_i + x][start_j + y] = pattern[x * 3 + y]

    return solution

def detecter_contexte_ameliore(input_3x3):
    """Détection de contexte améliorée"""
    positions_2 = []
    for x in range(3):
        for y in range(3):
            if input_3x3[x][y] == 2:
                positions_2.append((x, y))

    if not positions_2:
        return 'isole'

    # Critères de groupement
    lignes = set(x for x, y in positions_2)
    colonnes = set(y for x, y in positions_2)

    meme_ligne = len(lignes) == 1
    meme_colonne = len(colonnes) == 1
    ligne_complete = meme_ligne and len(positions_2) == 3
    colonne_complete = meme_colonne and len(positions_2) == 3
    adjacent = sont_adjacents(positions_2)

    # Nouveau critère: si 3 positions ou plus
    if len(positions_2) >= 3:
        return 'groupe'

    # Si 2 positions adjacentes
    if len(positions_2) == 2 and adjacent:
        return 'groupe'

    return 'isole'

if __name__ == "__main__":
    analyser_contexte_detaille()
    tester_contexte_ameliore()
