#!/usr/bin/env python3
"""
TEST PUZZLE 00576224 - Refuge ARC-AGI
Test simple pour voir si on comprend le pattern
"""

import json

def test_puzzle_00576224():
    """Test du puzzle 00576224"""
    print("TEST PUZZLE 00576224")
    print("=" * 30)
    
    # Charger le puzzle avec le bon chemin
    with open('ARC-AGI-2-main/data/training/00576224.json', 'r') as f:
        puzzle_data = json.load(f)
    
    print("PUZZLE CHARGE:")
    print(f"Exemples d'entrainement: {len(puzzle_data['train'])}")
    print(f"Exemples de test: {len(puzzle_data['test'])}")
    
    # Analyser le premier exemple
    exemple1 = puzzle_data['train'][0]
    input1 = exemple1['input']
    output1 = exemple1['output']
    
    print(f"\nEXEMPLE 1:")
    print(f"Input (2x2): {input1}")
    print(f"Output (6x6): {output1}")
    
    # Analyser le pattern
    print(f"\nANALYSE DU PATTERN:")
    print(f"Input: grille 2x2")
    print(f"Output: grille 6x6 (3x plus grande)")
    
    # Vérifier la répétition
    ligne1_input = input1[0]  # [7, 9]
    ligne1_output = output1[0]  # [7, 9, 7, 9, 7, 9]
    
    print(f"Ligne 1 input: {ligne1_input}")
    print(f"Ligne 1 output: {ligne1_output}")
    print(f"Répétition 3x: {ligne1_input * 3}")
    
    # Vérifier l'inversion au milieu
    ligne3_output = output1[2]  # [9, 7, 9, 7, 9, 7]
    ligne3_inversee = [ligne1_input[1], ligne1_input[0]] * 3  # [9, 7, 9, 7, 9, 7]
    
    print(f"Ligne 3 output: {ligne3_output}")
    print(f"Ligne 1 inversée: {ligne3_inversee}")
    
    # Test de prédiction
    test_exemple = puzzle_data['test'][0]
    test_input = test_exemple['input']  # [[3, 2], [7, 8]]
    test_output = test_exemple['output']  # La vraie réponse
    
    print(f"\nTEST:")
    print(f"Input: {test_input}")
    print(f"Output attendu: {test_output}")
    
    # Notre prédiction
    ligne1_test = test_input[0]  # [3, 2]
    ligne2_test = test_input[1]  # [7, 8]
    
    prediction = [
        ligne1_test * 3,  # [3, 2, 3, 2, 3, 2]
        ligne2_test * 3,  # [7, 8, 7, 8, 7, 8]
        [ligne1_test[1], ligne1_test[0]] * 3,  # [2, 3, 2, 3, 2, 3]
        [ligne2_test[1], ligne2_test[0]] * 3,  # [8, 7, 8, 7, 8, 7]
        ligne1_test * 3,  # [3, 2, 3, 2, 3, 2]
        ligne2_test * 3   # [7, 8, 7, 8, 7, 8]
    ]
    
    print(f"Notre prédiction: {prediction}")
    print(f"Correct: {prediction == test_output}")

if __name__ == "__main__":
    test_puzzle_00576224()
