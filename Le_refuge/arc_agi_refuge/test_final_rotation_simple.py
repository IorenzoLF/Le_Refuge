#!/usr/bin/env python3
"""
TEST FINAL - ROTATION 45° CORRIGEE
"""

from solveur_transparent_arc import SolveurTransparentARC

def test_final_rotation():
    solveur = SolveurTransparentARC()
    puzzle_id = "05269061"

    print("TEST FINAL - ROTATION 45 CORRIGEE")
    print("=" * 35)
    print(f"Puzzle: {puzzle_id}")

    try:
        resultat = solveur.analyser_puzzle_complet(puzzle_id)
        print(f"Pattern: {resultat.pattern_type}")
        print(".1f")

        if hasattr(resultat, 'similarite'):
            print(".1f")

            if resultat.similarite > 80:
                print("SUCCES - Pattern parfaitement adapte!")
            elif resultat.similarite > 50:
                print("AMELIORATION SIGNIFICATIVE")
            else:
                print("AJUSTEMENTS NECESSAIRES")

    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    test_final_rotation()
