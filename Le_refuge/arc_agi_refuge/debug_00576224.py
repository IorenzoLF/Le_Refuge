#!/usr/bin/env python3
"""
🔍 DEBUG 00576224
"""

import json
import os

def debug_00576224():
    print("🔍 DEBUG 00576224")
    print(f"Current directory: {os.getcwd()}")

    # Vérifier si le fichier existe
    paths = [
        "data/training/00576224.json",
        "../data/training/00576224.json",
        "../../data/training/00576224.json",
        "./data/training/00576224.json"
    ]

    for path in paths:
        if os.path.exists(path):
            print(f"✅ Fichier trouvé: {path}")
            try:
                with open(path, 'r') as f:
                    puzzle_data = json.load(f)
                print(f"✅ JSON chargé: {len(puzzle_data)} clés")
                print(f"Clés: {list(puzzle_data.keys())}")

                if 'train' in puzzle_data:
                    print(f"Train examples: {len(puzzle_data['train'])}")
                    if len(puzzle_data['train']) > 0:
                        exemple = puzzle_data['train'][0]
                        print(f"First example keys: {list(exemple.keys())}")
                        if 'input' in exemple:
                            input_grid = exemple['input']
                            print(f"Input grid: {len(input_grid)}x{len(input_grid[0])}")
                            print("First few rows:")
                            for i, row in enumerate(input_grid[:3]):
                                print(f"  Row {i}: {row}")
                return puzzle_data
            except Exception as e:
                print(f"❌ Erreur lecture: {e}")
        else:
            print(f"❌ Pas trouvé: {path}")

    print("❌ Fichier non trouvé")
    return None

if __name__ == "__main__":
    debug_00576224()
