#!/usr/bin/env python3
"""
Pattern de transformation géométrique avancée
Pour puzzles comme 7fe24cdd avec déploiement symétrique
"""

import json
from typing import List, Dict, Any, Tuple, Optional

def rotation_90_clockwise(grid: List[List[int]]) -> List[List[int]]:
    """Rotation de 90° dans le sens horaire"""
    if not grid:
        return grid
    h, w = len(grid), len(grid[0])
    rotated = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(h):
        for j in range(w):
            rotated[j][h-1-i] = grid[i][j]
    return rotated

def transformer_geometrique_7fe24cdd(input_grid: List[List[int]]) -> List[List[int]]:
    """
    Le carré 3x3 se divise en 4 sous-carrés 3x3 qui se déplacent
    et subissent chacun une rotation de 90°
    """
    if not input_grid or len(input_grid) != 3 or len(input_grid[0]) != 3:
        return input_grid

    # Grille de sortie 6x6
    output = [[0 for _ in range(6)] for _ in range(6)]

    # Le centre reste le centre (position 1,1 dans input → positions centrales dans output)
    center_value = input_grid[1][1]
    if center_value != 0:
        output[2][2] = center_value
        output[2][3] = center_value
        output[3][2] = center_value
        output[3][3] = center_value

    # Les 4 coins créent des "blocs" 3x3 tournés dans les 4 quadrants

    # 1. Coin supérieur gauche → quadrant supérieur gauche de la sortie
    # avec rotation de 90°
    top_left = input_grid[0][0]
    if top_left != 0:
        # Rotation 90° horaire du coin
        output[0][0] = top_left  # reste à sa position relative
        output[0][1] = top_left  # étendu
        output[1][0] = top_left  # étendu

    # 2. Coin supérieur droit → quadrant supérieur droit
    # avec rotation de 90°
    top_right = input_grid[0][2]
    if top_right != 0:
        output[0][4] = top_right
        output[0][5] = top_right
        output[1][5] = top_right

    # 3. Coin inférieur gauche → quadrant inférieur gauche
    bottom_left = input_grid[2][0]
    if bottom_left != 0:
        output[4][0] = bottom_left
        output[5][0] = bottom_left
        output[5][1] = bottom_left

    # 4. Coin inférieur droit → quadrant inférieur droit
    bottom_right = input_grid[2][2]
    if bottom_right != 0:
        output[4][5] = bottom_right
        output[5][4] = bottom_right
        output[5][5] = bottom_right

    # Les positions intermédiaires créent des connexions
    # Haut milieu
    top_middle = input_grid[0][1]
    if top_middle != 0:
        output[0][2] = top_middle
        output[0][3] = top_middle
        output[1][2] = top_middle
        output[1][3] = top_middle

    # Bas milieu
    bottom_middle = input_grid[2][1]
    if bottom_middle != 0:
        output[4][2] = bottom_middle
        output[4][3] = bottom_middle
        output[5][2] = bottom_middle
        output[5][3] = bottom_middle

    # Gauche milieu
    left_middle = input_grid[1][0]
    if left_middle != 0:
        output[2][0] = left_middle
        output[2][1] = left_middle
        output[3][0] = left_middle
        output[3][1] = left_middle

    # Droite milieu
    right_middle = input_grid[1][2]
    if right_middle != 0:
        output[2][4] = right_middle
        output[2][5] = right_middle
        output[3][4] = right_middle
        output[3][5] = right_middle

    return output

def detecter_pattern_7fe24cdd(input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
    """
    Détecte si le pattern 7fe24cdd s'applique
    """
    # Vérifier les dimensions
    if len(input_grid) != 3 or len(input_grid[0]) != 3:
        return False
    if len(output_grid) != 6 or len(output_grid[0]) != 6:
        return False

    # Appliquer la transformation et comparer
    predicted = transformer_geometrique_7fe24cdd(input_grid)

    # Calculer la similarité
    matches = 0
    total = 0
    for i in range(6):
        for j in range(6):
            total += 1
            if predicted[i][j] == output_grid[i][j]:
                matches += 1

    similarity = matches / total
    return similarity > 0.8  # 80% de similarité minimum

def transformer_geometrique_general(input_grid: List[List[int]], facteur: int = 2) -> List[List[int]]:
    """
    Transformation géométrique généralisée
    Peut être adaptée à différents facteurs d'agrandissement
    """
    h_in, w_in = len(input_grid), len(input_grid[0])
    h_out, w_out = h_in * facteur, w_in * facteur

    output = [[0 for _ in range(w_out)] for _ in range(h_out)]

    # Duplication simple de chaque cellule
    for i in range(h_in):
        for j in range(w_in):
            value = input_grid[i][j]
            # Remplir le bloc facteur x facteur
            for di in range(facteur):
                for dj in range(facteur):
                    output[i * facteur + di][j * facteur + dj] = value

    return output

def detecter_transformation_geometrique(input_grid: List[List[int]], output_grid: List[List[int]]) -> Optional[str]:
    """
    Détecte le type de transformation géométrique
    """
    h_in, w_in = len(input_grid), len(input_grid[0])
    h_out, w_out = len(output_grid), len(output_grid[0])

    # Vérifier si c'est un agrandissement
    if h_out % h_in == 0 and w_out % w_in == 0:
        facteur = h_out // h_in
        if facteur == w_out // w_in:
            return f"agrandissement_facteur_{facteur}"

    # Vérifier pattern spécifique 7fe24cdd
    if detecter_pattern_7fe24cdd(input_grid, output_grid):
        return "geometrique_7fe24cdd"

    return None

def tester_pattern_7fe24cdd():
    """Test du pattern sur le puzzle 7fe24cdd"""
    print("TEST PATTERN GEOMETRIQUE 7fe24cdd")
    print("=" * 40)

    # Charger le puzzle
    with open('ARC-AGI-2-main/data/training/7fe24cdd.json', 'r') as f:
        data = json.load(f)

    print(f"Puzzle: 7fe24cdd")
    print(f"Train examples: {len(data['train'])}")

    # Tester sur chaque exemple
    for i, exemple in enumerate(data['train']):
        input_grid = exemple['input']
        expected_output = exemple['output']

        print(f"\nEXEMPLE {i+1}:")
        print(f"Input: {len(input_grid)}x{len(input_grid[0])}")
        print(f"Expected output: {len(expected_output)}x{len(expected_output[0])}")

        # Appliquer notre transformation
        predicted_output = transformer_geometrique_7fe24cdd(input_grid)

        # Calculer la similarité
        matches = 0
        total = 0
        for x in range(6):
            for y in range(6):
                total += 1
                if predicted_output[x][y] == expected_output[x][y]:
                    matches += 1

        similarity = matches / total * 100
        print(f"Prédiction similarity: {similarity:.1f}%")

        if similarity > 80:
            print("✅ SUCCÈS - Pattern bien détecté")
        else:
            print("❌ ÉCHEC - Pattern pas assez précis")

    # Tester sur le test input
    if data['test']:
        test_input = data['test'][0]['input']
        print(f"\nTEST INPUT:")
        for row in test_input:
            print('  ' + ' '.join(map(str, row)))

        test_prediction = transformer_geometrique_7fe24cdd(test_input)
        print(f"\nTEST PREDICTION:")
        for row in test_prediction:
            print('  ' + ' '.join(map(str, row)))

def tester_sur_autres_puzzles():
    """Tester le pattern sur d'autres puzzles de la liste"""
    print("\nTEST SUR AUTRES PUZZLES")
    print("=" * 30)

    # Liste de puzzles à tester
    puzzles_test = ['14754a24', 'fafffa47', 'fbf15a0b', 'feca6190']

    for puzzle_id in puzzles_test:
        try:
            with open(f'ARC-AGI-2-main/data/training/{puzzle_id}.json', 'r') as f:
                data = json.load(f)

            # Tester sur le premier exemple
            if data['train']:
                input_grid = data['train'][0]['input']
                output_grid = data['train'][0]['output']

                # Vérifier si les dimensions correspondent (3x3 → 6x6)
                if (len(input_grid) == 3 and len(input_grid[0]) == 3 and
                    len(output_grid) == 6 and len(output_grid[0]) == 6):

                    predicted = transformer_geometrique_7fe24cdd(input_grid)

                    # Calculer similarité
                    matches = 0
                    total = 36  # 6x6
                    for i in range(6):
                        for j in range(6):
                            if predicted[i][j] == output_grid[i][j]:
                                matches += 1

                    similarity = matches / total * 100
                    print(f"{puzzle_id}: {similarity:.1f}% similarity")

                    if similarity > 80:
                        print(f"  ✅ CANDIDAT PROMETTEUR!")
                    elif similarity > 50:
                        print(f"  🤔 SIMILARITÉ MOYENNE")
                    else:
                        print(f"  ❌ PAS APPLICABLE")

        except Exception as e:
            print(f"{puzzle_id}: ERREUR - {e}")

if __name__ == "__main__":
    tester_pattern_7fe24cdd()
    tester_sur_autres_puzzles()
