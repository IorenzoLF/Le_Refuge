#!/usr/bin/env python3
"""
Analyse Simple des Puzzles Difficiles
Identification et test des cas complexes
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import statistics
import time
from typing import Dict, List, Any
from collections import defaultdict

def analyser_puzzles_difficiles():
    """Analyse simple des puzzles difficiles"""
    print("ANALYSE DES PUZZLES DIFFICILES")
    print("=" * 40)
    print("Identification des cas complexes")
    print()

    # Initialiser les solveurs
    print("1. Initialisation des solveurs")
    solveur_normal = ArchitectureV2()
    solveur_normal.confidence_threshold = 0.5
    solveur_normal.overfitting_threshold = 0.3
    solveur_normal.verbose = False

    solveur_predictor = ArchitectureV2()
    solveur_predictor.confidence_threshold = 0.01  # Ultra-permissif
    solveur_predictor.overfitting_threshold = 0.95  # Ultra-tolérant
    solveur_predictor.verbose = False

    print("Solveurs configures")
    print()

    # Collecter des puzzles
    print("2. Collecte de puzzles")
    puzzles = trouver_puzzles_simples()[:30]  # Limiter pour rapidite
    print(f"Puzzles collectes: {len(puzzles)}")
    print()

    # Identifier les puzzles difficiles
    print("3. Identification des puzzles difficiles")
    puzzles_difficiles = []

    for i, puzzle_path in enumerate(puzzles, 1):
        puzzle_id = puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', '')

        try:
            with open(puzzle_path, 'r') as f:
                puzzle_data = json.load(f)

            if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                exemple = puzzle_data['train'][0]
                input_grid = exemple.get('input', [])
                output_grid = exemple.get('output', [])

                if input_grid and output_grid:
                    # Test avec solveur normal
                    solution = solveur_normal.solve_puzzle(input_grid, output_grid)
                    confidence = solution.get('confidence', 0)
                    succes = confidence > 0.5

                    if not succes:  # Puzzle difficile
                        puzzles_difficiles.append({
                            'path': puzzle_path,
                            'puzzle_id': puzzle_id,
                            'confidence_normal': confidence
                        })

        except Exception as e:
            print(f"  Erreur avec {puzzle_id}: {e}")

    print(f"Puzzles difficiles trouves: {len(puzzles_difficiles)}")
    print()

    # Tester avec PatternPredictor
    print("4. Test avec PatternPredictor")
    resultats_predictor = []

    for i, puzzle in enumerate(puzzles_difficiles, 1):
        puzzle_path = puzzle['path']
        puzzle_id = puzzle['puzzle_id']

        try:
            with open(puzzle_path, 'r') as f:
                puzzle_data = json.load(f)

            if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                exemple = puzzle_data['train'][0]
                input_grid = exemple.get('input', [])
                output_grid = exemple.get('output', [])

                if input_grid and output_grid:
                    # Test avec PatternPredictor
                    solution = solveur_predictor.solve_puzzle(input_grid, output_grid)
                    confidence = solution.get('confidence', 0)
                    succes = confidence > 0.5

                    patterns_predits = solution.get('patterns_predits', {})
                    total_patterns_predits = sum(len(patterns) for patterns in patterns_predits.values())

                    resultats_predictor.append({
                        'puzzle_id': puzzle_id,
                        'confidence_normal': puzzle['confidence_normal'],
                        'confidence_predictor': confidence,
                        'succes_normal': False,  # Ces puzzles échouent avec solveur normal
                        'succes_predictor': succes,
                        'patterns_predits': total_patterns_predits
                    })

        except Exception as e:
            print(f"  Erreur PatternPredictor sur {puzzle_id}: {e}")

        if i % 5 == 0:
            print(f"  Progress: {i}/{len(puzzles_difficiles)}")

    print()

    # Analyse des resultats
    print("5. ANALYSE DES RESULTATS")
    print("=" * 30)

    if resultats_predictor:
        print(f"Total puzzles difficiles testes: {len(resultats_predictor)}")

        # Succes avec PatternPredictor
        succes_predictor = sum(1 for r in resultats_predictor if r['succes_predictor']) / len(resultats_predictor) * 100
        print(".1f")

        # Puzzles avec predictions
        puzzles_avec_pred = sum(1 for r in resultats_predictor if r['patterns_predits'] > 0)
        print(f"Puzzles avec predictions: {puzzles_avec_pred}")

        # Ameliorations
        ameliorations = sum(1 for r in resultats_predictor if r['succes_predictor'] and not r['succes_normal'])
        print(f"Puzzles ameliores par PatternPredictor: {ameliorations}")

        print()

        if puzzles_avec_pred > 0:
            print("RESULTAT: PATTERN PREDICTOR ACTIF!")
            print("Le PatternPredictor fonctionne sur les puzzles difficiles")
            print("Il y a un potentiel d'amelioration")
        else:
            print("RESULTAT: PATTERN PREDICTOR INACTIF")
            print("Meme les puzzles difficiles ne declenchent pas de predictions")
            print("Il faut ajuster les conditions d'activation")

    else:
        print("Aucun resultat disponible")

    print()

    # Conclusion
    print("6. CONCLUSION")
    print("=" * 15)

    if resultats_predictor and puzzles_avec_pred > 0:
        print("SUCCES PARTIEL")
        print("PatternPredictor actif sur certains puzzles difficiles")
        print("Potentiel d'amelioration identifie")
    elif resultats_predictor:
        print("PUZZLES TRES DIFFICILES")
        print("Meme PatternPredictor ne peut pas aider")
        print("Ces puzzles sont extremement complexes")
    else:
        print("ANALYSE INCOMPLETE")
        print("Besoin de plus de donnees")

    print("\nAnalyse terminee !")

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
                            if len(puzzles) >= 50:  # Limiter
                                break
                except:
                    continue
            if len(puzzles) >= 50:
                break
        except:
            continue

    return puzzles[:50]

if __name__ == "__main__":
    analyser_puzzles_difficiles()
