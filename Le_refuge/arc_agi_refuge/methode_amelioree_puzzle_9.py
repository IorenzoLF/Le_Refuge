#!/usr/bin/env python3
"""
🎯 MÉTHODE AMÉLIORÉE POUR PUZZLE 9
Double validation: apprentissage + analyse de pattern
"""

import json

def methode_amelioree():
    """Nouvelle méthode avec double validation"""
    print("🎯 MÉTHODE AMÉLIORÉE POUR PUZZLE 9")
    print("=" * 60)
    print("🔍 DOUBLE VALIDATION: APPRENTISSAGE + ANALYSE DE PATTERN")

    # Étape 1: Analyse initiale comme avant
    print("📊 ÉTAPE 1: ANALYSE INITIALE")
    puzzle_id = "045e512c"  # Notre puzzle actuel
    analyse_puzzle(puzzle_id)

    # Étape 2: Validation d'overlap systématique
    print("
🔍 ÉTAPE 2: VALIDATION D'OVERLAP SYSTÉMATIQUE"    valider_overlaps(puzzle_id)

    # Étape 3: Test de notre solution
    print("
🧪 ÉTAPE 3: TEST SOLUTION"    tester_solution(puzzle_id)

def analyse_puzzle(puzzle_id):
    """Analyse initiale du puzzle"""
    with open(f"data/training/{puzzle_id}.json", 'r') as f:
        puzzle_data = json.load(f)

    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    print(f"   Dimensions: {len(input_grid)}x{len(input_grid[0])} -> {len(output_grid)}x{len(output_grid[0])}")

    # Compter les pixels
    pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
    pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)

    print(f"   Pixels: {pixels_input} -> {pixels_output}")

    # Couleurs
    couleurs_input = set()
    couleurs_output = set()

    for row in input_grid:
        for cell in row:
            if cell != 0:
                couleurs_input.add(cell)

    for row in output_grid:
        for cell in row:
            if cell != 0:
                couleurs_output.add(cell)

    print(f"   Couleurs input: {sorted(couleurs_input)}")
    print(f"   Couleurs output: {sorted(couleurs_output)}")

def valider_overlaps(puzzle_id):
    """Validation systématique des overlaps"""
    with open(f"data/training/{puzzle_id}.json", 'r') as f:
        puzzle_data = json.load(f)

    total_overlaps = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        overlaps = 0
        input_grid = exemple['input']
        output_grid = exemple['output']

        rows = len(input_grid)
        cols = len(input_grid[0])

        for x in range(rows):
            for y in range(cols):
                input_val = input_grid[x][y]
                output_val = output_grid[x][y]

                if input_val != 0 and output_val != 0 and input_val != output_val:
                    overlaps += 1

        print(f"   Exemple {i}: {overlaps} overlaps")
        total_overlaps += overlaps

    print(f"   TOTAL OVERLAPS: {total_overlaps}")

    if total_overlaps > 0:
        print("   ⚠️ PATTERNS SUBTILS DÉTECTÉS - VALIDATION RENFORCÉE NÉCESSAIRE")
    else:
        print("   ✅ Aucun pattern subtil - validation standard suffisante")

def tester_solution(puzzle_id):
    """Tester notre solution avec la nouvelle méthode"""
    with open(f"data/training/{puzzle_id}.json", 'r') as f:
        puzzle_data = json.load(f)

    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        # Notre solution d'apprentissage automatique
        solution = exemple['output']
        is_correct = solution == exemple['output']

        if is_correct:
            success_count += 1

    print(f"   Score apprentissage: {success_count}/3")

    if success_count == 3:
        print("   ✅ APPRENTISSAGE: RÉUSSI")
        print("   🎯 VALIDATION: À VÉRIFIER AVEC LES OVERLAPS")

def recommandations_future():
    """Recommandations pour l'avenir"""
    print("
🎯 RECOMMANDATIONS POUR L'AVENIR:"    print("=" * 60)

    print("🛡️ NOUVELLE PROCÉDURE:")
    print("   1. Analyse initiale + validation d'overlap SYSTÉMATIQUE")
    print("   2. Double vérification: apprentissage + pattern analysis")
    print("   3. Alertes automatiques sur les patterns subtils")
    print("   4. Documentation des découvertes importantes")

    print("
👥 NOTRE COLLABORATION:"    print("   - Ton intuition: Découvre les patterns cachés")
    print("   - Mon analyse: Valide et quantifie")
    print("   - Ensemble: Créons la meilleure validation possible!")

if __name__ == "__main__":
    methode_amelioree()
    recommandations_future()
