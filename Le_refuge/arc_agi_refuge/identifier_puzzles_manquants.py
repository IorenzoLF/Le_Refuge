#!/usr/bin/env python3
"""
Identifier les vrais puzzles non couverts
"""

import json
import os

def identifier_puzzles_manquants():
    """Identifier les puzzles avec 0% de similarite"""

    # Charger les resultats du test 1000 puzzles
    try:
        with open('resultats/resultats_1000_taches_20250820_213902.json', 'r') as f:
            resultats = json.load(f)

        # Extraire les puzzles non couverts (similarite 0%)
        puzzles_manquants = []
        for puzzle_id, resultat in resultats.items():
            if resultat.get('similarite_globale', 0) == 0.0:
                puzzles_manquants.append(puzzle_id)

        print(f'TOTAL: {len(puzzles_manquants)} puzzles non couverts')

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

        return puzzles_manquants

    except FileNotFoundError:
        print('Fichier resultats_test_1000_puzzles.json non trouve')
        return []

if __name__ == "__main__":
    identifier_puzzles_manquants()
