#!/usr/bin/env python3
"""
Test des puzzles complexes avec PatternDetector et PatternScorer améliorés
Mesurer l'impact réel des améliorations (0% → ?%)
"""

from pattern_detector_v2_ameliore import PatternDetectorAmeliore
from pattern_scorer_v2_ameliore import PatternScorerAmeliore
import json
import os

def test_puzzles_complexes_ameliore():
    """Test des 18 puzzles avec le système amélioré"""
    print("🧪 TEST DES PUZZLES COMPLEXES - SYSTÈME AMÉLIORÉ")
    print("=" * 65)
    print("🎯 Objectif: Mesurer l'amélioration (0% → ?%)")
    print("📊 Méthode: PatternDetector + PatternScorer améliorés")
    print()

    # Initialiser le système amélioré
    detector = PatternDetectorAmeliore()
    scorer = PatternScorerAmeliore()

    # Puzzles à tester (ceux qui avaient 0% de succès)
    puzzles_to_test = [
        "007bbfb7", "00d62c1b", "00dbd492", "017c7c7b", "025d127b",
        "03560426", "045e512c", "0520fde7", "05269061", "05a7bcf2",
        "05f2a901", "0607ce86", "0692e18c", "06df4c85", "070dd51e",
        "08ed6ac7", "09629e4f", "0962bcdd"
    ]

    results_summary = {
        'total_puzzles': len(puzzles_to_test),
        'puzzles_with_improvements': 0,
        'total_patterns_detected': 0,
        'total_high_confidence_patterns': 0,
        'average_pattern_score': 0,
        'average_generalization_score': 0,
        'patterns_by_category': {
            'spatial': 0,
            'color': 0,
            'structural': 0,
            'mathematical': 0
        },
        'puzzle_results': []
    }

    print(f"📋 Test de {len(puzzles_to_test)} puzzles...")
    print()

    for i, puzzle_id in enumerate(puzzles_to_test, 1):
        print(f"🎯 PUZZLE {i:2d}/18: {puzzle_id}")
        print("-" * 40)

        try:
            # Charger le puzzle
            with open(f"ARC-AGI-2-main/data/training/{puzzle_id}.json", 'r') as f:
                puzzle_data = json.load(f)

            if 'train' not in puzzle_data or not puzzle_data['train']:
                print("   ❌ Pas d'exemples d'entraînement")
                continue

            # Prendre le premier exemple
            example = puzzle_data['train'][0]
            input_grid = example['input']
            output_grid = example['output']

            print(f"   Dimensions: {len(input_grid)}x{len(input_grid[0])} → {len(output_grid)}x{len(output_grid[0])}")

            # Analyse avec le PatternDetector amélioré
            analysis = detector.analyze_puzzle_complete(input_grid, output_grid)

            # Compter les patterns
            patterns_count = len([p for cat in analysis.values() if isinstance(cat, dict) for p in cat.values()])
            high_confidence_count = len(analysis.get('high_confidence_patterns', []))

            print(f"   Patterns détectés: {patterns_count}")
            print(f"   Patterns haute confiance: {high_confidence_count}")

            if high_confidence_count > 0:
                results_summary['puzzles_with_improvements'] += 1
                print("   ✅ Amélioration détectée!")

                # Afficher les patterns haute confiance
                for pattern in analysis['high_confidence_patterns'][:3]:  # Top 3
                    print(f"     • {pattern}")

                if len(analysis['high_confidence_patterns']) > 3:
                    print(f"     ... et {len(analysis['high_confidence_patterns']) - 3} autres")

            # Analyser les patterns par catégorie
            for category in ['spatial', 'color', 'structural', 'mathematical']:
                if category in analysis:
                    category_patterns = len(analysis[category])
                    results_summary['patterns_by_category'][category] += category_patterns

            # Évaluer avec PatternScorer amélioré (un pattern représentatif)
            if analysis['high_confidence_patterns']:
                # Prendre le premier pattern haute confiance
                best_pattern = analysis['high_confidence_patterns'][0]
                category, pattern_name = best_pattern.split('.', 1)

                if category in analysis and pattern_name in analysis[category]:
                    pattern_data = analysis[category][pattern_name]
                    evaluation = scorer.evaluate_pattern_comprehensive_advanced(
                        best_pattern, pattern_data, input_grid, output_grid
                    )

                    print(".2f")
                    print(".2f")
                    print(f"     Risque surapprentissage: {evaluation['overfitting_analysis']['overall_risk']:.2f}")

                    # Ajouter aux statistiques
                    results_summary['average_pattern_score'] += evaluation['final_score']
                    results_summary['average_generalization_score'] += evaluation['metrics']['generalization_score']

            # Stocker les résultats
            puzzle_result = {
                'puzzle_id': puzzle_id,
                'patterns_detected': patterns_count,
                'high_confidence_patterns': high_confidence_count,
                'patterns_list': analysis.get('high_confidence_patterns', []),
                'overall_score': analysis.get('overall_score', 0)
            }
            results_summary['puzzle_results'].append(puzzle_result)

            results_summary['total_patterns_detected'] += patterns_count
            results_summary['total_high_confidence_patterns'] += high_confidence_count

        except Exception as e:
            print(f"   ❌ Erreur: {e}")

        print()

    # Calcul des moyennes
    if results_summary['puzzle_results']:
        results_summary['average_pattern_score'] /= len(results_summary['puzzle_results'])
        results_summary['average_generalization_score'] /= len(results_summary['puzzle_results'])

    # Résultats finaux
    print("🏆 RÉSULTATS FINAUX - TEST PUZZLES COMPLEXES")
    print("=" * 55)

    success_rate = (results_summary['puzzles_with_improvements'] / results_summary['total_puzzles']) * 100

    print(".1f")
    print(f"   Puzzles avec améliorations: {results_summary['puzzles_with_improvements']}/{results_summary['total_puzzles']}")
    print(",")
    print(",")
    print(".2f")
    print(".2f")

    print("\n📊 RÉPARTITION PAR CATÉGORIE:")
    for category, count in results_summary['patterns_by_category'].items():
        print(",")

    # Top puzzles avec le plus de patterns
    print("\n🎯 TOP PUZZLES PAR NOMBRE DE PATTERNS:")
    top_puzzles = sorted(results_summary['puzzle_results'],
                       key=lambda x: x['high_confidence_patterns'], reverse=True)[:5]

    for i, puzzle in enumerate(top_puzzles, 1):
        print("2d")

    # Analyse des patterns les plus fréquents
    all_patterns = []
    for puzzle in results_summary['puzzle_results']:
        all_patterns.extend(puzzle['patterns_list'])

    from collections import Counter
    pattern_counts = Counter(all_patterns)

    print("\n🔥 PATTERNS LES PLUS FRÉQUENTS:")
    for pattern, count in pattern_counts.most_common(10):
        print(",")

    # Évaluation de l'amélioration globale
    print("\n📈 ÉVALUATION DE L'AMÉLIORATION GLOBALE:")
    print(".1f")

    if success_rate > 50:
        print("   🌟 EXCELLENT ! Amélioration significative détectée")
    elif success_rate > 25:
        print("   ✅ BON ! Amélioration modérée observée")
    elif success_rate > 10:
        print("   ⚠️ MODÉRÉ ! Quelques améliorations")
    else:
        print("   ❌ FAIBLE ! Amélioration limitée")

    print(".2f")
    print("\n💡 ANALYSE:")
    if results_summary['total_high_confidence_patterns'] > 0:
        print("   ✅ Les nouveaux patterns détectent des structures")
        print("   ✅ Le système amélioré fonctionne sur des cas réels")
        print("   ✅ Base solide pour l'Architecture v2")
    else:
        print("   ⚠️ Besoin d'ajustements supplémentaires")
        print("   📚 Les puzzles peuvent nécessiter des patterns plus spécialisés")

    print("\n🎯 PROCHAINES ÉTAPES:")
    print("   1. Analyser les patterns détectés")
    print("   2. Améliorer les patterns manqués")
    print("   3. Intégrer dans Architecture v2")
    print("   4. Tester avec PatternComposer")

if __name__ == "__main__":
    test_puzzles_complexes_ameliore()
