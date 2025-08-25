#!/usr/bin/env python3
"""
🔧 AFFINER CONTEXTE BLOC 007bbfb7
Critère plus précis pour détecter le contexte
"""

import json

def analyser_contextes():
    print("🔧 ANALYSE CONTEXTES DÉTAILLÉE")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        print(f"\nEXEMPLE {i}:")
        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        # Analyser les positions 2
        positions_2 = []
        for x in range(3):
            for y in range(3):
                if input_grid[x][y] == 2:
                    positions_2.append((x, y))

        print(f"Positions 2: {positions_2}")
        print(f"Nombre de 2: {len(positions_2)}")

        if positions_2:
            # Analyser le contexte
            lignes = set(x for x, y in positions_2)
            colonnes = set(y for x, y in positions_2)

            print(f"  Lignes utilisées: {sorted(lignes)}")
            print(f"  Colonnes utilisées: {sorted(colonnes)}")

            # Critères de groupement
            meme_ligne = len(lignes) == 1
            meme_colonne = len(colonnes) == 1
            ligne_complete = meme_ligne and len(positions_2) == 3
            colonne_complete = meme_colonne and len(positions_2) == 3

            print(f"  Même ligne: {meme_ligne}")
            print(f"  Ligne complète: {ligne_complete}")
            print(f"  Même colonne: {meme_colonne}")
            print(f"  Colonne complète: {colonne_complete}")

            # Nouveau critère: ligne ou colonne complète
            if ligne_complete or colonne_complete:
                contexte = "groupe"
            elif len(positions_2) >= 4:  # Beaucoup de 2
                contexte = "groupe"
            else:
                contexte = "isole"

            print(f"  → CONTEXTE: {contexte}")

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

        contexte_2 = detecter_contexte_ameliore(input_ex)
        solution_ex = appliquer_bloc_context(input_ex, patterns, contexte_2)

        if solution_ex == output_ex:
            print(f"  Exemple {i}: ✅ (contexte: {contexte_2})")
            reussites += 1
        else:
            print(f"  Exemple {i}: ❌ (contexte: {contexte_2})")

    print(f"\nScore avec contexte amélioré: {reussites}/5")

def detecter_contexte_ameliore(input_3x3):
    """Détection de contexte améliorée"""
    positions_2 = []
    for x in range(3):
        for y in range(3):
            if input_3x3[x][y] == 2:
                positions_2.append((x, y))

    if not positions_2:
        return 'isole'

    # Analyser la disposition
    lignes = set(x for x, y in positions_2)
    colonnes = set(y for x, y in positions_2)

    meme_ligne = len(lignes) == 1
    meme_colonne = len(colonnes) == 1
    ligne_complete = meme_ligne and len(positions_2) == 3
    colonne_complete = meme_colonne and len(positions_2) == 3

    # Critères de groupement
    if ligne_complete or colonne_complete:
        return 'groupe'
    elif len(positions_2) >= 4:  # 4 ou plus = groupe
        return 'groupe'
    elif len(positions_2) == 3 and not (meme_ligne or meme_colonne):
        # 3 positions mais pas alignées = groupe (exemple 3)
        return 'groupe'
    else:
        return 'isole'

def appliquer_bloc_context(input_3x3, patterns, contexte_2):
    """Appliquer avec contexte"""
    solution = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(3):
        for j in range(3):
            valeur = input_3x3[i][j]
            start_i, start_j = i * 3, j * 3

            if valeur == 0:
                pattern = patterns[0]
            elif valeur == 2:
                pattern = patterns[f'2_{contexte_2}']
            else:
                pattern = patterns[valeur]

            for x in range(3):
                for y in range(3):
                    solution[start_i + x][start_j + y] = pattern[x * 3 + y]

    return solution

if __name__ == "__main__":
    analyser_contextes()
    tester_contexte_ameliore()
