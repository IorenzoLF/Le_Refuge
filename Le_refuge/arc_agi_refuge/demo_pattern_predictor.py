#!/usr/bin/env python3
"""
Demo PatternPredictor V2 - Version simplifiée
"""

from pattern_predictor_v2 import PatternPredictorV2

def demo_pattern_predictor():
    """Demo simplifiée du PatternPredictor"""
    print("DEMO PATTERN PREDICTOR V2")
    print("=" * 30)

    predictor = PatternPredictorV2()

    # Demo 1: Prediction simple
    print("\n1. PREDICTION SIMPLE")

    patterns_detectes = {
        'spatial': {
            'spatial.symmetry': {
                'confidence': 0.8,
                'score': 0.7,
                'details': {}
            }
        }
    }

    contexte = {
        'dimensions': [10, 10],
        'couleurs_uniques': 4,
        'patterns_detectes': ['spatial.symmetry'],
        'complexite_estimee': 0.6
    }

    print("Patterns detectes: spatial.symmetry")

    predictions = predictor.predire_patterns_manquants(
        patterns_detectes, contexte, seuil_confiance=0.5
    )

    print("Predictions:")
    total = 0
    for categorie, patterns_predits in predictions.items():
        for pattern_name, prediction in patterns_predits.items():
            print(f"  - {pattern_name} ({prediction['methode']})")
            total += 1

    print(f"Total: {total} patterns predits")

    # Demo 2: Statistiques
    print("\n2. STATISTIQUES")

    stats = predictor.obtenir_statistiques()
    print(f"Predictions tentées: {stats['total_predictions']}")
    print(f"Méthodes de prediction: {stats['methodes_prediction']}")

    print("\n3. METHODES DE PREDICTION")
    for i, methode in enumerate(predictor.modeles_prediction.keys(), 1):
        print(f"  {i}. {methode}")

    print("\nDEMO TERMINEE AVEC SUCCES !")
    print("PatternPredictor V2 est operationnel")

if __name__ == "__main__":
    demo_pattern_predictor()
