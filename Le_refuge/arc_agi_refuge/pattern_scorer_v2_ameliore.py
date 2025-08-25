#!/usr/bin/env python3
"""
PatternScorer v2 Amélioré - Évaluation Anti-Surapprentissage Avancée
Métriques sophistiquées pour prévenir le surapprentissage systémique
"""

import json
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
import math
import statistics
import copy

class PatternScorerAmeliore:
    """
    PatternScorer v2 amélioré avec métriques anti-surapprentissage avancées
    """

    def __init__(self):
        # Seuils de détection du surapprentissage
        self.overfitting_threshold = 0.3
        self.generalization_weight = 0.4
        self.simplicity_weight = 0.3
        self.robustness_weight = 0.3

        # Métriques de validation croisée
        self.cross_validation_folds = 3
        self.validation_split_ratio = 0.2

        # Historique des évaluations pour détecter les tendances
        self.evaluation_history = defaultdict(list)

        # Métriques de référence pour différents types de patterns
        self.baseline_metrics = {
            'spatial': {
                'generalization': 0.65,
                'simplicity': 0.7,
                'robustness': 0.75
            },
            'color': {
                'generalization': 0.75,
                'simplicity': 0.8,
                'robustness': 0.85
            },
            'structural': {
                'generalization': 0.6,
                'simplicity': 0.65,
                'robustness': 0.7
            },
            'mathematical': {
                'generalization': 0.7,
                'simplicity': 0.75,
                'robustness': 0.8
            }
        }

    def evaluate_pattern_comprehensive_advanced(self, pattern_name: str,
                                               pattern_data: Dict[str, Any],
                                               input_grid: List[List[int]],
                                               output_grid: List[List[int]],
                                               training_examples: Optional[List[Dict[str, Any]]] = None,
                                               validation_examples: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Évaluation complète et avancée d'un pattern avec métriques anti-surapprentissage
        """
        evaluation = {
            'pattern_name': pattern_name,
            'timestamp': self._get_timestamp(),
            'metrics': {},
            'overfitting_analysis': {},
            'validation_results': {},
            'recommendations': [],
            'warnings': [],
            'improvement_suggestions': []
        }

        # Métriques de base
        evaluation['metrics'] = self._compute_advanced_metrics(
            pattern_name, pattern_data, training_examples, validation_examples
        )

        # Analyse du surapprentissage
        evaluation['overfitting_analysis'] = self._analyze_overfitting_risk_advanced(
            evaluation['metrics'], training_examples
        )

        # Validation croisée
        if training_examples and len(training_examples) >= self.cross_validation_folds:
            evaluation['validation_results'] = self._perform_cross_validation(
                pattern_name, pattern_data, training_examples
            )
        else:
            evaluation['validation_results'] = {'status': 'insufficient_data'}

        # Score final avec analyse de tendance
        evaluation['final_score'] = self._compute_final_score_with_trends(evaluation)

        # Recommandations et avertissements (après calcul du score final)
        evaluation['recommendations'] = self._generate_advanced_recommendations(evaluation)
        evaluation['warnings'] = self._generate_advanced_warnings(evaluation)
        evaluation['improvement_suggestions'] = self._generate_improvement_suggestions(evaluation)

        # Sauvegarder dans l'historique
        self._update_evaluation_history(pattern_name, evaluation)

        return evaluation

    def _compute_advanced_metrics(self, pattern_name: str, pattern_data: Dict[str, Any],
                                training_examples: Optional[List[Dict[str, Any]]] = None,
                                validation_examples: Optional[List[Dict[str, Any]]] = None) -> Dict[str, float]:
        """
        Calcul de métriques avancées
        """
        metrics = {}

        # 1. Métrique de généralisation avancée
        metrics['generalization_score'] = self._compute_generalization_advanced(
            pattern_name, pattern_data, training_examples, validation_examples
        )

        # 2. Métrique de simplicité avancée
        metrics['simplicity_score'] = self._compute_simplicity_advanced(
            pattern_name, pattern_data
        )

        # 3. Métrique de robustesse avancée
        metrics['robustness_score'] = self._compute_robustness_advanced(
            pattern_name, pattern_data, training_examples
        )

        # 4. Métriques de stabilité
        stability_metrics = self._compute_stability_metrics(
            pattern_name, pattern_data, training_examples
        )
        metrics.update(stability_metrics)

        # 5. Métriques de performance
        performance_metrics = self._compute_performance_metrics(
            pattern_name, pattern_data, training_examples
        )
        metrics.update(performance_metrics)

        return metrics

    def _compute_generalization_advanced(self, pattern_name: str, pattern_data: Dict[str, Any],
                                       training_examples: Optional[List[Dict[str, Any]]] = None,
                                       validation_examples: Optional[List[Dict[str, Any]]] = None) -> float:
        """
        Calcul avancé de la généralisation
        """
        if not training_examples:
            return 0.5

        generalization_score = 0.0
        total_tests = 0

        # Test sur données de validation si disponibles
        if validation_examples:
            validation_score = self._test_on_validation_set(
                pattern_name, pattern_data, validation_examples
            )
            generalization_score += validation_score * 0.6
            total_tests += 1

        # Validation croisée sur données d'entraînement
        if len(training_examples) >= 2:
            cv_score = self._compute_cross_validation_score(
                pattern_name, pattern_data, training_examples
            )
            generalization_score += cv_score * 0.4
            total_tests += 1

        if total_tests > 0:
            generalization_score /= total_tests

        # Pénalité pour les patterns trop spécifiques
        specificity_penalty = self._compute_specificity_penalty(pattern_name, pattern_data)
        generalization_score *= (1 - specificity_penalty)

        # Bonus pour la cohérence historique
        if pattern_name in self.evaluation_history:
            historical_bonus = self._compute_historical_consistency(pattern_name, generalization_score)
            generalization_score += historical_bonus * 0.1

        return max(0, min(generalization_score, 1.0))

    def _compute_simplicity_advanced(self, pattern_name: str, pattern_data: Dict[str, Any]) -> float:
        """
        Calcul avancé de la simplicité
        """
        simplicity_score = 1.0

        # Analyse de la complexité du nom du pattern
        name_complexity = len(pattern_name.split('.')) + len(pattern_name) / 10
        simplicity_score -= name_complexity * 0.05

        # Analyse des détails du pattern
        details = pattern_data.get('details', {})
        if isinstance(details, dict):
            # Plus de détails = plus complexe (généralement)
            detail_count = len(details)
            simplicity_score -= detail_count * 0.02

            # Détails complexes indiquent un pattern complexe
            if any('complex' in str(k).lower() or 'advanced' in str(k).lower() for k in details.keys()):
                simplicity_score -= 0.1

        # Score de base du pattern
        base_score = pattern_data.get('score', 0)
        confidence = pattern_data.get('confidence', 0)

        # Un score très élevé avec confiance élevée peut indiquer sur-optimisation
        if base_score > 0.9 and confidence > 0.8:
            simplicity_score -= 0.15
        elif base_score < 0.3:
            # Score faible peut indiquer pattern trop complexe
            simplicity_score -= 0.1

        # Bonus pour les patterns fondamentaux
        fundamental_patterns = [
            'symmetry', 'repetition', 'scaling', 'translation', 'filling',
            'color_mapping', 'rotation', 'homothety', 'reflection'
        ]

        pattern_type = pattern_name.split('.')[-1]
        if pattern_type in fundamental_patterns:
            simplicity_score += 0.1

        return max(0, min(simplicity_score, 1.0))

    def _compute_robustness_advanced(self, pattern_name: str, pattern_data: Dict[str, Any],
                                   training_examples: Optional[List[Dict[str, Any]]] = None) -> float:
        """
        Calcul avancé de la robustesse
        """
        robustness_score = 0.0

        # 1. Test de résistance au bruit
        noise_resistance = self._test_noise_resistance_advanced(pattern_name, pattern_data)
        robustness_score += noise_resistance * 0.25

        # 2. Test de résistance aux variations de dimensions
        dimension_resistance = self._test_dimension_resistance_advanced(pattern_name, pattern_data)
        robustness_score += dimension_resistance * 0.25

        # 3. Test de cohérence interne
        internal_consistency = self._test_internal_consistency_advanced(pattern_data)
        robustness_score += internal_consistency * 0.3

        # 4. Test de stabilité temporelle
        temporal_stability = self._test_temporal_stability(pattern_name, pattern_data)
        robustness_score += temporal_stability * 0.2

        return max(0, min(robustness_score, 1.0))

    def _test_noise_resistance_advanced(self, pattern_name: str, pattern_data: Dict[str, Any]) -> float:
        """
        Test avancé de résistance au bruit
        """
        # Simuler différents niveaux de bruit
        noise_levels = [0.1, 0.2, 0.3]  # 10%, 20%, 30% de bruit
        resistance_scores = []

        for noise_level in noise_levels:
            # Simuler l'effet du bruit sur le score du pattern
            noise_impact = noise_level * 0.5  # Impact estimé du bruit
            noisy_score = pattern_data.get('score', 0) * (1 - noise_impact)

            # Un pattern robuste maintient un score acceptable
            if noisy_score > 0.4:
                resistance_scores.append(1.0 - noise_level)
            elif noisy_score > 0.2:
                resistance_scores.append(0.7 - noise_level)
            else:
                resistance_scores.append(0.3 - noise_level)

        if resistance_scores:
            return statistics.mean(resistance_scores)

        return 0.7  # Score par défaut pour les patterns non testés

    def _test_dimension_resistance_advanced(self, pattern_name: str, pattern_data: Dict[str, Any]) -> float:
        """
        Test de résistance aux variations de dimensions
        """
        pattern_type = pattern_name.split('.')[-1]

        # Patterns plus résistants aux variations de dimensions
        dimension_resistant_patterns = [
            'color_mapping', 'repetition', 'filling', 'symmetry'
        ]

        if pattern_type in dimension_resistant_patterns:
            return 0.9
        elif pattern_type in ['rotation', 'homothety', 'reflection']:
            return 0.7
        else:
            return 0.6

    def _test_internal_consistency_advanced(self, pattern_data: Dict[str, Any]) -> float:
        """
        Test de cohérence interne avancé
        """
        details = pattern_data.get('details', {})
        consistency_score = 0.0

        if isinstance(details, dict):
            # Vérifier la présence d'informations cohérentes
            if len(details) == 0:
                return 0.4  # Peu d'informations

            consistency_indicators = 0
            total_indicators = 0

            # Vérifier les ratios numériques
            for key, value in details.items():
                if 'ratio' in key.lower() and isinstance(value, (int, float)):
                    if 0 < value < 10:  # Ratio raisonnable
                        consistency_indicators += 1
                    total_indicators += 1

            # Vérifier les listes de valeurs
            for key, value in details.items():
                if isinstance(value, list) and len(value) > 1:
                    # Vérifier si la liste est cohérente (pas de valeurs aberrantes)
                    if len(set(value)) <= len(value) * 0.8:  # Au moins 20% de répétitions
                        consistency_indicators += 1
                    total_indicators += 1

            if total_indicators > 0:
                consistency_score = consistency_indicators / total_indicators
            else:
                consistency_score = 0.8 if len(details) > 2 else 0.6

        return consistency_score

    def _test_temporal_stability(self, pattern_name: str, pattern_data: Dict[str, Any]) -> float:
        """
        Test de stabilité temporelle (cohérence historique)
        """
        if pattern_name not in self.evaluation_history:
            return 0.8  # Score neutre pour les nouveaux patterns

        historical_scores = self.evaluation_history[pattern_name]
        if len(historical_scores) < 2:
            return 0.8

        # Calculer la variance des scores historiques
        recent_scores = [h.get('final_score', 0) for h in historical_scores[-5:]]  # Derniers 5

        if len(recent_scores) >= 2:
            variance = statistics.variance(recent_scores)
            # Plus la variance est faible, plus le pattern est stable
            stability_score = max(0, 1.0 - variance * 2)
            return stability_score

        return 0.8

    def _compute_stability_metrics(self, pattern_name: str, pattern_data: Dict[str, Any],
                                 training_examples: Optional[List[Dict[str, Any]]] = None) -> Dict[str, float]:
        """
        Calcul des métriques de stabilité
        """
        metrics = {}

        # Variance du score sur différents exemples
        if training_examples and len(training_examples) >= 3:
            scores_on_examples = []
            for example in training_examples[:5]:  # Limiter à 5 exemples
                # Simuler l'application du pattern
                simulated_score = pattern_data.get('score', 0) * (0.9 + 0.1 * (len(example.get('input', [])) % 3) / 2)
                scores_on_examples.append(simulated_score)

            if len(scores_on_examples) >= 2:
                metrics['score_variance'] = statistics.variance(scores_on_examples)
                metrics['score_consistency'] = 1.0 - min(metrics['score_variance'], 0.5)
            else:
                metrics['score_variance'] = 0
                metrics['score_consistency'] = 1.0
        else:
            metrics['score_variance'] = 0
            metrics['score_consistency'] = 0.8

        return metrics

    def _compute_performance_metrics(self, pattern_name: str, pattern_data: Dict[str, Any],
                                   training_examples: Optional[List[Dict[str, Any]]] = None) -> Dict[str, float]:
        """
        Calcul des métriques de performance
        """
        metrics = {}

        # Métrique d'efficacité (score vs complexité)
        base_score = pattern_data.get('score', 0)
        details_count = len(pattern_data.get('details', {}))
        efficiency = base_score / max(details_count, 1)
        metrics['efficiency_score'] = min(efficiency, 1.0)

        # Métrique de fiabilité (confidence vs score)
        confidence = pattern_data.get('confidence', 0)
        reliability = (base_score + confidence) / 2
        metrics['reliability_score'] = reliability

        # Métrique de potentiel d'amélioration
        current_score = pattern_data.get('score', 0)
        if pattern_name in self.evaluation_history:
            historical_max = max([h.get('final_score', 0) for h in self.evaluation_history[pattern_name]])
            improvement_potential = max(0, historical_max - current_score)
        else:
            improvement_potential = 0.3  # Potentiel par défaut

        metrics['improvement_potential'] = improvement_potential

        return metrics

    def _analyze_overfitting_risk_advanced(self, metrics: Dict[str, float],
                                         training_examples: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Analyse avancée du risque de surapprentissage
        """
        analysis = {
            'overall_risk': 0,
            'risk_factors': [],
            'confidence_intervals': {},
            'recommendations': []
        }

        risk_score = 0.0

        # Facteur 1: Écart généralisation vs performance
        generalization = metrics.get('generalization_score', 0)
        base_score = metrics.get('raw_score', metrics.get('score', 0))

        if base_score > 0.8 and generalization < 0.4:
            risk_score += 0.4
            analysis['risk_factors'].append("Écart important entre performance et généralisation")

        # Facteur 2: Simplicité trop faible
        simplicity = metrics.get('simplicity_score', 0)
        if simplicity < 0.5:
            risk_score += 0.3
            analysis['risk_factors'].append("Pattern trop complexe")

        # Facteur 3: Manque de données d'entraînement
        if training_examples and len(training_examples) < 3:
            risk_score += 0.2
            analysis['risk_factors'].append("Données d'entraînement insuffisantes")

        # Facteur 4: Variance des scores élevée
        score_variance = metrics.get('score_variance', 0)
        if score_variance > 0.3:
            risk_score += 0.2
            analysis['risk_factors'].append("Scores instables sur différents exemples")

        # Facteur 5: Potentiel d'amélioration faible
        improvement_potential = metrics.get('improvement_potential', 0)
        if improvement_potential < 0.1:
            risk_score += 0.1
            analysis['risk_factors'].append("Peu de marge d'amélioration")

        analysis['overall_risk'] = min(risk_score, 1.0)

        # Niveau de risque
        if analysis['overall_risk'] > 0.7:
            analysis['risk_level'] = 'CRITIQUE'
        elif analysis['overall_risk'] > 0.5:
            analysis['risk_level'] = 'ÉLEVÉ'
        elif analysis['overall_risk'] > 0.3:
            analysis['risk_level'] = 'MOYEN'
        else:
            analysis['risk_level'] = 'FAIBLE'

        return analysis

    def _perform_cross_validation(self, pattern_name: str, pattern_data: Dict[str, Any],
                                training_examples: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Validation croisée avancée
        """
        if len(training_examples) < self.cross_validation_folds:
            return {'status': 'insufficient_data'}

        fold_size = len(training_examples) // self.cross_validation_folds
        cv_scores = []

        for fold in range(self.cross_validation_folds):
            # Créer les sets de test et d'entraînement pour ce fold
            test_start = fold * fold_size
            test_end = test_start + fold_size

            test_set = training_examples[test_start:test_end]
            train_set = training_examples[:test_start] + training_examples[test_end:]

            # Évaluer le pattern sur le set de test
            fold_score = self._evaluate_pattern_on_test_set(
                pattern_name, pattern_data, test_set
            )
            cv_scores.append(fold_score)

        # Analyser les résultats de validation croisée
        cv_results = {
            'status': 'completed',
            'fold_scores': cv_scores,
            'mean_score': statistics.mean(cv_scores) if cv_scores else 0,
            'std_score': statistics.stdev(cv_scores) if len(cv_scores) > 1 else 0,
            'cv_confidence': self._compute_cv_confidence(cv_scores)
        }

        return cv_results

    def _evaluate_pattern_on_test_set(self, pattern_name: str, pattern_data: Dict[str, Any],
                                    test_set: List[Dict[str, Any]]) -> float:
        """
        Évaluer un pattern sur un set de test
        """
        if not test_set:
            return 0

        test_scores = []
        for example in test_set:
            # Simuler l'application du pattern
            simulated_confidence = pattern_data.get('confidence', 0) * 0.8  # Légère dégradation
            test_scores.append(simulated_confidence)

        return statistics.mean(test_scores) if test_scores else 0

    def _compute_cv_confidence(self, cv_scores: List[float]) -> float:
        """
        Calculer la confiance dans les résultats de validation croisée
        """
        if len(cv_scores) < 2:
            return 0.5

        # Plus les scores sont cohérents, plus la confiance est élevée
        mean_score = statistics.mean(cv_scores)
        std_score = statistics.stdev(cv_scores)

        if std_score == 0:
            return 1.0  # Scores parfaitement cohérents

        # Coefficient de variation
        cv = std_score / mean_score if mean_score > 0 else 0

        # Convertir en score de confiance
        confidence = max(0, 1.0 - cv)

        return confidence

    def _test_on_validation_set(self, pattern_name: str, pattern_data: Dict[str, Any],
                              validation_examples: List[Dict[str, Any]]) -> float:
        """
        Tester le pattern sur un set de validation
        """
        if not validation_examples:
            return 0

        validation_scores = []
        for example in validation_examples:
            # Simuler l'application sur données non vues
            base_confidence = pattern_data.get('confidence', 0)
            # Dégradation plus importante sur données non vues
            validation_confidence = base_confidence * 0.7
            validation_scores.append(validation_confidence)

        return statistics.mean(validation_scores) if validation_scores else 0

    def _compute_cross_validation_score(self, pattern_name: str, pattern_data: Dict[str, Any],
                                      training_examples: List[Dict[str, Any]]) -> float:
        """
        Calculer le score de validation croisée
        """
        if len(training_examples) < 2:
            return pattern_data.get('confidence', 0)

        # Simulation simple de validation croisée
        cv_scores = []
        for i in range(min(3, len(training_examples))):  # Maximum 3 folds
            fold_score = pattern_data.get('confidence', 0) * (0.9 - i * 0.1)
            cv_scores.append(fold_score)

        return statistics.mean(cv_scores) if cv_scores else 0

    def _compute_specificity_penalty(self, pattern_name: str, pattern_data: Dict[str, Any]) -> float:
        """
        Calculer la pénalité pour les patterns trop spécifiques
        """
        penalty = 0.0

        # Pénalité pour les noms trop spécifiques
        specific_terms = ['specific', 'exact', 'particular', 'unique']
        for term in specific_terms:
            if term in pattern_name.lower():
                penalty += 0.2

        # Pénalité pour les scores très élevés (peuvent indiquer sur-optimisation)
        if pattern_data.get('score', 0) > 0.95:
            penalty += 0.1

        return min(penalty, 0.5)

    def _compute_historical_consistency(self, pattern_name: str, current_score: float) -> float:
        """
        Calculer la cohérence historique
        """
        if pattern_name not in self.evaluation_history:
            return 0

        historical_scores = [h.get('final_score', 0) for h in self.evaluation_history[pattern_name][-5:]]

        if not historical_scores:
            return 0

        mean_historical = statistics.mean(historical_scores)

        # Bonus si le score actuel est cohérent avec l'historique
        consistency = 1.0 - abs(current_score - mean_historical)
        return max(0, consistency)

    def _get_timestamp(self) -> str:
        """Obtenir le timestamp actuel"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _update_evaluation_history(self, pattern_name: str, evaluation: Dict[str, Any]):
        """Mettre à jour l'historique des évaluations"""
        self.evaluation_history[pattern_name].append({
            'timestamp': evaluation['timestamp'],
            'final_score': evaluation['final_score'],
            'generalization_score': evaluation['metrics'].get('generalization_score', 0),
            'overfitting_risk': evaluation['overfitting_analysis']['overall_risk']
        })

        # Garder seulement les 10 dernières évaluations
        if len(self.evaluation_history[pattern_name]) > 10:
            self.evaluation_history[pattern_name] = self.evaluation_history[pattern_name][-10:]

    def _generate_advanced_recommendations(self, evaluation: Dict[str, Any]) -> List[str]:
        """Générer des recommandations avancées"""
        recommendations = []
        metrics = evaluation['metrics']
        overfitting = evaluation['overfitting_analysis']

        # Recommandations basées sur les métriques
        generalization = metrics.get('generalization_score', 0)
        if generalization < 0.4:
            recommendations.append("Améliorer la généralisation - collecter plus d'exemples de validation")

        simplicity = metrics.get('simplicity_score', 0)
        if simplicity < 0.5:
            recommendations.append("Simplifier le pattern - identifier les composants essentiels")

        robustness = metrics.get('robustness_score', 0)
        if robustness < 0.6:
            recommendations.append("Augmenter la robustesse - tester avec du bruit et des variations")

        # Recommandations basées sur le surapprentissage
        if overfitting['overall_risk'] > 0.5:
            recommendations.append("Réduire le risque de surapprentissage - régularisation et simplification")

        # Recommandations basées sur la validation croisée
        validation = evaluation.get('validation_results', {})
        if validation.get('status') == 'completed':
            cv_confidence = validation.get('cv_confidence', 0)
            if cv_confidence < 0.6:
                recommendations.append("Résultats de validation croisée instables - besoin de plus de données")

        # Recommandations basées sur l'historique
        pattern_name = evaluation['pattern_name']
        if pattern_name in self.evaluation_history and len(self.evaluation_history[pattern_name]) > 3:
            recent_scores = [h['final_score'] for h in self.evaluation_history[pattern_name][-3:]]
            if statistics.stdev(recent_scores) > 0.2:
                recommendations.append("Scores instables historiquement - améliorer la stabilité")

        return recommendations

    def _generate_advanced_warnings(self, evaluation: Dict[str, Any]) -> List[str]:
        """Générer des avertissements avancés"""
        warnings = []
        metrics = evaluation['metrics']
        overfitting = evaluation['overfitting_analysis']

        # Avertissements critiques
        if overfitting['overall_risk'] > 0.8:
            warnings.append("ALERTE CRITIQUE: Risque de surapprentissage très élevé")

        # Avertissements sur les métriques
        generalization = metrics.get('generalization_score', 0)
        score_consistency = metrics.get('score_consistency', 1)

        if generalization < 0.3 and score_consistency > 0.8:
            warnings.append("ATTENTION: Pattern performant mais peu généralisable")

        if metrics.get('improvement_potential', 0) < 0.05:
            warnings.append("NOTE: Pattern proche de son optimum - peu de marge d'amélioration")

        # Avertissements sur la validation
        validation = evaluation.get('validation_results', {})
        if validation.get('status') == 'insufficient_data':
            warnings.append("ATTENTION: Données insuffisantes pour validation fiable")

        return warnings

    def _generate_improvement_suggestions(self, evaluation: Dict[str, Any]) -> List[str]:
        """Générer des suggestions d'amélioration"""
        suggestions = []
        metrics = evaluation['metrics']

        # Suggestions basées sur les métriques faibles
        if metrics.get('generalization_score', 0) < 0.5:
            suggestions.append("Expérimenter avec des transformations plus génériques")

        if metrics.get('simplicity_score', 0) < 0.6:
            suggestions.append("Décomposer le pattern en composants plus simples")

        if metrics.get('robustness_score', 0) < 0.7:
            suggestions.append("Ajouter des tests de résistance aux variations")

        # Suggestions basées sur l'historique
        pattern_name = evaluation['pattern_name']
        if pattern_name in self.evaluation_history:
            historical_avg = statistics.mean([h['final_score'] for h in self.evaluation_history[pattern_name]])
            current_score = evaluation['final_score']

            if current_score < historical_avg:
                suggestions.append("Score en baisse par rapport à l'historique - analyser les causes")

        return suggestions

    def _compute_final_score_with_trends(self, evaluation: Dict[str, Any]) -> float:
        """Calculer le score final avec analyse des tendances"""
        metrics = evaluation['metrics']
        overfitting_risk = evaluation['overfitting_analysis']['overall_risk']

        # Score de base pondéré
        base_score = (
            metrics.get('generalization_score', 0) * self.generalization_weight +
            metrics.get('simplicity_score', 0) * self.simplicity_weight +
            metrics.get('robustness_score', 0) * self.robustness_weight
        )

        # Pénalité pour le surapprentissage
        penalty = overfitting_risk * 0.4

        # Ajustement basé sur les métriques de performance
        performance_bonus = metrics.get('reliability_score', 0) * 0.1

        final_score = base_score - penalty + performance_bonus

        return max(0, min(final_score, 1.0))

    def evaluate_pattern_suite_advanced(self, patterns_analysis: Dict[str, Any],
                                      training_examples: Optional[List[Dict[str, Any]]] = None,
                                      validation_examples: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Évaluation avancée d'une suite complète de patterns
        """
        evaluation = {
            'overall_quality': 0,
            'pattern_diversity': 0,
            'overfitting_risk': 0,
            'recommended_patterns': [],
            'pattern_conflicts': [],
            'quality_report': [],
            'system_recommendations': [],
            'improvement_plan': []
        }

        if not patterns_analysis:
            return evaluation

        # Évaluer chaque pattern individuellement
        scored_patterns = []
        pattern_categories = ['spatial', 'color', 'structural', 'mathematical']

        for category in pattern_categories:
            if category in patterns_analysis:
                for pattern_name, pattern_data in patterns_analysis[category].items():
                    full_pattern_name = f"{category}.{pattern_name}"
                    pattern_evaluation = self.evaluate_pattern_comprehensive_advanced(
                        full_pattern_name, pattern_data, None, None,
                        training_examples, validation_examples
                    )
                    scored_patterns.append(pattern_evaluation)

        if scored_patterns:
            # Calcul de la qualité globale
            avg_quality = statistics.mean([p['final_score'] for p in scored_patterns])
            evaluation['overall_quality'] = avg_quality

            # Diversité des patterns
            categories_used = set(p['pattern_name'].split('.')[0] for p in scored_patterns)
            evaluation['pattern_diversity'] = len(categories_used) / len(pattern_categories)

            # Risque global de surapprentissage
            avg_overfitting_risk = statistics.mean([p['overfitting_analysis']['overall_risk'] for p in scored_patterns])
            evaluation['overfitting_risk'] = avg_overfitting_risk

            # Patterns recommandés (score final > 0.6)
            recommended = [p['pattern_name'] for p in scored_patterns if p['final_score'] > 0.6]
            evaluation['recommended_patterns'] = recommended

            # Détection de conflits
            evaluation['pattern_conflicts'] = self._detect_pattern_conflicts(scored_patterns)

            # Rapport de qualité détaillé
            evaluation['quality_report'] = [
                ".2f",
                ".2f",
                ".2f",
                f"Patterns analysés: {len(scored_patterns)}",
                f"Patterns recommandés: {len(recommended)}",
                f"Conflits détectés: {len(evaluation['pattern_conflicts'])}"
            ]

            # Recommandations système
            evaluation['system_recommendations'] = self._generate_system_recommendations(evaluation)

            # Plan d'amélioration
            evaluation['improvement_plan'] = self._generate_improvement_plan(scored_patterns)

        return evaluation

    def _detect_pattern_conflicts(self, scored_patterns: List[Dict[str, Any]]) -> List[str]:
        """Détecter les conflits entre patterns"""
        conflicts = []

        # Analyser les risques de surapprentissage élevés
        high_risk_patterns = [p for p in scored_patterns if p['overfitting_analysis']['overall_risk'] > 0.6]

        if len(high_risk_patterns) > 2:
            conflicts.append(f"Multiples patterns à risque élevé: {len(high_risk_patterns)}")

        # Analyser les scores très variables
        if scored_patterns:
            scores = [p['final_score'] for p in scored_patterns]
            if len(scores) > 1 and statistics.stdev(scores) > 0.3:
                conflicts.append("Scores très variables entre patterns")

        return conflicts

    def _generate_system_recommendations(self, evaluation: Dict[str, Any]) -> List[str]:
        """Générer des recommandations pour le système complet"""
        recommendations = []

        if evaluation['overall_quality'] < 0.5:
            recommendations.append("Qualité globale faible - focus sur l'amélioration des patterns de base")

        if evaluation['pattern_diversity'] < 0.5:
            recommendations.append("Diversité des patterns insuffisante - développer d'autres catégories")

        if evaluation['overfitting_risk'] > 0.4:
            recommendations.append("Risque de surapprentissage système élevé - implémenter régularisation globale")

        if len(evaluation['recommended_patterns']) < 3:
            recommendations.append("Peu de patterns recommandés - développer des patterns plus robustes")

        return recommendations

    def _generate_improvement_plan(self, scored_patterns: List[Dict[str, Any]]) -> List[str]:
        """Générer un plan d'amélioration"""
        plan = []

        # Prioriser les améliorations
        low_quality_patterns = [p for p in scored_patterns if p['final_score'] < 0.4]
        if low_quality_patterns:
            plan.append(f"Améliorer {len(low_quality_patterns)} patterns de basse qualité")

        # Identifier les patterns à risque
        high_risk_patterns = [p for p in scored_patterns if p['overfitting_analysis']['overall_risk'] > 0.5]
        if high_risk_patterns:
            plan.append(f"Traiter {len(high_risk_patterns)} patterns à risque de surapprentissage")

        # Recommandations générales
        if len(scored_patterns) < 5:
            plan.append("Développer plus de patterns pour améliorer la couverture")

        plan.append("Implémenter métriques de monitoring continu")
        plan.append("Ajouter tests de validation croisée automatiques")

        return plan

    def generate_comprehensive_report(self, evaluation: Dict[str, Any]) -> str:
        """Générer un rapport complet de l'évaluation"""
        report = ".2f"
        report += "\n" + "=" * 80

        # Métriques principales
        metrics = evaluation['metrics']
        report += ".2f"
        report += ".2f"
        report += ".2f"
        report += ".2f"
        report += ".2f"
        report += ".2f"
        report += ".2f"

        # Analyse du surapprentissage
        overfitting = evaluation['overfitting_analysis']
        report += ".2f"
        report += f"  Niveau de risque: {overfitting['risk_level']}\n"
        if overfitting['risk_factors']:
            report += "  Facteurs de risque:\n"
            for factor in overfitting['risk_factors']:
                report += f"    • {factor}\n"

        # Résultats de validation
        validation = evaluation.get('validation_results', {})
        if validation.get('status') == 'completed':
            report += ".2f"
            report += ".2f"
            report += ".2f"
        else:
            report += f"  Statut: {validation.get('status', 'unknown')}\n"

        # Recommandations
        if evaluation['recommendations']:
            report += "\n📋 RECOMMANDATIONS:\n"
            for i, rec in enumerate(evaluation['recommendations'], 1):
                report += f"  {i}. {rec}\n"

        # Avertissements
        if evaluation['warnings']:
            report += "\n⚠️ AVERTISSEMENTS:\n"
            for warning in evaluation['warnings']:
                report += f"  • {warning}\n"

        # Suggestions d'amélioration
        if evaluation['improvement_suggestions']:
            report += "\n💡 SUGGESTIONS D'AMÉLIORATION:\n"
            for suggestion in evaluation['improvement_suggestions']:
                report += f"  • {suggestion}\n"

        return report
