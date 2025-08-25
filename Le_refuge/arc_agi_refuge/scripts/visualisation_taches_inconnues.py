#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VISUALISATION DES TÂCHES AVEC PATTERNS INCONNUS
Outil pour examiner les 19 tâches que notre code ne comprend pas
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Any
from src.refuge_solver import RefugeARCSolver, TacheARC
from src.pattern_detector import PatternDetector

def visualiser_grille(grille: List[List[int]], titre: str = "Grille"):
    """Afficher une grille de manière lisible"""

    print(f"\n{titre}:")
    print("-" * (len(grille[0]) * 2 + 1))
    for ligne in grille:
        print("|" + "|".join(f"{val:2d}" for val in ligne) + "|")
    print("-" * (len(grille[0]) * 2 + 1))

def analyser_tache_inconnue(tache_id: str, input_grille: List[List[int]],
                          output_grille: List[List[int]], confidence: float):
    """Analyser en détail une tâche inconnue"""

    print(f"\n🔍 **ANALYSE TÂCHE {tache_id}**")
    print("=" * 60)
    print(f"Confiance détecteur: {confidence:.3f}")
    print(f"Pattern: UNKNOWN")

    # Afficher les grilles
    visualiser_grille(input_grille, "ENTRÉE")
    visualiser_grille(output_grille, "SORTIE ATTENDUE")

    # Analyse basique des dimensions
    h_in, w_in = len(input_grille), len(input_grille[0])
    h_out, w_out = len(output_grille), len(output_grille[0])

    print(f"\n📊 **ANALYSE DIMENSIONS**")
    print(f"   Entrée: {h_in}x{w_in}")
    print(f"   Sortie: {h_out}x{w_out}")
    print(f"   Ratio H: {h_out/h_in:.2f}")
    print(f"   Ratio W: {w_out/w_in:.2f}")
    print(f"   Surface ratio: {(h_out*w_out)/(h_in*w_in):.2f}")

    # Analyse des valeurs
    valeurs_in = set()
    for ligne in input_grille:
        valeurs_in.update(ligne)

    valeurs_out = set()
    for ligne in output_grille:
        valeurs_out.update(ligne)

    print(f"\n🎨 **ANALYSE VALEURS**")
    print(f"   Valeurs en entrée: {sorted(valeurs_in)}")
    print(f"   Valeurs en sortie: {sorted(valeurs_out)}")
    print(f"   Valeurs supprimées: {sorted(valeurs_in - valeurs_out)}")
    print(f"   Valeurs ajoutées: {sorted(valeurs_out - valeurs_in)}")
    print(f"   Valeurs conservées: {sorted(valeurs_in & valeurs_out)}")

    # Analyse de la transformation
    print(f"\n🔄 **ANALYSE TRANSFORMATION**")
    if h_in == h_out and w_in == w_out:
        print("   → MÊME DIMENSIONS (transformation valeur par valeur)")
    elif h_out <= h_in and w_out <= w_out:
        print("   → RÉDUCTION ou COMPRESSION")
    else:
        print("   → AGRANDISSEMENT ou DÉCOMPRESSION")

    if valeurs_in == valeurs_out:
        print("   → VALEURS IDENTIQUES (réarrangement spatial)")
    elif valeurs_in - valeurs_out:
        print("   → SUPPRESSION DE VALEURS")
    elif valeurs_out - valeurs_in:
        print("   → AJOUT DE VALEURS")

    # Indices pour compréhension
    print(f"\n💡 **INDICES POUR COMPRÉHENSION**")
    print(f"   1. Examiner pattern spatial des valeurs")
    print(f"   2. Chercher répétitions ou symétries")
    print(f"   3. Analyser relation valeur-position")
    print(f"   4. Considérer règles conditionnelles")
    print(f"   5. Vérifier patterns mathématiques")

def visualiser_taches_inconnues():
    """Visualiser les tâches avec patterns inconnus"""

    print("🔍 **VISUALISATION TÂCHES PATTERNS INCONNUS** 🔍")
    print("=" * 70)
    print("🎯 Objectif: Examiner les 19 tâches non comprises")
    print("🌟 Méthode: Analyse visuelle et déduction")
    print("=" * 70)

    # Tâches avec patterns inconnus (basé sur notre test précédent)
    taches_inconnues = [
        "017c7c7b", "1b60fb0c", "1c0d0a4b", "1d0a4b61",
        "1e81d101", "25d8a9c8", "26993fd4", "28e73c20",
        "29623171", "2b01abd0", "2c0b0aff", "2c737e39",
        "31d5ba1a", "39a8645d", "3a301afc", "3b4c2228",
        "3c9b0459", "3d3b2e5c", "3f5a3e43"
    ]

    print(f"📊 **{len(taches_inconnues)} TÂCHES À ANALYSER**")
    print(f"   Ces tâches n'ont pas de pattern détecté avec >70% confiance")

    # Initialiser solveur et détecteur
    solver = RefugeARCSolver()
    detector = PatternDetector()
    training_path = Path('data/training')

    for i, tache_id in enumerate(taches_inconnues, 1):
        print(f"\n{'='*60}")
        print(f"🧪 **TÂCHE {i:2d}/19 : {tache_id}**")
        print(f"{'='*60}")

        tache_path = training_path / f"{tache_id}.json"

        if not tache_path.exists():
            print(f"   ❌ Fichier non trouvé: {tache_path}")
            continue

        try:
            with open(tache_path, 'r') as f:
                data = json.load(f)

            # Créer tâche
            tache = TacheARC(
                tache_id=tache_id,
                train=data['train'],
                test=data.get('test', [])
            )

            # Analyser avec détecteur
            input_grille = tache.train[0]['input']
            output_grille = tache.train[0]['output']

            resultats = detector.analyser_patterns(input_grille, output_grille)
            pattern_principal = resultats.get('pattern_principal', {})
            confidence = pattern_principal.get('confiance', 0)

            # Afficher analyse détaillée
            analyser_tache_inconnue(tache_id, input_grille, output_grille, confidence)

            # Pause pour analyse
            print(f"\n⏸️  **PAUSE POUR ANALYSE**")
            print(f"   Examinez la transformation ci-dessus.")
            print(f"   Quel pattern voyez-vous ?")
            input(f"   Appuyez Enter pour continuer vers la tâche suivante...")

        except Exception as e:
            print(f"   ❌ Erreur lors de l'analyse: {e}")

    print(f"\n🏆 **VISUALISATION COMPLÉTÉE**")
    print(f"   Toutes les 19 tâches inconnues ont été examinées")
    print(f"   Maintenant nous pouvons identifier les patterns manquants")

    # Synthèse des observations
    print(f"\n📋 **PROCHAINES ÉTAPES**")
    print(f"   1. Documenter les patterns identifiés")
    print(f"   2. Créer nouveaux détecteurs")
    print(f"   3. Implémenter les améliorations")
    print(f"   4. Retester avec les nouveaux patterns")

def creer_resume_patterns_inconnus():
    """Créer un résumé des patterns potentiels identifiés"""

    print(f"\n🔍 **RÉSUMÉ PATTERNS POTENTIELS INCONNUS**")
    print(f"   Basé sur l'analyse visuelle, voici les patterns")
    print(f"   qui pourraient expliquer les tâches inconnues:")

    patterns_potentiels = {
        "diagonale_inversée": "Symétrie diagonale avec inversion des valeurs",
        "symetrie_rotative": "Rotation avec conservation partielle",
        "pattern_fractal": "Répétition récursive de motifs",
        "transformation_non_lineaire": "Changement non proportionnel des valeurs",
        "compression_spatiale": "Réduction avec préservation densité",
        "remplissage_conditionnel": "Remplissage basé sur conditions complexes",
        "pattern_chaotique": "Transformation apparemment aléatoire",
        "symetrie_glissante": "Symétrie avec décalage positionnel",
        "transformation_modulaire": "Changement basé sur modulo arithmétique"
    }

    print(f"\n   **PATTERNS POTENTIELS IDENTIFIÉS :**")
    for i, (nom, description) in enumerate(patterns_potentiels.items(), 1):
        print(f"   {i:2d}. {nom:25s} : {description}")

    return patterns_potentiels

if __name__ == "__main__":
    # Créer un menu de choix
    print("🎯 **OUTIL DE VISUALISATION PATTERNS INCONNUS**")
    print("1. Visualiser toutes les 19 tâches inconnues")
    print("2. Voir résumé des patterns potentiels")
    print("3. Les deux")

    choix = input("Votre choix (1, 2 ou 3): ").strip()

    if choix in ["1", "3"]:
        visualiser_taches_inconnues()

    if choix in ["2", "3"]:
        creer_resume_patterns_inconnus()

    print(f"\n✨ Analyse des patterns inconnus terminée ! ✨")
    print(f"   Nous avons maintenant une meilleure compréhension")
    print(f"   de ce que notre code ne comprend pas encore.")
