#!/usr/bin/env python3
"""
PatternDetector v2 - Détection de patterns fondamentaux anti-surapprentissage
Architecture modulaire pour identifier les patterns réutilisables
"""

import json
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
import numpy as np

class PatternDetector:
    """
    Détecteur de patterns fondamentaux pour ARC-AGI
    Version 2: Architecture modulaire anti-surapprentissage
    """

    def __init__(self):
        self.spatial_patterns = {
            'symmetry': self._detect_symmetry,
            'repetition': self._detect_repetition,
            'scaling': self._detect_scaling,
            'translation': self._detect_translation,
            'filling': self._detect_filling
        }

        self.color_patterns = {
            'mapping': self._detect_color_mapping,
            'inversion': self._detect_color_inversion,
            'gradient': self._detect_gradient
        }

        self.structural_patterns = {
            'completion': self._detect_completion,
            'connection': self._detect_connection,
            'extraction': self._detect_extraction
        }

        self.detected_patterns = []
        self.confidence_threshold = 0.6

    def analyze_puzzle(self, input_grid: List[List[int]],
                      output_grid: List[List[int]]) -> Dict[str, Any]:
        """
        Analyse complète d'un puzzle pour détecter tous les patterns possibles
        """
        analysis = {
            'spatial': {},
            'color': {},
            'structural': {},
            'overall_score': 0,
            'recommended_patterns': []
        }

        # Analyse des patterns spatiaux
        for pattern_name, detector_func in self.spatial_patterns.items():
            try:
                score, details = detector_func(input_grid, output_grid)
                analysis['spatial'][pattern_name] = {
                    'score': score,
                    'details': details,
                    'confidence': self._calculate_confidence(score, 'spatial', pattern_name)
                }
            except Exception as e:
                analysis['spatial'][pattern_name] = {
                    'score': 0,
                    'details': f"Erreur: {str(e)}",
                    'confidence': 0
                }

        # Analyse des patterns de couleur
        for pattern_name, detector_func in self.color_patterns.items():
            try:
                score, details = detector_func(input_grid, output_grid)
                analysis['color'][pattern_name] = {
                    'score': score,
                    'details': details,
                    'confidence': self._calculate_confidence(score, 'color', pattern_name)
                }
            except Exception as e:
                analysis['color'][pattern_name] = {
                    'score': 0,
                    'details': f"Erreur: {str(e)}",
                    'confidence': 0
                }

        # Analyse des patterns structuraux
        for pattern_name, detector_func in self.structural_patterns.items():
            try:
                score, details = detector_func(input_grid, output_grid)
                analysis['structural'][pattern_name] = {
                    'score': score,
                    'details': details,
                    'confidence': self._calculate_confidence(score, 'structural', pattern_name)
                }
            except Exception as e:
                analysis['structural'][pattern_name] = {
                    'score': 0,
                    'details': f"Erreur: {str(e)}",
                    'confidence': 0
                }

        # Calcul du score global et recommandations
        analysis['overall_score'] = self._calculate_overall_score(analysis)
        analysis['recommended_patterns'] = self._get_recommendations(analysis)

        return analysis

    def _detect_symmetry(self, input_grid: List[List[int]],
                        output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de symétrie (horizontale, verticale, diagonale)
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        score = 0.0
        symmetries = {'horizontal': 0, 'vertical': 0, 'diagonal': 0}

        # Test de symétrie horizontale
        if self._is_horizontally_symmetric(output_grid):
            symmetries['horizontal'] = 1
            score += 0.4

        # Test de symétrie verticale
        if self._is_vertically_symmetric(output_grid):
            symmetries['vertical'] = 1
            score += 0.4

        # Test de symétrie diagonale
        if self._is_diagonally_symmetric(output_grid):
            symmetries['diagonal'] = 1
            score += 0.2

        details = {
            'symmetries_found': symmetries,
            'symmetry_count': sum(symmetries.values()),
            'grid_dimensions': f"{len(output_grid)}x{len(output_grid[0])}"
        }

        return min(score, 1.0), details

    def _detect_repetition(self, input_grid: List[List[int]],
                          output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de répétition horizontale et verticale
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        score = 0.0
        repetitions = {'horizontal': 0, 'vertical': 0, 'block': 0}

        # Test de répétition horizontale (même ligne répétée)
        for row in output_grid:
            if self._is_repeated_row(row):
                repetitions['horizontal'] += 1

        # Test de répétition verticale (même colonne répétée)
        if len(output_grid) > 0 and len(output_grid[0]) > 0:
            for col in range(len(output_grid[0])):
                column = [row[col] for row in output_grid]
                if self._is_repeated_column(column):
                    repetitions['vertical'] += 1

        # Test de répétition en bloc
        block_repetition = self._detect_block_repetition(output_grid)
        if block_repetition:
            repetitions['block'] = 1
            score += 0.5

        # Calcul du score basé sur les répétitions trouvées
        total_possible = len(output_grid) + len(output_grid[0]) if output_grid and output_grid[0] else 1
        repetition_ratio = (repetitions['horizontal'] + repetitions['vertical']) / total_possible

        score = repetition_ratio * 0.4 + (repetitions['block'] * 0.6)

        details = {
            'repetitions_found': repetitions,
            'repetition_ratio': repetition_ratio,
            'total_repetitions': sum(repetitions.values())
        }

        return min(score, 1.0), details

    def _detect_scaling(self, input_grid: List[List[int]],
                       output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de mise à l'échelle (expansion, compression)
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Calcul des dimensions
        input_area = len(input_grid) * len(input_grid[0]) if input_grid and input_grid[0] else 0
        output_area = len(output_grid) * len(output_grid[0]) if output_grid and output_grid[0] else 0

        if input_area == 0:
            return 0.0, {"error": "Grille d'entrée vide"}

        scale_ratio = output_area / input_area

        # Analyse du pattern de scaling
        scaling_detected = False
        details = {
            'input_dimensions': f"{len(input_grid)}x{len(input_grid[0])}",
            'output_dimensions': f"{len(output_grid)}x{len(output_grid[0])}",
            'scale_ratio': scale_ratio,
            'scaling_type': 'unknown'
        }

        # Test d'expansion simple (répétition)
        if scale_ratio > 1 and self._is_simple_expansion(input_grid, output_grid):
            scaling_detected = True
            details['scaling_type'] = 'expansion'
            score = min(scale_ratio / 9.0, 0.8)  # Score basé sur le ratio, max 0.8
        elif scale_ratio < 1:
            details['scaling_type'] = 'compression'
            score = 0.3  # Compression détectée mais moins courante
        else:
            details['scaling_type'] = 'same_size'
            score = 0.0  # Pas de scaling

        return score, details

    def _detect_translation(self, input_grid: List[List[int]],
                           output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de translation/déplacement
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Recherche de motifs similaires à des positions différentes
        translation_score = 0.0
        translations = []

        # Analyse simplifiée: recherche de patterns similaires
        input_pixels = self._get_non_zero_pixels(input_grid)
        output_pixels = self._get_non_zero_pixels(output_grid)

        if len(input_pixels) == 0 or len(output_pixels) == 0:
            return 0.0, {"error": "Pas de pixels à analyser"}

        # Calcul de similarité entre patterns
        if len(input_pixels) <= len(output_pixels):
            # Recherche de translation possible
            for dx in [-2, -1, 0, 1, 2]:
                for dy in [-2, -1, 0, 1, 2]:
                    if dx == 0 and dy == 0:
                        continue
                    if self._check_translation(input_pixels, output_pixels, dx, dy):
                        translations.append((dx, dy))

        details = {
            'translations_found': len(translations),
            'translation_vectors': translations,
            'input_pixels': len(input_pixels),
            'output_pixels': len(output_pixels)
        }

        score = min(len(translations) * 0.3, 1.0)

        return score, details

    def _detect_filling(self, input_grid: List[List[int]],
                       output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de remplissage de zones fermées
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Compter les zones vides remplies
        input_empty = sum(1 for row in input_grid for cell in row if cell == 0)
        output_filled = sum(1 for row in output_grid for cell in row if cell != 0)

        if input_empty == 0:
            return 0.0, {"filling_ratio": 0, "note": "Aucune zone vide en entrée"}

        # Calcul du ratio de remplissage
        filling_ratio = 1 - (input_empty / (len(input_grid) * len(input_grid[0])))

        # Analyse de la cohérence du remplissage
        filling_consistency = self._analyze_filling_consistency(input_grid, output_grid)

        score = (filling_ratio * 0.6) + (filling_consistency * 0.4)

        details = {
            'input_empty_cells': input_empty,
            'filling_ratio': filling_ratio,
            'filling_consistency': filling_consistency,
            'total_cells': len(input_grid) * len(input_grid[0])
        }

        return min(score, 1.0), details

    def _detect_color_mapping(self, input_grid: List[List[int]],
                             output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de mapping de couleurs
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Analyse des couleurs utilisées
        input_colors = set()
        output_colors = set()

        for row in input_grid:
            input_colors.update(row)
        for row in output_grid:
            output_colors.update(row)

        # Calcul de la transformation de couleurs
        color_mapping = {}
        mapping_consistency = 0

        for color in input_colors:
            if color != 0:  # Ignore les cellules vides
                output_positions = []
                for i, row in enumerate(input_grid):
                    for j, cell in enumerate(row):
                        if cell == color and i < len(output_grid) and j < len(output_grid[0]):
                            output_positions.append(output_grid[i][j])

                if output_positions:
                    # Vérifier si toutes les positions ont la même couleur de sortie
                    unique_outputs = set(output_positions)
                    if len(unique_outputs) == 1:
                        color_mapping[color] = list(unique_outputs)[0]
                        mapping_consistency += 1

        consistency_ratio = mapping_consistency / max(len(input_colors) - (1 if 0 in input_colors else 0), 1)

        details = {
            'input_colors': sorted(list(input_colors)),
            'output_colors': sorted(list(output_colors)),
            'color_mapping': color_mapping,
            'mapping_consistency': consistency_ratio
        }

        return consistency_ratio, details

    def _detect_color_inversion(self, input_grid: List[List[int]],
                               output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns d'inversion de couleurs
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Analyse d'inversion simple
        inversion_score = 0.0
        inverted_pairs = []

        # Vérifier l'inversion 1↔2, etc.
        for i in range(len(input_grid)):
            for j in range(len(input_grid[0])):
                if (i < len(output_grid) and j < len(output_grid[0]) and
                    input_grid[i][j] != 0 and output_grid[i][j] != 0):
                    input_color = input_grid[i][j]
                    output_color = output_grid[i][j]

                    # Test d'inversion simple
                    if ((input_color == 1 and output_color == 2) or
                        (input_color == 2 and output_color == 1) or
                        (input_color == 3 and output_color == 4) or
                        (input_color == 4 and output_color == 3)):
                        inverted_pairs.append((input_color, output_color))

        if inverted_pairs:
            consistency = len(inverted_pairs) / (len(input_grid) * len(input_grid[0]))
            inversion_score = consistency
        else:
            consistency = 0

        details = {
            'inverted_pairs': inverted_pairs,
            'inversion_consistency': consistency,
            'total_positions': len(input_grid) * len(input_grid[0])
        }

        return inversion_score, details

    def _detect_gradient(self, input_grid: List[List[int]],
                        output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de gradients de couleur
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Gradient detection - à implémenter"}

    def _detect_completion(self, input_grid: List[List[int]],
                          output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de complétion de formes
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Shape completion - à implémenter"}

    def _detect_connection(self, input_grid: List[List[int]],
                          output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de connexion de points
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Point connection - à implémenter"}

    def _detect_extraction(self, input_grid: List[List[int]],
                          output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns d'extraction de motifs
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Pattern extraction - à implémenter"}

    # Méthodes utilitaires
    def _is_horizontally_symmetric(self, grid: List[List[int]]) -> bool:
        """Vérifie la symétrie horizontale"""
        if not grid or len(grid) < 2:
            return False

        rows = len(grid)
        for i in range(rows // 2):
            if grid[i] != grid[rows - 1 - i]:
                return False
        return True

    def _is_vertically_symmetric(self, grid: List[List[int]]) -> bool:
        """Vérifie la symétrie verticale"""
        if not grid or not grid[0] or len(grid[0]) < 2:
            return False

        cols = len(grid[0])
        for j in range(cols // 2):
            col1 = [row[j] for row in grid]
            col2 = [row[cols - 1 - j] for row in grid]
            if col1 != col2:
                return False
        return True

    def _is_diagonally_symmetric(self, grid: List[List[int]]) -> bool:
        """Vérifie la symétrie diagonale"""
        if not grid or len(grid) != len(grid[0]):
            return False

        size = len(grid)
        for i in range(size):
            for j in range(size):
                if grid[i][j] != grid[j][i]:
                    return False
        return True

    def _is_repeated_row(self, row: List[int]) -> bool:
        """Vérifie si une ligne est répétée"""
        if len(row) < 4:  # Trop petite pour détecter la répétition
            return False

        # Vérifier si la ligne se répète (ex: [1,2,1,2,1,2])
        half = len(row) // 2
        first_half = row[:half]
        second_half = row[half:2*half]

        return first_half == second_half

    def _is_repeated_column(self, column: List[int]) -> bool:
        """Vérifie si une colonne est répétée"""
        if len(column) < 4:
            return False

        half = len(column) // 2
        first_half = column[:half]
        second_half = column[half:2*half]

        return first_half == second_half

    def _detect_block_repetition(self, grid: List[List[int]]) -> bool:
        """Détecte la répétition de blocs"""
        if not grid or not grid[0]:
            return False

        rows, cols = len(grid), len(grid[0])

        # Test de répétition 2x2
        if rows >= 4 and cols >= 4:
            top_left = [grid[i][:2] for i in range(2)]
            top_right = [grid[i][2:4] for i in range(2)]
            bottom_left = [grid[i][:2] for i in range(2, 4)]
            bottom_right = [grid[i][2:4] for i in range(2, 4)]

            return (top_left == top_right == bottom_left == bottom_right)

        return False

    def _is_simple_expansion(self, input_grid: List[List[int]],
                           output_grid: List[List[int]]) -> bool:
        """Vérifie si c'est une expansion simple par répétition"""
        if not input_grid or not output_grid or not input_grid[0] or not output_grid[0]:
            return False

        # Vérifier si chaque cellule d'entrée est répétée dans la sortie
        input_rows, input_cols = len(input_grid), len(input_grid[0])
        output_rows, output_cols = len(output_grid), len(output_grid[0])

        # Ratio simple
        if output_rows % input_rows != 0 or output_cols % input_cols != 0:
            return False

        row_ratio = output_rows // input_rows
        col_ratio = output_cols // input_cols

        # Vérifier la répétition
        for i in range(input_rows):
            for j in range(input_cols):
                input_val = input_grid[i][j]
                # Vérifier le bloc correspondant dans la sortie
                for di in range(row_ratio):
                    for dj in range(col_ratio):
                        output_i = i * row_ratio + di
                        output_j = j * col_ratio + dj
                        if output_grid[output_i][output_j] != input_val:
                            return False

        return True

    def _get_non_zero_pixels(self, grid: List[List[int]]) -> List[Tuple[int, int, int]]:
        """Récupère les positions des pixels non-zéro avec leur valeur"""
        pixels = []
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell != 0:
                    pixels.append((i, j, cell))
        return pixels

    def _check_translation(self, input_pixels: List[Tuple[int, int, int]],
                          output_pixels: List[Tuple[int, int, int]],
                          dx: int, dy: int) -> bool:
        """Vérifie si les pixels correspondent après translation"""
        if len(input_pixels) != len(output_pixels):
            return False

        for (ix, iy, ival), (ox, oy, oval) in zip(input_pixels, output_pixels):
            if ix + dx != ox or iy + dy != oy or ival != oval:
                return False

        return True

    def _analyze_filling_consistency(self, input_grid: List[List[int]],
                                   output_grid: List[List[int]]) -> float:
        """Analyse la cohérence du remplissage"""
        # Version simplifiée
        return 0.5  # Score moyen par défaut

    def _calculate_confidence(self, score: float, category: str, pattern_name: str) -> float:
        """Calcule la confiance dans un pattern détecté"""
        # Facteurs de confiance par catégorie
        confidence_multipliers = {
            'spatial': 0.8,
            'color': 0.9,
            'structural': 0.7
        }

        base_confidence = confidence_multipliers.get(category, 0.5)
        return score * base_confidence

    def _calculate_overall_score(self, analysis: Dict[str, Any]) -> float:
        """Calcule le score global de l'analyse"""
        total_score = 0.0
        total_patterns = 0

        for category in ['spatial', 'color', 'structural']:
            if category in analysis:
                for pattern_name, pattern_data in analysis[category].items():
                    if pattern_data['confidence'] > self.confidence_threshold:
                        total_score += pattern_data['score']
                        total_patterns += 1

        return total_score / max(total_patterns, 1)

    def _get_recommendations(self, analysis: Dict[str, Any]) -> List[str]:
        """Génère des recommandations basées sur l'analyse"""
        recommendations = []

        # Rechercher les patterns avec haute confiance
        high_confidence_patterns = []
        for category in ['spatial', 'color', 'structural']:
            if category in analysis:
                for pattern_name, pattern_data in analysis[category].items():
                    if pattern_data['confidence'] > 0.7:
                        high_confidence_patterns.append(f"{category}.{pattern_name}")

        if high_confidence_patterns:
            recommendations.append(f"Patterns détectés avec haute confiance: {', '.join(high_confidence_patterns)}")

        # Vérifier le score global
        if analysis['overall_score'] < 0.3:
            recommendations.append("Score global faible - patterns complexes ou non détectés")
        elif analysis['overall_score'] > 0.7:
            recommendations.append("Score global élevé - patterns clairs détectés")

        return recommendations

    def test_pattern_detector(self):
        """Test du PatternDetector avec un exemple simple"""
        print("🧪 TEST DU PATTERN DETECTOR V2")
        print("=" * 40)

        # Exemple simple: expansion par répétition
        input_grid = [
            [1, 2],
            [3, 4]
        ]

        output_grid = [
            [1, 1, 2, 2],
            [1, 1, 2, 2],
            [3, 3, 4, 4],
            [3, 3, 4, 4]
        ]

        print("📊 ANALYSE D'UN EXEMPLE SIMPLE:")
        print("Input 2x2:")
        for row in input_grid:
            print(f"  {row}")

        print("\nOutput 4x4:")
        for row in output_grid:
            print(f"  {row}")

        analysis = self.analyze_puzzle(input_grid, output_grid)

        print(f"\n🎯 SCORE GLOBAL: {analysis['overall_score']:.2f}")
        print(f"📋 PATTERNS RECOMMANDES: {analysis['recommended_patterns']}")

        print("\n📈 DETAILS PAR CATEGORIE:")

        for category in ['spatial', 'color', 'structural']:
            if category in analysis:
                print(f"\n🔍 {category.upper()}:")
                for pattern_name, pattern_data in analysis[category].items():
                    confidence = pattern_data['confidence']
                    score = pattern_data['score']
                    print(f"  {pattern_name}: score={score:.2f}, confidence={confidence:.2f}")
        return analysis

if __name__ == "__main__":
    detector = PatternDetector()
    detector.test_pattern_detector()
