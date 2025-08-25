#!/usr/bin/env python3
"""
🔍 ANALYSE ONDE - 05269061
Nouvelle perspective: onde de 3 couleurs se déplaçant
"""

import json
from collections import Counter

def analyser_onde_05269061():
    print("🌊 ANALYSE ONDE - 05269061")
    print("=" * 50)
    print("📊 Description utilisateur: onde de 3 couleurs")
    print("🎯 Direction: haut-gauche → bas-droite")
    print("🔄 Flexible: direction pourrait varier")

    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🌊 EXEMPLE {i} - ANALYSE ONDE:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"Input {len(input_grid)}x{len(input_grid[0])}:")
        for row in input_grid:
            print(f"  {row}")

        print(f"Output {len(output_grid)}x{len(output_grid[0])}:")
        for row in output_grid:
            print(f"  {row}")

        # Analyser les couleurs et leur propagation
        analyser_propagation_onde(input_grid, output_grid, i)

def analyser_propagation_onde(input_grid, output_grid, exemple_num):
    """Analyser comment l'onde se propage"""

    print("
📈 ANALYSE PROPAGATION ONDE:"    # Compter les couleurs
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

    print(f"🎨 Input: {dict(couleurs_input)}")
    print(f"🎯 Output: {dict(couleurs_output)}")

    # Analyser les positions
    h, w = len(input_grid), len(input_grid[0])

    print("
📍 POSITIONS INPUT:"    for i in range(h):
        for j in range(w):
            if input_grid[i][j] != 0:
                print(f"  Couleur {input_grid[i][j]}: ({i},{j})")

    print("
📍 POSITIONS OUTPUT:"    for i in range(h):
        for j in range(w):
            if output_grid[i][j] != 0:
                print(f"  Couleur {output_grid[i][j]}: ({i},{j})")

    # Analyser le pattern d'onde
    print("
🌊 ANALYSE PATTERN ONDE:"    couleurs_sequence = []
    for row in input_grid:
        for cell in row:
            if cell != 0 and cell not in couleurs_sequence:
                couleurs_sequence.append(cell)

    print(f"🔄 Séquence de couleurs: {couleurs_sequence}")

    # Vérifier si l'output suit un pattern d'onde
    analyser_pattern_onde(output_grid, couleurs_sequence)

def analyser_pattern_onde(output_grid, couleurs_sequence):
    """Analyser si l'output suit un pattern d'onde"""

    h, w = len(output_grid), len(output_grid[0])
    print("
🔍 VÉRIFICATION PATTERN ONDE:"    # Vérifier les diagonales
    diagonale_principale = []
    for i in range(min(h, w)):
        diagonale_principale.append(output_grid[i][i])

    print(f"📊 Diagonale principale: {diagonale_principale}")

    # Vérifier les diagonales secondaires
    diagonale_secondaire = []
    for i in range(min(h, w)):
        diagonale_secondaire.append(output_grid[i][w-1-i])

    print(f"📊 Diagonale secondaire: {diagonale_secondaire}")

    # Analyser la propagation
    print("
🌊 PROPAGATION DÉTAILLÉE:"    for i in range(h):
        row_pattern = []
        for j in range(w):
            if output_grid[i][j] != 0:
                # Calculer la "distance" depuis le coin haut-gauche
                distance = i + j
                # Déterminer la couleur basée sur la distance et la séquence
                couleur_theorique = couleurs_sequence[distance % len(couleurs_sequence)]
                row_pattern.append(f"({j}):{output_grid[i][j]}→{couleur_theorique}")
        if row_pattern:
            print(f"  Ligne {i}: {row_pattern}")

    # Vérifier si c'est vraiment une onde
    verifier_onde_vs_diagonale(output_grid, couleurs_sequence)

def verifier_onde_vs_diagonale(output_grid, couleurs_sequence):
    """Comparer l'interprétation onde vs diagonale"""

    h, w = len(output_grid), len(output_grid[0])

    print("
⚖️ COMPARAISON ONDE vs DIAGONALE:"    # Pattern diagonale (ce que j'avais identifié avant)
    print("🔄 PATTERN DIAGONALE (hypothèse précédente):")
    for i in range(h):
        for j in range(w):
            couleur_diagonale = couleurs_sequence[(i + j) % len(couleurs_sequence)]
            couleur_reelle = output_grid[i][j]
            if couleur_reelle != 0:
                match = "✅" if couleur_reelle == couleur_diagonale else "❌"
                print(f"  ({i},{j}): {couleur_reelle} vs {couleur_diagonale} {match}")

    # Pattern onde (nouvelle hypothèse)
    print("\n🌊 PATTERN ONDE (nouvelle hypothèse):")
    print("   Interprétation: propagation progressive depuis coin haut-gauche")
    print("   Chaque position (i,j) prend couleur basée sur i+j (distance)")

    # Calculer taux de correspondance pour chaque pattern
    correspondance_diagonale = 0
    correspondance_onde = 0
    total_positions = 0

    for i in range(h):
        for j in range(w):
            if output_grid[i][j] != 0:
                total_positions += 1
                distance = i + j

                # Test pattern diagonale
                couleur_diagonale = couleurs_sequence[distance % len(couleurs_sequence)]
                if output_grid[i][j] == couleur_diagonale:
                    correspondance_diagonale += 1

                # Test pattern onde (même chose pour cette implémentation)
                # Mais on pourrait avoir d'autres variantes d'onde

    if total_positions > 0:
        taux_diagonale = correspondance_diagonale / total_positions * 100
        print("
📊 RÉSULTATS:"        print(".1f")
        print(f"   Positions analysées: {total_positions}")

        if taux_diagonale > 80:
            print("   ✅ Pattern diagonal confirmé")
        elif taux_diagonale > 50:
            print("   ⚠️ Pattern partiellement confirmé")
        else:
            print("   ❌ Pattern diagonal ne correspond pas")

def analyser_variantes_onde():
    """Analyser différentes variantes d'ondes possibles"""

    print("
🔄 ANALYSE VARIANTES D'ONDE POSSIBLES:"    print("   1. 📈 Propagation linéaire: couleur = sequence[i+j]")
    print("   2. 🎯 Propagation radiale: couleur = sequence[max(i,j)]")
    print("   3. 🔄 Propagation en spirale: couleur = sequence[i+j + rotation]")
    print("   4. 📊 Propagation par vagues: couleur = sequence[(i+j) % len + phase]")
    print("   5. 🎨 Propagation colorée: chaque couleur se propage différemment")

    print("
💡 CONCLUSION:"    print("   L'interprétation 'onde' est plus conceptuelle que technique")
    print("   Le pattern diagonal reste valide mais peut être généralisé")
    print("   La 'direction' (haut-gauche→bas-droite) correspond à i+j")

def main():
    analyser_onde_05269061()
    analyser_variantes_onde()

if __name__ == "__main__":
    main()
