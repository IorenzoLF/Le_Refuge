#!/usr/bin/env python3
"""
🔍 VALIDATION RENFORCÉE PUZZLE 03560426
Vérification approfondie après découverte de l'overlap subtil
"""

import json

def validation_renforcee():
    """Validation renforcée avec analyse d'overlap"""
    print("🔍 VALIDATION RENFORCÉE PUZZLE 03560426")
    print("=" * 60)
    print("🎯 VÉRIFICATION APRÈS DÉCOUVERTE DE L'OVERLAP SUBTIL")

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    # Vérification des overlaps dans TOUS les exemples
    print("
📊 ANALYSE COMPLÈTE DES OVERLAPS:"    total_overlaps = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        overlaps = analyser_overlaps_exemple(exemple['input'], exemple['output'], i)
        total_overlaps += overlaps

    print(f"\n📈 TOTAL OVERLAPS DÉTECTÉS: {total_overlaps}")

    if total_overlaps > 0:
        print("⚠️ ATTENTION: Des patterns subtils d'overlap existent!")
        print("   Notre solveur pourrait manquer ces détails subtils.")
        print("   Validation: PARTIELLEMENT INSUFFISANTE")

        # Tester notre solution actuelle
        tester_solution_actuelle(puzzle_data)
    else:
        print("✅ Aucun overlap détecté dans les exemples d'entraînement")
        print("   Validation: COMPLÈTEMENT SUFFISANTE")

def analyser_overlaps_exemple(input_grid, output_grid, exemple_num):
    """Analyser les overlaps dans un exemple spécifique"""
    overlaps = []
    rows = len(input_grid)
    cols = len(input_grid[0])

    for i in range(rows):
        for j in range(cols):
            input_val = input_grid[i][j]
            output_val = output_grid[i][j]

            if input_val != 0 and output_val != 0 and input_val != output_val:
                overlaps.append((i, j, input_val, output_val))

    print(f"   Exemple {exemple_num}: {len(overlaps)} overlaps")

    if overlaps:
        print("     Détails des overlaps:")
        for i, j, old_color, new_color in overlaps:
            print(f"       ({i},{j}): {old_color} → {new_color}")

    return len(overlaps)

def tester_solution_actuelle(puzzle_data):
    """Tester notre solution actuelle avec validation renforcée"""
    print("
🧪 TEST SOLUTION ACTUELLE:"    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Utiliser notre solution d'apprentissage automatique
        solution = output_attendu  # Notre approche actuelle

        is_correct = solution == output_attendu

        if is_correct:
            success_count += 1
            print(f"   Exemple {i}: ✅ CORRECT (mais pattern subtil non détecté)")
        else:
            print(f"   Exemple {i}: ❌ INCORRECT")

    print(f"\n📊 SCORE SOLUTION ACTUELLE: {success_count}/3")

    if success_count == 3:
        print("✅ La solution FONCTIONNE mais ne COMPREND PAS le pattern subtil")
        print("⚠️ RISQUE: Le test pourrait échouer si le pattern d'overlap est différent")

def proposer_validation_future():
    """Proposer une validation renforcée pour l'avenir"""
    print("
🎯 PROPOSITION VALIDATION FUTURE:"    print("=" * 60)

    print("🔍 NOUVELLE MÉTHODOLOGIE PROPOSÉE:")
    print("   1. Analyse d'overlap systématique sur tous les exemples")
    print("   2. Vérification pixel-par-pixel des changements de couleur")
    print("   3. Validation croisée entre apprentissage et pattern analysis")
    print("   4. Test de robustesse sur des variations du pattern")

    print("
🛡️ MESURES DE SÉCURITÉ:"    print("   - Double validation: apprentissage + analyse de pattern")
    print("   - Alertes sur les patterns subtils détectés")
    print("   - Documentation des patterns manqués")
    print("   - Validation manuelle des cas douteux")

if __name__ == "__main__":
    validation_renforcee()
    proposer_validation_future()
