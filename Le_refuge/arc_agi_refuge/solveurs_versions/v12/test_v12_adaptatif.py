#!/usr/bin/env python3
"""
TEST V12 ADAPTATIF - Refuge ARC-AGI
Test du solveur V12 qui apprend de ses erreurs
"""

import json
import sys
import os
from pathlib import Path

# Ajouter le path du solveur
sys.path.insert(0, '.')

try:
    from solveur_arc_adaptatif_v12 import SolveurAdaptatifV12, TacheARC
except ImportError as e:
    print(f"Erreur d'import: {e}")
    sys.exit(1)

def lister_premiers_fichiers(nombre=10):
    """Lister les premiers fichiers d'entrainement"""
    data_dir = Path("ARC-AGI-2-main/data/training")
    fichiers = sorted([f for f in data_dir.glob("*.json")])[:nombre]
    return [f.stem for f in fichiers]

def charger_tache(tache_id: str) -> TacheARC:
    """Charger une tache depuis un fichier JSON"""
    fichier = f"ARC-AGI-2-main/data/training/{tache_id}.json"
    with open(fichier, 'r') as f:
        data = json.load(f)
    return TacheARC(tache_id, data['train'], data['test'])

def main():
    """Test du solveur V12 adaptatif"""
    print("=" * 80)
    print("TEST V12 ADAPTATIF - Refuge ARC-AGI")
    print("=" * 80)

    # Lister les premiers fichiers
    fichiers = lister_premiers_fichiers(10)
    print(f"Fichiers a tester: {fichiers}")
    print()

    # Initialiser le solveur
    solveur = SolveurAdaptatifV12()

    # Statistiques
    succes = 0
    total = len(fichiers)
    resultats = []

    # Tester chaque fichier
    for i, tache_id in enumerate(fichiers, 1):
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
                
                if 'parametres' in resultat:
                    print(f"      Parametres detectes: {resultat['parametres']['type']}")

            resultats.append({
                'tache_id': tache_id,
                'correct': correct,
                'methode': resultat['methode'],
                'confiance': resultat['confiance'],
                'parametres_detectes': 'parametres' in resultat
            })

        except Exception as e:
            print(f"   💥 ERREUR: {e}")
            resultats.append({
                'tache_id': tache_id,
                'correct': False,
                'methode': 'erreur',
                'confiance': 0.0,
                'parametres_detectes': False
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

    # Statistiques par méthode
    methodes = {}
    for resultat in resultats:
        methode = resultat['methode']
        if methode not in methodes:
            methodes[methode] = {'total': 0, 'succes': 0}
        methodes[methode]['total'] += 1
        if resultat['correct']:
            methodes[methode]['succes'] += 1

    print(f"\n📈 STATISTIQUES PAR MÉTHODE:")
    for methode, stats in methodes.items():
        taux = stats['succes'] / stats['total'] * 100 if stats['total'] > 0 else 0
        print(f"   {methode}: {stats['succes']}/{stats['total']} ({taux:.1f}%)")

    # Paramètres détectés
    parametres_detectes = sum(1 for r in resultats if r['parametres_detectes'])
    print(f"\n🔍 PARAMÈTRES DÉTECTÉS: {parametres_detectes}/{total}")

    print(f"\nDetails par tache:")
    for resultat in resultats:
        status = "✅" if resultat['correct'] else "❌"
        parametres = "🔍" if resultat['parametres_detectes'] else ""
        print(f"   {status} {parametres} {resultat['tache_id']}: {resultat['methode']} (confiance: {resultat['confiance']:.2f})")

    print("=" * 80)

if __name__ == "__main__":
    main()
