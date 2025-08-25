#!/usr/bin/env python3
"""
🧪 TEST SIMPLE PROJECTION LIMITÉE
"""

import json
from pattern_projection_limitee_double_forme import detecter_pattern_projection_limitee_double_forme

def test_simple():
    print("🧪 TEST SIMPLE PROJECTION LIMITÉE")

    try:
        with open("ARC-AGI-2-main/data/training/0962bcdd.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print(f"Input: {len(input_grid)}x{len(input_grid[0])}")
    print(f"Output: {len(output_grid)}x{len(output_grid[0])}")

    # Test détection
    detection = detecter_pattern_projection_limitee_double_forme(input_grid, output_grid)

    print(f"Detecte: {detection['detecte']}")
    print(".1f")

    if detection['detecte']:
        print(f"Pattern: {detection['pattern']}")
        print(f"Couleurs: {detection['couleurs_sequence']}")
        print(f"Formes: {len(detection['formes_detectees'])}")
        print("SUCCES! Pattern fonctionne!")

if __name__ == "__main__":
    test_simple()
