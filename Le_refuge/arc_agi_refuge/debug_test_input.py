#!/usr/bin/env python3
"""
DEBUG TEST INPUT - Refuge ARC-AGI
Script pour debugger le test input du puzzle 00d62c1b
"""

import json
import sys
from pathlib import Path

# Ajouter le path du solveur
sys.path.insert(0, 'solveurs_versions/v11')

from solveur_arc_zones_v11 import ZoneAnalyzer, TacheARC

def debug_test_input():
    """Debugger le test input du puzzle 00d62c1b"""
    
    # Charger le puzzle 00d62c1b
    with open('ARC-AGI-2-main/data/training/00d62c1b.json', 'r') as f:
        data = json.load(f)
    
    tache = TacheARC('00d62c1b', data['train'], data['test'])
    zone_analyzer = ZoneAnalyzer()
    
    print("=" * 60)
    print("DEBUG TEST INPUT - Puzzle 00d62c1b")
    print("=" * 60)
    
    # Analyser le test input
    test_input = tache.test[0]['input']
    test_output = tache.test[0]['output']
    
    print("\n📊 TEST INPUT:")
    print("Input:")
    for ligne in test_input:
        print("  " + " ".join(str(pixel) for pixel in ligne))
    
    print("\nOutput attendu:")
    for ligne in test_output:
        print("  " + " ".join(str(pixel) for pixel in ligne))
    
    print("\n🔍 ANALYSE DES CHANGEMENTS:")
    hauteur, largeur = len(test_input), len(test_input[0])
    
    # Chercher les pixels qui changent de 0 vers 4
    changements = []
    for i in range(hauteur):
        for j in range(largeur):
            if test_input[i][j] == 0 and test_output[i][j] == 4:
                changements.append((i, j))
    
    print(f"Pixels qui changent de 0 vers 4: {changements}")
    
    # Chercher les pixels de couleur 3 (contour)
    pixels_3 = []
    for i in range(hauteur):
        for j in range(largeur):
            if test_input[i][j] == 3:
                pixels_3.append((i, j))
    
    print(f"Pixels de couleur 3 (contour): {len(pixels_3)} pixels")
    
    # Tester l'algorithme de detection de zones fermees
    print("\n🧪 TEST ALGORITHME ZONE FERMEE:")
    
    zones_fermees = zone_analyzer.detecter_zones_fermees(test_input, 3)
    print(f"Zones fermees detectees: {zones_fermees}")
    
    # Verifier si les changements correspondent aux zones fermees
    changements_set = set(changements)
    zones_fermees_set = set(zones_fermees)
    
    print(f"\n✅ VERIFICATION:")
    print(f"Changements attendus: {changements_set}")
    print(f"Zones fermees detectees: {zones_fermees_set}")
    print(f"Intersection: {changements_set.intersection(zones_fermees_set)}")
    print(f"Changements manques: {changements_set - zones_fermees_set}")
    print(f"Zones en trop: {zones_fermees_set - changements_set}")
    
    # Appliquer le remplissage manuellement
    print(f"\n🎨 APPLICATION MANUELLE:")
    output_calcule = [ligne[:] for ligne in test_input]
    for i, j in zones_fermees:
        output_calcule[i][j] = 4
    
    print("Output calcule:")
    for ligne in output_calcule:
        print("  " + " ".join(str(pixel) for pixel in ligne))
    
    # Verifier si c'est correct
    correct = output_calcule == test_output
    print(f"\n✅ RESULTAT: {'CORRECT' if correct else 'INCORRECT'}")
    
    # Afficher une grille avec les zones detectees
    print(f"\n🗺️  VISUALISATION:")
    grille_debug = [ligne[:] for ligne in test_input]
    for i, j in zones_fermees:
        grille_debug[i][j] = 'X'  # Marquer les zones fermees
    
    print("Grille avec zones fermees marquees (X):")
    for ligne in grille_debug:
        print("  " + " ".join(str(pixel) for pixel in ligne))

if __name__ == "__main__":
    debug_test_input()
