#!/usr/bin/env python3
"""
Test du PatternComposer v2
"""

from pattern_detector_v2 import PatternDetector
from pattern_composer_v2 import PatternComposer

def test_pattern_composer():
    print("Test PatternComposer v2")
    print("=" * 40)

    # Exemple avec plusieurs patterns
    input_grid = [
        [1, 2, 1],  # Symétrique horizontalement
        [3, 0, 3],
        [1, 2, 1]
    ]

    # Output avec expansion et mapping de couleur
    output_grid = [
        [1, 1, 2, 2, 1, 1],
        [1, 1, 2, 2, 1, 1],
        [3, 3, 0, 0, 3, 3],
        [3, 3, 0, 0, 3, 3],
        [1, 1, 2, 2, 1, 1],
        [1, 1, 2, 2, 1, 1]
    ]

    # Détection des patterns
    print("1. DETECTION DES PATTERNS:")
    detector = PatternDetector()
    analysis = detector.analyze_puzzle(input_grid, output_grid)

    print(".2f")

    # Afficher les patterns haute confiance
    for category in ['spatial', 'color', 'structural']:
        if category in analysis:
            for pattern_name, pattern_data in analysis[category].items():
                if pattern_data['confidence'] > 0.5:
                    print(".2f")

    print("\n2. COMPOSITION DES PATTERNS:")

    # Test des différentes stratégies de composition
    composer = PatternComposer()
    strategies = ['hierarchical', 'sequential', 'parallel']

    for strategy in strategies:
        print(f"\n   Strategie {strategy.upper()}:")
        composition = composer.compose_patterns(analysis, strategy)

        if composition and 'composition' in composition:
            comp_info = composition['composition']
            if comp_info:
                print(".2f")
                if 'type' in comp_info:
                    print(f"      Type: {comp_info['type']}")
                if 'primary' in comp_info:
                    print(f"      Primary patterns: {len(comp_info['primary'])}")
                if 'secondary' in comp_info:
                    print(f"      Secondary patterns: {len(comp_info['secondary'])}")
            else:
                print("      Aucune composition possible")
        else:
            print("      Composition vide")

    print("\n3. APPLICATION DE LA COMPOSITION:")

    # Appliquer la composition hiérarchique
    composition = composer.compose_patterns(analysis, 'hierarchical')
    if composition and 'composition' in composition:
        applied_grid = composer.apply_composition(composition, input_grid)

        print("   Grille d'entree:")
        for row in input_grid:
            print(f"   {row}")

        print("   Grille apres application:")
        for row in applied_grid:
            print(f"   {row}")

        # Évaluation de la qualité
        quality = composer.evaluate_composition_quality(composition, analysis)
        print(".2f")

if __name__ == "__main__":
    test_pattern_composer()
