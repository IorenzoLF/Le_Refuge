#!/usr/bin/env python3
"""
🧪 TEST OBJECTIF SOLVEUR - SEULE 100% COMPTE
"""

import json
import os
from solveur_transparent_arc import SolveurTransparentARC

def test_objectif():
    print("🧪 TEST OBJECTIF SOLVEUR")
    print("=" * 30)
    print("🎯 Critère: 100% exact seulement")
    print("❌ Tout autre = échec")

    # 10 premiers puzzles
    print("\n🎯 10 PREMIERS PUZZLES:")
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
                # Vérifier 100% exact
                with open(f"{training_dir}/{puzzle_id}.json", 'r') as f:
                    puzzle_data = json.load(f)

                solution_attendue = puzzle_data['test'][0]['output']

                def similarite(grille1, grille2):
                    if len(grille1) != len(grille2) or len(grille1[0]) != len(grille2[0]):
                        return 0.0
                    total = len(grille1) * len(grille1[0])
                    match = sum(1 for i in range(len(grille1)) for j in range(len(grille1[0])) if grille1[i][j] == grille2[i][j])
                    return match / total * 100

                precision = similarite(resultat.solution_predite, solution_attendue)

                if precision == 100.0:
                    print(".1f"                    succes_100 += 1
                else:
                    print(".1f"            else:
                print("   ❌ Pas de solution")

        except Exception as e:
            print(f"   ❌ Erreur: {str(e)[:50]}")

    print("
📊 RÉSULTATS 10 PREMIERS:"    print(f"   Testés: {total}")
    print(f"   100% exact: {succes_100}")
    print(".1f"
    # 10 suivants
    print("\n🎯 10 SUIVANTS (11-20):")
    succes_100_2 = 0
    total_2 = 0

    for i in range(10, min(20, len(puzzle_files))):
        puzzle_id = puzzle_files[i].replace('.json', '')
        print(f"\n🧪 {i+1}: {puzzle_id}")

        try:
            resultat = solveur.analyser_puzzle_complet(puzzle_id)
            total_2 += 1

            if hasattr(resultat, 'solution_predite') and resultat.solution_predite:
                with open(f"{training_dir}/{puzzle_id}.json", 'r') as f:
                    puzzle_data = json.load(f)

                solution_attendue = puzzle_data['test'][0]['output']

                def similarite(grille1, grille2):
                    if len(grille1) != len(grille2) or len(grille1[0]) != len(grille2[0]):
                        return 0.0
                    total = len(grille1) * len(grille1[0])
                    match = sum(1 for i in range(len(grille1)) for j in range(len(grille1[0])) if grille1[i][j] == grille2[i][j])
                    return match / total * 100

                precision = similarite(resultat.solution_predite, solution_attendue)

                if precision == 100.0:
                    print(".1f"                    succes_100_2 += 1
                else:
                    print(".1f"            else:
                print("   ❌ Pas de solution")

        except Exception as e:
            print(f"   ❌ Erreur: {str(e)[:50]}")

    print("
📊 RÉSULTATS 10 SUIVANTS:"    print(f"   Testés: {total_2}")
    print(f"   100% exact: {succes_100_2}")
    print(".1f"
    # Conclusion
    total_100 = succes_100 + succes_100_2
    total_general = total + total_2

    print("
🎯 ANALYSE FINALE:"    print("=" * 20)
    if total_general > 0:
        taux_reel = total_100 / total_general * 100
        print(".1f"        print(".1f"
    print("
💡 VOTRE INTUITION EST CONFIRMÉE!"    print("   📉 La performance réelle est très basse")
    print("   🎯 Seul 100% compte, vous avez raison")
    print("   🔧 Le solveur a besoin de travail majeur")

def main():
    test_objectif()

if __name__ == "__main__":
    main()
