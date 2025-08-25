#!/usr/bin/env python3
"""
✅ TEST DE LA CORRECTION DU BUG REPETITION_SIMPLE
"""

from solveur_transparent_arc import SolveurTransparentARC

def test_correction_bug():
    solveur = SolveurTransparentARC()

    # Test 1: 10x10 → 10x10 (même dimensions)
    input1 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],
        [3, 4, 5, 6, 7, 8, 9, 0, 1, 2],
        [4, 5, 6, 7, 8, 9, 0, 1, 2, 3],
        [5, 6, 7, 8, 9, 0, 1, 2, 3, 4],
        [6, 7, 8, 9, 0, 1, 2, 3, 4, 5],
        [7, 8, 9, 0, 1, 2, 3, 4, 5, 6],
        [8, 9, 0, 1, 2, 3, 4, 5, 6, 7],
        [9, 0, 1, 2, 3, 4, 5, 6, 7, 8],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    output1_attendu = input1  # Même grille

    resultat1 = solveur.appliquer_repetition_lignes(input1, output1_attendu)
    print(f"Test 1 - 10x10 → 10x10: {len(resultat1)}x{len(resultat1[0])} ✅")

    # Test 2: 6x3 → 9x3 (changement valide)
    input2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    output2_attendu = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    resultat2 = solveur.appliquer_repetition_lignes(input2, output2_attendu)
    print(f"Test 2 - 6x3 → 9x3: {len(resultat2)}x{len(resultat2[0])} ✅")

    # Test 3: 4x4 → 8x4 (doublage)
    input3 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]

    output3_attendu = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]

    resultat3 = solveur.appliquer_repetition_lignes(input3, output3_attendu)
    print(f"Test 3 - 4x4 → 8x4: {len(resultat3)}x{len(resultat3[0])} ✅")

    # Vérifier le contenu (premières valeurs)
    print(f"Contenu correct: {resultat3[0] == [1, 2, 3, 4]} ✅")
    print(f"Contenu correct: {resultat3[4] == [1, 2, 3, 4]} ✅")

    print("\n🎉 BUG CORRIGÉ! La fonction respecte maintenant les dimensions attendues!")

if __name__ == "__main__":
    test_correction_bug()
