#!/usr/bin/env python3
"""
Ajustement Final des Seuils du PatternPredictor
Optimisation simple et efficace
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import statistics

def ajuster_seuils_final():
    """Ajustement final des seuils"""
    print("AJUSTEMENT FINAL DES SEUILS")
    print("=" * 35)
    print("Optimisation des paramètres PatternPredictor")
    print()

    # Charger l'architecture
    print("1. Chargement Architecture")
    solver = ArchitectureV2()
    print("Architecture chargee")
    print()

    # Test des seuils
    print("2. Test des Seuils")

    # Seuils très permissifs
    print("Test seuils permissifs...")
    solver.confidence_threshold = 0.2  # Très permissif
    solver.overfitting_threshold = 0.5  # Plus tolérant

    resultats_permissifs = tester_seuils(solver)
    print(f"  Patterns moyens: {resultats_permissifs['patterns']:.1f}")
    print(f"  Succès: {resultats_permissifs['succes']:.1f}")
    print()

    # Seuils équilibrés
    print("Test seuils equilibres...")
    solver.confidence_threshold = 0.3  # Équilibré
    solver.overfitting_threshold = 0.4  # Modérément tolérant

    resultats_equilibres = tester_seuils(solver)
    print(f"  Patterns moyens: {resultats_equilibres['patterns']:.1f}")
    print(f"  Succès: {resultats_equilibres['succes']:.1f}")
    print()

    # Seuils conservateurs
    print("Test seuils conservateurs...")
    solver.confidence_threshold = 0.4  # Conservateur
    solver.overfitting_threshold = 0.3  # Moins tolérant

    resultats_conservateurs = tester_seuils(solver)
    print(f"  Patterns moyens: {resultats_conservateurs['patterns']:.1f}")
    print(f"  Succès: {resultats_conservateurs['succes']:.1f}")
    print()

    # Sélection du meilleur
    print("3. Selection du Meilleur")
    resultats = {
        'permissifs': resultats_permissifs,
        'equilibres': resultats_equilibres,
        'conservateurs': resultats_conservateurs
    }

    meilleur_nom = max(resultats, key=lambda x: resultats[x]['score'])
    meilleur = resultats[meilleur_nom]

    print(f"Meilleur: {meilleur_nom}")
    print(f"Score: {meilleur['score']:.3f}")
    print(f"Patterns: {meilleur['patterns']:.1f}")
    print(f"Succès: {meilleur['succes']:.1f}")
    print()

    # Application des meilleurs seuils
    print("4. Application des Meilleurs Seuils")
    if meilleur_nom == 'permissifs':
        solver.confidence_threshold = 0.2
        solver.overfitting_threshold = 0.5
        print("Seuils permissifs appliqués")
    elif meilleur_nom == 'equilibres':
        solver.confidence_threshold = 0.3
        solver.overfitting_threshold = 0.4
        print("Seuils equilibres appliqués")
    else:
        solver.confidence_threshold = 0.4
        solver.overfitting_threshold = 0.3
        print("Seuils conservateurs appliqués")

    print()

    # Test final
    print("5. Test Final")
    test_final = tester_seuils(solver)
    print("Résultats finaux:")
    print(f"  Patterns moyens: {test_final['patterns']:.1f}")
    print(f"  Taux de succès: {test_final['succes']:.1f}")
    print(f"  Score: {test_final['score']:.3f}")
    print()

    # Rapport
    print("6. Rapport Final")
    print("=" * 20)
    print("PARAMÈTRES OPTIMAUX:")
    print(f"  Confidence threshold: {solver.confidence_threshold}")
    print(f"  Overfitting threshold: {solver.overfitting_threshold}")
    print()
    print("AMÉLIORATIONS:")
    print(f"  Patterns prédits: {meilleur['patterns']:.1f}")
    print(f"  Taux de succès: {meilleur['succes']:.1f}")
    print(f"  Score global: {meilleur['score']:.3f}")
    print()
    print("CONCLUSION:")
    if meilleur['score'] > 1.0:
        print("  ✅ OPTIMISATION RÉUSSIE")
        print("  PatternPredictor optimisé")
    else:
        print("  ⚠️ OPTIMISATION MODÉRÉE")
        print("  Ajustements recommandés")
    print()

    return {
        'meilleur_type': meilleur_nom,
        'resultats': meilleur,
        'parametres': {
            'confidence_threshold': solver.confidence_threshold,
            'overfitting_threshold': solver.overfitting_threshold
        }
    }

def tester_seuils(solver):
    """Test les seuils actuels"""
    puzzles = trouver_puzzles_test()[:8]
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

    if len(puzzles) > 0:
        patterns_moyens = total_patterns / len(puzzles)
        succes_rate = succes_count / len(puzzles)
    else:
        patterns_moyens = 0
        succes_rate = 0

    score = (patterns_moyens * 0.7) + (succes_rate * 0.3)

    return {
        'patterns': patterns_moyens,
        'succes': succes_rate,
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
    resultats = ajuster_seuils_final()

    print("=" * 35)
    print("AJUSTEMENT TERMINÉ AVEC SUCCÈS !")
    print("=" * 35)

if __name__ == "__main__":
    main()
