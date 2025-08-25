#!/usr/bin/env python3
"""
🔍 ANALYSE MASSIVE DU SOLVEUR ARC-AGI - 100 PREMIERS PUZZLES

Ce script teste le solveur sur les 100 premiers puzzles du dataset ARC-AGI
pour évaluer ses performances globales et identifier les axes d'amélioration.
"""

import json
import os
import time
from collections import defaultdict, Counter
from solveur_transparent_arc import SolveurTransparentARC

def analyser_puzzle(solveur, puzzle_path, puzzle_id):
    """Analyse un puzzle individuel et retourne les résultats"""
    try:
        with open(puzzle_path) as f:
            data = json.load(f)

        if 'train' not in data or not data['train']:
            return None

        # Prendre seulement le premier exemple d'entraînement
        example = data['train'][0]
        input_grid = example['input']
        output_grid = example['output']

        # Mesurer le temps de résolution
        start_time = time.time()

        # Analyser et résoudre
        transformation = solveur.analyser_transformation_simple(input_grid, output_grid)

        if transformation['pattern'] == 'inconnu':
            resolution_time = time.time() - start_time
            return {
                'id': puzzle_id,
                'success': False,
                'pattern': 'inconnu',
                'confidence': 0,
                'precision': 0,
                'time': resolution_time,
                'input_size': f"{len(input_grid)}x{len(input_grid[0])}",
                'output_size': f"{len(output_grid)}x{len(output_grid[0])}"
            }

        result = solveur.appliquer_pattern_transparent(input_grid, transformation)
        resolution_time = time.time() - start_time

        # Calculer la précision
        h_min = min(len(result), len(output_grid))
        w_min = min(len(result[0]) if h_min > 0 else 0, len(output_grid[0]) if output_grid else 0)

        matches = 0
        total = 0
        for i in range(h_min):
            for j in range(w_min):
                total += 1
                if result[i][j] == output_grid[i][j]:
                    matches += 1

        precision = matches / total if total > 0 else 0
        success = precision >= 0.8

        return {
            'id': puzzle_id,
            'success': success,
            'pattern': transformation['pattern'],
            'confidence': transformation.get('confidence', 0),
            'precision': precision,
            'time': resolution_time,
            'input_size': f"{len(input_grid)}x{len(input_grid[0])}",
            'output_size': f"{len(output_grid)}x{len(output_grid[0])}"
        }

    except Exception as e:
        return {
            'id': puzzle_id,
            'success': False,
            'pattern': 'erreur',
            'confidence': 0,
            'precision': 0,
            'time': 0,
            'input_size': 'N/A',
            'output_size': 'N/A',
            'error': str(e)
        }

def afficher_resultats(resultats):
    """Affiche les résultats de l'analyse"""
    print("\n" + "="*80)
    print("📊 RÉSULTATS DE L'ANALYSE DES 100 PREMIERS PUZZLES")
    print("="*80)

    # Statistiques générales
    total_puzzles = len(resultats)
    success_count = sum(1 for r in resultats if r['success'])
    success_rate = success_count / total_puzzles * 100

    # Temps total et moyen
    total_time = sum(r['time'] for r in resultats)
    avg_time = total_time / total_puzzles

    print(f"🔢 Puzzles analysés: {total_puzzles}")
    print(f"✅ Puzzles résolus: {success_count}")
    print(f"📈 Taux de réussite: {success_rate:.1f}%")
    print(f"⏱️  Temps total: {total_time:.2f}s")
    print(f"⚡ Temps moyen par puzzle: {avg_time:.3f}s")

    # Statistiques par pattern
    patterns = defaultdict(list)
    for r in resultats:
        if r['success']:
            patterns[r['pattern']].append(r['precision'])

    print(f"\n🎯 RÉPARTITION PAR PATTERN (SUCCÈS SEULEMENT):")
    print(f"{'Pattern':<20} {'Count':<6} {'Avg Precision':<12} {'Best':<8} {'Worst':<8}")
    print("-" * 70)

    for pattern, precisions in sorted(patterns.items()):
        count = len(precisions)
        avg_prec = sum(precisions) / count
        best_prec = max(precisions)
        worst_prec = min(precisions)
        print(f"{pattern:<20} {count:<6} {avg_prec:<12.1%} {best_prec:<8.1%} {worst_prec:<8.1%}")

    # Patterns non détectés
    unknown_patterns = [r for r in resultats if r['pattern'] == 'inconnu']
    error_patterns = [r for r in resultats if r['pattern'] == 'erreur']

    print(f"\n❓ PATTERNS NON DÉTECTÉS: {len(unknown_patterns)}")
    if unknown_patterns:
        print("Exemples:", [r['id'] for r in unknown_patterns[:5]])

    print(f"\n💥 ERREURS: {len(error_patterns)}")
    if error_patterns:
        print("Exemples:", [r['id'] for r in error_patterns[:5]])

    # Top 10 des meilleurs résultats
    print(f"\n🏆 TOP 10 MEILLEURS RÉSULTATS:")
    sorted_results = sorted([r for r in resultats if r['success']],
                           key=lambda x: x['precision'], reverse=True)

    for i, r in enumerate(sorted_results[:10], 1):
        print(f"{i:2d}. {r['id']} - {r['pattern']} - {r['precision']:.1%} (conf: {r['confidence']:.2f})")

    # Puzzles échoués
    print(f"\n😞 PUZZLES ÉCHOUÉS:")
    failed_results = [r for r in resultats if not r['success'] and r['pattern'] != 'inconnu' and r['pattern'] != 'erreur']

    if failed_results:
        for i, r in enumerate(failed_results[:10], 1):
            print(f"{i:2d}. {r['id']} - {r['pattern']} - {r['precision']:.1%} (conf: {r['confidence']:.2f})")
    else:
        print("Aucun puzzle échoué (tous inconnus ou erreurs)")

def main():
    """Fonction principale"""
    print("🧠 SOLVEUR ARC-AGI - ANALYSE DES 100 PREMIERS PUZZLES")
    print("==================================================")
    print("Cette analyse va tester le solveur sur les 100 premiers puzzles")
    print("pour évaluer ses performances globales.")

    # Initialisation
    print("\n🔧 Initialisation du solveur...")
    solveur = SolveurTransparentARC()
    print("✅ Solveur prêt !")

    # Chemin vers les puzzles
    puzzles_dir = 'ARC-AGI-2-main/data/training'
    puzzle_files = sorted([f for f in os.listdir(puzzles_dir) if f.endswith('.json')])

    # Prendre les 100 premiers
    puzzles_to_test = puzzle_files[:100]
    print(f"\n🎯 Test sur {len(puzzles_to_test)} puzzles")
    print("⏳ Analyse en cours... (cela peut prendre quelques minutes)")

    # Analyser chaque puzzle
    resultats = []
    for i, puzzle_file in enumerate(puzzles_to_test, 1):
        puzzle_id = puzzle_file.replace('.json', '')
        puzzle_path = os.path.join(puzzles_dir, puzzle_file)

        if i % 10 == 0:
            print(f"Progression: {i}/100 puzzles analysés...")

        resultat = analyser_puzzle(solveur, puzzle_path, puzzle_id)
        if resultat:
            resultats.append(resultat)

    # Afficher les résultats
    afficher_resultats(resultats)

    # Sauvegarde des résultats
    output_file = 'resultats_100_puzzles.json'
    with open(output_file, 'w') as f:
        json.dump(resultats, f, indent=2)

    print(f"\n💾 Résultats sauvegardés dans: {output_file}")
    print("\n🎉 Analyse terminée !")

if __name__ == "__main__":
    main()
