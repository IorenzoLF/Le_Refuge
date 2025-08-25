#!/usr/bin/env python3
"""
🔍 EXPLORATION PERSPECTIVE "BLOC" POUR 007bbfb7
L'input 3x3 est un bloc répété selon les couleurs
"""

import json

def explorer_perspective_bloc():
    print("🔍 EXPLORATION PERSPECTIVE BLOC 007bbfb7")
    print("=" * 50)

    try:
        with open("data/training/007bbfb7.json", 'r') as f:
            puzzle_data = json.load(f)

        # Analyser chaque exemple selon la perspective bloc
        for i, exemple in enumerate(puzzle_data['train'], 1):
            print(f"\n🧪 EXEMPLE {i} - PERSPECTIVE BLOC")
            analyser_exemple_bloc(exemple, i)

        # Tester la nouvelle approche
        tester_approche_bloc(puzzle_data)

    except Exception as e:
        print(f"❌ Erreur: {e}")

def analyser_exemple_bloc(exemple, num):
    """Analyser un exemple selon la perspective bloc"""
    input_grid = exemple['input']
    output_grid = exemple['output']

    print("  📥 BLOC INPUT 3x3:")
    for row in input_grid:
        print(f"    {row}")

    print("  📤 OUTPUT 9x9 (répétitions du bloc):")

    # Analyser chaque zone 3x3
    for i in range(3):
        for j in range(3):
            valeur_input = input_grid[i][j]
            start_i, start_j = i * 3, j * 3

            # Extraire la zone 3x3 correspondante
            zone_output = []
            for x in range(3):
                for y in range(3):
                    zone_output.append(output_grid[start_i + x][start_j + y])

            print(f"  📍 Zone ({i},{j}): input={valeur_input} -> output={zone_output}")

            # Analyser la logique
            if valeur_input == 0:
                if all(cell == 0 for cell in zone_output):
                    print("    ✅ Correct: 0 -> zone vide")
                else:
                    print("    ❌ Incohérent: 0 mais zone non vide")
            else:
                # Analyser le pattern pour cette couleur
                analyser_pattern_couleur(valeur_input, zone_output)

def analyser_pattern_couleur(valeur, zone_output):
    """Analyser le pattern associé à une couleur"""
    print(f"    🎨 Pattern pour {valeur}: {zone_output}")

    # Compter les occurrences de chaque valeur dans la zone
    from collections import Counter
    compteur = Counter(zone_output)

    print(f"    📊 Distribution: {dict(compteur)}")

    # Vérifier si c'est cohérent avec la valeur
    if compteur[valeur] > 0:
        print(f"    ✅ Contient la couleur {valeur}")
    else:
        print(f"    ⚠️  Ne contient pas la couleur {valeur}")

def tester_approche_bloc(puzzle_data):
    """Tester l'approche bloc"""
    print("
🧪 TEST APPROCHE BLOC"    print("-" * 30)

    # Patterns découverts par couleur
    patterns_par_couleur = {}

    # Analyser tous les exemples pour construire les patterns
    for exemple in puzzle_data['train']:
        input_grid = exemple['input']
        output_grid = exemple['output']

        for i in range(3):
            for j in range(3):
                valeur = input_grid[i][j]
                if valeur != 0:
                    start_i, start_j = i * 3, j * 3

                    # Extraire le pattern
                    pattern = []
                    for x in range(3):
                        for y in range(3):
                            pattern.append(output_grid[start_i + x][start_j + y])

                    if valeur not in patterns_par_couleur:
                        patterns_par_couleur[valeur] = []
                    patterns_par_couleur[valeur].append(pattern)

    # Afficher les patterns découverts
    print("🎨 PATTERNS DÉCOUVERTS:")
    for couleur in sorted(patterns_par_couleur.keys()):
        patterns = patterns_par_couleur[couleur]
        print(f"  {couleur}: {len(patterns)} occurrences")

        # Vérifier si les patterns sont cohérents
        unique_patterns = set(tuple(p) for p in patterns)
        if len(unique_patterns) == 1:
            print(f"    ✅ Pattern cohérent: {patterns[0]}")
        else:
            print(f"    ⚠️  Patterns différents: {len(unique_patterns)} variantes")
            for i, pattern in enumerate(unique_patterns):
                print(f"      Variante {i+1}: {pattern}")

    # Tester la reconstruction
    print("
🔄 TEST RECONSTRUCTION:"    reussites = 0
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_attendu = exemple['output']

        # Reconstruire selon l'approche bloc
        output_reconstruit = reconstruire_selon_bloc(input_grid, patterns_par_couleur)

        if output_reconstruit == output_attendu:
            print(f"  ✅ Exemple {i}: Reconstruction parfaite")
            reussites += 1
        else:
            print(f"  ❌ Exemple {i}: Reconstruction échoue")
            # Afficher les différences
            differences = 0
            for x in range(9):
                for y in range(9):
                    if output_reconstruit[x][y] != output_attendu[x][y]:
                        differences += 1
            print(f"      {differences} différences détectées")

    print(f"\n📊 Score: {reussites}/5 exemples")

def reconstruire_selon_bloc(input_grid, patterns_par_couleur):
    """Reconstruire l'output selon l'approche bloc"""
    output_grid = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(3):
        for j in range(3):
            valeur = input_grid[i][j]
            start_i, start_j = i * 3, j * 3

            if valeur == 0:
                # Zone vide
                pattern = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            else:
                # Utiliser le pattern de la couleur
                if valeur in patterns_par_couleur and patterns_par_couleur[valeur]:
                    pattern = patterns_par_couleur[valeur][0]  # Prendre le premier pattern
                else:
                    # Pattern par défaut si inconnu
                    pattern = [valeur, valeur, 0, valeur, 0, 0, 0, valeur, valeur]

            # Appliquer le pattern
            for x in range(3):
                for y in range(3):
                    output_grid[start_i + x][start_j + y] = pattern[x * 3 + y]

    return output_grid

def analyser_test_bloc():
    """Analyser l'exemple de test"""
    print("
🧪 ANALYSE TEST:"    try:
        with open("data/training/007bbfb7.json", 'r') as f:
            puzzle_data = json.load(f)

        test_input = puzzle_data['test'][0]['input']
        print("TEST INPUT:")
        for row in test_input:
            print(f"  {row}")

        # Analyser les valeurs présentes
        valeurs_presentes = set()
        for row in test_input:
            for cell in row:
                if cell != 0:
                    valeurs_presentes.add(cell)

        print(f"Valeurs à traiter: {sorted(valeurs_presentes)}")

        # Construire les patterns depuis les exemples d'entraînement
        patterns_par_couleur = {}
        for exemple in puzzle_data['train']:
            input_grid = exemple['input']
            output_grid = exemple['output']

            for i in range(3):
                for j in range(3):
                    valeur = input_grid[i][j]
                    if valeur != 0:
                        start_i, start_j = i * 3, j * 3
                        pattern = []
                        for x in range(3):
                            for y in range(3):
                                pattern.append(output_grid[start_i + x][start_j + y])

                        if valeur not in patterns_par_couleur:
                            patterns_par_couleur[valeur] = pattern

        print("\nPATTERNS POUR LES COULEURS:")
        for couleur in sorted(patterns_par_couleur.keys()):
            print(f"  {couleur}: {patterns_par_couleur[couleur]}")

    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    explorer_perspective_bloc()
    analyser_test_bloc()
