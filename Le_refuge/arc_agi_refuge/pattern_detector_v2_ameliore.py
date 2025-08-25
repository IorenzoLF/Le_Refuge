#!/usr/bin/env python3
"""
PatternDetector v2 Amélioré - Patterns Géométriques et Mathématiques
Version étendue avec transformations géométriques complexes
"""

import json
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
import math
import copy
from pattern_detector_v2 import PatternDetector

class PatternDetectorAmeliore(PatternDetector):
    """
    PatternDetector v2 amélioré avec patterns géométriques et mathématiques
    """

    def __init__(self):
        # Appeler le constructeur parent
        super().__init__()

        # Étendre les patterns existants avec les nouveaux
        self.spatial_patterns.update({
            # Nouveaux patterns géométriques
            'rotation': self._detect_rotation,
            'homothety': self._detect_homothety,
            'shear': self._detect_shear,
            'reflection': self._detect_reflection,
            'fractal': self._detect_fractal
        })

        self.color_patterns.update({
            # Nouveaux patterns couleur
            'cycling': self._detect_color_cycling,
            'blending': self._detect_color_blending
        })

        self.structural_patterns.update({
            # Nouveaux patterns structuraux
            'projection': self._detect_projection,
            'folding': self._detect_folding
        })

        # Nouveaux patterns mathématiques
        self.mathematical_patterns = {
            'arithmetic': self._detect_arithmetic_progression,
            'geometric': self._detect_geometric_progression,
            'parity': self._detect_parity_pattern,
            'modulo': self._detect_modulo_pattern,
            'linear_transform': self._detect_linear_transform
        }

    def analyze_puzzle_complete(self, input_grid: List[List[int]],
                               output_grid: List[List[int]]) -> Dict[str, Any]:
        """
        Analyse complète avec tous les types de patterns
        """
        analysis = {
            'spatial': {},
            'color': {},
            'structural': {},
            'mathematical': {},  # Nouveau
            'overall_score': 0,
            'detected_patterns_count': 0,
            'high_confidence_patterns': [],
            'pattern_combinations': []
        }

        # Analyse de tous les types de patterns
        pattern_categories = {
            'spatial': self.spatial_patterns,
            'color': self.color_patterns,
            'structural': self.structural_patterns,
            'mathematical': self.mathematical_patterns
        }

        for category_name, patterns in pattern_categories.items():
            for pattern_name, detector_func in patterns.items():
                try:
                    score, details = detector_func(input_grid, output_grid)
                    analysis[category_name][pattern_name] = {
                        'score': score,
                        'details': details,
                        'confidence': self._calculate_confidence(score, category_name, pattern_name)
                    }

                    if score > self.confidence_threshold:
                        analysis['high_confidence_patterns'].append(f"{category_name}.{pattern_name}")

                except Exception as e:
                    analysis[category_name][pattern_name] = {
                        'score': 0,
                        'details': f"Erreur: {str(e)}",
                        'confidence': 0
                    }

        # Statistiques
        analysis['detected_patterns_count'] = len(analysis['high_confidence_patterns'])
        analysis['overall_score'] = self._calculate_overall_score(analysis)

        # Détection de combinaisons de patterns
        analysis['pattern_combinations'] = self._detect_pattern_combinations(analysis)

        return analysis

    # ============ NOUVEAUX PATTERNS GÉOMÉTRIQUES ============

    def _detect_rotation(self, input_grid: List[List[int]],
                        output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de rotation (90°, 180°, 270°)
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Test des rotations possibles
        rotations = []
        input_pixels = self._get_non_zero_pixels(input_grid)

        for angle in [90, 180, 270]:
            rotated_grid = self._rotate_grid(input_grid, angle)
            similarity = self._calculate_grid_similarity(rotated_grid, output_grid)
            if similarity > 0.7:
                rotations.append({
                    'angle': angle,
                    'similarity': similarity
                })

        if rotations:
            best_rotation = max(rotations, key=lambda x: x['similarity'])
            score = best_rotation['similarity']
            details = {
                'rotations_found': rotations,
                'best_rotation': best_rotation,
                'rotation_type': f"{best_rotation['angle']}° rotation"
            }
        else:
            score = 0.0
            details = {"rotations_found": [], "note": "Aucune rotation détectée"}

        return min(score, 1.0), details

    def _detect_homothety(self, input_grid: List[List[int]],
                         output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les homothéties (agrandissement/réduction avec centre)
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Calcul des ratios de dimensions
        input_h, input_w = len(input_grid), len(input_grid[0])
        output_h, output_w = len(output_grid), len(output_grid[0])

        # Ratio approximatif (pour les cas simples)
        ratio_h = output_h / input_h if input_h > 0 else 0
        ratio_w = output_w / input_w if input_w > 0 else 0

        # Vérifier si c'est un ratio simple (2, 3, 1/2, etc.)
        simple_ratios = [0.5, 1, 2, 3, 4]
        is_simple_ratio = any(abs(ratio_h - r) < 0.1 and abs(ratio_w - r) < 0.1 for r in simple_ratios)

        if is_simple_ratio:
            score = 0.8  # Score élevé pour ratio simple
            details = {
                'ratio_h': ratio_h,
                'ratio_w': ratio_w,
                'is_homothety': True,
                'homothety_type': f"Scale by {ratio_h}"
            }
        else:
            score = 0.0
            details = {
                'ratio_h': ratio_h,
                'ratio_w': ratio_w,
                'is_homothety': False,
                'note': "Ratio complexe - pas une homothétie simple"
            }

        return score, details

    def _detect_shear(self, input_grid: List[List[int]],
                     output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les cisaillements (shear transformations)
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Shear detection - à développer"}

    def _detect_reflection(self, input_grid: List[List[int]],
                          output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les réflexions (plus complexe que les symétries simples)
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Test des réflexions par rapport à différents axes
        reflections = []

        # Réflexion horizontale
        reflected_h = [row[::-1] for row in input_grid]
        similarity_h = self._calculate_grid_similarity(reflected_h, output_grid)
        if similarity_h > 0.7:
            reflections.append({'axis': 'horizontal', 'similarity': similarity_h})

        # Réflexion verticale
        reflected_v = input_grid[::-1]
        similarity_v = self._calculate_grid_similarity(reflected_v, output_grid)
        if similarity_v > 0.7:
            reflections.append({'axis': 'vertical', 'similarity': similarity_v})

        if reflections:
            best_reflection = max(reflections, key=lambda x: x['similarity'])
            score = best_reflection['similarity']
            details = {
                'reflections_found': reflections,
                'best_reflection': best_reflection,
                'reflection_type': f"Reflection over {best_reflection['axis']} axis"
            }
        else:
            score = 0.0
            details = {"reflections_found": [], "note": "Aucune réflexion détectée"}

        return min(score, 1.0), details

    def _detect_fractal(self, input_grid: List[List[int]],
                        output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns fractals ou auto-similaires
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Fractal detection - à développer"}

    # ============ NOUVEAUX PATTERNS COULEUR ============

    def _detect_color_cycling(self, input_grid: List[List[int]],
                             output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les cycles de couleur (1→2→3→1)
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Analyser les transformations de couleur
        color_transforms = defaultdict(list)

        for i in range(len(input_grid)):
            for j in range(len(input_grid[0])):
                if (i < len(output_grid) and j < len(output_grid[0]) and
                    input_grid[i][j] != 0 and output_grid[i][j] != 0):
                    color_transforms[input_grid[i][j]].append(output_grid[i][j])

        # Détecter les cycles
        cycles_detected = []
        for input_color, output_colors in color_transforms.items():
            if len(set(output_colors)) == 1:  # Même couleur de sortie
                output_color = output_colors[0]
                if output_color != input_color:
                    cycles_detected.append(f"{input_color}→{output_color}")

        if cycles_detected:
            score = min(len(cycles_detected) * 0.3, 1.0)
            details = {
                'cycles_detected': cycles_detected,
                'cycle_count': len(cycles_detected),
                'color_transforms': dict(color_transforms)
            }
        else:
            score = 0.0
            details = {"cycles_detected": [], "note": "Aucun cycle détecté"}

        return score, details

    def _detect_color_blending(self, input_grid: List[List[int]],
                              output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les mélanges de couleurs
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Color blending - à développer"}

    # ============ NOUVEAUX PATTERNS STRUCTURAUX ============

    def _detect_projection(self, input_grid: List[List[int]],
                          output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les projections (par exemple, projection d'ombre)
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Projection detection - à développer"}

    def _detect_folding(self, input_grid: List[List[int]],
                        output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns de pliage
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Folding detection - à développer"}

    # ============ NOUVEAUX PATTERNS MATHÉMATIQUES ============

    def _detect_arithmetic_progression(self, input_grid: List[List[int]],
                                      output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les progressions arithmétiques
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Analyser les valeurs numériques
        input_values = [cell for row in input_grid for cell in row if cell != 0]
        output_values = [cell for row in output_grid for cell in row if cell != 0]

        if len(input_values) < 3 or len(output_values) < 3:
            return 0.0, {"note": "Pas assez de valeurs pour détecter une progression"}

        # Calcul de la différence commune pour input
        input_diffs = []
        for i in range(len(input_values) - 1):
            input_diffs.append(input_values[i+1] - input_values[i])

        # Calcul de la différence commune pour output
        output_diffs = []
        for i in range(len(output_values) - 1):
            output_diffs.append(output_values[i+1] - output_values[i])

        # Vérifier si c'est une progression arithmétique
        if len(set(input_diffs)) == 1 and len(set(output_diffs)) == 1:
            input_diff = list(set(input_diffs))[0]
            output_diff = list(set(output_diffs))[0]

            if abs(input_diff - output_diff) <= 1:  # Même différence ou proche
                score = 0.8
                details = {
                    'input_difference': input_diff,
                    'output_difference': output_diff,
                    'is_arithmetic': True,
                    'input_values': sorted(input_values),
                    'output_values': sorted(output_values)
                }
            else:
                score = 0.0
                details = {"note": "Différences différentes entre input et output"}
        else:
            score = 0.0
            details = {"note": "Pas de progression arithmétique détectée"}

        return score, details

    def _detect_geometric_progression(self, input_grid: List[List[int]],
                                     output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les progressions géométriques
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Geometric progression - à développer"}

    def _detect_parity_pattern(self, input_grid: List[List[int]],
                              output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns basés sur la parité (pair/impair)
        """
        if not input_grid or not output_grid:
            return 0.0, {"error": "Grilles vides"}

        # Compter les nombres pairs et impairs
        input_even = sum(1 for row in input_grid for cell in row if cell % 2 == 0 and cell != 0)
        input_odd = sum(1 for row in input_grid for cell in row if cell % 2 == 1)

        output_even = sum(1 for row in output_grid for cell in row if cell % 2 == 0 and cell != 0)
        output_odd = sum(1 for row in output_grid for cell in row if cell % 2 == 1)

        # Vérifier les patterns de parité
        input_total = input_even + input_odd
        output_total = output_even + output_odd

        if input_total == 0 or output_total == 0:
            return 0.0, {"note": "Pas de valeurs numériques"}

        # Pattern détecté si la proportion de parité change de manière cohérente
        input_even_ratio = input_even / input_total
        output_even_ratio = output_even / output_total

        ratio_change = abs(input_even_ratio - output_even_ratio)

        if ratio_change > 0.7:  # Changement significatif de parité
            score = min(ratio_change, 1.0)
            details = {
                'input_even': input_even,
                'input_odd': input_odd,
                'output_even': output_even,
                'output_odd': output_odd,
                'input_even_ratio': input_even_ratio,
                'output_even_ratio': output_even_ratio,
                'parity_change': ratio_change,
                'is_parity_pattern': True
            }
        else:
            score = 0.0
            details = {"note": "Pas de pattern de parité détecté"}

        return score, details

    def _detect_modulo_pattern(self, input_grid: List[List[int]],
                              output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les patterns basés sur modulo
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Modulo pattern - à développer"}

    def _detect_linear_transform(self, input_grid: List[List[int]],
                                output_grid: List[List[int]]) -> Tuple[float, Dict[str, Any]]:
        """
        Détecte les transformations linéaires
        """
        # Version simplifiée pour commencer
        return 0.0, {"note": "Linear transform - à développer"}

    # ============ MÉTHODES UTILITAIRES ============

    def _rotate_grid(self, grid: List[List[int]], angle: int) -> List[List[int]]:
        """
        Effectue une rotation de la grille
        """
        if not grid or angle not in [90, 180, 270]:
            return grid

        if angle == 90:
            return [list(reversed(col)) for col in zip(*grid)]
        elif angle == 180:
            return [row[::-1] for row in grid[::-1]]
        elif angle == 270:
            return [list(col) for col in zip(*[row[::-1] for row in grid])]
        else:
            return grid

    def _calculate_grid_similarity(self, grid1: List[List[int]], grid2: List[List[int]]) -> float:
        """
        Calcule la similarité entre deux grilles
        """
        if not grid1 or not grid2:
            return 0

        max_rows = max(len(grid1), len(grid2))
        max_cols = max(len(grid1[0]) if grid1 else 0, len(grid2[0]) if grid2 else 0)

        matching = 0
        total = max_rows * max_cols

        for i in range(max_rows):
            for j in range(max_cols):
                val1 = grid1[i][j] if i < len(grid1) and j < len(grid1[0]) else 0
                val2 = grid2[i][j] if i < len(grid2) and j < len(grid2[0]) else 0
                if val1 == val2:
                    matching += 1

        return matching / total

    def _get_non_zero_pixels(self, grid: List[List[int]]) -> List[Tuple[int, int, int]]:
        """Récupère les positions des pixels non-zéro"""
        pixels = []
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell != 0:
                    pixels.append((i, j, cell))
        return pixels

    def _calculate_confidence(self, score: float, category: str, pattern_name: str) -> float:
        """Calcule la confiance dans un pattern"""
        confidence_multipliers = {
            'spatial': 0.8,
            'color': 0.9,
            'structural': 0.7,
            'mathematical': 0.85  # Nouveau
        }

        base_confidence = confidence_multipliers.get(category, 0.5)
        return score * base_confidence

    def _calculate_overall_score(self, analysis: Dict[str, Any]) -> float:
        """Calcule le score global"""
        total_score = 0.0
        total_patterns = 0

        for category in ['spatial', 'color', 'structural', 'mathematical']:
            if category in analysis:
                for pattern_name, pattern_data in analysis[category].items():
                    if pattern_data['confidence'] > self.confidence_threshold:
                        total_score += pattern_data['score']
                        total_patterns += 1

        return total_score / max(total_patterns, 1)

    def _detect_pattern_combinations(self, analysis: Dict[str, Any]) -> List[str]:
        """Détecte les combinaisons intéressantes de patterns"""
        combinations = []
        high_confidence = analysis.get('high_confidence_patterns', [])

        # Combinaisons connues intéressantes
        spatial_patterns = [p for p in high_confidence if p.startswith('spatial.')]
        color_patterns = [p for p in high_confidence if p.startswith('color.')]
        math_patterns = [p for p in high_confidence if p.startswith('mathematical.')]

        if spatial_patterns and color_patterns:
            combinations.append("Spatial + Color: Transformation géométrique avec changement de couleur")

        if spatial_patterns and math_patterns:
            combinations.append("Spatial + Mathematical: Règles géométriques avec logique mathématique")

        if color_patterns and math_patterns:
            combinations.append("Color + Mathematical: Transformations colorées basées sur des calculs")

        return combinations

    def test_améliorations(self):
        """Test les améliorations du PatternDetector"""
        print("🧪 TEST DES AMÉLIORATIONS PATTERNDETECTOR V2")
        print("=" * 55)

        # Test 1: Rotation 90°
        print("\n🔄 TEST 1: ROTATION 90°")
        input_rotation = [
            [1, 2],
            [3, 4]
        ]
        output_rotation = [
            [3, 1],
            [4, 2]
        ]

        analysis = self.analyze_puzzle_complete(input_rotation, output_rotation)
        rotation_score = analysis['spatial']['rotation']['score']
        print(".2f")

        # Test 2: Réflexion
        print("\n🪞 TEST 2: RÉFLEXION")
        input_reflect = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        output_reflect = [
            [3, 2, 1],
            [6, 5, 4],
            [9, 8, 7]
        ]

        analysis = self.analyze_puzzle_complete(input_reflect, output_reflect)
        reflection_score = analysis['spatial']['reflection']['score']
        print(".2f")

        # Test 3: Progression arithmétique
        print("\n🔢 TEST 3: PROGRESSION ARITHMÉTIQUE")
        input_arith = [
            [1, 2],
            [2, 3]
        ]
        output_arith = [
            [2, 3],
            [3, 4]
        ]

        analysis = self.analyze_puzzle_complete(input_arith, output_arith)
        arithmetic_score = analysis['mathematical']['arithmetic']['score']
        print(".2f")

        # Test 4: Pattern de parité
        print("\n⚖️ TEST 4: PATTERN DE PARITÉ")
        input_parity = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        output_parity = [
            [2, 1, 4],
            [5, 3, 6]  # Inversion des nombres impairs
        ]

        analysis = self.analyze_puzzle_complete(input_parity, output_parity)
        parity_score = analysis['mathematical']['parity']['score']
        print(".2f")

        # Synthèse
        print("\n📊 SYNTHÈSE DES AMÉLIORATIONS:")
        improvements = {
            "Rotation": rotation_score,
            "Réflexion": reflection_score,
            "Progression arithmétique": arithmetic_score,
            "Parité": parity_score
        }

        total_improved = sum(1 for score in improvements.values() if score > 0.5)
        avg_score = sum(improvements.values()) / len(improvements)

        print(".2f")
        print(".1f")
        print(f"   Améliorations fonctionnelles: {total_improved}/{len(improvements)}")

        for pattern, score in improvements.items():
            status = "✅" if score > 0.5 else "⚠️" if score > 0.2 else "❌"
            print(".2f")

        return improvements

if __name__ == "__main__":
    detector = PatternDetectorAmeliore()
    detector.test_améliorations()
