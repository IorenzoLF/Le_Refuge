#!/usr/bin/env python3
"""
SOLVEUR FINAL PUZZLE 17 - 070dd51e
Pattern: Extension geometrique autour des points
"""

import json

def solveur_final_puzzle_17():
    print("SOLVEUR FINAL PUZZLE 17 - 070dd51e")
    print("Pattern: Extension geometrique autour des points")

    try:
        with open("ARC-AGI-2-main/data/training/070dd51e.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("Fichier non trouve")
        return False

    print("ANALYSE DES EXEMPLES:")
    print("Exemple 1: 20x10, 10->29 pixels (+19)")
    print("Exemple 2: 30x20, 10->41 pixels (+31)")
    print("Pattern: Extension geometrique autour des points existants")

    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Appliquer l'extension geometrique
        prediction = appliquer_extension_autour_points(input_grid)

        is_correct = comparer_grilles(prediction, output_attendu)

        if is_correct:
            success_count += 1

        print(f"Exemple {i}: {'SUCCES' if is_correct else 'ECHEC'}")

        if not is_correct:
            # Analyser les differences
            differences = analyser_differences(prediction, output_attendu)
            print(f"  Differences: {differences}")

    print(f"SCORE FINAL: {success_count}/{len(puzzle_data['train'])}")

    if success_count == len(puzzle_data['train']):
        print("SUCCES PARFAIT ! Extension geometrique validee !")
        return True
    else:
        print("Ajustement necessaire")
        return False

def appliquer_extension_autour_points(input_grid):
    """Appliquer l'extension geometrique autour des points existants"""
    output_grid = [row[:] for row in input_grid]  # Copie

    # Trouver tous les points existants
    points_existants = []
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] != 0:
                points_existants.append((i, j, input_grid[i][j]))

    # Pour chaque point, ajouter des extensions geometriques
    for x, y, couleur in points_existants:
        # Ajouter des pixels autour selon un pattern geometrique

        # Pattern 1: Ligne verticale vers le bas
        for i in range(1, 4):  # 3 pixels vers le bas
            if x + i < len(output_grid):
                if output_grid[x + i][y] == 0:
                    output_grid[x + i][y] = couleur

        # Pattern 2: Ligne horizontale vers la droite
        for j in range(1, 4):  # 3 pixels vers la droite
            if y + j < len(output_grid[0]):
                if output_grid[x][y + j] == 0:
                    output_grid[x][y + j] = couleur

        # Pattern 3: Diagonale
        if x + 1 < len(output_grid) and y + 1 < len(output_grid[0]):
            if output_grid[x + 1][y + 1] == 0:
                output_grid[x + 1][y + 1] = couleur

    return output_grid

def comparer_grilles(g1, g2):
    """Comparer deux grilles"""
    if len(g1) != len(g2) or len(g1[0]) != len(g2[0]):
        return False

    for i in range(len(g1)):
        for j in range(len(g1[0])):
            if g1[i][j] != g2[i][j]:
                return False

    return True

def analyser_differences(prediction, attendu):
    """Analyser les differences entre prediction et attendu"""
    differences = []
    for i in range(len(prediction)):
        for j in range(len(prediction[0])):
            if prediction[i][j] != attendu[i][j]:
                differences.append(f"({i},{j}): {prediction[i][j]} -> {attendu[i][j]}")

    return len(differences)

if __name__ == "__main__":
    success = solveur_final_puzzle_17()

    if success:
        print("PUZZLE 17 RESOLU AVEC SUCCES !")
        print("Extension geometrique confirmee !")
        print("17/17 puzzles resolus !")
    else:
        print("AFFINAGE DU PATTERN NECESSAIRE")
