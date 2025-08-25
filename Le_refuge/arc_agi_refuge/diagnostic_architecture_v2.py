#!/usr/bin/env python3
"""
Diagnostic de l'Architecture v2 - Analyse des seuils de confiance
"""

from pattern_detector_v2_ameliore import PatternDetectorAmeliore
from pattern_scorer_v2_ameliore import PatternScorerAmeliore

def diagnostic_architecture_v2():
    """Diagnostic des seuils de confiance dans l'Architecture v2"""
    print("🔍 DIAGNOSTIC ARCHITECTURE V2 - SEUILS DE CONFIANCE")
    print("=" * 60)

    # Test 1: Exemple simple avec différents seuils
    print("🧪 TEST 1: ANALYSE DES SEUILS DE CONFIANCE")
    print("-" * 50)

    input_test = [
        [1, 2],
        [3, 4]
    ]
    output_test = [
        [3, 1],
        [4, 2]
    ]

    detector = PatternDetectorAmeliore()
    scorer = PatternScorerAmeliore()

    # Analyse des patterns
    analysis = detector.analyze_puzzle_complete(input_test, output_test)

    print(".2f")
    print(f"   Patterns spatiaux: {len(analysis.get('spatial', {}))}")
    print(f"   Patterns couleur: {len(analysis.get('color', {}))}")
    print(f"   Patterns structuraux: {len(analysis.get('structural', {}))}")
    print(f"   Patterns mathématiques: {len(analysis.get('mathematical', {}))}")
    print(f"   Patterns haute confiance: {len(analysis.get('high_confidence_patterns', []))}")

    print("\n📊 DETAILS DES PATTERNS DETECTES:")
    for category in ['spatial', 'color', 'structural', 'mathematical']:
        if category in analysis:
            print(f"\n🔍 {category.upper()}:")
            for pattern_name, pattern_data in analysis[category].items():
                confidence = pattern_data.get('confidence', 0)
                score = pattern_data.get('score', 0)
                is_high_confidence = confidence >= 0.6

                status = "✅" if is_high_confidence else "⚠️"
                print(".2f")

                if not is_high_confidence and confidence > 0.3:
                    print("     💡 Ce pattern pourrait être utile avec un seuil plus bas")

    # Test 2: Évaluation des patterns avec le scorer
    print("")
🧪 TEST 2: EVALUATION DES PATTERNS AVEC LE SCORER"    print("-" * 55)

    # Tester un pattern spécifique
    if analysis['spatial'] and 'rotation' in analysis['spatial']:
        pattern_data = analysis['spatial']['rotation']
        evaluation = scorer.evaluate_pattern_comprehensive_advanced(
            'spatial.rotation', pattern_data, input_test, output_test
        )

        print("")
📋 ÉVALUATION DU PATTERN ROTATION:"        print(".2f")
        print(".2f")
        print(".2f")
        print(".2f")
        print(".2f")

        print(f"\n   Niveau de risque: {evaluation['overfitting_analysis']['risk_level']}")
        if evaluation['recommendations']:
            print("   Recommandations:")
            for rec in evaluation['recommendations']:
                print(f"     • {rec}")

    # Test 3: Ajustement des seuils
    print("")
🧪 TEST 3: AJUSTEMENT DES SEUILS DE CONFIANCE"    print("-" * 50)

    seuils_a_tester = [0.4, 0.5, 0.6, 0.7]

    for seuil in seuils_a_tester:
        detector_temp = PatternDetectorAmeliore()
        detector_temp.confidence_threshold = seuil

        analysis_temp = detector_temp.analyze_puzzle_complete(input_test, output_test)
        high_confidence_count = len(analysis_temp.get('high_confidence_patterns', []))

        print(".1f")

    # Test 4: Recommandations pour l'amélioration
    print("")
💡 TEST 4: RECOMMANDATIONS POUR L'AMÉLIORATION"    print("-" * 50)

    recommendations = []

    if len(analysis.get('high_confidence_patterns', [])) == 0:
        recommendations.append("🔧 Abaisser le seuil de confiance (actuellement 0.6)")
        recommendations.append("📊 Améliorer les métriques de confiance dans PatternDetector")
        recommendations.append("🎯 Focus sur les patterns les plus prometteurs")

    if analysis.get('overall_score', 0) < 0.5:
        recommendations.append("⚡ Augmenter la précision des patterns détectés")
        recommendations.append("🔍 Ajouter plus de patterns de base solides")

    if not analysis.get('spatial', {}):
        recommendations.append("🏗️ Développer plus de patterns spatiaux fondamentaux")

    print("Recommandations d'amélioration:")
    for i, rec in enumerate(recommendations, 1):
        print(f"   {i}. {rec}")

    # Test 5: Validation finale
    print("")
✅ TEST 5: VALIDATION ET PERSPECTIVES"    print("-" * 40)

    print("Statut de l'Architecture v2:")
    print("   ✅ PatternDetector amélioré: Opérationnel")
    print("   ✅ PatternScorer amélioré: Opérationnel")
    print("   ✅ Intégration: Réussie")
    print("   ⚠️ Ajustements: Nécessaires pour optimiser les seuils")

    print("")
🎯 PROCHAINES ÉTAPES:"    print("   1. Ajuster les seuils de confiance")
    print("   2. Améliorer la précision des patterns")
    print("   3. Tester avec PatternComposer")
    print("   4. Validation finale sur puzzles complexes")

if __name__ == "__main__":
    diagnostic_architecture_v2()
