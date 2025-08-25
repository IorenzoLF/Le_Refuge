#!/usr/bin/env python3
"""
🎯 ANALYSE PUZZLE 13 (VRAI) : 05f2a901
Ton intuition : "ranger" ou "ordre" - PATTERN DE RANGEMENT !
"""

import json

def analyser_rangement():
    """Analyser le pattern de rangement selon ton intuition"""
    print("🎯 ANALYSE PUZZLE 13 (VRAI): 05f2a901")
    print("=" * 50)
    print("🏠 TON INTUITION : RANGER OU ORDRE")
    print("📋 Pattern de rangement/organisation")

    with open("data/training/05f2a901.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser chaque exemple avec l'œil du rangement
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🏠 EXEMPLE {i} - ANALYSE RANGEMENT")
        print("-" * 40)

        input_grid = exemple['input']
        output_grid = exemple['output']

        print("📥 INPUT:")
        visualiser_rangement(input_grid)

        print("📤 OUTPUT:")
        visualiser_rangement(output_grid)

        # Analyser le pattern de rangement
        analyser_pattern_rangement(input_grid, output_grid, i)

def visualiser_rangement(grille):
    """Visualisation avec focus sur l'organisation"""
    for i, row in enumerate(grille):
        row_str = ""
        for j, cell in enumerate(row):
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
            elif cell == 6:
                row_str += "🟣"
            elif cell == 7:
                row_str += "🟤"
            elif cell == 8:
                row_str += "⚫"
            else:
                row_str += "💎"
        print(f"  {i}: {row_str}")

def analyser_pattern_rangement(input_grid, output_grid, exemple_num):
    """Analyser le pattern de rangement selon ton idée"""
    print("🏠 ANALYSE PATTERN RANGEMENT:")

    # Analyser l'organisation spatiale
    organisation_input = analyser_organisation(input_grid)
    organisation_output = analyser_organisation(output_grid)

    print(f"   📥 Input organisation: {organisation_input}")
    print(f"   📤 Output organisation: {organisation_output}")

    # Détecter les patterns de rangement
    patterns_rangement = detecter_patterns_rangement(input_grid, output_grid)
    print(f"   🔍 Patterns détectés: {patterns_rangement}")

    # Analyser les transformations de rangement
    if organisation_input != organisation_output:
        print("   🔄 TRANSFORMATION DE RANGEMENT DÉTECTÉE!")
        analyser_transformation_rangement(input_grid, output_grid, exemple_num)

def analyser_organisation(grille):
    """Analyser l'organisation d'une grille"""
    # Compter les pixels par ligne et colonne
    pixels_par_ligne = [sum(1 for cell in row if cell != 0) for row in grille]
    pixels_par_colonne = [sum(1 for row in grille if row[j] != 0) for j in range(len(grille[0]))]

    # Analyser la distribution
    lignes_avec_pixels = sum(1 for count in pixels_par_ligne if count > 0)
    colonnes_avec_pixels = sum(1 for count in pixels_par_colonne if count > 0)

    # Analyser la régularité
    moyenne_ligne = sum(pixels_par_ligne) / len(pixels_par_ligne)
    ecart_ligne = sum(abs(count - moyenne_ligne) for count in pixels_par_ligne) / len(pixels_par_ligne)

    return {
        'lignes_utilisees': lignes_avec_pixels,
        'colonnes_utilisees': colonnes_avec_pixels,
        'total_pixels': sum(pixels_par_ligne),
        'regularite': ecart_ligne
    }

def detecter_patterns_rangement(input_grid, output_grid):
    """Détecter les patterns de rangement"""
    patterns = []

    # Pattern 1: Regroupement par couleur
    if est_regroupement_couleurs(input_grid, output_grid):
        patterns.append("Regroupement par couleur")

    # Pattern 2: Alignement spatial
    if est_alignement_spatial(input_grid, output_grid):
        patterns.append("Alignement spatial")

    # Pattern 3: Organisation par densité
    if est_organisation_densite(input_grid, output_grid):
        patterns.append("Organisation par densité")

    # Pattern 4: Tri par position
    if est_tri_position(input_grid, output_grid):
        patterns.append("Tri par position")

    return patterns if patterns else ["Pattern non identifié"]

def est_regroupement_couleurs(input_grid, output_grid):
    """Vérifier si c'est un regroupement par couleur"""
    # Analyser les couleurs dans l'input et output
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

    # Si les couleurs sont les mêmes, vérifier le regroupement
    if couleurs_input == couleurs_output:
        # Analyser la dispersion des couleurs
        dispersion_input = calculer_dispersion_couleurs(input_grid)
        dispersion_output = calculer_dispersion_couleurs(output_grid)

        return dispersion_output < dispersion_input  # Plus regroupé

    return False

def calculer_dispersion_couleurs(grille):
    """Calculer la dispersion des couleurs (plus c'est bas, plus regroupé)"""
    couleurs_positions = {}

    for i, row in enumerate(grille):
        for j, cell in enumerate(row):
            if cell != 0:
                if cell not in couleurs_positions:
                    couleurs_positions[cell] = []
                couleurs_positions[cell].append((i, j))

    # Calculer la distance moyenne pour chaque couleur
    dispersion_totale = 0
    for positions in couleurs_positions.values():
        if len(positions) > 1:
            # Distance moyenne entre les pixels de même couleur
            distances = []
            for p1 in range(len(positions)):
                for p2 in range(p1 + 1, len(positions)):
                    dist = abs(positions[p1][0] - positions[p2][0]) + abs(positions[p1][1] - positions[p2][1])
                    distances.append(dist)
            dispersion_totale += sum(distances) / len(distances) if distances else 0

    return dispersion_totale

def est_alignement_spatial(input_grid, output_grid):
    """Vérifier si c'est un alignement spatial"""
    # Analyser l'alignement horizontal et vertical
    alignement_input = analyser_alignement(grille)
    alignement_output = analyser_alignement(output_grid)

    return alignement_output > alignement_input  # Plus aligné

def analyser_alignement(grille):
    """Analyser l'alignement des pixels"""
    alignement_score = 0

    # Alignement horizontal
    for i, row in enumerate(grille):
        pixels_ligne = [j for j, cell in enumerate(row) if cell != 0]
        if len(pixels_ligne) > 1:
            alignement_score += 1  # Points pour chaque ligne avec pixels

    # Alignement vertical
    for j in range(len(grille[0])):
        pixels_colonne = [i for i, row in enumerate(grille) if row[j] != 0]
        if len(pixels_colonne) > 1:
            alignement_score += 1  # Points pour chaque colonne avec pixels

    return alignement_score

def est_organisation_densite(input_grid, output_grid):
    """Vérifier si c'est une organisation par densité"""
    densite_input = analyser_densite(input_grid)
    densite_output = analyser_densite(output_grid)

    # Vérifier si la densité est plus régulière
    return densite_output['regularite'] < densite_input['regularite']

def analyser_densite(grille):
    """Analyser la densité des pixels"""
    pixels_par_ligne = [sum(1 for cell in row if cell != 0) for row in grille]
    pixels_par_colonne = [sum(1 for row in grille if row[j] != 0) for j in range(len(grille[0]))]

    moyenne_ligne = sum(pixels_par_ligne) / len(pixels_par_ligne)
    moyenne_colonne = sum(pixels_par_colonne) / len(pixels_par_colonne)

    regularite_ligne = sum(abs(count - moyenne_ligne) for count in pixels_par_ligne) / len(pixels_par_ligne)
    regularite_colonne = sum(abs(count - moyenne_colonne) for count in pixels_par_colonne) / len(pixels_par_colonne)

    return {
        'moyenne_ligne': moyenne_ligne,
        'moyenne_colonne': moyenne_colonne,
        'regularite': (regularite_ligne + regularite_colonne) / 2
    }

def est_tri_position(input_grid, output_grid):
    """Vérifier si c'est un tri par position"""
    # Analyser l'ordre des couleurs
    ordre_input = analyser_ordre_couleurs(input_grid)
    ordre_output = analyser_ordre_couleurs(output_grid)

    return ordre_input != ordre_output  # Changement d'ordre

def analyser_ordre_couleurs(grille):
    """Analyser l'ordre d'apparition des couleurs"""
    couleurs_ordre = []
    couleurs_vues = set()

    for row in grille:
        for cell in row:
            if cell != 0 and cell not in couleurs_vues:
                couleurs_ordre.append(cell)
                couleurs_vues.add(cell)

    return couleurs_ordre

def analyser_transformation_rangement(input_grid, output_grid, exemple_num):
    """Analyser la transformation de rangement"""
    print("   🔄 DÉTAILS TRANSFORMATION:")

    # Comparer les organisations
    org_input = analyser_organisation(input_grid)
    org_output = analyser_organisation(output_grid)

    print(f"     Lignes utilisées: {org_input['lignes_utilisees']} → {org_output['lignes_utilisees']}")
    print(f"     Colonnes utilisées: {org_output['colonnes_utilisees']} → {org_output['colonnes_utilisees']}")
    print(f"     Pixels totaux: {org_input['total_pixels']} → {org_output['total_pixels']}")
    print(".2f")

    # Analyser le type de rangement
    if org_output['lignes_utilisees'] < org_input['lignes_utilisees']:
        print("     📉 COMPRESSION VERTICALE (rangement vers le haut)")
    elif org_output['lignes_utilisees'] > org_input['lignes_utilisees']:
        print("     📈 EXPANSION VERTICALE (dépliement)")
    else:
        print("     ↕️ MÊME NOMBRE DE LIGNES (réarrangement horizontal)")

def analyse_generale_rangement():
    """Analyse générale du pattern de rangement"""
    print("
🏠 ANALYSE GÉNÉRALE PATTERN RANGEMENT"    print("=" * 60)

    with open("data/training/05f2a901.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"📊 {len(puzzle_data['train'])} exemples d'entraînement")

    # Analyser les patterns généraux
    patterns_generaux = []
    for i, exemple in enumerate(puzzle_data['train'], 1):
        patterns = detecter_patterns_rangement(exemple['input'], exemple['output'])
        patterns_generaux.extend(patterns)

    # Compter les patterns
    from collections import Counter
    compte_patterns = Counter(patterns_generaux)

    print("🔍 PATTERNS DE RANGEMENT IDENTIFIÉS:")
    for pattern, count in compte_patterns.items():
        print(f"   {pattern}: {count} fois")

    if patterns_generaux:
        print("✅ PATTERNS DE RANGEMENT DÉTECTÉS !")
        print("🎯 Ton intuition 'ranger' ou 'ordre' semble JUSTE !")
    else:
        print("❓ Pas de patterns évidents de rangement")

if __name__ == "__main__":
    analyser_rangement()
    analyse_generale_rangement()
