#!/usr/bin/env python3
"""
🎨 RÉSOLUTION PUZZLE 3: 00d62c1b
Pattern de remplissage des trous avec couleur 4 (jaune)
"""

import json

def resoudre_00d62c1b():
    """Résoudre le puzzle 00d62c1b avec le pattern de remplissage"""
    print("🎨 RÉSOLUTION PUZZLE 3: 00d62c1b")
    print("=" * 50)
    print("💡 HYPOTHÈSE: Remplissage des trous avec couleur 🟡 (4)")

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Tester sur les exemples d'entraînement
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Appliquer le pattern de remplissage
        solution = appliquer_remplissage_trous(input_grid)

        # Vérifier le résultat
        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1
        else:
            print("   ❌ ÉCHEC - Analysons la différence:")
            analyser_difference(solution, output_attendu)

    print("
🎉 RÉSULTATS GÉNÉRAUX:"    print(f"   Score: {success_count}/{len(puzzle_data['train'])}")

    if success_count == len(puzzle_data['train']):
        print("   ✅ PARFAIT! Le pattern fonctionne sur tous les exemples!")

        # Résoudre le test
        print("
🧪 RÉSOLUTION DU TEST:"        test_input = puzzle_data['test'][0]['input']
        solution_test = appliquer_remplissage_trous(test_input)

        # Sauvegarder la solution
        submission = {"00d62c1b": solution_test}
        with open("submission_00d62c1b_remplissage.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("   💾 Solution sauvegardée: submission_00d62c1b_remplissage.json")

        # Visualiser le test
        print("   📥 TEST INPUT:")
        visualiser_grille(test_input)
        print("   📤 SOLUTION:")
        visualiser_grille(solution_test)

    else:
        print(f"   ⚠️ Le pattern ne fonctionne que sur {success_count} exemples")
        print("   📝 Il faut affiner l'algorithme de remplissage")

def appliquer_remplissage_trous(input_grid):
    """Appliquer le pattern de remplissage des trous"""
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Créer une copie de la grille
    solution = [row[:] for row in input_grid]

    # Identifier les positions où ajouter des pixels jaunes (4)
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == 0:  # Case vide
                # Vérifier si cette case est entourée de pixels bleus (3)
                # ou si elle est dans un "trou" à l'intérieur d'une forme
                if est_dans_trou(input_grid, i, j):
                    solution[i][j] = 4  # Remplir avec jaune

    return solution

def est_dans_trou(grid, i, j):
    """Déterminer si la position (i,j) est dans un trou à remplir"""
    rows = len(grid)
    cols = len(grid[0])

    # Vérifier les 8 directions autour
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    bleus_autour = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            if grid[ni][nj] == 3:  # Pixel bleu
                bleus_autour += 1

    # Si entouré de plusieurs pixels bleus, c'est probablement un trou
    return bleus_autour >= 3

def visualiser_grille(grille):
    """Visualiser une grille"""
    for row in grille:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 3:
                row_str += "🔵"
            elif cell == 4:
                row_str += "🟡"
            else:
                row_str += "⚪"
        print(f"      {row_str}")

def analyser_difference(solution, attendu):
    """Analyser les différences entre solution et résultat attendu"""
    rows = len(solution)
    cols = len(solution[0])

    erreurs = 0
    for i in range(rows):
        for j in range(cols):
            if solution[i][j] != attendu[i][j]:
                erreurs += 1
                print(f"   Position ({i},{j}): obtenu {solution[i][j]}, attendu {attendu[i][j]}")

    print(f"   Nombre d'erreurs: {erreurs}")

def tester_patterns_alternatifs():
    """Tester d'autres patterns possibles"""
    print("
🔍 TEST DE PATTERNS ALTERNATIFS"    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Pattern 1: Remplissage simple des diagonales
    print("   📐 Pattern 1: Remplissage diagonal")

    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_attendu = exemple['output']

    solution_diag = appliquer_remplissage_diagonal(input_grid)
    is_correct_diag = solution_diag == output_attendu
    print(f"   ✅ SUCCÈS diagonal: {is_correct_diag}")

    # Pattern 2: Remplissage par proximité
    print("   📐 Pattern 2: Remplissage par proximité")

    solution_prox = appliquer_remplissage_proximite(input_grid)
    is_correct_prox = solution_prox == output_attendu
    print(f"   ✅ SUCCÈS proximité: {is_correct_prox}")

def appliquer_remplissage_diagonal(grid):
    """Pattern de remplissage diagonal"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                # Vérifier les diagonales
                diag_positions = [(i-1,j-1), (i-1,j+1), (i+1,j-1), (i+1,j+1)]
                diag_bleus = 0
                for di, dj in diag_positions:
                    if 0 <= di < rows and 0 <= dj < cols:
                        if grid[di][dj] == 3:
                            diag_bleus += 1
                if diag_bleus >= 2:
                    solution[i][j] = 4

    return solution

def appliquer_remplissage_proximite(grid):
    """Pattern de remplissage par proximité"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    # Créer une grille de "scores" de proximité
    scores = [[0 for _ in range(cols)] for _ in range(rows)]

    # Calculer les scores
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 3:
                # Propager le score aux cases voisines
                for di in range(-2, 3):
                    for dj in range(-2, 3):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols:
                            distance = abs(di) + abs(dj)
                            if distance > 0:
                                scores[ni][nj] += 1 / distance

    # Appliquer le seuil
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and scores[i][j] >= 1.5:
                solution[i][j] = 4

    return solution

if __name__ == "__main__":
    resoudre_00d62c1b()
    tester_patterns_alternatifs()
