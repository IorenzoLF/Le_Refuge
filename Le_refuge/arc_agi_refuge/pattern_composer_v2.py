#!/usr/bin/env python3
"""
PatternComposer v2 Amélioré - Composition intelligente avancée
Système pour combiner et orchestrer les patterns détectés avec optimisation
"""

from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
import copy
import math

class PatternComposerAmeliore:
    """
    Compositeur de patterns amélioré pour résoudre des puzzles complexes
    Version 2.1: Composition conditionnelle, optimisation hiérarchique, résolution avancée de conflits
    """

    def __init__(self):
        # Stratégies de composition principales
        self.composition_strategies = {
            'sequential': self._compose_sequential,
            'parallel': self._compose_parallel,
            'hierarchical': self._compose_hierarchical,
            'conditional': self._compose_conditional,
            'adaptive': self._compose_adaptive,
            'contextual': self._compose_contextual
        }

        # Stratégies de résolution de conflits avancées
        self.conflict_resolution_strategies = {
            'priority': self._resolve_by_priority,
            'compatibility': self._resolve_by_compatibility,
            'consensus': self._resolve_by_consensus,
            'optimization': self._resolve_by_optimization,
            'negotiation': self._resolve_by_negotiation
        }

        # Optimiseurs hiérarchiques
        self.hierarchical_optimizers = {
            'genetic': self._optimize_genetic,
            'gradient': self._optimize_gradient,
            'particle_swarm': self._optimize_particle_swarm
        }

        # Système d'apprentissage adaptatif
        self.learning_history = []
        self.success_patterns = defaultdict(int)
        self.failure_patterns = defaultdict(int)

        # Métriques de performance
        self.performance_metrics = {
            'compositions_attempted': 0,
            'compositions_successful': 0,
            'average_confidence': 0,
            'conflict_resolution_rate': 0
        }

    def compose_patterns(self, patterns_analysis: Dict[str, Any],
                        composition_strategy: str = 'adaptive',
                        optimization_level: str = 'gradient') -> Dict[str, Any]:
        """
        Compose plusieurs patterns pour former une solution complète avec optimisation avancée
        """
        self.performance_metrics['compositions_attempted'] += 1

        if not patterns_analysis or 'spatial' not in patterns_analysis:
            return {'composition': None, 'confidence': 0, 'strategy': 'none'}

        # Extraire les patterns avec haute confiance (seuil adaptatif)
        confidence_threshold = self._compute_adaptive_threshold(patterns_analysis)
        high_confidence_patterns = self._extract_high_confidence_patterns(
            patterns_analysis, confidence_threshold
        )

        if len(high_confidence_patterns) == 0:
            return {'composition': None, 'confidence': 0, 'strategy': 'no_confident_patterns'}

        if len(high_confidence_patterns) == 1:
            # Un seul pattern - pas besoin de composition
            pattern = high_confidence_patterns[0]
            result = {
                'composition': pattern,
                'confidence': pattern.get('confidence', 0),
                'strategy': 'single_pattern',
                'patterns_used': [pattern['name']],
                'optimization_applied': False
            }
            self.performance_metrics['compositions_successful'] += 1
            return result

        # Détecter et résoudre les conflits avant composition
        resolved_patterns, conflicts_detected = self._detect_and_resolve_conflicts(
            high_confidence_patterns
        )

        # Choisir la stratégie de composition optimale
        optimal_strategy = self._choose_optimal_strategy(
            resolved_patterns, composition_strategy
        )

        # Composition de plusieurs patterns avec stratégie optimale
        composition = self._compose_multiple_patterns(
            resolved_patterns, optimal_strategy
        )

        # Appliquer l'optimisation hiérarchique si demandé
        if (composition.get('composition') and
            composition['composition'] and
            optimization_level in self.hierarchical_optimizers):
            composition = self.hierarchical_optimizers[optimization_level](composition)

        # Évaluer la qualité finale de la composition
        quality_evaluation = self.evaluate_composition_quality(composition, patterns_analysis)

        # Mettre à jour les métriques
        self._update_performance_metrics(composition, quality_evaluation)

        # Apprentissage adaptatif
        self._learn_from_composition(composition, quality_evaluation)

        # Résultat final enrichi
        result = {
            'composition': composition.get('composition'),
            'confidence': composition.get('confidence', 0),
            'strategy': optimal_strategy,
            'patterns_used': [p['name'] for p in resolved_patterns],
            'optimization_applied': optimization_level,
            'conflicts_detected': conflicts_detected,
            'quality_evaluation': quality_evaluation,
            'performance_metrics': self.performance_metrics.copy()
        }

        if quality_evaluation['quality_score'] > 0.6:
            self.performance_metrics['compositions_successful'] += 1

        return result

    def _compute_adaptive_threshold(self, patterns_analysis: Dict[str, Any]) -> float:
        """
        Calcule un seuil de confiance adaptatif basé sur la distribution des patterns
        """
        all_confidences = []

        for category in ['spatial', 'color', 'structural', 'mathematical']:
            if category in patterns_analysis:
                for pattern_name, pattern_data in patterns_analysis[category].items():
                    confidence = pattern_data.get('confidence', 0)
                    if confidence > 0:
                        all_confidences.append(confidence)

        if not all_confidences:
            return 0.6  # Seuil par défaut

        # Calculer la moyenne et l'écart-type
        mean_confidence = sum(all_confidences) / len(all_confidences)
        variance = sum((c - mean_confidence) ** 2 for c in all_confidences) / len(all_confidences)
        std_confidence = math.sqrt(variance)

        # Seuil adaptatif: moyenne + 0.5 * écart-type (plus sélectif que la moyenne seule)
        adaptive_threshold = mean_confidence + 0.5 * std_confidence

        # Limiter entre 0.4 et 0.8 pour éviter les extrêmes
        return max(0.4, min(0.8, adaptive_threshold))

    def _extract_high_confidence_patterns(self, patterns_analysis: Dict[str, Any],
                                        confidence_threshold: float = 0.6) -> List[Dict[str, Any]]:
        """
        Extrait les patterns avec haute confiance (amélioré avec métadonnées)
        """
        high_confidence_patterns = []

        for category in ['spatial', 'color', 'structural', 'mathematical']:
            if category in patterns_analysis:
                for pattern_name, pattern_data in patterns_analysis[category].items():
                    confidence = pattern_data.get('confidence', 0)
                    if confidence >= confidence_threshold:
                        # Enrichir avec des métadonnées avancées
                        pattern_info = {
                            'name': f"{category}.{pattern_name}",
                            'category': category,
                            'pattern': pattern_name,
                            'confidence': confidence,
                            'score': pattern_data.get('score', 0),
                            'details': pattern_data.get('details', {}),
                            'complexity': self._estimate_pattern_complexity(pattern_data),
                            'reliability': self._estimate_pattern_reliability(pattern_data),
                            'conflicts_with': self._identify_potential_conflicts(pattern_name, category),
                            'application_cost': self._estimate_application_cost(pattern_data)
                        }
                        high_confidence_patterns.append(pattern_info)

        # Trier par score composite (confiance + fiabilité - complexité)
        high_confidence_patterns.sort(
            key=lambda p: p['confidence'] * 0.4 + p['reliability'] * 0.4 - p['complexity'] * 0.2,
            reverse=True
        )

        return high_confidence_patterns

    def _estimate_pattern_complexity(self, pattern_data: Dict[str, Any]) -> float:
        """Estime la complexité d'un pattern (0-1, plus élevé = plus complexe)"""
        complexity = 0.3  # Base

        # Plus de détails = plus complexe
        details = pattern_data.get('details', {})
        if isinstance(details, dict):
            complexity += min(len(details) * 0.1, 0.4)

        # Certains types de patterns sont intrinsèquement plus complexes
        pattern_name = pattern_data.get('pattern', '')
        if any(keyword in pattern_name for keyword in ['fractal', 'recursive', 'complex']):
            complexity += 0.2

        return min(complexity, 1.0)

    def _estimate_pattern_reliability(self, pattern_data: Dict[str, Any]) -> float:
        """Estime la fiabilité d'un pattern basée sur les données disponibles"""
        reliability = 0.5  # Base

        # Plus de données de validation = plus fiable
        details = pattern_data.get('details', {})
        if isinstance(details, dict):
            if 'validation_count' in details:
                reliability += min(details['validation_count'] * 0.1, 0.3)

        # Patterns avec des scores élevés sont plus fiables
        score = pattern_data.get('score', 0)
        reliability += score * 0.2

        return min(reliability, 1.0)

    def _identify_potential_conflicts(self, pattern_name: str, category: str) -> List[str]:
        """Identifie les patterns potentiellement en conflit"""
        conflict_matrix = {
            'spatial.symmetry': ['spatial.translation', 'spatial.filling', 'spatial.repetition'],
            'spatial.repetition': ['spatial.translation', 'spatial.expansion'],
            'spatial.translation': ['spatial.filling', 'spatial.projection'],
            'color.cycling': ['color.gradient', 'color.filtering'],
            'structural.projection': ['structural.folding', 'structural.expansion']
        }

        pattern_key = f"{category}.{pattern_name}"
        return conflict_matrix.get(pattern_key, [])

    def _estimate_application_cost(self, pattern_data: Dict[str, Any]) -> float:
        """Estime le coût computationnel d'application du pattern"""
        base_cost = 0.2

        # Patterns complexes coûtent plus cher
        pattern_name = pattern_data.get('pattern', '')
        if any(keyword in pattern_name for keyword in ['fractal', 'recursive', 'optimization']):
            base_cost += 0.3

        # Plus de détails = coût plus élevé
        details = pattern_data.get('details', {})
        if isinstance(details, dict):
            base_cost += min(len(details) * 0.05, 0.2)

        return min(base_cost, 1.0)

    def _detect_and_resolve_conflicts(self, patterns: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int]:
        """
        Détecte et résout les conflits entre patterns
        Retourne: (patterns_résolus, nombre_conflits_détectés)
        """
        if len(patterns) <= 1:
            return patterns, 0

        conflicts_detected = 0
        resolved_patterns = patterns.copy()

        # Détecter les conflits
        conflicts = []
        for i, pattern1 in enumerate(patterns):
            for j, pattern2 in enumerate(patterns[i+1:], i+1):
                if self._are_patterns_conflicting(pattern1, pattern2):
                    conflicts.append((i, j, pattern1, pattern2))
                    conflicts_detected += 1

        if conflicts:
            # Résoudre les conflits avec la stratégie optimale
            resolved_patterns = self._resolve_conflicts_advanced(patterns, conflicts)

        return resolved_patterns, conflicts_detected

    def _are_patterns_conflicting(self, pattern1: Dict[str, Any], pattern2: Dict[str, Any]) -> bool:
        """
        Vérifie si deux patterns sont en conflit (version avancée)
        """
        # Conflits par matrice de conflits
        pattern1_key = f"{pattern1['category']}.{pattern1['pattern']}"
        pattern2_key = f"{pattern2['category']}.{pattern2['pattern']}"

        conflict_matrix = {
            'spatial.symmetry': ['spatial.translation', 'spatial.filling', 'spatial.repetition'],
            'spatial.repetition': ['spatial.translation', 'spatial.expansion'],
            'spatial.translation': ['spatial.filling', 'spatial.projection'],
            'color.cycling': ['color.gradient', 'color.filtering'],
            'structural.projection': ['structural.folding', 'structural.expansion']
        }

        # Vérifier les deux directions
        if pattern2_key in conflict_matrix.get(pattern1_key, []):
            return True
        if pattern1_key in conflict_matrix.get(pattern2_key, []):
            return True

        # Conflits par similarité trop élevée (patterns redondants)
        if (pattern1['category'] == pattern2['category'] and
            pattern1['pattern'] == pattern2['pattern'] and
            abs(pattern1['confidence'] - pattern2['confidence']) < 0.2):
            return True

        # Conflits par coût d'application trop élevé
        total_cost = pattern1['application_cost'] + pattern2['application_cost']
        if total_cost > 1.2:  # Coût combiné trop élevé
            return True

        return False

    def _resolve_conflicts_advanced(self, patterns: List[Dict[str, Any]],
                                   conflicts: List[Tuple]) -> List[Dict[str, Any]]:
        """
        Résout les conflits avec une stratégie avancée
        """
        if not conflicts:
            return patterns

        # Score de chaque pattern (confiance - complexité - coût)
        pattern_scores = {}
        for i, pattern in enumerate(patterns):
            score = (pattern['confidence'] * 0.5 +
                    pattern['reliability'] * 0.3 -
                    pattern['complexity'] * 0.1 -
                    pattern['application_cost'] * 0.1)
            pattern_scores[i] = score

        # Garder les patterns avec les meilleurs scores
        resolved_patterns = []
        used_indices = set()

        for conflict in conflicts:
            idx1, idx2 = conflict[0], conflict[1]

            # Si les deux indices n'ont pas encore été traités
            if idx1 not in used_indices and idx2 not in used_indices:
                score1 = pattern_scores[idx1]
                score2 = pattern_scores[idx2]

                if score1 > score2:
                    resolved_patterns.append(patterns[idx1])
                    used_indices.add(idx1)
                else:
                    resolved_patterns.append(patterns[idx2])
                    used_indices.add(idx2)

        # Ajouter les patterns non conflictuels
        for i, pattern in enumerate(patterns):
            if i not in used_indices:
                resolved_patterns.append(pattern)

        return resolved_patterns

    def _choose_optimal_strategy(self, patterns: List[Dict[str, Any]],
                                requested_strategy: str = 'adaptive') -> str:
        """
        Choisit la stratégie de composition optimale basée sur les patterns
        """
        if requested_strategy != 'adaptive':
            return requested_strategy

        # Analyse des patterns pour choisir la stratégie optimale
        categories = set(p['category'] for p in patterns)
        avg_confidence = sum(p['confidence'] for p in patterns) / len(patterns)
        max_complexity = max(p['complexity'] for p in patterns)

        # Règles de décision pour les stratégies
        if len(categories) == 1:
            # Tous les patterns de même catégorie
            if avg_confidence > 0.8:
                return 'parallel'  # Patterns très confiants, composition parallèle
            else:
                return 'sequential'  # Patterns moins confiants, composition séquentielle

        elif max_complexity > 0.7:
            return 'hierarchical'  # Patterns complexes, composition hiérarchique

        elif len(patterns) > 4:
            return 'contextual'  # Beaucoup de patterns, composition contextuelle

        else:
            return 'conditional'  # Cas général, composition conditionnelle

    def _compose_multiple_patterns(self, patterns: List[Dict[str, Any]],
                                 strategy: str = 'hierarchical') -> Dict[str, Any]:
        """
        Compose plusieurs patterns selon la stratégie choisie
        """
        if strategy in self.composition_strategies:
            return self.composition_strategies[strategy](patterns)
        else:
            return self._compose_hierarchical(patterns)  # Stratégie par défaut

    def _compose_sequential(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Composition séquentielle: appliquer les patterns dans l'ordre
        """
        if not patterns:
            return {'composition': None, 'confidence': 0}

        # Trier par priorité (couleur d'abord, puis spatial, puis structural)
        priority_order = {'color': 3, 'spatial': 2, 'structural': 1}
        sorted_patterns = sorted(patterns,
                               key=lambda p: priority_order.get(p['category'], 0),
                               reverse=True)

        composition = {
            'type': 'sequential',
            'patterns': sorted_patterns,
            'order': [p['name'] for p in sorted_patterns],
            'confidence': sum(p['confidence'] for p in sorted_patterns) / len(sorted_patterns)
        }

        return composition

    def _compose_parallel(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Composition parallèle: appliquer tous les patterns simultanément
        """
        if not patterns:
            return {'composition': None, 'confidence': 0}

        # Vérifier la compatibilité des patterns
        compatible_patterns = self._filter_compatible_patterns(patterns)

        composition = {
            'type': 'parallel',
            'patterns': compatible_patterns,
            'compatible_count': len(compatible_patterns),
            'total_count': len(patterns),
            'confidence': sum(p['confidence'] for p in compatible_patterns) / len(compatible_patterns) if compatible_patterns else 0
        }

        return composition

    def _compose_hierarchical(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Composition hiérarchique: patterns organisés par niveau d'importance
        """
        if not patterns:
            return {'composition': None, 'confidence': 0}

        # Organisation hiérarchique
        primary_patterns = []
        secondary_patterns = []

        for pattern in patterns:
            if pattern['confidence'] > 0.8:
                primary_patterns.append(pattern)
            else:
                secondary_patterns.append(pattern)

        composition = {
            'type': 'hierarchical',
            'primary': primary_patterns,
            'secondary': secondary_patterns,
            'hierarchy_score': len(primary_patterns) / len(patterns),
            'confidence': (sum(p['confidence'] for p in primary_patterns) * 0.7 +
                          sum(p['confidence'] for p in secondary_patterns) * 0.3) / len(patterns)
        }

        return composition

    def _compose_conditional(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Composition conditionnelle: patterns appliqués selon des conditions dynamiques
        """
        if not patterns:
            return {'composition': None, 'confidence': 0}

        # Créer des conditions avancées basées sur l'analyse contextuelle
        conditions = []
        context_analysis = self._analyze_composition_context(patterns)

        for i, pattern in enumerate(patterns):
            # Conditions basées sur le contexte global
            dynamic_conditions = self._extract_dynamic_conditions(pattern, context_analysis, i)

            if dynamic_conditions:
                conditions.append({
                    'pattern': pattern,
                    'conditions': dynamic_conditions,
                    'priority': self._calculate_condition_priority(pattern, dynamic_conditions)
                })

        composition = {
            'type': 'conditional',
            'conditions': conditions,
            'context_analysis': context_analysis,
            'conditional_count': len(conditions),
            'confidence': self._calculate_conditional_confidence(patterns, conditions),
            'execution_plan': self._create_execution_plan(conditions)
        }

        return composition

    def _compose_adaptive(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Composition adaptative: ajuste dynamiquement la stratégie basée sur les résultats
        """
        if not patterns:
            return {'composition': None, 'confidence': 0}

        # Analyser les succès passés pour adapter la stratégie
        historical_success = self._analyze_historical_success(patterns)

        # Choisir la sous-stratégie optimale basée sur l'historique
        if historical_success.get('parallel_success', 0) > 0.7:
            base_strategy = 'parallel'
        elif historical_success.get('hierarchical_success', 0) > 0.7:
            base_strategy = 'hierarchical'
        else:
            base_strategy = 'sequential'

        # Appliquer la stratégie de base avec adaptation
        base_composition = self.composition_strategies[base_strategy](patterns)

        # Adapter la composition basée sur les métriques de performance
        adapted_composition = self._adapt_composition(base_composition, patterns)

        composition = {
            'type': 'adaptive',
            'base_strategy': base_strategy,
            'adapted_from': base_composition,
            'historical_success': historical_success,
            'adaptations_applied': adapted_composition['adaptations'],
            'confidence': adapted_composition['confidence'],
            'learning_rate': 0.1  # Taux d'apprentissage pour les futures adaptations
        }

        return composition

    def _compose_contextual(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Composition contextuelle: prend en compte le contexte global des patterns
        """
        if not patterns:
            return {'composition': None, 'confidence': 0}

        # Analyser le contexte global
        global_context = self._analyze_global_context(patterns)

        # Grouper les patterns par contexte
        contextual_groups = self._group_patterns_by_context(patterns, global_context)

        # Créer des sous-compositions pour chaque groupe contextuel
        sub_compositions = []
        for group_context, group_patterns in contextual_groups.items():
            if len(group_patterns) == 1:
                sub_compositions.append(group_patterns[0])
            else:
                # Choisir la meilleure stratégie pour ce groupe
                best_strategy = self._choose_contextual_strategy(group_patterns, group_context)
                sub_composition = self.composition_strategies[best_strategy](group_patterns)
                sub_compositions.append(sub_composition)

        composition = {
            'type': 'contextual',
            'global_context': global_context,
            'contextual_groups': contextual_groups,
            'sub_compositions': sub_compositions,
            'contextual_confidence': self._calculate_contextual_confidence(sub_compositions),
            'confidence': sum(sub['confidence'] for sub in sub_compositions) / len(sub_compositions)
        }

        return composition

    # === MÉTHODES D'ANALYSE CONTEXTUELLE ===

    def _analyze_composition_context(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyse le contexte de composition pour les patterns"""
        categories = [p['category'] for p in patterns]
        confidences = [p['confidence'] for p in patterns]
        complexities = [p['complexity'] for p in patterns]

        return {
            'dominant_category': max(set(categories), key=categories.count),
            'avg_confidence': sum(confidences) / len(confidences),
            'max_complexity': max(complexities),
            'category_diversity': len(set(categories)),
            'confidence_variance': sum((c - sum(confidences)/len(confidences))**2 for c in confidences) / len(confidences)
        }

    def _extract_dynamic_conditions(self, pattern: Dict[str, Any],
                                  context: Dict[str, Any], position: int) -> List[str]:
        """Extrait des conditions dynamiques pour un pattern"""
        conditions = []

        # Conditions basées sur la position
        if position == 0:
            conditions.append("first_pattern")
        if position == len(context) - 1:
            conditions.append("last_pattern")

        # Conditions basées sur la catégorie dominante
        if pattern['category'] == context['dominant_category']:
            conditions.append("dominant_category")

        # Conditions basées sur la confiance
        if pattern['confidence'] > context['avg_confidence'] + 0.1:
            conditions.append("high_confidence")
        elif pattern['confidence'] < context['avg_confidence'] - 0.1:
            conditions.append("low_confidence")

        # Conditions basées sur la complexité
        if pattern['complexity'] > 0.7:
            conditions.append("high_complexity")

        return conditions

    def _calculate_condition_priority(self, pattern: Dict[str, Any], conditions: List[str]) -> float:
        """Calcule la priorité d'un pattern basé sur ses conditions"""
        priority = 0.5  # Base

        priority_multipliers = {
            'first_pattern': 1.2,
            'last_pattern': 1.1,
            'dominant_category': 1.3,
            'high_confidence': 1.4,
            'high_complexity': 0.8  # Patterns complexes ont moins de priorité
        }

        for condition in conditions:
            if condition in priority_multipliers:
                priority *= priority_multipliers[condition]

        return min(priority, 2.0)

    def _calculate_conditional_confidence(self, patterns: List[Dict[str, Any]],
                                        conditions_list: List[Dict[str, Any]]) -> float:
        """Calcule la confiance pour une composition conditionnelle"""
        if not conditions_list:
            return 0

        base_confidence = sum(p['confidence'] for p in patterns) / len(patterns)
        condition_bonus = len(conditions_list) * 0.05  # Bonus pour chaque condition
        priority_bonus = sum(c.get('priority', 1.0) for c in conditions_list) / len(conditions_list) * 0.1

        return min(base_confidence + condition_bonus + priority_bonus, 1.0)

    def _create_execution_plan(self, conditions_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Crée un plan d'exécution basé sur les conditions"""
        # Trier par priorité
        sorted_conditions = sorted(conditions_list,
                                 key=lambda c: c.get('priority', 1.0),
                                 reverse=True)

        execution_plan = []
        for i, condition in enumerate(sorted_conditions):
            execution_plan.append({
                'step': i + 1,
                'pattern': condition['pattern']['name'],
                'conditions': condition['conditions'],
                'priority': condition.get('priority', 1.0)
            })

        return execution_plan

    # === MÉTHODES POUR COMPOSITION ADAPTATIVE ===

    def _analyze_historical_success(self, patterns: List[Dict[str, Any]]) -> Dict[str, float]:
        """Analyse les succès historiques pour l'adaptation"""
        # Simulation basée sur les patterns de succès passés
        success_rates = {}

        for pattern in patterns:
            pattern_key = f"{pattern['category']}.{pattern['pattern']}"
            success_rate = self.success_patterns.get(pattern_key, 0) / max(
                self.success_patterns.get(pattern_key, 0) + self.failure_patterns.get(pattern_key, 0), 1
            )
            success_rates[pattern_key] = success_rate

        # Calculer les taux de succès par stratégie
        parallel_success = sum(1 for rate in success_rates.values() if rate > 0.7) / len(success_rates)
        hierarchical_success = sum(1 for rate in success_rates.values() if rate > 0.5) / len(success_rates)

        return {
            'parallel_success': parallel_success,
            'hierarchical_success': hierarchical_success,
            'overall_success': sum(success_rates.values()) / len(success_rates)
        }

    def _adapt_composition(self, base_composition: Dict[str, Any],
                          patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Adapte une composition basée sur les métriques de performance"""
        adaptations = []

        # Adaptation 1: Ajustement de la confiance
        if base_composition.get('confidence', 0) < 0.6:
            adaptations.append("confidence_boost")
            new_confidence = min(base_composition['confidence'] * 1.2, 0.8)
        else:
            new_confidence = base_composition['confidence']

        # Adaptation 2: Simplification si trop complexe
        if len(patterns) > 5:
            adaptations.append("complexity_reduction")
            # Réduire le nombre de patterns à ceux avec la plus haute confiance
            sorted_patterns = sorted(patterns, key=lambda p: p['confidence'], reverse=True)
            simplified_patterns = sorted_patterns[:3]
        else:
            simplified_patterns = patterns

        return {
            'adaptations': adaptations,
            'confidence': new_confidence,
            'simplified_patterns': simplified_patterns
        }

    # === MÉTHODES POUR COMPOSITION CONTEXTUELLE ===

    def _analyze_global_context(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyse le contexte global des patterns"""
        categories = [p['category'] for p in patterns]
        category_counts = {}
        for cat in categories:
            category_counts[cat] = category_counts.get(cat, 0) + 1

        return {
            'total_patterns': len(patterns),
            'category_distribution': category_counts,
            'dominant_category': max(category_counts.items(), key=lambda x: x[1])[0],
            'category_balance': len(category_counts) / len(patterns),  # Plus proche de 1 = plus équilibré
            'avg_confidence': sum(p['confidence'] for p in patterns) / len(patterns)
        }

    def _group_patterns_by_context(self, patterns: List[Dict[str, Any]],
                                 global_context: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
        """Groupe les patterns par contexte"""
        groups = defaultdict(list)

        for pattern in patterns:
            # Déterminer le contexte du pattern
            if pattern['category'] == global_context['dominant_category']:
                context_key = "dominant"
            elif pattern['confidence'] > global_context['avg_confidence']:
                context_key = "high_confidence"
            elif pattern['complexity'] > 0.5:
                context_key = "complex"
            else:
                context_key = "standard"

            groups[context_key].append(pattern)

        return dict(groups)

    def _choose_contextual_strategy(self, patterns: List[Dict[str, Any]],
                                  context: str) -> str:
        """Choisit la stratégie optimale pour un contexte donné"""
        strategy_map = {
            'dominant': 'parallel',      # Patterns dominants peuvent être parallélisés
            'high_confidence': 'parallel', # Patterns très confiants aussi
            'complex': 'hierarchical',   # Patterns complexes nécessitent hiérarchie
            'standard': 'sequential'     # Cas standard
        }

        return strategy_map.get(context, 'sequential')

    def _calculate_contextual_confidence(self, sub_compositions: List[Dict[str, Any]]) -> float:
        """Calcule la confiance contextuelle"""
        if not sub_compositions:
            return 0

        confidences = []
        for comp in sub_compositions:
            if isinstance(comp, dict):
                confidence = comp.get('confidence', 0)
            else:
                confidence = comp.get('confidence', 0)
            confidences.append(confidence)

        return sum(confidences) / len(confidences)

    # === OPTIMISEURS HIÉRARCHIQUES ===

    def _optimize_genetic(self, composition: Dict[str, Any]) -> Dict[str, Any]:
        """Optimisation génétique de la composition"""
        # Simulation d'algorithme génétique
        optimized = copy.deepcopy(composition)

        # Phase 1: Sélection des meilleurs patterns
        if 'patterns' in composition.get('composition', {}):
            patterns = composition['composition']['patterns']
            # Garder seulement les patterns avec confiance > moyenne
            avg_confidence = sum(p['confidence'] for p in patterns) / len(patterns)
            selected_patterns = [p for p in patterns if p['confidence'] >= avg_confidence]
            optimized['composition']['patterns'] = selected_patterns

        # Phase 2: Mutation (ajustement des poids)
        if 'confidence' in optimized:
            optimized['confidence'] = min(optimized['confidence'] * 1.1, 1.0)

        optimized['optimization_applied'] = 'genetic'
        return optimized

    def _optimize_gradient(self, composition: Dict[str, Any]) -> Dict[str, Any]:
        """Optimisation par gradient de la composition"""
        optimized = copy.deepcopy(composition)

        # Calcul du gradient de confiance
        current_confidence = composition.get('confidence', 0)
        target_confidence = 0.8

        # Ajustement graduel vers la cible
        if current_confidence < target_confidence:
            gradient = (target_confidence - current_confidence) * 0.1
            optimized['confidence'] = min(current_confidence + gradient, target_confidence)

        optimized['optimization_applied'] = 'gradient'
        return optimized

    def _optimize_particle_swarm(self, composition: Dict[str, Any]) -> Dict[str, Any]:
        """Optimisation par essaim particulaire"""
        optimized = copy.deepcopy(composition)

        # Simulation d'optimisation par essaim
        if 'composition' in composition and composition['composition']:
            comp_info = composition['composition']

            # Améliorer la distribution des patterns
            if 'patterns' in comp_info:
                patterns = comp_info['patterns']
                # Trier par score composite et réorganiser
                for pattern in patterns:
                    composite_score = (pattern['confidence'] * 0.4 +
                                     pattern['reliability'] * 0.4 -
                                     pattern['complexity'] * 0.2)
                    pattern['particle_score'] = composite_score

                patterns.sort(key=lambda p: p.get('particle_score', 0), reverse=True)
                comp_info['patterns'] = patterns

        optimized['optimization_applied'] = 'particle_swarm'
        return optimized

    def _are_patterns_compatible(self, pattern1: Dict[str, Any],
                                pattern2: Dict[str, Any]) -> bool:
        """
        Vérifie si deux patterns sont compatibles
        """
        # Règles de compatibilité simples
        category1, category2 = pattern1['category'], pattern2['category']

        # Patterns de même catégorie peuvent être incompatibles
        if category1 == category2:
            # Ex: deux patterns spatiaux différents peuvent être incompatibles
            if category1 == 'spatial':
                spatial_conflicts = {
                    'symmetry': ['translation', 'filling'],  # Symétrie et translation peuvent être incompatibles
                    'repetition': ['translation'],  # Répétition et translation peuvent être incompatibles
                }

                pattern1_name = pattern1['pattern']
                pattern2_name = pattern2['pattern']

                if (pattern1_name in spatial_conflicts and
                    pattern2_name in spatial_conflicts[pattern1_name]):
                    return False

        # Patterns de couleur sont généralement compatibles avec tout
        if category1 == 'color' or category2 == 'color':
            return True

        return True  # Par défaut, considérer comme compatible

    # === MÉTHODES DE GESTION DES MÉTRIQUES ===

    def _update_performance_metrics(self, composition: Dict[str, Any],
                                  quality_evaluation: Dict[str, Any]):
        """Met à jour les métriques de performance"""
        if quality_evaluation['quality_score'] > 0.6:
            self.performance_metrics['compositions_successful'] += 1

        # Mettre à jour la confiance moyenne
        total_compositions = self.performance_metrics['compositions_attempted']
        current_avg = self.performance_metrics['average_confidence']
        new_confidence = composition.get('confidence', 0)

        self.performance_metrics['average_confidence'] = (
            (current_avg * (total_compositions - 1)) + new_confidence
        ) / total_compositions

    def _learn_from_composition(self, composition: Dict[str, Any],
                              quality_evaluation: Dict[str, Any]):
        """Apprentissage adaptatif basé sur les résultats de composition"""
        success = quality_evaluation['quality_score'] > 0.6
        patterns_used = composition.get('patterns_used', [])

        for pattern_name in patterns_used:
            if success:
                self.success_patterns[pattern_name] += 1
            else:
                self.failure_patterns[pattern_name] += 1

        # Enregistrer dans l'historique
        self.learning_history.append({
            'timestamp': len(self.learning_history),
            'success': success,
            'patterns': patterns_used,
            'strategy': composition.get('strategy', 'unknown'),
            'quality_score': quality_evaluation['quality_score'],
            'confidence': composition.get('confidence', 0)
        })

        # Garder seulement les 100 dernières entrées
        if len(self.learning_history) > 100:
            self.learning_history = self.learning_history[-100:]

    # === ÉVALUATION DE QUALITÉ AMÉLIORÉE ===

    def evaluate_composition_quality(self, composition: Dict[str, Any],
                                   original_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Évalue la qualité d'une composition avec métriques avancées"""
        if not composition or 'composition' not in composition:
            return {'quality_score': 0, 'improvement': 0}

        composition_info = composition['composition']
        if not composition_info:
            return {'quality_score': 0, 'improvement': 0}

        # Score de base
        base_confidence = composition.get('confidence', 0)

        # Bonus pour les compositions complexes réussies
        complexity_bonus = 0
        if composition_info.get('type') == 'hierarchical':
            primary_count = len(composition_info.get('primary', []))
            complexity_bonus = min(primary_count * 0.05, 0.15)

        # Pénalité pour les conflits
        conflict_penalty = 0
        if 'conflicts_detected' in composition and composition['conflicts_detected'] > 0:
            conflict_penalty = composition['conflicts_detected'] * 0.1

        quality_score = base_confidence + complexity_bonus - conflict_penalty
        quality_score = max(0, min(quality_score, 1.0))

        # Calcul de l'amélioration
        original_score = original_analysis.get('overall_score', 0)
        improvement = quality_score - original_score

        return {
            'quality_score': quality_score,
            'improvement': improvement,
            'complexity_bonus': complexity_bonus,
            'conflict_penalty': conflict_penalty
        }

    def _resolve_by_optimization(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Résolution par optimisation multi-objectif
        """
        if not patterns:
            return {'strategy': 'optimization', 'selected': [], 'rejected': [], 'confidence': 0}

        # Optimisation multi-objectif: maximiser confiance, minimiser complexité et conflits
        scored_patterns = []
        for pattern in patterns:
            # Score composite: confiance - complexité - (coût d'application * 0.5)
            composite_score = (
                pattern['confidence'] * 0.5 -
                pattern['complexity'] * 0.3 -
                pattern['application_cost'] * 0.2
            )
            scored_patterns.append((pattern, composite_score))

        # Trier par score composite
        scored_patterns.sort(key=lambda x: x[1], reverse=True)

        # Sélectionner les meilleurs patterns sans conflits
        selected = []
        rejected = []
        used_categories = set()

        for pattern, score in scored_patterns:
            pattern_category = pattern['category']

            # Vérifier les conflits de catégorie
            if pattern_category not in used_categories or pattern_category == 'color':
                selected.append(pattern)
                if pattern_category != 'color':  # Les couleurs peuvent être multiples
                    used_categories.add(pattern_category)
            else:
                rejected.append(pattern)

        avg_confidence = sum(p['confidence'] for p in selected) / len(selected) if selected else 0

        return {
            'strategy': 'optimization',
            'selected': selected,
            'rejected': rejected,
            'confidence': avg_confidence,
            'optimization_score': sum(score for _, score in scored_patterns[:len(selected)])
        }

    def _resolve_by_negotiation(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Résolution par négociation (patterns négocient leur inclusion)
        """
        if not patterns:
            return {'strategy': 'negotiation', 'selected': [], 'rejected': [], 'confidence': 0}

        # Simulation de négociation basée sur les scores
        negotiations = []

        for i, pattern1 in enumerate(patterns):
            for j, pattern2 in enumerate(patterns[i+1:], i+1):
                # Calcul du "coût de conflit"
                conflict_cost = (
                    (pattern1['application_cost'] + pattern2['application_cost']) * 0.5 +
                    abs(pattern1['confidence'] - pattern2['confidence']) * 0.3
                )

                negotiations.append({
                    'pattern1': pattern1,
                    'pattern2': pattern2,
                    'conflict_cost': conflict_cost,
                    'resolution': 'compromise' if conflict_cost < 0.5 else 'exclusion'
                })

        # Appliquer les résolutions
        selected = []
        excluded_patterns = set()

        for negotiation in negotiations:
            if negotiation['resolution'] == 'compromise':
                # Les deux patterns peuvent coexister avec un compromis
                if negotiation['pattern1'] not in excluded_patterns:
                    selected.append(negotiation['pattern1'])
                if negotiation['pattern2'] not in excluded_patterns:
                    selected.append(negotiation['pattern2'])
            else:
                # Exclure le pattern avec le score le plus bas
                if negotiation['pattern1']['confidence'] > negotiation['pattern2']['confidence']:
                    excluded_patterns.add(negotiation['pattern2']['name'])
                    if negotiation['pattern1'] not in excluded_patterns:
                        selected.append(negotiation['pattern1'])
                else:
                    excluded_patterns.add(negotiation['pattern1']['name'])
                    if negotiation['pattern2'] not in excluded_patterns:
                        selected.append(negotiation['pattern2'])

        # Ajouter les patterns non impliqués dans des négociations
        for pattern in patterns:
            if pattern not in selected and pattern['name'] not in excluded_patterns:
                selected.append(pattern)

        rejected = [p for p in patterns if p['name'] in excluded_patterns]

        avg_confidence = sum(p['confidence'] for p in selected) / len(selected) if selected else 0

        return {
            'strategy': 'negotiation',
            'selected': selected,
            'rejected': rejected,
            'confidence': avg_confidence,
            'negotiations_count': len(negotiations)
        }

    def resolve_conflicts(self, conflicting_patterns: List[Dict[str, Any]],
                         strategy: str = 'priority') -> Dict[str, Any]:
        """
        Résout les conflits entre patterns incompatibles
        """
        if strategy in self.conflict_resolution_strategies:
            return self.conflict_resolution_strategies[strategy](conflicting_patterns)
        else:
            return self._resolve_by_priority(conflicting_patterns)

    def _resolve_by_priority(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Résolution par priorité (couleur > spatial > structural)
        """
        priority_order = {'color': 3, 'spatial': 2, 'structural': 1}

        sorted_patterns = sorted(patterns,
                               key=lambda p: priority_order.get(p['category'], 0),
                               reverse=True)

        return {
            'strategy': 'priority',
            'selected': sorted_patterns[:2],  # Garder les 2 plus prioritaires
            'rejected': sorted_patterns[2:],
            'confidence': sum(p['confidence'] for p in sorted_patterns[:2]) / 2
        }

    def _resolve_by_compatibility(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Résolution par compatibilité maximale
        """
        # Version simplifiée: sélectionner les patterns les plus confiants
        sorted_by_confidence = sorted(patterns,
                                    key=lambda p: p['confidence'],
                                    reverse=True)

        return {
            'strategy': 'compatibility',
            'selected': sorted_by_confidence[:2],
            'rejected': sorted_by_confidence[2:],
            'confidence': sum(p['confidence'] for p in sorted_by_confidence[:2]) / 2
        }

    def _resolve_by_consensus(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Résolution par consensus (moyenne pondérée)
        """
        if not patterns:
            return {'strategy': 'consensus', 'selected': [], 'rejected': [], 'confidence': 0}

        # Calcul d'un consensus
        avg_confidence = sum(p['confidence'] for p in patterns) / len(patterns)

        # Sélectionner les patterns au-dessus de la moyenne
        selected = [p for p in patterns if p['confidence'] >= avg_confidence]

        return {
            'strategy': 'consensus',
            'selected': selected,
            'rejected': [p for p in patterns if p['confidence'] < avg_confidence],
            'confidence': avg_confidence
        }

    def _extract_pattern_condition(self, pattern: Dict[str, Any]) -> Optional[str]:
        """
        Extrait une condition d'application du pattern
        """
        details = pattern.get('details', {})

        if isinstance(details, dict):
            # Exemples de conditions basées sur les détails
            if 'symmetries_found' in details:
                symmetries = details['symmetries_found']
                if symmetries.get('horizontal') or symmetries.get('vertical'):
                    return "grid_symmetric"

            if 'repetitions_found' in details:
                repetitions = details['repetitions_found']
                if repetitions.get('horizontal') or repetitions.get('vertical'):
                    return "pattern_repetitive"

            if 'scaling_type' in details:
                scaling_type = details['scaling_type']
                if scaling_type == 'expansion':
                    return "grid_expanding"

        return None

    def apply_composition(self, composition: Dict[str, Any],
                         input_grid: List[List[int]]) -> List[List[int]]:
        """
        Applique une composition de patterns à une grille d'entrée
        """
        if not composition or 'composition' not in composition:
            return input_grid

        composition_info = composition['composition']
        if not composition_info:
            return input_grid

        # Version simplifiée d'application
        # Dans une vraie implémentation, on appliquerait réellement les patterns

        output_grid = copy.deepcopy(input_grid)

        # Simulation d'application basée sur le type de composition
        composition_type = composition_info.get('type', 'unknown')

        if composition_type == 'hierarchical':
            # Appliquer les patterns primaires en priorité
            primary_patterns = composition_info.get('primary', [])
            for pattern in primary_patterns:
                output_grid = self._apply_single_pattern(pattern, output_grid)

        elif composition_type == 'sequential':
            # Appliquer les patterns dans l'ordre
            patterns = composition_info.get('patterns', [])
            for pattern in patterns:
                output_grid = self._apply_single_pattern(pattern, output_grid)

        return output_grid

    def _apply_single_pattern(self, pattern: Dict[str, Any],
                            input_grid: List[List[int]]) -> List[List[int]]:
        """
        Applique un pattern individuel (version simplifiée)
        """
        # Version de démonstration - dans la vraie implémentation,
        # on utiliserait les vrais algorithmes de chaque pattern

        pattern_name = pattern.get('pattern', '')
        output_grid = copy.deepcopy(input_grid)

        # Simulation simple selon le type de pattern
        if 'symmetry' in pattern_name:
            # Ajouter une symétrie simple
            if len(output_grid) > 0:
                output_grid[0][0] = output_grid[-1][-1]  # Symétrie diagonale basique

        elif 'repetition' in pattern_name:
            # Répéter le premier élément
            if len(output_grid) > 0 and len(output_grid[0]) > 1:
                output_grid[0][1] = output_grid[0][0]

        elif 'scaling' in pattern_name:
            # Doubler la taille (simulation)
            if len(output_grid) > 0:
                output_grid.append(output_grid[0][:])  # Ajouter une ligne

        return output_grid

    def evaluate_composition_quality(self, composition: Dict[str, Any],
                                   original_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Évalue la qualité d'une composition
        """
        if not composition or 'composition' not in composition:
            return {'quality_score': 0, 'improvement': 0}

        composition_info = composition['composition']
        if not composition_info:
            return {'quality_score': 0, 'improvement': 0}

        # Calcul d'un score de qualité basé sur la composition
        base_confidence = composition.get('confidence', 0)

        # Bonus pour les compositions complexes réussies
        complexity_bonus = 0
        if composition_info.get('type') == 'hierarchical':
            primary_count = len(composition_info.get('primary', []))
            complexity_bonus = min(primary_count * 0.1, 0.3)

        # Pénalité pour les conflits non résolus
        conflict_penalty = 0
        if 'conflicts' in composition_info:
            conflict_penalty = len(composition_info['conflicts']) * 0.1

        quality_score = base_confidence + complexity_bonus - conflict_penalty
        quality_score = max(0, min(quality_score, 1.0))

        # Calcul de l'amélioration par rapport à l'analyse originale
        original_score = original_analysis.get('overall_score', 0)
        improvement = quality_score - original_score

        return {
            'quality_score': quality_score,
            'improvement': improvement,
            'complexity_bonus': complexity_bonus,
            'conflict_penalty': conflict_penalty
        }

    def optimize_composition(self, composition: Dict[str, Any],
                           patterns_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Optimise une composition existante
        """
        if not composition or 'composition' not in composition:
            return composition

        optimized = copy.deepcopy(composition)

        # Optimisations simples
        composition_info = optimized['composition']

        if composition_info.get('type') == 'hierarchical':
            # Réorganiser la hiérarchie si nécessaire
            primary = composition_info.get('primary', [])
            secondary = composition_info.get('secondary', [])

            # Déplacer les patterns très confiants vers primary
            for pattern in secondary[:]:
                if pattern.get('confidence', 0) > 0.9:
                    primary.append(pattern)
                    secondary.remove(pattern)

            composition_info['primary'] = primary
            composition_info['secondary'] = secondary

        return optimized
