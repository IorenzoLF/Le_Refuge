#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPLORATION COMPLÈTE DES DONNÉES ARC-AGI TRAINING
"""

import json
import random
from pathlib import Path
from collections import Counter, defaultdict

def exploration_complete():
    """Exploration systématique de toutes les tâches de training"""

    print("🏛️ EXPLORATION COMPLÈTE ARC-AGI TRAINING 🏛️")
    print("=" * 60)

    training_path = Path('data/training')
    taches = list(training_path.glob('*.json'))

    print(f"Total de tâches disponibles: {len(taches)}")
    print(f"Échantillon à analyser: 500 tâches (50%)")

    # Échantillon représentatif de 500 tâches
    echantillon = random.sample(taches, min(500, len(taches)))

    # Statistiques globales
    stats = {
        'dimensions': {'meme': 0, 'aggrandissement': 0, 'reduction': 0},
        'patterns': defaultdict(int),
        'valeurs_uniques': Counter(),
        'complexite_patterns': defaultdict(int)
    }

    print(f"\n🔍 Analyse de {len(echantillon)} tâches...")

    for i, tache_path in enumerate(echantillon):
        if i % 50 == 0:
            print(f"  Progression: {i}/{len(echantillon)} tâches analysées")

        with open(tache_path, 'r') as f:
            data = json.load(f)

        if not data['train']:
            continue

        # Analyse du premier exemple
        exemple = data['train'][0]
        input_grid = exemple['input']
        output_grid = exemple['output']

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        # Classification dimensions
        if h_out > h_in or w_out > w_in:
            stats['dimensions']['aggrandissement'] += 1
        elif h_out < h_in or w_out < w_in:
            stats['dimensions']['reduction'] += 1
        else:
            stats['dimensions']['meme'] += 1

        # Analyse des valeurs
        valeurs_in = set()
        valeurs_out = set()
        for row in input_grid:
            valeurs_in.update(row)
        for row in output_grid:
            valeurs_out.update(row)

        stats['valeurs_uniques'][len(valeurs_in)] += 1

        # Détection de patterns simples
        if h_in == h_out and w_in == w_out:
            if len(valeurs_out) < len(valeurs_in):
                stats['patterns']['filtrage_couleur'] += 1
            elif valeurs_in != valeurs_out:
                stats['patterns']['transformation_couleur'] += 1
            else:
                stats['patterns']['symetrie_repetition'] += 1
        else:
            if h_out > h_in or w_out > w_in:
                stats['patterns']['agrandissement'] += 1
            else:
                stats['patterns']['reduction'] += 1

        # Complexité basée sur le nombre de patterns potentiels
        complexite = 0
        if h_in != h_out or w_in != w_out: complexite += 1
        if valeurs_in != valeurs_out: complexite += 1
        if len(valeurs_in) != len(valeurs_out): complexite += 1

        stats['complexite_patterns'][min(complexite, 3)] += 1

    # Résultats
    print(f"\n📊 RÉSULTATS DE L'EXPLORATION COMPLÈTE")
    print("=" * 60)

    print(f"\n🏗️ STATISTIQUES DIMENSIONS:")
    total = sum(stats['dimensions'].values())
    for dim_type, count in stats['dimensions'].items():
        print(f"  {dim_type.capitalize()}: {count} ({count/total*100:.1f}%)")

    print(f"\n🎨 DISTRIBUTION DES PATTERNS:")
    total_patterns = sum(stats['patterns'].values())
    for pattern, count in sorted(stats['patterns'].items()):
        print(f"  {pattern}: {count} ({count/total_patterns*100:.1f}%)")

    print(f"\n🔢 DISTRIBUTION VALEURS UNIQUES:")
    for nb_valeurs, count in sorted(stats['valeurs_uniques'].items()):
        print(f"  {nb_valeurs} valeurs: {count} tâches")

    print(f"\n🌟 COMPLEXITÉ DES PATTERNS:")
    total_complex = sum(stats['complexite_patterns'].values())
    for complexite, count in sorted(stats['complexite_patterns'].items()):
        print(f"  Complexité {complexite}: {count} ({count/total_complex*100:.1f}%)")

    # Analyse approfondie
    print(f"\n🔬 ANALYSE APPROFONDIE:")
    print(f"  - {stats['dimensions']['meme']/total*100:.1f}% gardent dimensions (focus transformation)")
    print(f"  - {stats['patterns']['filtrage_couleur']/total_patterns*100:.1f}% filtrage couleur (opportunité)")
    print(f"  - Complexité moyenne: {sum(k*v for k,v in stats['complexite_patterns'].items())/total_complex:.2f}")

    # Recommandations
    print(f"\n💡 RECOMMANDATIONS:")
    print(f"  1. Focus sur filtrage couleur: {stats['patterns']['filtrage_couleur']} tâches")
    print(f"  2. Améliorer réduction: {stats['patterns']['reduction']} tâches")
    print(f"  3. Explorer patterns complexes: {stats['complexite_patterns'][3]} tâches niveau max")

    print(f"\n🏛️ CONCLUSION:")
    print(f"  Données de training riches et variées")
    print(f"  {len(echantillon)} tâches analysées - base solide pour l'amélioration")
    print(f"  Potentiel d'amélioration identifié dans les patterns subtils")

if __name__ == "__main__":
    exploration_complete()
