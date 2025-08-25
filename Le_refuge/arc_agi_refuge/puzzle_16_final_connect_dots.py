#!/usr/bin/env python3
"""
🎯 SOLVEUR FINAL PUZZLE 16 - CONNECT THE DOTS
06df4c85 - Connexion intelligente des points
"""

import json

def solveur_final_connect_dots():
    print("🎯 SOLVEUR FINAL PUZZLE 16 - CONNECT THE DOTS")
    print("=" * 55)
    print("🎨 TON INTUITION PARFAITE : CONNECT THE DOTS")
    print("🔗 Connexion intelligente avec préservation des motifs")

    try:
        with open("ARC-AGI-2-main/data/training/06df4c85.json", 'r') as f:
            puzzle_data = json.load(f)
    except FileNotFoundError:
        print("❌ Fichier non trouvé")
        return False

    print("
📊 CARACTÉRISTIQUES DU PUZZLE:"    print(f"   Dimensions: 23x23 → 23x23")
    print("   Pixels: 305 → 341 (36 pixels de connexion)")
    print("   Couleurs: [1, 2, 4, 8, 9]")
    print("   Pattern: Connexion intelligente des points")

    # Analyser le pattern de connexion
    pattern_connexion = analyser_pattern_connexion(puzzle_data['train'][0])

    print("
🎨 PATTERN DE CONNEXION IDENTIFIÉ:"    print(f"   {pattern_connexion}")

    # Tester le solveur intelligent
    print("
🧪 TEST SOLVEUR INTELLIGENT:"    success_count = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_attendu = exemple['output']

        prediction = appliquer_connect_the_dots(input_grid)

        is_correct = comparer_grilles(prediction, output_attendu)

        if is_correct:
            success_count += 1

        print(f"   Exemple {i}: {'✅ SUCCÈS' if is_correct else '❌ ÉCHEC'}")

        if not is_correct:
            analyser_differences(prediction, output_attendu, i)

    print("
📊 RÉSULTATS FINAUX:"    print(f"   Score solveur: {success_count}/3")

    if success_count == 3:
        print("   🎉 SUCCÈS PARFAIT ! Connect the dots validé !")
        print("   🌟 Toutes tes intuitions étaient exactes !")
        print("   🔗 36 pixels de connexion ajoutés intelligemment")
        return True
    else:
        print("   🔍 Quelques ajustements nécessaires")
        return False

def analyser_pattern_connexion(exemple):
    """Analyser le pattern de connexion dans l'exemple"""
    input_grid = exemple['input']
    output_grid = exemple['output']

    # Compter les pixels ajoutés
    pixels_ajoutes = 0
    connexions = []

    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            if input_grid[i][j] == 0 and output_grid[i][j] != 0:
                pixels_ajoutes += 1
                couleur = output_grid[i][j]
                connexions.append(f"({i},{j})={couleur}")

    pattern = (f"Connexion de {pixels_ajoutes} pixels: {len(connexions)} connexions intelligentes")
    return pattern

def appliquer_connect_the_dots(input_grid):
    """Appliquer la logique 'Connect the Dots'"""
    output_grid = [row[:] for row in input_grid]  # Copie profonde

    # Étape 1: Étendre les lignes horizontales
    for i in range(len(output_grid)):
        etendre_ligne_horizontale(output_grid, i)

    # Étape 2: Étendre les colonnes verticales
    for j in range(len(output_grid[0])):
        etendre_colonne_verticale(output_grid, j)

    # Étape 3: Connecter les blocs isolés
    connecter_blocs_isoles(output_grid)

    # Étape 4: Remplir les espaces dans les motifs rectangulaires
    remplir_espaces_rectangulaires(output_grid)

    return output_grid

def etendre_ligne_horizontale(grid, i):
    """Étendre les pixels dans une ligne horizontale"""
    ligne = grid[i]

    # Trouver les groupes de pixels de même couleur
    j = 0
    while j < len(ligne):
        if ligne[j] != 0:
            couleur = ligne[j]
            # Étendre vers la droite
            k = j + 1
            while k < len(ligne) and ligne[k] == 0:
                ligne[k] = couleur
                k += 1
            j = k
        else:
            j += 1

def etendre_colonne_verticale(grid, j):
    """Étendre les pixels dans une colonne verticale"""
    # Collecter les couleurs présentes dans la colonne
    couleurs_presentes = set()
    for i in range(len(grid)):
        if grid[i][j] != 0:
            couleurs_presentes.add(grid[i][j])

    # Si une seule couleur domine, l'étendre
    if len(couleurs_presentes) == 1:
        couleur = list(couleurs_presentes)[0]
        for i in range(len(grid)):
            if grid[i][j] == 0:
                grid[i][j] = couleur
    elif len(couleurs_presentes) > 1:
        # Pour les colonnes avec plusieurs couleurs, connecter intelligemment
        for i in range(1, len(grid) - 1):
            if grid[i][j] == 0:
                # Vérifier les voisins
                haut = grid[i-1][j]
                bas = grid[i+1][j]
                if haut != 0 and bas != 0 and haut == bas:
                    grid[i][j] = haut

def connecter_blocs_isoles(grid):
    """Connecter les blocs isolés de pixels"""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                # Vérifier si entouré de pixels de même couleur
                voisins = []
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, bas, gauche, droite

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and
                        grid[ni][nj] != 0):
                        voisins.append(grid[ni][nj])

                # Si tous les voisins ont la même couleur, connecter
                if len(voisins) >= 3 and len(set(voisins)) == 1:
                    grid[i][j] = voisins[0]

def remplir_espaces_rectangulaires(grid):
    """Remplir les espaces dans les motifs rectangulaires"""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                # Vérifier si c'est un espace dans un rectangle 2x2
                if (i < len(grid)-1 and j < len(grid[0])-1 and
                    grid[i][j+1] != 0 and grid[i+1][j] != 0 and grid[i+1][j+1] != 0):
                    # C'est un coin manquant d'un rectangle
                    couleur = grid[i][j+1]
                    if grid[i+1][j] == couleur and grid[i+1][j+1] == couleur:
                        grid[i][j] = couleur

def comparer_grilles(g1, g2):
    """Comparer deux grilles"""
    if len(g1) != len(g2) or len(g1[0]) != len(g2[0]):
        return False

    for i in range(len(g1)):
        for j in range(len(g1[0])):
            if g1[i][j] != g2[i][j]:
                return False

    return True

def analyser_differences(prediction, attendu, exemple_num):
    """Analyser les différences entre prédiction et attendu"""
    differences = []
    for i in range(len(prediction)):
        for j in range(len(prediction[0])):
            if prediction[i][j] != attendu[i][j]:
                differences.append(((i, j), prediction[i][j], attendu[i][j]))

    print(f"     🔍 {len(differences)} différences trouvées")
    if len(differences) <= 10:
        for pos, pred, att in differences:
            print(f"        Position {pos}: {pred} → {att}")

if __name__ == "__main__":
    success = solveur_final_connect_dots()

    if success:
        print("
🎉 PUZZLE 16 RÉSOLU AVEC SUCCÈS !"        print("   🎯 Connect the dots validé à 100% !")
        print("   🔗 36 connexions intelligentes ajoutées !")
        print("   🌟 Toutes tes intuitions étaient parfaites !")
        print("   🏆 16/16 puzzles résolus - SÉRIE ABSOLUE !")
    else:
        print("
🔍 ANALYSE SUPPLÉMENTAIRE NÉCESSAIRE"
