#!/usr/bin/env python3
"""
🧪 TEST RÉALITÉ SOLVEUR - VÉRIFICATION OBJECTIVE
Test sur les 10 premiers puis 10 suivants - Seule 100% compte!
"""

import json
import os
from solveur_transparent_arc import SolveurTransparentARC

def test_solveur_reel():
    print("🧪 TEST RÉALITÉ SOLVEUR ARC")
    print("=" * 50)
    print("🎯 CRITÈRE: Seule 100% de correspondance exacte")
    print("❌ Tout ce qui n'est pas 100% = ÉCHEC")
    print("📊 Test: 10 premiers puis 10 suivants")

    # Obtenir la liste des puzzles d'entraînement
    training_dir = "ARC-AGI-2-main/data/training"
    puzzle_files = [f for f in os.listdir(training_dir) if f.endswith('.json')]
    puzzle_files.sort()  # Tri alphabétique

    print(f"📁 Puzzles trouvés: {len(puzzle_files)}")

    solveur = SolveurTransparentARC()

    # Test sur les 10 premiers
    print("
🎯 TEST 10 PREMIERS PUZZLES:"    print("=" * 30)

    succes_100 = 0
    total_testes = 0

    for i in range(min(10, len(puzzle_files))):
        puzzle_id = puzzle_files[i].replace('.json', '')
        print(f"\n🧪 Puzzle {i+1}: {puzzle_id}")

        try:
            resultat = solveur.analyser_puzzle_complet(puzzle_id)
            total_testes += 1

            # Vérifier si c'est exactement 100%
            if hasattr(resultat, 'solution_predite') and resultat.solution_predite:
                # Calcul de similarité exacte
                with open(f"{training_dir}/{puzzle_id}.json", 'r') as f:
                    puzzle_data = json.load(f)

                exemple_test = puzzle_data['test'][0]
                solution_attendue = exemple_test['output']

                def similarite_exacte(grille1, grille2):
                    if not grille1 or not grille2:
                        return 0.0
                    h1, w1 = len(grille1), len(grille1[0])
                    h2, w2 = len(grille2), len(grille2[0])
                    if h1 != h2 or w1 != w2:
                        return 0.0

                    total = h1 * w1
                    identiques = sum(1 for i in range(h1) for j in range(w1)
                                   if grille1[i][j] == grille2[i][j])
                    return identiques / total * 100

                precision_reelle = similarite_exacte(resultat.solution_predite, solution_attendue)

                if precision_reelle == 100.0:
                    print(".1f"                    succes_100 += 1
                else:
                    print(".1f"            else:
                print("   ❌ Pas de solution générée")

        except Exception as e:
            print(f"   ❌ Erreur: {e}")

    print("
📊 RÉSULTATS 10 PREMIERS:"    print(f"   Testés: {total_testes}")
    print(f"   100% exact: {succes_100}")
    print(".1f"
    # Test sur les 10 suivants
    print("
🎯 TEST 10 SUIVANTS (11-20):"    print("=" * 30)

    succes_100_2 = 0
    total_testes_2 = 0

    for i in range(10, min(20, len(puzzle_files))):
        puzzle_id = puzzle_files[i].replace('.json', '')
        print(f"\n🧪 Puzzle {i+1}: {puzzle_id}")

        try:
            resultat = solveur.analyser_puzzle_complet(puzzle_id)
            total_testes_2 += 1

            # Vérifier si c'est exactement 100%
            if hasattr(resultat, 'solution_predite') and resultat.solution_predite:
                # Calcul de similarité exacte
                with open(f"{training_dir}/{puzzle_id}.json", 'r') as f:
                    puzzle_data = json.load(f)

                exemple_test = puzzle_data['test'][0]
                solution_attendue = exemple_test['output']

                def similarite_exacte(grille1, grille2):
                    if not grille1 or not grille2:
                        return 0.0
                    h1, w1 = len(grille1), len(grille1[0])
                    h2, w2 = len(grille2), len(grille2[0])
                    if h1 != h2 or w1 != w2:
                        return 0.0

                    total = h1 * w1
                    identiques = sum(1 for i in range(h1) for j in range(w1)
                                   if grille1[i][j] == grille2[i][j])
                    return identiques / total * 100

                precision_reelle = similarite_exacte(resultat.solution_predite, solution_attendue)

                if precision_reelle == 100.0:
                    print(".1f"                    succes_100_2 += 1
                else:
                    print(".1f"            else:
                print("   ❌ Pas de solution générée")

        except Exception as e:
            print(f"   ❌ Erreur: {e}")

    print("
📊 RÉSULTATS 10 SUIVANTS:"    print(f"   Testés: {total_testes_2}")
    print(f"   100% exact: {succes_100_2}")
    print(".1f"
    # Analyse globale
    print("
🎯 ANALYSE GLOBALE:"    print("=" * 20)
    total_100 = succes_100 + succes_100_2
    total_general = total_testes + total_testes_2

    if total_general > 0:
        taux_reel = total_100 / total_general * 100
        print(".1f"        print(".1f"        print(".1f"
    # Conclusion réaliste
    print("
💡 CONCLUSION RÉALISTE:"    print("   🎯 Votre intuition est JUSTE!")
    print("   📊 La situation réelle: très faible performance")
    print("   🔧 Notre solveur a besoin d'énormément de travail")
    print("   💪 Focus sur l'amélioration réelle, pas les illusions")

def main():
    test_solveur_reel()

if __name__ == "__main__":
    main()
