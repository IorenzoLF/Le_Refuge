#!/usr/bin/env python3
"""
🧪 TESTER SOLVEUR SUR PUZZLE 5: 017c7c7b
Vérifier si notre solveur peut résoudre l'extension verticale
"""

import json

def tester_solveur_puzzle_5():
    """Tester notre solveur sur le puzzle 5"""
    print("🧪 TEST SOLVEUR SUR PUZZLE 5: 017c7c7b")
    print("=" * 50)

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Tester sur les exemples d'entraînement
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Essayer différents patterns
        solution = essayer_patterns(input_grid)

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
        solution_test = essayer_patterns(test_input)

        submission = {"017c7c7b": solution_test}
        with open("submission_017c7c7b_solveur.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/3 - Pattern d'extension verticale à implémenter")

def essayer_patterns(grid):
    """Essayer différents patterns d'extension"""
    # Pattern 1: Extension verticale simple
    solution1 = appliquer_extension_verticale(grid)
    if valider_solution(solution1, grid):
        print("   🔄 Pattern utilisé: Extension verticale")
        return solution1

    # Pattern 2: Extension avec répétition
    solution2 = appliquer_extension_repetition(grid)
    if valider_solution(solution2, grid):
        print("   🔄 Pattern utilisé: Extension avec répétition")
        return solution2

    # Pattern 3: Transformation couleur avec extension
    solution3 = appliquer_transformation_extension(grid)
    if valider_solution(solution3, grid):
        print("   🔄 Pattern utilisé: Transformation + extension")
        return solution3

    # Si aucun pattern ne marche, retourner la grille originale
    print("   ❓ Aucun pattern connu détecté")
    return grid

def appliquer_extension_verticale(grid):
    """Appliquer une extension verticale simple"""
    rows = len(grid)
    cols = len(grid[0])

    # Doubler verticalement et transformer couleur
    extended_rows = rows * 2  # Doubler
    solution = [[0 for _ in range(cols)] for _ in range(extended_rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                # Placer dans la nouvelle grille avec transformation de couleur
                solution[i][j] = 2  # Rouge -> Vert
                solution[i + rows][j] = 2  # Répéter en bas

    return solution

def appliquer_extension_repetition(grid):
    """Appliquer extension avec répétition du motif"""
    rows = len(grid)
    cols = len(grid[0])

    # Étendre à 9 lignes (comme dans l'exemple)
    solution = [[0 for _ in range(cols)] for _ in range(9)]

    # Copier le pattern original
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                solution[i][j] = 2  # Transformer en vert

    # Répéter le pattern dans les lignes supplémentaires
    for i in range(rows, 9):
        for j in range(cols):
            original_i = i % rows
            if grid[original_i][j] != 0:
                solution[i][j] = 2

    return solution

def appliquer_transformation_extension(grid):
    """Appliquer transformation de couleur avec extension"""
    rows = len(grid)
    cols = len(grid[0])

    # Étendre et transformer
    solution = [[0 for _ in range(cols)] for _ in range(9)]

    for i in range(9):
        for j in range(cols):
            original_i = i % rows
            if grid[original_i][j] != 0:
                solution[i][j] = 2  # Rouge -> Vert

    return solution

def valider_solution(solution, original):
    """Valider qu'une solution est cohérente"""
    # Vérifier que les dimensions sont correctes
    if len(solution) < len(original) or len(solution[0]) != len(original[0]):
        return False

    # Vérifier qu'il y a des pixels dans la solution
    pixels_solution = sum(1 for row in solution for cell in row if cell != 0)
    pixels_original = sum(1 for row in original for cell in row if cell != 0)

    return pixels_solution >= pixels_original

def analyser_echec(solution, attendu):
    """Analyser pourquoi une solution a échoué"""
    rows = len(solution)
    cols = len(solution[0])

    erreurs = 0
    for i in range(rows):
        for j in range(cols):
            if i < len(attendu) and solution[i][j] != attendu[i][j]:
                erreurs += 1

    print(f"   Nombre d'erreurs: {erreurs}")

    # Analyser les types d'erreurs
    faux_positifs = 0  # Pixels en trop
    faux_negatifs = 0  # Pixels manquants

    for i in range(len(attendu)):
        for j in range(cols):
            if solution[i][j] != 0 and attendu[i][j] == 0:
                faux_positifs += 1
            elif solution[i][j] == 0 and attendu[i][j] != 0:
                faux_negatifs += 1

    print(f"   Faux positifs: {faux_positifs}")
    print(f"   Faux négatifs: {faux_negatifs}")

if __name__ == "__main__":
    tester_solveur_puzzle_5()
