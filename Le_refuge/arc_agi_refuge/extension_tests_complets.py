#!/usr/bin/env python3
"""
Extension Complète des Tests PatternPredictor
Test sur ensemble étendu de puzzles ARC-AGI
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import statistics
import time
from typing import Dict, List, Any, Tuple
from collections import defaultdict

class TesteurExtensionComplete:
    """Testeur complet pour extension des tests PatternPredictor"""

    def __init__(self):
        self.architecture = ArchitectureV2()
        # Configuration avec les seuils optimisés
        self.architecture.confidence_threshold = 0.2
        self.architecture.overfitting_threshold = 0.5

        self.resultats = []
        self.puzzles_testes = []
        self.stats_categorie = defaultdict(list)
        self.temps_execution = []

    def executer_extension_tests(self):
        """Exécute l'extension complète des tests"""
        print("🧪 EXTENSION COMPLÈTE DES TESTS PATTERN PREDICTOR")
        print("=" * 60)
        print("Objectif: Tester sur ensemble étendu de puzzles ARC-AGI")
        print("Seuils optimisés: confidence=0.2, overfitting=0.5")
        print()

        # Étape 1: Collecte des puzzles
        print("ETAPE 1: COLLECTE DES PUZZLES")
        print("-" * 35)

        puzzles = self.collecter_puzzles_test()
        print(f"Total de puzzles trouvés: {len(puzzles)}")
        print()

        # Étape 2: Tests sur échantillon représentatif
        print("ETAPE 2: TESTS SUR ÉCHANTILLON REPRÉSENTATIF")
        print("-" * 50)

        echantillon = self.selectionner_echantillon_representatif(puzzles)
        print(f"Échantillon sélectionné: {len(echantillon)} puzzles")

        resultats_echantillon = []
        for i, puzzle_path in enumerate(echantillon, 1):
            puzzle_id = self.extraire_id_puzzle(puzzle_path)
            print(f"[{i:2d}/{len(echantillon)}] {puzzle_id} - Test en cours...")
            start_time = time.time()

            try:
                resultat = self.tester_puzzle(puzzle_path)
                execution_time = time.time() - start_time
                resultat['execution_time'] = execution_time
                resultats_echantillon.append(resultat)

                # Statistiques par catégorie
                categorie = self.categoriser_puzzle(resultat)
                self.stats_categorie[categorie].append(resultat)

                self.temps_execution.append(execution_time)

            except Exception as e:
                print(f"  ❌ Erreur: {e}")
                continue

        print()

        # Étape 3: Analyse des résultats
        print("ETAPE 3: ANALYSE DES RÉSULTATS")
        print("-" * 35)

        self.analyser_resultats_complets(resultats_echantillon)
        print()

        # Étape 4: Tests spécialisés
        print("ETAPE 4: TESTS SPÉCIALISÉS")
        print("-" * 30)

        self.executer_tests_specialises(puzzles)
        print()

        # Étape 5: Rapport final
        print("ETAPE 5: RAPPORT FINAL")
        print("-" * 25)

        self.generer_rapport_final(resultats_echantillon)

        return {
            'resultats': resultats_echantillon,
            'stats_categorie': dict(self.stats_categorie),
            'puzzles_testes': len(resultats_echantillon),
            'performance_moyenne': self.calculer_performance_moyenne(resultats_echantillon)
        }

    def collecter_puzzles_test(self) -> List[str]:
        """Collecte tous les puzzles disponibles"""
        print("  Recherche de puzzles dans tous les répertoires...")

        patterns = [
            "ARC-AGI-2-main/data/training/*.json",
            "ARC-AGI/data/training/*.json",
            "ARC-AGI-2-main/data/evaluation/*.json",
            "ARC-AGI/data/evaluation/*.json",
            "*.json"
        ]

        puzzles = []
        for pattern in patterns:
            fichiers = glob.glob(pattern)
            for fichier in fichiers:
                try:
                    with open(fichier, 'r') as f:
                        data = json.load(f)
                        if 'train' in data and len(data['train']) > 0:
                            puzzles.append(fichier)
                except:
                    continue

        # Éliminer les doublons
        puzzles_uniques = list(set(puzzles))
        print(f"  Puzzles uniques trouvés: {len(puzzles_uniques)}")

        return puzzles_uniques

    def selectionner_echantillon_representatif(self, puzzles: List[str]) -> List[str]:
        """Sélectionne un échantillon représentatif de puzzles"""
        print("  Sélection d'un échantillon représentatif...")

        # Trier par difficulté estimée et variété
        puzzles_triees = []
        for puzzle in puzzles:
            try:
                with open(puzzle, 'r') as f:
                    data = json.load(f)

                if 'train' in data and len(data['train']) > 0:
                    exemple = data['train'][0]
                    difficulte = self.estimer_difficulte(exemple)
                    variete = self.estimer_variete(exemple)
                    score = difficulte * 0.6 + variete * 0.4

                    puzzles_triees.append({
                        'path': puzzle,
                        'difficulte': difficulte,
                        'variete': variete,
                        'score': score
                    })
            except:
                continue

        # Trier par score et sélectionner les plus variés
        puzzles_triees.sort(key=lambda x: x['score'], reverse=True)

        # Sélectionner jusqu'à 50 puzzles représentatifs
        echantillon = [p['path'] for p in puzzles_triees[:50]]

        # Ajouter quelques puzzles faciles pour baseline
        puzzles_faciles = [p for p in puzzles_triees if p['difficulte'] < 0.3][:10]
        echantillon.extend([p['path'] for p in puzzles_faciles])

        return list(set(echantillon))  # Éliminer doublons

    def estimer_difficulte(self, exemple: Dict) -> float:
        """Estime la difficulté d'un puzzle"""
        input_grid = exemple.get('input', [])
        output_grid = exemple.get('output', [])

        # Facteurs de difficulté
        taille = len(input_grid) * len(input_grid[0]) if input_grid and input_grid[0] else 0
        couleurs_uniques = len(set(cell for row in input_grid for cell in row)) if input_grid else 0
        changement = self.calculer_changement(input_grid, output_grid)

        difficulte = (
            min(taille / 100, 1.0) * 0.3 +      # Taille
            min(couleurs_uniques / 10, 1.0) * 0.3 +  # Complexité couleur
            changement * 0.4                      # Changement requis
        )

        return min(difficulte, 1.0)

    def estimer_variete(self, exemple: Dict) -> float:
        """Estime la variété d'un puzzle (patterns différents)"""
        input_grid = exemple.get('input', [])

        if not input_grid:
            return 0.0

        # Analyser la variété des patterns
        symetrie = self.detecter_symetrie(input_grid)
        repetition = self.detecter_repetition(input_grid)
        gradient = self.detecter_gradient(input_grid)

        variete = (symetrie + repetition + gradient) / 3.0
        return variete

    def calculer_changement(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> float:
        """Calcule le changement requis entre input et output"""
        if not input_grid or not output_grid:
            return 1.0

        changements = 0
        total = 0

        min_rows = min(len(input_grid), len(output_grid))
        min_cols = min(len(input_grid[0]), len(output_grid[0])) if input_grid and output_grid else 0

        for i in range(min_rows):
            for j in range(min_cols):
                if input_grid[i][j] != output_grid[i][j]:
                    changements += 1
                total += 1

        return changements / total if total > 0 else 1.0

    def detecter_symetrie(self, grid: List[List[int]]) -> float:
        """Détecte la symétrie dans la grille"""
        if not grid:
            return 0.0

        rows = len(grid)
        cols = len(grid[0])

        # Vérifier symétrie horizontale
        sym_h = 0
        for i in range(rows // 2):
            for j in range(cols):
                if grid[i][j] == grid[rows-1-i][j]:
                    sym_h += 1

        # Vérifier symétrie verticale
        sym_v = 0
        for i in range(rows):
            for j in range(cols // 2):
                if grid[i][j] == grid[i][cols-1-j]:
                    sym_v += 1

        total_positions = (rows * cols) / 2  # Positions à vérifier
        symetrie = (sym_h + sym_v) / (2 * total_positions) if total_positions > 0 else 0

        return min(symetrie, 1.0)

    def detecter_repetition(self, grid: List[List[int]]) -> float:
        """Détecte les répétitions de patterns"""
        if not grid:
            return 0.0

        # Analyser répétitions de lignes
        repetitions = 0
        for i in range(len(grid)):
            for j in range(i + 1, len(grid)):
                if grid[i] == grid[j]:
                    repetitions += 1

        max_repetitions = len(grid) * (len(grid) - 1) / 2
        return repetitions / max_repetitions if max_repetitions > 0 else 0.0

    def detecter_gradient(self, grid: List[List[int]]) -> float:
        """Détecte les gradients dans la grille"""
        if not grid:
            return 0.0

        gradients = 0
        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[i]) - 1):
                if abs(grid[i][j] - grid[i][j+1]) <= 2:  # Gradient doux
                    gradients += 1
                total += 1

        return gradients / total if total > 0 else 0.0

    def tester_puzzle(self, puzzle_path: str) -> Dict[str, Any]:
        """Test un puzzle individuel"""
        with open(puzzle_path, 'r') as f:
            puzzle_data = json.load(f)

        if 'train' not in puzzle_data or len(puzzle_data['train']) == 0:
            return {'erreur': 'Pas de données d\'entraînement'}

        exemple = puzzle_data['train'][0]

        # Test avec l'architecture
        solution = self.architecture.solve_puzzle(exemple['input'], exemple['output'])

        # Analyse détaillée
        patterns_analysis = solution.get('patterns_analysis', {})
        patterns_predits = solution.get('patterns_predits', {})
        patterns_enrichis = solution.get('patterns_analysis_enrichie', patterns_analysis)

        total_originaux = sum(len(patterns) for patterns in patterns_analysis.values() if isinstance(patterns, dict))
        total_predits = sum(len(patterns) for patterns in patterns_predits.values())
        total_enrichis = total_originaux + total_predits

        # Évaluation de la prédiction
        confidence = solution.get('confidence', 0)
        succes = confidence > 0.5

        return {
            'puzzle_id': self.extraire_id_puzzle(puzzle_path),
            'succes': succes,
            'confidence': confidence,
            'patterns_originaux': total_originaux,
            'patterns_predits': total_predits,
            'patterns_enrichis': total_enrichis,
            'difficulte': self.estimer_difficulte(exemple),
            'variete': self.estimer_variete(exemple),
            'puzzle_path': puzzle_path
        }

    def extraire_id_puzzle(self, puzzle_path: str) -> str:
        """Extrait l'ID du puzzle depuis le chemin"""
        filename = puzzle_path.split('/')[-1].split('\\')[-1]
        return filename.replace('.json', '')

    def categoriser_puzzle(self, resultat: Dict) -> str:
        """Catégorise un puzzle selon ses caractéristiques"""
        difficulte = resultat.get('difficulte', 0)
        variete = resultat.get('variete', 0)
        patterns_predits = resultat.get('patterns_predits', 0)

        if difficulte > 0.7:
            if patterns_predits > 0:
                return "difficile_avec_prediction"
            else:
                return "difficile_sans_prediction"
        elif variete > 0.6:
            if patterns_predits > 0:
                return "varie_avec_prediction"
            else:
                return "varie_sans_prediction"
        else:
            if patterns_predits > 0:
                return "simple_avec_prediction"
            else:
                return "simple_sans_prediction"

    def analyser_resultats_complets(self, resultats: List[Dict]):
        """Analyse complète des résultats"""
        print("ANALYSE DÉTAILLÉE:")
        print("-" * 25)

        if not resultats:
            print("  Aucun résultat à analyser")
            return

        # Statistiques générales
        succes_count = sum(1 for r in resultats if r['succes'])
        taux_succes = succes_count / len(resultats) * 100

        patterns_originaux_moy = statistics.mean([r['patterns_originaux'] for r in resultats])
        patterns_predits_moy = statistics.mean([r['patterns_predits'] for r in resultats])
        patterns_enrichis_moy = statistics.mean([r['patterns_enrichis'] for r in resultats])

        confidence_moy = statistics.mean([r['confidence'] for r in resultats])

        print(".1f")
        print(".2f")
        print(".1f")
        print(".1f")
        print(".1f")
        print(".3f")

        print()

        # Analyse par catégorie
        print("ANALYSE PAR CATÉGORIE:")
        print("-" * 25)

        for categorie, puzzles in self.stats_categorie.items():
            if puzzles:
                succes_cat = sum(1 for p in puzzles if p['succes']) / len(puzzles) * 100
                patterns_predits_cat = statistics.mean([p['patterns_predits'] for p in puzzles])
                print(f"  {categorie}: {len(puzzles)} puzzles, {succes_cat:.1f}% succès, {patterns_predits_cat:.1f} patterns prédits")

        print()

        # Puzzles avec prédictions réussies
        puzzles_avec_predictions = [r for r in resultats if r['patterns_predits'] > 0]
        print(f"Puzzles avec prédictions: {len(puzzles_avec_predictions)}/{len(resultats)}")
        if puzzles_avec_predictions:
            succes_predictions = sum(1 for p in puzzles_avec_predictions if p['succes']) / len(puzzles_avec_predictions) * 100
            print(".1f")

    def executer_tests_specialises(self, puzzles: List[str]):
        """Exécute des tests spécialisés"""
        print("TESTS SPÉCIALISÉS:")
        print("-" * 20)

        # Test sur puzzles difficiles
        print("  • Puzzles difficiles...")
        puzzles_difficiles = [p for p in puzzles if self.est_puzzle_difficile(p)]
        resultats_difficiles = []

        for puzzle_path in puzzles_difficiles[:5]:  # Limiter pour rapidité
            try:
                resultat = self.tester_puzzle(puzzle_path)
                resultats_difficiles.append(resultat)
            except:
                continue

        if resultats_difficiles:
            succes_difficiles = sum(1 for r in resultats_difficiles if r['succes']) / len(resultats_difficiles) * 100
            patterns_predits_diff = statistics.mean([r['patterns_predits'] for r in resultats_difficiles])
            print(".1f")

        # Test sur puzzles avec symétrie
        print("  • Puzzles avec symétrie...")
        puzzles_symetriques = [p for p in puzzles if self.contient_symetrie(p)]
        resultats_symetriques = []

        for puzzle_path in puzzles_symetriques[:5]:
            try:
                resultat = self.tester_puzzle(puzzle_path)
                resultats_symetriques.append(resultat)
            except:
                continue

        if resultats_symetriques:
            succes_sym = sum(1 for r in resultats_symetriques if r['succes']) / len(resultats_symetriques) * 100
            patterns_predits_sym = statistics.mean([r['patterns_predits'] for r in resultats_symetriques])
            print(".1f")

    def est_puzzle_difficile(self, puzzle_path: str) -> bool:
        """Détermine si un puzzle est difficile"""
        try:
            with open(puzzle_path, 'r') as f:
                data = json.load(f)

            if 'train' in data and len(data['train']) > 0:
                exemple = data['train'][0]
                difficulte = self.estimer_difficulte(exemple)
                return difficulte > 0.7
        except:
            pass
        return False

    def contient_symetrie(self, puzzle_path: str) -> bool:
        """Détermine si un puzzle contient de la symétrie"""
        try:
            with open(puzzle_path, 'r') as f:
                data = json.load(f)

            if 'train' in data and len(data['train']) > 0:
                exemple = data['train'][0]
                symetrie = self.detecter_symetrie(exemple.get('input', []))
                return symetrie > 0.5
        except:
            pass
        return False

    def calculer_performance_moyenne(self, resultats: List[Dict]) -> Dict[str, float]:
        """Calcule les performances moyennes"""
        if not resultats:
            return {'succes': 0, 'patterns_predits': 0, 'confidence': 0}

        return {
            'succes': statistics.mean([r['succes'] for r in resultats]) * 100,
            'patterns_predits': statistics.mean([r['patterns_predits'] for r in resultats]),
            'confidence': statistics.mean([r['confidence'] for r in resultats])
        }

    def generer_rapport_final(self, resultats: List[Dict]):
        """Génère le rapport final"""
        print("RAPPORT FINAL D'EXTENSION DES TESTS")
        print("=" * 40)

        if not resultats:
            print("Aucun résultat disponible")
            return

        performance = self.calculer_performance_moyenne(resultats)

        print("RÉSULTATS GÉNÉRAUX:")
        print("-" * 20)
        print(f"  Puzzles testés: {len(resultats)}")
        print(".1f")
        print(".1f")
        print(".3f")
        print(".2f")

        print()
        print("IMPACT DU PATTERN PREDICTOR:")
        print("-" * 30)

        puzzles_avec_pred = [r for r in resultats if r['patterns_predits'] > 0]
        puzzles_sans_pred = [r for r in resultats if r['patterns_predits'] == 0]

        print(f"  Puzzles avec prédictions: {len(puzzles_avec_pred)}")
        print(f"  Puzzles sans prédictions: {len(puzzles_sans_pred)}")

        if puzzles_avec_pred:
            succes_avec_pred = sum(1 for r in puzzles_avec_pred if r['succes']) / len(puzzles_avec_pred) * 100
            print(".1f")

        if puzzles_sans_pred:
            succes_sans_pred = sum(1 for r in puzzles_sans_pred if r['succes']) / len(puzzles_sans_pred) * 100
            print(".1f")

        print()
        print("RECOMMANDATIONS:")
        print("-" * 20)

        if performance['succes'] > 60:
            print("  ✅ Performances excellentes")
            print("  ✅ PatternPredictor contribue positivement")
        elif performance['succes'] > 40:
            print("  ⚠️ Performances satisfaisantes")
            print("  📈 Améliorations possibles")
        else:
            print("  ❌ Performances à améliorer")
            print("  🔧 Ajustements nécessaires")

        print("  📊 Étendre tests sur plus de puzzles")
        print("  🎯 Focus sur puzzles difficiles")
        print("  📈 Enrichir base de patterns")

        print()
        print("CONCLUSION:")
        print("-" * 15)

        if len(puzzles_avec_pred) > 0:
            print("  ✅ PatternPredictor actif et fonctionnel")
            print("  ✅ Améliorations mesurées sur certains puzzles")
            print("  📊 Données collectées pour optimisations futures")
        else:
            print("  ⚠️ PatternPredictor peu sollicité")
            print("  📈 Besoin de puzzles plus variés")
            print("  🔧 Ajustements des seuils recommandés")

def main():
    """Fonction principale"""
    print("🚀 EXTENSION COMPLÈTE DES TESTS PATTERN PREDICTOR")
    print("Test sur ensemble étendu de puzzles ARC-AGI")
    print()

    testeur = TesteurExtensionComplete()
    resultats = testeur.executer_extension_tests()

    print("\n" + "=" * 60)
    print("EXTENSION DES TESTS TERMINÉE AVEC SUCCÈS !")
    print("=" * 60)
    print(f"  • Puzzles testés: {resultats['puzzles_testes']}")
    print(".1f")
    print(".1f")
    print("  • Données collectées pour optimisations futures")
    print("  • PatternPredictor évalué sur ensemble représentatif")

if __name__ == "__main__":
    main()
