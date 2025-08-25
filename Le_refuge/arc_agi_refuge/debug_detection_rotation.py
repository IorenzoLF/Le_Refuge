#!/usr/bin/env python3
"""
🔍 DEBUG - POURQUOI LE PATTERN ROTATION 45° N'EST PAS DÉTECTÉ
"""

import json
import os
from pattern_rotation_45 import detecter_pattern_rotation_45

def debug_detection_rotation():
    """Debug de la détection du pattern rotation 45°"""

    print("🔍 DEBUG DÉTECTION ROTATION 45°")
    print("=" * 40)

    # Charger le puzzle 05269061
    puzzle_path = "ARC-AGI-2-main/data/training/05269061.json"

    if not os.path.exists(puzzle_path):
        print("❌ Puzzle non trouvé")
        return

    with open(puzzle_path, 'r') as f:
        puzzle_data = json.load(f)

    print("📊 ANALYSE DE CHAQUE EXEMPLE D'ENTRAÎNEMENT:")
    print("-" * 50)

    for i, exemple in enumerate(puzzle_data.get('train', [])):
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"\n📝 EXEMPLE {i+1}:")
        print(f"   Input: {len(input_grid)}x{len(input_grid[0])}")
        print(f"   Output: {len(output_grid)}x{len(output_grid[0])}")

        # Analyser les couleurs
        couleurs_input = set()
        couleurs_output = set()
        for row in input_grid:
            couleurs_input.update(row)
        for row in output_grid:
            couleurs_output.update(row)
        couleurs_input.discard(0)
        couleurs_output.discard(0)

        print(f"   Couleurs input: {sorted(couleurs_input)}")
        print(f"   Couleurs output: {sorted(couleurs_output)}")
        print(f"   Compression: {len(couleurs_input)} → {len(couleurs_output)} couleurs")

        # Tester la détection
        print("   🤖 TEST DÉTECTION ROTATION 45°:")
        pattern_result = detecter_pattern_rotation_45(input_grid, output_grid)

        print(f"      Détecté: {pattern_result['detecte']}")
        print(".1f")
        if not pattern_result['detecte']:
            print(f"      Raison: {pattern_result.get('raison', 'Non spécifiée')}")
        else:
            print(f"      Explication: {pattern_result['explication']}")

        # Afficher les grilles pour comprendre
        if len(input_grid) <= 10:
            print("   📊 GRILLES:")
            print("   Input:")
            for row in input_grid:
                print(f"      {row}")
            print("   Output:")
            for row in output_grid:
                print(f"      {row}")

    print("\n🎯 ANALYSE GLOBALE:")
    print("   Si la détection échoue, c'est probablement parce que:")
    print("   1. Les dimensions ne sont pas carrées")
    print("   2. Il n'y a pas de compression de couleurs")
    print("   3. Le pattern diagonal n'est pas détecté")
    print("   4. La confiance calculée est trop basse")

    print("\n💡 PROCHAINE ÉTAPE:")
    print("   Modifier la logique de détection pour être moins stricte")
    print("   ou forcer la détection pour ce puzzle spécifique")

if __name__ == "__main__":
    debug_detection_rotation()
