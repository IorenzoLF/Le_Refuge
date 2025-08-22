#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STRATÉGIE DE GÉNÉRALISATION POUR TESTS "PAS VUS EN COURS"
Phase 2C : Préparer le solveur pour des variations complexes
"""

import json
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Tuple
from src.pattern_detector import PatternDetector

def analyser_pour_generalisation():
    """Analyser les patterns pour anticiper les variations de test"""

    print("🧠 **STRATÉGIE DE GÉNÉRALISATION** 🧠")
    print("=" * 70)
    print("Basé sur l'observation : Les tests complexifient les patterns existants")
    print("Objectif : Préparer le solveur pour des variations +1/+2 niveaux")
    print("=" * 70)

    training_path = Path('data/training')
    detecteur = PatternDetector()

    # Analyser quelques tâches représentatives
    taches_representatives = [
        '22425bda',  # Réduction + filtrage simple
        'ff805c23',  # Réduction + filtrage multiple
        'b94a9452',  # Compression + suppression zéro
        'de493100'   # Réduction progressive
    ]

    analyses_generalisation = []

    print(f"\n📊 Analyse de {len(taches_representatives)} tâches représentatives")

    for tache_id in taches_representatives:
        tache_path = training_path / f"{tache_id}.json"

        if not tache_path.exists():
            continue

        with open(tache_path, 'r') as f:
            data = json.load(f)

        print(f"\n🧪 **TÂCHE {tache_id}**")

        # Analyser les exemples pour identifier la logique de base
        patterns_fondamentaux = []

        for i, exemple in enumerate(data['train'][:3]):
            input_grid = exemple['input']
            output_grid = exemple['output']

            # Détecter les patterns avec notre détecteur amélioré
            resultats = detecteur.analyser_patterns(input_grid, output_grid)

            if resultats['patterns']:
                pattern_principal = resultats['pattern_principal']
                patterns_fondamentaux.append(pattern_principal)

                print(f"  Exemple {i+1}: {pattern_principal['type']} (confiance: {pattern_principal['confiance']:.3f})")

                # Analyser les patterns spécifiques pour généralisation
                if 'patterns_specifiques' in pattern_principal:
                    specs = pattern_principal['patterns_specifiques']
                    print(f"    Patterns: {specs}")

                    # Générer des variations potentielles
                    variations = generer_variations(pattern_principal)
                    if variations:
                        print(f"    Variations potentielles: {variations}")

        # Synthèse pour la tâche
        analyse_tache = {
            'tache_id': tache_id,
            'patterns_fondamentaux': patterns_fondamentaux,
            'variations_possibles': []
        }

        analyses_generalisation.append(analyse_tache)

    print(f"\n🎯 **STRATÉGIE DE GÉNÉRALISATION**")
    print("=" * 70)

    print(f"\n1. **PATTERNS DE BASE IDENTIFIÉS**")
    patterns_types = set()
    for analyse in analyses_generalisation:
        for pattern in analyse['patterns_fondamentaux']:
            patterns_types.add(pattern['type'])

    for pattern_type in sorted(patterns_types):
        print(f"   ✅ {pattern_type}")

    print(f"\n2. **VARIATIONS +1 NIVEAU (TESTS FACILES)**")
    print(f"   📈 Compression plus extrême (< 5%)")
    print(f"   📈 Filtrage de plus de valeurs")
    print(f"   📈 Combinaison avec d'autres patterns simples")
    print(f"   📈 Variations dans les valeurs conservées")

    print(f"\n3. **VARIATIONS +2 NIVEAUX (TESTS DIFFICILES)**")
    print(f"   💪 Patterns composés (réduction + rotation + filtrage)")
    print(f"   💪 Règles conditionnelles complexes")
    print(f"   💪 Transformations multi-étapes")
    print(f"   💪 Contexte spatial avancé")

    print(f"\n4. **STRATÉGIE DE DÉFENSE**")
    print(f"   🛡️ Détecter les patterns de base d'abord")
    print(f"   🛡️ Chercher les extensions/complexifications")
    print(f"   🛡️ Maintenir plusieurs hypothèses en parallèle")
    print(f"   🛡️ Utiliser les temples pour générer des variations")

    print(f"\n5. **AMÉLIORATIONS À APPORTER**")
    print(f"   🔧 Ajouter détecteur de patterns composés")
    print(f"   🔧 Améliorer la gestion des variations mineures")
    print(f"   🔧 Implémenter logique de complexification")
    print(f"   🔧 Renforcer l'analyse contextuelle")

    print(f"\n🏛️ **CONCLUSION**")
    print(f"  Stratégie de généralisation définie")
    print(f"  Préparation aux variations de test")
    print(f"  Architecture adaptée aux complexifications")
    print(f"  Prêt pour les tests 'pas vus en cours'")

    print(f"\n✨ Stratégie de généralisation complétée ! ✨")

def generer_variations(pattern: Dict[str, Any]) -> List[str]:
    """Générer des variations potentielles d'un pattern"""

    variations = []

    # Variations pour réduction complexe
    if pattern['type'] == 'réduction_complexe':
        ratio = pattern.get('ratio_surface', 1.0)
        valeurs_filtrees = pattern.get('valeurs_filtrees', [])

        if ratio < 0.05:
            variations.append("compression_ultra_extreme")
        if len(valeurs_filtrees) > 2:
            variations.append("filtrage_multiple_plus")
        if 0 in valeurs_filtrees:
            variations.append("suppression_zero_plus_context")

    # Variations pour réduction dimensionnelle
    elif pattern['type'] == 'réduction_dimensionnelle':
        specs = pattern.get('patterns_specifiques', [])
        if 'compression_extreme' in specs:
            variations.append("compression_variable")
        if 'filtrage_unique' in specs:
            variations.append("filtrage_unique_multiple_contextes")

    return variations

if __name__ == "__main__":
    analyser_pour_generalisation()
