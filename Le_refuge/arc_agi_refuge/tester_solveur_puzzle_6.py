#!/usr/bin/env python3
"""
🧪 TESTER SOLVEUR SUR PUZZLE 6: 025d127b
Vérifier si notre solveur peut résoudre la transformation structurelle
"""

import json

def tester_solveur_puzzle_6():
    """Tester notre solveur sur le puzzle 6"""
    print("🧪 TEST SOLVEUR SUR PUZZLE 6: 025d127b")
    print("=" * 50)

    with open("data/training/025d127b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Tester sur les exemples d'entraînement
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Essayer différents patterns de transformation
        solution = essayer_patterns_transformation(input_grid)

        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1
        else:
            print("   📊 Échec - Analysons:")
            analyser_echec(solution, output_attendu)

    print(f"\n🎉 SCORE: {success_count}/{len(puzzle_data['train'])}")

    if success_count == len(puzzle_data['train']):
        print("✅ PARFAIT! Le solveur connaît ce pattern!")
        print("💾 Résolution du test...")

        test_input = puzzle_data['test'][0]['input']
        solution_test = essayer_patterns_transformation(test_input)

        submission = {"025d127b": solution_test}
        with open("submission_025d127b_solveur.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/2 - Pattern de transformation structurelle à implémenter")

def essayer_patterns_transformation(grid):
    """Essayer différents patterns de transformation structurelle"""
    # Pattern 1: Translation simple
    solution1 = appliquer_translation(grid)
    if valider_solution(solution1, grid):
        print("   🔄 Pattern utilisé: Translation")
        return solution1

    # Pattern 2: Rotation
    solution2 = appliquer_rotation(grid)
    if valider_solution(solution2, grid):
        print("   🔄 Pattern utilisé: Rotation")
        return solution2

    # Pattern 3: Symétrie
    solution3 = appliquer_symetrie(grid)
    if valider_solution(solution3, grid):
        print("   🔄 Pattern utilisé: Symétrie")
        return solution3

    # Pattern 4: Décalage
    solution4 = appliquer_decalage(grid)
    if valider_solution(solution4, grid):
        print("   🔄 Pattern utilisé: Décalage")
        return solution4

    # Si aucun pattern ne marche, retourner la grille originale
    print("   ❓ Aucun pattern connu détecté")
    return grid

def appliquer_translation(grid):
    """Appliquer une translation des pixels"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [[0 for _ in range(cols)] for _ in range(rows)]

    # Translation vers la droite de 1
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                new_j = (j + 1) % cols
                solution[i][new_j] = grid[i][j]

    return solution

def appliquer_rotation(grid):
    """Appliquer une rotation"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [[0 for _ in range(cols)] for _ in range(rows)]

    # Rotation de 90 degrés
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                solution[j][rows-1-i] = grid[i][j]

    return solution

def appliquer_symetrie(grid):
    """Appliquer une symétrie"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [[0 for _ in range(cols)] for _ in range(rows)]

    # Symétrie horizontale
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                solution[i][cols-1-j] = grid[i][j]

    return solution

def appliquer_decalage(grid):
    """Appliquer un décalage des éléments"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [[0 for _ in range(cols)] for _ in range(rows)]

    # Décalage vers le centre
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                # Décaler vers le centre
                center_j = cols // 2
                if j < center_j:
                    new_j = j + 1
                else:
                    new_j = j - 1
                if 0 <= new_j < cols:
                    solution[i][new_j] = grid[i][j]
                else:
                    solution[i][j] = grid[i][j]

    return solution

def valider_solution(solution, original):
    """Valider qu'une solution est cohérente"""
    # Compter les pixels
    pixels_solution = sum(1 for row in solution for cell in row if cell != 0)
    pixels_original = sum(1 for row in original for cell in row if cell != 0)

    # Le nombre de pixels devrait être le même
    return pixels_solution == pixels_original

def analyser_echec(solution, attendu):
    """Analyser les échecs"""
    rows = len(solution)
    cols = len(solution[0])

    erreurs = 0
    for i in range(rows):
        for j in range(cols):
            if solution[i][j] != attendu[i][j]:
                erreurs += 1

    print(f"   Nombre d'erreurs: {erreurs}")

    # Analyser les types d'erreurs
    faux_positifs = 0  # Pixels mal placés
    faux_negatifs = 0  # Pixels manquants

    for i in range(rows):
        for j in range(cols):
            if solution[i][j] != 0 and attendu[i][j] == 0:
                faux_positifs += 1
            elif solution[i][j] == 0 and attendu[i][j] != 0:
                faux_negatifs += 1

    print(f"   Faux positifs: {faux_positifs}")
    print(f"   Faux négatifs: {faux_negatifs}")

if __name__ == "__main__":
    tester_solveur_puzzle_6()
