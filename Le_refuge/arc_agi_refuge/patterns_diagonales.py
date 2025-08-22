#!/usr/bin/env python3
"""
🔄 Patterns de Propagation Diagonale
Module pour gérer les patterns diagonaux complexes identifiés dans l'audit
"""

from typing import List, Dict, Any, Tuple, Set
from collections import defaultdict

class GestionnairePatternsDiagonales:
    def __init__(self):
        self.confiance_minimale = 0.8

    def detecter_pattern_diagonal(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """
        Détecte les patterns diagonaux complexes (feca6190, 7fe24cdd, etc.)
        """
        if not self._est_candidat_diagonal(input_grid, output_grid):
            return {'detecte': False}

        # Analyser le type de pattern diagonal
        type_pattern = self._classifier_type_diagonal(input_grid, output_grid)

        if type_pattern == 'diagonal_simple':
            return self._analyser_diagonal_simple(input_grid, output_grid)
        elif type_pattern == 'propagation_cascade':
            return self._analyser_propagation_cascade(input_grid, output_grid)
        elif type_pattern == 'diagonal_avec_rythme':
            return self._analyser_diagonal_rythme(input_grid, output_grid)

        return {'detecte': False}

    def _est_candidat_diagonal(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Vérifie si le puzzle est un candidat pour un pattern diagonal"""
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        # Critères de base pour un pattern diagonal
        return (
            h_in == 1 and  # Input est une ligne horizontale
            h_out == w_out and  # Output est une matrice carrée
            h_out > w_in and  # Output plus grand que input
            h_out >= 5  # Taille minimale pour un pattern diagonal
        )

    def _classifier_type_diagonal(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> str:
        """Classifie le type de pattern diagonal"""
        h_out, w_out = len(output_grid), len(output_grid[0])
        elements_input = [x for x in input_grid[0] if x != 0]

        # Compter les occurrences de chaque élément dans l'output
        element_counts = defaultdict(int)
        for i in range(h_out):
            for j in range(w_out):
                if output_grid[i][j] != 0:
                    element_counts[output_grid[i][j]] += 1

        # Si chaque élément de l'input apparaît plusieurs fois = propagation
        max_occurrences = max(element_counts.values()) if element_counts else 0
        if max_occurrences >= len(elements_input):
            return 'propagation_cascade'

        # Si éléments principalement sur la diagonale = diagonal simple
        elements_sur_diagonale = 0
        for i in range(h_out):
            for j in range(w_out):
                if i + j == h_out - 1 and output_grid[i][j] in elements_input:
                    elements_sur_diagonale += 1

        if elements_sur_diagonale >= len(elements_input) * 0.7:
            return 'diagonal_simple'

        # Sinon, pattern avec rythme
        return 'diagonal_avec_rythme'

    def _analyser_diagonal_simple(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse un pattern diagonal simple (comme feca6190)"""
        h_out, w_out = len(output_grid), len(output_grid[0])
        elements_input = [x for x in input_grid[0] if x != 0]

        # Vérifier que tous les éléments de l'input sont sur la diagonale
        elements_trouves = set()
        positions_diagonales = []

        for i in range(h_out):
            j = h_out - 1 - i  # Position sur la diagonale principale
            if j < w_out and output_grid[i][j] in elements_input:
                elements_trouves.add(output_grid[i][j])
                positions_diagonales.append((i, j))

        # Calculer la confiance
        couverture = len(elements_trouves) / len(elements_input)
        confiance = min(1.0, couverture * 0.9 + 0.1)

        return {
            'detecte': True,
            'type': 'diagonal_simple',
            'confiance': confiance,
            'elements_input': elements_input,
            'elements_trouves': list(elements_trouves),
            'positions_diagonales': positions_diagonales,
            'couverture': couverture,
            'explication': f"Pattern diagonal simple - {len(elements_trouves)}/{len(elements_input)} éléments placés sur la diagonale"
        }

    def _analyser_propagation_cascade(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse un pattern de propagation en cascade (comme 7fe24cdd)"""
        h_out, w_out = len(output_grid), len(output_grid[0])
        elements_input = [x for x in input_grid[0] if x != 0]

        # Analyser les séquences de propagation pour chaque élément
        sequences_propagation = {}
        confiance_totale = 0

        for element in elements_input:
            positions = []
            for i in range(h_out):
                for j in range(w_out):
                    if output_grid[i][j] == element:
                        positions.append((i, j))

            if len(positions) > 1:
                # Analyser la régularité de la séquence
                regularite = self._analyser_regularite_sequence(positions)
                sequences_propagation[element] = {
                    'positions': positions,
                    'regularite': regularite,
                    'nb_occurrences': len(positions)
                }
                confiance_totale += regularite

        # Calculer la confiance globale
        nb_sequences = len(sequences_propagation)
        confiance_moyenne = confiance_totale / nb_sequences if nb_sequences > 0 else 0

        return {
            'detecte': True,
            'type': 'propagation_cascade',
            'confiance': confiance_moyenne,
            'sequences_propagation': sequences_propagation,
            'nb_sequences': nb_sequences,
            'explication': f"Pattern de propagation en cascade - {nb_sequences} séquences détectées avec {confiance_moyenne:.1%} de régularité"
        }

    def _analyser_diagonal_rythme(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse un pattern diagonal avec rythme spécifique"""
        # Version simplifiée pour l'instant
        return {
            'detecte': True,
            'type': 'diagonal_avec_rythme',
            'confiance': 0.7,
            'explication': "Pattern diagonal avec rythme spécifique détecté"
        }

    def _analyser_regularite_sequence(self, positions: List[Tuple[int, int]]) -> float:
        """Analyse la régularité d'une séquence de positions"""
        if len(positions) < 3:
            return 0.5  # Pas assez de points pour analyser

        # Trier par ligne
        positions.sort(key=lambda x: x[0])

        # Calculer les différences
        diff_i = [positions[i+1][0] - positions[i][0] for i in range(len(positions)-1)]
        diff_j = [positions[i+1][1] - positions[i][1] for i in range(len(positions)-1)]

        # La régularité est basée sur la constance des différences
        regularite_i = 1.0 - (len(set(diff_i)) - 1) / len(diff_i) if diff_i else 0
        regularite_j = 1.0 - (len(set(diff_j)) - 1) / len(diff_j) if diff_j else 0

        return (regularite_i + regularite_j) / 2

    def appliquer_pattern_diagonal(self, input_grid: List[List[int]], dimensions_cible: Tuple[int, int], type_pattern: str) -> List[List[int]]:
        """Applique un pattern diagonal à une nouvelle grille"""
        h_cible, w_cible = dimensions_cible

        if type_pattern == 'diagonal_simple':
            return self._appliquer_diagonal_simple(input_grid, h_cible, w_cible)
        elif type_pattern == 'propagation_cascade':
            return self._appliquer_propagation_cascade(input_grid, h_cible, w_cible)

        # Fallback
        return [[0 for _ in range(w_cible)] for _ in range(h_cible)]

    def _appliquer_diagonal_simple(self, input_grid: List[List[int]], h_cible: int, w_cible: int) -> List[List[int]]:
        """Applique un pattern diagonal simple"""
        grille_resultat = [[0 for _ in range(w_cible)] for _ in range(h_cible)]
        elements_input = [x for x in input_grid[0] if x != 0]

        # Placer les éléments sur la diagonale
        for idx, element in enumerate(elements_input):
            if idx < h_cible:
                i, j = idx, h_cible - 1 - idx
                if j < w_cible:
                    grille_resultat[i][j] = element

        return grille_resultat

    def _appliquer_propagation_cascade(self, input_grid: List[List[int]], h_cible: int, w_cible: int) -> List[List[int]]:
        """Applique un pattern de propagation en cascade"""
        grille_resultat = [[0 for _ in range(w_cible)] for _ in range(h_cible)]
        elements_input = [x for x in input_grid[0] if x != 0]

        # Pour chaque élément, créer une séquence diagonale
        for idx, element in enumerate(elements_input):
            # Position de départ: décalée pour chaque élément
            start_i = idx
            start_j = w_cible - 1 - idx

            # Générer la séquence diagonale
            i, j = start_i, start_j
            while i < h_cible and j >= 0:
                if i < h_cible and j < w_cible and i >= 0 and j >= 0:
                    grille_resultat[i][j] = element
                i += 1
                j -= 1

        return grille_resultat

# Instance globale
gestionnaire_diagonales = GestionnairePatternsDiagonales()

def detecter_pattern_diagonal(input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
    """Fonction principale pour détecter les patterns diagonaux"""
    return gestionnaire_diagonales.detecter_pattern_diagonal(input_grid, output_grid)

def appliquer_pattern_diagonal(input_grid: List[List[int]], dimensions_cible: Tuple[int, int], type_pattern: str) -> List[List[int]]:
    """Fonction principale pour appliquer les patterns diagonaux"""
    return gestionnaire_diagonales.appliquer_pattern_diagonal(input_grid, dimensions_cible, type_pattern)

if __name__ == "__main__":
    # Test du module
    print("=== TEST PATTERNS DIAGONAUX ===")

    # Test diagonal simple (feca6190 style)
    input_simple = [[0, 9, 0, 8, 4]]
    output_simple = [[0] * 15 for _ in range(15)]  # 15x15 vide
    # Remplir la diagonale
    for i in range(15):
        output_simple[i][14-i] = [0, 9, 0, 8, 4][i % 5] if i < 15 else 0

    detection = detecter_pattern_diagonal(input_simple, output_simple)
    print(f"Diagonal simple détecté: {detection['detecte']}")
    if detection['detecte']:
        print(f"Type: {detection['type']}")
        print(".1%")
        print(f"Explication: {detection['explication']}")

    # Test propagation cascade (7fe24cdd style)
    input_cascade = [[3, 0, 0]]
    output_cascade = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 3, 0],
        [0, 0, 0, 3, 0, 0],
        [0, 0, 3, 0, 0, 0],
        [0, 3, 0, 0, 0, 0]
    ]

    detection_cascade = detecter_pattern_diagonal(input_cascade, output_cascade)
    print(f"\nPropagation cascade détectée: {detection_cascade['detecte']}")
    if detection_cascade['detecte']:
        print(f"Type: {detection_cascade['type']}")
        print(".1%")
        print(f"Explication: {detection_cascade['explication']}")
