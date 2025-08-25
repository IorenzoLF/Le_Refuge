#!/usr/bin/env python3
"""
🎨 ANALYSE PUZZLE 7: 03560426
Copulation de formes selon l'intuition de l'utilisateur
"""

import json

def analyser_puzzle_7():
    """Analyser le puzzle 7 avec l'approche copulation de formes"""
    print("🎨 ANALYSE PUZZLE 7: 03560426")
    print("=" * 50)
    print("💡 APPROCHE: Copulation de formes - ordre et points de connexion")

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"📊 Informations: {len(puzzle_data['train'])} exemples d'entraînement")

    # Analyser chaque exemple avec l'approche copulation
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🖼️ EXEMPLE {i} - COPULATION DE FORMES")

        input_grid = exemple['input']
        output_grid = exemple['output']

        # Dimensions
        dim_input = f"{len(input_grid)}x{len(input_grid[0])}"
        dim_output = f"{len(output_grid)}x{len(output_grid[0])}"

        print(f"   📥 INPUT {dim_input} → 📤 OUTPUT {dim_output}")

        # Visualisation avec notre interface
        print("   📥 FORMES D'ENTRÉE:")
        visualiser_formes(input_grid, "INPUT")

        # Visualisation du résultat
        print("   📤 RÉSULTAT COPULATION:")
        visualiser_formes(output_grid, "OUTPUT")

        # Analyse de la copulation
        analyser_copulation(input_grid, output_grid, i)

def visualiser_formes(grille, nom):
    """Visualiser les formes avec notre interface"""
    print(f"   {nom} {len(grille)}x{len(grille[0])}:")

    for row in grille:
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
            elif cell == 6:
                row_str += "🟣"
            elif cell == 7:
                row_str += "🟤"
            elif cell == 8:
                row_str += "⚫"
            elif cell == 9:
                row_str += "⚪"
            else:
                row_str += "💎"
        print(f"      {row_str}")

def analyser_copulation(input_grid, output_grid, exemple_num):
    """Analyser la copulation selon l'intuition de l'utilisateur"""
    print("   🔄 ANALYSE COPULATION:")

    # Identifier les formes dans l'input
    formes_input = identifier_formes(input_grid)
    print(f"      📐 Formes identifiées en input: {len(formes_input)}")

    for idx, forme in enumerate(formes_input):
        print(f"         Forme {idx+1}: {len(forme)} pixels, couleur: {get_couleur_forme(input_grid, forme)}")

    # Identifier les formes dans l'output
    formes_output = identifier_formes(output_grid)
    print(f"      📐 Formes identifiées en output: {len(formes_output)}")

    for idx, forme in enumerate(formes_output):
        print(f"         Forme {idx+1}: {len(forme)} pixels, couleur: {get_couleur_forme(output_grid, forme)}")

    # Analyser la transformation
    if len(formes_input) > len(formes_output):
        print("      🔄 TRANSFORMATION: FUSION - plusieurs formes se copulent")
    elif len(formes_input) < len(formes_output):
        print("      🔄 TRANSFORMATION: DIVISION - une forme se sépare")
    else:
        print("      🔄 TRANSFORMATION: MODIFICATION - même nombre de formes")

    # Analyser les points de connexion potentiels
    analyser_points_connexion(input_grid, output_grid)

def identifier_formes(grille):
    """Identifier les formes connectées"""
    rows = len(grille)
    cols = len(grille[0])
    visited = set()
    formes = []

    for i in range(rows):
        for j in range(cols):
            if grille[i][j] != 0 and (i, j) not in visited:
                # Nouvelle forme trouvée
                forme = flood_fill_forme(grille, i, j, visited)
                formes.append(forme)

    return formes

def flood_fill_forme(grille, start_i, start_j, visited):
    """Identifier une forme connectée"""
    rows = len(grille)
    cols = len(grille[0])
    forme = set()
    pile = [(start_i, start_j)]

    couleur = grille[start_i][start_j]

    while pile:
        i, j = pile.pop()

        if (i < 0 or i >= rows or j < 0 or j >= cols or
            (i, j) in visited or grille[i][j] != couleur):
            continue

        visited.add((i, j))
        forme.add((i, j))

        # Ajouter les 4 directions
        pile.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])

    return forme

def get_couleur_forme(grille, forme):
    """Obtenir la couleur d'une forme"""
    if not forme:
        return 0
    i, j = next(iter(forme))
    return grille[i][j]

def analyser_points_connexion(input_grid, output_grid):
    """Analyser les points de connexion selon l'intuition 'par où'"""
    print("      🎯 ANALYSE POINTS DE CONNEXION:")

    # Identifier les pixels qui changent
    pixels_changement = []
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] != output_grid[i][j]:
                pixels_changement.append((i, j, input_grid[i][j], output_grid[i][j]))

    print(f"      Pixels modifiés: {len(pixels_changement)}")

    if pixels_changement:
        # Analyser les types de changements
        nouvelles_formes = [p for p in pixels_changement if p[2] == 0]  # Input vide
        formes_disparues = [p for p in pixels_changement if p[3] == 0]  # Output vide
        changements_couleur = [p for p in pixels_changement if p[2] != 0 and p[3] != 0 and p[2] != p[3]]

        print(f"      Nouvelles formes: {len(nouvelles_formes)}")
        print(f"      Formes disparues: {len(formes_disparues)}")
        print(f"      Changements couleur: {len(changements_couleur)}")

        # Identifier les points de connexion potentiels
        points_connexion = identifier_points_connexion(pixels_changement)
        if points_connexion:
            print(f"      Points de connexion identifiés: {points_connexion}")

def identifier_points_connexion(pixels_changement):
    """Identifier les points de connexion 'par où'"""
    points = []

    for i, j, couleur_input, couleur_output in pixels_changement:
        # Un point de connexion est où deux couleurs différentes se rencontrent
        if couleur_input != 0 and couleur_output != 0 and couleur_input != couleur_output:
            points.append((i, j))

    return points

def analyser_patterns_generaux():
    """Analyse générale des patterns du puzzle"""
    print("
🎯 ANALYSE GÉNÉRALE PUZZLE 7:"    print("=" * 50)

    with open("data/training/03560426.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser les dimensions
    dims_input = set()
    dims_output = set()

    for exemple in puzzle_data['train']:
        input_grid = exemple['input']
        output_grid = exemple['output']

        dims_input.add(f"{len(input_grid)}x{len(input_grid[0])}")
        dims_output.add(f"{len(output_grid)}x{len(output_grid[0])}")

    print(f"   📐 Dimensions d'entrée: {sorted(dims_input)}")
    print(f"   📐 Dimensions de sortie: {sorted(dims_output)}")

    # Analyser les couleurs
    couleurs_input = set()
    couleurs_output = set()

    for exemple in puzzle_data['train']:
        input_grid = exemple['input']
        output_grid = exemple['output']

        for row in input_grid:
            for cell in row:
                if cell != 0:
                    couleurs_input.add(cell)

        for row in output_grid:
            for cell in row:
                if cell != 0:
                    couleurs_output.add(cell)

    print(f"   🎨 Couleurs en input: {sorted(couleurs_input)}")
    print(f"   🎨 Couleurs en output: {sorted(couleurs_output)}")

    # Analyser la complexité
    complexite = "simple" if len(couleurs_output) <= 2 else "complexe"
    print(f"   🧠 Complexité estimée: {complexite}")

    print("
   💡 HYPOTHÈSE:"    print("   Les formes se 'copulent' selon un ordre spécifique"    print("   Les points de connexion déterminent comment elles se joignent"    print("   L'ordre et les points de connexion sont les clés du puzzle"

if __name__ == "__main__":
    analyser_puzzle_7()
    analyser_patterns_generaux()
