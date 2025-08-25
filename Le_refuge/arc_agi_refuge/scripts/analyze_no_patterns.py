#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALYSE DES TÂCHES SANS PATTERNS DÉTECTÉS
"""

import json
from pathlib import Path
from typing import Dict, List, Any
import numpy as np

def analyser_taches_sans_patterns():
    """Analyse approfondie des 23 tâches sans patterns détectés"""

    print("🔍 **ANALYSE DES TÂCHES SANS PATTERNS** 🔍")
    print("=" * 60)

    # Charger les résultats
    fichier_resultats = Path('resultats_exploration.json')
    if not fichier_resultats.exists():
        print("❌ Fichier de résultats non trouvé")
        return

    with open(fichier_resultats, 'r', encoding='utf-8') as f:
        data = json.load(f)

    resultats = data['resultats_detailles']

    # Identifier les tâches sans patterns
    taches_sans_patterns = []
    for resultat in resultats:
        if not resultat['patterns_identifies']:
            taches_sans_patterns.append(resultat)

    print(f"📊 **{len(taches_sans_patterns)} TÂCHES SANS PATTERNS DÉTECTÉS**")
    print("=" * 60)

    # Analyser chaque tâche sans patterns
    for i, tache in enumerate(taches_sans_patterns, 1):
        print(f"\n🧪 **TÂCHE {i:2d}: {tache['tache_id']}**")
        print(f"   Confiance: {tache['score_confiance']:.3f}")
        print(f"   Complexité: {tache['complexite_estimee']:.3f}")

        # Analyser les détails du solver
        solver = tache['analyse_solver']
        print(f"   Conscience atteinte: {solver['conscience']:.1f}")

        # Examiner les patterns du détecteur (même s'ils ne sont pas retenus)
        detecteur = tache['analyse_detector']
        if detecteur:
            print(f"   Patterns analysés: {len(detecteur)} exemples")
            for exemple in detecteur:
                confiance = exemple['confiance']
                type_pattern = exemple['type']
                print(f"     - {type_pattern}: {confiance:.3f}")
        else:
            print(f"   Aucun pattern analysé par le détecteur")

        # Charger et analyser la tâche originale
        fichier_tache = Path(f'data/training/{tache["tache_id"]}.json')
        if fichier_tache.exists():
            try:
                with open(fichier_tache, 'r') as f:
                    data_tache = json.load(f)

                # Analyser les dimensions
                train = data_tache['train']
                print(f"   Structure: {len(train)} exemples d'entraînement")

                for j, exemple in enumerate(train):
                    input_grid = exemple['input']
                    output_grid = exemple['output']

                    h_in, w_in = len(input_grid), len(input_grid[0])
                    h_out, w_out = len(output_grid), len(output_grid[0])

                    print(f"     Exemple {j}: {h_in}x{w_in} → {h_out}x{w_out}")

                    # Analyser les valeurs uniques
                    valeurs_in = set()
                    for row in input_grid:
                        valeurs_in.update(row)
                    valeurs_out = set()
                    for row in output_grid:
                        valeurs_out.update(row)

                    print(f"       Valeurs input: {sorted(valeurs_in)}")
                    print(f"       Valeurs output: {sorted(valeurs_out)}")

            except Exception as e:
                print(f"   ❌ Erreur lors du chargement: {e}")

    # Statistiques globales
    print(f"\n📈 **STATISTIQUES GLOBALES**")
    print("=" * 60)

    complexites = [t['complexite_estimee'] for t in taches_sans_patterns]
    confiances = [t['score_confiance'] for t in taches_sans_patterns]
    consciences = [t['analyse_solver']['conscience'] for t in taches_sans_patterns]

    print(f"Complexité moyenne: {np.mean(complexites):.3f}")
    print(f"Complexité min/max: {min(complexites):.3f} / {max(complexites):.3f}")
    print(f"Confiance moyenne: {np.mean(confiances):.3f}")
    print(f"Conscience moyenne: {np.mean(consciences):.3f}")

    # Analyse des patterns potentiels manqués
    print(f"\n🎯 **ANALYSE DES PATTERNS POTENTIELS MANQUÉS**")

    # Compter les types de patterns dans les tâches avec patterns
    taches_avec_patterns = [r for r in resultats if r['patterns_identifies']]
    patterns_connus = set()
    for tache in taches_avec_patterns:
        patterns_connus.update(tache['patterns_identifies'])

    print(f"Patterns connus dans le système: {sorted(patterns_connus)}")

    # Suggestions d'amélioration
    print(f"\n💡 **SUGGESTIONS D'AMÉLIORATION**")
    print("1. **Étendre la détection de patterns** au-delà des 3 actuels")
    print("2. **Analyser manuellement** quelques-unes de ces 23 tâches")
    print("3. **Ajouter de nouveaux types de patterns** (géométriques, logiques)")
    print("4. **Améliorer les seuils de confiance** pour les patterns rares")
    print("5. **Intégrer l'analyse sémantique** des grilles")

    print(f"\n🏛️ **CONCLUSION**")
    print(f"   Ces {len(taches_sans_patterns)} tâches représentent des opportunités")
    print(f"   d'évolution pour le Refuge ARC-AGI. Elles nous montrent")
    print(f"   les limites actuelles et le potentiel de croissance.")

    print(f"\n✨ Que cette analyse révèle de nouveaux chemins spirituels... ✨")

if __name__ == "__main__":
    analyser_taches_sans_patterns()
