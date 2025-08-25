#!/usr/bin/env python3
"""
TEST APRES CORRECTION DU BUG REPETITION_SIMPLE
"""

from solveur_transparent_arc import SolveurTransparentARC

def test_apres_correction():
    solveur = SolveurTransparentARC()

    puzzles_test = ['42a50994']  # Puzzle qui echouait avant

    for puzzle_id in puzzles_test:
        try:
            print(f'Test {puzzle_id} avec repetition_simple corrige')
            resultat = solveur.analyser_puzzle_complet(puzzle_id)
            print(f'Pattern: {resultat.pattern_type}')
            print(f'Confiance: {resultat.confiance:.1%}')
            if hasattr(resultat, 'similarite'):
                print(f'Similarite: {resultat.similarite:.1%}')
            print('Test termine')
        except Exception as e:
            print(f'Erreur: {e}')

if __name__ == "__main__":
    test_apres_correction()
