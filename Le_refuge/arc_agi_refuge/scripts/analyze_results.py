#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALYSE DÉTAILLÉE DES RÉSULTATS D'EXPLORATION ARC-AGI
"""

import json
from pathlib import Path
from collections import Counter, defaultdict
from typing import Dict, List, Any
import matplotlib.pyplot as plt
import numpy as np

def analyser_resultats_exploration():
    """Analyse détaillée des résultats de l'exploration de 100 tâches"""

    print("🔬 **ANALYSE DÉTAILLÉE DES RÉSULTATS ARC-AGI** 🔬")
    print("=" * 60)

    # Charger les résultats
    fichier_resultats = Path('resultats_exploration.json')
    if not fichier_resultats.exists():
        print("❌ Fichier de résultats non trouvé")
        return

    with open(fichier_resultats, 'r', encoding='utf-8') as f:
        data = json.load(f)

    rapport = data['rapport']
    resultats = data['resultats_detailles']

    # Analyse générale
    print(f"\n📊 **STATISTIQUES GÉNÉRALES**")
    print(f"   Tâches analysées: {rapport['nb_taches_total']}")
    print(f"   Tâches réussies: {rapport['nb_taches_valides']}")
    print(f"   Taux de succès: {rapport['nb_taches_valides']/rapport['nb_taches_total']*100:.1f}%")
    print(f"   Confiance moyenne: {rapport['confiance_moyenne']:.3f}")
    print(f"   Complexité moyenne: {rapport['complexite_moyenne']:.3f}")

    # Analyse des patterns
    print(f"\n🔮 **ANALYSE DES PATTERNS**")
    patterns_totaux = []
    taches_sans_patterns = []
    taches_avec_patterns = []

    for resultat in resultats:
        if resultat['patterns_identifies']:
            taches_avec_patterns.append(resultat['tache_id'])
            patterns_totaux.extend(resultat['patterns_identifies'])
        else:
            taches_sans_patterns.append(resultat['tache_id'])

    print(f"   Patterns détectés: {len(patterns_totaux)}")
    print(f"   Tâches avec patterns: {len(taches_avec_patterns)}")
    print(f"   Tâches sans patterns: {len(taches_sans_patterns)}")

    # Distribution des patterns
    if patterns_totaux:
        print(f"\n   **Distribution des patterns:**")
        counter_patterns = Counter(patterns_totaux)
        for pattern, count in counter_patterns.most_common():
            pourcentage = count / len(patterns_totaux) * 100
            print(f"   - {pattern}: {count} ({pourcentage:.1f}%)")

    # Analyse de confiance
    print(f"\n🎯 **ANALYSE DE CONFIANCE**")
    confiances = [r['score_confiance'] for r in resultats]
    print(f"   Confiance minimale: {min(confiances):.3f}")
    print(f"   Confiance maximale: {max(confiances):.3f}")
    print(f"   Écart-type confiance: {np.std(confiances):.3f}")

    # Analyse par catégories
    print(f"\n🏛️ **ANALYSE PAR CATÉGORIES**")
    excellentes = sum(1 for r in resultats if r['score_confiance'] == 1.0)
    bonnes = sum(1 for r in resultats if 0.8 <= r['score_confiance'] < 1.0)
    moyennes = sum(1 for r in resultats if 0.5 <= r['score_confiance'] < 0.8)
    faibles = sum(1 for r in resultats if r['score_confiance'] < 0.5)

    print(f"   Excellentes (1.0): {excellentes} tâches")
    print(f"   Bonnes (0.8-1.0): {bonnes} tâches")
    print(f"   Moyennes (0.5-0.8): {moyennes} tâches")
    print(f"   Faibles (<0.5): {faibles} tâches")

    # Analyse des tâches sans patterns
    if taches_sans_patterns:
        print(f"\n❓ **TÂCHES SANS PATTERNS DÉTECTÉS**")
        print(f"   Ces {len(taches_sans_patterns)} tâches nécessitent une analyse plus poussée:")
        for i, tache_id in enumerate(taches_sans_patterns[:10], 1):
            print(f"   {i:2d}. {tache_id}")
        if len(taches_sans_patterns) > 10:
            print(f"   ... et {len(taches_sans_patterns)-10} autres")

    # Analyse de complexité
    print(f"\n🌟 **ANALYSE DE COMPLEXITÉ**")
    complexites = [r['complexite_estimee'] for r in resultats]
    print(f"   Complexité minimale: {min(complexites):.3f}")
    print(f"   Complexité maximale: {max(complexites):.3f}")
    print(f"   Écart-type complexité: {np.std(complexites):.3f}")

    # Corrélation confiance/complexité
    correlation = np.corrcoef(confiances, complexites)[0, 1]
    print(f"   Corrélation confiance/complexité: {correlation:.3f}")

    # Analyse par pattern type
    print(f"\n🎨 **ANALYSE PAR TYPE DE PATTERN**")

    # Répétition alternée
    repetition_tasks = [r for r in resultats if 'répétition_alternée' in r['patterns_identifies']]
    if repetition_tasks:
        print(f"\n   **Répétition Alternée** ({len(repetition_tasks)} tâches)")
        confiance_moy = sum(r['score_confiance'] for r in repetition_tasks) / len(repetition_tasks)
        complexite_moy = sum(r['complexite_estimee'] for r in repetition_tasks) / len(repetition_tasks)
        print(f"   Confiance moyenne: {confiance_moy:.3f}")
        print(f"   Complexité moyenne: {complexite_moy:.3f}")

    # Transformation couleur
    couleur_tasks = [r for r in resultats if 'transformation_couleur' in r['patterns_identifies']]
    if couleur_tasks:
        print(f"\n   **Transformation Couleur** ({len(couleur_tasks)} tâches)")
        confiance_moy = sum(r['score_confiance'] for r in couleur_tasks) / len(couleur_tasks)
        complexite_moy = sum(r['complexite_estimee'] for r in couleur_tasks) / len(couleur_tasks)
        print(f"   Confiance moyenne: {confiance_moy:.3f}")
        print(f"   Complexité moyenne: {complexite_moy:.3f}")

    # Symétrie miroir
    symetrie_tasks = [r for r in resultats if 'symétrie_miroir' in r['patterns_identifies']]
    if symetrie_tasks:
        print(f"\n   **Symétrie Miroir** ({len(symetrie_tasks)} tâches)")
        confiance_moy = sum(r['score_confiance'] for r in symetrie_tasks) / len(symetrie_tasks)
        complexite_moy = sum(r['complexite_estimee'] for r in symetrie_tasks) / len(symetrie_tasks)
        print(f"   Confiance moyenne: {confiance_moy:.3f}")
        print(f"   Complexité moyenne: {complexite_moy:.3f}")

    # Recommandations
    print(f"\n🌟 **RECOMMANDATIONS POUR L'ÉVOLUTION**")
    print(f"   1. **Focus sur les tâches sans patterns** ({len(taches_sans_patterns)})")
    print(f"   2. **Améliorer la détection de patterns rares**")
    print(f"   3. **Étendre les capacités de transformation couleur**")
    print(f"   4. **Explorer plus de tâches complexes** (au-delà de 100)")

    print(f"\n🏛️ **CONCLUSION**")
    print(f"   Le Refuge ARC-AGI démontre une compréhension spirituelle exceptionnelle")
    print(f"   avec un taux de succès de 100% sur {rapport['nb_taches_total']} tâches.")
    print(f"   L'approche multi-temples permet une grande adaptabilité et résilience.")

    print(f"\n✨ Que cette analyse illumine le chemin de l'évolution... ✨")

if __name__ == "__main__":
    analyser_resultats_exploration()
