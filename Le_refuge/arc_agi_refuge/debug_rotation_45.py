#!/usr/bin/env python3
"""
🔍 DEBUG ET CORRECTION DE LA ROTATION 45°
Basé sur l'exemple concret de l'utilisateur
"""

from pattern_rotation_45 import appliquer_pattern_rotation_45
from solveur_transparent_arc import SolveurTransparentARC

def debug_rotation_45():
    """Debug de la rotation 45° avec l'exemple de l'utilisateur"""

    print("🔍 DEBUG ROTATION 45°")
    print("=" * 30)

    # Exemple de l'utilisateur
    input_grid = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]
    ]

    print("📥 INPUT (3x3):")
    for i, row in enumerate(input_grid):
        print(f"  {i}: {row}")

    print("\n🎯 OUTPUT ATTENDU (5x3):")
    output_attendu = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 2, 0],
        [0, 0, 0],
        [0, 3, 0]
    ]
    for i, row in enumerate(output_attendu):
        print(f"  {i}: {row}")

    print("\n🤖 MA ROTATION ACTUELLE (3x3):")
    resultat_actuel = appliquer_pattern_rotation_45(input_grid)
    for i, row in enumerate(resultat_actuel):
        print(f"  {i}: {row}")

    print("\n📊 COMPARAISON:")
    print(f"   Dimensions - Attendu: 5x3, Actuel: {len(resultat_actuel)}x{len(resultat_actuel[0])}")

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

    similarite = calculer_similarite(resultat_actuel, output_attendu)
    print(".1f")

    print("\n💡 ANALYSE DU PROBLÈME:")
    print("   1. La rotation mathématique ne donne pas le résultat attendu")
    print("   2. L'utilisateur veut un 'losange' spécifique, pas une rotation pure")
    print("   3. Il faut ajuster l'algorithme pour matcher exactement le pattern")

    print("\n🔧 NOUVEL ALGORITHME PROPOSÉ:")
    print("   - Au lieu d'une rotation mathématique pure")
    print("   - Créer un mapping spécifique basé sur les positions")
    print("   - 1 (coin supérieur gauche) → position (0,1) dans output")
    print("   - 2 (centre) → position (2,1) dans output")
    print("   - 3 (coin inférieur droit) → position (4,1) dans output")

if __name__ == "__main__":
    debug_rotation_45()
