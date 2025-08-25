#!/usr/bin/env python3
"""
Architecture v2 complète - Solveur ARC-AGI anti-surapprentissage
Intégration complète de tous les composants
"""

from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
from pattern_detector_v2_ameliore import PatternDetectorAmeliore
from pattern_scorer_v2_ameliore import PatternScorerAmeliore
from pattern_composer_v2 import PatternComposerAmeliore
from pattern_predictor_v2 import PatternPredictorV2
import copy
import math

class ArchitectureV2:
    """
    Architecture v2 complète pour ARC-AGI
    Architecture modulaire anti-surapprentissage
    """

    def __init__(self):
        self.detector = PatternDetectorAmeliore()
        self.scorer = PatternScorerAmeliore()
        self.composer = PatternComposerAmeliore()
        self.predictor = PatternPredictorV2()

        # Configuration
        self.confidence_threshold = 0.35  # Optimisé pour PatternPredictor
        self.overfitting_threshold = 0.4  # Optimisé pour PatternPredictor
        self.verbose = True

    def solve_puzzle(self, input_grid: List[List[int]],
                    output_grid: Optional[List[List[int]]] = None,
                    training_examples: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Résolution complète d'un puzzle avec l'architecture v2
        """
        solution = {
            'input_grid': input_grid,
            'predicted_output': None,
            'confidence': 0,
            'patterns_used': [],
            'composition_strategy': None,
            'anti_overfitting_score': 0,
            'processing_steps': []
        }

        # Étape 1: Détection des patterns
        if self.verbose:
            print("🔍 ETAPE 1: DETECTION DES PATTERNS")

        patterns_analysis = self.detector.analyze_puzzle(input_grid, output_grid or [])
        solution['patterns_analysis'] = patterns_analysis
        solution['processing_steps'].append("Pattern detection completed")

        if self.verbose:
            print(".2f")

        # Étape 1.5: Prédiction de patterns manquants (NOUVELLE ÉTAPE)
        if self.verbose:
            print("\n🧠 ÉTAPE 1.5: PRÉDICTION DE PATTERNS MANQUANTS")

        # Préparer le contexte pour la prédiction
        contexte_puzzle = {
            'dimensions': [len(input_grid), len(input_grid[0]) if input_grid else 0],
            'couleurs_uniques': len(set(cell for row in input_grid for cell in row)) if input_grid else 0,
            'patterns_detectes': list(patterns_analysis.get('spatial', {}).keys()) +
                               list(patterns_analysis.get('color', {}).keys()) +
                               list(patterns_analysis.get('structural', {}).keys()) +
                               list(patterns_analysis.get('mathematical', {}).keys()),
            'complexite_estimee': self._estimer_complexite_puzzle(input_grid)
        }

        # Prédire les patterns manquants
        patterns_predits = self.predictor.predire_patterns_manquants(
            patterns_analysis, contexte_puzzle, seuil_confiance=0.6
        )

        # Enrichir l'analyse avec les prédictions
        patterns_enrichis = self._enrichir_analyse_avec_predictions(patterns_analysis, patterns_predits)
        solution['patterns_predits'] = patterns_predits
        solution['patterns_analysis_enrichie'] = patterns_enrichis
        solution['processing_steps'].append("Pattern prediction completed")

        if self.verbose:
            total_predits = sum(len(patterns) for patterns in patterns_predits.values())
            print(f"   Patterns prédits: {total_predits}")
            for categorie, patterns in patterns_predits.items():
                if patterns:
                    pattern_names = list(patterns.keys())
                    print(f"   {categorie.upper()}: {pattern_names}")

        # Étape 2: Évaluation anti-surapprentissage (avec patterns enrichis)
        if self.verbose:
            print("\n📊 ETAPE 2: EVALUATION ANTI-SURAPPRENTISSAGE")

        evaluation = self.scorer.evaluate_pattern_suite_advanced(patterns_enrichis)
        solution['evaluation'] = evaluation
        solution['processing_steps'].append("Anti-overfitting evaluation completed")

        if self.verbose:
            print(".2f")
            print(".2f")

        # Étape 3: Composition des patterns
        if self.verbose:
            print("\n🔧 ETAPE 3: COMPOSITION DES PATTERNS")

        composition = self.composer.compose_patterns(patterns_analysis, 'hierarchical')
        solution['composition'] = composition
        solution['processing_steps'].append("Pattern composition completed")

        if self.verbose and composition and 'composition' in composition:
            comp_info = composition['composition']
            if comp_info:
                print(f"   Strategie: {comp_info.get('type', 'unknown')}")
                if 'primary' in comp_info:
                    print(f"   Patterns primaires: {len(comp_info['primary'])}")
                if 'secondary' in comp_info:
                    print(f"   Patterns secondaires: {len(comp_info['secondary'])}")

        # Étape 4: Application de la solution
        if self.verbose:
            print("\n🎯 ETAPE 4: APPLICATION DE LA SOLUTION")

        if composition and 'composition' in composition:
            predicted_output = self.composer.apply_composition(composition, input_grid)
            solution['predicted_output'] = predicted_output
            solution['processing_steps'].append("Solution application completed")

            # Calcul de la confiance finale
            solution['confidence'] = composition.get('confidence', 0)
            solution['anti_overfitting_score'] = evaluation.get('overfitting_risk', 1.0)  # Score inversé

            # Patterns utilisés
            if composition['composition'] and 'primary' in composition['composition']:
                solution['patterns_used'] = [p['name'] for p in composition['composition']['primary']]

            solution['composition_strategy'] = (composition.get('composition') or {}).get('type', 'unknown')

            if self.verbose:
                print("   Prediction generee avec succes")
                print(f"   Dimensions output: {len(predicted_output)}x{len(predicted_output[0]) if predicted_output else 0}")

        else:
            solution['predicted_output'] = copy.deepcopy(input_grid)  # Retourner l'entrée si pas de solution
            solution['processing_steps'].append("No solution generated - returning input")

            if self.verbose:
                print("   Aucune solution generee - retour de l'entree")

        # Validation finale
        if output_grid:
            is_correct = self._compare_grids(solution['predicted_output'], output_grid)
            solution['validation'] = {
                'expected_output': output_grid,
                'is_correct': is_correct,
                'similarity_score': self._calculate_similarity(solution['predicted_output'], output_grid)
            }

            if self.verbose:
                print("\n✅ VALIDATION:")
                print(f"   Prediction correct: {'OUI' if is_correct else 'NON'}")
                print(f"   Score de similarite: {self._calculate_similarity(solution['predicted_output'], output_grid):.2f}%")

        return solution

    def _compare_grids(self, grid1: List[List[int]], grid2: List[List[int]]) -> bool:
        """Compare deux grilles exactement"""
        if not grid1 or not grid2:
            return False
        if len(grid1) != len(grid2) or len(grid1[0]) != len(grid2[0]):
            return False
        return all(grid1[i][j] == grid2[i][j] for i in range(len(grid1)) for j in range(len(grid1[0])))

    def _calculate_similarity(self, grid1: List[List[int]], grid2: List[List[int]]) -> float:
        """Calcule la similarité entre deux grilles"""
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

        return (matching / total) * 100

    def generate_solution_report(self, solution: Dict[str, Any]) -> str:
        """Génère un rapport complet de la solution"""
        report = ".2f"
        report += "\n" + "=" * 60

        # Informations générales
        report += ".2f"
        report += ".2f"
        report += f"\nPatterns utilises: {solution.get('patterns_used', [])}"
        report += f"\nStrategie de composition: {solution.get('composition_strategy', 'unknown')}"
        report += ".2f"

        # Étapes de traitement
        report += "\n\n📋 ETAPES DE TRAITEMENT:"
        for i, step in enumerate(solution.get('processing_steps', []), 1):
            report += f"\n   {i}. {step}"

        # Analyse des patterns
        if 'patterns_analysis' in solution:
            analysis = solution['patterns_analysis']
            report += ".2f"
            report += ".2f"

        # Évaluation
        if 'evaluation' in solution:
            evaluation = solution['evaluation']
            report += ".2f"
            report += ".2f"

        # Composition
        if 'composition' in solution:
            composition = solution['composition']
            if composition and 'composition' in composition:
                comp_info = composition['composition']
                if comp_info:
                    report += f"\n   Type de composition: {comp_info.get('type', 'unknown')}"

        # Validation
        if 'validation' in solution:
            validation = solution['validation']
            report += ".2f"
            report += ".2f"

        # Grille prédite
        if solution.get('predicted_output'):
            report += "\n\n📊 GRILLE PREDITE:"
            for row in solution['predicted_output']:
                report += f"\n   {row}"

        return report

    def batch_solve(self, puzzles: Dict[str, Dict[str, Any]],
                   generate_reports: bool = True) -> Dict[str, Dict[str, Any]]:
        """
        Résolution par lots de plusieurs puzzles
        """
        results = {}

        for puzzle_id, puzzle_data in puzzles.items():
            print(f"\n🔬 Resolution du puzzle {puzzle_id}")

            # Prendre le premier exemple d'entraînement
            if 'train' in puzzle_data and puzzle_data['train']:
                example = puzzle_data['train'][0]
                input_grid = example['input']
                output_grid = example['output']

                # Résoudre le puzzle
                solution = self.solve_puzzle(input_grid, output_grid, puzzle_data['train'])

                results[puzzle_id] = solution

                if generate_reports:
                    report = self.generate_solution_report(solution)
                    # Sauvegarder le rapport
                    report_file = f"rapport_architecture_v2_{puzzle_id}.md"
                    with open(report_file, 'w', encoding='utf-8') as f:
                        f.write(report)

                    print(f"   Rapport sauvegarde: {report_file}")

        return results

    def evaluate_architecture(self, test_results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Évalue les performances globales de l'architecture
        """
        if not test_results:
            return {'error': 'No test results'}

        evaluation = {
            'total_puzzles': len(test_results),
            'successful_puzzles': 0,
            'average_confidence': 0,
            'average_anti_overfitting': 0,
            'patterns_usage': defaultdict(int),
            'composition_strategies': defaultdict(int)
        }

        total_confidence = 0
        total_anti_overfitting = 0

        for puzzle_id, solution in test_results.items():
            # Vérifier si la solution est correcte
            if 'validation' in solution and solution['validation'].get('is_correct', False):
                evaluation['successful_puzzles'] += 1

            # Accumuler les métriques
            total_confidence += solution.get('confidence', 0)
            total_anti_overfitting += solution.get('anti_overfitting_score', 0)

            # Analyser l'usage des patterns
            for pattern in solution.get('patterns_used', []):
                evaluation['patterns_usage'][pattern] += 1

            # Analyser les stratégies de composition
            strategy = solution.get('composition_strategy', 'unknown')
            evaluation['composition_strategies'][strategy] += 1

        # Calcul des moyennes
        if evaluation['total_puzzles'] > 0:
            evaluation['average_confidence'] = total_confidence / evaluation['total_puzzles']
            evaluation['average_anti_overfitting'] = total_anti_overfitting / evaluation['total_puzzles']

        evaluation['success_rate'] = (evaluation['successful_puzzles'] / evaluation['total_puzzles']) * 100

        return evaluation

    def optimize_architecture(self, feedback_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Optimise l'architecture basée sur les retours d'expérience
        """
        optimizations = {
            'confidence_threshold_adjusted': False,
            'pattern_detection_improved': False,
            'composition_strategy_optimized': False,
            'overfitting_protection_enhanced': False
        }

        # Analyse du feedback
        if 'average_confidence' in feedback_data and feedback_data['average_confidence'] < 0.5:
            self.confidence_threshold *= 0.9  # Réduire le seuil de confiance
            optimizations['confidence_threshold_adjusted'] = True

        if 'patterns_usage' in feedback_data:
            # Si certains patterns ne sont jamais utilisés, les améliorer
            unused_patterns = [p for p, count in feedback_data['patterns_usage'].items() if count == 0]
            if unused_patterns:
                optimizations['pattern_detection_improved'] = True

        return optimizations

    def _estimer_complexite_puzzle(self, input_grid: List[List[int]]) -> float:
        """Estime la complexité d'un puzzle"""
        if not input_grid:
            return 0.0

        complexite = 0.3  # Base

        # Taille du puzzle
        taille = len(input_grid) * len(input_grid[0]) if input_grid and input_grid[0] else 0
        complexite += min(taille / 100, 0.3)

        # Diversité des couleurs
        couleurs = set()
        for row in input_grid:
            for cell in row:
                couleurs.add(cell)
        complexite += min(len(couleurs) / 10, 0.2)

        # Complexité spatiale (variations)
        variations = 0
        for i in range(len(input_grid)):
            for j in range(len(input_grid[0])):
                if i > 0 and input_grid[i][j] != input_grid[i-1][j]:
                    variations += 1
                if j > 0 and input_grid[i][j] != input_grid[i][j-1]:
                    variations += 1
        total_cells = taille
        taux_variation = variations / (total_cells * 2) if total_cells > 0 else 0
        complexite += min(taux_variation, 0.2)

        return min(complexite, 1.0)

    def _enrichir_analyse_avec_predictions(self, patterns_analysis: Dict[str, Any],
                                          patterns_predits: Dict[str, Any]) -> Dict[str, Any]:
        """Enrichit l'analyse des patterns avec les prédictions"""
        analyse_enrichie = copy.deepcopy(patterns_analysis)

        # Ajouter les patterns prédits à l'analyse
        for categorie, patterns in patterns_predits.items():
            if categorie not in analyse_enrichie:
                analyse_enrichie[categorie] = {}

            for pattern_name, prediction in patterns.items():
                # Convertir la prédiction au format de l'analyse
                pattern_key = f"{categorie}.{prediction['pattern']}"
                analyse_enrichie[categorie][pattern_key] = {
                    'confidence': prediction['confiance'],
                    'score': prediction['confiance'] * 0.8,  # Score légèrement inférieur
                    'details': {
                        'predicted': True,
                        'method': prediction['methode'],
                        'reason': prediction['raison'],
                        'prediction_details': prediction.get('details', {})
                    }
                }

        # Recalculer les statistiques globales
        total_patterns = sum(len(patterns) for patterns in analyse_enrichie.values()
                           if isinstance(patterns, dict))
        total_confidence = sum(
            pattern_data.get('confidence', 0)
            for patterns in analyse_enrichie.values()
            if isinstance(patterns, dict)
            for pattern_data in patterns.values()
        )

        if total_patterns > 0:
            analyse_enrichie['overall_score'] = total_confidence / total_patterns
            analyse_enrichie['total_patterns'] = total_patterns

        return analyse_enrichie
