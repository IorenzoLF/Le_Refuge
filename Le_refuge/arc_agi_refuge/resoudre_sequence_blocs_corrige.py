#!/usr/bin/env python3
"""
🎯 RÉSOLUTION CORRIGÉE PUZZLE 5: 017c7c7b
Blocs de 3x2 correctement implémentés
"""

import json

def resoudre_sequence_blocs_corrige():
    """Résoudre avec l'approche séquence de blocs corrigée"""
    print("🎯 RÉSOLUTION CORRIGÉE SÉQUENCE BLOCS")
    print("=" * 50)

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Tester sur le premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_attendu = exemple['output']

    print(f"📐 EXEMPLE 1 - Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_attendu)}x{len(output_attendu[0])}")

    print("\nINPUT ORIGINAL:")
    for i, row in enumerate(input_grid):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
        print(f"  {i}: {row_str}")

    print("\nOUTPUT ATTENDU:")
    for i, row in enumerate(output_attendu):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 2:
                row_str += "🟢"
        print(f"  {i}: {row_str}")

    # Appliquer la logique des blocs 3x2
    solution = appliquer_blocs_3x2(input_grid)

    print("\nSOLUTION CALCULÉE:")
    for i, row in enumerate(solution):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 2:
                row_str += "🟢"
        print(f"  {i}: {row_str}")

    # Vérifier
    is_correct = solution == output_attendu
    print(f"\n✅ RÉSULTAT: {'SUCCÈS' if is_correct else 'ÉCHEC'}")

def appliquer_blocs_3x2(grid):
    """Appliquer correctement la logique des blocs 3x2"""
    # Grille 6x3 contient 3 blocs de 3x2 disposés verticalement
    # Chaque bloc: 3 lignes x 3 colonnes (mais seulement 2 colonnes utilisées? Attends...)

    # Attends, l'utilisateur a dit "blocs de 3x2" mais la grille est 3x6...
    # Je pense qu'il veut dire des blocs de 3x2 disposés horizontalement

    # Regardons la grille 3x6:
    # Ligne 0: ⬜🔴⬜ 🔴⬜🔴  -> 2 blocs de 3x2
    # Ligne 1: 🔴⬜🔴 ⬜🔴⬜  -> 2 blocs de 3x2
    # Ligne 2: ⬜🔴⬜ 🔴⬜🔴  -> 2 blocs de 3x2

    # Donc: Bloc1, Bloc2, Bloc1 (séquence)

    # Extraire les blocs horizontaux
    blocs = []

    # Chaque bloc fait 3x2
    for start_col in range(0, 6, 2):  # Étape de 2 colonnes
        bloc = []
        for row in range(3):  # 3 lignes
            row_data = []
            for col in range(2):  # 2 colonnes
                if start_col + col < 6:
                    row_data.append(grid[row][start_col + col])
                else:
                    row_data.append(0)  # Padding si nécessaire
            bloc.append(row_data)
        blocs.append(bloc)

    print(f"   🔍 {len(blocs)} blocs de 3x2 identifiés:")
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

    # La séquence est: Bloc1, Bloc2, Bloc1
    # Donc on doit étendre avec: Bloc2, Bloc1, Bloc2, etc.

    # Créer la solution 9x3
    solution = [[0 for _ in range(3)] for _ in range(9)]

    # Remplir les 6 premières lignes (input original transformé)
    for i in range(6):
        for j in range(3):
            if grid[i][j] == 1:
                solution[i][j] = 2  # Rouge -> Vert

    # Ajouter les 3 lignes d'extension selon la séquence
    sequence = [1, 2, 1]  # Indices des blocs: 0, 1, 0

    for ext_idx in range(3):  # 3 lignes d'extension
        bloc_idx = sequence[ext_idx % len(sequence)]
        bloc = blocs[bloc_idx]

        for row_in_bloc in range(3):
            for col_in_bloc in range(2):
                solution_row = 6 + ext_idx * 1 + row_in_bloc  # Calcul de la ligne
                solution_col = col_in_bloc * 2 + (ext_idx % 2) * 2  # Calcul de la colonne

                if solution_row < 9 and solution_col < 3:
                    if bloc[row_in_bloc][col_in_bloc] == 1:
                        solution[solution_row][solution_col] = 2

    return solution

if __name__ == "__main__":
    resoudre_sequence_blocs_corrige()
