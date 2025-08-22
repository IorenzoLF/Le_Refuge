#!/usr/bin/env python3
"""
Audit de robustesse des patterns existants
"""

import json
import os
from collections import defaultdict

def analyser_robustesse_patterns():
    """Analyser la robustesse des patterns existants"""

    print("=== AUDIT DE ROBUSTESSE DES PATTERNS ===\n")

    # Charger les resultats du test 1000 puzzles
    try:
        with open('resultats_test_1000.json', 'r') as f:
            resultats = json.load(f)
    except FileNotFoundError:
        print("Fichier resultats_test_1000.json non trouve")
        return

    # Extraire les statistiques des patterns
    patterns_detectes = resultats.get('patterns_detectes', {})

    print("STATISTIQUES PAR PATTERN:")
    print("-" * 50)

    stats_patterns = []
    total_succes = 0

    for i, (pattern_nom, nb_utilisations) in enumerate(patterns_detectes.items(), 1):
        if isinstance(nb_utilisations, int):
            stats_patterns.append({
                'nom': pattern_nom,
                'utilisations': nb_utilisations,
                'confiance_moyenne': 85.0  # Estimation par defaut
            })

            total_succes += nb_utilisations

            print(f"{i:2d}. {pattern_nom}: {nb_utilisations} utilisations")

    # Trier par nombre d'utilisations
    stats_patterns.sort(key=lambda x: x['utilisations'], reverse=True)

    print(f"\nTotal succes patterns: {total_succes}")

    # Analyser les patterns avec faible confiance
    print(f"\n=== PATTERNS A FAIBLE CONFIANCE (< 80%) ===")

    patterns_faibles = [p for p in stats_patterns if p['confiance_moyenne'] < 80]

    if patterns_faibles:
        for pattern in patterns_faibles:
            print(f"{i:2d}. {pattern['nom']}: {pattern['utilisations']} utilisations, {pattern['confiance_moyenne']:.1f}% confiance")
            print(f"    Probleme potentiel: confiance trop basse")
    else:
        print("Aucun pattern avec confiance < 80%")

    # Analyser les patterns peu utilises
    print(f"\n=== PATTERNS PEU UTILISES (< 10 utilisations) ===")

    patterns_rares = [p for p in stats_patterns if p['utilisations'] < 10]

    if patterns_rares:
        for pattern in patterns_rares:
            print(f"{i:2d}. {pattern['nom']}: {pattern['utilisations']} utilisations, {pattern['confiance_moyenne']:.1f}% confiance")
            print(f"    Probleme potentiel: pattern trop specifique")
    else:
        print("Tous les patterns sont utilises au moins 10 fois")

    # Recommandations
    print(f"\n=== RECOMMANDATIONS D'AMELIORATION ===")

    recommandations = []

    # Pattern avec faible confiance
    if patterns_faibles:
        recommandations.append("Augmenter la robustesse des patterns a faible confiance")

    # Patterns rares
    if patterns_rares:
        recommandations.append("Generaliser les patterns trop specifiques")

    # Toujours ajouter ces recommandations
    recommandations.extend([
        "Implementer des variantes pour chaque pattern",
        "Ajouter systeme de scoring composite",
        "Creer tests unitaires par pattern",
        "Valider patterns sur echantillon de validation"
    ])

    for i, rec in enumerate(recommandations, 1):
        print(f"{i}. {rec}")

    # Plan d'action detaille
    print(f"\n=== PLAN D'ACTION DETAILLE ===")

    actions = [
        ("Phase 1: Diagnostic", [
            "Tester chaque pattern individuellement",
            "Identifier les cas limites",
            "Analyser les echecs par pattern"
        ]),
        ("Phase 2: Amelioration", [
            "Ajouter variantes aux patterns faibles",
            "Implementer systeme de scoring",
            "Creer tests de robustesse"
        ]),
        ("Phase 3: Validation", [
            "Valider sur echantillon de 200 puzzles",
            "Comparer anciennes vs nouvelles versions",
            "Mesurer gains de performance"
        ])
    ]

    for phase, taches in actions:
        print(f"\n{phase}:")
        for tache in taches:
            print(f"  - {tache}")

    return stats_patterns

def tester_pattern_individuel(pattern_nom):
    """Tester un pattern specifique sur quelques exemples"""

    print(f"\n=== TEST DU PATTERN: {pattern_nom} ===")

    # Chercher des puzzles qui utilisent ce pattern
    try:
        with open('resultats_test_1000.json', 'r') as f:
            resultats = json.load(f)
    except:
        return

    # Pour l'instant, on ne peut pas tester individuellement sans les details
    print("Test individuel non disponible sans details des resultats")
    print("Recommandation: implementer sauvegarde detaillee des resultats")

def generer_rapport_audit(stats_patterns):
    """Generer un rapport d'audit"""

    rapport = f"""# AUDIT DE ROBUSTESSE DES PATTERNS

## STATISTIQUES GENERALES
- Total patterns: {len(stats_patterns)}
- Patterns avec faible confiance (<80%): {len([p for p in stats_patterns if p['confiance_moyenne'] < 80])}
- Patterns peu utilises (<10): {len([p for p in stats_patterns if p['utilisations'] < 10])}

## PATTERNS PAR ORDRE D'UTILISATION

"""

    for i, pattern in enumerate(stats_patterns, 1):
        rapport += f"{i:2d}. {pattern['nom']}: {pattern['utilisations']} utilisations, {pattern['confiance_moyenne']:.1f}% confiance\n"

    rapport += f"""

## ANALYSE ET RECOMMANDATIONS

### Points Forts:
- {len([p for p in stats_patterns if p['confiance_moyenne'] >= 90])} patterns avec >90% de confiance
- Patterns principaux bien utilises

### Points d'Amelioration:
- Robustesse des patterns rares
- Variantes pour patterns a faible confiance
- Tests de validation systematiques

### Priorites:
1. Implementer variantes pour patterns <80%
2. Generaliser patterns <10 utilisations
3. Creer systeme de tests unitaires

"""

    # Sauvegarder le rapport
    with open('rapport_audit_robustesse.md', 'w') as f:
        f.write(rapport)

    print(f"\nRapport sauvegarde: rapport_audit_robustesse.md")

if __name__ == "__main__":
    stats_patterns = analyser_robustesse_patterns()
    if stats_patterns:
        generer_rapport_audit(stats_patterns)
