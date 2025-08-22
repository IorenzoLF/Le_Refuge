#!/usr/bin/env python3
"""
TEST V11 CORRIGE - Refuge ARC-AGI
Test du solveur V11 corrige sur les 10 premiers fichiers d'entrainement
"""

import json
import sys
import os
from pathlib import Path

# Ajouter le path du solveur
sys.path.insert(0, 'solveurs_versions/v11')

try:
    from solveur_arc_zones_v11 import SolveurZonesV11Simple, TacheARC
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
    """Test du solveur V11 corrige"""
    print("=" * 60)
    print("TEST V11 CORRIGE - Refuge ARC-AGI")
    print("=" * 60)
    
    # Lister les premiers fichiers
    fichiers = lister_premiers_fichiers(10)
    print(f"Fichiers a tester: {fichiers}")
    print()
    
    # Initialiser le solveur
    solveur = SolveurZonesV11Simple()
    
    # Statistiques
    succes = 0
    total = len(fichiers)
    resultats = []
    
    # Tester chaque fichier
    for i, tache_id in enumerate(fichiers, 1):
        print(f"📊 TEST {i}/{total}: {tache_id}")
        
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
    print("=" * 60)
    print("RESULTATS FINAUX")
    print("=" * 60)
    print(f"Total: {total}")
    print(f"Succes: {succes}")
    print(f"Echecs: {total - succes}")
    print(f"Taux de succes: {succes/total*100:.1f}%")
    
    print("\nDetails par tache:")
    for resultat in resultats:
        status = "✅" if resultat['correct'] else "❌"
        print(f"   {status} {resultat['tache_id']}: {resultat['methode']} (confiance: {resultat['confiance']:.2f})")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
