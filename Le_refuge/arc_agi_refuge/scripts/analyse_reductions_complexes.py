#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALYSE DES RÉDUCTIONS COMPLEXES
Phase 2 : Améliorer la détection des 12 tâches complexes de réduction
"""

import json
import numpy as np
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Any, Tuple

def analyser_reductions_complexes():
    """Analyse approfondie des réductions complexes"""

    print("🔬 **ANALYSE DES RÉDUCTIONS COMPLEXES** 🔬")
    print("=" * 60)
    print("Focus : Les 12 tâches complexes (85.7% des cas complexes)")
    print("Objectif : Comprendre les patterns de réduction + filtrage")
    print("=" * 60)

    # Tâches complexes identifiées avec réduction
    taches_reduction = [
        '22425bda', 'aee291af', 'b94a9452', '1fad071e',
        'ac6f9922', '8a6d367c', 'ff805c23', 'b7999b51',
        '5d2a5c43', 'b0f4d537', 'de493100', '9f236235'
    ]

    training_path = Path('data/training')
    analyses_reductions = []

    print(f"\n📊 Analyse des {len(taches_reduction)} tâches de réduction complexes")

    for i, tache_id in enumerate(taches_reduction, 1):
        print(f"\n🧪 **TÂCHE {i}: {tache_id}**")

        tache_path = training_path / f"{tache_id}.json"
        if not tache_path.exists():
            print(f"  ❌ Fichier non trouvé")
            continue

        try:
            with open(tache_path, 'r') as f:
                data = json.load(f)

            if not data['train']:
                continue

            # Analyser chaque exemple
            for j, exemple in enumerate(data['train'][:3]):  # Max 3 exemples
                input_grid = exemple['input']
                output_grid = exemple['output']

                h_in, w_in = len(input_grid), len(input_grid[0])
                h_out, w_out = len(output_grid), len(output_grid[0])

                # Calculer les métriques de réduction
                ratio_h = h_out / h_in if h_in > 0 else 0
                ratio_w = w_out / w_in if w_in > 0 else 0
                ratio_surface = (h_out * w_out) / (h_in * w_in) if (h_in * w_in) > 0 else 0

                # Analyser les valeurs
                valeurs_in = set()
                for row in input_grid:
                    valeurs_in.update(row)
                valeurs_out = set()
                for row in output_grid:
                    valeurs_out.update(row)

                valeurs_filtrees = valeurs_in - valeurs_out
                valeurs_conservees = valeurs_in & valeurs_out

                print(f"  Exemple {j+1}: {h_in}x{w_in} → {h_out}x{w_out}")
                print(f"    Ratios: H={ratio_h:.2f}, W={ratio_w:.2f}, Surface={ratio_surface:.2f}")
                print(f"    Valeurs: {sorted(valeurs_in)} → {sorted(valeurs_out)}")
                print(f"    Filtrées: {sorted(valeurs_filtrees)}")
                print(f"    Conservées: {sorted(valeurs_conservees)}")

                # Classifier le type de réduction
                if valeurs_filtrees:
                    print(f"    → RÉDUCTION AVEC FILTRAGE ({len(valeurs_filtrees)} valeurs supprimées)")
                else:
                    print(f"    → RÉDUCTION SIMPLE (toutes valeurs conservées)")

                # Analyser les patterns spécifiques
                if ratio_surface < 0.1:
                    print(f"    → COMPRESSION EXTRÊME (< 10% de la surface)")
                elif 0 in valeurs_filtrees:
                    print(f"    → SUPPRESSION DE ZÉRO")
                elif max(valeurs_in) in valeurs_filtrees:
                    print(f"    → SUPPRESSION DE VALEUR MAX")
                elif min(valeurs_in) in valeurs_filtrees:
                    print(f"    → SUPPRESSION DE VALEUR MIN")

                analyses_reductions.append({
                    'tache_id': tache_id,
                    'exemple': j,
                    'ratio_h': ratio_h,
                    'ratio_w': ratio_w,
                    'ratio_surface': ratio_surface,
                    'valeurs_filtrees': list(valeurs_filtrees),
                    'nb_valeurs_filtrees': len(valeurs_filtrees),
                    'avec_filtrage': len(valeurs_filtrees) > 0
                })

        except Exception as e:
            print(f"  ❌ Erreur: {e}")

    # Analyse statistique
    print(f"\n📈 **ANALYSE STATISTIQUE**")
    print("=" * 60)

    # Statistiques des ratios
    ratios_surface = [a['ratio_surface'] for a in analyses_reductions]
    print(f"Ratio surface moyen: {np.mean(ratios_surface):.3f}")
    print(f"Ratio surface min: {min(ratios_surface):.3f}")
    print(f"Ratio surface max: {max(ratios_surface):.3f}")

    # Statistiques du filtrage
    avec_filtrage = sum(1 for a in analyses_reductions if a['avec_filtrage'])
    print(f"Exemples avec filtrage: {avec_filtrage}/{len(analyses_reductions)} ({avec_filtrage/len(analyses_reductions)*100:.1f}%)")

    # Valeurs le plus souvent filtrées
    toutes_valeurs_filtrees = []
    for a in analyses_reductions:
        toutes_valeurs_filtrees.extend(a['valeurs_filtrees'])

    if toutes_valeurs_filtrees:
        valeurs_freq = Counter(toutes_valeurs_filtrees)
        print(f"Valeurs les plus filtrées:")
        for valeur, count in valeurs_freq.most_common(5):
            print(f"  Valeur {valeur}: {count} fois")

    # Patterns identifiés
    print(f"\n🎯 **PATTERNS DE RÉDUCTION IDENTIFIÉS**")

    patterns_identifies = defaultdict(int)

    for analyse in analyses_reductions:
        ratio = analyse['ratio_surface']
        nb_filtrees = analyse['nb_valeurs_filtrees']

        if ratio < 0.1:
            patterns_identifies['compression_extreme'] += 1
        elif nb_filtrees == 0:
            patterns_identifies['reduction_simple'] += 1
        elif nb_filtrees == 1:
            patterns_identifies['filtrage_unique'] += 1
        elif nb_filtrees > 1:
            patterns_identifies['filtrage_multiple'] += 1

        # Patterns spécifiques
        valeurs_filtrees = analyse['valeurs_filtrees']
        if 0 in valeurs_filtrees:
            patterns_identifies['suppression_zero'] += 1
        if valeurs_filtrees and max(valeurs_filtrees) == max([v for a in analyses_reductions for v in a['valeurs_filtrees']]):
            patterns_identifies['suppression_max'] += 1

    for pattern, count in sorted(patterns_identifies.items(), key=lambda x: x[1], reverse=True):
        print(f"  {pattern}: {count} occurrences")

    # Recommandations pour l'amélioration
    print(f"\n💡 **RECOMMANDATIONS POUR L'AMÉLIORATION**")
    print("1. **Prioriser compression extrême** (ratio < 10%)")
    print("2. **Améliorer réduction avec filtrage unique**")
    print("3. **Optimiser suppression de zéro**")
    print("4. **Gérer les ratios de surface variables**")
    print("5. **Implémenter logique de conservation intelligente**")

    # Plan d'amélioration concret
    print(f"\n🔧 **PLAN D'AMÉLIORATION CONCRET**")
    print("Phase 2A: Améliorer détecteur de réduction existant")
    print("Phase 2B: Ajouter logique de filtrage intelligent")
    print("Phase 2C: Implémenter compression extrême")
    print("Phase 2D: Tester sur les 12 tâches complexes")

    print(f"\n🏛️ **CONCLUSION**")
    print(f"  Analyse complète des réductions complexes terminée")
    print(f"  Patterns spécifiques identifiés pour amélioration")
    print(f"  Prêt pour implémentation des améliorations")

    print(f"\n✨ Données collectées pour Phase 2 ! ✨")

if __name__ == "__main__":
    analyser_reductions_complexes()
