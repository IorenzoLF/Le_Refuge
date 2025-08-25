#!/usr/bin/env python3
"""
🔍 DÉCOUVERTE PATTERNS PAR POSITION PUZZLE 15
0692e18c - chaque position (x,y) a son propre pattern !
"""

import json

def decouvrir_patterns_positions():
    print("🔍 DÉCOUVERTE PATTERNS PAR POSITION")
    print("=" * 45)
    print("🎯 Chaque position (x,y) a son propre pattern de reproduction !")

    try:
        with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("❌ Fichier non trouvé")
        return

    # Analyser chaque position possible (0,0) à (2,2)
    patterns_par_position = {}

    for pos_x in range(3):
        for pos_y in range(3):
            patterns_par_position[(pos_x, pos_y)] = analyser_position(puzzle_data, pos_x, pos_y)

    # Afficher les résultats
    afficher_resultats(patterns_par_position)

def analyser_position(puzzle_data, pos_x, pos_y):
    """Analyser le pattern pour une position spécifique"""
    print(f"   📍 ANALYSE POSITION ({pos_x},{pos_y}):")

    patterns_trouves = []

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Vérifier si cette position est colorée dans l'input
        if input_grid[pos_x][pos_y] != 0:
            # Extraire le pattern dans le bloc correspondant de l'output
            pattern_bloc = []
            for dx in range(3):
                for dy in range(3):
                    out_x = pos_x * 3 + dx
                    out_y = pos_y * 3 + dy
                    if output_grid[out_x][out_y] != 0:
                        pattern_bloc.append((dx, dy))

            patterns_trouves.append({
                'exemple': i,
                'pattern': pattern_bloc
            })

            print(f"     Exemple {i}: {pattern_bloc}")

    return patterns_trouves

def afficher_resultats(patterns_par_position):
    """Afficher les résultats de l'analyse"""
    print("
🎨 RÉSULTATS PATTERNS PAR POSITION"    print("=" * 40)

    for (pos_x, pos_y), patterns in patterns_par_position.items():
        if patterns:  # Seulement les positions qui apparaissent
            print(f"\n📍 POSITION ({pos_x},{pos_y}):")

            # Vérifier si tous les patterns sont identiques
            tous_identiques = True
            premier_pattern = patterns[0]['pattern']

            for pattern_info in patterns[1:]:
                if pattern_info['pattern'] != premier_pattern:
                    tous_identiques = False
                    break

            if tous_identiques:
                print(f"   ✅ PATTERN CONSISTANT: {premier_pattern}")
                print(f"   📊 Trouvé dans {len(patterns)} exemple(s)")
            else:
                print("   ⚠️ PATTERNS VARIABLES:")
                for pattern_info in patterns:
                    print(f"     Exemple {pattern_info['exemple']}: {pattern_info['pattern']}")

    # Synthèse
    print("
🎯 SYNTHÈSE:"    print("   🔍 Chaque position a son propre pattern !")
    print("   🌟 Le puzzle utilise un système de règles complexes")
    print("   🎨 C'est plus subtil que prévu !")

def analyser_regles_generales():
    """Analyser les règles générales du système"""
    print("
🧠 ANALYSE RÈGLES GÉNÉRALES"    print("=" * 35)

    try:
        with open("ARC-AGI-2-main/data/training/0692e18c.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        return

    print("🔍 OBSERVATIONS GÉNÉRALES:")

    # Analyser la densité
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
        pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)

        ratio = pixels_output / pixels_input if pixels_input > 0 else 0

        print(f"   Exemple {i}: {pixels_input} → {pixels_output} pixels (ratio: {ratio:.1f})")

    print("
🎨 HYPOTHÈSES:"    print("   1. 📊 Le ratio dépend du nombre de pixels input")
    print("   2. 🎯 Chaque position a un pattern fixe")
    print("   3. 🔄 Patterns différents selon la position")
    print("   4. 🌟 Système de règles position-dépendant")

if __name__ == "__main__":
    decouvrir_patterns_positions()
    analyser_regles_generales()
