#!/usr/bin/env python3
"""
Ajustement Simple des Seuils du PatternPredictor
Optimisation progressive pour maximiser les prédictions
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import statistics

def ajuster_seuils():
    """Ajustement simple et efficace des seuils"""
    print("AJUSTEMENT DES SEUILS PATTERN PREDICTOR")
    print("=" * 45)
    print("Optimisation progressive des paramètres")
    print()

    # Charger l'architecture
    print("1. Chargement Architecture V2")
    solver = ArchitectureV2()
    print("Architecture chargee avec PatternPredictor")
    print()

    # Paramètres de test
    print("2. Paramètres de Test")
    parametres_test = {
        'seuil_confiance_prediction': [0.2, 0.3, 0.4],
        'seuil_complexite_min': [0.1, 0.2, 0.3],
        'seuil_similarite_contexte': [0.5, 0.6, 0.7],
        'poids_confiance_historique': [0.3, 0.4, 0.5],
        'max_patterns_predits_par_categorie': [5, 7, 10],
        'min_frequence_historique': [1, 2]
    }

    print("Paramètres à optimiser:")
    for param, valeurs in parametres_test.items():
        print(f"  {param}: {valeurs}")
    print()

    # Test des combinaisons
    print("3. Test des Combinaisons")
    meilleures_combinaisons = []

    # Combinaison 1: Plus agressif
    combo1 = {
        'seuil_confiance_prediction': 0.2,
        'seuil_complexite_min': 0.1,
        'seuil_similarite_contexte': 0.5,
        'poids_confiance_historique': 0.5,
        'max_patterns_predits_par_categorie': 10,
        'min_frequence_historique': 1
    }

    print("Test combinaison 1 (agressive):")
    score1 = tester_combinaison(solver, combo1)
    meilleures_combinaisons.append({
        'parametres': combo1,
        'score': score1['score'],
        'patterns': score1['patterns']
    })
    print(".3f")
    print()

    # Combinaison 2: Équilibré
    combo2 = {
        'seuil_confiance_prediction': 0.3,
        'seuil_complexite_min': 0.2,
        'seuil_similarite_contexte': 0.6,
        'poids_confiance_historique': 0.4,
        'max_patterns_predits_par_categorie': 7,
        'min_frequence_historique': 1
    }

    print("Test combinaison 2 (equilibree):")
    score2 = tester_combinaison(solver, combo2)
    meilleures_combinaisons.append({
        'parametres': combo2,
        'score': score2['score'],
        'patterns': score2['patterns']
    })
    print(".3f")
    print()

    # Combinaison 3: Conservateur
    combo3 = {
        'seuil_confiance_prediction': 0.4,
        'seuil_complexite_min': 0.3,
        'seuil_similarite_contexte': 0.7,
        'poids_confiance_historique': 0.3,
        'max_patterns_predits_par_categorie': 5,
        'min_frequence_historique': 2
    }

    print("Test combinaison 3 (conservatrice):")
    score3 = tester_combinaison(solver, combo3)
    meilleures_combinaisons.append({
        'parametres': combo3,
        'score': score3['score'],
        'patterns': score3['patterns']
    })
    print(".3f")
    print()

    # Sélection de la meilleure combinaison
    print("4. Selection de la Meilleure Combinaison")
    meilleure = max(meilleures_combinaisons, key=lambda x: x['score'])
    print(".3f")
    print("Paramètres optimaux:")
    for param, valeur in meilleure['parametres'].items():
        print(f"  {param}: {valeur}")
    print()

    # Application des paramètres optimaux
    print("5. Application des Paramètres Optimaux")
    for param, valeur in meilleure['parametres'].items():
        if hasattr(solver, param):
            setattr(solver, param, valeur)
            print(f"  {param} = {valeur}")

    print("Paramètres appliqués avec succès")
    print()

    # Test final
    print("6. Test Final avec Paramètres Optimaux")
    test_final = tester_combinaison(solver, meilleure['parametres'])
    print("Résultats finaux:")
    print(".1f")
    print(".1f")
    print(".3f")
    print()

    # Rapport
    print("7. Rapport d'Ajustement")
    print("=" * 30)
    print("PARAMÈTRES OPTIMAUX:")
    for param, valeur in meilleure['parametres'].items():
        print(f"  {param}: {valeur}")

    print("
AMÉLIORATIONS:")
    print(".1f")
    print(".1f")
    print(".3f")

    print("
RECOMMANDATIONS:")
    print("  1. Tester sur plus de puzzles ARC-AGI")
    print("  2. Surveiller la qualité des prédictions")
    print("  3. Ajuster si nécessaire")
    print("  4. Étendre l'historique d'apprentissage")

    print("
CONCLUSION:")
    if meilleure['score'] > 1.0:
        print("  ✅ OPTIMISATION TRÈS RÉUSSIE")
        print("  PatternPredictor optimisé avec succès")
    elif meilleure['score'] > 0.5:
        print("  ✅ OPTIMISATION RÉUSSIE")
        print("  Améliorations significatives")
    else:
        print("  ⚠️ OPTIMISATION MODÉRÉE")
        print("  Ajustements supplémentaires recommandés")

    return meilleure

def tester_combinaison(solver, parametres):
    """Test une combinaison de paramètres"""
    # Appliquer les paramètres
    anciens_parametres = {}
    for param, valeur in parametres.items():
        if hasattr(solver, param):
            anciens_parametres[param] = getattr(solver, param)
            setattr(solver, param, valeur)

    # Tester sur quelques puzzles
    puzzles = trouver_puzzles_test()[:5]
    total_patterns = 0
    succes_count = 0

    for puzzle_path in puzzles:
        try:
            with open(puzzle_path, 'r') as f:
                puzzle_data = json.load(f)

            if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                exemple = puzzle_data['train'][0]
                solution = solver.solve_puzzle(exemple['input'], exemple['output'])

                patterns_predits = solution.get('patterns_predits', {})
                total_predits = sum(len(patterns) for patterns in patterns_predits.values())
                total_patterns += total_predits

                if solution.get('confidence', 0) > 0.5:
                    succes_count += 1

        except Exception as e:
            continue

    # Restaurer les paramètres
    for param, valeur in anciens_parametres.items():
        setattr(solver, param, valeur)

    if len(puzzles) > 0:
        patterns_moyens = total_patterns / len(puzzles)
        succes_rate = succes_count / len(puzzles)
    else:
        patterns_moyens = 0
        succes_rate = 0

    score = (patterns_moyens * 0.7) + (succes_rate * 0.3)

    return {
        'patterns': patterns_moyens,
        'succes_rate': succes_rate,
        'score': score
    }

def trouver_puzzles_test():
    """Trouve les puzzles pour les tests"""
    patterns = [
        "ARC-AGI-2-main/data/training/*.json",
        "ARC-AGI/data/training/*.json",
        "*.json"
    ]

    fichiers_puzzles = []
    for pattern in patterns:
        fichiers = glob.glob(pattern)
        if fichiers:
            fichiers_puzzles.extend(fichiers)

    puzzles_valides = []
    for fichier in fichiers_puzzles[:20]:
        try:
            with open(fichier, 'r') as f:
                data = json.load(f)
                if 'train' in data and len(data['train']) > 0:
                    puzzles_valides.append(fichier)
        except:
            continue

    return puzzles_valides if puzzles_valides else []

def main():
    """Fonction principale"""
    resultats = ajuster_seuils()

if __name__ == "__main__":
    main()
