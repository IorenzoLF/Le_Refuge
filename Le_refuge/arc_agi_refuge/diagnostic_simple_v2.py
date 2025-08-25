#!/usr/bin/env python3
"""
Diagnostic simple Architecture v2
"""

from pattern_detector_v2_ameliore import PatternDetectorAmeliore
from pattern_scorer_v2_ameliore import PatternScorerAmeliore

def diagnostic_simple():
    """Diagnostic simple des seuils de confiance"""
    print("Diagnostic Architecture v2 - Seuils de confiance")
    print("=" * 50)

    input_test = [
        [1, 2],
        [3, 4]
    ]
    output_test = [
        [3, 1],
        [4, 2]
    ]

    detector = PatternDetectorAmeliore()
    analysis = detector.analyze_puzzle_complete(input_test, output_test)

    print(".2f")
    print(f"Patterns spatiaux: {len(analysis.get('spatial', {}))}")
    print(f"Patterns couleur: {len(analysis.get('color', {}))}")
    print(f"Patterns structuraux: {len(analysis.get('structural', {}))}")
    print(f"Patterns mathematiques: {len(analysis.get('mathematical', {}))}")
    print(f"Patterns haute confiance: {len(analysis.get('high_confidence_patterns', []))}")

    print("\nDetails des patterns:")
    for category in ['spatial', 'color', 'structural', 'mathematical']:
        if category in analysis:
            print(f"\n{category.upper()}:")
            for pattern_name, pattern_data in analysis[category].items():
                confidence = pattern_data.get('confidence', 0)
                score = pattern_data.get('score', 0)
                is_high = confidence >= 0.6
                status = "OK" if is_high else "LOW"
                print(".2f")

    # Test avec seuil plus bas
    print("\nTest avec seuil 0.4:")
    detector.confidence_threshold = 0.4
    analysis_low = detector.analyze_puzzle_complete(input_test, output_test)
    print(f"Patterns haute confiance (seuil 0.4): {len(analysis_low.get('high_confidence_patterns', []))}")

    # Recommandations
    print("\nRecommandations:")
    if len(analysis.get('high_confidence_patterns', [])) == 0:
        print("1. Abaisser le seuil de confiance (actuellement 0.6)")
        print("2. Ameliorer les metriques de confiance")
        print("3. Focus sur les patterns les plus prometteurs")

if __name__ == "__main__":
    diagnostic_simple()
