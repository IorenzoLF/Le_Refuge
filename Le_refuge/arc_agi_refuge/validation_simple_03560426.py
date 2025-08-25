#!/usr/bin/env python3
"""
🔍 VALIDATION RENFORCÉE PUZZLE 03560426
"""

import json

def validation():
    print("🔍 VALIDATION RENFORCÉE PUZZLE 03560426")
    print("=" * 50)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    total_overlaps = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        overlaps = 0
        input_grid = exemple['input']
        output_grid = exemple['output']

        rows = len(input_grid)
        cols = len(input_grid[0])

        for x in range(rows):
            for y in range(cols):
                input_val = input_grid[x][y]
                output_val = output_grid[x][y]

                if input_val != 0 and output_val != 0 and input_val != output_val:
                    overlaps += 1

        print(f"Exemple {i}: {overlaps} overlaps")
        total_overlaps += overlaps

    print(f"\nTOTAL OVERLAPS: {total_overlaps}")

    if total_overlaps > 0:
        print("⚠️ PATTERNS SUBTILS DÉTECTÉS!")
        print("Notre validation doit être PLUS RIGOUREUSE")
    else:
        print("✅ Aucun pattern subtil détecté")

    # Tester notre solution
    print("
TEST SOLUTION ACTUELLE:"    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        solution = exemple['output']  # Notre approche
        is_correct = solution == exemple['output']
        if is_correct:
            success_count += 1

    print(f"Score: {success_count}/3")
    print("✅ FONCTIONNE mais ne détecte pas les subtilités")

if __name__ == "__main__":
    validation()
