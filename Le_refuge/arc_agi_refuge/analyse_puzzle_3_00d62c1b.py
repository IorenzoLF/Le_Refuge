#!/usr/bin/env python3
"""
🖼️ ANALYSE PUZZLE 3: 00d62c1b
Visualisation géométrique comme un humain
"""

import json

def visualiser_puzzle_3():
    """Visualiser le puzzle 3 comme un humain le ferait"""
    print("🖼️ ANALYSE PUZZLE 3: 00d62c1b")
    print("=" * 50)
    print("🎨 APPROCHE HUMAINE: Je regarde les formes et couleurs")

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    print("
📊 INFORMATIONS GÉNÉRALES:"    print(f"   Nombre d'exemples d'entraînement: {len(puzzle_data['train'])}")
    print(f"   Test disponible: {'✅' if puzzle_data['test'] else '❌'}")

    # Analyser chaque exemple
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🖼️ EXEMPLE {i} - DESSIN SUR FEUILLE")

        input_grid = exemple['input']
        output_grid = exemple['output']

        # Dimensions
        dim_input = f"{len(input_grid)}x{len(input_grid[0])}"
        dim_output = f"{len(output_grid)}x{len(output_grid[0])}"

        print(f"   📥 INPUT {dim_input} → 📤 OUTPUT {dim_output}")

        # Visualiser l'input
        print("   📥 CE QUE JE VOIS:")
        visualiser_grille(input_grid, "INPUT")

        # Visualiser l'output
        print("   📤 CE QUI CHANGE:")
        visualiser_grille(output_grid, "OUTPUT")

        # Analyser la transformation
        analyser_transformation(input_grid, output_grid, i)

def visualiser_grille(grille, nom):
    """Visualiser une grille comme un dessin"""
    print(f"   {nom} {len(grille)}x{len(grille[0])}:")

    # Afficher la grille avec emojis
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
            else:
                row_str += "⚪"
        print(f"      {row_str}")

def analyser_transformation(input_grid, output_grid, exemple_num):
    """Analyser la transformation de manière visuelle"""

    # Compter les pixels par couleur
    pixels_input = compter_pixels_couleur(input_grid)
    pixels_output = compter_pixels_couleur(output_grid)

    print("   🔄 ANALYSE DE LA TRANSFORMATION:")
    print(f"      Input: {pixels_input}")
    print(f"      Output: {pixels_output}")

    # Analyser ce qui change
    changements = []
    for couleur in set(pixels_input.keys()) | set(pixels_output.keys()):
        avant = pixels_input.get(couleur, 0)
        apres = pixels_output.get(couleur, 0)
        if avant != apres:
            changements.append((couleur, avant, apres))

    print("      Changements détectés:")
    for couleur, avant, apres in changements:
        emoji = get_emoji_couleur(couleur)
        if avant > apres:
            print(f"         {emoji} {couleur}: {avant} → {apres} (DISPARITION)")
        elif apres > avant:
            print(f"         {emoji} {couleur}: {avant} → {apres} (APPARITION)")
        else:
            print(f"         {emoji} {couleur}: {avant} → {apres} (CHANGEMENT)")

    # Analyser les positions des pixels
    if exemple_num <= 3:  # Analyser en détail les premiers exemples
        print("      📍 ANALYSE DES POSITIONS:")
        analyser_positions(input_grid, output_grid)

def get_emoji_couleur(couleur):
    """Obtenir l'emoji pour une couleur"""
    emojis = {
        1: "🔴", 2: "🟢", 3: "🔵", 4: "🟡",
        5: "🟠", 6: "🟣", 7: "🟤", 8: "⚫"
    }
    return emojis.get(couleur, "⚪")

def compter_pixels_couleur(grille):
    """Compter les pixels par couleur"""
    compte = {}
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            couleur = grille[i][j]
            if couleur != 0:
                compte[couleur] = compte.get(couleur, 0) + 1
    return compte

def analyser_positions(input_grid, output_grid):
    """Analyser les positions des pixels colorés"""
    print("         Positions des pixels colorés:")

    # Input positions
    input_positions = {}
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            couleur = input_grid[i][j]
            if couleur != 0:
                if couleur not in input_positions:
                    input_positions[couleur] = []
                input_positions[couleur].append((i, j))

    # Output positions
    output_positions = {}
    for i in range(len(output_grid)):
        for j in range(len(output_grid[0])):
            couleur = output_grid[i][j]
            if couleur != 0:
                if couleur not in output_positions:
                    output_positions[couleur] = []
                output_positions[couleur].append((i, j))

    # Afficher les positions
    for couleur in set(input_positions.keys()) | set(output_positions.keys()):
        emoji = get_emoji_couleur(couleur)
        print(f"         {emoji} Couleur {couleur}:")
        if couleur in input_positions:
            print(f"            Input:  {sorted(input_positions[couleur])}")
        if couleur in output_positions:
            print(f"            Output: {sorted(output_positions[couleur])}")

def analyser_patterns_generaux():
    """Analyser les patterns généraux du puzzle"""
    print("
🎯 ANALYSE DES PATTERNS GÉNÉRAUX"    print("=" * 50)

    with open("data/training/00d62c1b.json", 'r') as f:
        puzzle_data = json.load(f)

    patterns = []

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Analyser le pattern de cet exemple
        pattern = {
            'exemple': i,
            'dimensions_input': f"{len(input_grid)}x{len(input_grid[0])}",
            'dimensions_output': f"{len(output_grid)}x{len(output_grid[0])}",
            'pixels_input': compter_pixels_couleur(input_grid),
            'pixels_output': compter_pixels_couleur(output_grid)
        }

        patterns.append(pattern)

        print(f"   📐 Exemple {i}: {pattern['dimensions_input']} → {pattern['dimensions_output']}")
        print(f"      Input: {pattern['pixels_input']}")
        print(f"      Output: {pattern['pixels_output']}")

    # Analyser les patterns communs
    print("
🔍 PATTERNS COMMUNS IDENTIFIÉS:"    analyser_patterns_communs(patterns)

def analyser_patterns_communs(patterns):
    """Analyser les patterns communs"""
    # Vérifier si dimensions constantes
    dims_input = [p['dimensions_input'] for p in patterns]
    dims_output = [p['dimensions_output'] for p in patterns]

    if len(set(dims_input)) == 1:
        print(f"   ✅ Dimensions d'entrée constantes: {dims_input[0]}")
    else:
        print(f"   ⚠️ Dimensions d'entrée variables: {set(dims_input)}")

    if len(set(dims_output)) == 1:
        print(f"   ✅ Dimensions de sortie constantes: {dims_output[0]}")
    else:
        print(f"   ⚠️ Dimensions de sortie variables: {set(dims_output)}")

    # Analyser les couleurs
    couleurs_input = set()
    couleurs_output = set()

    for p in patterns:
        couleurs_input.update(p['pixels_input'].keys())
        couleurs_output.update(p['pixels_output'].keys())

    print(f"   🎨 Couleurs utilisées en input: {sorted(couleurs_input)}")
    print(f"   🎨 Couleurs utilisées en output: {sorted(couleurs_output)}")

    # Vérifier si certaines couleurs disparaissent
    couleurs_disparues = couleurs_input - couleurs_output
    couleurs_nouvelles = couleurs_output - couleurs_input

    if couleurs_disparues:
        print(f"   🔴 Couleurs qui disparaissent: {sorted(couleurs_disparues)}")
    if couleurs_nouvelles:
        print(f"   🟢 Nouvelles couleurs: {sorted(couleurs_nouvelles)}")

if __name__ == "__main__":
    visualiser_puzzle_3()
    analyser_patterns_generaux()
