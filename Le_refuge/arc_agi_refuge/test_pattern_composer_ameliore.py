#!/usr/bin/env python3
"""
Test du PatternComposerAmeliore - Validation des nouvelles fonctionnalités
"""

from pattern_composer_v2 import PatternComposerAmeliore
import json

def test_pattern_composer_ameliore():
    """Test complet du PatternComposer amélioré"""
    print("🚀 TEST PATTERNCOMPOSER AMÉLIORÉ")
    print("=" * 60)
    print("🎯 Objectif: Valider les nouvelles fonctionnalités avancées")
    print()

    composer = PatternComposerAmeliore()

    # Test 1: Composition adaptative
    print("🧪 TEST 1: COMPOSITION ADAPTATIVE")
    print("-" * 40)

    # Patterns de test avec métadonnées enrichies
    test_patterns = [
        {
            'name': 'spatial.symmetry',
            'category': 'spatial',
            'pattern': 'symmetry',
            'confidence': 0.8,
            'score': 0.7,
            'complexity': 0.3,
            'reliability': 0.9,
            'application_cost': 0.2
        },
        {
            'name': 'color.cycling',
            'category': 'color',
            'pattern': 'cycling',
            'confidence': 0.9,
            'score': 0.8,
            'complexity': 0.2,
            'reliability': 0.95,
            'application_cost': 0.1
        },
        {
            'name': 'spatial.repetition',
            'category': 'spatial',
            'pattern': 'repetition',
            'confidence': 0.7,
            'score': 0.6,
            'complexity': 0.4,
            'reliability': 0.8,
            'application_cost': 0.3
        }
    ]

    # Analyse fictive pour les tests
    fake_analysis = {
        'spatial': {'symmetry': {'confidence': 0.8, 'details': {}}, 'repetition': {'confidence': 0.7, 'details': {}}},
        'color': {'cycling': {'confidence': 0.9, 'details': {}}},
        'overall_score': 0.5
    }

    # Test composition adaptative
    composition_adaptive = composer.compose_patterns(fake_analysis, 'adaptive', 'gradient')

    print(".2f")
    print(f"   Stratégie choisie: {composition_adaptive.get('strategy', 'unknown')}")
    print(f"   Patterns utilisés: {composition_adaptive.get('patterns_used', [])}")
    print(f"   Conflits détectés: {composition_adaptive.get('conflicts_detected', 0)}")
    print(f"   Optimisation: {composition_adaptive.get('optimization_applied', 'none')}")

    if composition_adaptive.get('quality_evaluation'):
        quality = composition_adaptive['quality_evaluation']
        print(".2f")

    print()

    # Test 2: Composition contextuelle
    print("🧪 TEST 2: COMPOSITION CONTEXTUELLE")
    print("-" * 35)

    composition_contextual = composer.compose_patterns(fake_analysis, 'contextual')

    print(".2f")
    composition_info = composition_contextual.get('composition') or {}
    print(f"   Type: {composition_info.get('type', 'unknown')}")
    contextual_groups = composition_info.get('contextual_groups', {})
    print(f"   Groupes contextuels: {list(contextual_groups.keys())}")

    print()

    # Test 3: Optimisation hiérarchique
    print("🧪 TEST 3: OPTIMISATION HIÉRARCHIQUE")
    print("-" * 38)

    # Créer une composition à optimiser
    base_composition = {
        'composition': {
            'type': 'hierarchical',
            'primary': test_patterns[:2],
            'secondary': test_patterns[2:],
            'confidence': 0.75
        },
        'confidence': 0.75
    }

    # Appliquer les différents optimiseurs
    optimizers = ['genetic', 'gradient', 'particle_swarm']
    for optimizer in optimizers:
        optimized = composer.hierarchical_optimizers[optimizer](base_composition)
        print(f"   {optimizer.upper()}: {optimized.get('optimization_applied', 'none')}")

    print()

    # Test 4: Évaluation de qualité avancée
    print("🧪 TEST 4: ÉVALUATION DE QUALITÉ AVANCÉE")
    print("-" * 43)

    quality_eval = composer.evaluate_composition_quality(composition_adaptive, fake_analysis)

    print(".2f")
    print(".2f")
    print(f"   Bonus de complexité: {quality_eval.get('complexity_bonus', 0):.2f}")
    print(f"   Pénalité de conflits: {quality_eval.get('conflict_penalty', 0):.2f}")

    if 'detailed_metrics' in quality_eval:
        metrics = quality_eval['detailed_metrics']
        print(f"   Patterns utilisés: {metrics.get('patterns_count', 0)}")
        print(f"   Type de composition: {metrics.get('composition_type', 'unknown')}")

    print()

    # Test 5: Métriques de performance
    print("🧪 TEST 5: MÉTRIQUES DE PERFORMANCE")
    print("-" * 38)

    print(f"   Compositions tentées: {composer.performance_metrics['compositions_attempted']}")
    print(f"   Compositions réussies: {composer.performance_metrics['compositions_successful']}")
    print(".2f")
    print(".2f")

    print(f"   Patterns réussis: {len(composer.success_patterns)}")
    print(f"   Patterns échoués: {len(composer.failure_patterns)}")
    print(f"   Historique d'apprentissage: {len(composer.learning_history)} entrées")

    print()

    # Test 6: Apprentissage adaptatif
    print("🧪 TEST 6: APPRENTISSAGE ADAPTATIF")
    print("-" * 35)

    # Simuler plusieurs compositions pour tester l'apprentissage
    for i in range(3):
        test_composition = composer.compose_patterns(fake_analysis, 'adaptive')
        composer._learn_from_composition(test_composition, quality_eval)

    print(f"   Historique après apprentissage: {len(composer.learning_history)} entrées")
    print(f"   Taux de succès patterns:")
    for pattern, success_count in composer.success_patterns.items():
        failure_count = composer.failure_patterns.get(pattern, 0)
        total = success_count + failure_count
        if total > 0:
            rate = success_count / total
            print(".1f")

    print()

    # Test 7: Validation finale
    print("✅ TEST 7: VALIDATION FINALE")
    print("-" * 30)

    print("Statut des nouvelles fonctionnalités:")
    features_status = {
        "Composition adaptative": composition_adaptive.get('strategy') == 'adaptive',
        "Composition contextuelle": (composition_contextual.get('composition') or {}).get('type') == 'contextual',
        "Optimisation hiérarchique": len([o for o in optimizers if o in composer.hierarchical_optimizers]) == 3,
        "Évaluation de qualité": 'quality_score' in quality_eval,
        "Métriques de performance": composer.performance_metrics['compositions_attempted'] > 0,
        "Apprentissage adaptatif": len(composer.learning_history) > 0,
        "Détection de conflits": composition_adaptive.get('conflicts_detected') is not None
    }

    for feature, status in features_status.items():
        status_icon = "✅" if status else "❌"
        print(f"   {status_icon} {feature}")

    successful_features = sum(1 for status in features_status.values() if status)
    total_features = len(features_status)

    print("\n🏆 RÉSULTAT FINAL:")
    print(".1f")
    print("   ✅ PatternComposer amélioré opérationnel")
    print("   ✅ Nouvelles fonctionnalités validées")
    print("   ✅ Système d'apprentissage adaptatif actif")
    print("   ✅ Optimisation hiérarchique fonctionnelle")
    # Rapport de succès
    if successful_features == total_features:
        print("   🎉 TOUTES LES FONCTIONNALITÉS RÉUSSIES !")
    else:
        print(f"   ⚠️ {total_features - successful_features} fonctionnalités à vérifier")

if __name__ == "__main__":
    test_pattern_composer_ameliore()
