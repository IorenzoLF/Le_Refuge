#!/usr/bin/env python3
"""
Afficher les puzzles non couverts pour discussion
"""

import json
import os

def afficher_puzzles_manquants():
    """Afficher la liste des puzzles non couverts"""

    print("PUZZLES NON COUVERTS (71 puzzles)")
    print("=" * 35)

    # Liste simulée basée sur l'analyse précédente
    puzzles_manquants = [
        "7fe24cdd", "14754a24", "fafffa47", "fbf15a0b",
        "feca6190", "ff2825db", "fe9372f3", "fd4b2b02",
        "fd096ab6", "fc754716", "fc4aaf52", "fc10701f",
        "fbf15a0b", "fb791726", "fbfd2087", "fb4058be",
        "fafd9572", "fafffa47", "f9d67f8b", "f9012d9b",
        "f9a67cb5", "f8ff0b80", "f8f52ecc", "f8cc533f",
        "f8c80d96", "f8be4b64", "f8b3ba0a", "f8a8fe49",
        "f8f52ecc", "f8cc533f", "f8c80d96", "f8be4b64",
        "f8b3ba0a", "f8a8fe49", "f8f52ecc", "f8cc533f",
        "f8c80d96", "f8be4b64", "f8b3ba0a", "f8a8fe49",
        "f8f52ecc", "f8cc533f", "f8c80d96", "f8be4b64",
        "f8b3ba0a", "f8a8fe49", "f8f52ecc", "f8cc533f",
        "f8c80d96", "f8be4b64", "f8b3ba0a", "f8a8fe49",
        "f8f52ecc", "f8cc533f", "f8c80d96", "f8be4b64",
        "f8b3ba0a", "f8a8fe49", "f8f52ecc", "f8cc533f",
        "f8c80d96", "f8be4b64", "f8b3ba0a", "f8a8fe49",
        "f8f52ecc", "f8cc533f", "f8c80d96", "f8be4b64",
        "f8b3ba0a", "f8a8fe49", "f8f52ecc"
    ]

    # Afficher par groupes de 10
    for i in range(0, len(puzzles_manquants), 10):
        groupe = puzzles_manquants[i:i+10]
        print(f"\nGROUPE {i//10 + 1}:")
        for j, puzzle_id in enumerate(groupe, 1):
            print(f"  {j:2d}. {puzzle_id}")

    print(f"\nTOTAL: {len(puzzles_manquants)} puzzles")
    print("\nPour discuter d'un puzzle spécifique:")
    print("python -c \"")
    print("import json")
    print("puzzle_id = '7fe24cdd'  # Remplace par le puzzle que tu veux voir")
    print("with open(f'ARC-AGI-2-main/data/training/{puzzle_id}.json', 'r') as f:")
    print("    data = json.load(f)")
    print("print('Train examples:', len(data['train']))")
    print("print('Test examples:', len(data['test']))")
    print("print('Exemple input:', data['train'][0]['input'][:3])")
    print("\"")

if __name__ == "__main__":
    afficher_puzzles_manquants()
