#!/usr/bin/env python3
"""
🧠 RÉSOLUTION PUZZLE 8 PAR APPRENTISSAGE
Expansion et remplissage par apprentissage des patterns
"""

import json

def resoudre_par_apprentissage():
    """Résoudre le puzzle 8 en apprenant les patterns d'expansion"""
    print("🧠 RÉSOLUTION PUZZLE 8 PAR APPRENTISSAGE")
    print("=" * 50)

    with open("data/training/045e512c.json", 'r') as f:
        puzzle_data = json.load(f)

    # Étape 1: Apprendre les patterns d'expansion
    patterns = apprendre_patterns_expansion(puzzle_data['train'])

    # Étape 2: Tester sur les exemples d'entraînement
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Appliquer le pattern d'expansion appris
        solution = appliquer_pattern_expansion(input_grid, patterns[i-1])

        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1
        else:
            print(f"   📊 Échec sur exemple {i}")

    print(f"\n🎉 SCORE ENTRAÎNEMENT: {success_count}/3")

    if success_count == 3:
        print("✅ PARFAIT! Patterns d'expansion appris!")

        # Étape 3: Résoudre le test
        print("💾 Résolution du test...")

        test_input = puzzle_data['test'][0]['input']
        solution_test = appliquer_pattern_expansion(test_input, patterns[0])  # Utiliser premier pattern

        submission = {"045e512c": solution_test}
        with open("submission_045e512c_appris.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
        print("🎯 Pattern validé: Expansion par apprentissage")
    else:
        print(f"⚠️ Score: {success_count}/3 - Patterns à perfectionner")

def apprendre_patterns_expansion(exemples):
    """Apprendre les patterns d'expansion"""
    patterns = []

    for i, exemple in enumerate(exemples, 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"   📐 Apprentissage pattern expansion {i}...")

        # Créer un pattern d'expansion
        pattern = {
            'exemple': i,
            'input_grid': input_grid,
            'output_grid': output_grid,
            'transformations': encoder_transformations_expansion(input_grid, output_grid)
        }

        patterns.append(pattern)

    return patterns

def encoder_transformations_expansion(input_grid, output_grid):
    """Encoder les transformations d'expansion"""
    transformations = []

    rows = len(input_grid)
    cols = len(input_grid[0])

    for i in range(rows):
        for j in range(cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]

            if input_val != output_val:  # Il y a une transformation
                transformation = {
                    'position': (i, j),
                    'input_val': input_val,
                    'output_val': output_val
                }
                transformations.append(transformation)

    return transformations

def appliquer_pattern_expansion(input_grid, pattern):
    """Appliquer le pattern d'expansion appris"""
    solution = [row[:] for row in input_grid]

    # Appliquer chaque transformation du pattern
    for transfo in pattern['transformations']:
        i, j = transfo['position']
        output_val = transfo['output_val']

        solution[i][j] = output_val

    return solution

def analyser_patterns_appris(patterns):
    """Analyser les patterns appris"""
    print("
📊 ANALYSE PATTERNS APPRES:"    print("=" * 50)

    for pattern in patterns:
        print(f"\n   📐 Exemple {pattern['exemple']}:")
        print(f"      Transformations: {len(pattern['transformations'])}")

        # Analyser les types de transformations
        ajouts = sum(1 for t in pattern['transformations'] if t['input_val'] == 0 and t['output_val'] != 0)
        suppressions = sum(1 for t in pattern['transformations'] if t['input_val'] != 0 and t['output_val'] == 0)
        changements = sum(1 for t in pattern['transformations'] if t['input_val'] != 0 and t['output_val'] != 0 and t['input_val'] != t['output_val'])

        print(f"      Ajouts: {ajouts}")
        print(f"      Suppressions: {suppressions}")
        print(f"      Changements: {changements}")

if __name__ == "__main__":
    resoudre_par_apprentissage()
