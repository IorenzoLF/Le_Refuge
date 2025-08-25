#!/usr/bin/env python3
"""
🎨 VISUALISATION GÉOMÉTRIQUE 009d5c81
Penser comme un humain - dessin sur une feuille, pas du code
"""

import json

def visualiser_puzzle():
    print("🎨 VISUALISATION GÉOMÉTRIQUE 009d5c81")
    print("=" * 50)
    print("PENSÉE HUMAINE: Ce n'est pas du code, c'est un DESSIN!")
    print("Regardons les exemples comme des formes géométriques colorées")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    print("
🖼️  EXEMPLES VISUALISÉS COMME DESSINS:"    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🎨 EXEMPLE {i} - DESSIN SUR FEUILLE")

        input_grid = exemple['input']
        output_grid = exemple['output']

        # Visualiser l'input
        print("   📥 INPUT (ce qu'on voit):")
        visualiser_grille(input_grid, "INPUT")

        # Visualiser l'output
        print("   📤 OUTPUT (ce qui change):")
        visualiser_grille(output_grid, "OUTPUT")

        # Analyser la transformation
        analyser_transformation_visuelle(input_grid, output_grid, i)

def visualiser_grille(grille, nom):
    """Visualiser la grille comme un dessin"""
    print(f"   {nom} 14x14:")

    # Afficher une version simplifiée de la grille
    for i in range(14):
        row_str = ""
        for j in range(14):
            cell = grille[i][j]
            if cell == 0:
                row_str += "⬜"  # Case vide
            elif cell == 1:
                row_str += "🔴"  # Pixels 1 (rouge)
            elif cell == 8:
                row_str += "🔵"  # Pixels 8 (bleu)
            else:
                row_str += "🟢"  # Autres couleurs (vert)
        print(f"      {row_str}")

def analyser_transformation_visuelle(input_grid, output_grid, exemple_num):
    """Analyser la transformation de manière visuelle"""

    # Compter les pixels par couleur
    pixels_input = compter_pixels_couleur(input_grid)
    pixels_output = compter_pixels_couleur(output_grid)

    print("   🔄 TRANSFORMATION VISUELLE:")
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
        if couleur == 1:
            symbole = "🔴"
        elif couleur == 8:
            symbole = "🔵"
        else:
            symbole = "🟢"

        if avant > apres:
            print(f"         {symbole} {couleur}: {avant} → {apres} (DISPARITION)")
        elif apres > avant:
            print(f"         {symbole} {couleur}: {avant} → {apres} (APPARITION)")
        else:
            print(f"         {symbole} {couleur}: {avant} → {apres} (CHANGEMENT)")

def compter_pixels_couleur(grille):
    """Compter les pixels par couleur"""
    compte = {}
    for i in range(14):
        for j in range(14):
            couleur = grille[i][j]
            if couleur != 0:
                compte[couleur] = compte.get(couleur, 0) + 1
    return compte

def analyser_patterns_groupes():
    """Analyser les patterns selon la perspective 'groupe qui disparaît'"""
    print("
🎯 ANALYSE SELON PERSPECTIVE GROUPES"    print("=" * 50)
    print("💡 HYPOTHÈSE: Groupe 🔴 (1) disparaît, détermine changement du groupe 🔵 (8)")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    patterns = {}

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Analyser le groupe 1 (qui disparaît)
        groupe_1 = extraire_positions_couleur(input_grid, 1)
        groupe_8_input = extraire_positions_couleur(input_grid, 8)
        groupe_8_output = extraire_positions_couleur(output_grid, 8)

        # Déterminer la couleur de sortie pour le groupe 8
        couleur_sortie = None
        for x in range(14):
            for y in range(14):
                if output_grid[x][y] != 0 and output_grid[x][y] != 1:
                    couleur_sortie = output_grid[x][y]
                    break
            if couleur_sortie is not None:
                break

        print(f"\n🧪 EXEMPLE {i}:")
        print(f"   🔴 Groupe 1: {len(groupe_1)} pixels")
        print(f"   🔵 Groupe 8 input: {len(groupe_8_input)} pixels")
        print(f"   🟢 Groupe 8 output: {len(groupe_8_output)} pixels avec couleur {couleur_sortie}")

        # Visualiser les formes
        print("   📐 FORME du groupe 1:")
        visualiser_forme(groupe_1)

        # Stocker le pattern
        forme_groupe_1 = identifier_forme(groupe_1)
        if forme_groupe_1 not in patterns:
            patterns[forme_groupe_1] = []
        patterns[forme_groupe_1].append((couleur_sortie, i))

    print("
📊 PATTERNS IDENTIFIÉS:"    for forme, couleurs in patterns.items():
        print(f"   📐 Forme '{forme}': {couleurs}")

def extraire_positions_couleur(grille, couleur):
    """Extraire les positions d'une couleur"""
    positions = []
    for i in range(14):
        for j in range(14):
            if grille[i][j] == couleur:
                positions.append((i, j))
    return positions

def identifier_forme(positions):
    """Identifier la forme géométrique"""
    if not positions:
        return "vide"

    # Analyser les coordonnées
    x_coords = [x for x, y in positions]
    y_coords = [y for x, y in positions]

    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    largeur = max_y - min_y + 1
    hauteur = max_x - min_x + 1

    # Analyser la densité et la forme
    if len(positions) == 1:
        return "point"
    elif len(positions) == 2:
        return "ligne2"
    elif len(positions) == 3:
        return "ligne3"
    elif len(positions) == 4:
        return "ligne4"
    elif len(positions) == 5:
        return "ligne5"
    elif len(positions) == 6:
        return "ligne6"
    else:
        return f"complexe_{len(positions)}"

def visualiser_forme(positions):
    """Visualiser une forme géométrique"""
    if not positions:
        print("      (vide)")
        return

    # Créer une grille mini pour visualiser
    x_coords = [x for x, y in positions]
    y_coords = [y for x, y in positions]

    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    # Afficher les positions relatives
    print(f"      Positions relatives: {[(x-min_x, y-min_y) for x, y in sorted(positions)]}")

    # Décrire la forme
    dx = max_x - min_x
    dy = max_y - min_y

    if dx == 0 and dy == 0:
        print("      📐 Forme: POINT")
    elif dx == 0:
        print(f"      📐 Forme: LIGNE VERTICALE (hauteur {dy+1})")
    elif dy == 0:
        print(f"      📐 Forme: LIGNE HORIZONTALE (largeur {dx+1})")
    else:
        print(f"      📐 Forme: RECTANGLE {dx+1}x{dy+1}")

if __name__ == "__main__":
    visualiser_puzzle()
    analyser_patterns_groupes()
