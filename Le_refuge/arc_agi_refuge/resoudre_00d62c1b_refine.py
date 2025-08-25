#!/usr/bin/env python3
"""
🎨 RÉSOLUTION AFFINÉE PUZZLE 3: 00d62c1b
Pattern de remplissage intelligent basé sur l'analyse des exemples
"""

import json

def resoudre_00d62c1b_refine():
    """Résoudre avec une approche plus intelligente"""
    print("🎨 RÉSOLUTION AFFINÉE PUZZLE 3: 00d62c1b")
    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Utiliser une approche adaptative selon la taille
        if len(input_grid) <= 6:
            solution = appliquer_remplissage_simple(input_grid)
        else:
            solution = appliquer_remplissage_intelligent(input_grid)

        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1
        else:
            print("   📊 Analyse des erreurs:")
            analyser_erreurs(solution, output_attendu)

    print(f"\n🎉 SCORE: {success_count}/{len(puzzle_data['train'])}")

    if success_count == len(puzzle_data['train']):
        print("✅ PARFAIT! Résolution du test...")

        test_input = puzzle_data['test'][0]['input']
        if len(test_input) <= 6:
            solution_test = appliquer_remplissage_simple(test_input)
        else:
            solution_test = appliquer_remplissage_intelligent(test_input)

        submission = {"00d62c1b": solution_test}
        with open("submission_00d62c1b_refine.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/5 - Besoin d'affiner encore")

def appliquer_remplissage_simple(grid):
    """Remplissage simple pour petites grilles"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    # Remplir les cases isolées entourées de bleu
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and est_entoure_de_bleu(grid, i, j, 1):
                solution[i][j] = 4

    return solution

def appliquer_remplissage_intelligent(grid):
    """Remplissage intelligent pour grandes grilles"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    # Étape 1: Identifier les régions bleues
    regions_bleues = identifier_regions_bleues(grid)

    # Étape 2: Pour chaque région, identifier les trous internes
    for region in regions_bleues:
        trous = identifier_trous_region(grid, region)
        for trou in trous:
            i, j = trou
            solution[i][j] = 4

    return solution

def est_entoure_de_bleu(grid, i, j, seuil=1):
    """Vérifier si une case est entourée de bleu"""
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    bleus = 0

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 3:
            bleus += 1

    return bleus >= seuil

def identifier_regions_bleues(grid):
    """Identifier les régions connectées de pixels bleus"""
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 3 and not visited[i][j]:
                # Nouvelle région trouvée
                region = []
                pile = [(i, j)]

                while pile:
                    x, y = pile.pop()
                    if not visited[x][y]:
                        visited[x][y] = True
                        region.append((x, y))

                        # Ajouter les voisins bleus
                        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < rows and 0 <= ny < cols:
                                if grid[nx][ny] == 3 and not visited[nx][ny]:
                                    pile.append((nx, ny))

                regions.append(region)

    return regions

def identifier_trous_region(grid, region):
    """Identifier les trous internes d'une région"""
    if not region:
        return []

    rows = len(grid)
    cols = len(grid[0])

    # Trouver les limites de la région
    min_x = min(x for x, y in region)
    max_x = max(x for x, y in region)
    min_y = min(y for x, y in region)
    max_y = max(y for x, y in region)

    # Étendre légèrement les limites
    min_x = max(0, min_x - 1)
    max_x = min(rows - 1, max_x + 1)
    min_y = max(0, min_y - 1)
    max_y = min(cols - 1, max_y + 1)

    trous = []

    # Scanner la zone étendue
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if grid[i][j] == 0:  # Case vide
                # Vérifier si elle est complètement entourée par la région
                if est_interieur_region(grid, region, i, j):
                    trous.append((i, j))

    return trous

def est_interieur_region(grid, region, i, j):
    """Vérifier si une position est à l'intérieur d'une région"""
    # Convertir la région en set pour recherche rapide
    region_set = set(region)

    # Vérifier les 4 directions principales
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    murs_autour = 0

    for di, dj in directions:
        ni, nj = i + di, j + dj
        # Considérer les bords comme des murs
        if (ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]) or
            (ni, nj) in region_set):
            murs_autour += 1

    # Si entouré de tous les côtés, c'est un trou intérieur
    return murs_autour >= 3

def analyser_erreurs(solution, attendu):
    """Analyser les erreurs pour améliorer l'algorithme"""
    rows = len(solution)
    cols = len(solution[0])

    faux_positifs = 0  # Jaunes en trop
    faux_negatifs = 0  # Jaunes manquants

    for i in range(rows):
        for j in range(cols):
            if solution[i][j] == 4 and attendu[i][j] != 4:
                faux_positifs += 1
            elif solution[i][j] != 4 and attendu[i][j] == 4:
                faux_negatifs += 1

    print(f"   Faux positifs (jaunes en trop): {faux_positifs}")
    print(f"   Faux négatifs (jaunes manquants): {faux_negatifs}")

    if faux_positifs > 0 or faux_negatifs > 0:
        print("   💡 Indice: Ajuster les paramètres de détection des trous")

def tester_parametres():
    """Tester différents paramètres"""
    print("
🔧 TEST DE PARAMÈTRES:"    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    exemple = puzzle_data['train'][0]  # Tester sur exemple 1
    input_grid = exemple['input']
    output_attendu = exemple['output']

    # Tester différents seuils
    for seuil in [1, 2, 3, 4]:
        solution = [row[:] for row in input_grid]
        for i in range(len(input_grid)):
            for j in range(len(input_grid[0])):
                if input_grid[i][j] == 0 and est_entoure_de_bleu(input_grid, i, j, seuil):
                    solution[i][j] = 4

        is_correct = solution == output_attendu
        print(f"   Seuil {seuil}: {'✅' if is_correct else '❌'}")

if __name__ == "__main__":
    resoudre_00d62c1b_refine()
    tester_parametres()
