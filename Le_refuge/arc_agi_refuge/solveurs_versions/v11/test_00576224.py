#!/usr/bin/env python3
"""
Test du solveur sur le puzzle 00576224
"""

import json
import sys
sys.path.insert(0, '.')

from solveur_arc_zones_v11 import SolveurZonesV11, TacheARC

def main():
    # Charger le puzzle
    with open('../../ARC-AGI-2-main/data/training/00576224.json', 'r') as f:
        data = json.load(f)

    tache = TacheARC('00576224', data['train'], data['test'])
    solveur = SolveurZonesV11()

    print('=== TEST SOLVEUR COMPLET SUR 00576224 ===')

    # Resoudre avec le solveur complet
    resultat = solveur.resoudre_tache(tache)

    print('RESULTAT FINAL:')
    print('Methode choisie:', resultat['methode'])
    print('Confiance:', resultat['confiance'])

    print('\nInput 2x2:')
    for ligne in tache.test[0]['input']:
        print('  ' + ' '.join(str(x) for x in ligne))

    print('\nOutput 6x6 genere:')
    for ligne in resultat['solution']:
        print('  ' + ' '.join(str(x) for x in ligne))

    # Verifier si c'est correct
    output_attendu = tache.test[0]['output']
    correct = resultat['solution'] == output_attendu

    print(f'\nRESULTAT: {"CORRECT" if correct else "INCORRECT"}')
    print(f'Confiance finale: {resultat["confiance"]:.2f}')

    if not correct:
        print('\nAnalyse de l erreur:')
        print(f'Methode utilisee: {resultat["methode"]}')
        if resultat['methode'] == 'tiling_repetitif':
            print('Le solveur a choisi l approche de tiling !')
        else:
            print('Le solveur n a pas choisi l approche de tiling')

        print('\nComparaison attendue:')
        print('Attendu:')
        for ligne in output_attendu:
            print('  ' + ' '.join(str(x) for x in ligne))

    else:
        print('\nSUCCES TOTAL ! Le puzzle est resolu !')

if __name__ == "__main__":
    main()
