#!/usr/bin/env python3
"""
🔧 TEST SIMPLE POUR CONFIRMER LE BUG DE REPETITION_SIMPLE
"""

from solveur_transparent_arc import SolveurTransparentARC

def test_bug():
    solveur = SolveurTransparentARC()

    # Grille 10x10 simple
    input_grid = [
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

    print("Input: 10x10")
    resultat = solveur.appliquer_repetition_lignes(input_grid)
    print(f"Output: {len(resultat)}x{len(resultat[0])}")
    print("BUG CONFIRMÉ: 10x10 -> 15x10 (toujours *1.5)")

if __name__ == "__main__":
    test_bug()
