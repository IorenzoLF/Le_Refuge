#!/usr/bin/env python3
"""
🌊 ANALYSE ONDE APPROFONDIE - 05269061
Comprendre la logique d'onde derrière les exemples
"""

import json
from collections import Counter

def analyser_onde_approfondie():
    print("🌊 ANALYSE ONDE APPROFONDIE - 05269061")
    print("=" * 50)
    print("🎯 Objectif: Comprendre la logique d'onde")
    print("📊 Résultats: Exemple 2 = 100%, autres = 0%")
    print("🔍 Hypothèse: Logique d'onde plus complexe")

    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🎯 EXEMPLE {i} - ANALYSE APPROFONDIE:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Extraire la séquence d'input
        couleurs_sequence = []
        positions_input = []
        for x in range(len(input_grid)):
            for y in range(len(input_grid[0])):
                if input_grid[x][y] != 0:
                    couleurs_sequence.append(input_grid[x][y])
                    positions_input.append((x, y))

        print(f"Sequence input: {couleurs_sequence}")
        print(f"Positions input: {positions_input}")

        # Analyser l'output
        analyser_output_onde(output_grid, couleurs_sequence, i)

def analyser_output_onde(output_grid, couleurs_sequence, exemple_num):
    """Analyser l'output pour identifier la logique d'onde"""

    h, w = len(output_grid), len(output_grid[0])

    print("
🔍 ANALYSE OUTPUT:"    # Afficher la grille avec indices
    print("   j→ 0 1 2 3 4 5 6")
    print("  i↓")
    for i in range(h):
        row_str = f"  {i}  "
        for j in range(w):
            row_str += f"{output_grid[i][j]} "
        print(row_str)

    # Analyser les patterns possibles
    print("
📊 ANALYSE PATTERNS POSSIBLES:"    # Pattern 1: Répétition cyclique diagonale
    print("1. 🔄 Répétition cyclique diagonale:")
    pattern1_matches = 0
    total_positions = 0

    for i in range(h):
        for j in range(w):
            if output_grid[i][j] != 0:
                total_positions += 1
                couleur_theorique = couleurs_sequence[(i + j) % len(couleurs_sequence)]
                if output_grid[i][j] == couleur_theorique:
                    pattern1_matches += 1
                    print(f"   ✅ ({i},{j}): {output_grid[i][j]} = {couleur_theorique}")
                else:
                    print(f"   ❌ ({i},{j}): {output_grid[i][j]} ≠ {couleur_theorique}")

    if total_positions > 0:
        taux1 = pattern1_matches / total_positions * 100
        print(".1f")

    # Pattern 2: Répétition par ligne/colonne
    print("\n2. 📊 Répétition par ligne:")
    pattern2_matches = 0

    for i in range(h):
        for j in range(w):
            if output_grid[i][j] != 0:
                couleur_theorique = couleurs_sequence[j % len(couleurs_sequence)]
                if output_grid[i][j] == couleur_theorique:
                    pattern2_matches += 1
                else:
                    print(f"   ❌ ({i},{j}): {output_grid[i][j]} ≠ {couleur_theorique} (ligne)")

    if total_positions > 0:
        taux2 = pattern2_matches / total_positions * 100
        print(".1f")

    # Pattern 3: Répétition par colonne
    print("\n3. 📊 Répétition par colonne:")
    pattern3_matches = 0

    for i in range(h):
        for j in range(w):
            if output_grid[i][j] != 0:
                couleur_theorique = couleurs_sequence[i % len(couleurs_sequence)]
                if output_grid[i][j] == couleur_theorique:
                    pattern3_matches += 1
                else:
                    print(f"   ❌ ({i},{j}): {output_grid[i][j]} ≠ {couleur_theorique} (colonne)")

    if total_positions > 0:
        taux3 = pattern3_matches / total_positions * 100
        print(".1f")

    # Identifier le meilleur pattern
    patterns = {
        "Diagonale (i+j)": taux1,
        "Par ligne": taux2,
        "Par colonne": taux3
    }

    meilleur_pattern = max(patterns.items(), key=lambda x: x[1])
    print("
🏆 MEILLEUR PATTERN:"    print(f"   {meilleur_pattern[0]}: {meilleur_pattern[1]:.1f}%")

    if meilleur_pattern[1] > 80:
        print("   ✅ Pattern identifié avec succès")
    elif meilleur_pattern[1] > 50:
        print("   ⚠️ Pattern partiellement identifié")
    else:
        print("   ❌ Aucun pattern simple trouvé")

def analyser_logique_onde():
    """Analyser la logique d'onde conceptuelle"""

    print("
🌊 ANALYSE LOGIQUE D'ONDE:"    print("=" * 40)

    print("\n📝 INTERPRÉTATION DE L'UTILISATEUR:")
    print("   'onde de 3 couleurs qui se déplace'")
    print("   'de en haut à gauche, vers en bas à droite'")
    print("   'direction pourrait être différentes dans d'autres cas'")

    print("\n🔬 ANALYSE TECHNIQUE:")
    print("   ✅ Exemple 2: Suit parfaitement pattern diagonal")
    print("   ❌ Exemple 1: Ne suit pas le même pattern")
    print("   ❌ Exemple 3: Ne suit pas le même pattern")

    print("\n💡 HYPOTHÈSES:")
    print("   1. 🔄 Chaque exemple a sa propre 'direction' d'onde")
    print("   2. 📊 L'onde s'adapte à la position des couleurs input")
    print("   3. 🎯 Pattern diagonal = onde avec direction fixe")
    print("   4. 🌊 L'onde pourrait être multidirectionnelle")

    print("\n🎯 CONCLUSION:")
    print("   L'interprétation 'onde' est VALIDE mais plus GÉNÉRIQUE")
    print("   Le pattern diagonal est une SPÉCIALISATION d'onde")
    print("   Chaque puzzle peut avoir sa propre 'logique d'onde'")

def main():
    analyser_onde_approfondie()
    analyser_logique_onde()

if __name__ == "__main__":
    main()
