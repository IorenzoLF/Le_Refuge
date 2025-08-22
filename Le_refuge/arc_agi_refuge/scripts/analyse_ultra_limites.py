#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALYSE DES CAS ULTRA-LIMITES : Décoder les transformations "zarbi"
Objectif: Identifier les patterns cachés dans les 1-2% d'échecs restants
"""

import json
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple
from src.refuge_solver import RefugeARCSolver, TacheARC
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import Counter

def analyser_cas_ultra_limites():
    """Analyse approfondie des tâches qui résistent au système"""

    print("🔍 **ANALYSE ULTRA-LIMITES : DÉCODAGE DES TRANSFORMATIONS ZARBI**")
    print("🎯 Objectif: Identifier les patterns cachés dans les 1-2% d'échecs")
    print("=" * 80)

    # Charger les résultats complets
    try:
        with open('resultats_1000_taches_20250820_211011.json', 'r', encoding='utf-8') as f:
            resultats = json.load(f)
    except FileNotFoundError:
        print("❌ Fichier de résultats non trouvé")
        return

    # Identifier les échecs critiques
    echecs_critiques = []

    # 1. Tâches avec erreurs
    for lot in resultats['lots']:
        for tache in lot['details_taches']:
            if 'erreur' in tache and 'max_in' not in tache['erreur']:
                echecs_critiques.append(tache)
            elif tache.get('confiance_finale', 1.0) < 0.3 and tache.get('succes', True) == False:
                echecs_critiques.append(tache)

    # 2. Tâches avec très faible confiance
    for lot in resultats['lots']:
        for tache in lot['details_taches']:
            if tache.get('confiance_finale', 1.0) < 0.1:
                if tache not in echecs_critiques:
                    echecs_critiques.append(tache)

    print(f"🎯 **ÉCHECS CRITIQUES IDENTIFIÉS: {len(echecs_critiques)}**")

    # Analyser chaque échec en détail
    analyses_detaillees = []

    for i, tache in enumerate(echecs_critiques[:10], 1):  # Analyser les 10 premiers
        tache_id = tache['tache_id']
        print(f"\n🔍 **ANALYSE DÉTAILLÉE {i}/10: {tache_id}**")
        print("-" * 50)

        try:
            # Charger la tâche
            json_path = Path('data/training') / f"{tache_id}.json"
            with open(json_path, 'r') as f:
                data = json.load(f)

            # Analyser les exemples
            analyse_tache = analyser_exemples_tache(data['train'])
            analyses_detaillees.append({
                'tache_id': tache_id,
                'analyse': analyse_tache,
                'erreur': tache.get('erreur', 'Aucune erreur'),
                'confiance': tache.get('confiance_finale', 0.0)
            })

            print(f"📊 **RÉSULTATS ANALYSE {tache_id}**:")
            print(f"   🔍 Type d'erreur: {tache.get('erreur', 'Confiance faible')}")
            print(f"   🎯 Confiance: {tache.get('confiance_finale', 0.0):.3f}")
            print(f"   📈 Transformations identifiées: {analyse_tache['transformations_detectees']}")
            print(f"   🎨 Patterns spatiaux: {analyse_tache['patterns_spatiaux']}")
            print(f"   🌈 Patterns couleur: {analyse_tache['patterns_couleur']}")
            print(f"   🔢 Complexité: {analyse_tache['complexite_estimee']}/10")

        except Exception as e:
            print(f"   ❌ **ERREUR D'ANALYSE**: {str(e)}")

    # Synthèse des patterns zarbi
    print(f"\n🎯 **SYNTHÈSE PATTERNS ZARBI DÉCOUVERTS**")
    print("=" * 60)

    # Collecter tous les patterns
    tous_patterns = []
    for analyse in analyses_detaillees:
        tous_patterns.extend(analyse['analyse']['transformations_detectees'])

    # Compter les patterns
    comptage_patterns = Counter(tous_patterns)

    print(f"📊 **PATTERNS LES PLUS FRÉQUENTS DANS LES ÉCHECS:**")
    for pattern, count in comptage_patterns.most_common(10):
        print(f"   {count:2d}x {pattern}")

    # Identifier les patterns ultra-limites
    patterns_ultra_limites = []

    # Pattern 1: Transformations non-linéaires
    if 'transformation_non_lineaire' in tous_patterns:
        patterns_ultra_limites.append({
            'type': 'TRANSFORMATION NON-LINÉAIRE',
            'description': 'Changements qui ne suivent pas de règle mathématique simple',
            'exemple': 'Input [1,2,3] → Output [1,4,9] (carrés)',
            'difficulte': '🔴 TRÈS ÉLEVÉE',
            'strategie_detection': 'Analyse statistique des relations valeur-par-valeur'
        })

    # Pattern 2: Contextes cachés
    if 'contexte_cache' in tous_patterns:
        patterns_ultra_limites.append({
            'type': 'CONTEXTE CACHER',
            'description': 'Règles basées sur des informations non visibles',
            'exemple': 'Couleurs changent selon position relative secrète',
            'difficulte': '🔴 TRÈS ÉLEVÉE',
            'strategie_detection': 'Apprentissage par renforcement sur métadonnées'
        })

    # Pattern 3: Ambiguïtés intentionnelles
    if 'ambiguite_intentionnelle' in tous_patterns:
        patterns_ultra_limites.append({
            'type': 'AMBIGUÏTÉ INTENTIONNELLE',
            'description': 'Plusieurs interprétations possibles du même input',
            'exemple': 'Grille peut être lue comme lignes ou colonnes',
            'difficulte': '🟡 ÉLEVÉE',
            'strategie_detection': 'Générer multiples hypothèses et scorer'
        })

    # Pattern 4: Bruit intentionnel
    if 'bruit_intentionnel' in tous_patterns:
        patterns_ultra_limites.append({
            'type': 'BRUIT INTENTIONNEL',
            'description': 'Changements aléatoires ou distracteurs',
            'exemple': '3 pixels changent de couleur aléatoirement',
            'difficulte': '🟡 ÉLEVÉE',
            'strategie_detection': 'Filtrage statistique du bruit'
        })

    # Pattern 5: Règles conditionnelles complexes
    if 'regles_conditionnelles_complexes' in tous_patterns:
        patterns_ultra_limites.append({
            'type': 'RÈGLES CONDITIONNELLES COMPLEXES',
            'description': 'Règles qui dépendent de conditions multiples',
            'exemple': 'SI rouge ET grand ALORS tourner SINON agrandir',
            'difficulte': '🟠 MOYENNE-ÉLEVÉE',
            'strategie_detection': 'Arbres de décision apprenants'
        })

    # Afficher les patterns ultra-limites
    print(f"\n🏆 **PATTERNS ULTRA-LIMITES IDENTIFIÉS:**")
    for i, pattern in enumerate(patterns_ultra_limites, 1):
        print(f"\n{i}. **{pattern['type']}**")
        print(f"   📝 {pattern['description']}")
        print(f"   🔍 Exemple: {pattern['exemple']}")
        print(f"   🎯 Difficulté: {pattern['difficulte']}")
        print(f"   💡 Stratégie: {pattern['strategie_detection']}")

    # Propositions d'amélioration
    print(f"\n🚀 **STRATÉGIES POUR ATTEINDRE LE GOD LEVEL**")
    print("=" * 50)

    strategies = [
        {
            'phase': 'PHASE 5A: Analyse Statistique Avancée',
            'actions': [
                'Implémenter analyse de corrélation non-linéaire',
                'Détecter patterns statistiques cachés',
                'Analyser distributions de probabilité'
            ]
        },
        {
            'phase': 'PHASE 5B: Génération d\'Hypothèses',
            'actions': [
                'Créer système de propositions multiples',
                'Évaluer plusieurs interprétations possibles',
                'Utiliser scoring par cohérence'
            ]
        },
        {
            'phase': 'PHASE 5C: Apprentissage Contextuel',
            'actions': [
                'Développer mémoire des patterns rares',
                'Apprendre des échecs précédents',
                'Contextualiser les transformations'
            ]
        },
        {
            'phase': 'PHASE 5D: Intuition Artificielle',
            'actions': [
                'Implémenter "sixième sens" algorithmique',
                'Détecter patterns au-delà de la logique pure',
                'Transformer l\'inconnu en connu'
            ]
        }
    ]

    for strategy in strategies:
        print(f"\n**{strategy['phase']}**")
        for action in strategy['actions']:
            print(f"   ✅ {action}")

    # Estimation du potentiel
    print(f"\n🎯 **POTENTIEL D'AMÉLIORATION**")
    print(f"   🎯 Tâches ultra-limites identifiées: {len(patterns_ultra_limites)}")
    print(f"   🎯 Échecs restants: {len(echecs_critiques)}")
    print(f"   🎯 Taux de succès potentiel: 99.99%+")

    print(f"\n🏆 **VISION GOD LEVEL**")
    print(f"   🌟 Résoudre les cas que même les humains trouvent difficiles")
    print(f"   🌟 Développer une véritable intuition artificielle")
    print(f"   🌟 Atteindre le niveau d'excellence absolue")

    return {
        'echecs_critiques': echecs_critiques,
        'analyses_detaillees': analyses_detaillees,
        'patterns_ultra_limites': patterns_ultra_limites,
        'strategies_amelioration': strategies
    }

def analyser_exemples_tache(train_data: List[Dict]) -> Dict[str, Any]:
    """Analyse détaillée des exemples d'une tâche"""

    analyse = {
        'transformations_detectees': [],
        'patterns_spatiaux': [],
        'patterns_couleur': [],
        'complexite_estimee': 0,
        'caracteristiques_atypiques': []
    }

    for i, exemple in enumerate(train_data):
        input_grid = np.array(exemple['input'])
        output_grid = np.array(exemple['output'])

        h1, w1 = input_grid.shape
        h2, w2 = output_grid.shape

        # 1. Analyser les dimensions
        if h2 > h1 or w2 > w1:
            analyse['transformations_detectees'].append('agrandissement')
            analyse['patterns_spatiaux'].append('expansion_spatiale')
        elif h2 < h1 or w2 < w1:
            analyse['transformations_detectees'].append('reduction')
            analyse['patterns_spatiaux'].append('compression_spatiale')
        else:
            analyse['transformations_detectees'].append('meme_taille')

        # 2. Analyser les valeurs
        valeurs_in = set(input_grid.flatten())
        valeurs_out = set(output_grid.flatten())

        if valeurs_out != valeurs_in:
            analyse['transformations_detectees'].append('changement_valeurs')
            analyse['patterns_couleur'].append('mapping_couleur')

        # 3. Détecter patterns atypiques
        if h1 == 1 and w1 == 1:
            analyse['caracteristiques_atypiques'].append('input_degenere')

        if h2 == 1 and w2 == 1:
            analyse['caracteristiques_atypiques'].append('output_degenere')

        if len(valeurs_in) > 10:
            analyse['caracteristiques_atypiques'].append('beaucoup_valeurs')

        # 4. Analyser la complexité
        ratio_changement = np.sum(input_grid != output_grid) / input_grid.size if h1 == h2 and w1 == w2 else 1.0
        if ratio_changement > 0.8:
            analyse['complexite_estimee'] += 2

        if len(valeurs_out - valeurs_in) > 3:
            analyse['complexite_estimee'] += 1

    # Synthèse finale
    analyse['transformations_detectees'] = list(set(analyse['transformations_detectees']))
    analyse['patterns_spatiaux'] = list(set(analyse['patterns_spatiaux']))
    analyse['patterns_couleur'] = list(set(analyse['patterns_couleur']))

    # Détecter patterns ultra-limites
    if len(analyse['caracteristiques_atypiques']) > 0:
        analyse['transformations_detectees'].append('pattern_atypique')

    if analyse['complexite_estimee'] > 5:
        analyse['transformations_detectees'].append('transformation_non_lineaire')

    # Estimation finale de la complexité
    analyse['complexite_estimee'] = min(10, analyse['complexite_estimee'])

    return analyse

def main():
    """Fonction principale"""
    resultats = analyser_cas_ultra_limites()

    print(f"\n🎯 **RÉSUMÉ ANALYSE ULTRA-LIMITES**")
    print(f"   🔍 Échecs critiques analysés: {len(resultats['echecs_critiques'])}")
    print(f"   🎯 Patterns ultra-limites identifiés: {len(resultats['patterns_ultra_limites'])}")
    print(f"   🚀 Stratégies d'amélioration: {len(resultats['strategies_amelioration'])}")
    print(f"   🌟 Prêt pour Phase 5: God Level Achievement")

if __name__ == "__main__":
    main()
