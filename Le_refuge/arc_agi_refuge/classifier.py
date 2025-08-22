#!/usr/bin/env python3
"""
CLASSIFICATEUR AUTOMATIQUE DES PUZZLES ARC-AGI
Analyse et classification automatique des 1000 puzzles
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Tuple, Set
from collections import Counter

def analyser_puzzle_basique(puzzle_id: str, data: Dict) -> Dict[str, Any]:
    """Analyse basique d'un puzzle"""

    # Dimensions
    input_grid = data['train'][0]['input']
    output_grid = data['train'][0]['output']

    taille_input = (len(input_grid), len(input_grid[0]))
    taille_output = (len(output_grid), len(output_grid[0]))
    ratio_taille = (taille_output[0] * taille_output[1]) / (taille_input[0] * taille_input[1])

    # Couleurs
    couleurs_input = set()
    for ligne in input_grid:
        couleurs_input.update(ligne)

    couleurs_output = set()
    for ligne in output_grid:
        couleurs_output.update(ligne)

    # Modifications
    nombre_pixels_modifies = 0
    for i in range(min(len(input_grid), len(output_grid))):
        for j in range(min(len(input_grid[0]), len(output_grid[0]))):
            if input_grid[i][j] != output_grid[i][j]:
                nombre_pixels_modifies += 1

    total_pixels = taille_input[0] * taille_input[1]
    pourcentage_modification = nombre_pixels_modifies / total_pixels

    # Classification simple
    if ratio_taille > 3.0:
        categorie = "repetition"  # Expansion importante = répétition
    elif len(couleurs_output - couleurs_input) > 0:
        categorie = "couleur"  # Couleurs ajoutées
    elif pourcentage_modification > 0.5:
        categorie = "geometrie"  # Beaucoup de modifications = formes géométriques
    elif len(couleurs_input) <= 3 and pourcentage_modification < 0.3:
        categorie = "logique"  # Peu de couleurs, peu de modifications = logique
    else:
        categorie = "special"  # Cas particulier

    return {
        'id': puzzle_id,
        'categorie': categorie,
        'taille_input': taille_input,
        'taille_output': taille_output,
        'ratio_taille': ratio_taille,
        'couleurs_input': len(couleurs_input),
        'couleurs_output': len(couleurs_output),
        'pourcentage_modification': pourcentage_modification
    }

def main():
    """Analyse des puzzles"""
    training_dir = Path('../../ARC-AGI-2-main/data/training')

    resultats = {
        'total_puzzles': 0,
        'categories': Counter(),
        'tailles': Counter()
    }

    # Analyse d'un échantillon
    json_files = list(training_dir.glob('*.json'))[:100]

    print("=== CLASSIFICATION AUTOMATIQUE ===")
    print(f"Analyse de {len(json_files)} puzzles...")

    for i, json_file in enumerate(json_files, 1):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)

            # Analyse du puzzle
            analyse = analyser_puzzle_basique(json_file.stem, data)

            resultats['total_puzzles'] += 1
            resultats['categories'][analyse['categorie']] += 1
            resultats['tailles'][analyse['taille_input']] += 1

            if i % 20 == 0:
                print(f"Progression: {i}/{len(json_files)}")

        except Exception as e:
            print(f"Erreur avec {json_file.stem}: {e}")

    # Résultats
    print(f"\n=== RESULTATS ===")
    print(f"Total analysé: {resultats['total_puzzles']}")

    print(f"\nRépartition par catégories:")
    for categorie, count in resultats['categories'].most_common():
        pourcentage = (count / resultats['total_puzzles']) * 100
        print(f"  {categorie}: {count} ({pourcentage:.1f}%)")

    print(f"\nTailles d'input les plus fréquentes:")
    for taille, count in resultats['tailles'].most_common()[:5]:
        pourcentage = (count / resultats['total_puzzles']) * 100
        print(f"  {taille}: {count} ({pourcentage:.1f}%)")

if __name__ == "__main__":
    main()
