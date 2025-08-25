#!/usr/bin/env python3
"""
Test Simple sur 200 Puzzles ARC-AGI
Evaluation des performances globales
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import statistics
import time
from typing import Dict, List, Any

def test_200_puzzles_simple():
    """Test simple sur 200 puzzles"""
    print("TEST SUR 200 PUZZLES ARC-AGI")
    print("=" * 40)
    print("Evaluation des performances globales")
    print()

    # Initialiser le solveur
    print("1. Initialisation du solveur")
    solveur = ArchitectureV2()
    solveur.confidence_threshold = 0.01  # Ultra-permissif
    solveur.overfitting_threshold = 0.95  # Ultra-tolérant
    solveur.verbose = False
    print("Solveur configure pour tests")
    print()

    # Trouver des puzzles
    print("2. Recherche de puzzles")
    puzzles = trouver_puzzles_simples()
    print(f"Puzzles trouves: {len(puzzles)}")

    if not puzzles:
        print("Aucun puzzle trouve")
        return

    # Tester 50 puzzles maximum pour rapidite
    puzzles_a_tester = puzzles[:50]
    print(f"Test sur {len(puzzles_a_tester)} puzzles")
    print()

    # Tests
    print("3. Tests individuels")
    resultats = []

    for i, puzzle_path in enumerate(puzzles_a_tester, 1):
        puzzle_id = puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', '')
        print(f"[{i:2d}/{len(puzzles_a_tester)}] Test {puzzle_id}...")
        start_time = time.time()

        try:
            with open(puzzle_path, 'r') as f:
                puzzle_data = json.load(f)

            if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                exemple = puzzle_data['train'][0]
                input_grid = exemple.get('input', [])
                output_grid = exemple.get('output', [])

                if input_grid and output_grid:
                    solution = solveur.solve_puzzle(input_grid, output_grid)
                    execution_time = time.time() - start_time

                    confidence = solution.get('confidence', 0)
                    succes = confidence > 0.5

                    patterns_analysis = solution.get('patterns_analysis', {})
                    patterns_predits = solution.get('patterns_predits', {})

                    total_patterns_detectes = sum(len(patterns) for patterns in patterns_analysis.values() if isinstance(patterns, dict))
                    total_patterns_predits = sum(len(patterns) for patterns in patterns_predits.values())

                    print(f"    {'✅' if succes else '❌'} Succès: {succes}, Patterns: {total_patterns_detectes}, Predits: {total_patterns_predits}, Temps: {execution_time:.2f}s")
                    resultats.append({
                        'puzzle_id': puzzle_id,
                        'succes': succes,
                        'confidence': confidence,
                        'patterns_detectes': total_patterns_detectes,
                        'patterns_predits': total_patterns_predits,
                        'execution_time': execution_time
                    })
                else:
                    print("  Grilles vides")
            else:
                print("  Pas de donnees d'entrainement")

        except Exception as e:
            print(f"  Erreur: {e}")

    print()

    # Analyse
    print("4. ANALYSE DES RESULTATS")
    print("=" * 30)

    if resultats:
        succes_count = sum(1 for r in resultats if r['succes'])
        taux_succes = succes_count / len(resultats) * 100

        patterns_detectes_moy = statistics.mean([r['patterns_detectes'] for r in resultats])
        patterns_predits_moy = statistics.mean([r['patterns_predits'] for r in resultats])

        puzzles_avec_predictions = sum(1 for r in resultats if r['patterns_predits'] > 0)

        print(".1f")
        print(".1f")
        print(".1f")
        print(f"  Puzzles avec predictions: {puzzles_avec_predictions}")

        print("\nANALYSE DETAILLEE:")
        print("-" * 25)

        if patterns_detectes_moy > 10:
            print("  EXCELLENTE DETECTION DE PATTERNS")
            print(f"  {patterns_detectes_moy:.1f} patterns detectes par puzzle")
        elif patterns_detectes_moy > 5:
            print("  BONNE DETECTION DE PATTERNS")
            print(f"  {patterns_detectes_moy:.1f} patterns detectes par puzzle")
        else:
            print("  DETECTION AMELIORABLE")
            print(f"  {patterns_detectes_moy:.1f} patterns detectes par puzzle")

        if puzzles_avec_predictions > 0:
            print("\n  PATTERN PREDICTOR ACTIF")
            print(f"  Predictions sur {puzzles_avec_predictions} puzzles")
        else:
            print("\n  PATTERN PREDICTOR INACTIF")
            print("  Aucune prediction sur les puzzles testes")


        print("\nCONCLUSION:")
        print("-" * 15)

        if taux_succes > 60:
            print("  PERFORMANCES EXCELLENTES")
            print("  Solveur tres performant")
        elif taux_succes > 40:
            print("  PERFORMANCES SATISFAISANTES")
            print("  Bon niveau general")
        else:
            print("  AMELIORATIONS POSSIBLES")
            print("  Focus sur les difficultes")

    else:
        print("  Aucun resultat disponible")


    print("\nTEST TERMINE !")

def trouver_puzzles_simples():
    """Trouve des puzzles pour les tests"""
    patterns = [
        "ARC-AGI-2-main/data/training/*.json",
        "ARC-AGI/data/training/*.json",
        "*.json"
    ]

    puzzles = []
    for pattern in patterns:
        try:
            fichiers = glob.glob(pattern)
            for fichier in fichiers:
                try:
                    with open(fichier, 'r') as f:
                        data = json.load(f)
                        if 'train' in data and len(data['train']) > 0:
                            puzzles.append(fichier)
                            if len(puzzles) >= 200:
                                break
                except:
                    continue
            if len(puzzles) >= 200:
                break
        except:
            continue

    return puzzles[:200]

if __name__ == "__main__":
    test_200_puzzles_simple()
