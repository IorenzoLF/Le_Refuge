#!/usr/bin/env python3
"""
🏗️ ANALYSE ESCALIERS DE COULEUR PUZZLE 11 (05269061)
Ton intuition : "construire des escaliers de couleur"
"""

import json

def analyser_escaliers():
    """Analyser les escaliers de couleur selon ton intuition"""
    print("🏗️ ANALYSE ESCALIERS DE COULEUR")
    print("=" * 50)
    print("🎯 TON INTUITION : CONSTRUIRE DES ESCALIERS")
    print("🏢 Pattern géométrique d'escaliers colorés")

    with open("data/training/05269061.json", 'r') as f:
        puzzle_data = json.load(f)

    # Analyser chaque exemple avec l'œil de l'escalier
    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🏗️ EXEMPLE {i} - RECHERCHE D'ESCALIERS")
        print("-" * 40)

        input_grid = exemple['input']
        output_grid = exemple['output']

        print("📥 INPUT:")
        visualiser_avec_escaliers(input_grid, "INPUT")

        print("📤 OUTPUT:")
        visualiser_avec_escaliers(output_grid, "OUTPUT")

        # Analyser les patterns d'escaliers
        analyser_pattern_escaliers(input_grid, output_grid, i)

def visualiser_avec_escaliers(grille, nom):
    """Visualisation avec détection potentielle d'escaliers"""
    print(f"   {nom} {len(grille)}x{len(grille[0])}:")

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
        print(f"      {row_str}")

def analyser_pattern_escaliers(input_grid, output_grid, exemple_num):
    """Analyser les patterns d'escaliers selon ton idée"""
    print("🏗️ ANALYSE PATTERN ESCALIERS:")

    # Chercher des patterns en escalier dans l'input
    escaliers_input = detecter_escaliers(input_grid)
    print(f"   📥 Escaliers détectés input: {len(escaliers_input)}")

    # Chercher des patterns en escalier dans l'output
    escaliers_output = detecter_escaliers(output_grid)
    print(f"   📤 Escaliers détectés output: {len(escaliers_output)}")

    # Analyser la transformation
    analyser_transformation_escaliers(escaliers_input, escaliers_output, exemple_num)

    # Chercher d'autres patterns géométriques
    analyser_geometrie_generale(input_grid, output_grid)

def detecter_escaliers(grille):
    """Détecter des patterns en escalier"""
    escaliers = []
    rows = len(grille)
    cols = len(grille[0])

    # Chercher escaliers horizontaux (même ligne, progression)
    for i in range(rows):
        escalier = detecter_escalier_horizontal(grille[i])
        if escalier:
            escaliers.append(f"Horizontal ligne {i}: {escalier}")

    # Chercher escaliers verticaux (même colonne, progression)
    for j in range(cols):
        colonne = [grille[i][j] for i in range(rows)]
        escalier = detecter_escalier_vertical(colonne)
        if escalier:
            escaliers.append(f"Vertical colonne {j}: {escalier}")

    # Chercher escaliers diagonaux
    escaliers_diagonaux = detecter_escaliers_diagonaux(grille)
    escaliers.extend(escaliers_diagonaux)

    return escaliers

def detecter_escalier_horizontal(ligne):
    """Détecter un escalier horizontal dans une ligne"""
    couleurs_presentes = [cell for cell in ligne if cell != 0]

    if len(couleurs_presentes) < 2:
        return None

    # Chercher une progression de couleurs
    progression = []
    derniere_couleur = None

    for cell in ligne:
        if cell != 0:
            if derniere_couleur != cell:
                progression.append(cell)
                derniere_couleur = cell

    if len(progression) >= 2:
        return f"Progression: {progression}"

    return None

def detecter_escalier_vertical(colonne):
    """Détecter un escalier vertical dans une colonne"""
    couleurs_presentes = [cell for cell in colonne if cell != 0]

    if len(couleurs_presentes) < 2:
        return None

    # Chercher une progression de couleurs
    progression = []
    derniere_couleur = None

    for cell in colonne:
        if cell != 0:
            if derniere_couleur != cell:
                progression.append(cell)
                derniere_couleur = cell

    if len(progression) >= 2:
        return f"Progression: {progression}"

    return None

def detecter_escaliers_diagonaux(grille):
    """Détecter des escaliers diagonaux"""
    escaliers = []
    rows = len(grille)
    cols = len(grille[0])

    # Diagonale principale
    diagonale_principale = []
    for i in range(min(rows, cols)):
        diagonale_principale.append(grille[i][i])

    escalier = detecter_escalier_horizontal(diagonale_principale)
    if escalier:
        escaliers.append(f"Diagonale principale: {escalier}")

    # Diagonale secondaire
    diagonale_secondaire = []
    for i in range(min(rows, cols)):
        diagonale_secondaire.append(grille[i][cols-1-i])

    escalier = detecter_escalier_horizontal(diagonale_secondaire)
    if escalier:
        escaliers.append(f"Diagonale secondaire: {escalier}")

    return escaliers

def analyser_transformation_escaliers(escaliers_input, escaliers_output, exemple_num):
    """Analyser la transformation des escaliers"""
    print("🔄 TRANSFORMATION ESCALIERS:")

    print("   📥 Input patterns:")
    for esc in escaliers_input:
        print(f"      {esc}")

    print("   📤 Output patterns:")
    for esc in escaliers_output:
        print(f"      {esc}")

    # Analyser la différence
    if escaliers_input and escaliers_output:
        print("   🎯 Transformation détectée !")
    elif escaliers_input and not escaliers_output:
        print("   ❌ Perte des patterns d'escalier")
    elif not escaliers_input and escaliers_output:
        print("   ✨ Création de patterns d'escalier")
    else:
        print("   ❓ Pas de patterns d'escalier clairs")

def analyser_geometrie_generale(input_grid, output_grid):
    """Analyser la géométrie générale"""
    print("🔍 ANALYSE GÉOMÉTRIE GÉNÉRALE:")

    # Compter les pixels par couleur
    couleurs_input = compter_couleurs(input_grid)
    couleurs_output = compter_couleurs(output_grid)

    print(f"   📥 Couleurs input: {couleurs_input}")
    print(f"   📤 Couleurs output: {couleurs_output}")

    # Analyser les changements
    changements = []
    for couleur in set(couleurs_input.keys()) | set(couleurs_output.keys()):
        avant = couleurs_input.get(couleur, 0)
        apres = couleurs_output.get(couleur, 0)
        if avant != apres:
            changements.append((couleur, avant, apres))

    print("   🔄 Changements détectés:")
    for couleur, avant, apres in changements:
        emoji = get_emoji_couleur(couleur)
        print(f"      {emoji} {couleur}: {avant} → {apres}")

def compter_couleurs(grille):
    """Compter les pixels par couleur"""
    compte = {}
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            couleur = grille[i][j]
            if couleur != 0:
                compte[couleur] = compte.get(couleur, 0) + 1
    return compte

def get_emoji_couleur(couleur):
    """Emoji des couleurs"""
    emojis = {
        1: "🔴", 2: "🟢", 3: "🔵", 4: "🟡",
        5: "🟠", 6: "🟣", 7: "🟤", 8: "⚫"
    }
    return emojis.get(couleur, "💎")

def analyse_generale_escaliers():
    """Analyse générale du pattern d'escaliers"""
    print("
🏗️ ANALYSE GÉNÉRALE PATTERN ESCALIERS"    print("=" * 60)

    with open("data/training/05269061.json", 'r') as f:
        puzzle_data = json.load(f)

    total_escaliers_input = 0
    total_escaliers_output = 0

    for i, exemple in enumerate(puzzle_data['train'], 1):
        escaliers_input = detecter_escaliers(exemple['input'])
        escaliers_output = detecter_escaliers(exemple['output'])

        total_escaliers_input += len(escaliers_input)
        total_escaliers_output += len(escaliers_output)

    print(f"📊 Total escaliers input: {total_escaliers_input}")
    print(f"📊 Total escaliers output: {total_escaliers_output}")

    if total_escaliers_input > 0 or total_escaliers_output > 0:
        print("✅ PATTERNS D'ESCALIERS DÉTECTÉS !")
        print("🎯 Ton intuition est probablement JUSTE !")
    else:
        print("❓ Pas de patterns d'escaliers évidents")
        print("🔍 Peut-être un pattern d'escaliers plus subtil")

if __name__ == "__main__":
    analyser_escaliers()
    analyse_generale_escaliers()
