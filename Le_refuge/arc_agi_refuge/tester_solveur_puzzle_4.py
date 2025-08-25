#!/usr/bin/env python3
"""
🧪 TESTER SOLVEUR SUR PUZZLE 4: 00dbd492
Vérifier si notre solveur peut le résoudre automatiquement
"""

import json

def tester_solveur_puzzle_4():
    """Tester notre solveur sur le puzzle 4"""
    print("🧪 TEST SOLVEUR SUR PUZZLE 4: 00dbd492")
    print("=" * 50)

    with open("data/training/00dbd492.json", 'r') as f:
        puzzle_data = json.load(f)

    # Tester sur les exemples d'entraînement
    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Essayer différents patterns
        solution = essayer_patterns(input_grid)

        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1
        else:
            print("   📊 Échec - Analysons pourquoi:")
            analyser_echec(solution, output_attendu)

    print(f"\n🎉 SCORE: {success_count}/{len(puzzle_data['train'])}")

    if success_count == len(puzzle_data['train']):
        print("✅ PARFAIT! Le solveur connaît ce pattern!")
        print("💾 Résolution du test...")

        test_input = puzzle_data['test'][0]['input']
        solution_test = essayer_patterns(test_input)

        submission = {"00dbd492": solution_test}
        with open("submission_00dbd492_solveur.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/4 - Pattern pas encore implémenté")

def essayer_patterns(grid):
    """Essayer différents patterns connus"""
    # Pattern 1: Remplissage de zones fermées (comme puzzle 3)
    solution1 = appliquer_remplissage_zones(grid)
    if valider_solution(solution1, grid):
        print("   🔄 Pattern utilisé: Remplissage zones fermées")
        return solution1

    # Pattern 2: Symétrie
    solution2 = appliquer_symetrie(grid)
    if valider_solution(solution2, grid):
        print("   🔄 Pattern utilisé: Symétrie")
        return solution2

    # Pattern 3: Répétition de motif
    solution3 = appliquer_repetition(grid)
    if valider_solution(solution3, grid):
        print("   🔄 Pattern utilisé: Répétition")
        return solution3

    # Pattern 4: Transformation couleur
    solution4 = appliquer_transformation_couleur(grid)
    if valider_solution(solution4, grid):
        print("   🔄 Pattern utilisé: Transformation couleur")
        return solution4

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

    # Remplir les zones fermées avec couleur 3 (bleu)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and (i, j) not in zones_bord:
                if est_zone_fermee(grid, i, j):
                    solution[i][j] = 3  # Bleu

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
            grid[ni][nj] == 2):  # Vert = mur
            murs_autour += 1

    return murs_autour >= 3

def appliquer_symetrie(grid):
    """Appliquer un pattern de symétrie"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    # Symétrie horizontale
    for i in range(rows):
        for j in range(cols // 2):
            if grid[i][j] == 0 and grid[i][cols-1-j] == 0:
                # Les deux positions sont vides, on peut appliquer la symétrie
                pass

    return solution

def appliquer_repetition(grid):
    """Appliquer un pattern de répétition"""
    solution = [row[:] for row in grid]
    # Pattern de répétition à implémenter selon les besoins
    return solution

def appliquer_transformation_couleur(grid):
    """Appliquer une transformation de couleur"""
    solution = [row[:] for row in grid]

    # Transformer certaines couleurs
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:  # Vert
                solution[i][j] = 3  # Devient bleu

    return solution

def valider_solution(solution, original):
    """Valider qu'une solution est cohérente"""
    # Compter les pixels verts dans la solution
    verts_solution = sum(1 for row in solution for cell in row if cell == 2)
    verts_original = sum(1 for row in original for cell in row if cell == 2)

    # Les pixels verts ne devraient pas disparaître
    return verts_solution >= verts_original

def analyser_echec(solution, attendu):
    """Analyser pourquoi une solution a échoué"""
    rows = len(solution)
    cols = len(solution[0])

    erreurs = 0
    for i in range(rows):
        for j in range(cols):
            if solution[i][j] != attendu[i][j]:
                erreurs += 1

    print(f"   Nombre d'erreurs: {erreurs}")

    # Analyser les types d'erreurs
    faux_positifs = 0  # Pixels ajoutés en trop
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
    tester_solveur_puzzle_4()
