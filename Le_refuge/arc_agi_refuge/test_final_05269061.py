#!/usr/bin/env python3
"""
🎯 TEST FINAL PATTERN DIAGONAL - 05269061
"""

import json
from typing import List

def calculer_similarite(grille1: List[List[int]], grille2: List[List[int]]) -> float:
    """Calcule la similarité entre deux grilles"""
    if not grille1 or not grille2:
        return 0.0

    h1, w1 = len(grille1), len(grille1[0])
    h2, w2 = len(grille2), len(grille2[0])

    if h1 != h2 or w1 != w2:
        return 0.0

    total = h1 * w1
    correct = sum(1 for i in range(h1) for j in range(w1)
                 if grille1[i][j] == grille2[i][j])

    return correct / total * 100

def appliquer_pattern_diagonal(input_grid: List[List[int]]) -> List[List[int]]:
    """Applique le pattern diagonal observé"""

    h, w = len(input_grid), len(input_grid[0])

    # Extraire les couleurs dans l'ordre diagonal
    couleurs = []
    for i in range(h):
        for j in range(w):
            if input_grid[i][j] != 0:
                couleurs.append(input_grid[i][j])

    if not couleurs:
        couleurs = [1, 2, 4]  # Séquence par défaut

    # Créer la grille de sortie remplie diagonalement
    output = [[0 for _ in range(w)] for _ in range(h)]

    # Remplir toute la grille avec le pattern diagonal
    couleurs_idx = 0
    for i in range(h):
        for j in range(w):
            output[i][j] = couleurs[couleurs_idx % len(couleurs)]
            couleurs_idx += 1

    return output

def main():
    print("🎯 TEST FINAL PATTERN DIAGONAL - 05269061")
    print("=" * 50)

    # Charger le puzzle
    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return

    test_input = puzzle_data['test'][0]['input']
    print(f"🧩 Input: {len(test_input)}x{len(test_input[0])}")

    # Appliquer le pattern diagonal
    resultat = appliquer_pattern_diagonal(test_input)
    print(f"📤 Output: {len(resultat)}x{len(resultat[0])}")

    # Afficher aperçu
    print("\n🔍 RÉSULTAT:")
    for i, row in enumerate(resultat[:3]):
        print(f"   {i}: {row}")
    if len(resultat) > 3:
        print("   ...")

    # Validation avec les exemples
    print("\n✅ VALIDATION:")
    total_sim = 0
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_ex = exemple['input']
        output_ex = exemple['output']

        resultat_ex = appliquer_pattern_diagonal(input_ex)
        sim = calculer_similarite(resultat_ex, output_ex)
        total_sim += sim
        print(".1f")

    moyenne = total_sim / len(puzzle_data['train'])
    print(".1f")

    print("
📈 COMPARAISON:"    print("   ❌ Ancien: 24.49%")
    print(".1f")

    if moyenne > 24.49:
        print("   🎉 AMÉLIORATION RÉUSSIE!")
    else:
        print("   ⚠️  Pas d'amélioration")

if __name__ == "__main__":
    main()
