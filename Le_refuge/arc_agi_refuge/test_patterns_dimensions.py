#!/usr/bin/env python3
"""
Test des patterns de dimensions
"""

import json
import os
from solveur_transparent_arc import SolveurTransparentARC
from patterns_dimensions import detecter_pattern_dimensions, appliquer_pattern_dimensions

def tester_detection_dimensions():
    """Test la détection des patterns de dimensions"""
    print("=== TEST DÉTECTION PATTERNS DE DIMENSIONS ===\n")

    # Créer des grilles de test
    test_cases = [
        {
            'nom': 'Réduction 4x4 → 2x2',
            'input': [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]],
            'output': [[1, 3], [9, 2]]
        },
        {
            'nom': 'Agrandissement 2x2 → 4x4',
            'input': [[1, 2], [3, 4]],
            'output': [[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4], [3, 3, 4, 4]]
        },
        {
            'nom': 'Changement asymétrique 3x4 → 2x3',
            'input': [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3]],
            'output': [[1, 2, 3], [5, 6, 7]]
        }
    ]

    for test in test_cases:
        print(f"Test: {test['nom']}")
        print(f"Input: {len(test['input'])}x{len(test['input'][0])}")
        print(f"Output: {len(test['output'])}x{len(test['output'][0])}")

        # Tester la détection
        detection = detecter_pattern_dimensions(test['input'], test['output'])
        print(f"Détection: {detection}")

        if detection['changement']:
            print(f"Type: {detection['type_changement']}")
            print(".1f")

            # Tester l'application
            resultat = appliquer_pattern_dimensions(test['input'], detection['dimensions_output'], detection['type_changement'])
            print(f"Résultat: {len(resultat)}x{len(resultat[0])}")

            # Vérifier si ça correspond à l'output attendu
            correspondance = resultat == test['output']
            print(f"Correspondance: {correspondance}")

        print("-" * 50)

def tester_integration_solveur():
    """Test l'intégration dans le solveur"""
    print("\n=== TEST INTÉGRATION DANS LE SOLVEUR ===\n")

    solveur = SolveurTransparentARC()

    # Tester quelques puzzles de dimensions
    puzzles_test = [
        'feca6190',  # 1x5 → 15x15 (agrandissement)
        '7fe24cdd',  # 3x3 → 6x6 (agrandissement)
    ]

    for puzzle_id in puzzles_test:
        try:
            print(f"\n--- Test Puzzle {puzzle_id} ---")
            resultat = solveur.analyser_puzzle_complet(puzzle_id)
            print(f"Pattern trouvé: {resultat.pattern_type}")
            print(".1%")

        except Exception as e:
            print(f"Erreur avec {puzzle_id}: {e}")

def tester_generateur_variantes():
    """Test le générateur de variantes"""
    print("\n=== TEST GÉNÉRATEUR DE VARIANTES ===\n")

    grille_test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    dimensions_cible = (6, 6)

    print(f"Grille source: {len(grille_test)}x{len(grille_test[0])}")
    print(f"Dimensions cible: {dimensions_cible}")

    from patterns_dimensions import generer_variantes_dimensions

    variantes = generer_variantes_dimensions(grille_test, dimensions_cible)

    print(f"\nVariantes générées: {len(variantes)}")

    for i, variante in enumerate(variantes):
        print(f"\nVariante {i+1}: {variante['type']}")
        print(".1f")
        print(f"Dimensions: {len(variante['grille'])}x{len(variante['grille'][0])}")

if __name__ == "__main__":
    tester_detection_dimensions()
    tester_generateur_variantes()
    tester_integration_solveur()
