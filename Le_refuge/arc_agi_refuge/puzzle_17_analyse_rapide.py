#!/usr/bin/env python3
"""
🎯 PUZZLE 17 RAPIDE - 070dd51e
Analyse rapide pour identifier le pattern
"""

import json

def analyse_rapide_puzzle_17():
    print("🎯 PUZZLE 17 RAPIDE - 070dd51e")
    print("=" * 50)

    try:
        with open("ARC-AGI-2-main/data/training/070dd51e.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("❌ Fichier non trouvé")
        return

    print(f"📊 {len(puzzle_data['train'])} exemples d'entraînement")

    # Premier exemple
    exemple = puzzle_data['train'][0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    # Dimensions
    dim_input = f"{len(input_grid)}x{len(input_grid[0])}"
    dim_output = f"{len(output_grid)}x{len(output_grid[0])}"
    print(f"📐 Dimensions: {dim_input} → {dim_output}")

    # Analyser les pixels
    pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
    pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)
    print(f"📊 Pixels: {pixels_input} → {pixels_output}")

    # Couleurs
    couleurs_input = set(cell for row in input_grid for cell in row if cell != 0)
    couleurs_output = set(cell for row in output_grid for cell in row if cell != 0)
    print(f"🎨 Couleurs: {sorted(couleurs_input)} → {sorted(couleurs_output)}")

    print("\n📥 INPUT:")
    visualiser(input_grid)

    print("📤 OUTPUT:")
    visualiser(output_grid)

    # Analyser les transformations
    analyser_transformations(input_grid, output_grid)

    # Analyser tous les exemples
    print("\n🔍 ANALYSE DE TOUS LES EXEMPLES:")
    analyser_tous_exemples(puzzle_data['train'])

    # Identifier le pattern principal
    identifier_pattern_principal(puzzle_data['train'])

def visualiser(grille):
    """Visualisation simple"""
    for i, row in enumerate(grille):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
            elif cell == 2:
                row_str += "🟢"
            elif cell == 3:
                row_str += "🔵"
            elif cell == 4:
                row_str += "🟡"
            elif cell == 5:
                row_str += "🟠"
            elif cell == 8:
                row_str += "⚫"
            elif cell == 9:
                row_str += "💎"
            else:
                row_str += "❓"
        print(f"  {i:2}: {row_str}")

def analyser_transformations(input_grid, output_grid):
    """Analyser les transformations entre input et output"""
    print("🔄 ANALYSE TRANSFORMATIONS:")

    changements = []
    ajouts = []
    suppressions = []

    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            input_cell = input_grid[i][j]
            output_cell = output_grid[i][j]

            if input_cell != output_cell:
                if input_cell == 0 and output_cell != 0:
                    ajouts.append((i, j, output_cell))
                elif input_cell != 0 and output_cell == 0:
                    suppressions.append((i, j, input_cell))
                else:
                    changements.append((i, j, input_cell, output_cell))

    print(f"   ➕ Ajouts: {len(ajouts)}")
    print(f"   ➖ Suppressions: {len(suppressions)}")
    print(f"   🔄 Changements: {len(changements)}")

    if ajouts:
        couleurs_ajoutees = set(couleur for _, _, couleur in ajouts)
        print(f"   🎨 Couleurs ajoutées: {sorted(couleurs_ajoutees)}")

    if changements:
        changements_couleurs = [(old, new) for _, _, old, new in changements]
        print(f"   🎨 Changements de couleurs: {changements_couleurs[:5]}...")

def analyser_tous_exemples(exemples):
    """Analyser tous les exemples pour identifier les patterns"""
    patterns = []

    for i, exemple in enumerate(exemples, 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
        pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)

        couleurs_input = set(cell for row in input_grid for cell in row if cell != 0)
        couleurs_output = set(cell for row in output_grid for cell in row if cell != 0)

        patterns.append({
            'exemple': i,
            'pixels': f"{pixels_input}→{pixels_output}",
            'couleurs_input': couleurs_input,
            'couleurs_output': couleurs_output,
            'dimensions': f"{len(input_grid)}x{len(input_grid[0])}"
        })

        print(f"   Exemple {i}: {pixels_input}→{pixels_output} pixels, couleurs {sorted(couleurs_input)}→{sorted(couleurs_output)}")

def identifier_pattern_principal(exemples):
    """Identifier le pattern principal du puzzle"""
    print("
🎨 IDENTIFICATION PATTERN PRINCIPAL:")

    # Analyser le premier exemple en détail
    exemple = exemples[0]
    input_grid = exemple['input']
    output_grid = exemple['output']

    # Chercher des patterns évidents
    pattern_trouve = False

    # Pattern 1: Symétrie
    if est_symetrique(input_grid, output_grid):
        print("   ✅ PATTERN: SYMÉTRIE détectée")
        pattern_trouve = True

    # Pattern 2: Remplissage
    if est_remplissage(input_grid, output_grid):
        print("   ✅ PATTERN: REMPLISSAGE détecté")
        pattern_trouve = True

    # Pattern 3: Translation
    if est_translation(input_grid, output_grid):
        print("   ✅ PATTERN: TRANSLATION détectée")
        pattern_trouve = True

    # Pattern 4: Rotation
    if est_rotation(input_grid, output_grid):
        print("   ✅ PATTERN: ROTATION détectée")
        pattern_trouve = True

    # Pattern 5: Mise à l'échelle
    if est_mise_a_echelle(input_grid, output_grid):
        print("   ✅ PATTERN: MISE À L'ÉCHELLE détectée")
        pattern_trouve = True

    # Pattern 6: Changement de couleur
    if est_changement_couleur(input_grid, output_grid):
        print("   ✅ PATTERN: CHANGEMENT DE COULEUR détecté")
        pattern_trouve = True

    if not pattern_trouve:
        print("   🔍 Pattern plus complexe ou unique à analyser manuellement")

def est_symetrique(input_grid, output_grid):
    """Vérifier si c'est un pattern de symétrie"""
    # Symétrie horizontale
    if len(input_grid) == len(output_grid) and len(input_grid[0]) == len(output_grid[0]):
        return output_grid == [row[::-1] for row in input_grid]
    return False

def est_remplissage(input_grid, output_grid):
    """Vérifier si c'est un pattern de remplissage"""
    pixels_input = sum(1 for row in input_grid for cell in row if cell != 0)
    pixels_output = sum(1 for row in output_grid for cell in row if cell != 0)
    return pixels_output > pixels_input * 1.5  # Plus de 50% de pixels en plus

def est_translation(input_grid, output_grid):
    """Vérifier si c'est un pattern de translation"""
    if len(input_grid) == len(output_grid) and len(input_grid[0]) == len(output_grid[0]):
        # Translation simple vers la droite
        for i in range(len(input_grid)):
            if input_grid[i][:-1] == output_grid[i][1:]:
                return True
    return False

def est_rotation(input_grid, output_grid):
    """Vérifier si c'est un pattern de rotation"""
    # Rotation 90°
    if len(input_grid) == len(output_grid[0]) and len(input_grid[0]) == len(output_grid):
        rotated = [[input_grid[j][len(input_grid)-1-i] for j in range(len(input_grid))] for i in range(len(input_grid[0]))]
        return rotated == output_grid
    return False

def est_mise_a_echelle(input_grid, output_grid):
    """Vérifier si c'est un pattern de mise à l'échelle"""
    facteur_ligne = len(output_grid) // len(input_grid) if len(output_grid) % len(input_grid) == 0 else 0
    facteur_colonne = len(output_grid[0]) // len(input_grid[0]) if len(output_grid[0]) % len(input_grid[0]) == 0 else 0

    if facteur_ligne > 1 and facteur_colonne > 1 and facteur_ligne == facteur_colonne:
        return True
    return False

def est_changement_couleur(input_grid, output_grid):
    """Vérifier si c'est principalement un changement de couleur"""
    if len(input_grid) == len(output_grid) and len(input_grid[0]) == len(output_grid[0]):
        changements_couleur = 0
        pixels_total = 0

        for i in range(len(input_grid)):
            for j in range(len(input_grid[0])):
                if input_grid[i][j] != 0:
                    pixels_total += 1
                    if input_grid[i][j] != output_grid[i][j] and output_grid[i][j] != 0:
                        changements_couleur += 1

        return changements_couleur > pixels_total * 0.7  # Plus de 70% de changements
    return False

if __name__ == "__main__":
    analyse_rapide_puzzle_17()
