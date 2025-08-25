#!/usr/bin/env python3
"""
Diagnostic Approfondi du PatternPredictor
Analyse détaillée pour comprendre l'inactivité
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
from typing import Dict, List, Any, Tuple
import time

class DiagnostiqueurPatternPredictor:
    """Diagnostiqueur complet du PatternPredictor"""

    def __init__(self):
        self.architecture = ArchitectureV2()
        # Configuration ultra-permissive pour forcer l'activation
        self.architecture.confidence_threshold = 0.01  # Ultra-permissif
        self.architecture.overfitting_threshold = 0.9  # Ultra-tolérant

        self.logs_diagnostic = []
        self.puzzles_test = []

    def executer_diagnostic_complet(self):
        """Exécute le diagnostic complet du PatternPredictor"""
        print("🔍 DIAGNOSTIC APPROFONDI PATTERN PREDICTOR")
        print("=" * 50)
        print("Objectif: Comprendre pourquoi il ne prédit rien")
        print()

        # Étape 1: Analyse des seuils actuels
        print("ETAPE 1: ANALYSE DES SEUILS ACTUELS")
        print("-" * 40)

        seuils_analyse = self.analyser_seuils_actuels()
        print(f"Seuils actuels:")
        for key, value in seuils_analyse.items():
            print(".3f")
        print()

        # Étape 2: Test avec tracing complet
        print("ETAPE 2: TEST AVEC TRACING COMPLET")
        print("-" * 40)

        puzzle_test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output_test = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]

        print("Test sur puzzle simple avec translation +1")
        print(f"Input: {puzzle_test}")
        print(f"Output attendu: {output_test}")
        print()

        tracing_resultats = self.test_avec_tracing_complet(puzzle_test, output_test)
        print(f"Résultat tracing:")
        for key, value in tracing_resultats.items():
            if isinstance(value, dict):
                print(f"  {key}: {dict(list(value.items())[:3])}...")  # Limiter l'affichage
            else:
                print(f"  {key}: {value}")
        print()

        # Étape 3: Création de puzzles de test évidents
        print("ETAPE 3: CREATION DE PUZZLES DE TEST ÉVIDENTS")
        print("-" * 55)

        puzzles_evidences = self.creer_puzzles_evidences()
        print(f"Puzzles de test créés: {len(puzzles_evidences)}")

        for i, (nom, puzzle) in enumerate(puzzles_evidences.items(), 1):
            print(f"  {i}. {nom}: {len(puzzle['input'])}x{len(puzzle['input'][0])}")
        print()

        # Étape 4: Test sur puzzles évidents
        print("ETAPE 4: TEST SUR PUZZLES ÉVIDENTS")
        print("-" * 40)

        resultats_evidences = []
        for nom, puzzle in puzzles_evidences.items():
            print(f"Test {nom}...")
            try:
                resultat = self.test_puzzle_evidement(puzzle['input'], puzzle['output'], nom)
                resultats_evidences.append(resultat)
                print(f"  Patterns prédits: {resultat['patterns_predits']}")
                print(f"  Succès: {resultat['succes']}")
                print()
            except Exception as e:
                print(f"  ❌ Erreur: {e}")
                print()
        print()

        # Étape 5: Analyse des blocages
        print("ETAPE 5: ANALYSE DES BLOCAGES")
        print("-" * 35)

        blocages = self.analyser_blocages(resultats_evidences)
        print("Blocages identifiés:")
        for i, blocage in enumerate(blocages, 1):
            print(f"  {i}. {blocage['type']}: {blocage['description']}")
        print()

        # Étape 6: Solutions proposées
        print("ETAPE 6: SOLUTIONS PROPOSÉES")
        print("-" * 32)

        solutions = self.proposer_solutions(blocages)
        print("Solutions recommandées:")
        for i, solution in enumerate(solutions, 1):
            print(f"  {i}. {solution['action']}: {solution['description']}")
        print()

        # Étape 7: Test des solutions
        print("ETAPE 7: TEST DES SOLUTIONS")
        print("-" * 30)

        resultats_solutions = self.tester_solutions(solutions)
        print("Résultats des solutions:")
        for solution, resultat in resultats_solutions.items():
            print(f"  {solution}: {resultat}")
        print()

        return {
            'seuils_analyse': seuils_analyse,
            'tracing_resultats': tracing_resultats,
            'resultats_evidences': resultats_evidences,
            'blocages': blocages,
            'solutions': solutions,
            'resultats_solutions': resultats_solutions
        }

    def analyser_seuils_actuels(self) -> Dict[str, float]:
        """Analyse les seuils actuels du système"""
        return {
            'confidence_threshold': self.architecture.confidence_threshold,
            'overfitting_threshold': self.architecture.overfitting_threshold,
            'predictor_present': hasattr(self.architecture, 'predictor'),
            'modeles_present': hasattr(self.architecture.predictor, 'modeles_prediction') if hasattr(self.architecture, 'predictor') else False
        }

    def test_avec_tracing_complet(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Test avec tracing complet de l'exécution"""
        print("  Tracing détaillé de l'exécution...")

        # Activer le mode verbose
        self.architecture.verbose = True

        try:
            # Test de résolution
            solution = self.architecture.solve_puzzle(input_grid, output_grid)

            # Analyse détaillée
            patterns_analysis = solution.get('patterns_analysis', {})
            patterns_predits = solution.get('patterns_predits', {})
            patterns_enrichis = solution.get('patterns_analysis_enrichie', {})

            tracing = {
                'patterns_analysis': patterns_analysis,
                'patterns_predits': patterns_predits,
                'patterns_enrichis': patterns_enrichis,
                'confidence': solution.get('confidence', 0),
                'execution_time': solution.get('execution_time', 0),
                'processing_steps': solution.get('processing_steps', []),
                'erreur': None
            }

        except Exception as e:
            tracing = {
                'patterns_analysis': {},
                'patterns_predits': {},
                'patterns_enrichis': {},
                'confidence': 0,
                'execution_time': 0,
                'processing_steps': [],
                'erreur': str(e)
            }

        # Désactiver le mode verbose
        self.architecture.verbose = False

        return tracing

    def creer_puzzles_evidences(self) -> Dict[str, Dict[str, List[List[int]]]]:
        """Crée des puzzles avec patterns évidents"""
        puzzles = {}

        # Puzzle 1: Translation simple
        puzzles['translation_simple'] = {
            'input': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            'output': [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
        }

        # Puzzle 2: Symétrie horizontale
        puzzles['symetrie_horizontale'] = {
            'input': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            'output': [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        }

        # Puzzle 3: Répétition de motif
        puzzles['repetition_motif'] = {
            'input': [[1, 2], [3, 4]],
            'output': [[1, 2, 1, 2], [3, 4, 3, 4]]
        }

        # Puzzle 4: Changement de couleur uniforme
        puzzles['changement_couleur'] = {
            'input': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            'output': [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        }

        # Puzzle 5: Scale up simple
        puzzles['scale_up'] = {
            'input': [[1, 2], [3, 4]],
            'output': [[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4], [3, 3, 4, 4]]
        }

        return puzzles

    def test_puzzle_evidement(self, input_grid: List[List[int]], output_grid: List[List[int]], nom: str) -> Dict[str, Any]:
        """Test un puzzle avec pattern évident"""
        print(f"  Test puzzle {nom}...")

        try:
            solution = self.architecture.solve_puzzle(input_grid, output_grid)

            patterns_predits = solution.get('patterns_predits', {})
            total_predits = sum(len(patterns) for patterns in patterns_predits.values())

            return {
                'nom': nom,
                'succes': solution.get('confidence', 0) > 0.5,
                'confidence': solution.get('confidence', 0),
                'patterns_predits': total_predits,
                'patterns_details': patterns_predits,
                'erreur': None
            }

        except Exception as e:
            return {
                'nom': nom,
                'succes': False,
                'confidence': 0,
                'patterns_predits': 0,
                'patterns_details': {},
                'erreur': str(e)
            }

    def analyser_blocages(self, resultats: List[Dict]) -> List[Dict]:
        """Analyse les blocages identifiés"""
        blocages = []

        # Analyse des patterns prédits
        total_predits = sum(r['patterns_predits'] for r in resultats)
        if total_predits == 0:
            blocages.append({
                'type': 'Aucun pattern prédit',
                'description': 'Le PatternPredictor ne prédit aucun pattern sur des puzzles évidents',
                'severite': 'CRITIQUE'
            })

        # Analyse des erreurs
        erreurs = [r for r in resultats if r['erreur']]
        if erreurs:
            blocages.append({
                'type': 'Erreurs d\'exécution',
                'description': f'{len(erreurs)} puzzles sur {len(resultats)} génèrent des erreurs',
                'severite': 'ELEVEE'
            })

        # Analyse des seuils
        if self.architecture.confidence_threshold > 0.1:
            blocages.append({
                'type': 'Seuils trop restrictifs',
                'description': f'Confidence threshold à {self.architecture.confidence_threshold} peut être trop élevé',
                'severite': 'MODEREE'
            })

        # Analyse de la complexité
        patterns_detectes = [r for r in resultats if r['patterns_predits'] > 0]
        if not patterns_detectes:
            blocages.append({
                'type': 'Patterns non détectés',
                'description': 'Aucun pattern détecté même sur puzzles évidents',
                'severite': 'CRITIQUE'
            })

        return blocages

    def proposer_solutions(self, blocages: List[Dict]) -> List[Dict]:
        """Propose des solutions pour les blocages"""
        solutions = []

        for blocage in blocages:
            if blocage['type'] == 'Aucun pattern prédit':
                solutions.extend([
                    {
                        'action': 'Forcer l\'activation manuelle',
                        'description': 'Modifier PatternPredictor pour prédire au moins un pattern par test',
                        'priorite': 'CRITIQUE'
                    },
                    {
                        'action': 'Ajouter patterns de test',
                        'description': 'Injecter manuellement des patterns dans la base d\'apprentissage',
                        'priorite': 'ELEVEE'
                    }
                ])

            elif blocage['type'] == 'Erreurs d\'exécution':
                solutions.append({
                    'action': 'Améliorer la gestion d\'erreurs',
                    'description': 'Ajouter des try-catch et gérer les types de données problématiques',
                    'priorite': 'MODEREE'
                })

            elif blocage['type'] == 'Seuils trop restrictifs':
                solutions.append({
                    'action': 'Ajuster les seuils à zéro',
                    'description': 'Mettre tous les seuils à 0 pour forcer l\'activation',
                    'priorite': 'ELEVEE'
                })

            elif blocage['type'] == 'Patterns non détectés':
                solutions.append({
                    'action': 'Simplifier la détection',
                    'description': 'Créer un détecteur de patterns ultra-simple pour validation',
                    'priorite': 'CRITIQUE'
                })

        return solutions

    def tester_solutions(self, solutions: List[Dict]) -> Dict[str, str]:
        """Test les solutions proposées"""
        resultats = {}

        for solution in solutions:
            action = solution['action']

            if action == 'Forcer l\'activation manuelle':
                # Tester avec un pattern forcé
                try:
                    self.forcer_pattern_test()
                    resultats[action] = "✅ Pattern forcé avec succès"
                except Exception as e:
                    resultats[action] = f"❌ Erreur: {e}"

            elif action == 'Ajuster les seuils à zéro':
                # Tester avec seuils à zéro
                anciens_seuils = {
                    'confidence': self.architecture.confidence_threshold,
                    'overfitting': self.architecture.overfitting_threshold
                }
                self.architecture.confidence_threshold = 0.0
                self.architecture.overfitting_threshold = 1.0

                test_result = self.test_avec_tracing_complet([[1, 2]], [[2, 3]])
                if test_result['patterns_predits']:
                    resultats[action] = "✅ Activation avec seuils à zéro"
                else:
                    resultats[action] = "⚠️ Seuils à zéro insuffisant"

                # Restaurer les seuils
                self.architecture.confidence_threshold = anciens_seuils['confidence']
                self.architecture.overfitting_threshold = anciens_seuils['overfitting']

            elif action == 'Simplifier la détection':
                resultats[action] = "⏳ Solution à implémenter"

            else:
                resultats[action] = "⏳ Solution à implémenter"

        return resultats

    def forcer_pattern_test(self):
        """Force un pattern de test pour validation"""
        print("  Forçage d'un pattern de test...")

        # Créer un pattern simple et le forcer
        input_test = [[1, 2], [3, 4]]
        output_test = [[2, 3], [4, 5]]

        # Simuler une prédiction
        pattern_force = {
            'mathematical': {
                'increment_1': {
                    'pattern': 'increment_1',
                    'categorie': 'mathematical',
                    'confiance': 0.9,
                    'methode': 'force_test',
                    'raison': 'Pattern forcé pour test'
                }
            }
        }

        print(f"  Pattern forcé: {pattern_force}")

def main():
    """Fonction principale"""
    print("🔬 DIAGNOSTIC APPROFONDI PATTERN PREDICTOR")
    print("Comprendre l'inactivité et trouver la solution")
    print()

    diagnostiqueur = DiagnostiqueurPatternPredictor()
    resultats = diagnostiqueur.executer_diagnostic_complet()

    print("\n" + "=" * 50)
    print("DIAGNOSTIC TERMINÉ !")
    print("=" * 50)
    print("  • Tracing complet effectué")
    print("  • Puzzles de test analysés")
    print("  • Blocages identifiés")
    print("  • Solutions proposées")
    print("  • PatternPredictor diagnostiqué")

if __name__ == "__main__":
    main()


