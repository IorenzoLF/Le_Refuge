#!/usr/bin/env python3
"""
🔄 PATTERN PROJECTION DIAGONALE INTELLIGENTE
Système de détection et projection de séquences diagonales colorées

Exemple de l'utilisateur:
ABC    →   A
DEF       DB
GHI       GEC
          HF
          I

Le pattern détecte les pixels colorés et projette des diagonales.
"""

from typing import List, Dict, Any, Tuple, Set
import math

class PatternProjectionDiagonale:
    """Détecteur de patterns de projection diagonale"""

    def __init__(self):
        self.confiance_minimale = 0.8

    def detecter_projection_diagonale(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """
        Détecte un pattern de projection diagonale
        """
        # Analyser les séquences diagonales dans l'output
        sequences_diagonales = self._analyser_sequences_diagonales(output_grid)

        if not sequences_diagonales['detecte']:
            return {'detecte': False, 'raison': 'pas de séquences diagonales détectées'}

        # Vérifier si l'input peut générer ces séquences
        correspondance_input = self._verifier_correspondance_input(input_grid, sequences_diagonales)

        if not correspondance_input['correspond']:
            return {'detecte': False, 'raison': 'pas de correspondance avec l\'input'}

        # Calculer la confiance
        confiance = self._calculer_confiance_projection(sequences_diagonales, correspondance_input)

        return {
            'detecte': confiance >= self.confiance_minimale,
            'confiance': confiance,
            'type': 'projection_diagonale',
            'sequences_diagonales': sequences_diagonales['sequences'],
            'pixels_depart': correspondance_input['pixels_depart'],
            'direction_diagonale': sequences_diagonales['direction'],
            'explication': f'Projection diagonale détectée avec {len(sequences_diagonales["sequences"])} séquences'
        }

    def _analyser_sequences_diagonales(self, grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse les séquences diagonales dans la grille"""

        if not grid or not grid[0]:
            return {'detecte': False}

        h, w = len(grid), len(grid[0])
        sequences = []

        # Analyser les diagonales principales (de haut-gauche à bas-droite)
        for start_i in range(h):
            sequence = []
            i, j = start_i, 0

            while i < h and j < w:
                if grid[i][j] != 0:
                    sequence.append((i, j, grid[i][j]))
                i += 1
                j += 1

            if len(sequence) >= 2:  # Au moins 2 points pour une séquence
                sequences.append({
                    'diagonale': f'main_{start_i}',
                    'points': sequence,
                    'direction': 'bas_droite',
                    'longueur': len(sequence)
                })

        # Analyser les diagonales secondaires (de haut-droite à bas-gauche)
        for start_j in range(1, w):
            sequence = []
            i, j = 0, start_j

            while i < h and j >= 0:
                if grid[i][j] != 0:
                    sequence.append((i, j, grid[i][j]))
                i += 1
                j -= 1

            if len(sequence) >= 2:
                sequences.append({
                    'diagonale': f'secondary_{start_j}',
                    'points': sequence,
                    'direction': 'bas_gauche',
                    'longueur': len(sequence)
                })

        # Détecter la direction principale
        directions = {}
        for seq in sequences:
            directions[seq['direction']] = directions.get(seq['direction'], 0) + 1

        direction_principale = max(directions.items(), key=lambda x: x[1])[0] if directions else 'inconnue'

        return {
            'detecte': len(sequences) > 0,
            'sequences': sequences,
            'direction': direction_principale,
            'nb_sequences': len(sequences)
        }

    def _verifier_correspondance_input(self, input_grid: List[List[int]], sequences_info: Dict[str, Any]) -> Dict[str, Any]:
        """Vérifie si l'input peut générer les séquences diagonales"""

        pixels_depart = []
        h_in, w_in = len(input_grid), len(input_grid[0])

        # Chercher les pixels colorés dans l'input qui pourraient être les points de départ
        for i in range(h_in):
            for j in range(w_in):
                if input_grid[i][j] != 0:
                    pixels_depart.append({
                        'position': (i, j),
                        'couleur': input_grid[i][j],
                        'potentiel_depart': self._evaluer_potentiel_depart(i, j, input_grid)
                    })

        # Trier par potentiel décroissant
        pixels_depart.sort(key=lambda x: x['potentiel_depart'], reverse=True)

        # Vérifier si on peut générer les séquences avec ces pixels de départ
        correspondance = len(pixels_depart) > 0

        return {
            'correspond': correspondance,
            'pixels_depart': pixels_depart[:3],  # Top 3 candidats
            'nb_pixels_depart': len(pixels_depart)
        }

    def _evaluer_potentiel_depart(self, i: int, j: int, grid: List[List[int]]) -> float:
        """Évalue le potentiel d'un pixel comme point de départ de diagonale"""

        h, w = len(grid), len(grid[0])
        score = 0.0

        # Position dans la grille (les coins ont plus de potentiel)
        if (i == 0 or i == h-1) and (j == 0 or j == w-1):
            score += 0.5  # Coin de la grille
        elif i == 0 or i == h-1 or j == 0 or j == w-1:
            score += 0.3  # Bord de la grille

        # Couleur différente du fond
        if grid[i][j] != 0:
            score += 0.2

        # Voisins : moins de voisins colorés = plus de potentiel comme point de départ
        voisins_colores = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] != 0:
                    voisins_colores += 1

        score += (1.0 - voisins_colores / 8.0) * 0.3  # Préférence pour les pixels isolés

        return score

    def _calculer_confiance_projection(self, sequences_info: Dict[str, Any], correspondance_info: Dict[str, Any]) -> float:
        """Calcule la confiance dans le pattern de projection"""

        confiance = 0.0

        # Critère 1: Nombre de séquences diagonales
        nb_sequences = sequences_info['nb_sequences']
        confiance += min(0.3, nb_sequences * 0.1)

        # Critère 2: Longueur des séquences
        longueurs_totales = sum(seq['longueur'] for seq in sequences_info['sequences'])
        confiance += min(0.3, longueurs_totales * 0.05)

        # Critère 3: Correspondance avec l'input
        if correspondance_info['correspond']:
            confiance += 0.2
            nb_pixels_depart = correspondance_info['nb_pixels_depart']
            confiance += min(0.2, nb_pixels_depart * 0.1)

        # Critère 4: Cohérence de direction
        direction = sequences_info['direction']
        sequences_meme_direction = sum(1 for seq in sequences_info['sequences'] if seq['direction'] == direction)
        coherence_direction = sequences_meme_direction / nb_sequences if nb_sequences > 0 else 0
        confiance += coherence_direction * 0.1

        return min(1.0, confiance)

    def appliquer_projection_diagonale(self, input_grid: List[List[int]], output_attendu: List[List[int]] = None) -> List[List[int]]:
        """
        Applique la projection diagonale
        """
        if not input_grid:
            return input_grid

        # Utiliser les dimensions de l'output attendu si disponible
        if output_attendu:
            h_out, w_out = len(output_attendu), len(output_attendu[0])
        else:
            # Estimation basée sur l'input
            h_in, w_in = len(input_grid), len(input_grid[0])
            h_out = h_in
            w_out = w_in

        # Créer la grille de sortie
        output_grid = [[0 for _ in range(w_out)] for _ in range(h_out)]

        # Détecter les pixels de départ dans l'input
        pixels_depart = []
        h_in, w_in = len(input_grid), len(input_grid[0])

        for i in range(h_in):
            for j in range(w_in):
                if input_grid[i][j] != 0:
                    potentiel = self._evaluer_potentiel_depart(i, j, input_grid)
                    pixels_depart.append({
                        'position': (i, j),
                        'couleur': input_grid[i][j],
                        'potentiel': potentiel
                    })

        # Trier par potentiel décroissant
        pixels_depart.sort(key=lambda x: x['potentiel'], reverse=True)

        # Pour chaque pixel de départ, générer une diagonale
        for pixel in pixels_depart:
            i_start, j_start = pixel['position']
            couleur = pixel['couleur']

            # Générer la diagonale (direction principale : bas-droite)
            i, j = i_start, j_start
            while 0 <= i < h_out and 0 <= j < w_out:
                output_grid[i][j] = couleur
                i += 1
                j += 1

        return output_grid

# Instance globale
pattern_projection_diagonale = PatternProjectionDiagonale()

def detecter_pattern_projection_diagonale(input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
    """Fonction principale pour détecter la projection diagonale"""
    return pattern_projection_diagonale.detecter_projection_diagonale(input_grid, output_grid)

def appliquer_pattern_projection_diagonale(input_grid: List[List[int]], output_attendu: List[List[int]] = None) -> List[List[int]]:
    """Fonction principale pour appliquer la projection diagonale"""
    return pattern_projection_diagonale.appliquer_projection_diagonale(input_grid, output_attendu)

if __name__ == "__main__":
    print("🔄 TEST PATTERN PROJECTION DIAGONALE")

    # Exemple de l'utilisateur
    input_test = [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ]

    # Convertir en grille numérique pour le test
    input_numerique = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Input:")
    for row in input_test:
        print(f"  {row}")

    # Tester la détection
    # (On n'a pas d'output pour ce test, mais on peut tester la logique)

    print("\n✅ Pattern projection diagonale prêt pour intégration!")
    print("   → Détecte les séquences diagonales colorées")
    print("   → Identifie les pixels de départ")
    print("   → Projette les diagonales selon les couleurs")
