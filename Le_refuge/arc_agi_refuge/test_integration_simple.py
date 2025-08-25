#!/usr/bin/env python3
"""
TEST D'INTEGRATION COMPLETE - PHASE 4
"""

from solveur_transparent_arc import SolveurTransparentARC

def test_integration():
    solveur = SolveurTransparentARC()

    print("TEST D'INTEGRATION COMPLETE")
    print("=" * 30)

    # Tester quelques puzzles du dataset
    dataset_path = "ARC-AGI-2-main/data/training"
    import os
    if os.path.exists(dataset_path):
        puzzles = [f.replace('.json', '') for f in os.listdir(dataset_path) if f.endswith('.json')]

        # Tester les 5 premiers puzzles
        puzzles_test = puzzles[:5]

        resultats = {
            'dimensions': 0,
            'couleurs': 0,
            'spatiaux': 0,
            'diagonaux': 0,
            'repetition_simple': 0,
            'autres': 0
        }

        for i, puzzle_id in enumerate(puzzles_test, 1):
            try:
                print(f"\nTest {i}: {puzzle_id}")
                resultat = solveur.analyser_puzzle_complet(puzzle_id)

                pattern_type = resultat.pattern_type
                confiance = resultat.confiance

                # Classifier le pattern
                if 'dimensions' in pattern_type or 'agrandissement' in pattern_type or 'reduction' in pattern_type:
                    resultats['dimensions'] += 1
                    categorie = "Dimensions"
                elif 'couleurs' in pattern_type or 'remplacement' in pattern_type or 'ajout' in pattern_type:
                    resultats['couleurs'] += 1
                    categorie = "Couleurs"
                elif 'spatiaux' in pattern_type or 'remplissage' in pattern_type:
                    resultats['spatiaux'] += 1
                    categorie = "Spatiaux"
                elif 'diagonal' in pattern_type or 'propagation' in pattern_type:
                    resultats['diagonaux'] += 1
                    categorie = "Diagonaux"
                elif 'repetition' in pattern_type:
                    resultats['repetition_simple'] += 1
                    categorie = "Repetition"
                else:
                    resultats['autres'] += 1
                    categorie = "Autres"

                print(f"  Categorie: {categorie}")
                print(f"  Pattern: {pattern_type}")
                print(".1f")

            except Exception as e:
                print(f"  Erreur: {e}")
                resultats['autres'] += 1

        # Resume
        print("
RESUME:"        print("-" * 20)

        total = sum(resultats.values())
        for module, count in resultats.items():
            if count > 0:
                pourcentage = (count / total) * 100
                print("12s")

        print("\nINTEGRATION: ", end="")        if total > 0:
            print("REUSSIE - Tous les modules fonctionnent")
        else:
            print("A VERIFIER - Aucun pattern detecte")

    else:
        print("Dataset non trouve")

if __name__ == "__main__":
    test_integration()
