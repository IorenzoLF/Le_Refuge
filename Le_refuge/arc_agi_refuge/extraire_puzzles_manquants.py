#!/usr/bin/env python3
"""
Extraire les vrais puzzles non couverts
"""

import json

def extraire_puzzles_manquants():
    """Extraire les puzzles avec 0% de similarite"""

    # Charger les resultats
    try:
        with open('resultats_test_1000.json', 'r') as f:
            resultats = json.load(f)
    except FileNotFoundError:
        print("Fichier resultats_test_1000.json non trouve")
        return []

    # Extraire les puzzles non couverts
    puzzles_manquants = []
    if 'erreurs_detaillees' in resultats:
        for erreur in resultats['erreurs_detaillees']:
            if isinstance(erreur, dict) and erreur.get('similarite_globale', 0) == 0.0:
                puzzles_manquants.append(erreur.get('puzzle_id', 'inconnu'))
    else:
        # Fallback: chercher dans tous les éléments
        for key, value in resultats.items():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict) and item.get('similarite_globale', 0) == 0.0:
                        puzzles_manquants.append(item.get('puzzle_id', 'inconnu'))

    print(f'{len(puzzles_manquants)} puzzles non couverts identifies')

    # Afficher par groupes de 10
    for i in range(0, len(puzzles_manquants), 10):
        groupe = puzzles_manquants[i:i+10]
        print(f'\nGROUPE {i//10 + 1}:')
        for j, puzzle_id in enumerate(groupe, 1):
            print(f'  {j:2d}. {puzzle_id}')

    # Sauvegarder la vraie liste
    with open('puzzles_manquants_verite.json', 'w') as f:
        json.dump(puzzles_manquants, f, indent=2)

    print(f'\nListe sauvegardee: puzzles_manquants_verite.json')

    # Analyser les patterns des puzzles manquants
    analyser_patterns_manquants(puzzles_manquants)

    return puzzles_manquants

def analyser_patterns_manquants(puzzles_manquants):
    """Analyser les patterns des puzzles manquants"""

    print(f'\n=== ANALYSE DES {len(puzzles_manquants)} PUZZLES NON COUVERTS ===')

    # Charger quelques exemples pour comprendre les patterns
    exemples_analyses = []
    for i, puzzle_id in enumerate(puzzles_manquants[:5]):  # Analyser les 5 premiers
        try:
            with open(f'ARC-AGI-2-main/data/training/{puzzle_id}.json', 'r') as f:
                data = json.load(f)

            # Analyser les dimensions et couleurs
            train_examples = data['train']
            input_dims = [(len(ex['input']), len(ex['input'][0]) if ex['input'] else 0) for ex in train_examples]
            output_dims = [(len(ex['output']), len(ex['output'][0]) if ex['output'] else 0) for ex in train_examples]

            # Couleurs utilisées
            couleurs_input = set()
            couleurs_output = set()
            for ex in train_examples:
                couleurs_input.update(cell for row in ex['input'] for cell in row)
                couleurs_output.update(cell for row in ex['output'] for cell in row)

            analyse = {
                'puzzle_id': puzzle_id,
                'nb_examples': len(train_examples),
                'input_dims': input_dims,
                'output_dims': output_dims,
                'couleurs_input': sorted(list(couleurs_input)),
                'couleurs_output': sorted(list(couleurs_output)),
                'changement_dims': any(in_dim != out_dim for in_dim, out_dim in zip(input_dims, output_dims))
            }

            exemples_analyses.append(analyse)

            print(f'\nPuzzle {i+1}: {puzzle_id}')
            print(f'  Exemples: {analyse["nb_examples"]}')
            print(f'  Dimensions: {set(analyse["input_dims"])} -> {set(analyse["output_dims"])}')
            print(f'  Couleurs: {analyse["couleurs_input"]} -> {analyse["couleurs_output"]}')

        except Exception as e:
            print(f'Erreur analyse {puzzle_id}: {e}')

    # Classifier les types de puzzles manquants
    stats = {
        'changement_dimensions': 0,
        'changement_couleurs': 0,
        'complexite_geometrique': 0,
        'patterns_spatiaux': 0,
        'autres': 0
    }

    for analyse in exemples_analyses:
        if analyse['changement_dims']:
            stats['changement_dimensions'] += 1
        elif set(analyse['couleurs_output']) != set(analyse['couleurs_input']):
            stats['changement_couleurs'] += 1
        else:
            stats['autres'] += 1

    print(f'\n=== CLASSIFICATION ===')
    print(f'Changement dimensions: {stats["changement_dimensions"]}')
    print(f'Changement couleurs: {stats["changement_couleurs"]}')
    print(f'Autres: {stats["autres"]}')

    # Recommandations
    print(f'\n=== RECOMMANDATIONS ===')
    print('1. Prioriser les changements de dimensions')
    print('2. Implementer patterns de transformation geometrique')
    print('3. Analyser plus systematiquement les exemples d\'echec')
    print('4. Creer un systeme de detection de patterns complexes')

if __name__ == "__main__":
    extraire_puzzles_manquants()
