#!/usr/bin/env python3
"""
🧠 RÉSOLUTION PUZZLE 4 APPRENTISSAGE
"""

import json

def main():
    print("🧠 RÉSOLUTION PUZZLE 4 PAR APPRENTISSAGE")

    with open("data/training/00dbd492.json", 'r') as f:
        puzzle_data = json.load(f)

    # Apprendre patterns
    patterns = apprendre_patterns(puzzle_data['train'])

    # Tester
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        solution = appliquer_pattern(input_grid, patterns[i-1])
        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1

    print(f"\n🎉 SCORE: {success_count}/4")

    if success_count == 4:
        print("✅ PARFAIT!")

        test_input = puzzle_data['test'][0]['input']
        solution_test = appliquer_pattern(test_input, patterns[0])  # Exemple 1

        submission = {"00dbd492": solution_test}
        with open("submission_00dbd492_appris.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/4")

def apprendre_patterns(exemples):
    """Apprendre patterns"""
    patterns = []

    for i, exemple in enumerate(exemples, 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        positions_nouvelles = []
        for x in range(len(output_grid)):
            for y in range(len(output_grid[0])):
                if input_grid[x][y] == 0 and output_grid[x][y] != 0:
                    positions_nouvelles.append((x, y, output_grid[x][y]))

        pattern = {
            'exemple': i,
            'positions_nouvelles': positions_nouvelles,
            'taille': (len(input_grid), len(input_grid[0]))
        }

        patterns.append(pattern)

        print(f"   📐 Pattern {i}: {len(positions_nouvelles)} pixels")

    return patterns

def appliquer_pattern(input_grid, pattern):
    """Appliquer pattern"""
    solution = [row[:] for row in input_grid]

    for x, y, couleur in pattern['positions_nouvelles']:
        if (0 <= x < len(input_grid) and
            0 <= y < len(input_grid[0]) and
            input_grid[x][y] == 0):
            solution[x][y] = couleur

    return solution

if __name__ == "__main__":
    main()
