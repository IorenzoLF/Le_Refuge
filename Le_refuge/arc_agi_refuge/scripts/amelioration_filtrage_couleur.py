#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMÉLIORATION DU FILTRAGE COULEUR
Priorité #1 : 53 tâches identifiées (10.6%)
"""

import json
from pathlib import Path
from collections import defaultdict
import numpy as np

def analyser_filtrage_couleur():
    """Analyse approfondie du filtrage couleur"""

    print("🎯 AMÉLIORATION FILTRAGE COULEUR")
    print("=" * 50)

    # Chercher des exemples de filtrage couleur
    training_path = Path('data/training')
    exemples_filtrage = []

    # Analyser quelques tâches pour comprendre les patterns
    for tache_path in list(training_path.glob('*.json'))[:200]:  # Échantillon
        with open(tache_path, 'r') as f:
            data = json.load(f)

        if not data['train']:
            continue

        exemple = data['train'][0]
        input_grid = exemple['input']
        output_grid = exemple['output']

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        # Même dimensions = potentiel filtrage
        if h_in == h_out and w_in == w_out:
            valeurs_in = set()
            valeurs_out = set()
            for row in input_grid:
                valeurs_in.update(row)
            for row in output_grid:
                valeurs_out.update(row)

            # Filtrage détecté
            if len(valeurs_out) < len(valeurs_in):
                couleurs_supprimees = valeurs_in - valeurs_out
                couleurs_conservees = valeurs_in & valeurs_out

                exemples_filtrage.append({
                    'tache_id': tache_path.stem,
                    'valeurs_in': sorted(valeurs_in),
                    'valeurs_out': sorted(valeurs_out),
                    'supprimees': sorted(couleurs_supprimees),
                    'conservees': sorted(couleurs_conservees)
                })

    print(f"📊 {len(exemples_filtrage)} EXEMPLES DE FILTRAGE COULEUR TROUVÉS")

    # Analyser les patterns de suppression
    patterns_suppression = defaultdict(int)

    for exemple in exemples_filtrage[:20]:  # Analyser 20 exemples
        print(f"\n🧪 {exemple['tache_id']}:")
        print(f"   Input: {exemple['valeurs_in']}")
        print(f"   Output: {exemple['valeurs_out']}")
        print(f"   Supprimé: {exemple['supprimees']}")
        print(f"   Conservé: {exemple['conservees']}")

        # Patterns communs
        if 0 in exemple['supprimees']:
            patterns_suppression['suppression_zero'] += 1
        if len(exemple['supprimees']) == 1:
            patterns_suppression['une_seule_couleur'] += 1
        if max(exemple['supprimees']) == max(exemple['valeurs_in']):
            patterns_suppression['valeur_max'] += 1
        if min(exemple['supprimees']) == min(exemple['valeurs_in']):
            patterns_suppression['valeur_min'] += 1

    print(f"\n🎨 PATTERNS DE SUPPRESSION IDENTIFIÉS:")
    for pattern, count in patterns_suppression.items():
        print(f"   {pattern}: {count} occurrences")

    # Propositions d'amélioration
    print(f"\n💡 PROPOSITIONS D'AMÉLIORATION:")
    print("1. Ajouter détection suppression valeur 0 (pattern le plus commun)")
    print("2. Implémenter filtrage par valeur maximale/minimale")
    print("3. Améliorer la confiance pour les suppressions uniques")
    print("4. Ajouter analyse contextuelle des couleurs supprimées")

    return exemples_filtrage

def implementer_ameliorations_filtrage(exemples):
    """Implémenter les améliorations basées sur l'analyse"""

    print(f"\n🔧 IMPLEMENTATION DES AMÉLIORATIONS")

    # Analyse des fréquences de suppression
    suppression_zero = sum(1 for ex in exemples if 0 in ex['supprimees'])
    suppression_unique = sum(1 for ex in exemples if len(ex['supprimees']) == 1)

    print(f"   Suppression de 0: {suppression_zero}/{len(exemples)} exemples")
    print(f"   Suppression unique: {suppression_unique}/{len(exemples)} exemples")

    # Recommandations concrètes
    print(f"\n📈 PLAN D'ACTION:")
    print("1. Modifier _detecter_filtrage_couleur() pour prioriser suppression de 0")
    print("2. Ajouter bonus de confiance pour suppressions uniques")
    print("3. Implémenter détection valeur max/min supprimée")
    print("4. Tester sur les 53 tâches identifiées")

if __name__ == "__main__":
    exemples = analyser_filtrage_couleur()
    implementer_ameliorations_filtrage(exemples)
