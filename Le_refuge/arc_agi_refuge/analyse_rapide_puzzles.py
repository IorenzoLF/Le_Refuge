#!/usr/bin/env python3
"""
📊 ANALYSE RAPIDE DES PUZZLES SPÉCIFIQUES
"""

import json

def analyser_puzzle_0962bcdd():
    print("🎯 ANALYSE 0962bcdd - 83.33% (réussi)")
    print("=" * 40)

    try:
        with open("ARC-AGI-2-main/data/training/0962bcdd.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    print(f"📏 Dimensions: {len(puzzle_data['train'][0]['input'])}x{len(puzzle_data['train'][0]['input'][0])}")

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        couleurs_in = set()
        couleurs_out = set()

        for row in input_grid:
            for cell in row:
                if cell != 0:
                    couleurs_in.add(cell)

        for row in output_grid:
            for cell in row:
                if cell != 0:
                    couleurs_out.add(cell)

        print(f"Exemple {i}: {sorted(couleurs_in)} → {sorted(couleurs_out)}")

def analyser_puzzle_05a7bcf2():
    print("\n🎯 ANALYSE 05a7bcf2 - 76.89% (échoué)")
    print("=" * 40)

    try:
        with open("ARC-AGI-2-main/data/training/05a7bcf2.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    print(f"📏 Dimensions: {len(puzzle_data['train'][0]['input'])}x{len(puzzle_data['train'][0]['input'][0])}")

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        couleurs_in = set()
        couleurs_out = set()

        for row in input_grid:
            for cell in row:
                if cell != 0:
                    couleurs_in.add(cell)

        for row in output_grid:
            for cell in row:
                if cell != 0:
                    couleurs_out.add(cell)

        print(f"Exemple {i}: {sorted(couleurs_in)} → {sorted(couleurs_out)}")

def main():
    analyser_puzzle_0962bcdd()
    analyser_puzzle_05a7bcf2()

    print("\n📊 RÉSULTATS DES RÉSULTATS EXISTANTS:")
    print("   ✅ 0962bcdd: 83.33% avec repetition_simple")
    print("   ❌ 05a7bcf2: 76.89% avec repetition_simple")
    print("\n💡 ANALYSE:")
    print("   📈 0962bcdd: Score correct, stable")
    print("   🔧 05a7bcf2: Score moyen, améliorable")
    print("   🎯 Les deux utilisent repetition_simple")

if __name__ == "__main__":
    main()
