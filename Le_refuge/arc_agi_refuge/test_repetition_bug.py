#!/usr/bin/env python3
"""
🔧 TEST POUR CORRIGER LE BUG CRITIQUE DE REPETITION_SIMPLE
Le problème: repetition_simple génère toujours dimensions * 1.5
Exemple: 10x10 → 15x10 (au lieu de rester 10x10)
"""

from typing import List
from solveur_transparent_arc import SolveurTransparentARC

def test_repetition_simple_bug():
    """Test pour démontrer et corriger le bug de repetition_simple"""

    print("🔧 TEST BUG REPETITION_SIMPLE")
    print("=" * 40)

    solveur = SolveurTransparentARC()

    # Test case 1: Grille 10x10 qui devrait rester 10x10
    input_grille = [
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

    # Output attendu: même dimensions 10x10
    output_attendu = [
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

    print("📥 INPUT: 10x10")
    print("📤 OUTPUT ATTENDU: 10x10")
    print("❌ OUTPUT ACTUEL:")

    # Tester la fonction buggée
    resultat_bug = solveur.appliquer_repetition_lignes(input_grille, output_attendu)

    print(f"   Dimensions: {len(resultat_bug)}x{len(resultat_bug[0])} (devrait être 10x10)")

    # Calculer la similarité
    def calculer_similarite(grille1, grille2):
        if len(grille1) != len(grille2) or len(grille1[0]) != len(grille2[0]):
            return 0.0

        total = len(grille1) * len(grille1[0])
        correct = 0

        for i in range(len(grille1)):
            for j in range(len(grille1[0])):
                if grille1[i][j] == grille2[i][j]:
                    correct += 1

        return correct / total * 100

    similarite = calculer_similarite(resultat_bug, output_attendu)
    print(".1f"
    print("🔍 ANALYSE DU BUG:")
    print("   → La fonction multiplie TOUJOURS par 1.5")
    print("   → Elle ignore les dimensions attendues")
    print("   → Résultat: 10x10 → 15x10 = 0% similarité")

    # Test case 2: Grille 6x3 qui devrait devenir 9x3
    print("\n🧪 TEST CASE 2: 6x3 → 9x3 (changement valide)")    input2 = [
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
    print(f"   Input: 6x3, Output: {len(resultat2)}x{len(resultat2[0])} (attendu: 9x3)")

    similarite2 = calculer_similarite(resultat2, output2_attendu)
    print(".1f"
    print("✅ Ce cas devrait fonctionner car 6*1.5=9")

    print("\n🎯 CONCLUSION:")
    print("   Le bug est dans la ligne 857:")
    print("   nouvelle_hauteur = int(hauteur * 1.5)")
    print("   → Cette ligne ignore les dimensions attendues!")
    print("   → Elle force toujours une multiplication par 1.5")

if __name__ == "__main__":
    test_repetition_simple_bug()
