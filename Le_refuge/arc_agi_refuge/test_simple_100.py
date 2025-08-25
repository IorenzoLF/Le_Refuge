#!/usr/bin/env python3
"""
🧪 TEST SIMPLE 100%
"""

import os
from solveur_transparent_arc import SolveurTransparentARC

def test_simple():
    print("🧪 TEST SIMPLE 100%")

    training_dir = "ARC-AGI-2-main/data/training"
    puzzle_files = [f for f in os.listdir(training_dir) if f.endswith('.json')]
    puzzle_files.sort()

    solveur = SolveurTransparentARC()
    succes_100 = 0
    total = 0

    print("\n🎯 10 PREMIERS:")
    for i in range(min(10, len(puzzle_files))):
        puzzle_id = puzzle_files[i].replace('.json', '')
        print(f"\n🧪 {i+1}: {puzzle_id}")

        try:
            resultat = solveur.analyser_puzzle_complet(puzzle_id)
            total += 1

            if hasattr(resultat, 'solution_predite') and resultat.solution_predite:
                print(".1f")
            else:
                print("   Pas de solution")

        except Exception as e:
            print(f"   Erreur")

    print("
📊 10 PREMIERS:"    print(f"   Testes: {total}")
    print(f"   100% exact: {succes_100}")
    if total > 0:
        taux = succes_100 / total * 100
        print(".1f"
    print("
💡 VOTRE INTUITION EST JUSTE!"    print("   Performance reelle tres basse")
    print("   Travail majeur necessaire")

if __name__ == "__main__":
    test_simple()
