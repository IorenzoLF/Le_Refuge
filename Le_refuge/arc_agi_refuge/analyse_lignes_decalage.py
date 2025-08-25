#!/usr/bin/env python3
"""
📊 ANALYSE LIGNES AVEC DÉCALAGE - 05269061
Nouvelle perspective: reconstruction par lignes avec décalage diagonal
"""

import json
from collections import Counter

def analyser_lignes_decalage():
    print("📊 ANALYSE LIGNES AVEC DÉCALAGE - 05269061")
    print("=" * 60)
    print("🎯 Description utilisateur: reconstruction par lignes")
    print("🔄 Pattern: bleu, rouge, jaune avec décalage")
    print("📍 Infos importantes: diagonales + nombre de couleurs")

    try:
        with open("ARC-AGI-2-main/data/training/05269061.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i} - ANALYSE PAR LIGNES:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        print("INPUT:")
        for j, row in enumerate(input_grid):
            print(f"  Ligne {j}: {row}")

        print("OUTPUT:")
        for j, row in enumerate(output_grid):
            print(f"  Ligne {j}: {row}")

        # Analyser les patterns par ligne
        analyser_pattern_lignes(output_grid, i)

def analyser_pattern_lignes(output_grid, exemple_num):
    """Analyser le pattern de lignes avec décalage"""

    h, w = len(output_grid), len(output_grid[0])

    print("
🔍 ANALYSE PATTERNS LIGNES:"    # Identifier les lignes avec des couleurs
    lignes_avec_couleurs = []
    for i in range(h):
        if any(cell != 0 for cell in output_grid[i]):
            lignes_avec_couleurs.append(i)

    print(f"Lignes avec couleurs: {lignes_avec_couleurs}")

    # Analyser la dernière ligne comme référence
    derniere_ligne = output_grid[-1]
    print(f"\n📍 DERNIÈRE LIGNE (référence): {derniere_ligne}")

    # Extraire le pattern de base
    pattern_base = []
    positions_couleurs = []
    for j, cell in enumerate(derniere_ligne):
        if cell != 0:
            pattern_base.append(cell)
            positions_couleurs.append(j)

    print(f"Pattern base: {pattern_base}")
    print(f"Positions couleurs: {positions_couleurs}")

    # Analyser les autres lignes avec décalage
    print("
🔄 ANALYSE DÉCALAGE:"    for i in range(h-1):  # Toutes les lignes sauf la dernière
        ligne_courante = output_grid[i]
        print(f"\nLigne {i}: {ligne_courante}")

        # Chercher le pattern avec décalage
        decalages_possibles = range(-w, w+1)  # Décalages possibles
        meilleur_decalage = None
        meilleur_score = 0

        for decalage in decalages_possibles:
            score = 0
            correspondances = []

            for j, couleur in enumerate(pattern_base):
                pos_originale = positions_couleurs[j]
                pos_decalage = pos_originale + decalage

                if 0 <= pos_decalage < w:
                    couleur_trouvee = ligne_courante[pos_decalage]
                    if couleur_trouvee == couleur:
                        score += 1
                        correspondances.append(f"✅ pos{j}({pos_originale}+{decalage}={pos_decalage}): {couleur}")
                    else:
                        correspondances.append(f"❌ pos{j}({pos_originale}+{decalage}={pos_decalage}): {couleur_trouvee}≠{couleur}")
                else:
                    correspondances.append(f"⚠️ pos{j}: hors limites")

            if score > meilleur_score:
                meilleur_score = score
                meilleur_decalage = decalage

        print(f"  Meilleur décalage: {meilleur_decalage} (score: {meilleur_score}/{len(pattern_base)})")
        if meilleur_score > 0:
            print(f"  Correspondances: {meilleur_score} réussies")

    # Analyser la logique de décalage
    analyser_logique_decalage(output_grid, pattern_base, positions_couleurs)

def analyser_logique_decalage(output_grid, pattern_base, positions_couleurs):
    """Analyser la logique derrière le décalage"""

    h, w = len(output_grid), len(output_grid[0])

    print("
🎯 ANALYSE LOGIQUE DÉCALAGE:"    print(f"Pattern base: {pattern_base}")
    print(f"Longueur pattern: {len(pattern_base)} couleurs")

    # Vérifier si c'est un décalage régulier
    print("
📈 VÉRIFICATION DÉCALAGE RÉGULIER:"    decalages = []

    for i in range(h-1):
        ligne_courante = output_grid[i]

        # Chercher la position du premier pixel de couleur
        premier_pixel_pos = None
        for j, cell in enumerate(ligne_courante):
            if cell != 0:
                premier_pixel_pos = j
                break

        if premier_pixel_pos is not None:
            decalage = premier_pixel_pos - positions_couleurs[0]
            decalages.append(decalage)
            print(f"  Ligne {i}: premier pixel à pos {premier_pixel_pos} (décalage: {decalage})")

    print(f"Décalages calculés: {decalages}")

    # Vérifier si les décalages sont réguliers
    if len(set(decalages)) == 1:
        print(f"✅ DÉCALAGE RÉGULIER: {decalages[0]} positions")
    else:
        print(f"⚠️ DÉCALAGES VARIABLES: {decalages}")

    # Analyser le pattern complet
    analyser_pattern_complet(output_grid, pattern_base, positions_couleurs)

def analyser_pattern_complet(output_grid, pattern_base, positions_couleurs):
    """Analyser le pattern complet de reconstruction"""

    h, w = len(output_grid), len(output_grid[0])

    print("
🔧 RECONSTRUCTION COMPLÈTE:"    print("Hypothèse: Chaque ligne = pattern base avec décalage")

    # Calculer le décalage par ligne
    decalage_par_ligne = []
    for i in range(h):
        ligne = output_grid[i]

        # Trouver la position du pattern dans cette ligne
        pattern_trouve = False
        decalage = 0

        for decalage_test in range(-w, w):
            match = True
            for j, couleur in enumerate(pattern_base):
                pos = positions_couleurs[j] + decalage_test
                if 0 <= pos < w:
                    if ligne[pos] != couleur:
                        match = False
                        break
                else:
                    match = False
                    break

            if match:
                decalage = decalage_test
                pattern_trouve = True
                break

        if pattern_trouve:
            decalage_par_ligne.append(decalage)
            print(f"  Ligne {i}: décalage {decalage} ✅")
        else:
            decalage_par_ligne.append(None)
            print(f"  Ligne {i}: pattern non trouvé ❌")

    # Analyser la progression des décalages
    decalages_valides = [d for d in decalage_par_ligne if d is not None]
    print(f"\n📊 PROGRESSION DÉCALAGES: {decalages_valides}")

    if len(decalages_valides) > 1:
        differences = []
        for k in range(len(decalages_valides)-1):
            diff = decalages_valides[k+1] - decalages_valides[k]
            differences.append(diff)

        print(f"Différences entre décalages: {differences}")

        if len(set(differences)) == 1:
            print(f"✅ PROGRESSION RÉGULIÈRE: {differences[0]} par ligne")
        else:
            print(f"⚠️ PROGRESSION IRRÉGULIÈRE: {differences}")

def main():
    analyser_lignes_decalage()

if __name__ == "__main__":
    main()
