#!/usr/bin/env python3
"""
🎨 RÉSOLUTION PUZZLE 3: 00d62c1b
Pattern de remplissage des trous
"""

import json

def resoudre_00d62c1b():
    """Résoudre le puzzle 00d62c1b"""
    print("🎨 RÉSOLUTION PUZZLE 3: 00d62c1b")
    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Appliquer le pattern
        solution = appliquer_remplissage_trous(input_grid)

        # Vérifier
        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1

    print(f"\n🎉 SCORE: {success_count}/{len(puzzle_data['train'])}")

    if success_count == len(puzzle_data['train']):
        print("✅ PARFAIT! Résolution du test...")

        test_input = puzzle_data['test'][0]['input']
        solution_test = appliquer_remplissage_trous(test_input)

        submission = {"00d62c1b": solution_test}
        with open("submission_00d62c1b_remplissage.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print("⚠️ Pattern à affiner")

def appliquer_remplissage_trous(input_grid):
    """Appliquer le pattern de remplissage"""
    rows = len(input_grid)
    cols = len(input_grid[0])

    solution = [row[:] for row in input_grid]

    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == 0:  # Case vide
                if est_dans_trou(input_grid, i, j):
                    solution[i][j] = 4  # Remplir avec jaune

    return solution

def est_dans_trou(grid, i, j):
    """Déterminer si position dans un trou"""
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    bleus_autour = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            if grid[ni][nj] == 3:
                bleus_autour += 1

    return bleus_autour >= 3

if __name__ == "__main__":
    resoudre_00d62c1b()
