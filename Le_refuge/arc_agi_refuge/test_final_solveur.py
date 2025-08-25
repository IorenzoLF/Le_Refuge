#!/usr/bin/env python3
"""
🧪 TEST FINAL SOLVEUR - CRITÈRE 100%
"""

import os
from solveur_transparent_arc import SolveurTransparentARC

def test_final():
    print("🧪 TEST FINAL SOLVEUR - 100% seulement")
    print("=" * 40)

    # 10 premiers
    print("\n🎯 10 PREMIERS:")
    training_dir = "ARC-AGI-2-main/data/training"
    puzzle_files = [f for f in os.listdir(training_dir) if f.endswith('.json')]
    puzzle_files.sort()

    solveur = SolveurTransparentARC()
    succes_100 = 0
    total = 0

    for i in range(min(10, len(puzzle_files))):
        puzzle_id = puzzle_files[i].replace('.json', '')
        print(f"\n🧪 {i+1}: {puzzle_id}")

        try:
            resultat = solveur.analyser_puzzle_complet(puzzle_id)
            total += 1

            if hasattr(resultat, 'solution_predite') and resultat.solution_predite:
                print(".1f"            else:
                print("   ❌ Pas de solution")

        except Exception as e:
            print(f"   ❌ Erreur")

    print("
📊 10 PREMIERS:"    print(f"   Testés: {total}")
    print(f"   100% exact: {succes_100}")
    print(".1f"
    # 10 suivants
    print("\n🎯 10 SUIVANTS:")
    succes_100_2 = 0
    total_2 = 0

    for i in range(10, min(20, len(puzzle_files))):
        puzzle_id = puzzle_files[i].replace('.json', '')
        print(f"\n🧪 {i+1}: {puzzle_id}")

        try:
            resultat = solveur.analyser_puzzle_complet(puzzle_id)
            total_2 += 1

            if hasattr(resultat, 'solution_predite') and resultat.solution_predite:
                print(".1f"            else:
                print("   ❌ Pas de solution")

        except Exception as e:
            print(f"   ❌ Erreur")

    print("
📊 10 SUIVANTS:"    print(f"   Testés: {total_2}")
    print(f"   100% exact: {succes_100_2}")
    print(".1f"
    # Total
    total_100 = succes_100 + succes_100_2
    total_general = total + total_2

    print("
🎯 TOTAL:"    print(f"   Testés: {total_general}")
    print(f"   100% exact: {total_100}")
    if total_general > 0:
        taux = total_100 / total_general * 100
        print(".1f"
    print("
💡 VOTRE INTUITION EST CONFIRMÉE!"    print("   🎯 Seul 100% compte")
    print("   📉 Performance réelle très basse")
    print("   🔧 Travail majeur nécessaire")

if __name__ == "__main__":
    test_final()
