#!/usr/bin/env python3
"""
PatternScorer v2 - Évaluation des patterns avec métriques anti-surapprentissage
Architecture pour prévenir le surapprentissage systémique
"""

import json
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
import math

class PatternScorer:
    """
    Évaluateur de patterns avec métriques anti-surapprentissage
    Version 2: Focus sur la généralisation et la robustesse
    """

    def __init__(self):
        self.overfitting_threshold = 0.3  # Seuil de détection du surapprentissage
        self.generalization_weight = 0.4  # Poids de la généralisation
        self.simplicity_weight = 0.3      # Poids de la simplicité
        self.robustness_weight = 0.3      # Poids de la robustesse

    def score_pattern_comprehensive(self, pattern_name: str, pattern_data: Dict[str, Any],
                                 input_grid: List[List[int]], output_grid: List[List[int]],
                                 training_examples: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Évaluation complète d'un pattern avec métriques anti-surapprentissage
        """
        scores = {
            'pattern_name': pattern_name,
            'raw_score': pattern_data.get('score', 0),
            'confidence': pattern_data.get('confidence', 0),
            'generalization_score': 0,
            'simplicity_score': 0,
            'robustness_score': 0,
            'overfitting_risk': 0,
            'final_score': 0,
            'recommendations': [],
            'warnings': []
        }

        # Calcul des métriques individuelles
        scores['generalization_score'] = self._calculate_generalization_score(
            pattern_name, pattern_data, training_examples
        )

        scores['simplicity_score'] = self._calculate_simplicity_score(
            pattern_name, pattern_data
        )

        scores['robustness_score'] = self._calculate_robustness_score(
            pattern_name, pattern_data, input_grid, output_grid
        )

        # Évaluation du risque de surapprentissage
        scores['overfitting_risk'] = self._assess_overfitting_risk(
            scores, training_examples
        )

        # Score final pondéré
        scores['final_score'] = self._calculate_final_score(scores)

        # Génération de recommandations
        scores['recommendations'] = self._generate_recommendations(scores)
        scores['warnings'] = self._generate_warnings(scores)

        return scores

    def _calculate_generalization_score(self, pattern_name: str, pattern_data: Dict[str, Any],
                                      training_examples: List[Dict[str, Any]] = None) -> float:
        """
        Évalue la capacité de généralisation du pattern
        """
        if not training_examples or len(training_examples) < 2:
            return 0.5  # Score neutre si pas assez de données

        generalization_score = 0.0
        consistency_count = 0
        total_comparisons = 0

        # Test de validation croisée simple
        for i, test_example in enumerate(training_examples):
            # Utiliser les autres exemples comme entraînement
            training_subset = [ex for j, ex in enumerate(training_examples) if j != i]

            # Simuler l'application du pattern sur l'exemple de test
            simulated_score = self._simulate_pattern_application(
                pattern_name, pattern_data, test_example, training_subset
            )

            if simulated_score > 0.5:  # Pattern s'applique bien
                consistency_count += 1
            total_comparisons += 1

        if total_comparisons > 0:
            generalization_score = consistency_count / total_comparisons

        # Pénalité pour les patterns trop spécifiques
        if "specific" in pattern_name.lower() or "exact" in pattern_name.lower():
            generalization_score *= 0.7

        return generalization_score

    def _calculate_simplicity_score(self, pattern_name: str, pattern_data: Dict[str, Any]) -> float:
        """
        Évalue la simplicité du pattern (principe de parcimonie)
        """
        simplicity_score = 1.0  # Score de base

        # Pénalité pour les patterns complexes
        if "complex" in pattern_name.lower() or "advanced" in pattern_name.lower():
            simplicity_score *= 0.8

        # Bonus pour les patterns fondamentaux
        fundamental_patterns = [
            'symmetry', 'repetition', 'scaling', 'color_mapping'
        ]
        if any(fundamental in pattern_name for fundamental in fundamental_patterns):
            simplicity_score *= 1.1

        # Ajustement basé sur le score brut (patterns simples ont souvent des scores nets)
        raw_score = pattern_data.get('score', 0)
        if raw_score > 0.8:  # Score très élevé peut indiquer sur-spécialisation
            simplicity_score *= 0.9
        elif raw_score < 0.3:  # Score faible peut indiquer pattern trop complexe
            simplicity_score *= 0.8

        return min(simplicity_score, 1.0)

    def _calculate_robustness_score(self, pattern_name: str, pattern_data: Dict[str, Any],
                                  input_grid: List[List[int]], output_grid: List[List[int]]) -> float:
        """
        Évalue la robustesse du pattern face aux variations
        """
        robustness_score = 0.0

        # Test de stabilité face au bruit
        noise_resistance = self._test_noise_resistance(pattern_name, input_grid, output_grid)
        robustness_score += noise_resistance * 0.3

        # Test de stabilité face aux changements de dimensions
        dimension_resistance = self._test_dimension_resistance(pattern_name, pattern_data)
        robustness_score += dimension_resistance * 0.3

        # Test de cohérence interne
        internal_consistency = self._test_internal_consistency(pattern_data)
        robustness_score += internal_consistency * 0.4

        return robustness_score

    def _assess_overfitting_risk(self, scores: Dict[str, float],
                               training_examples: List[Dict[str, Any]] = None) -> float:
        """
        Évalue le risque de surapprentissage
        """
        overfitting_risk = 0.0

        # Risque basé sur l'écart entre score brut et score de généralisation
        raw_score = scores.get('raw_score', 0)
        generalization_score = scores.get('generalization_score', 0)

        if raw_score > 0.8 and generalization_score < 0.4:
            overfitting_risk += 0.6  # Fort risque de surapprentissage

        # Risque basé sur la simplicité (patterns trop complexes)
        simplicity_score = scores.get('simplicity_score', 0)
        if simplicity_score < 0.5:
            overfitting_risk += 0.3

        # Risque basé sur le nombre d'exemples
        if training_examples and len(training_examples) < 3:
            overfitting_risk += 0.2

        # Risque basé sur la confiance (trop de confiance peut indiquer sur-optimisation)
        confidence = scores.get('confidence', 0)
        if confidence > 0.9 and generalization_score < 0.5:
            overfitting_risk += 0.2

        return min(overfitting_risk, 1.0)

    def _calculate_final_score(self, scores: Dict[str, float]) -> float:
        """
        Calcule le score final pondéré
        """
        generalization = scores.get('generalization_score', 0)
        simplicity = scores.get('simplicity_score', 0)
        robustness = scores.get('robustness_score', 0)
        overfitting_risk = scores.get('overfitting_risk', 0)

        # Score de base pondéré
        base_score = (
            generalization * self.generalization_weight +
            simplicity * self.simplicity_weight +
            robustness * self.robustness_weight
        )

        # Pénalité pour le risque de surapprentissage
        penalty = overfitting_risk * 0.3

        final_score = base_score * (1 - penalty)

        return max(0, min(final_score, 1.0))

    def _generate_recommendations(self, scores: Dict[str, float]) -> List[str]:
        """
        Génère des recommandations basées sur les scores
        """
        recommendations = []

        generalization = scores.get('generalization_score', 0)
        simplicity = scores.get('simplicity_score', 0)
        overfitting_risk = scores.get('overfitting_risk', 0)

        if generalization < 0.4:
            recommendations.append("Améliorer la généralisation - tester sur plus d'exemples")

        if simplicity < 0.5:
            recommendations.append("Simplifier le pattern - rechercher une solution plus élégante")

        if overfitting_risk > 0.5:
            recommendations.append("Réduire le risque de surapprentissage - ajouter de la régularisation")

        if generalization > 0.7 and simplicity > 0.7:
            recommendations.append("Pattern de qualité - peut être utilisé en production")

        return recommendations

    def _generate_warnings(self, scores: Dict[str, float]) -> List[str]:
        """
        Génère des avertissements basés sur les scores
        """
        warnings = []

        overfitting_risk = scores.get('overfitting_risk', 0)
        confidence = scores.get('confidence', 0)
        raw_score = scores.get('raw_score', 0)

        if overfitting_risk > 0.7:
            warnings.append("ALERTE: Risque élevé de surapprentissage")

        if confidence > 0.9 and raw_score > 0.8:
            warnings.append("ATTENTION: Possible sur-confiance dans le pattern")

        if raw_score < 0.2:
            warnings.append("NOTE: Pattern faiblement détecté - résultats incertains")

        return warnings

    # Méthodes utilitaires
    def _simulate_pattern_application(self, pattern_name: str, pattern_data: Dict[str, Any],
                                    test_example: Dict[str, Any],
                                    training_examples: List[Dict[str, Any]]) -> float:
        """
        Simule l'application du pattern sur un exemple de test
        """
        # Version simplifiée de simulation
        # Dans une implémentation réelle, on testerait vraiment l'application

        # Score basé sur la cohérence du pattern
        base_consistency = pattern_data.get('score', 0)

        # Ajustement basé sur la similarité avec les exemples d'entraînement
        similarity_bonus = 0.0
        if training_examples:
            avg_similarity = sum(self._calculate_example_similarity(test_example, ex)
                               for ex in training_examples) / len(training_examples)
            similarity_bonus = avg_similarity * 0.2

        return min(base_consistency + similarity_bonus, 1.0)

    def _calculate_example_similarity(self, ex1: Dict[str, Any], ex2: Dict[str, Any]) -> float:
        """
        Calcule la similarité entre deux exemples
        """
        # Similarité basée sur les dimensions
        input1 = ex1.get('input', [])
        input2 = ex2.get('input', [])
        output1 = ex1.get('output', [])
        output2 = ex2.get('output', [])

        if not input1 or not input2:
            return 0

        dim_similarity = 1.0 if (len(input1) == len(input2) and
                                len(input1[0]) == len(input2[0])) else 0.5

        return dim_similarity

    def _test_noise_resistance(self, pattern_name: str, input_grid: List[List[int]],
                             output_grid: List[List[int]]) -> float:
        """
        Teste la résistance au bruit du pattern
        """
        # Version simplifiée - test avec un pixel modifié
        if not input_grid or not input_grid[0]:
            return 0

        # Créer une version avec bruit
        noisy_input = [row[:] for row in input_grid]
        if len(noisy_input) > 0 and len(noisy_input[0]) > 0:
            # Modifier un pixel (simuler du bruit)
            noisy_input[0][0] = (noisy_input[0][0] + 1) % 10

        # Dans une vraie implémentation, on testerait si le pattern
        # reste détectable avec le bruit
        return 0.7  # Score conservateur

    def _test_dimension_resistance(self, pattern_name: str, pattern_data: Dict[str, Any]) -> float:
        """
        Teste la résistance aux changements de dimensions
        """
        # Patterns spatiaux sont plus sensibles aux dimensions
        if 'spatial' in pattern_name:
            return 0.6
        elif 'color' in pattern_name:
            return 0.8  # Plus robuste
        else:
            return 0.7

    def _test_internal_consistency(self, pattern_data: Dict[str, Any]) -> float:
        """
        Teste la cohérence interne du pattern
        """
        details = pattern_data.get('details', {})

        if isinstance(details, dict):
            # Vérifier la présence d'informations cohérentes
            if len(details) > 2:  # Pattern bien décrit
                return 0.8
            elif len(details) > 0:  # Informations basiques
                return 0.6
            else:
                return 0.4  # Peu d'informations

        return 0.5  # Score par défaut

    def evaluate_pattern_suite(self, patterns_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Évalue une suite complète de patterns détectés
        """
        evaluation = {
            'overall_quality': 0,
            'pattern_diversity': 0,
            'overfitting_risk': 0,
            'recommended_patterns': [],
            'pattern_conflicts': [],
            'quality_report': []
        }

        if not patterns_analysis:
            return evaluation

        # Évaluer chaque pattern
        scored_patterns = []
        for category in ['spatial', 'color', 'structural']:
            if category in patterns_analysis:
                for pattern_name, pattern_data in patterns_analysis[category].items():
                    score = self.score_pattern_comprehensive(
                        f"{category}.{pattern_name}",
                        pattern_data,
                        [], [],  # Grilles vides pour l'instant
                        None    # Pas d'exemples d'entraînement
                    )
                    scored_patterns.append(score)

        if scored_patterns:
            # Calcul de la qualité globale
            avg_final_score = sum(p['final_score'] for p in scored_patterns) / len(scored_patterns)
            evaluation['overall_quality'] = avg_final_score

            # Diversité des patterns
            categories_used = set(p['pattern_name'].split('.')[0] for p in scored_patterns)
            evaluation['pattern_diversity'] = len(categories_used) / 3  # Max 3 catégories

            # Risque global de surapprentissage
            avg_overfitting_risk = sum(p['overfitting_risk'] for p in scored_patterns) / len(scored_patterns)
            evaluation['overfitting_risk'] = avg_overfitting_risk

            # Patterns recommandés (score final > 0.6)
            recommended = [p['pattern_name'] for p in scored_patterns if p['final_score'] > 0.6]
            evaluation['recommended_patterns'] = recommended

            # Rapport de qualité
            evaluation['quality_report'] = [
                ".2f",
                ".2f",
                ".2f",
                f"Patterns recommandés: {len(recommended)}/{len(scored_patterns)}"
            ]

        return evaluation

    def generate_anti_overfitting_report(self, patterns_analysis: Dict[str, Any]) -> str:
        """
        Génère un rapport anti-surapprentissage détaillé
        """
        evaluation = self.evaluate_pattern_suite(patterns_analysis)

        report = ".2f"
        report += "\n" + "=" * 60

        report += ".2f"
        report += ".2f"
        report += ".2f"

        if evaluation['recommended_patterns']:
            report += "\n\n✅ PATTERNS RECOMMANDÉS:"
            for pattern in evaluation['recommended_patterns']:
                report += f"\n   • {pattern}"

        report += "\n\n📊 RAPPORT DE QUALITÉ:"
        for item in evaluation['quality_report']:
            report += f"\n   • {item}"

        # Recommandations spécifiques
        if evaluation['overfitting_risk'] > 0.5:
            report += "\n\n⚠️ RECOMMANDATIONS ANTI-SURAPPRENTISSAGE:"
            report += "\n   • Ajouter plus d'exemples de validation"
            report += "\n   • Simplifier les patterns complexes"
            report += "\n   • Tester sur des données non vues"

        if evaluation['pattern_diversity'] < 0.5:
            report += "\n\n💡 SUGGESTIONS D'AMÉLIORATION:"
            report += "\n   • Explorer d'autres catégories de patterns"
            report += "\n   • Combiner plusieurs types de patterns"
            report += "\n   • Tester des patterns plus génériques"

        return report
