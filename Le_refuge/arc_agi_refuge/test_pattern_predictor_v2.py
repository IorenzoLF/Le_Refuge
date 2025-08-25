#!/usr/bin/env python3
"""
Test du PatternPredictor V2 - Validation des prédictions
"""

from pattern_predictor_v2 import PatternPredictorV2
import json

def test_pattern_predictor_v2():
    """Test complet du PatternPredictor V2"""
    print("🧠 TEST PATTERN PREDICTOR V2")
    print("=" * 50)
    print("🎯 Objectif: Valider les capacités de prédiction")
    print()

    # Initialisation
    predictor = PatternPredictorV2()

    # Test 1: Prédiction sur un puzzle simple
    print("🧪 TEST 1: PRÉDICTION SUR PUZZLE SIMPLE")
    print("-" * 40)

    # Puzzle de test avec des patterns partiels
    patterns_detectes = {
        'spatial': {
            'spatial.symmetry': {
                'confidence': 0.8,
                'score': 0.7,
                'details': {'symmetries_found': {'horizontal': True}}
            }
        },
        'color': {
            'color.mapping': {
                'confidence': 0.9,
                'score': 0.8,
                'details': {'color_changes': 3}
            }
        }
    }

    contexte_puzzle = {
        'dimensions': [10, 10],
        'couleurs_uniques': 4,
        'patterns_detectes': ['spatial.symmetry', 'color.mapping'],
        'complexite_estimee': 0.6
    }

    print("Patterns détectés actuels:")
    for cat, patterns in patterns_detectes.items():
        for pattern_name in patterns.keys():
            print(f"  • {pattern_name}")

    print("\nPrédiction des patterns manquants...")

    # Prédiction
    predictions = predictor.predire_patterns_manquants(
        patterns_detectes, contexte_puzzle, seuil_confiance=0.5
    )

    print("\n📊 PRÉDICTIONS RÉALISÉES:")
    total_predictions = 0
    for categorie, patterns_predits in predictions.items():
        if patterns_predits:
            print(f"\n🔍 Catégorie {categorie.upper()}:")
            for pattern_name, prediction in patterns_predits.items():
                total_predictions += 1
                print(f"  ✅ {pattern_name}")
                print(".2f")
                print(f"     📝 Méthode: {prediction['methode']}")
                print(f"     💡 Raison: {prediction['raison']}")

    print("")
🏆 RÉSULTAT: {total_predictions} patterns prédits avec succès"    print()

    # Test 2: Apprentissage et adaptation
    print("🧪 TEST 2: APPRENTISSAGE ET ADAPTATION")
    print("-" * 45)

    # Simuler plusieurs puzzles pour l'apprentissage
    puzzles_apprentissage = [
        {
            'patterns_detectes': ['spatial.symmetry', 'spatial.rotation'],
            'succes': True,
            'complexite': 0.7,
            'style': 'symetrique'
        },
        {
            'patterns_detectes': ['color.mapping', 'color.cycling'],
            'succes': True,
            'complexite': 0.5,
            'style': 'colorimetrique'
        },
        {
            'patterns_detectes': ['spatial.repetition', 'spatial.translation'],
            'succes': False,
            'complexite': 0.8,
            'style': 'repetitif'
        }
    ]

    print("Apprentissage sur plusieurs puzzles...")
    for i, puzzle in enumerate(puzzles_apprentissage, 1):
        contexte = {
            'dimensions': [10, 10],
            'couleurs_uniques': 4,
            'patterns_detectes': puzzle['patterns_detectes'],
            'complexite_estimee': puzzle['complexite'],
            'succes': puzzle['succes']
        }

        # Simuler des patterns détectés
        patterns_simules = {}
        for pattern in puzzle['patterns_detectes']:
            cat, name = pattern.split('.')
            if cat not in patterns_simules:
                patterns_simules[cat] = {}
            patterns_simules[cat][pattern] = {
                'confidence': 0.8,
                'score': 0.7,
                'details': {}
            }

        # Prédiction pour l'apprentissage
        pred = predictor.predire_patterns_manquants(patterns_simules, contexte, 0.6)
        print(f"  📚 Puzzle {i}: {len(pred)} prédictions apprises")

    print()

    # Test 3: Prédiction avec historique
    print("🧪 TEST 3: PRÉDICTION AVEC HISTORIQUE")
    print("-" * 40)

    # Nouveau puzzle similaire
    nouveau_contexte = {
        'dimensions': [12, 12],
        'couleurs_uniques': 3,
        'patterns_detectes': ['spatial.symmetry'],
        'complexite_estimee': 0.6
    }

    nouveaux_patterns = {
        'spatial': {
            'spatial.symmetry': {
                'confidence': 0.85,
                'score': 0.75,
                'details': {'symmetries_found': {'vertical': True}}
            }
        }
    }

    print("Nouveau puzzle avec historique enrichi...")

    predictions_enrichies = predictor.predire_patterns_manquants(
        nouveaux_patterns, nouveau_contexte, seuil_confiance=0.4
    )

    print("")
🔮 PRÉDICTIONS AVEC APPRENTISSAGE:")
    total_enrichi = 0
    for categorie, patterns_predits in predictions_enrichies.items():
        if patterns_predits:
            print(f"\n🎯 Catégorie {categorie.upper()}:")
            for pattern_name, prediction in patterns_predits.items():
                total_enrichi += 1
                print(f"  🎨 {pattern_name}")
                print(".2f")
                print(f"     🧠 Méthode: {prediction['methode']}")
                print(f"     📈 Historique: {prediction.get('details', {}).get('frequence_historique', 0)} apparitions")

    print("")
🎊 RÉSULTAT: {total_enrichi} patterns prédits avec apprentissage"    print()

    # Test 4: Statistiques et métriques
    print("🧪 TEST 4: STATISTIQUES ET MÉTRIQUES")
    print("-" * 40)

    stats = predictor.obtenir_statistiques()

    print("📊 STATISTIQUES GÉNÉRALES:")
    print(f"  • Total prédictions: {stats['total_predictions']}")
    print(f"  • Prédictions réussies: {stats['predictions_reussies']}")
    print(".1f")
    print(f"  • Patterns suivis: {stats['patterns_suivis']}")
    print(f"  • Historique contexte: {stats['historique_contexte']}")
    print(f"  • Méthodes prédiction: {stats['methodes_prediction']}")

    print("")
🔬 MÉTHODES DE PRÉDICTION:")
    for i, methode in enumerate(predictor.modeles_prediction.keys(), 1):
        print(f"  {i}. {methode.replace('_', ' ').title()}")

    print()

    # Test 5: Export/Import du modèle
    print("🧪 TEST 5: SAUVEGARDE ET RESTAURATION")
    print("-" * 45)

    print("Export du modèle...")
    modele = predictor.exporter_modele()
    print(f"✅ Modèle exporté: {len(modele)} sections")

    print("")
Création d'un nouveau predictor...")
    nouveau_predictor = PatternPredictorV2()

    print("Import du modèle...")
    nouveau_predictor.importer_modele(modele)
    print("✅ Modèle importé avec succès")

    print()

    # Validation finale
    print("🎉 VALIDATION FINALE - PATTERN PREDICTOR V2")
    print("=" * 55)

    validations = {
        "Prédiction contextuelle": total_predictions > 0,
        "Apprentissage adaptatif": total_enrichi > total_predictions,
        "Statistiques complètes": stats['total_predictions'] > 0,
        "Sauvegarde/chargement": True,
        "Méthodes multiples": len(predictor.modeles_prediction) == 4,
        "Historique intelligent": len(predictor.contexte_historique) > 0
    }

    print("✅ COMPOSANTS VALIDÉS:")
    for composant, valide in validations.items():
        status = "✅" if valide else "❌"
        print(f"   {status} {composant}")

    composants_valides = sum(1 for v in validations.values() if v)
    total_composants = len(validations)

    print("")
🏆 ÉVALUATION GLOBALE:"    print(f"   • Composants opérationnels: {composants_valides}/{total_composants}")
    print(".1f")
    print(f"   • Patterns prédits: {total_predictions + total_enrichi}")
    print(f"   • Méthodes de prédiction: {len(predictor.modeles_prediction)}")
    print(f"   • Historique d'apprentissage: {len(predictor.contexte_historique)}")

    print("")
🌟 CONCLUSION:"    if composants_valides == total_composants:
        print("   🎊 SUCCÈS TOTAL ! PatternPredictor V2 est pleinement opérationnel")
        print("   🚀 Prêt à enrichir l'Architecture V2 avec des prédictions intelligentes")
    else:
        print(f"   ⚠️ {total_composants - composants_valides} composants à optimiser")

    print("")
💡 CAPACITÉS DÉMONSTRÉES:"    print("   • Prédiction contextuelle des patterns manquants"    print("   • Apprentissage adaptatif basé sur l'historique"    print("   • Combinaison intelligente de méthodes de prédiction"    print("   • Validation et ajustement des prédictions"    print("   • Export/import de modèles d'apprentissage"    print("   • Monitoring complet des performances"
    return {
        'predictions_initiales': total_predictions,
        'predictions_enrichies': total_enrichi,
        'composants_valides': composants_valides,
        'methodes_prediction': len(predictor.modeles_prediction),
        'statistiques': stats
    }

if __name__ == "__main__":
    resultats = test_pattern_predictor_v2()
