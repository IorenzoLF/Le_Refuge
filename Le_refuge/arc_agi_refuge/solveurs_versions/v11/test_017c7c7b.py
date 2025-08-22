#!/usr/bin/env python3
"""
TEST 017C7C7B - Refuge ARC-AGI
Test spécifique du puzzle 017c7c7b
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

def main():
    """Test du puzzle 017c7c7b"""
    print("=" * 60)
    print("TEST 017C7C7B - Refuge ARC-AGI")
    print("=" * 60)

    # Charger le puzzle
    with open('ARC-AGI-2-main/data/training/017c7c7b.json', 'r') as f:
        data = json.load(f)

    tache = TacheARC('017c7c7b', data['train'], data['test'])
    solveur = SolveurZonesV11Simple()

    print("📊 ANALYSE DU PUZZLE:")
    print(f"   Nombre d'exemples: {len(tache.train)}")
    print(f"   Nombre de tests: {len(tache.test)}")
    
    # Afficher le premier exemple
    exemple = tache.train[0]
    print(f"\n📋 EXEMPLE 1:")
    print("Input:")
    for ligne in exemple['input']:
        print("  " + " ".join(str(pixel) for pixel in ligne))
    
    print("\nOutput:")
    for ligne in exemple['output']:
        print("  " + " ".join(str(pixel) for pixel in ligne))
    
    # Afficher le test
    test = tache.test[0]
    print(f"\n🧪 TEST:")
    print("Input:")
    for ligne in test['input']:
        print("  " + " ".join(str(pixel) for pixel in ligne))
    
    print("\nOutput attendu:")
    for ligne in test['output']:
        print("  " + " ".join(str(pixel) for pixel in ligne))

    print(f"\n🔍 RÉSOLUTION:")
    resultat = solveur.resoudre_tache(tache)

    print(f"\nRESULTAT:")
    print(f"   Solution: {resultat['solution']}")
    print(f"   Confiance: {resultat['confiance']:.2f}")
    print(f"   Methode: {resultat['methode']}")
    print(f"   Validation: {resultat['validation']}")

    # Vérifier si c'est correct
    test_output_attendu = tache.test[0]['output']
    test_output_calcule = resultat['solution']
    
    correct = test_output_calcule == test_output_attendu
    print(f"\n✅ RÉSULTAT FINAL: {'SUCCÈS' if correct else 'ÉCHEC'}")
    
    if not correct:
        print(f"   Différences détectées!")
        print(f"   Attendu: {test_output_attendu}")
        print(f"   Calculé: {test_output_calcule}")

    print("=" * 60)

if __name__ == "__main__":
    main()
