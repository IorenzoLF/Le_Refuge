#!/usr/bin/env python3
"""
TEST DE LA VRAIE ROTATION 45° GÉOMÉTRIQUE
"""

import math
from pattern_rotation_45 import appliquer_pattern_rotation_45

def test_vraie_rotation_45():
    """Test de la vraie rotation géométrique de 45°"""

    print("🔄 TEST VRAIE ROTATION 45° GÉOMÉTRIQUE")
    print("=" * 50)

    # Exemple de l'utilisateur
    input_grid = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]
    ]

    print("📥 INPUT 3x3:")
    for i, row in enumerate(input_grid):
        print(f"  {i}: {row}")

    # Output attendu selon l'utilisateur
    expected_output = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 2, 0],
        [0, 0, 0],
        [0, 3, 0]
    ]

    print("\n🎯 OUTPUT ATTENDU 5x3:")
    for i, row in enumerate(expected_output):
        print(f"  {i}: {row}")

    # Appliquer notre rotation
    result = appliquer_pattern_rotation_45(input_grid)

    print(f"\n🤖 NOTRE ROTATION {len(result)}x{len(result[0])}:")
    for i, row in enumerate(result):
        print(f"  {i}: {row}")

    # Calculer la similarité
    def calculer_similarite(g1, g2):
        h1, w1 = len(g1), len(g1[0])
        h2, w2 = len(g2), len(g2[0])

        # Pour comparer, prendre la partie commune
        h_min, w_min = min(h1, h2), min(w1, w2)

        correct = 0
        total = 0

        for i in range(h_min):
            for j in range(w_min):
                if g1[i][j] == g2[i][j]:
                    correct += 1
                total += 1

        return correct / total * 100 if total > 0 else 0

    similarite = calculer_similarite(result, expected_output)
    print(".1f")

    if similarite < 100:
        print("\n❌ ROTATION INCORRECTE")
        print("💡 Besoin d'ajustements pour matcher exactement le pattern")
        print("   Le problème: La rotation mathématique pure ne donne pas")
        print("   le résultat attendu. Il faut un mapping spécifique.")

        # Analyser les positions
        print("\n🔍 ANALYSE DES POSITIONS:")
        print("Input non-zero positions:")
        for i in range(len(input_grid)):
            for j in range(len(input_grid[0])):
                if input_grid[i][j] != 0:
                    print(f"  {input_grid[i][j]} à ({i},{j})")

        print("Expected output non-zero positions:")
        for i in range(len(expected_output)):
            for j in range(len(expected_output[0])):
                if expected_output[i][j] != 0:
                    print(f"  {expected_output[i][j]} à ({i},{j})")

        print("\n💡 MAPPING NÉCESSAIRE:")
        print("  1 à (0,0) → doit aller à (0,1)")
        print("  2 à (1,1) → doit aller à (2,1)")
        print("  3 à (2,2) → doit aller à (4,1)")
        print("  → Ce n'est pas une rotation pure, mais un pattern spécifique!")

    else:
        print("\n✅ ROTATION PARFAITE - 100% DE SIMILARITÉ!")

if __name__ == "__main__":
    test_vraie_rotation_45()
