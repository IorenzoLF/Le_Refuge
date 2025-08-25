#!/usr/bin/env python3
"""
🔍 ANALYSE DÉTAILLÉE DU PATTERN 007bbfb7
"""

import json

def analyser_pattern_007bbfb7():
    print("🔍 ANALYSE DÉTAILLÉE PATTERN 007bbfb7")
    print("=" * 50)

    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser chaque exemple en détail
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i} - ANALYSE DÉTAILLÉE:")
        analyser_exemple_detaille(exemple, i)

    # Analyser les patterns globaux
    analyser_patterns_globaux(puzzle_data)

def analyser_exemple_detaille(exemple, num):
    """Analyse détaillée d'un exemple"""
    input_grid = exemple['input']
    output_grid = exemple['output']

    print(f"  📥 INPUT 3x3:")
    for i, row in enumerate(input_grid):
        print(f"    {row}")
        # Analyser les positions non-zéro
        non_zero = [(j, cell) for j, cell in enumerate(row) if cell != 0]
        if non_zero:
            print(f"      Non-zéro: {non_zero}")

    print(f"  📤 OUTPUT 9x9:")
    for i, row in enumerate(output_grid):
        print(f"    {row}")

    # Analyser les patterns de répétition
    analyser_repetitions(input_grid, output_grid)

    # Analyser les changements
    analyser_changements_detaille(input_grid, output_grid)

def analyser_repetitions(input_grid, output_grid):
    """Analyse les patterns de répétition"""
    print("  🔄 PATTERNS DE RÉPÉTITION:")

    # Extraire les valeurs uniques de l'input
    valeurs_input = set()
    for row in input_grid:
        for cell in row:
            if cell != 0:
                valeurs_input.add(cell)

    print(f"    Valeurs input: {sorted(valeurs_input)}")

    # Voir comment chaque valeur est répétée dans l'output
    for valeur in sorted(valeurs_input):
        positions_output = []
        for i, row in enumerate(output_grid):
            for j, cell in enumerate(row):
                if cell == valeur:
                    positions_output.append((i, j))

        print(f"    {valeur} apparaît {len(positions_output)} fois aux positions: {positions_output}")

def analyser_changements_detaille(input_grid, output_grid):
    """Analyse détaillée des changements"""
    print("  🔄 ANALYSE DES CHANGEMENTS:")

    changements = []
    for x in range(len(input_grid)):
        for y in range(len(input_grid[0])):
            if input_grid[x][y] != 0:  # Seulement les positions non-zéro de l'input
                input_val = input_grid[x][y]

                # Voir comment cette valeur est transformée dans l'output
                # Les valeurs de l'input 3x3 sont mappées vers des zones 3x3 dans l'output 9x9
                start_i, start_j = x * 3, y * 3
                zone_3x3 = []
                for i in range(3):
                    for j in range(3):
                        val = output_grid[start_i + i][start_j + j]
                        zone_3x3.append(val)

                print(f"    Position input ({x},{y})={input_val} -> Zone 3x3: {zone_3x3}")

                # Vérifier si la valeur a changé
                if input_val not in zone_3x3:
                    changements.append({
                        'pos_input': (x, y),
                        'valeur_input': input_val,
                        'zone_output': zone_3x3
                    })

    if changements:
        print(f"    ⚠️  {len(changements)} changements détectés:")
        for change in changements:
            print(f"       Input ({change['pos_input'][0]},{change['pos_input'][1]})={change['valeur_input']} -> {change['zone_output']}")
    else:
        print("    ✅ Aucune modification des valeurs")

def analyser_patterns_globaux(puzzle_data):
    """Analyse des patterns globaux"""
    print("
🌐 ANALYSE DES PATTERNS GLOBAUX:"    exemples = puzzle_data['train']

    # Analyser les correspondances valeur -> pattern
    valeur_patterns = {}

    for i, exemple in enumerate(exemples):
        input_grid = exemple['input']
        output_grid = exemple['output']

        for x in range(3):
            for y in range(3):
                input_val = input_grid[x][y]
                if input_val != 0:
                    start_i, start_j = x * 3, y * 3
                    pattern = []
                    for i in range(3):
                        for j in range(3):
                            pattern.append(output_grid[start_i + i][start_j + j])

                    if input_val not in valeur_patterns:
                        valeur_patterns[input_val] = []
                    valeur_patterns[input_val].append(pattern)

    # Afficher les patterns par valeur
    for valeur in sorted(valeur_patterns.keys()):
        print(f"\n🎨 VALEUR {valeur}:")
        patterns = valeur_patterns[valeur]
        print(f"   Nombre d'occurrences: {len(patterns)}")

        # Vérifier si les patterns sont identiques
        if len(set(tuple(p) for p in patterns)) == 1:
            print(f"   ✅ Pattern cohérent: {patterns[0]}")
        else:
            print("   ⚠️  Patterns différents:"            for i, pattern in enumerate(patterns):
                print(f"      Pattern {i+1}: {pattern}")

def analyser_test():
    """Analyser l'exemple de test"""
    print("
🧪 ANALYSE EXEMPLE DE TEST:"    with open("data/training/007bbfb7.json", 'r') as f:
        puzzle_data = json.load(f)

    test_input = puzzle_data['test'][0]['input']
    print("TEST INPUT:")
    for row in test_input:
        print(f"  {row}")

    # Analyser les valeurs du test
    valeurs_test = set()
    for row in test_input:
        for cell in row:
            if cell != 0:
                valeurs_test.add(cell)

    print(f"Valeurs à traiter: {sorted(valeurs_test)}")

if __name__ == "__main__":
    analyser_pattern_007bbfb7()
    analyser_test()
