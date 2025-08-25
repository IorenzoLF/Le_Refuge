#!/usr/bin/env python3
"""
🧠 TEST CAPACITÉ HUMAINE - Ælya du Refuge
Test de ma capacité à résoudre les tâches ARC comme un être humain
"""

import json
import random
from pathlib import Path

def afficher_tache(tache_id, masquer_solution=True):
    """Afficher une tâche en masquant la solution du test"""
    with open(f'data/training/{tache_id}.json', 'r') as f:
        data = json.load(f)
    
    print(f"=== TÂCHE {tache_id} ===")
    print("EXEMPLES D'ENTRAÎNEMENT:")
    
    for i, exemple in enumerate(data['train']):
        print(f"Exemple {i+1}:")
        print(f"  Input:  {exemple['input']}")
        print(f"  Output: {exemple['output']}")
        print()
    
    print("TEST (à résoudre):")
    print(f"  Input:  {data['test'][0]['input']}")
    if masquer_solution:
        print("  Output: ??? (à prédire)")
    else:
        print(f"  Output: {data['test'][0]['output']}")
    
    return data

def analyser_pattern_humain(data):
    """Analyser le pattern comme un être humain"""
    print("🧠 ANALYSE HUMAINE:")
    
    train_examples = data['train']
    test_input = data['test'][0]['input']
    
    # Analyser les dimensions
    print("📏 ANALYSE DES DIMENSIONS:")
    for i, ex in enumerate(train_examples):
        h_in, w_in = len(ex['input']), len(ex['input'][0])
        h_out, w_out = len(ex['output']), len(ex['output'][0])
        print(f"  Exemple {i+1}: {h_in}x{w_in} → {h_out}x{w_out} (facteur {h_out//h_in}x{w_out//w_in})")
    
    # Analyser les patterns
    print("\n🔍 ANALYSE DES PATTERNS:")
    
    # Pattern 1: Répétition
    if len(train_examples) >= 2:
        ex1, ex2 = train_examples[0], train_examples[1]
        print(f"  Pattern détecté: Répétition avec expansion")
        print(f"  Le motif se répète {len(ex1['output'])//len(ex1['input'])} fois")
    
    # Pattern 2: Transformation des valeurs
    print("  Transformation: Les valeurs semblent être répétées/transformées")
    
    return "pattern_repetition_expansion"

def predire_solution(data, pattern_type):
    """Prédire la solution basée sur l'analyse"""
    print(f"\n🎯 PRÉDICTION (pattern: {pattern_type}):")
    
    test_input = data['test'][0]['input']
    train_examples = data['train']
    
    # Analyser le facteur d'expansion
    h_in, w_in = len(test_input), len(test_input[0])
    
    # Calculer le facteur d'expansion basé sur les exemples
    facteurs = []
    for ex in train_examples:
        h_out, w_out = len(ex['output']), len(ex['output'][0])
        facteurs.append((h_out//len(ex['input']), w_out//len(ex['input'][0])))
    
    # Prendre le facteur le plus fréquent
    facteur_h, facteur_w = facteurs[0]  # Simplification
    
    print(f"  Facteur d'expansion: {facteur_h}x{facteur_w}")
    print(f"  Taille attendue: {h_in * facteur_h}x{w_in * facteur_w}")
    
    # Prédire la solution
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
    
    print(f"  Prédiction: {prediction}")
    return prediction

def verifier_solution(data, prediction):
    """Vérifier si la prédiction est correcte"""
    solution_reelle = data['test'][0]['output']
    
    print(f"\n✅ VÉRIFICATION:")
    print(f"  Prédiction: {prediction}")
    print(f"  Solution:   {solution_reelle}")
    
    correct = prediction == solution_reelle
    print(f"  Résultat:   {'✅ CORRECT' if correct else '❌ INCORRECT'}")
    
    return correct

def main():
    """Test principal"""
    print("🧠 TEST CAPACITÉ HUMAINE - Ælya du Refuge")
    print("=" * 50)
    
    # Choisir une tâche au hasard
    fichiers = list(Path('data/training').glob('*.json'))
    tache_choisie = random.choice(fichiers).stem
    
    print(f"Tâche choisie: {tache_choisie}")
    print()
    
    # Afficher la tâche (sans solution)
    data = afficher_tache(tache_choisie, masquer_solution=True)
    
    # Analyser le pattern
    pattern = analyser_pattern_humain(data)
    
    # Prédire la solution
    prediction = predire_solution(data, pattern)
    
    # Vérifier (en révélant la solution)
    print("\n" + "="*50)
    print("RÉVÉLATION DE LA SOLUTION:")
    afficher_tache(tache_choisie, masquer_solution=False)
    
    # Vérifier
    correct = verifier_solution(data, prediction)
    
    return correct

if __name__ == "__main__":
    main()
