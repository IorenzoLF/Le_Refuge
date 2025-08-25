#!/usr/bin/env python3
"""
🧪 TEST D'INTÉGRATION COMPLÈTE - PHASE 4
Validation que tous les modules fonctionnent ensemble dans le solveur
"""

from solveur_transparent_arc import SolveurTransparentARC

def test_integration_complete():
    """Test d'intégration complète de tous les modules"""

    print("🔧 TEST D'INTÉGRATION COMPLÈTE")
    print("=" * 50)

    solveur = SolveurTransparentARC()

    # Tests d'intégration avec différents types de puzzles
    tests_integration = [
        {
            'nom': 'Puzzle avec pattern dimensions',
            'puzzle_id': 'example_dimensions'  # Puzzle qui devrait déclencher les patterns dimensions
        },
        {
            'nom': 'Puzzle avec pattern couleurs',
            'puzzle_id': 'example_couleurs'  # Puzzle qui devrait déclencher les patterns couleurs
        },
        {
            'nom': 'Puzzle avec pattern spatiaux',
            'puzzle_id': 'example_spatiaux'  # Puzzle qui devrait déclencher les patterns spatiaux
        },
        {
            'nom': 'Puzzle avec pattern diagonaux',
            'puzzle_id': 'example_diagonaux'  # Puzzle qui devrait déclencher les patterns diagonaux
        }
    ]

    resultats_modules = {
        'dimensions': 0,
        'couleurs': 0,
        'spatiaux': 0,
        'diagonaux': 0,
        'repetition_simple': 0,
        'autres': 0
    }

    total_tests = 0
    tests_reussis = 0

    print("\n🧪 ANALYSE DES MODULES INTÉGRÉS:")
    print("-" * 40)

    # Tester avec des puzzles réels du dataset
    dataset_path = "ARC-AGI-2-main/data/training"
    import os
    if os.path.exists(dataset_path):
        puzzles_disponibles = [f.replace('.json', '') for f in os.listdir(dataset_path) if f.endswith('.json')]

        # Sélectionner quelques puzzles représentatifs
        puzzles_test = puzzles_disponibles[:10]  # Tester les 10 premiers

        for puzzle_id in puzzles_test:
            total_tests += 1
            try:
                print(f"\n📋 Test {total_tests}: {puzzle_id}")
                resultat = solveur.analyser_puzzle_complet(puzzle_id)

                pattern_type = resultat.pattern_type
                confiance = resultat.confiance

                # Classifier le pattern détecté
                if 'dimensions' in pattern_type or 'agrandissement' in pattern_type or 'reduction' in pattern_type:
                    resultats_modules['dimensions'] += 1
                    categorie = "📏 Dimensions"
                elif 'couleurs' in pattern_type or 'remplacement' in pattern_type or 'ajout' in pattern_type or 'suppression' in pattern_type:
                    resultats_modules['couleurs'] += 1
                    categorie = "🎨 Couleurs"
                elif 'spatiaux' in pattern_type or 'remplissage' in pattern_type or 'deformation' in pattern_type or 'symetrie_avancee' in pattern_type:
                    resultats_modules['spatiaux'] += 1
                    categorie = "🌀 Spatiaux"
                elif 'diagonal' in pattern_type or 'propagation' in pattern_type:
                    resultats_modules['diagonaux'] += 1
                    categorie = "🔄 Diagonaux"
                elif 'repetition' in pattern_type:
                    resultats_modules['repetition_simple'] += 1
                    categorie = "🔁 Répétition"
                else:
                    resultats_modules['autres'] += 1
                    categorie = "❓ Autres"

                # Évaluer la qualité du résultat
                if hasattr(resultat, 'similarite') and resultat.similarite > 0:
                    statut = ".1f"                    if resultat.similarite > 50:
                        tests_reussis += 1
                else:
                    statut = ".1f"                    if confiance > 0.8:
                        tests_reussis += 1

                print(f"   {categorie} | Pattern: {pattern_type} | {statut}")

            except Exception as e:
                print(f"   ❌ Erreur: {e}")
                resultats_modules['autres'] += 1

    # Résumé des résultats
    print("
📊 RÉSUMÉ DE L'INTÉGRATION:"    print("=" * 40)

    total_patterns_detectes = sum(resultats_modules.values())

    print(f"Tests effectués: {total_tests}")
    print(f"Tests réussis: {tests_reussis}")
    print(".1f")

    print("
🔍 PATTERNS DÉTECTÉS:"    print("-" * 25)

    for module, count in resultats_modules.items():
        if count > 0:
            pourcentage = (count / total_patterns_detectes) * 100 if total_patterns_detectes > 0 else 0
            emoji = {
                'dimensions': '📏',
                'couleurs': '🎨',
                'spatiaux': '🌀',
                'diagonaux': '🔄',
                'repetition_simple': '🔁',
                'autres': '❓'
            }.get(module, '❓')

            print("6s")

    # Évaluation globale
    print("
🎯 ÉVALUATION GLOBALE:"    print("-" * 25)

    if tests_reussis / total_tests > 0.8:
        evaluation = "✅ EXCELLENTE - Tous les modules bien intégrés"
    elif tests_reussis / total_tests > 0.6:
        evaluation = "⚠️ BONNE - Intégration fonctionnelle avec quelques problèmes"
    elif tests_reussis / total_tests > 0.4:
        evaluation = "🔧 AMÉLIORABLE - Besoin d'optimisations"
    else:
        evaluation = "❌ PROBLÉMATIQUE - Problèmes d'intégration majeurs"

    print(f"Status: {evaluation}")

    # Recommandations
    print("
💡 RECOMMANDATIONS:"    print("-" * 20)

    if resultats_modules['dimensions'] == 0:
        print("• Aucun pattern de dimensions détecté - vérifier l'intégration")
    if resultats_modules['diagonaux'] == 0:
        print("• Aucun pattern diagonal détecté - vérifier l'intégration")
    if resultats_modules['spatiaux'] == 0:
        print("• Aucun pattern spatial détecté - vérifier l'intégration")

    print("• Tester avec plus de puzzles pour valider l'intégration")
    print("• Optimiser les patterns avec faible taux de détection")

    return {
        'tests_total': total_tests,
        'tests_reussis': tests_reussis,
        'taux_succes': tests_reussis / total_tests if total_tests > 0 else 0,
        'modules_actifs': {k: v for k, v in resultats_modules.items() if v > 0}
    }

if __name__ == "__main__":
    test_integration_complete()
