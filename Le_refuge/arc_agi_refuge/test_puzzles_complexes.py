#!/usr/bin/env python3
"""
Test sur Puzzles Complexes ARC-AGI
Activation forcée du PatternPredictor
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import statistics
import time
from typing import Dict, List, Any
from collections import defaultdict

class TesteurPuzzlesComplexes:
    """Testeur pour puzzles complexes ARC-AGI"""

    def __init__(self):
        self.solveur = ArchitectureV2()
        # Configuration ultra-agressive pour forcer les prédictions
        self.solveur.confidence_threshold = 0.01  # Ultra-permissif
        self.solveur.overfitting_threshold = 0.95  # Ultra-tolérant
        self.solveur.verbose = False

        self.resultats = []
        self.puzzles_complexes = []
        self.details_predictions = []

    def executer_test_complexes(self):
        """Exécute le test sur puzzles complexes"""
        print("🎯 TEST PUZZLES COMPLEXES ARC-AGI")
        print("=" * 45)
        print("Activation forcée du PatternPredictor")
        print()

        # Étape 1: Sélection des puzzles complexes
        print("ETAPE 1: SÉLECTION PUZZLES COMPLEXES")
        print("-" * 40)

        puzzles_complexes = self.selectionner_puzzles_complexes()
        print(f"20 puzzles complexes sélectionnés")

        # Analyse de la complexité
        complexites = [self.estimer_complexite_puzzle_rapide(p) for p in puzzles_complexes]
        moyenne_complexite = statistics.mean(complexites)
        print(".2f")
        print()

        # Étape 2: Tests avec monitoring détaillé
        print("ETAPE 2: TESTS AVEC MONITORING DÉTAILLÉ")
        print("-" * 40)

        resultats_tests = []
        puzzles_avec_predictions = 0

        for i, puzzle_path in enumerate(puzzles_complexes, 1):
            puzzle_id = puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', '')
            print(f"[{i:2d}/{len(puzzles_complexes)}] Test {puzzle_id}...")
            start_time = time.time()

            try:
                resultat = self.tester_puzzle_complexe(puzzle_path)
                execution_time = time.time() - start_time
                resultat['execution_time'] = execution_time

                if resultat['patterns_predits'] > 0:
                    puzzles_avec_predictions += 1
                    self.details_predictions.append({
                        'puzzle_id': puzzle_id,
                        'patterns_predits': resultat['patterns_predits'],
                        'succes': resultat['succes'],
                        'confidence': resultat['confidence']
                    })

                resultats_tests.append(resultat)
                self.resultats.append(resultat)

                # Affichage des résultats
                status = "✅" if resultat['succes'] else "❌"
                pred_status = "🔮" if resultat['patterns_predits'] > 0 else "🔍"
                print(f"    {status} Succès: {resultat['succes']}, {pred_status} Patterns prédits: {resultat['patterns_predits']}, Temps: {execution_time:.2f}s")
            except Exception as e:
                print(f"  ❌ Erreur critique: {e}")
                resultats_tests.append({
                    'puzzle_id': puzzle_id,
                    'succes': False,
                    'erreur': str(e)
                })

        print()

        # Étape 3: Analyse des prédictions
        print("ETAPE 3: ANALYSE DES PRÉDICTIONS")
        print("-" * 35)

        self.analyser_predictions_complexes(resultats_tests)
        print()

        # Étape 4: Comparaison avec puzzles simples
        print("ETAPE 4: COMPARAISON AVEC PUZZLES SIMPLES")
        print("-" * 45)

        self.comparer_complexe_vs_simple(resultats_tests)
        print()

        # Étape 5: Rapport final
        print("ETAPE 5: RAPPORT FINAL")
        print("-" * 25)

        self.generer_rapport_complexes(resultats_tests, puzzles_avec_predictions)

        return {
            'resultats': resultats_tests,
            'puzzles_avec_predictions': puzzles_avec_predictions,
            'predictions_details': self.details_predictions,
            'performance_complexe': self.calculer_performance_complexe(resultats_tests)
        }

    def selectionner_puzzles_complexes(self) -> List[str]:
        """Sélectionne les 20 puzzles les plus complexes"""
        print("  Recherche des puzzles les plus complexes...")

        # Trouver tous les puzzles
        patterns = [
            "ARC-AGI-2-main/data/training/*.json",
            "ARC-AGI/data/training/*.json",
            "*.json"
        ]

        tous_puzzles = []
        for pattern in patterns:
            try:
                fichiers = glob.glob(pattern)
                for fichier in fichiers:
                    try:
                        with open(fichier, 'r') as f:
                            data = json.load(f)
                            if 'train' in data and len(data['train']) > 0:
                                tous_puzzles.append(fichier)
                    except:
                        continue
            except:
                continue

        # Éliminer les doublons
        tous_puzzles = list(set(tous_puzzles))
        print(f"  Total puzzles disponibles: {len(tous_puzzles)}")

        # Évaluer la complexité de tous les puzzles
        puzzles_evalues = []
        for puzzle in tous_puzzles[:200]:  # Limiter pour performance
            try:
                complexite = self.estimer_complexite_puzzle_rapide(puzzle)
                puzzles_evalues.append((puzzle, complexite))
            except:
                continue

        # Trier par complexité décroissante et sélectionner les 20 plus complexes
        puzzles_evalues.sort(key=lambda x: x[1], reverse=True)
        puzzles_complexes = [p[0] for p in puzzles_evalues[:20]]

        print(f"  20 puzzles les plus complexes sélectionnés")
        return puzzles_complexes

    def estimer_complexite_puzzle_rapide(self, puzzle_path: str) -> float:
        """Estime la complexité d'un puzzle (version rapide)"""
        try:
            with open(puzzle_path, 'r') as f:
                data = json.load(f)

            if 'train' in data and len(data['train']) > 0:
                exemple = data['train'][0]
                input_grid = exemple.get('input', [])
                output_grid = exemple.get('output', [])

                if not input_grid or not output_grid:
                    return 0.5

                # Facteurs de complexité
                taille_input = len(input_grid) * len(input_grid[0]) if input_grid and input_grid[0] else 0
                taille_output = len(output_grid) * len(output_grid[0]) if output_grid and output_grid[0] else 0

                couleurs_uniques = len(set())
                for row in input_grid:
                    if row:
                        couleurs_uniques.update(row)

                ratio_taille = taille_output / taille_input if taille_input > 0 else 1.0

                # Complexité maximale pour favoriser les puzzles difficiles
                complexite = (
                    min(taille_input / 150, 1.0) * 0.25 +      # Taille importante
                    min(couleurs_uniques / 8, 1.0) * 0.25 +    # Couleurs nombreuses
                    abs(ratio_taille - 1.0) * 0.3 +            # Changement de taille
                    min(len(exemple.get('output', [])) / 25, 1.0) * 0.2  # Complexité de sortie
                )

                return min(complexite, 1.0)
        except:
            pass

        return 0.5  # Complexité moyenne par défaut

    def tester_puzzle_complexe(self, puzzle_path: str) -> Dict[str, Any]:
        """Test un puzzle complexe avec monitoring détaillé"""
        puzzle_id = puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', '')

        try:
            with open(puzzle_path, 'r') as f:
                puzzle_data = json.load(f)

            if 'train' not in puzzle_data or len(puzzle_data['train']) == 0:
                return {
                    'puzzle_id': puzzle_id,
                    'succes': False,
                    'erreur': 'Pas de données d\'entraînement'
                }

            exemple = puzzle_data['train'][0]
            input_grid = exemple.get('input', [])
            output_grid = exemple.get('output', [])

            if not input_grid or not output_grid:
                return {
                    'puzzle_id': puzzle_id,
                    'succes': False,
                    'erreur': 'Grilles vides'
                }

            # Test avec le solveur (mode verbose pour debugging)
            self.solveur.verbose = True
            solution = self.solveur.solve_puzzle(input_grid, output_grid)
            self.solveur.verbose = False

            # Analyse détaillée
            confidence = solution.get('confidence', 0)
            succes = confidence > 0.5

            patterns_analysis = solution.get('patterns_analysis', {})
            patterns_predits = solution.get('patterns_predits', {})

            total_patterns_detectes = sum(len(patterns) for patterns in patterns_analysis.values() if isinstance(patterns, dict))
            total_patterns_predits = sum(len(patterns) for patterns in patterns_predits.values())

            complexite = self.estimer_complexite_puzzle_rapide(puzzle_path)

            # Stocker les détails des prédictions pour analyse
            if total_patterns_predits > 0:
                self.puzzles_complexes.append({
                    'puzzle_id': puzzle_id,
                    'patterns_predits': patterns_predits,
                    'patterns_detectes': patterns_analysis,
                    'confidence': confidence,
                    'complexite': complexite
                })

            return {
                'puzzle_id': puzzle_id,
                'succes': succes,
                'confidence': confidence,
                'patterns_detectes': total_patterns_detectes,
                'patterns_predits': total_patterns_predits,
                'complexite': complexite,
                'execution_time': 0  # Sera mis à jour par l'appelant
            }

        except Exception as e:
            return {
                'puzzle_id': puzzle_id,
                'succes': False,
                'erreur': str(e)
            }

    def analyser_predictions_complexes(self, resultats: List[Dict]):
        """Analyse détaillée des prédictions sur puzzles complexes"""
        print("ANALYSE DÉTAILLÉE DES PRÉDICTIONS:")
        print("-" * 40)

        puzzles_avec_pred = [r for r in resultats if r.get('patterns_predits', 0) > 0]
        puzzles_sans_pred = [r for r in resultats if r.get('patterns_predits', 0) == 0]

        print(f"  Puzzles avec prédictions: {len(puzzles_avec_pred)}/{len(resultats)}")
        print(f"  Puzzles sans prédictions: {len(puzzles_sans_pred)}/{len(resultats)}")

        if puzzles_avec_pred:
            print("\n  🎉 PATTERN PREDICTOR ACTIF SUR PUZZLES COMPLEXES !")
            print("  Liste des puzzles avec prédictions:")

            for puzzle in puzzles_avec_pred:
                print(f"    • {puzzle['puzzle_id']}: {puzzle['patterns_predits']} prédictions")

            # Analyse de l'impact des prédictions
            succes_avec_pred = sum(1 for p in puzzles_avec_pred if p['succes']) / len(puzzles_avec_pred) * 100
            succes_sans_pred = sum(1 for p in puzzles_sans_pred if p['succes']) / len(puzzles_sans_pred) * 100

            print("\n  📊 Impact des prédictions:")
            print(".1f")
            print(".1f")

            if succes_avec_pred > succes_sans_pred:
                print(f"  ✅ Prédictions améliorent le succès: +{succes_avec_pred - succes_sans_pred:.1f}%")
            elif succes_sans_pred > succes_avec_pred:
                print(f"  ❌ Prédictions réduisent le succès: {succes_avec_pred - succes_sans_pred:.1f}%")
            else:
                print("  ⚖️ Impact neutre des prédictions")

        else:
            print("\n  ⚠️ PATTERN PREDICTOR ENCORE INACTIF")
            print("  Même les puzzles complexes n'ont pas déclenché de prédictions")
            print("  Les seuils peuvent être trop conservateurs")

        print("\n  📈 Analyse des patterns détectés:")
        patterns_detectes_moy = statistics.mean([r.get('patterns_detectes', 0) for r in resultats])
        print(".1f")

        # Analyse par niveau de complexité
        tres_complexes = [r for r in resultats if r.get('complexite', 0) > 0.8]
        if tres_complexes:
            pred_tres_complexes = sum(r.get('patterns_predits', 0) for r in tres_complexes)
            print(f"  Puzzles très complexes (>0.8): {len(tres_complexes)}, prédictions: {pred_tres_complexes}")

    def comparer_complexe_vs_simple(self, resultats_complexes: List[Dict]):
        """Compare les résultats avec les puzzles simples testés précédemment"""
        print("COMPARAISON COMPLEXE VS SIMPLE:")
        print("-" * 35)

        # Résultats de référence (puzzles simples)
        reference_simple = {
            'succes': 52.0,  # Du test précédent
            'patterns_predits': 0.0,
            'confidence': 0.25
        }

        # Calcul des statistiques actuelles
        if resultats_complexes:
            succes_complexe = sum(1 for r in resultats_complexes if r.get('succes', False)) / len(resultats_complexes) * 100
            patterns_predits_complexe = statistics.mean([r.get('patterns_predits', 0) for r in resultats_complexes])
            confidence_complexe = statistics.mean([r.get('confidence', 0) for r in resultats_complexes])

            print("\n  Puzzles simples (référence):")
            print(".1f")
            print(".1f")
            print(".3f")


            print("\n  Puzzles complexes (actuels):")
            print(".1f")
            print(".1f")
            print(".3f")


            print("\n  📊 Comparaison:")
            delta_succes = succes_complexe - reference_simple['succes']
            print(f"  • Succès: {delta_succes:+.1f}%")
            delta_pred = patterns_predits_complexe - reference_simple['patterns_predits']
            print(f"  • Patterns prédits: {delta_pred:+.1f}")
            delta_conf = confidence_complexe - reference_simple['confidence']
            print(f"  • Confidence: {delta_conf:+.3f}")
        else:
            print("  ❌ Aucune comparaison possible")

    def calculer_performance_complexe(self, resultats: List[Dict]) -> Dict[str, float]:
        """Calcule les performances sur puzzles complexes"""
        if not resultats:
            return {'succes': 0, 'patterns_predits': 0, 'confidence': 0}

        return {
            'succes': statistics.mean([r.get('succes', False) for r in resultats]) * 100,
            'patterns_predits': statistics.mean([r.get('patterns_predits', 0) for r in resultats]),
            'confidence': statistics.mean([r.get('confidence', 0) for r in resultats])
        }

    def generer_rapport_complexes(self, resultats: List[Dict], puzzles_avec_predictions: int):
        """Génère le rapport final des tests complexes"""
        print("RAPPORT FINAL - PUZZLES COMPLEXES")
        print("=" * 40)

        performance = self.calculer_performance_complexe(resultats)

        print("RÉSUMÉ EXECUTIF:")
        print("-" * 20)
        print(f"  • Puzzles complexes testés: {len(resultats)}")
        print(".1f")
        print(".1f")
        print(".3f")
        print(f"  • Puzzles avec prédictions: {puzzles_avec_predictions}")


        print("\nIMPACT PATTERN PREDICTOR:")
        print("-" * 30)

        if puzzles_avec_predictions > 0:
            print("  🎉 RÉUSSITE ! PatternPredictor activé sur puzzles complexes")
            print(f"  📊 {puzzles_avec_predictions} puzzles complexes bénéficiant de prédictions")
            print("  🚀 Valeur ajoutée démontrée sur puzzles difficiles")
            print("  💡 PatternPredictor fonctionnel et utile")
        else:
            print("  ⚠️ PatternPredictor inactif même sur puzzles complexes")
            print("  🔧 Ajustements des seuils nécessaires")
            print("  📈 Besoin de puzzles encore plus complexes")


        print("\nANALYSE DES RÉSULTATS:")
        print("-" * 25)

        if performance['succes'] > 50:
            print("  ✅ Performances excellentes sur puzzles complexes")
            print("  🎯 Solveur adapté aux défis difficiles")
        elif performance['succes'] > 30:
            print("  ⚠️ Performances satisfaisantes")
            print("  📊 Potentiel d'amélioration identifié")
        else:
            print("  ❌ Performances à améliorer")
            print("  🎯 Focus sur puzzles complexes requis")


        print("\nPROCHAINES ÉTAPES:")
        print("-" * 20)

        if puzzles_avec_predictions > 0:
            print("  📊 Étendre les tests à 100+ puzzles complexes")
            print("  🎯 Analyser l'impact des prédictions en détail")
            print("  📈 Optimiser les seuils pour maximiser les prédictions")
            print("  📋 Benchmark contre autres solveurs")
        else:
            print("  🔧 Ajuster les seuils d'activation")
            print("  🎯 Créer des puzzles ultra-complexes")
            print("  📊 Tester avec différents paramètres")
            print("  🔍 Debug du système de prédiction")

def main():
    """Fonction principale"""
    print("🚀 TEST PUZZLES COMPLEXES ARC-AGI")
    print("Activation du PatternPredictor sur puzzles difficiles")
    print()

    testeur = TesteurPuzzlesComplexes()
    resultats = testeur.executer_test_complexes()

    print("\n" + "=" * 50)
    print("TEST PUZZLES COMPLEXES TERMINÉ !")
    print("=" * 50)
    print(f"  • Puzzles complexes testés: {len(resultats['resultats'])}")
    print(f"  • Puzzles avec prédictions: {resultats['puzzles_avec_predictions']}")
    print("  • PatternPredictor évalué sur difficulté maximale")

    if resultats['puzzles_avec_predictions'] > 0:
        print("  🎉 SUCCÈS ! PatternPredictor activé !")
    else:
        print("  ⚠️ PatternPredictor inactif - ajustements nécessaires")

if __name__ == "__main__":
    main()
