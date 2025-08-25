#!/usr/bin/env python3
"""
🎨 ANALYSE GÉOMÉTRIQUE DU DÉCOUPAGE PUZZLE 10 (0520fde7)
Interprétation : ligne grise = découpage, 2 zones superposées
"""

import json

def analyser_decoupage_geometrique():
    """Analyser le découpage géométrique selon ton interprétation"""
    print("🎨 ANALYSE GÉOMÉTRIQUE DU DÉCOUPAGE")
    print("=" * 50)
    print("🏷️ LIGNE GRISE = MARQUAGE DE DÉCOUPAGE")
    print("✂️ DÉCOUPAGE CRÉE 2 ZONES")
    print("🔄 SUPERPOSITION DES ZONES")

    with open("data/training/0520fde7.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser chaque exemple selon ton interprétation
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🎯 EXEMPLE {i} - ANALYSE GÉOMÉTRIQUE")
        print("-" * 40)

        input_grid = exemple['input']
        output_grid = exemple['output']

        print("📥 INPUT:")
        visualiser(input_grid)

        print("📤 OUTPUT:")
        visualiser(output_grid)

        # Identifier la ligne grise (couleur 5)
        lignes_grises = detecter_lignes_grises(input_grid)
        print(f"🏷️ LIGNES GRISES DÉTECTÉES: {lignes_grises}")

        # Analyser le découpage selon ton idée
        analyser_zones_decoupees(input_grid, output_grid, i)

def visualiser(grille):
    """Visualisation avec indication des zones"""
    for i, row in enumerate(grille):
        row_str = ""
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += "⬜"
            elif cell == 1:
                row_str += "🔴"
            elif cell == 2:
                row_str += "🟢"
            elif cell == 5:
                row_str += "⚫"  # Ligne grise de découpage
            else:
                row_str += "💎"
        print(f"  {i}: {row_str}")

def detecter_lignes_grises(grille):
    """Détecter les lignes grises (couleur 5)"""
    lignes_grises = []

    # Lignes horizontales
    for i in range(len(grille)):
        ligne_complete_grise = all(cell == 5 for cell in grille[i])
        if ligne_complete_grise:
            lignes_grises.append(f"Ligne horizontale {i}")

    # Colonnes verticales
    for j in range(len(grille[0])):
        colonne_complete_grise = all(grille[i][j] == 5 for i in range(len(grille)))
        if colonne_complete_grise:
            lignes_grises.append(f"Colonne verticale {j}")

    return lignes_grises

def analyser_zones_decoupees(input_grid, output_grid, exemple_num):
    """Analyser les zones découpées selon ton interprétation"""
    print("✂️ ANALYSE DU DÉCOUPAGE:")

    # Identifier les zones non-grises dans l'input
    zones_input = extraire_zones_non_grises(input_grid)
    print(f"   📥 Zones input identifiées: {len(zones_input)}")

    # Analyser l'output
    zones_output = extraire_zones_non_grises(output_grid)
    print(f"   📤 Zones output identifiées: {len(zones_output)}")

    # Analyser la superposition selon ton idée
    analyser_superposition(zones_input, zones_output, exemple_num)

def extraire_zones_non_grises(grille):
    """Extraire les zones qui ne sont pas grises"""
    zones = []
    rows = len(grille)
    cols = len(grille[0])

    for i in range(rows):
        for j in range(cols):
            if grille[i][j] != 0 and grille[i][j] != 5:  # Ni vide ni gris
                # Trouver la zone connectée
                zone = trouver_zone(grille, i, j)
                if zone and zone not in zones:
                    zones.append(zone)

    return zones

def trouver_zone(grille, start_i, start_j):
    """Trouver une zone connectée (même couleur, pas grise)"""
    rows = len(grille)
    cols = len(grille[0])
    couleur = grille[start_i][start_j]

    if couleur == 5 or couleur == 0:  # Gris ou vide
        return None

    zone = set()
    visite = set()
    pile = [(start_i, start_j)]

    while pile:
        i, j = pile.pop()
        if (i < 0 or i >= rows or j < 0 or j >= cols or
            (i, j) in visite or grille[i][j] != couleur):
            continue

        visite.add((i, j))
        zone.add((i, j))

        # Voisins
        pile.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])

    return zone if zone else None

def analyser_superposition(zones_input, zones_output, exemple_num):
    """Analyser la superposition selon ton interprétation"""
    print("🔄 ANALYSE DE SUPERPOSITION:")

    if not zones_input:
        print("   ❌ Aucune zone input détectée")
        return

    print(f"   🎯 Interprétation géométrique possible:")
    print(f"   📐 Zone 1 input: {len(zones_input[0]) if zones_input else 0} pixels")
    if len(zones_input) > 1:
        print(f"   📐 Zone 2 input: {len(zones_input[1])} pixels")

    print(f"   🔄 Superposition → {len(zones_output)} zone(s) output")

    # Analyser les règles de superposition possibles
    print(f"   🧠 Règles possibles de superposition:")
    if len(zones_input) >= 2:
        print(f"   - Intersection des zones")
        print(f"   - Union des zones")
        print(f"   - Différence des zones")
        print(f"   - Conditions spéciales selon position")

def analyse_generale_decoupage():
    """Analyse générale du pattern de découpage"""
    print("
🎯 ANALYSE GÉNÉRALE PATTERN DÉCOUPAGE"    print("=" * 60)

    with open("data/training/0520fde7.json", 'r') as f:
        puzzle_data = json.load(f)

    total_lignes_grises = 0
    patterns_decoupage = []

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        lignes_grises = detecter_lignes_grises(input_grid)
        total_lignes_grises += len(lignes_grises)

        patterns_decoupage.append({
            'exemple': i,
            'lignes_grises': lignes_grises,
            'dimensions_input': f"{len(input_grid)}x{len(input_grid[0])}",
            'dimensions_output': f"{len(exemple['output'])}x{len(exemple['output'][0])}"
        })

    print(f"📊 TOTAL LIGNES GRISES: {total_lignes_grises}")
    print("🔍 PATTERNS DÉCOUPAGE IDENTIFIÉS:")

    for pattern in patterns_decoupage:
        print(f"   Exemple {pattern['exemple']}:")
        print(f"     Lignes grises: {pattern['lignes_grises']}")
        print(f"     Dimensions: {pattern['dimensions_input']} → {pattern['dimensions_output']}")

if __name__ == "__main__":
    analyser_decoupage_geometrique()
    analyse_generale_decoupage()
