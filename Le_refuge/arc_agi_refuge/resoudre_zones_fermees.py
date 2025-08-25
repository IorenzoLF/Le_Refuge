#!/usr/bin/env python3
"""
🎯 RÉSOLUTION ZONES FERMÉES PUZZLE 3: 00d62c1b
Remplir les zones complètement fermées par des pixels bleus
"""

import json

def resoudre_zones_fermees():
    """Résoudre en remplissant les zones fermées"""
    print("🎯 RÉSOLUTION ZONES FERMÉES 00d62c1b")
    print("=" * 50)
    print("💡 APPROCHE: Identifier et remplir les zones fermées")

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 TEST EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Appliquer l'algorithme de zones fermées
        solution = remplir_zones_fermees(input_grid)

        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1
        else:
            print("   📊 Analyse des différences:")
            analyser_differences(solution, output_attendu)

    print(f"\n🎉 SCORE: {success_count}/{len(puzzle_data['train'])}")

    if success_count == len(puzzle_data['train']):
        print("✅ PARFAIT! Toutes les zones fermées identifiées!")
        print("💾 Résolution du test...")

        test_input = puzzle_data['test'][0]['input']
        solution_test = remplir_zones_fermees(test_input)

        submission = {"00d62c1b": solution_test}
        with open("submission_00d62c1b_zones_fermees.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/5 - Affiner la détection de zones fermées")

def remplir_zones_fermees(grid):
    """Remplir les zones fermées avec des pixels jaunes"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    # Étape 1: Identifier toutes les zones vides connectées aux bords
    zones_bord = identifier_zones_bord(grid)

    # Étape 2: Identifier les pixels bleus comme "murs"
    murs = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 3:  # Pixel bleu = mur
                murs.add((i, j))

    # Étape 3: Pour chaque case vide, vérifier si elle est dans une zone fermée
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and (i, j) not in zones_bord:
                # Cette case vide n'est pas connectée au bord
                # Vérifier si elle est complètement entourée par des murs
                if est_zone_fermee(grid, i, j, murs):
                    solution[i][j] = 4

    return solution

def identifier_zones_bord(grid):
    """Identifier les zones vides connectées aux bords (zones "ouvertes")"""
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    # Parcourir tous les bords
    bord_positions = []

    # Bord supérieur et inférieur
    for j in range(cols):
        bord_positions.append((0, j))      # Première ligne
        bord_positions.append((rows-1, j)) # Dernière ligne

    # Bord gauche et droite (sans les coins déjà ajoutés)
    for i in range(1, rows-1):
        bord_positions.append((i, 0))      # Première colonne
        bord_positions.append((i, cols-1)) # Dernière colonne

    zones_bord = set()

    # Pour chaque position de bord vide, faire un flood fill
    for start_i, start_j in bord_positions:
        if grid[start_i][start_j] == 0 and (start_i, start_j) not in visited:
            # Nouvelle zone vide connectée au bord
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

        # Ajouter les 4 directions
        pile.extend([
            (i-1, j), (i+1, j), (i, j-1), (i, j+1)
        ])

    return zone

def est_zone_fermee(grid, i, j, murs):
    """Vérifier si une position est dans une zone fermée"""
    rows = len(grid)
    cols = len(grid[0])

    # Pour être dans une zone fermée, toutes les directions adjacentes
    # doivent être soit des murs, soit d'autres cases de la même zone fermée
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    murs_adj = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if (ni < 0 or ni >= rows or nj < 0 or nj >= cols or
            (ni, nj) in murs):
            murs_adj += 1

    # Si entouré de tous les côtés par des murs ou bords, c'est fermé
    return murs_adj >= 3

def analyser_differences(solution, attendu):
    """Analyser les différences entre solution et attendu"""
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
        print("   💡 Indice: Ajuster la définition de 'zone fermée'")

def visualiser_zones_fermees():
    """Visualiser les zones fermées identifiées"""
    print("
🔍 VISUALISATION ZONES FERMÉES:"    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    # Prendre le premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']

    print("   🔵 = murs (pixels bleus)")
    print("   🟡 = zones fermées identifiées")
    print("   ⬜ = zones ouvertes")

    zones_bord = identifier_zones_bord(input_grid)
    murs = set()
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 3:
                murs.add((i, j))

    for i in range(len(input_grid)):
        row_str = ""
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 3:
                row_str += "🔵"  # Mur
            elif (i, j) in zones_bord:
                row_str += "⬜"  # Zone ouverte
            elif input_grid[i][j] == 0 and est_zone_fermee(input_grid, i, j, murs):
                row_str += "🟡"  # Zone fermée
            else:
                row_str += "⬜"  # Zone vide non classifiée
        print(f"      {row_str}")

if __name__ == "__main__":
    resoudre_zones_fermees()
    visualiser_zones_fermees()
