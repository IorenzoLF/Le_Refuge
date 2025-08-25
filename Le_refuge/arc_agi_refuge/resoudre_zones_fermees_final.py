#!/usr/bin/env python3
"""
🎯 ZONES FERMÉES PUZZLE 3: 00d62c1b
Remplir les zones complètement fermées
"""

import json

def main():
    print("🎯 ZONES FERMÉES 00d62c1b")

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i}")

        input_grid = exemple['input']
        output_attendu = exemple['output']

        solution = remplir_zones_fermees(input_grid)
        is_correct = solution == output_attendu
        print(f"   ✅ SUCCÈS: {is_correct}")

        if is_correct:
            success_count += 1

    print(f"\n🎉 SCORE: {success_count}/5")

    if success_count == 5:
        print("✅ PARFAIT!")

        test_input = puzzle_data['test'][0]['input']
        solution_test = remplir_zones_fermees(test_input)

        submission = {"00d62c1b": solution_test}
        with open("submission_00d62c1b_zones.json", 'w') as f:
            json.dump(submission, f, indent=2)

        print("💾 Solution sauvegardée!")
    else:
        print(f"⚠️ Score: {success_count}/5")

def remplir_zones_fermees(grid):
    """Remplir les zones fermées"""
    rows = len(grid)
    cols = len(grid[0])
    solution = [row[:] for row in grid]

    # Identifier zones bord
    zones_bord = identifier_zones_bord(grid)

    # Pour chaque case vide pas connectée au bord
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and (i, j) not in zones_bord:
                if est_zone_fermee(grid, i, j):
                    solution[i][j] = 4

    return solution

def identifier_zones_bord(grid):
    """Identifier zones connectées aux bords"""
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    # Positions de bord
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
    """Flood fill"""
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
    """Vérifier si zone fermée"""
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    murs_autour = 0

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if (ni < 0 or ni >= rows or nj < 0 or nj >= cols or
            grid[ni][nj] == 3):
            murs_autour += 1

    return murs_autour >= 3

if __name__ == "__main__":
    main()
