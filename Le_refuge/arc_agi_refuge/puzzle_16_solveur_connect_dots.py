#!/usr/bin/env python3
"""
🎯 SOLVEUR PUZZLE 16 - CONNECT THE DOTS
06df4c85 - Connexion intelligente des points
"""

import json

def solveur_connect_dots():
    print("🎯 SOLVEUR PUZZLE 16 - CONNECT THE DOTS")
    print("=" * 50)
    print("🎨 TON INTUITION : CONNECT THE DOTS")
    print("🔍 Connexion intelligente des points avec préservation des motifs")

    try:
        with open("ARC-AGI-2-main/data/training/06df4c85.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("❌ Fichier non trouvé")
        return False

    print("
📊 ANALYSE DU PUZZLE:"    print(f"   Dimensions: 23x23 → 23x23")
    print("   Pixels: 305 → 341 (36 pixels de connexion)")
    print("   Couleurs: [1, 2, 4, 8, 9]")

    # Analyser les patterns de connexion
    patterns_connexion = analyser_patterns_connexion(puzzle_data['train'][0])

    print("
🎨 PATTERNS DE CONNEXION IDENTIFIÉS:"    for i, pattern in enumerate(patterns_connexion):
        print(f"   {i+1}. {pattern}")

    # Tester le solveur
    print("
🧪 TEST SOLVEUR CONNECT THE DOTS:"    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_attendu = exemple['output']

        prediction = appliquer_connexions(input_grid, patterns_connexion)

        is_correct = comparer_grilles(prediction, output_attendu)

        if is_correct:
            success_count += 1

        print(f"   Exemple {i}: {'✅ SUCCÈS' if is_correct else '❌ ÉCHEC'}")

    print(f"   📊 Score: {success_count}/3")

    if success_count == 3:
        print("   🎉 SUCCÈS PARFAIT ! Connect the dots confirmé !")
        print("   🌟 Toutes tes intuitions étaient exactes !")
        return True
    else:
        print("   🔍 Analyse plus fine nécessaire")
        return False

def analyser_patterns_connexion(exemple):
    """Analyser les patterns de connexion dans l'exemple"""
    input_grid = exemple['input']
    output_grid = exemple['output']

    patterns = []

    # Analyser par lignes
    for i in range(len(input_grid)):
        ligne_input = input_grid[i]
        ligne_output = output_grid[i]

        # Trouver les positions des pixels dans la ligne
        positions_input = [j for j in range(len(ligne_input)) if ligne_input[j] != 0]
        positions_output = [j for j in range(len(ligne_output)) if ligne_output[j] != 0]

        if positions_input != positions_output:
            # Il y a eu des ajouts de connexion
            ajouts = [pos for pos in positions_output if pos not in positions_input]
            if ajouts:
                couleur_connexion = ligne_output[ajouts[0]]
                patterns.append(f"Ligne {i}: connexion avec couleur {couleur_connexion} aux positions {ajouts}")

    # Analyser par colonnes
    for j in range(len(input_grid[0])):
        col_input = [input_grid[i][j] for i in range(len(input_grid))]
        col_output = [output_grid[i][j] for i in range(len(output_grid))]

        positions_input = [i for i in range(len(col_input)) if col_input[i] != 0]
        positions_output = [i for i in range(len(col_output)) if col_output[i] != 0]

        if positions_input != positions_output:
            ajouts = [pos for pos in positions_output if pos not in positions_input]
            if ajouts:
                couleur_connexion = col_output[ajouts[0]]
                patterns.append(f"Colonne {j}: connexion avec couleur {couleur_connexion} aux positions {ajouts}")

    return patterns

def appliquer_connexions(input_grid, patterns_connexion):
    """Appliquer les connexions basées sur les patterns identifiés"""
    output_grid = [row[:] for row in input_grid]  # Copie profonde

    # Appliquer les connexions horizontales (lignes)
    for i in range(len(input_grid)):
        ligne = output_grid[i]

        # Trouver les groupes de pixels de même couleur dans la ligne
        j = 0
        while j < len(ligne):
            if ligne[j] != 0:
                couleur = ligne[j]
                # Étendre vers la droite jusqu'à trouver un pixel différent ou vide
                k = j + 1
                while k < len(ligne) and ligne[k] == 0:
                    ligne[k] = couleur  # Remplir les espaces
                    k += 1
                j = k
            else:
                j += 1

    # Appliquer les connexions verticales (colonnes)
    for j in range(len(input_grid[0])):
        # Collecter les couleurs de la colonne
        couleurs_colonne = []
        for i in range(len(input_grid)):
            if output_grid[i][j] != 0:
                couleurs_colonne.append((i, output_grid[i][j]))

        # Connecter les pixels de même couleur dans la colonne
        if len(couleurs_colonne) > 1:
            couleur_principale = couleurs_colonne[0][1]
            for i in range(len(output_grid)):
                if output_grid[i][j] == 0:
                    # Vérifier s'il faut connecter
                    # Connecter si entouré de pixels de même couleur
                    if ((i > 0 and output_grid[i-1][j] == couleur_principale) and
                        (i < len(output_grid)-1 and output_grid[i+1][j] == couleur_principale)):
                        output_grid[i][j] = couleur_principale

    # Appliquer des connexions intelligentes basées sur les motifs observés
    appliquer_connexions_intelligentes(output_grid, input_grid)

    return output_grid

def appliquer_connexions_intelligentes(output_grid, input_grid):
    """Appliquer des connexions plus intelligentes basées sur les motifs"""

    # 1. Connecter les pixels isolés aux groupes proches
    for i in range(len(output_grid)):
        for j in range(len(output_grid[0])):
            if output_grid[i][j] == 0 and input_grid[i][j] == 0:  # Case vide dans les deux
                # Vérifier les voisins pour déterminer s'il faut connecter
                voisins = []
                if i > 0 and output_grid[i-1][j] != 0:
                    voisins.append(output_grid[i-1][j])
                if i < len(output_grid)-1 and output_grid[i+1][j] != 0:
                    voisins.append(output_grid[i+1][j])
                if j > 0 and output_grid[i][j-1] != 0:
                    voisins.append(output_grid[i][j-1])
                if j < len(output_grid[0])-1 and output_grid[i][j+1] != 0:
                    voisins.append(output_grid[i][j+1])

                # Si tous les voisins ont la même couleur, connecter
                if len(voisins) >= 3 and len(set(voisins)) == 1:
                    output_grid[i][j] = voisins[0]

    # 2. Étendre les blocs de couleur
    for i in range(len(output_grid)):
        for j in range(len(output_grid[0])):
            if output_grid[i][j] == 0:
                # Vérifier si c'est un espace dans un bloc rectangulaire
                bloc_couleur = detecter_bloc_rectangulaire(output_grid, i, j)
                if bloc_couleur:
                    output_grid[i][j] = bloc_couleur

def detecter_bloc_rectangulaire(grid, x, y):
    """Détecter si la position (x,y) fait partie d'un bloc rectangulaire"""
    # Cette fonction simplifiée vérifie les patterns de bloc
    # En réalité, elle devrait analyser la structure complète

    # Vérifier les motifs de 2x2
    if (x < len(grid)-1 and y < len(grid[0])-1 and
        grid[x][y+1] != 0 and grid[x+1][y] != 0 and grid[x+1][y+1] != 0):
        return grid[x][y+1]  # Retourner la couleur du bloc

    # Vérifier les motifs horizontaux
    if y > 0 and y < len(grid[0])-1 and grid[x][y-1] != 0 and grid[x][y+1] != 0:
        return grid[x][y-1]

    # Vérifier les motifs verticaux
    if x > 0 and x < len(grid)-1 and grid[x-1][y] != 0 and grid[x+1][y] != 0:
        return grid[x-1][y]

    return None

def comparer_grilles(g1, g2):
    """Comparer deux grilles"""
    if len(g1) != len(g2) or len(g1[0]) != len(g2[0]):
        return False

    for i in range(len(g1)):
        for j in range(len(g1[0])):
            if g1[i][j] != g2[i][j]:
                return False

    return True

def visualiser_grille(grille, titre=""):
    """Visualisation simple d'une grille"""
    if titre:
        print(f"\n{titre}:")
    for i, row in enumerate(grille):
        row_str = ""
        for cell in row:
            if cell == 0:
                row_str += "."
            elif cell == 1:
                row_str += "R"
            elif cell == 2:
                row_str += "G"
            elif cell == 4:
                row_str += "Y"
            elif cell == 8:
                row_str += "B"
            elif cell == 9:
                row_str += "D"
            else:
                row_str += "?"
        print(f"  {i:2}: {row_str}")

if __name__ == "__main__":
    solveur_connect_dots()
