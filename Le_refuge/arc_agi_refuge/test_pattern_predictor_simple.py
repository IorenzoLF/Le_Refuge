#!/usr/bin/env python3
"""
Test Simple du PatternPredictor V2
"""

from pattern_predictor_v2 import PatternPredictorV2

def test_pattern_predictor_simple():
    """Test simple du PatternPredictor"""
    print("TEST PATTERN PREDICTOR V2")
    print("=" * 40)
    print("Objectif: Valider les capacites de prediction")
    print()

    predictor = PatternPredictorV2()

    # Test de prediction simple
    print("TEST 1: PREDICTION SIMPLE")
    print("-" * 30)

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

    print("Patterns detectes:")
    for cat, patterns in patterns_detectes.items():
        for pattern_name in patterns.keys():
            print(f"  - {pattern_name}")

    print("\nPrediction des patterns manquants...")

    predictions = predictor.predire_patterns_manquants(
        patterns_detectes, contexte_puzzle, seuil_confiance=0.5
    )

    print("\nPREDICTIONS REALISEES:")
    total_predictions = 0
    for categorie, patterns_predits in predictions.items():
        if patterns_predits:
            print(f"\nCategorie {categorie.upper()}:")
            for pattern_name, prediction in patterns_predits.items():
                total_predictions += 1
                print(f"  + {pattern_name}")
                print(".2f")
                print(f"    Methode: {prediction['methode']}")
                print(f"    Raison: {prediction['raison']}")

    print(f"\nRESULTAT: {total_predictions} patterns predits avec succes")
    print()

    # Test d'apprentissage
    print("TEST 2: APPRENTISSAGE")
    print("-" * 25)

    for i in range(3):
        contexte_apprentissage = {
            'dimensions': [10, 10],
            'couleurs_uniques': 4,
            'patterns_detectes': ['spatial.symmetry', 'spatial.rotation'],
            'complexite_estimee': 0.7
        }

        patterns_apprentissage = {
            'spatial': {
                'spatial.symmetry': {'confidence': 0.8, 'score': 0.7, 'details': {}},
                'spatial.rotation': {'confidence': 0.7, 'score': 0.6, 'details': {}}
            }
        }

        pred = predictor.predire_patterns_manquants(
            patterns_apprentissage, contexte_apprentissage, 0.6
        )
        print(f"  Apprentissage {i+1}: {sum(len(p) for p in pred.values())} predictions")

    print()

    # Test avec historique
    print("TEST 3: PREDICTION AVEC HISTORIQUE")
    print("-" * 40)

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

    predictions_enrichies = predictor.predire_patterns_manquants(
        nouveaux_patterns, nouveau_contexte, seuil_confiance=0.4
    )

    print("PREDICTIONS AVEC APPRENTISSAGE:")
    total_enrichi = 0
    for categorie, patterns_predits in predictions_enrichies.items():
        if patterns_predits:
            print(f"\nCategorie {categorie.upper()}:")
            for pattern_name, prediction in patterns_predits.items():
                total_enrichi += 1
                print(f"  * {pattern_name}")
                print(".2f")
                print(f"    Methode: {prediction['methode']}")

    print(f"\nRESULTAT: {total_enrichi} patterns predits avec apprentissage")
    print()

    # Statistiques
    print("TEST 4: STATISTIQUES")
    print("-" * 25)

    stats = predictor.obtenir_statistiques()
    print(f"Total predictions: {stats['total_predictions']}")
    print(f"Predictions reussies: {stats['predictions_reussies']}")
    print(".1f")
    print(f"Patterns suivis: {stats['patterns_suivis']}")
    print(f"Méthodes prediction: {stats['methodes_prediction']}")

    print()

    # Validation finale
    print("VALIDATION FINALE")
    print("=" * 30)

    validations = {
        "Prediction contextuelle": total_predictions > 0,
        "Apprentissage adaptatif": total_enrichi > 0,
        "Statistiques completes": stats['total_predictions'] > 0,
        "Methodes multiples": len(predictor.modeles_prediction) == 4,
        "Historique intelligent": len(predictor.contexte_historique) > 0
    }

    print("COMPOSANTS VALIDES:")
    for composant, valide in validations.items():
        status = "OK" if valide else "NOK"
        print(f"  {status} - {composant}")

    composants_valides = sum(1 for v in validations.values() if v)
    total_composants = len(validations)

    print("\nEVALUATION GLOBALE:")
    print(f"  Composants operationnels: {composants_valides}/{total_composants}")
    print(".1f")
    print(f"  Patterns predits: {total_predictions + total_enrichi}")
    print(f"  Methodes de prediction: {len(predictor.modeles_prediction)}")
    print(f"  Historique d'apprentissage: {len(predictor.contexte_historique)}")

    print("
CONCLUSION:"    if composants_valides == total_composants:
        print("  SUCCES ! PatternPredictor V2 est operationnel")
        print("  Pret a enrichir l'Architecture V2")
    else:
        print(f"  {total_composants - composants_valides} composants a optimiser")

    return {
        'predictions_initiales': total_predictions,
        'predictions_enrichies': total_enrichi,
        'composants_valides': composants_valides,
        'methodes_prediction': len(predictor.modeles_prediction),
        'statistiques': stats
    }

if __name__ == "__main__":
    resultats = test_pattern_predictor_simple()
