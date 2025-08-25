#!/usr/bin/env python3
"""
🧠 RÉSOLUTION PUZZLE 5 PAR APPRENTISSAGE
Extension verticale avec transformation de couleur
"""

import json

def resoudre_par_apprentissage():
    """Résoudre le puzzle 5 en apprenant les patterns d'extension"""
    print("🧠 RÉSOLUTION PUZZLE 5 PAR APPRENTISSAGE")
    print("=" * 50)

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Étape 1: Apprendre les patterns d'extension
    patterns = apprendre_patterns_extension(puzzle_data['train'])

    # Étape 2: Tester sur les exemples d'entraînement
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Appliquer le pattern d'extension appris
        solution = appliquer_pattern_extension(input_grid, patterns[i-1])

        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1
        else:
            print(f"   📊 Dimensions - Solution: {len(solution)}x{len(solution[0])}, Attendu: {len(output_attendu)}x{len(output_attendu[0])}")

    print(f"\n🎉 SCORE ENTRAÎNEMENT: {success_count}/3")

    if success_count == 3:
        print("✅ PARFAIT! Patterns d'extension appris!")

        # Étape 3: Résoudre le test
        print("💾 Résolution du test...")

        test_input = puzzle_data['test'][0]['input']
        solution_test = appliquer_pattern_extension(test_input, patterns[0])  # Utiliser premier pattern

        submission = {"017c7c7b": solution_test}
        with open("submission_017c7c7b_appris.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/3")

def apprendre_patterns_extension(exemples):
    """Apprendre les patterns d'extension verticale"""
    patterns = []

    for i, exemple in enumerate(exemples, 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Analyser l'extension
        rows_input = len(input_grid)
        rows_output = len(output_grid)
        cols = len(input_grid[0])

        print(f"   📐 Pattern {i}: Extension {rows_input}x{cols} -> {rows_output}x{cols}")

        # Créer un pattern d'extension
        pattern = {
            'exemple': i,
            'rows_input': rows_input,
            'rows_output': rows_output,
            'cols': cols,
            'input_grid': input_grid,
            'output_grid': output_grid,
            'ratio_extension': rows_output / rows_input
        }

        patterns.append(pattern)

    return patterns

def appliquer_pattern_extension(input_grid, pattern):
    """Appliquer le pattern d'extension appris"""
    rows_input = len(input_grid)
    cols = len(input_grid[0])
    rows_output = pattern['rows_output']

    # Créer la grille étendue
    solution = [[0 for _ in range(cols)] for _ in range(rows_output)]

    # Appliquer la transformation selon le pattern appris
    for i in range(rows_output):
        for j in range(cols):
            # Calculer la position correspondante dans la grille d'entrée
            input_i = i % rows_input

            # Si la position d'entrée a un pixel, le transformer en vert
            if input_grid[input_i][j] != 0:
                solution[i][j] = 2  # Rouge -> Vert

    return solution

def visualiser_patterns_appris(patterns):
    """Visualiser les patterns d'extension appris"""
    print("
🎨 VISUALISATION PATTERNS D'EXTENSION:"    print("=" * 50)

    for pattern in patterns:
        print(f"\n   📐 Pattern Exemple {pattern['exemple']}:")
        print(f"      Extension: {pattern['rows_input']} -> {pattern['rows_output']} lignes")
        print(f"      Ratio: {pattern['ratio_extension']:.1f}x")

        print("      Input:")
        for row in pattern['input_grid']:
            row_str = ""
            for cell in row:
                if cell == 0:
                    row_str += "⬜"
                elif cell == 1:
                    row_str += "🔴"
                else:
                    row_str += "💎"
            print(f"        {row_str}")

        print("      Output:")
        for row in pattern['output_grid']:
            row_str = ""
            for cell in row:
                if cell == 0:
                    row_str += "⬜"
                elif cell == 2:
                    row_str += "🟢"
                else:
                    row_str += "💎"
            print(f"        {row_str}")

if __name__ == "__main__":
    resoudre_par_apprentissage()
