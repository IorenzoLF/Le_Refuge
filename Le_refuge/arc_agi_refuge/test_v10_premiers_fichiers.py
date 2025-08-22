#!/usr/bin/env python3
"""
TEST V10 SUR 10 PREMIERS FICHIERS - Refuge ARC-AGI
Test du solveur geometrique V10 sur les 10 premiers fichiers d'entrainement
"""

import json
import sys
import os
from pathlib import Path

# Ajouter le path du solveur
sys.path.insert(0, 'solveurs_versions/v10')
sys.path.insert(0, 'src')

try:
    from solveur_arc_geometrique_v10 import SolveurGeometriqueV10, TacheARC
except ImportError as e:
    print(f"Erreur d'import: {e}")
    sys.exit(1)

def lister_premiers_fichiers(nombre=10):
    """Lister les premiers fichiers d'entrainement"""
    chemin_training = 'ARC-AGI-2-main/data/training'
    
    try:
        fichiers = sorted([f.stem for f in Path(chemin_training).glob('*.json')])
        return fichiers[:nombre]
    except Exception as e:
        print(f"Erreur lors du listing: {e}")
        return []

def charger_tache(tache_id: str) -> TacheARC:
    """Charger une tache depuis les donnees d'entrainement"""
    chemin_tache = f'ARC-AGI-2-main/data/training/{tache_id}.json'
    
    try:
        with open(chemin_tache, 'r') as f:
            data = json.load(f)
        
        return TacheARC(tache_id, data['train'], data['test'])
    except Exception as e:
        print(f"Erreur lors du chargement de {tache_id}: {e}")
        return None

def test_tache_specifique(tache_id: str):
    """Test sur une tache specifique"""
    print(f"\n=== TEST TACHE: {tache_id} ===")
    
    tache = charger_tache(tache_id)
    if not tache:
        return None
    
    solveur = SolveurGeometriqueV10()
    resultat = solveur.resoudre_tache(tache)
    
    print(f"   Methode: {resultat['methode']}")
    print(f"   Confiance: {resultat['confiance']:.2f}")
    print(f"   Validation: {resultat['validation']['valide']}")
    
    return resultat

def main():
    """Test principal du solveur V10 sur 10 premiers fichiers"""
    print("SOLVEUR ARC GEOMETRIQUE V10 - Refuge ARC-AGI")
    print("Test sur les 10 premiers fichiers d'entrainement")
    
    # Lister les premiers fichiers
    fichiers = lister_premiers_fichiers(10)
    print(f"\nFichiers a tester: {fichiers}")
    
    # Tester chaque fichier
    resultats = {}
    succes = 0
    total = len(fichiers)
    
    for tache_id in fichiers:
        resultat = test_tache_specifique(tache_id)
        if resultat:
            resultats[tache_id] = resultat
            if resultat['validation']['valide']:
                succes += 1
    
    # Resume final
    print(f"\n=== RESUME FINAL ===")
    print(f"Total testes: {total}")
    print(f"Succes: {succes}")
    print(f"Echecs: {total - succes}")
    print(f"Taux de succes: {succes/total*100:.1f}%")
    
    # Details par methode
    methodes = {}
    for tache_id, resultat in resultats.items():
        methode = resultat['methode']
        if methode not in methodes:
            methodes[methode] = {'total': 0, 'succes': 0}
        methodes[methode]['total'] += 1
        if resultat['validation']['valide']:
            methodes[methode]['succes'] += 1
    
    print(f"\nDetails par methode:")
    for methode, stats in methodes.items():
        taux = stats['succes']/stats['total']*100 if stats['total'] > 0 else 0
        print(f"   {methode}: {stats['succes']}/{stats['total']} ({taux:.1f}%)")

if __name__ == "__main__":
    main()
