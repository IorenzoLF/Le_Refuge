#!/usr/bin/env python3
"""
🌟 PATTERN PROJECTION LIMITÉE DOUBLE FORME
Implémentation pour 0962bcdd - Découverte de la "croix en deux parties"
"""

from typing import List, Dict, Any
import numpy as np

class PatternProjectionLimiteeDoubleForme:
    """
    Pattern de projection limitée par deux formes géométriques
    Découvert dans 0962bcdd: deux régions définissent les limites de projection
    """

    def __init__(self):
        self.nom = "projection_limitee_double_forme"
        self.description = "Projection limitée par deux formes géométriques séparées"
        self.priorite = 90  # Haute priorité pour ce pattern sophistiqué

    def detecter(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """
        Détecte le pattern de projection limitée par deux formes
        """
        if not input_grid or not output_grid:
            return {'detecte': False, 'confiance': 0.0}

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        # Vérifications de base
        if h_out != w_out or h_in != h_out or w_in != w_out:
            return {'detecte': False, 'confiance': 0.0}

        # Extraire les couleurs de l'input
        couleurs_sequence = []
        for i in range(h_in):
            for j in range(w_in):
                if input_grid[i][j] != 0 and input_grid[i][j] not in couleurs_sequence:
                    couleurs_sequence.append(input_grid[i][j])

        if len(couleurs_sequence) != 2:  # Doit avoir exactement 2 couleurs
            return {'detecte': False, 'confiance': 0.0}

        # Détecter les deux formes dans l'input
        formes = self._detecter_deux_formes(input_grid, couleurs_sequence)

        if not formes or len(formes) < 2:
            return {'detecte': False, 'confiance': 0.0}

        # Calculer les rectangles englobants
        rectangles = self._calculer_rectangles_englobants(formes)

        # Vérifier le pattern de projection limitée
        confiance_projection = self._verifier_projection_limitee(output_grid, couleurs_sequence, rectangles)

        # Vérifier la cohérence globale
        confiance = confiance_projection

        # Seuil de détection adapté pour ce pattern complexe
        detecte = confiance > 0.8

        return {
            'detecte': detecte,
            'confiance': confiance,
            'pattern': self.nom,
            'couleurs_sequence': couleurs_sequence,
            'formes_detectees': formes,
            'rectangles_englobants': rectangles,
            'projection_confiance': confiance_projection,
            'description': f"Projection limitée par {len(formes)} formes géométriques"
        }

    def _detecter_deux_formes(self, input_grid: List[List[int]], couleurs_sequence: List[int]) -> List[Dict]:
        """
        Détecte les deux formes principales dans la grille
        """
        h, w = len(input_grid), len(input_grid[0])

        # Collecter les positions pour chaque couleur
        positions_par_couleur = {}
        for couleur in couleurs_sequence:
            positions = []
            for i in range(h):
                for j in range(w):
                    if input_grid[i][j] == couleur:
                        positions.append((i, j))
            positions_par_couleur[couleur] = positions

        # Pour chaque couleur, diviser en deux groupes (haut-gauche vs bas-droite)
        formes = []
        for couleur, positions in positions_par_couleur.items():
            if len(positions) >= 5:  # Suffisant pour former deux formes
                # Diviser en deux groupes
                forme1 = [(i, j) for i, j in positions if i <= h//2 and j <= w//2]  # Haut-gauche
                forme2 = [(i, j) for i, j in positions if i >= h//2 and j >= w//2]  # Bas-droite

                if len(forme1) >= 2 and len(forme2) >= 2:
                    formes.append({
                        'couleur': couleur,
                        'forme1': forme1,
                        'forme2': forme2
                    })

        return formes

    def _calculer_rectangles_englobants(self, formes: List[Dict]) -> List[Dict]:
        """
        Calcule les rectangles englobants pour chaque forme
        """
        rectangles = []

        for forme in formes:
            # Calculer rectangle pour forme1
            if forme['forme1']:
                min_x1 = min(i for i, j in forme['forme1'])
                max_x1 = max(i for i, j in forme['forme1'])
                min_y1 = min(j for i, j in forme['forme1'])
                max_y1 = max(j for i, j in forme['forme1'])

                rectangles.append({
                    'couleur': forme['couleur'],
                    'forme_id': 1,
                    'rect': (min_x1, min_y1, max_x1, max_y1)
                })

            # Calculer rectangle pour forme2
            if forme['forme2']:
                min_x2 = min(i for i, j in forme['forme2'])
                max_x2 = max(i for i, j in forme['forme2'])
                min_y2 = min(j for i, j in forme['forme2'])
                max_y2 = max(j for i, j in forme['forme2'])

                rectangles.append({
                    'couleur': forme['couleur'],
                    'forme_id': 2,
                    'rect': (min_x2, min_y2, max_x2, max_y2)
                })

        return rectangles

    def _verifier_projection_limitee(self, output_grid: List[List[int]],
                                   couleurs_sequence: List[int],
                                   rectangles: List[Dict]) -> float:
        """
        Vérifie si l'output correspond à une projection limitée par les rectangles
        """
        if not output_grid or not couleurs_sequence or not rectangles:
            return 0.0

        h, w = len(output_grid), len(output_grid[0])
        correspondances = 0
        total_positions = 0

        # Créer un masque des zones autorisées (union des rectangles)
        masque_autorise = [[False for _ in range(w)] for _ in range(h)]

        for rect_info in rectangles:
            min_x, min_y, max_x, max_y = rect_info['rect']
            for i in range(max(0, min_x), min(h, max_x + 1)):
                for j in range(max(0, min_y), min(w, max_y + 1)):
                    masque_autorise[i][j] = True

        # Vérifier chaque position de l'output
        for i in range(h):
            for j in range(w):
                if output_grid[i][j] != 0:
                    total_positions += 1

                    # Position dans séquence diagonale
                    position_diagonale = (i + j) % len(couleurs_sequence)
                    couleur_attendue = couleurs_sequence[position_diagonale]

                    # Vérifier si on est dans une zone autorisée
                    if masque_autorise[i][j]:
                        if output_grid[i][j] == couleur_attendue:
                            correspondances += 1
                    # Si hors zone, devrait être 0
                    else:
                        if output_grid[i][j] == 0:
                            correspondances += 1

        return correspondances / total_positions if total_positions > 0 else 0.0

    def appliquer(self, input_grid: List[List[int]], output_attendu: List[List[int]] = None) -> List[List[int]]:
        """
        Applique le pattern de projection limitée par double forme
        """
        if not input_grid:
            return input_grid

        h, w = len(input_grid), len(input_grid[0])

        # Extraire couleurs
        couleurs_sequence = []
        for i in range(h):
            for j in range(w):
                if input_grid[i][j] != 0 and input_grid[i][j] not in couleurs_sequence:
                    couleurs_sequence.append(input_grid[i][j])

        if len(couleurs_sequence) != 2:
            return input_grid

        # Détecter les formes
        formes = self._detecter_deux_formes(input_grid, couleurs_sequence)

        if not formes:
            return input_grid

        # Calculer rectangles
        rectangles = self._calculer_rectangles_englobants(formes)

        # Créer masque des zones autorisées
        masque_autorise = [[False for _ in range(w)] for _ in range(h)]

        for rect_info in rectangles:
            min_x, min_y, max_x, max_y = rect_info['rect']
            for i in range(max(0, min_x), min(h, max_x + 1)):
                for j in range(max(0, min_y), min(w, max_y + 1)):
                    masque_autorise[i][j] = True

        # Générer output avec projection limitée
        output_grid = [[0 for _ in range(w)] for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if masque_autorise[i][j]:
                    # Appliquer projection diagonale dans la zone autorisée
                    position_diagonale = (i + j) % len(couleurs_sequence)
                    output_grid[i][j] = couleurs_sequence[position_diagonale]

        return output_grid

# Instance globale
pattern_projection_limitee = PatternProjectionLimiteeDoubleForme()

def detecter_pattern_projection_limitee_double_forme(input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
    """Fonction wrapper pour la détection"""
    return pattern_projection_limitee.detecter(input_grid, output_grid)

def appliquer_pattern_projection_limitee_double_forme(input_grid: List[List[int]], output_attendu: List[List[int]] = None) -> List[List[int]]:
    """Fonction wrapper pour l'application"""
    return pattern_projection_limitee.appliquer(input_grid, output_attendu)

# Test rapide
if __name__ == "__main__":
    print("🌟 Pattern Projection Limitée Double Forme - Prêt!")
    print(f"Nom: {pattern_projection_limitee.nom}")
    print(f"Description: {pattern_projection_limitee.description}")
    print(f"Priorité: {pattern_projection_limitee.priorite}")
