#!/usr/bin/env python3
"""
TEST SOLVEUR GEOMETRIQUE V10 - Refuge ARC-AGI
Test du solveur avec detection de formes geometriques
"""

import json
import sys
import os
from pathlib import Path

# Ajouter le path du solveur
sys.path.insert(0, '../../solveurs_versions/v10')

try:
    from solveur_arc_geometrique_v10 import SolveurGeometriqueV10, TacheARC
except ImportError as e:
    print(f"Erreur d'import: {e}")
    sys.exit(1)

def charger_tache(tache_id: str) -> TacheARC:
    """Charger une tache depuis les donnees d'entrainement"""
    chemin_tache = f'../../ARC-AGI-2-main/data/training/{tache_id}.json'
    
    try:
        with open(chemin_tache, 'r') as f:
            data = json.load(f)
        
        return TacheARC(tache_id, data['train'], data['test'])
    except Exception as e:
        print(f"Erreur lors du chargement de {tache_id}: {e}")
        return None

def test_tache_specifique(tache_id: str):
    """Test sur une tache specifique"""
    print(f"\n=== TEST TACHE SPECIFIQUE: {tache_id} ===")
    
    tache = charger_tache(tache_id)
    if not tache:
        return
    
    solveur = SolveurGeometriqueV10()
    resultat = solveur.resoudre_tache(tache)
    
    print(f"\nRESULTAT FINAL:")
    print(f"   Tache: {tache_id}")
    print(f"   Methode: {resultat['methode']}")
    print(f"   Confiance: {resultat['confiance']:.2f}")
    print(f"   Approches testees: {resultat['approches_testees']}")
    print(f"   Validation: {resultat['validation']}")
    
    # Afficher les patterns geometriques detectes
    patterns = resultat.get('patterns_geometriques', {})
    if patterns.get('formes_detectees'):
        print(f"   Formes detectees: {len(patterns['formes_detectees'])}")
    if patterns.get('marqueurs_geometriques'):
        print(f"   Marqueurs geometriques: {len(patterns['marqueurs_geometriques'])}")
    if patterns.get('transformations_conditionnelles'):
        print(f"   Transformations conditionnelles: {len(patterns['transformations_conditionnelles'])}")

def test_puzzles_geometriques():
    """Test sur des puzzles avec patterns geometriques"""
    puzzles_geometriques = [
        '009d5c81',  # Transformation conditionnelle
        '007bbfb7',  # Masque de deploiement
        '00576224',  # Tiling repetitif
    ]
    
    print("=== TEST PUZZLES GEOMETRIQUES ===")
    
    for tache_id in puzzles_geometriques:
        test_tache_specifique(tache_id)

def main():
    """Test principal du solveur geometrique V10"""
    print("SOLVEUR ARC GEOMETRIQUE V10 - Refuge ARC-AGI")
    print("Test avec detection de formes geometriques et transformations conditionnelles")
    
    # Test sur les puzzles geometriques
    test_puzzles_geometriques()
    
    print("\n=== FIN DES TESTS ===")

if __name__ == "__main__":
    main()
