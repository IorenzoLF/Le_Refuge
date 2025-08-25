#!/usr/bin/env python3
"""
Test d'intégration PatternDetector + PatternScorer
"""

from pattern_detector_v2 import PatternDetector
from pattern_scorer_v2 import PatternScorer

def test_integration():
    print("Test integration PatternDetector + PatternScorer")
    print("=" * 50)

    # Exemple simple: expansion par repetition
    input_grid = [
        [1, 2],
        [3, 4]
    ]
    output_grid = [
        [1, 1, 2, 2],
        [1, 1, 2, 2],
        [3, 3, 4, 4],
        [3, 3, 4, 4]
    ]

    # Detection des patterns
    print("1. DETECTION DES PATTERNS:")
    detector = PatternDetector()
    analysis = detector.analyze_puzzle(input_grid, output_grid)

    print(".2f")

    for category in ['spatial', 'color', 'structural']:
        if category in analysis:
            for pattern_name, pattern_data in analysis[category].items():
                if pattern_data['confidence'] > 0.5:
                    print(".2f")

    print("\n2. EVALUATION AVEC PATTERN SCORER:")
    scorer = PatternScorer()
    evaluation = scorer.evaluate_pattern_suite(analysis)

    print("Qualite globale:", evaluation['overall_quality'])
    print("Diversite patterns:", evaluation['pattern_diversity'])
    print("Risque surapprentissage:", evaluation['overfitting_risk'])

    if evaluation['recommended_patterns']:
        print("Patterns recommandes:")
        for pattern in evaluation['recommended_patterns']:
            print(f"  - {pattern}")

    print("\n3. RAPPORT ANTI-SURAPPRENTISSAGE:")
    print(scorer.generate_anti_overfitting_report(analysis))

if __name__ == "__main__":
    test_integration()
