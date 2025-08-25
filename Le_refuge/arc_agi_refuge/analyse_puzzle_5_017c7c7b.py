#!/usr/bin/env python3
"""
🎨 ANALYSE PUZZLE 5: 017c7c7b
Notre interface de visualisation éprouvée
"""

import json

def analyser_puzzle_5():
    """Analyser le puzzle 5 avec notre approche visuelle"""
    print("🎨 ANALYSE PUZZLE 5: 017c7c7b")
    print("=" * 50)
    print("🖼️ Pensée visuelle - comme un humain regarderait le dessin")

    with open("data/training/017c7c7b.json", 'r') as f:
        puzzle_data = json.load(f)

    print(f"📊 Informations: {len(puzzle_data['train'])} exemples d'entraînement")

    # Analyser chaque exemple avec notre interface visuelle
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🖼️ EXEMPLE {i} - DESSIN SUR FEUILLE")

        input_grid = exemple['input']
        output_grid = exemple['output']

        # Dimensions
        dim_input = f"{len(input_grid)}x{len(input_grid[0])}"
        dim_output = f"{len(output_grid)}x{len(output_grid[0])}"

        print(f"   📥 INPUT {dim_input} → 📤 OUTPUT {dim_output}")

        # Visualisation avec notre interface éprouvée
        print("   📥 CE QUE JE VOIS:")
        visualiser_grille(input_grid, "INPUT")

        # Visualisation du résultat
        print("   📤 CE QUI SE TRANSFORME:")
        visualiser_grille(output_grid, "OUTPUT")

        # Analyse intuitive de la transformation
        analyser_transformation(input_grid, output_grid, i)

def visualiser_grille(grille, nom):
    """Notre interface de visualisation éprouvée"""
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

def analyser_transformation(input_grid, output_grid, exemple_num):
    """Analyse intuitive comme un humain le ferait"""
    pixels_input = compter_pixels_couleur(input_grid)
    pixels_output = compter_pixels_couleur(output_grid)

    print("   🔄 ANALYSE INTUITIVE:")
    print(f"      Input: {pixels_input}")
    print(f"      Output: {pixels_output}")

    # Identifier les changements de manière intuitive
    changements = []
    for couleur in set(pixels_input.keys()) | set(pixels_output.keys()):
        avant = pixels_input.get(couleur, 0)
        apres = pixels_output.get(couleur, 0)
        if avant != apres:
            changements.append((couleur, avant, apres))

    print("      Changements observés:")
    for couleur, avant, apres in changements:
        emoji = get_emoji_couleur(couleur)
        if avant > apres:
            print(f"         {emoji} {couleur}: {avant} → {apres} (disparaissent)")
        elif apres > avant:
            print(f"         {emoji} {couleur}: {avant} → {apres} (apparaissent)")
        else:
            print(f"         {emoji} {couleur}: {avant} → {apres} (inchangé)")

    # Analyse des patterns spéciaux
    if exemple_num <= 3:
        analyser_patterns_speciaux(input_grid, output_grid)

def get_emoji_couleur(couleur):
    """Notre système de couleurs éprouvé"""
    emojis = {
        1: "🔴", 2: "🟢", 3: "🔵", 4: "🟡",
        5: "🟠", 6: "🟣", 7: "🟤", 8: "⚫", 9: "⚪"
    }
    return emojis.get(couleur, "💎")

def compter_pixels_couleur(grille):
    """Comptage des pixels par couleur"""
    compte = {}
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            couleur = grille[i][j]
            if couleur != 0:
                compte[couleur] = compte.get(couleur, 0) + 1
    return compte

def analyser_patterns_speciaux(input_grid, output_grid):
    """Analyse des patterns spéciaux de manière intuitive"""
    print("      🎯 PATTERNS SPÉCIAUX:")

    # Vérifier si c'est un pattern connu
    if est_pattern_remplissage(input_grid, output_grid):
        print("         🔄 Ressemble à: REMPLISSAGE (comme puzzles 3-4)")
    elif est_pattern_symetrie(input_grid, output_grid):
        print("         🔄 Ressemble à: SYMÉTRIE")
    elif est_pattern_repetition(input_grid, output_grid):
        print("         🔄 Ressemble à: RÉPÉTITION")
    elif est_pattern_couleur(input_grid, output_grid):
        print("         🔄 Ressemble à: TRANSFORMATION COULEUR")
    else:
        print("         ❓ Pattern: NOUVEAU - à découvrir ensemble")

def est_pattern_remplissage(input_grid, output_grid):
    """Détecter si c'est un pattern de remplissage"""
    pixels_ajoutes = []
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 0 and output_grid[i][j] != 0:
                pixels_ajoutes.append((i, j))

    return len(pixels_ajoutes) > 0

def est_pattern_symetrie(input_grid, output_grid):
    """Détecter si c'est un pattern de symétrie"""
    rows, cols = len(input_grid), len(input_grid[0])

    # Vérifier symétrie horizontale
    sym_h = True
    for i in range(rows):
        for j in range(cols // 2):
            if output_grid[i][j] != output_grid[i][cols-1-j]:
                sym_h = False
                break
        if not sym_h:
            break

    # Vérifier symétrie verticale
    sym_v = True
    for i in range(rows // 2):
        for j in range(cols):
            if output_grid[i][j] != output_grid[rows-1-i][j]:
                sym_v = False
                break
        if not sym_v:
            break

    return sym_h or sym_v

def est_pattern_repetition(input_grid, output_grid):
    """Détecter si c'est un pattern de répétition"""
    rows, cols = len(input_grid), len(input_grid[0])

    # Vérifier si le pattern se répète horizontalement
    if cols % 2 == 0:
        moitie_gauche = [row[:cols//2] for row in output_grid]
        moitie_droite = [row[cols//2:] for row in output_grid]

        if moitie_gauche == moitie_droite:
            return True

    # Vérifier si le pattern se répète verticalement
    if rows % 2 == 0:
        moitie_haut = output_grid[:rows//2]
        moitie_bas = output_grid[rows//2:]

        if moitie_haut == moitie_bas:
            return True

    return False

def est_pattern_couleur(input_grid, output_grid):
    """Détecter si c'est un pattern de transformation couleur"""
    changements_couleur = []
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if (input_grid[i][j] != 0 and output_grid[i][j] != 0 and
                input_grid[i][j] != output_grid[i][j]):
                changements_couleur.append((input_grid[i][j], output_grid[i][j]))

    return len(changements_couleur) > 0

def analyser_patterns_generaux():
    """Analyse générale des patterns du puzzle"""
    print("
🎯 ANALYSE GÉNÉRALE PUZZLE 5:"    print("=" * 50)

    with open("data/training/017c7c7b.json", 'r') as f:
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

if __name__ == "__main__":
    analyser_puzzle_5()
    analyser_patterns_generaux()
