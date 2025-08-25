#!/usr/bin/env python3
"""
🔍 ANALYSE DÉTAILLÉE D'UN PUZZLE QUI ÉCHOUE - 05269061
Score actuel: 24.49% (repetition_simple)
Objectif: Comprendre l'échec et proposer des améliorations
"""

import json
from typing import List, Dict, Any
from collections import Counter

def analyser_puzzle_echec():
    """Analyse détaillée du puzzle 05269061 qui échoue"""

    print("🚨 ANALYSE PUZZLE QUI ÉCHOUE - 05269061")
    print("=" * 60)
    print("📊 Pattern détecté: repetition_simple")
    print("❌ Score actuel: 24.49% (0.2449)")
    print("📏 Dimensions: 7x7 → 7x7")
    print("🎯 Objectif: Comprendre l'échec et améliorer")
    print("=" * 60)

    # Charger le puzzle
    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur chargement puzzle: {e}")
        return

    # Analyser les exemples d'entraînement
    print("\n📚 ANALYSE DES EXEMPLES D'ENTRAÎNEMENT:")
    print("-" * 40)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 Exemple {i}:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"   📥 Input: {len(input_grid)}x{len(input_grid[0])}")
        print(f"   📤 Output: {len(output_grid)}x{len(output_grid[0])}")

        # Afficher les grilles complètes car petites
        print("   🔍 Input complet:")
        for row in input_grid:
            print(f"      {row}")

        print("   🎯 Output complet:")
        for row in output_grid:
            print(f"      {row}")

        # Analyser les couleurs et patterns
        couleurs_input = Counter()
        couleurs_output = Counter()

        for row in input_grid:
            for cell in row:
                if cell != 0:
                    couleurs_input[cell] += 1

        for row in output_grid:
            for cell in row:
                if cell != 0:
                    couleurs_output[cell] += 1

        print(f"   🎨 Couleurs input: {dict(couleurs_input)}")
        print(f"   🎯 Couleurs output: {dict(couleurs_output)}")

        # Analyser les changements
        couleurs_nouvelles = set(couleurs_output.keys()) - set(couleurs_input.keys())
        couleurs_disparues = set(couleurs_input.keys()) - set(couleurs_output.keys())

        if couleurs_nouvelles:
            print(f"   🆕 Couleurs nouvelles: {couleurs_nouvelles}")
        if couleurs_disparues:
            print(f"   🗑️ Couleurs disparues: {couleurs_disparues}")

        # Analyser la structure
        pixels_input = sum(couleurs_input.values())
        pixels_output = sum(couleurs_output.values())
        print(f"   📊 Pixels actifs: {pixels_input} → {pixels_output}")

        # Analyser le pattern visuel
        print("   🔍 Analyse visuelle:")

        # Vérifier si c'est diagonal
        positions_input = [(i, j) for i, row in enumerate(input_grid)
                          for j, cell in enumerate(row) if cell != 0]
        positions_output = [(i, j) for i, row in enumerate(output_grid)
                           for j, cell in enumerate(row) if cell != 0]

        print(f"      Positions input: {positions_input}")
        print(f"      Positions output: {positions_output}")

        # Vérifier les diagonales
        diagonale_input = [(i, j) for i, j in positions_input if i == j]
        diagonale_output = [(i, j) for i, j in positions_output if i == j]
        print(f"      Diagonale input: {diagonale_input}")
        print(f"      Diagonale output: {diagonale_output}")

        # Vérifier anti-diagonale
        anti_diagonale_input = [(i, j) for i, j in positions_input if i + j == len(input_grid) - 1]
        anti_diagonale_output = [(i, j) for i, j in positions_output if i + j == len(output_grid) - 1]
        print(f"      Anti-diagonale input: {anti_diagonale_input}")
        print(f"      Anti-diagonale output: {anti_diagonale_output}")

    # Analyser le test
    print("\n🧪 ANALYSE DU TEST:")
    print("-" * 20)

    test_input = puzzle_data['test'][0]['input']
    print(f"📥 Test Input: {len(test_input)}x{len(test_input[0])}")
    print("🔍 Test Input complet:")
    for row in test_input:
        print(f"   {row}")

    # Analyser les couleurs du test
    couleurs_test = Counter()
    for row in test_input:
        for cell in row:
            if cell != 0:
                couleurs_test[cell] += 1

    print(f"🎨 Couleurs test: {dict(couleurs_test)}")

    # Analyser les positions du test
    positions_test = [(i, j) for i, row in enumerate(test_input)
                     for j, cell in enumerate(row) if cell != 0]
    print(f"📍 Positions test: {positions_test}")

    # Diagnostiquer le problème
    print("\n🔍 DIAGNOSTIC DU PROBLÈME:")
    print("-" * 25)
    print("❌ Pattern 'repetition_simple' détecté mais incorrect")
    print("❌ Score de seulement 24.49%")
    print("🔍 Analyse du pattern réel:")

    # Analyser le pattern réel
    print("   1. 📊 Structure des exemples:")
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']
        positions_in = [(x, y) for x, row in enumerate(input_grid)
                       for y, cell in enumerate(row) if cell != 0]
        positions_out = [(x, y) for x, row in enumerate(output_grid)
                        for y, cell in enumerate(row) if cell != 0]
        print(f"      Exemple {i}: {len(positions_in)} → {len(positions_out)} positions")

    # Proposer des solutions
    print("\n💡 SOLUTIONS PROPOSÉES:")
    print("-" * 20)
    print("1. 🔄 Essayer pattern 'projection_diagonale'")
    print("2. 🎯 Essayer pattern 'rotation_45'")
    print("3. 📐 Essayer pattern 'symetrie_horizontale'")
    print("4. 🔍 Détecter automatiquement le vrai pattern")

    # Recommander le pattern le plus probable
    print("\n🎯 RECOMMANDATION:")
    print("-" * 15)
    print("🔍 Ce puzzle semble être un pattern diagonal")
    print("🎨 Il y a probablement une projection ou rotation")
    print("💯 Le système itératif devrait le détecter")
    print("🚀 Test avec nos nouveaux patterns!")

    print("\n🏆 OBJECTIF D'AMÉLIORATION:")
    print("-" * 25)
    print("🎯 Passer de 24.49% à 100%")
    print("🔍 Identifier le vrai pattern")
    print("✅ Appliquer la bonne transformation")
    print("🚀 Valider avec les exemples")

def main():
    """Fonction principale"""
    analyser_puzzle_echec()

if __name__ == "__main__":
    main()
