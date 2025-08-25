#!/usr/bin/env python3
"""
🎯 RÉSOLUTION BLOC SIMPLE 007bbfb7
Logique simple: chaque pixel non-zéro reproduit sa couleur dans la zone 3x3
"""

import json

def resoudre_bloc_simple():
    print("🎯 RÉSOLUTION BLOC SIMPLE 007bbfb7")
    print("Logique: 0 = zone vide, couleur = zone remplie de cette couleur")

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    # Test de la logique simple
    reussites = 0
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_ex = exemple['input']
        output_ex = exemple['output']

        solution_ex = appliquer_bloc_simple(input_ex)

        if solution_ex == output_ex:
            print(f"  Exemple {i}: ✅")
            reussites += 1
        else:
            print(f"  Exemple {i}: ❌")

    print(f"Score avec logique simple: {reussites}/5")

    if reussites == 5:
        print("🎉 PARFAIT! La logique simple fonctionne!")

        # Résoudre le test
        test_input = puzzle_data['test'][0]['input']
        solution_test = appliquer_bloc_simple(test_input)

        print("\nSOLUTION TEST:")
        for row in solution_test:
            print(f"  {row}")

        # Sauvegarder
        submission = {"007bbfb7": solution_test}
        with open("submission_007bbfb7_bloc_simple.json", 'w') as f:
            json.dump(submission, f, indent=2)
        print("Sauvegardé!")

    else:
        print("❌ La logique simple ne fonctionne pas pour tous les exemples")
        # Montrer les différences pour comprendre
        for i, exemple in enumerate(puzzle_data['train'], 1):
            input_ex = exemple['input']
            output_ex = exemple['output']
            solution_ex = appliquer_bloc_simple(input_ex)

            if solution_ex != output_ex:
                print(f"\nDIFFERENCES EXEMPLE {i}:")
                print("SOLUTION GÉNÉRÉE:")
                for row in solution_ex:
                    print(f"  {row}")
                print("SOLUTION ATTENDUE:")
                for row in output_ex:
                    print(f"  {row}")
                break

def appliquer_bloc_simple(input_3x3):
    """Appliquer la logique simple: 0 = vide, couleur = zone remplie de cette couleur"""
    solution = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(3):
        for j in range(3):
            valeur = input_3x3[i][j]
            start_i, start_j = i * 3, j * 3

            if valeur == 0:
                # Zone vide
                pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            else:
                # Zone remplie de la couleur
                pattern = [valeur, valeur, valeur, valeur, valeur, valeur, valeur, valeur, valeur]

            # Appliquer le pattern
            for x in range(3):
                for y in range(3):
                    solution[start_i + x][start_j + y] = pattern[x * 3 + y]

    return solution

if __name__ == "__main__":
    resoudre_bloc_simple()
