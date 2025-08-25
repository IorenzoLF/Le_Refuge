#!/usr/bin/env python3
"""
🎯 RÉSOLUTION PUZZLE 5: 017c7c7b
Approche séquence de blocs 3x2
"""

import json

def resoudre_sequence_blocs():
    """Résoudre avec l'approche séquence de blocs"""
    print("🎯 RÉSOLUTION SÉQUENCE BLOCS PUZZLE 5: 017c7c7b")
    print("=" * 50)
    print("💡 APPROCHE: Séquences de blocs 3x2")

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Tester sur les exemples
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Appliquer l'approche séquence de blocs
        solution = appliquer_sequence_blocs(input_grid)

        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1
        else:
            print("   📊 Échec - Analysons:")
            analyser_echec(solution, output_attendu)

    print(f"\n🎉 SCORE: {success_count}/{len(puzzle_data['train'])}")

    if success_count == len(puzzle_data['train']):
        print("✅ PARFAIT! Approche séquence de blocs validée!")

        # Résoudre le test
        print("💾 Résolution du test...")

        test_input = puzzle_data['test'][0]['input']
        solution_test = appliquer_sequence_blocs(test_input)

        submission = {"017c7c7b": solution_test}
        with open("submission_017c7c7b_sequence.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/3 - Ajustement de l'approche séquence")

def appliquer_sequence_blocs(grid):
    """Appliquer l'approche séquence de blocs"""
    rows = len(grid)
    cols = len(grid[0])

    # Pour une grille 3x6, on a des blocs de 3x2
    if cols == 3 and rows == 6:
        return resoudre_blocs_3x2(grid)
    else:
        # Pour d'autres dimensions, adapter l'approche
        return resoudre_blocs_generique(grid)

def resoudre_blocs_3x2(grid):
    """Résoudre pour des blocs de 3x2"""
    # La grille 3x6 contient 3 blocs de 3x2
    # Chaque bloc fait 3 lignes x 2 colonnes

    # Extraire les blocs
    blocs = []
    for i in range(0, 6, 3):  # Étape de 3 lignes
        bloc = []
        for x in range(3):  # 3 lignes par bloc
            row = []
            for y in range(3):  # 3 colonnes
                row.append(grid[i + x][y])
            bloc.append(row)
        blocs.append(bloc)

    print(f"   🔍 Blocs identifiés: {len(blocs)}")
    for idx, bloc in enumerate(blocs):
        print(f"      Bloc {idx + 1}:")
        for row in bloc:
            row_str = ""
            for cell in row:
                if cell == 0:
                    row_str += "⬜"
                elif cell == 1:
                    row_str += "🔴"
            print(f"        {row_str}")

    # Pour l'exemple 1: séquence bloc1, bloc2, bloc1
    # Donc on doit ajouter un 4ème bloc qui suit la séquence: bloc2

    # Créer la solution étendue (9x3)
    solution = [[0 for _ in range(3)] for _ in range(9)]

    # Copier les 3 premiers blocs (lignes 0-8)
    for i in range(3):  # 3 blocs
        for x in range(3):  # 3 lignes par bloc
            for y in range(3):  # 3 colonnes
                solution[i * 3 + x][y] = grid[i * 3 + x][y]

    # Ajouter le 4ème bloc selon la séquence
    # Séquence: bloc1, bloc2, bloc1, donc le suivant est bloc2
    for x in range(3):
        for y in range(3):
            solution[9 + x][y] = blocs[1][x][y]  # bloc2

    # Transformer tous les pixels rouges en verts
    for i in range(9):
        for j in range(3):
            if solution[i][j] == 1:
                solution[i][j] = 2

    return solution

def resoudre_blocs_generique(grid):
    """Résoudre pour d'autres dimensions"""
    rows = len(grid)
    cols = len(grid[0])

    # Étendre verticalement
    solution = [[0 for _ in range(cols)] for _ in range(9)]

    # Répéter le pattern verticalement
    for i in range(9):
        for j in range(cols):
            original_i = i % rows
            if grid[original_i][j] != 0:
                solution[i][j] = 2  # Rouge -> Vert

    return solution

def analyser_echec(solution, attendu):
    """Analyser les échecs"""
    rows = len(solution)
    cols = len(solution[0])

    erreurs = 0
    for i in range(rows):
        for j in range(cols):
            if i < len(attendu) and solution[i][j] != attendu[i][j]:
                erreurs += 1

    print(f"   Nombre d'erreurs: {erreurs}")

if __name__ == "__main__":
    resoudre_sequence_blocs()
