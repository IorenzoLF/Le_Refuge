#!/usr/bin/env python3
"""
📋 ANALYSE DU CADRE DES PUZZLES ARC
Quelles informations sont disponibles dans les puzzles ?
"""

import json
from collections import Counter

def analyser_cadre_puzzles():
    print("📋 ANALYSE DU CADRE DES PUZZLES ARC")
    print("=" * 50)
    print("🎯 Objectif: Identifier TOUTES les informations disponibles")

    # Analyser quelques puzzles représentatifs
    puzzles = ["00576224", "007bbfb7", "009d5c81", "00d62c1b", "00dbd492"]

    for puzzle_id in puzzles[:3]:  # Analyser les 3 premiers
        print(f"\n🧩 PUZZLE {puzzle_id}")
        print("-" * 30)

        try:
            with open(f"data/training/{puzzle_id}.json", 'r') as f:
                puzzle_data = json.load(f)

            analyser_informations_puzzle(puzzle_data, puzzle_id)

        except Exception as e:
            print(f"❌ Erreur: {e}")

def analyser_informations_puzzle(puzzle_data, puzzle_id):
    """Analyser toutes les informations disponibles dans un puzzle"""

    print("📊 INFORMATIONS STRUCTURELLES:")
    print(f"   📚 Nombre d'exemples d'entraînement: {len(puzzle_data['train'])}")
    print(f"   🧪 Nombre d'exemples de test: {len(puzzle_data['test'])}")

    # Analyser les dimensions
    print("
📐 INFORMATIONS DIMENSIONNELLES:"    dimensions_input = set()
    dimensions_output = set()

    for exemple in puzzle_data['train']:
        h_in, w_in = len(exemple['input']), len(exemple['input'][0])
        h_out, w_out = len(exemple['output']), len(exemple['output'][0])
        dimensions_input.add((h_in, w_in))
        dimensions_output.add((h_out, w_out))

    print(f"   📥 Dimensions input possibles: {sorted(dimensions_input)}")
    print(f"   📤 Dimensions output possibles: {sorted(dimensions_output)}")

    # Analyser les couleurs
    print("
🎨 INFORMATIONS SUR LES COULEURS:"    toutes_couleurs = set()
    couleurs_par_exemple = []

    for i, exemple in enumerate(puzzle_data['train']):
        couleurs_exemple = set()
        for grid in [exemple['input'], exemple['output']]:
            for row in grid:
                for cell in row:
                    if cell != 0:
                        couleurs_exemple.add(cell)
                        toutes_couleurs.add(cell)
        couleurs_par_exemple.append(couleurs_exemple)
        print(f"   Exemple {i+1}: {sorted(couleurs_exemple)}")

    print(f"   🌈 Toutes les couleurs utilisées: {sorted(toutes_couleurs)}")
    print(f"   📊 Nombre total de couleurs: {len(toutes_couleurs)}")

    # Analyser les positions
    print("
📍 INFORMATIONS SUR LES POSITIONS:"    for i, exemple in enumerate(puzzle_data['train'][:2]):  # Analyser 2 exemples
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"   Exemple {i+1}:")
        print(f"      Input {len(input_grid)}x{len(input_grid[0])}: positions non-zéro: {compter_positions_non_zero(input_grid)}")
        print(f"      Output {len(output_grid)}x{len(output_grid[0])}: positions non-zéro: {compter_positions_non_zero(output_grid)}")

    # Analyser les patterns spatiaux
    print("
🔄 INFORMATIONS SPATIALES:"    for i, exemple in enumerate(puzzle_data['train'][:1]):  # Analyser 1 exemple
        input_grid = exemple['input']
        output_grid = exemple['output']

        print(f"   Exemple {i+1}:")

        # Analyse des formes dans l'input
        formes_input = analyser_formes(input_grid)
        print(f"      📥 Formes input: {formes_input}")

        # Analyse des formes dans l'output
        formes_output = analyser_formes(output_grid)
        print(f"      📤 Formes output: {formes_output}")

        # Analyse des relations spatiales
        relations = analyser_relations_spatiales(input_grid, output_grid)
        print(f"      🔗 Relations: {relations}")

def compter_positions_non_zero(grille):
    """Compter les positions non-zéro"""
    positions = []
    for i, row in enumerate(grille):
        for j, cell in enumerate(row):
            if cell != 0:
                positions.append((i, j, cell))
    return len(positions)

def analyser_formes(grille):
    """Analyser les formes présentes dans la grille"""
    h, w = len(grille), len(grille[0])

    # Compter les pixels par couleur
    pixels_par_couleur = Counter()
    for row in grille:
        for cell in row:
            if cell != 0:
                pixels_par_couleur[cell] += 1

    # Détecter les régions connectées
    regions = detecter_regions(grille)

    formes = {
        'pixels_par_couleur': dict(pixels_par_couleur),
        'nombre_regions': len(regions),
        'tailles_regions': [len(region) for region in regions]
    }

    return formes

def detecter_regions(grille):
    """Détecter les régions connectées (simplifié)"""
    if not grille or not grille[0]:
        return []

    h, w = len(grille), len(grille[0])
    visite = [[False for _ in range(w)] for _ in range(h)]
    regions = []

    def dfs(i, j, couleur):
        if (i < 0 or i >= h or j < 0 or j >= w or
            visite[i][j] or grille[i][j] != couleur):
            return []

        visite[i][j] = True
        region = [(i, j)]

        # Voisins (4 directions)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            region.extend(dfs(i + di, j + dj, couleur))

        return region

    for i in range(h):
        for j in range(w):
            if grille[i][j] != 0 and not visite[i][j]:
                region = dfs(i, j, grille[i][j])
                if region:
                    regions.append(region)

    return regions

def analyser_relations_spatiales(input_grid, output_grid):
    """Analyser les relations spatiales entre input et output"""
    h_in, w_in = len(input_grid), len(input_grid[0])
    h_out, w_out = len(output_grid), len(output_grid[0])

    relations = {
        'ratio_hauteur': h_out / h_in if h_in > 0 else 0,
        'ratio_largeur': w_out / w_in if w_in > 0 else 0,
        'expansion': h_out * w_out / (h_in * w_in) if h_in > 0 and w_in > 0 else 0
    }

    # Vérifier si c'est une expansion par bloc
    if h_out % h_in == 0 and w_out % w_in == 0:
        facteur_h = h_out // h_in
        facteur_w = w_out // w_in
        if facteur_h == facteur_w:
            relations['expansion_par_bloc'] = facteur_h

    return relations

def analyser_cadre_general():
    """Analyser le cadre général des puzzles ARC"""
    print("
🌍 CADRE GÉNÉRAL DES PUZZLES ARC"    print("=" * 50)

    # Analyser quelques puzzles pour généraliser
    puzzle_ids = ["00576224", "007bbfb7", "009d5c81"]

    stats_generales = {
        'dimensions_input': Counter(),
        'dimensions_output': Counter(),
        'couleurs_totales': set(),
        'ratios_expansion': Counter()
    }

    for puzzle_id in puzzle_ids:
        try:
            with open(f"data/training/{puzzle_id}.json", 'r') as f:
                puzzle_data = json.load(f)

            for exemple in puzzle_data['train']:
                h_in, w_in = len(exemple['input']), len(exemple['input'][0])
                h_out, w_out = len(exemple['output']), len(exemple['output'][0])

                stats_generales['dimensions_input'][(h_in, w_in)] += 1
                stats_generales['dimensions_output'][(h_out, w_out)] += 1

                for grid in [exemple['input'], exemple['output']]:
                    for row in grid:
                        for cell in row:
                            if cell != 0:
                                stats_generales['couleurs_totales'].add(cell)

                ratio = (h_out * w_out) / (h_in * w_in) if h_in > 0 and w_in > 0 else 0
                stats_generales['ratios_expansion'][round(ratio, 1)] += 1

        except:
            pass

    print("📊 STATISTIQUES GÉNÉRALES:")
    print(f"   📐 Dimensions input les plus communes: {stats_generales['dimensions_input'].most_common(3)}")
    print(f"   📐 Dimensions output les plus communes: {stats_generales['dimensions_output'].most_common(3)}")
    print(f"   🌈 Couleurs disponibles (0-9): {sorted(stats_generales['couleurs_totales'])}")
    print(f"   📈 Ratios d'expansion: {stats_generales['ratios_expansion'].most_common(5)}")

    print("
💡 CONSTATS IMPORTANTS:"    print("   🎯 Les puzzles ont un cadre TRES restreint:"    print("      - Grille 2D de petite taille (rarement > 30x30)"    print("      - Couleurs limitées (0-9, 0=transparent)"    print("      - Transformations géométriques simples"    print("      - Patterns répétitifs et logiques"    print("   🎯 Informations disponibles:"    print("      - Positions exactes de chaque pixel"    print("      - Couleurs de chaque pixel"    print("      - Relations spatiales entre pixels"    print("      - Groupes de pixels de même couleur"    print("      - Transformations dimensionnelles"    print("   🎯 Ce qui rend les puzzles solubles:"    print("      - Cadre limité = moins de possibilités"    print("      - Patterns répétitifs"    print("      - Logique déductive possible"    print("      - Validation par exemples d'entraînement"
def explorer_nouvelle_perspective_007bbfb7():
    """Explorer la nouvelle perspective pour 007bbfb7"""
    print("
🆕 NOUVELLE PERSPECTIVE POUR 007bbfb7"    print("=" * 50)

    try:
        with open("data/training/007bbfb7.json", 'r') as f:
            puzzle_data = json.load(f)

        # Analyser le premier exemple
        exemple = puzzle_data['train'][0]
        input_grid = exemple['input']
        output_grid = exemple['output']

        print("📥 INPUT 3x3 (le 'bloc'):")
        for row in input_grid:
            print(f"   {row}")

        print("
📤 OUTPUT 9x9 (répétitions du bloc):"        for row in output_grid:
            print(f"   {row}")

        print("
🔍 ANALYSE SELON LA NOUVELLE PERSPECTIVE:"        print("   💡 Idée: Chaque pixel de l'input détermine si le bloc est répété"        print("   💡 0 = pas de répétition du bloc dans cette zone 3x3"        print("   💡 couleur = oui, répéter le bloc dans cette zone 3x3"
        # Simuler cette logique
        print("
🧪 SIMULATION:"        for i in range(3):
            for j in range(3):
                valeur = input_grid[i][j]
                start_i, start_j = i * 3, j * 3

                print(f"   Position ({i},{j}) = {valeur}")
                if valeur == 0:
                    print("     → Zone 3x3 devrait être vide (0)"                else:
                    print(f"     → Zone 3x3 devrait contenir le bloc avec couleur {valeur}")

                # Afficher la zone correspondante
                zone = []
                for x in range(3):
                    for y in range(3):
                        zone.append(output_grid[start_i + x][start_j + y])
                print(f"     → Zone réelle: {zone}")

    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    analyser_cadre_puzzles()
    analyser_cadre_general()
    explorer_nouvelle_perspective_007bbfb7()
