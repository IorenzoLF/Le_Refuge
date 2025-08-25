#!/usr/bin/env python3
"""
TEST V11 COMPLET - Refuge ARC-AGI
Test du solveur V11 sur les puzzles qu'on a analysés ensemble
"""

import json
import sys
import os
from pathlib import Path

# Ajouter le path du solveur
sys.path.insert(0, '.')

try:
    from solveur_arc_zones_v11 import SolveurZonesV11Simple, TacheARC
except ImportError as e:
    print(f"Erreur d'import: {e}")
    sys.exit(1)

def charger_tache(tache_id: str) -> TacheARC:
    """Charger une tache depuis un fichier JSON"""
    fichier = f"../ARC-AGI-2-main/data/training/{tache_id}.json"
    with open(fichier, 'r') as f:
        data = json.load(f)
    return TacheARC(tache_id, data['train'], data['test'])

def main():
    """Test du solveur V11 sur les puzzles analysés"""
    print("=" * 80)
    print("TEST V11 COMPLET - Refuge ARC-AGI")
    print("=" * 80)

    # Puzzles qu'on a analysés ensemble
    puzzles_analyses = [
        "00576224",  # Tiling répétitif
        "007bbfb7",  # Masque de déploiement
        "009d5c81",  # Géométrie conditionnelle
        "00d62c1b",  # Remplissage de zones (réussi)
        "00dbd492",  # Remplissage de zones avec paramètres
        "017c7c7b",  # Transformation de couleur + répétition
    ]

    print(f"Puzzles a tester: {puzzles_analyses}")
    print()

    # Initialiser le solveur
    solveur = SolveurZonesV11Simple()

    # Statistiques
    succes = 0
    total = len(puzzles_analyses)
    resultats = []

    # Tester chaque puzzle
    for i, tache_id in enumerate(puzzles_analyses, 1):
        print(f"📊 TEST {i}/{total}: {tache_id}")
        print("-" * 60)

        try:
            # Charger la tache
            tache = charger_tache(tache_id)

            # Resoudre
            resultat = solveur.resoudre_tache(tache)

            # Verifier si c'est correct
            test_output_attendu = tache.test[0]['output']
            test_output_calcule = resultat['solution']

            correct = test_output_calcule == test_output_attendu
            if correct:
                succes += 1
                print(f"   ✅ SUCCES - Methode: {resultat['methode']}")
            else:
                print(f"   ❌ ECHEC - Methode: {resultat['methode']}")
                print(f"      Confiance: {resultat['confiance']:.2f}")
                if 'validation' in resultat:
                    validation = resultat['validation']
                    print(f"      Validation: {validation['erreurs']}/{validation['total_tests']} erreurs")

            resultats.append({
                'tache_id': tache_id,
                'correct': correct,
                'methode': resultat['methode'],
                'confiance': resultat['confiance']
            })

        except Exception as e:
            print(f"   💥 ERREUR: {e}")
            resultats.append({
                'tache_id': tache_id,
                'correct': False,
                'methode': 'erreur',
                'confiance': 0.0
            })

        print()

    # Afficher les resultats finaux
    print("=" * 80)
    print("RESULTATS FINAUX")
    print("=" * 80)
    print(f"Total: {total}")
    print(f"Succes: {succes}")
    print(f"Echecs: {total - succes}")
    print(f"Taux de succes: {succes/total*100:.1f}%")

    print(f"\nDetails par puzzle:")
    for resultat in resultats:
        status = "✅" if resultat['correct'] else "❌"
        print(f"   {status} {resultat['tache_id']}: {resultat['methode']} (confiance: {resultat['confiance']:.2f})")

    print("=" * 80)

    # Analyse des échecs
    echecs = [r for r in resultats if not r['correct']]
    if echecs:
        print(f"\n🔍 ANALYSE DES ÉCHECS:")
        for echec in echecs:
            print(f"   - {echec['tache_id']}: {echec['methode']}")
            if echec['tache_id'] == "017c7c7b":
                print(f"     → Attendu: transformation 1→2 + répétition")
            elif echec['tache_id'] == "00576224":
                print(f"     → Attendu: tiling répétitif")
            elif echec['tache_id'] == "007bbfb7":
                print(f"     → Attendu: masque de déploiement")
            elif echec['tache_id'] == "009d5c81":
                print(f"     → Attendu: géométrie conditionnelle")

    print("=" * 80)

if __name__ == "__main__":
    main()
