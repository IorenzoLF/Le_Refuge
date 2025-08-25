#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALYSE DES 14 TÂCHES COMPLEXES IDENTIFIÉES
"""

import json
from pathlib import Path
from collections import defaultdict
import numpy as np

def analyser_taches_complexes():
    """Analyse approfondie des 14 tâches complexes"""

    print("🔬 **ANALYSE DES 14 TÂCHES COMPLEXES** 🔬")
    print("=" * 60)

    # Les 14 tâches complexes identifiées
    taches_complexes = [
        '22425bda', 'aee291af', 'b94a9452', '1fad071e', '695367ec',
        'bd14c3bf', 'ac6f9922', '8a6d367c', 'ff805c23', 'b7999b51',
        '5d2a5c43', 'b0f4d537', 'de493100', '9f236235'
    ]

    training_path = Path('data/training')
    analyses_detaillees = []

    for tache_id in taches_complexes:
        tache_path = training_path / f"{tache_id}.json"

        if not tache_path.exists():
            print(f"❌ Tâche {tache_id} non trouvée")
            continue

        try:
            with open(tache_path, 'r') as f:
                data = json.load(f)

            if not data['train']:
                continue

            print(f"\n🧪 **ANALYSE DE {tache_id}**")

            # Analyser tous les exemples
            for i, exemple in enumerate(data['train']):
                input_grid = exemple['input']
                output_grid = exemple['output']

                h_in, w_in = len(input_grid), len(input_grid[0])
                h_out, w_out = len(output_grid), len(output_grid[0])

                print(f"  Exemple {i+1}: {h_in}x{w_in} → {h_out}x{w_out}")

                # Analyse des valeurs
                valeurs_in = set()
                for row in input_grid:
                    valeurs_in.update(row)
                valeurs_out = set()
                for row in output_grid:
                    valeurs_out.update(row)

                print(f"    Input: {sorted(valeurs_in)}")
                print(f"    Output: {sorted(valeurs_out)}")

                # Détecter les changements
                changements = 0
                if h_in == h_out and w_in == w_out:
                    for x in range(h_in):
                        for y in range(w_in):
                            if input_grid[x][y] != output_grid[x][y]:
                                changements += 1

                    ratio_changement = changements / (h_in * w_in)
                    print(f"    Changements: {changements}/{h_in*w_in} ({ratio_changement:.1%})")

                    # Identifier le type de transformation
                    if len(valeurs_out) < len(valeurs_in):
                        print(f"    → FILTRAGE COULEUR (suppression de {len(valeurs_in)-len(valeurs_out)} valeurs)")
                    elif valeurs_in != valeurs_out:
                        print(f"    → TRANSFORMATION COULEUR")
                    else:
                        print(f"    → TRANSFORMATION SPATIALE (même valeurs)")
                else:
                    print(f"    → CHANGEMENT DE DIMENSIONS")

            # Stocker l'analyse
            analyses_detaillees.append({
                'tache_id': tache_id,
                'nb_exemples': len(data['train']),
                'complexite': calculer_complexite_tache(data['train'][0]['input'], data['train'][0]['output'])
            })

        except Exception as e:
            print(f"  ❌ Erreur: {e}")

    print(f"\n📊 **SYNTHÈSE DES 14 TÂCHES COMPLEXES**")
    print("=" * 60)

    # Statistiques
    total_exemples = sum(analyse['nb_exemples'] for analyse in analyses_detaillees)
    complexites = [analyse['complexite'] for analyse in analyses_detaillees]

    print(f"Nombre de tâches analysées: {len(analyses_detaillees)}")
    print(f"Total d'exemples: {total_exemples}")
    print(f"Complexité moyenne: {np.mean(complexites):.2f}")
    print(f"Complexité max: {max(complexites):.2f}")
    print(f"Complexité min: {min(complexites):.2f}")

    # Classification des patterns
    patterns_identifies = defaultdict(int)

    for tache_id in taches_complexes:
        tache_path = training_path / f"{tache_id}.json"
        if not tache_path.exists():
            continue

        try:
            with open(tache_path, 'r') as f:
                data = json.load(f)

            if data['train']:
                exemple = data['train'][0]
                input_grid = exemple['input']
                output_grid = exemple['output']

                h_in, w_in = len(input_grid), len(input_grid[0])
                h_out, w_out = len(output_grid), len(output_grid[0])

                valeurs_in = set()
                for row in input_grid:
                    valeurs_in.update(row)
                valeurs_out = set()
                for row in output_grid:
                    valeurs_out.update(row)

                # Classification
                if h_in == h_out and w_in == w_out:
                    if len(valeurs_out) < len(valeurs_in):
                        patterns_identifies['filtrage_couleur'] += 1
                    elif valeurs_in != valeurs_out:
                        patterns_identifies['transformation_couleur'] += 1
                    else:
                        patterns_identifies['transformation_spatiale'] += 1
                else:
                    if h_out < h_in or w_out < w_in:
                        patterns_identifies['reduction'] += 1
                    else:
                        patterns_identifies['agrandissement'] += 1
        except:
            continue

    print(f"\n🎯 PATTERNS DANS LES TÂCHES COMPLEXES:")
    for pattern, count in patterns_identifies.items():
        print(f"  {pattern}: {count} tâches ({count/len(taches_complexes)*100:.1f}%)")

    # Recommandations
    print(f"\n💡 **RECOMMANDATIONS POUR PHASE 2**")
    print(f"  1. **Filtrage couleur complexe**: {patterns_identifies['filtrage_couleur']} tâches")
    print(f"  2. **Transformations spatiales**: {patterns_identifies.get('transformation_spatiale', 0)} tâches")
    print(f"  3. **Réductions avancées**: {patterns_identifies['reduction']} tâches")
    print(f"  4. Focus sur les patterns composites (multi-types)")

    print(f"\n🏛️ **CONCLUSION**")
    print(f"  Ces 14 tâches complexes sont les clés pour atteindre 100%")
    print(f"  Elles nécessitent des détecteurs plus sophistiqués")
    print(f"  Priorité: améliorer les patterns existants plutôt qu'en créer de nouveaux")

    print(f"\n✨ Phase 1 terminée - Phase 2 peut commencer ! ✨")

def calculer_complexite_tache(input_grid, output_grid):
    """Calcule la complexité d'une tâche"""

    h_in, w_in = len(input_grid), len(input_grid[0])
    h_out, w_out = len(output_grid), len(output_grid[0])

    complexite = 0

    # Changement de dimensions
    if h_in != h_out or w_in != w_out:
        complexite += 1

    # Changement de valeurs
    valeurs_in = set()
    for row in input_grid:
        valeurs_in.update(row)
    valeurs_out = set()
    for row in output_grid:
        valeurs_out.update(row)

    if len(valeurs_in) != len(valeurs_out):
        complexite += 1

    # Ratio de changement
    changements = 0
    if h_in == h_out and w_in == w_out:
        for i in range(h_in):
            for j in range(w_in):
                if input_grid[i][j] != output_grid[i][j]:
                    changements += 1
        ratio_changement = changements / (h_in * w_in)
        complexite += ratio_changement

    # Diversité des valeurs
    if len(valeurs_in) > 5:
        complexite += 0.5

    return complexite

if __name__ == "__main__":
    analyser_taches_complexes()
