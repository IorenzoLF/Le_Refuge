#!/usr/bin/env python3
"""
🧪 TESTER SOLVEUR SUR PUZZLE 8: 045e512c
Vérifier si notre solveur peut résoudre l'expansion
"""

import json

def tester_solveur_puzzle_8():
    """Tester notre solveur sur le puzzle 8"""
    print("🧪 TEST SOLVEUR SUR PUZZLE 8: 045e512c")
    print("=" * 50)

    with open("data/training/045e512c.json", 'r') as f:
        puzzle_data = json.load(f)

    # Tester sur les exemples d'entraînement
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Essayer différents patterns d'expansion
        solution = essayer_patterns_expansion(input_grid)

        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1
        else:
            print("   📊 Échec - Analysons:")
            analyser_echec(solution, output_attendu)

    print(f"\n🎉 SCORE: {success_count}/{len(puzzle_data['train'])}")

    if success_count == len(puzzle_data['train']):
        print("✅ PARFAIT! Le solveur connaît ce pattern!")
        print("💾 Résolution du test...")

        test_input = puzzle_data['test'][0]['input']
        solution_test = essayer_patterns_expansion(test_input)

        submission = {"045e512c": solution_test}
        with open("submission_045e512c_solveur.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/3 - Pattern d'expansion à implémenter")

def essayer_patterns_expansion(grid):
    """Essayer différents patterns d'expansion"""
    # Pattern 1: Remplissage de zones fermées (comme puzzle 3)
    solution1 = appliquer_remplissage_zones(grid)
    if valider_solution(solution1, grid):
        print("   🔄 Pattern utilisé: Remplissage zones fermées")
        return solution1

    # Pattern 2: Expansion par proximité
    solution2 = appliquer_expansion_proximite(grid)
    if valider_solution(solution2, grid):
        print("   🔄 Pattern utilisé: Expansion proximité")
        return solution2

    # Pattern 3: Remplissage diagonal
    solution3 = appliquer_remplissage_diagonal(grid)
    if valider_solution(solution3, grid):
        print("   🔄 Pattern utilisé: Remplissage diagonal")
        return solution3

    # Si aucun pattern ne marche, retourner la grille originale
    print("   ❓ Aucun pattern connu détecté")
    return grid

def appliquer_remplissage_zones(grid):
    """Appliquer le pattern de remplissage de zones (comme puzzle 3)"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    # Identifier zones bord
    zones_bord = identifier_zones_bord(grid)

    # Remplir les zones fermées avec la couleur appropriée
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and (i, j) not in zones_bord:
                if est_zone_fermee(grid, i, j):
                    # Trouver la couleur à utiliser basée sur les pixels environnants
                    couleur = determiner_couleur_remplissage(grid, i, j)
                    solution[i][j] = couleur

    return solution

def identifier_zones_bord(grid):
    """Identifier les zones connectées aux bords"""
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    bord_positions = []
    for j in range(cols):
        bord_positions.append((0, j))
        bord_positions.append((rows-1, j))
    for i in range(1, rows-1):
        bord_positions.append((i, 0))
        bord_positions.append((i, cols-1))

    zones_bord = set()

    for start_i, start_j in bord_positions:
        if grid[start_i][start_j] == 0 and (start_i, start_j) not in visited:
            zone = flood_fill(grid, start_i, start_j, visited)
            zones_bord.update(zone)

    return zones_bord

def flood_fill(grid, start_i, start_j, visited):
    """Flood fill pour identifier une zone connectée"""
    rows = len(grid)
    cols = len(grid[0])
    zone = set()
    pile = [(start_i, start_j)]

    while pile:
        i, j = pile.pop()
        if (i < 0 or i >= rows or j < 0 or j >= cols or
            (i, j) in visited or grid[i][j] != 0):
            continue

        visited.add((i, j))
        zone.add((i, j))

        pile.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])

    return zone

def est_zone_fermee(grid, i, j):
    """Vérifier si une position est dans une zone fermée"""
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    murs_autour = 0

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if (ni < 0 or ni >= rows or nj < 0 or nj >= cols or
            grid[ni][nj] != 0):
            murs_autour += 1

    return murs_autour >= 3

def determiner_couleur_remplissage(grid, i, j):
    """Déterminer quelle couleur utiliser pour le remplissage"""
    # Compter les couleurs environnantes
    couleurs_autour = {}
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if (0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and
                grid[ni][nj] != 0):
                couleur = grid[ni][nj]
                couleurs_autour[couleur] = couleurs_autour.get(couleur, 0) + 1

    # Retourner la couleur la plus fréquente
    if couleurs_autour:
        return max(couleurs_autour.keys(), key=lambda k: couleurs_autour[k])

    # Par défaut, utiliser la couleur 4 (jaune)
    return 4

def appliquer_expansion_proximite(grid):
    """Appliquer expansion par proximité"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    # Créer une grille de proximité
    proximite = [[0 for _ in range(cols)] for _ in range(rows)]

    # Calculer la proximité pour chaque pixel vide
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                # Calculer la distance au pixel coloré le plus proche
                dist_min = float('inf')
                couleur_proche = 0

                for x in range(rows):
                    for y in range(cols):
                        if grid[x][y] != 0:
                            dist = abs(i - x) + abs(j - y)
                            if dist < dist_min:
                                dist_min = dist
                                couleur_proche = grid[x][y]

                proximite[i][j] = (dist_min, couleur_proche)

    # Appliquer l'expansion pour les pixels proches
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                dist, couleur = proximite[i][j]
                if dist <= 2:  # Seuil de proximité
                    solution[i][j] = couleur

    return solution

def appliquer_remplissage_diagonal(grid):
    """Appliquer remplissage diagonal"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and est_entoure_diagonal(grid, i, j):
                couleur = determiner_couleur_remplissage(grid, i, j)
                solution[i][j] = couleur

    return solution

def est_entoure_diagonal(grid, i, j):
    """Vérifier si entouré en diagonal"""
    directions_diagonales = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    couleurs_autour = 0

    for di, dj in directions_diagonales:
        ni, nj = i + di, j + dj
        if (0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and
            grid[ni][nj] != 0):
            couleurs_autour += 1

    return couleurs_autour >= 2

def valider_solution(solution, original):
    """Valider qu'une solution est cohérente"""
    pixels_solution = sum(1 for row in solution for cell in row if cell != 0)
    pixels_original = sum(1 for row in original for cell in row if cell != 0)

    return pixels_solution >= pixels_original

def analyser_echec(solution, attendu):
    """Analyser les échecs"""
    rows = len(solution)
    cols = len(solution[0])

    erreurs = 0
    for i in range(rows):
        for j in range(cols):
            if solution[i][j] != attendu[i][j]:
                erreurs += 1

    print(f"   Nombre d'erreurs: {erreurs}")

    # Analyser les types d'erreurs
    faux_positifs = 0  # Pixels en trop
    faux_negatifs = 0  # Pixels manquants

    for i in range(rows):
        for j in range(cols):
            if solution[i][j] != 0 and attendu[i][j] == 0:
                faux_positifs += 1
            elif solution[i][j] == 0 and attendu[i][j] != 0:
                faux_negatifs += 1

    print(f"   Faux positifs: {faux_positifs}")
    print(f"   Faux négatifs: {faux_negatifs}")

if __name__ == "__main__":
    tester_solveur_puzzle_8()
