#!/usr/bin/env python3
"""
🎯 ANALYSE PROJECTION LIMITÉE PAR CROIX - 0962bcdd
Nouvelle perspective: projection vaisseau limitée par une forme (croix)
"""

import json

def analyser_projection_croix():
    print("🎯 ANALYSE PROJECTION LIMITÉE PAR CROIX - 0962bcdd")
    print("=" * 60)
    print("🔍 Description utilisateur:")
    print("   ❌ PAS une projection vaisseau infinie")
    print("   ✅ Projection limitée par une CROIX")
    print("   🎨 Croix identifiée par sa couleur")
    print("   📐 Projection limitée à l'intérieur du carré englobant la croix")

    try:
        with open("ARC-AGI-2-main/data/training/0962bcdd.json", 'r') as f:
            puzzle_data = json.load(f)
    except Exception as e:
        print(f"Erreur: {e}")
        return

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i} - ANALYSE CROIX:")
        input_grid = exemple['input']
        output_grid = exemple['output']

        print("INPUT:")
        for row in input_grid:
            print(f"  {row}")

        print("OUTPUT:")
        for row in output_grid:
            print(f"  {row}")

        # Analyser les couleurs et identifier la croix
        analyser_couleurs_et_formes(input_grid, output_grid, i)

def analyser_couleurs_et_formes(input_grid, output_grid, exemple_num):
    """Analyser les couleurs et identifier les formes (croix)"""

    h, w = len(input_grid), len(input_grid[0])

    print("
🎨 ANALYSE COULEURS:"    # Compter les couleurs dans l'input
    couleurs_input = {}
    for i in range(h):
        for j in range(w):
            cell = input_grid[i][j]
            if cell != 0:
                if cell not in couleurs_input:
                    couleurs_input[cell] = []
                couleurs_input[cell].append((i, j))

    print(f"Couleurs présentes: {list(couleurs_input.keys())}")

    for couleur, positions in couleurs_input.items():
        print(f"  Couleur {couleur}: {len(positions)} positions {positions}")

        # Analyser la forme créée par cette couleur
        if len(positions) >= 5:  # Suffisamment de positions pour former une forme
            analyser_forme(positions, couleur, h, w)

    # Analyser l'output
    print("
📤 ANALYSE OUTPUT:"    couleurs_output = {}
    for i in range(h):
        for j in range(w):
            cell = output_grid[i][j]
            if cell != 0:
                if cell not in couleurs_output:
                    couleurs_output[cell] = []
                couleurs_output[cell].append((i, j))

    print(f"Couleurs output: {list(couleurs_output.keys())}")

    for couleur, positions in couleurs_output.items():
        print(f"  Couleur {couleur}: {len(positions)} positions")

def analyser_forme(positions, couleur, h, w):
    """Analyser si les positions forment une croix"""

    print(f"  🔍 Analyse forme couleur {couleur}:")

    # Créer une grille pour visualiser la forme
    grille_forme = [[0 for _ in range(w)] for _ in range(h)]
    for i, j in positions:
        grille_forme[i][j] = 1

    print("  Forme visuelle:")
    for row in grille_forme:
        print(f"    {row}")

    # Analyser les caractéristiques de la forme
    rows_with_pixels = set(i for i, j in positions)
    cols_with_pixels = set(j for i, j in positions)

    print(f"  Lignes occupées: {sorted(rows_with_pixels)}")
    print(f"  Colonnes occupées: {sorted(cols_with_pixels)}")

    # Détecter si c'est une forme croisée
    if len(rows_with_pixels) >= 3 and len(cols_with_pixels) >= 3:
        # Vérifier si c'est centré
        center_row = h // 2
        center_col = w // 2

        # Vérifier présence au centre
        has_center = (center_row, center_col) in positions
        print(f"  Centre ({center_row}, {center_col}): {'✅' if has_center else '❌'}")

        # Analyser la structure
        structure = analyser_structure_croix(positions, center_row, center_col, h, w)
        print(f"  Structure: {structure}")

def analyser_structure_croix(positions, center_row, center_col, h, w):
    """Analyser si la structure correspond à une croix"""

    # Convertir positions en set pour recherche rapide
    pos_set = set(positions)

    # Vérifier la présence de branches
    branches = {
        'haut': (center_row - 1, center_col) in pos_set,
        'bas': (center_row + 1, center_col) in pos_set,
        'gauche': (center_row, center_col - 1) in pos_set,
        'droite': (center_row, center_col + 1) in pos_set
    }

    print(f"    Branches: {branches}")

    # Compter les branches présentes
    branches_presentes = sum(branches.values())

    if branches_presentes >= 2:
        return f"croix avec {branches_presentes} branches"
    else:
        return "forme non-croix"

def analyser_projection_limitee():
    """Analyser le concept de projection limitée"""

    print("
🧠 ANALYSE CONCEPT PROJECTION LIMITÉE:"    print("=" * 40)

    print("🎯 HYPOTHÈSE UTILISATEUR:")
    print("   1. 📍 Il y a une CROIX dans l'input")
    print("   2. 🎨 Croix identifiée par sa couleur")
    print("   3. 📐 Carré englobant la croix défini")
    print("   4. 🚀 Projection limitée à l'intérieur de ce carré")

    print("
🔬 LOGIQUE TECHNIQUE POSSIBLE:"    print("   1. 🔍 Détecter la forme (croix) dans l'input")
    print("   2. 📏 Calculer le rectangle englobant")
    print("   3. 🎯 Appliquer la projection vaisseau")
    print("   4. ✂️ Masquer en dehors du rectangle")
    print("   5. 📤 Générer l'output final")

    print("
💡 IMPLICATIONS:"    print("   ✅ Pattern plus sophistiqué que projection simple")
    print("   ✅ Nécessite détection de formes géométriques")
    print("   ✅ Combinaison: projection + masquage géométrique")
    print("   🎯 Expliquerait pourquoi 83% → peut aller à 100%")

def main():
    analyser_projection_croix()
    analyser_projection_limitee()

    print("
🎉 SYNTHÈSE:"    print("=" * 20)
    print("✅ Découverte majeure: projection limitée par forme géométrique")
    print("🎯 Nouveau pattern: 'projection_masquee_geometrique'")
    print("🚀 Potentiel: 83% → 100% avec ce pattern avancé")
    print("🔍 Prochaine étape: implémenter la détection de formes")

if __name__ == "__main__":
    main()
