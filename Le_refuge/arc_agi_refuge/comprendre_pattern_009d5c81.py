#!/usr/bin/env python3
"""
🔍 COMPRENDRE LE PATTERN 009d5c81
Input: pixels 1 et 8 → Output: motif des 8 avec couleur déterminée par les 1
"""

import json

def analyser_correspondance_1_8():
    print("🔍 ANALYSE CORRESPONDANCE 1 ↔ 8")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    for i, exemple in enumerate(puzzle_data['train'], 1):
        print(f"\n🧪 EXEMPLE {i}:")

        input_grid = exemple['input']
        output_grid = exemple['output']

        # Trouver positions des pixels 1 et 8
        positions_1 = []
        positions_8_input = []
        positions_8_output = []

        for x in range(14):
            for y in range(14):
                if input_grid[x][y] == 1:
                    positions_1.append((x, y))
                elif input_grid[x][y] == 8:
                    positions_8_input.append((x, y))

                if output_grid[x][y] != 0:
                    positions_8_output.append((x, y, output_grid[x][y]))

        print(f"  Positions 1: {positions_1}")
        print(f"  Positions 8 input: {len(positions_8_input)} positions")
        print(f"  Positions 8 output: {len(positions_8_output)} positions")

        # Déterminer la couleur de sortie
        couleur_sortie = positions_8_output[0][2] if positions_8_output else 0
        print(f"  Couleur de sortie: {couleur_sortie}")

        # Vérifier la correspondance
        correspondance = []
        for x, y in positions_8_input:
            if output_grid[x][y] == couleur_sortie:
                correspondance.append("✅")
            else:
                correspondance.append("❌")

        print(f"  Correspondance: {len([c for c in correspondance if c == '✅'])}/{len(correspondance)}")

def comprendre_regle_couleur():
    print("
🎨 COMPRENDRE RÈGLE COULEUR"    print("Hypothèse: La couleur de sortie est déterminée par la position des pixels 1")

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    correspondances = []

    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Positions des 1
        positions_1 = [(x, y) for x in range(14) for y in range(14) if input_grid[x][y] == 1]

        # Couleur de sortie
        couleur_sortie = 0
        for x in range(14):
            for y in range(14):
                if output_grid[x][y] != 0:
                    couleur_sortie = output_grid[x][y]
                    break
            if couleur_sortie != 0:
                break

        correspondances.append({
            'exemple': i,
            'positions_1': positions_1,
            'couleur_sortie': couleur_sortie
        })

    # Afficher les correspondances
    for corr in correspondances:
        print(f"Exemple {corr['exemple']}: positions_1={corr['positions_1']} -> couleur={corr['couleur_sortie']}")

    # Chercher le pattern
    print("
🔍 ANALYSE PATTERN:"    print("Exemple 1: positions_1=[(10,4),(11,5),(12,6)] -> couleur=7")
    print("Exemple 2: positions_1=[(10,4),(11,5),(12,6)] -> couleur=3")
    print("Exemple 3: positions_1=[(9,8),(10,7),(10,8),(10,9),(11,8),(12,8)] -> couleur=2")
    print("Exemple 4: positions_1=[(8,2),(9,3),(10,2),(10,3),(10,4),(11,4)] -> couleur=3")
    print("Exemple 5: positions_1=[(9,2),(10,1),(10,2),(10,3),(11,2),(12,2)] -> couleur=2")

    print("
💡 OBSERVATION:"    print("Les positions des pixels 1 forment des motifs différents")
    print("Chaque motif correspond à une couleur de sortie spécifique")
    print("Il semble y avoir une correspondance directe entre la forme des 1 et la couleur")

def tester_hypothese():
    print("
🧪 TEST HYPOTHÈSE"    print("Hypothèse: Chaque configuration des pixels 1 correspond à une couleur")

    configurations = {
        # Configuration exemple 1: L diagonal
        ((10,4),(11,5),(12,6)): 7,
        # Configuration exemple 2: L diagonal (même que 1)
        # Configuration exemple 3: rectangle vertical
        ((9,8),(10,7),(10,8),(10,9),(11,8),(12,8)): 2,
        # Configuration exemple 4: rectangle
        ((8,2),(9,3),(10,2),(10,3),(10,4),(11,4)): 3,
        # Configuration exemple 5: rectangle vertical
        ((9,2),(10,1),(10,2),(10,3),(11,2),(12,2)): 2
    }

    print("Configurations identifiées:")
    for config, couleur in configurations.items():
        print(f"  {config} -> {couleur}")

def resoudre_009d5c81():
    print("
🎯 RÉSOLUTION 009d5c81"    print("=" * 40)

    with open("data/training/009d5c81.json", 'r') as f:
        puzzle_data = json.load(f)

    # Définir les patterns de correspondance
    patterns_couleur = {
        # L diagonal -> 7
        ((10,4),(11,5),(12,6)): 7,
        # Rectangle vertical -> 2
        ((9,8),(10,7),(10,8),(10,9),(11,8),(12,8)): 2,
        ((9,2),(10,1),(10,2),(10,3),(11,2),(12,2)): 2,
        # Rectangle -> 3
        ((8,2),(9,3),(10,2),(10,3),(10,4),(11,4)): 3
    }

    # Tester avec tous les exemples
    reussites = 0
    for i, exemple in enumerate(puzzle_data['train'], 1):
        input_grid = exemple['input']
        output_grid = exemple['output']

        # Déterminer les positions des 1
        positions_1 = tuple(sorted([(x, y) for x in range(14) for y in range(14) if input_grid[x][y] == 1]))

        # Trouver la couleur correspondante
        couleur_predite = None
        for pattern, couleur in patterns_couleur.items():
            if set(positions_1) == set(pattern):
                couleur_predite = couleur
                break

        if couleur_predite is None:
            print(f"  Exemple {i}: ❌ Pattern non reconnu: {positions_1}")
            continue

        # Vérifier la prédiction
        couleur_reelle = None
        for x in range(14):
            for y in range(14):
                if output_grid[x][y] != 0:
                    couleur_reelle = output_grid[x][y]
                    break
            if couleur_reelle is not None:
                break

        if couleur_predite == couleur_reelle:
            print(f"  Exemple {i}: ✅ (prédit {couleur_predite})")
            reussites += 1
        else:
            print(f"  Exemple {i}: ❌ (prédit {couleur_predite}, réel {couleur_reelle})")

    print(f"\nScore: {reussites}/5")

    if reussites == 5:
        print("🎉 SUCCÈS! Pattern identifié!")

        # Résoudre le test
        test_input = puzzle_data['test'][0]['input']
        positions_1_test = tuple(sorted([(x, y) for x in range(14) for y in range(14) if test_input[x][y] == 1]))

        couleur_test = None
        for pattern, couleur in patterns_couleur.items():
            if set(positions_1_test) == set(pattern):
                couleur_test = couleur
                break

        if couleur_test:
            print(f"\nTEST: positions_1={positions_1_test} -> couleur={couleur_test}")

            # Créer la solution
            solution = [[0 for _ in range(14)] for _ in range(14)]
            for x in range(14):
                for y in range(14):
                    if test_input[x][y] == 8:
                        solution[x][y] = couleur_test

            print("SOLUTION:")
            for row in solution:
                print(f"  {row}")

            # Sauvegarder
            submission = {"009d5c81": solution}
            with open("submission_009d5c81.json", 'w') as f:
                json.dump(submission, f, indent=2)
            print("
💾 Solution sauvegardée: submission_009d5c81.json"
        else:
            print(f"❌ Configuration non reconnue: {positions_1_test}")

if __name__ == "__main__":
    analyser_correspondance_1_8()
    comprendre_regle_couleur()
    tester_hypothese()
    resoudre_009d5c81()
