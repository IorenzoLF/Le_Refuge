#!/usr/bin/env python3
"""
🎯 RÉSOLUTION SIMPLE PUZZLE 5: 017c7c7b
Extension verticale simple selon séquence
"""

import json

def resoudre_simple():
    """Résoudre avec extension verticale simple"""
    print("🎯 RÉSOLUTION SIMPLE PUZZLE 5")
    print("=" * 50)

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Tester tous les exemples
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        solution = extension_verticale_simple(input_grid)
        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1

    print(f"\n🎉 SCORE: {success_count}/3")

    if success_count == 3:
        print("✅ PARFAIT! Extension verticale validée!")

        test_input = puzzle_data['test'][0]['input']
        solution_test = extension_verticale_simple(test_input)

        submission = {"017c7c7b": solution_test}
        with open("submission_017c7c7b_simple.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/3")

def extension_verticale_simple(grid):
    """Extension verticale simple: répéter le pattern"""
    rows_input = len(grid)
    cols = len(grid[0])

    # Créer une grille de 9 lignes
    solution = [[0 for _ in range(cols)] for _ in range(9)]

    # Remplir avec le pattern répété
    for i in range(9):
        for j in range(cols):
            # Répéter le pattern de l'input
            original_i = i % rows_input
            if grid[original_i][j] != 0:
                solution[i][j] = 2  # Rouge -> Vert

    return solution

def visualiser_exemple(exemple_num=1):
    """Visualiser un exemple pour comprendre"""
    print(f"\n📊 VISUALISATION EXEMPLE {exemple_num}:")

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    exemple = puzzle_data['train'][exemple_num - 1]
    input_grid = exemple['input']
    output_attendu = exemple['output']

    print("INPUT (6x3):")
    for row in input_grid:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
        print(f"  {row_str}")

    print("OUTPUT ATTENDU (9x3):")
    for row in output_attendu:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 2:
                row_str += "🟢"
        print(f"  {row_str}")

    solution = extension_verticale_simple(input_grid)
    print("SOLUTION CALCULÉE (9x3):")
    for row in solution:
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 2:
                row_str += "🟢"
        print(f"  {row_str}")

    is_correct = solution == output_attendu
    print(f"✅ CORRECT: {is_correct}")

if __name__ == "__main__":
    visualiser_exemple(1)
    resoudre_simple()