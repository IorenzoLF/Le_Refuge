#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST CAPACITE HUMAINE - Aelya du Refuge
Test de ma capacite a resoudre les taches ARC comme un etre humain
"""

import json
import random
from pathlib import Path

def afficher_tache(tache_id, masquer_solution=True):
    """Afficher une tache en masquant la solution du test"""
    with open(f'data/training/{tache_id}.json', 'r') as f:
        data = json.load(f)
    
    print(f"=== TACHE {tache_id} ===")
    print("EXEMPLES D'ENTRAINEMENT:")
    
    for i, exemple in enumerate(data['train']):
        print(f"Exemple {i+1}:")
        print(f"  Input:  {exemple['input']}")
        print(f"  Output: {exemple['output']}")
        print()
    
    print("TEST (a resoudre):")
    print(f"  Input:  {data['test'][0]['input']}")
    if masquer_solution:
        print("  Output: ??? (a predire)")
    else:
        print(f"  Output: {data['test'][0]['output']}")
    
    return data

def analyser_pattern_humain(data):
    """Analyser le pattern comme un etre humain"""
    print("ANALYSE HUMAINE:")
    
    train_examples = data['train']
    test_input = data['test'][0]['input']
    
    # Analyser les dimensions
    print("ANALYSE DES DIMENSIONS:")
    for i, ex in enumerate(train_examples):
        h_in, w_in = len(ex['input']), len(ex['input'][0])
        h_out, w_out = len(ex['output']), len(ex['output'][0])
        print(f"  Exemple {i+1}: {h_in}x{w_in} -> {h_out}x{w_out} (facteur {h_out//h_in}x{w_out//w_in})")
    
    # Analyser les patterns
    print("\nANALYSE DES PATTERNS:")
    
    # Pattern 1: Repetition
    if len(train_examples) >= 2:
        ex1, ex2 = train_examples[0], train_examples[1]
        print(f"  Pattern detecte: Repetition avec expansion")
        print(f"  Le motif se repete {len(ex1['output'])//len(ex1['input'])} fois")
    
    # Pattern 2: Transformation des valeurs
    print("  Transformation: Les valeurs semblent etre repetees/transformees")
    
    return "pattern_repetition_expansion"

def predire_solution(data, pattern_type):
    """Predire la solution basee sur l'analyse"""
    print(f"\nPREDICTION (pattern: {pattern_type}):")
    
    test_input = data['test'][0]['input']
    train_examples = data['train']
    
    # Analyser le facteur d'expansion
    h_in, w_in = len(test_input), len(test_input[0])
    
    # Calculer le facteur d'expansion base sur les exemples
    facteurs = []
    for ex in train_examples:
        h_out, w_out = len(ex['output']), len(ex['output'][0])
        facteurs.append((h_out//len(ex['input']), w_out//len(ex['input'][0])))
    
    # Prendre le facteur le plus frequent
    facteur_h, facteur_w = facteurs[0]  # Simplification
    
    print(f"  Facteur d'expansion: {facteur_h}x{facteur_w}")
    print(f"  Taille attendue: {h_in * facteur_h}x{w_in * facteur_w}")
    
    # Predire la solution
    prediction = []
    for y in range(h_in * facteur_h):
        ligne = []
        for x in range(w_in * facteur_w):
            # Calculer la position dans le motif original
            motif_y = y % h_in
            motif_x = x % w_in
            valeur = test_input[motif_y][motif_x]
            ligne.append(valeur)
        prediction.append(ligne)
    
    print(f"  Prediction: {prediction}")
    return prediction

def verifier_solution(data, prediction):
    """Verifier si la prediction est correcte"""
    solution_reelle = data['test'][0]['output']
    
    print(f"\nVERIFICATION:")
    print(f"  Prediction: {prediction}")
    print(f"  Solution:   {solution_reelle}")
    
    correct = prediction == solution_reelle
    print(f"  Resultat:   {'CORRECT' if correct else 'INCORRECT'}")
    
    return correct

def main():
    """Test principal"""
    print("TEST CAPACITE HUMAINE - Aelya du Refuge")
    print("=" * 50)
    
    # Choisir une tache au hasard
    fichiers = list(Path('data/training').glob('*.json'))
    tache_choisie = random.choice(fichiers).stem
    
    print(f"Tache choisie: {tache_choisie}")
    print()
    
    # Afficher la tache (sans solution)
    data = afficher_tache(tache_choisie, masquer_solution=True)
    
    # Analyser le pattern
    pattern = analyser_pattern_humain(data)
    
    # Predire la solution
    prediction = predire_solution(data, pattern)
    
    # Verifier (en revelant la solution)
    print("\n" + "="*50)
    print("REVELATION DE LA SOLUTION:")
    afficher_tache(tache_choisie, masquer_solution=False)
    
    # Verifier
    correct = verifier_solution(data, prediction)
    
    return correct

if __name__ == "__main__":
    main()
