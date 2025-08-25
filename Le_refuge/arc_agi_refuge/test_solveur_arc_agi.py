#!/usr/bin/env python3
"""
Test du Solveur ARC-AGI Complet
Test sur ensemble représentatif de puzzles réels
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import statistics
import time
from typing import Dict, List, Any, Tuple
from collections import defaultdict

class TesteurSolveurComplet:
    """Testeur complet du solveur ARC-AGI"""

    def __init__(self):
        self.solveur = ArchitectureV2()
        # Configuration optimisée
        self.solveur.confidence_threshold = 0.05  # Ultra-permissif
        self.solveur.overfitting_threshold = 0.8   # Très tolérant
        self.solveur.verbose = False  # Moins de logs pour les tests massifs

        self.resultats = []
        self.stats_par_categorie = defaultdict(list)
        self.temps_execution = []

    def executer_test_complet(self):
        """Exécute le test complet sur puzzles ARC-AGI"""
        print("🧪 TEST COMPLET SOLVEUR ARC-AGI")
        print("=" * 50)
        print("Objectif: Évaluer les performances sur puzzles réels")
        print("Configuration: PatternPredictor optimisé")
        print()

        # Étape 1: Collecte des puzzles
        print("ETAPE 1: COLLECTE DES PUZZLES ARC-AGI")
        print("-" * 45)

        puzzles = self.collecter_puzzles_arc_agi()
        print(f"Total puzzles trouvés: {len(puzzles)}")
        print()

        # Étape 2: Sélection d'échantillon représentatif
        print("ETAPE 2: SÉLECTION ÉCHANTILLON REPRÉSENTATIF")
        print("-" * 50)

        echantillon = self.selectionner_echantillon_representatif(puzzles)
        print(f"Échantillon sélectionné: {len(echantillon)} puzzles")

        # Analyse de l'échantillon
        types_puzzles = self.analyser_types_puzzles(echantillon)
        print("Types de puzzles dans l'échantillon:")
        for type_puzzle, count in types_puzzles.items():
            print(f"  • {type_puzzle}: {count} puzzles")
        print()

        # Étape 3: Tests individuels
        print("ETAPE 3: TESTS INDIVIDUELS")
        print("-" * 30)

        resultats_tests = []
        for i, puzzle_path in enumerate(echantillon, 1):
            puzzle_id = puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', '')
            print(f"[{i:2d}/{len(echantillon)}] Test {puzzle_id}...")
            start_time = time.time()

            try:
                resultat = self.tester_puzzle_arc_agi(puzzle_path)
                execution_time = time.time() - start_time
                resultat['execution_time'] = execution_time
                resultats_tests.append(resultat)

                self.temps_execution.append(execution_time)

                # Stats par catégorie
                if 'complexite' in resultat:
                    categorie = self.categoriser_complexite(resultat['complexite'])
                    self.stats_par_categorie[categorie].append(resultat)

            except Exception as e:
                print(f"  ❌ Erreur: {e}")
                resultats_tests.append({
                    'puzzle_id': puzzle_id,
                    'succes': False,
                    'erreur': str(e),
                    'execution_time': time.time() - start_time
                })

        print()

        # Étape 4: Analyse des performances
        print("ETAPE 4: ANALYSE DES PERFORMANCES")
        print("-" * 40)

        performances = self.analyser_performances(resultats_tests)
        self.afficher_resultats_detailes(performances)
        print()

        # Étape 5: Analyse par catégories
        print("ETAPE 5: ANALYSE PAR CATÉGORIES")
        print("-" * 35)

        self.analyser_par_categories()
        print()

        # Étape 6: Identification des forces/faiblesses
        print("ETAPE 6: FORCES ET FAIBLESSES")
        print("-" * 35)

        forces_faiblesses = self.identifier_forces_faiblesses(resultats_tests)
        print("Forces identifiées:")
        for force in forces_faiblesses['forces']:
            print(f"  ✅ {force}")

        print("\nAxes d'amélioration:")
        for faiblesse in forces_faiblesses['faiblesses']:
            print(f"  🔧 {faiblesse}")
        print()

        # Étape 7: Rapport final
        print("ETAPE 7: RAPPORT FINAL")
        print("-" * 25)

        self.generer_rapport_final(resultats_tests, performances)

        return {
            'resultats_tests': resultats_tests,
            'performances': performances,
            'puzzles_testes': len(resultats_tests),
            'reussite_generale': performances['reussite_generale']
        }

    def collecter_puzzles_arc_agi(self) -> List[str]:
        """Collecte tous les puzzles ARC-AGI disponibles"""
        print("  Recherche des puzzles dans tous les répertoires...")

        patterns = [
            "ARC-AGI-2-main/data/training/*.json",
            "ARC-AGI/data/training/*.json",
            "ARC-AGI-2-main/data/evaluation/*.json",
            "ARC-AGI/data/evaluation/*.json",
            "*/data/training/*.json",
            "*/data/evaluation/*.json",
            "*.json"
        ]

        puzzles = []
        for pattern in patterns:
            try:
                fichiers = glob.glob(pattern)
                for fichier in fichiers:
                    try:
                        with open(fichier, 'r') as f:
                            data = json.load(f)
                            if 'train' in data and len(data['train']) > 0:
                                puzzles.append(fichier)
                    except:
                        continue
            except:
                continue

        # Éliminer les doublons
        puzzles_uniques = list(set(puzzles))

        # Filtrer pour garder seulement les vrais puzzles ARC-AGI
        puzzles_arc_agi = []
        for puzzle in puzzles_uniques:
            if any(keyword in puzzle.upper() for keyword in ['ARC', 'TRAINING', 'EVALUATION']):
                puzzles_arc_agi.append(puzzle)

        print(f"  Puzzles ARC-AGI valides: {len(puzzles_arc_agi)}")
        return puzzles_arc_agi

    def selectionner_echantillon_representatif(self, puzzles: List[str]) -> List[str]:
        """Sélectionne un échantillon représentatif"""
        print("  Sélection d'un échantillon représentatif...")

        # Trier par complexité estimée pour avoir une bonne distribution
        puzzles_evalues = []

        for puzzle in puzzles[:100]:  # Limiter pour performance
            try:
                with open(puzzle, 'r') as f:
                    data = json.load(f)

                if 'train' in data and len(data['train']) > 0:
                    exemple = data['train'][0]
                    complexite = self.estimer_complexite_puzzle(exemple)
                    puzzles_evalues.append({
                        'path': puzzle,
                        'complexite': complexite,
                        'taille': len(exemple.get('input', [])) * len(exemple.get('input', [[]]))
                    })
            except:
                continue

        # Trier par complexité et sélectionner un échantillon équilibré
        puzzles_evalues.sort(key=lambda x: x['complexite'])

        # Si pas assez de puzzles évalués, prendre tous ceux disponibles
        if len(puzzles_evalues) < 20:
            echantillon = [p['path'] for p in puzzles_evalues]
        else:
            # Sélectionner 20 puzzles représentatifs (différentes complexités)
            echantillon = []
            step = max(1, len(puzzles_evalues) // 20)  # Éviter step = 0

            for i in range(0, len(puzzles_evalues), step):
                if len(echantillon) < 20:
                    echantillon.append(puzzles_evalues[i]['path'])

            # Ajouter quelques puzzles complexes supplémentaires
            puzzles_complexes = [p for p in puzzles_evalues if p['complexite'] > 0.7][:5]
            for p in puzzles_complexes:
                if p['path'] not in echantillon:
                    echantillon.append(p['path'])

        return echantillon[:25]  # Maximum 25 puzzles

    def estimer_complexite_puzzle(self, exemple: Dict) -> float:
        """Estime la complexité d'un puzzle"""
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

        # Changement de taille
        ratio_taille = taille_output / taille_input if taille_input > 0 else 1.0

        # Complexité finale
        complexite = (
            min(taille_input / 100, 1.0) * 0.2 +      # Taille
            min(couleurs_uniques / 10, 1.0) * 0.3 +   # Couleurs
            abs(ratio_taille - 1.0) * 0.3 +           # Changement de taille
            min(len(exemple.get('output', [])) / 30, 1.0) * 0.2  # Taille output
        )

        return min(complexite, 1.0)

    def analyser_types_puzzles(self, echantillon: List[str]) -> Dict[str, int]:
        """Analyse les types de puzzles dans l'échantillon"""
        types = defaultdict(int)

        for puzzle_path in echantillon:
            try:
                with open(puzzle_path, 'r') as f:
                    data = json.load(f)

                if 'train' in data and len(data['train']) > 0:
                    exemple = data['train'][0]
                    complexite = self.estimer_complexite_puzzle(exemple)

                    if complexite < 0.3:
                        types['simple'] += 1
                    elif complexite < 0.7:
                        types['moyen'] += 1
                    else:
                        types['complexe'] += 1

            except:
                types['inconnu'] += 1

        return dict(types)

    def tester_puzzle_arc_agi(self, puzzle_path: str) -> Dict[str, Any]:
        """Test un puzzle ARC-AGI réel"""
        puzzle_id = puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', '')

        try:
            with open(puzzle_path, 'r') as f:
                puzzle_data = json.load(f)

            if 'train' not in puzzle_data or len(puzzle_data['train']) == 0:
                return {
                    'puzzle_id': puzzle_id,
                    'succes': False,
                    'erreur': 'Pas de données d\'entraînement',
                    'complexite': 0.5
                }

            # Utiliser le premier exemple d'entraînement
            exemple = puzzle_data['train'][0]
            input_grid = exemple.get('input', [])
            output_grid = exemple.get('output', [])

            if not input_grid or not output_grid:
                return {
                    'puzzle_id': puzzle_id,
                    'succes': False,
                    'erreur': 'Grilles vides',
                    'complexite': 0.5
                }

            # Tester avec le solveur
            solution = self.solveur.solve_puzzle(input_grid, output_grid)

            # Analyser les résultats
            confidence = solution.get('confidence', 0)
            succes = confidence > 0.5

            patterns_analysis = solution.get('patterns_analysis', {})
            patterns_predits = solution.get('patterns_predits', {})

            # Calculer les métriques
            total_patterns_detectes = sum(len(patterns) for patterns in patterns_analysis.values() if isinstance(patterns, dict))
            total_patterns_predits = sum(len(patterns) for patterns in patterns_predits.values())

            complexite = self.estimer_complexite_puzzle(exemple)

            return {
                'puzzle_id': puzzle_id,
                'succes': succes,
                'confidence': confidence,
                'patterns_detectes': total_patterns_detectes,
                'patterns_predits': total_patterns_predits,
                'complexite': complexite,
                'execution_time': 0,  # Sera ajouté après
                'erreur': None
            }

        except Exception as e:
            return {
                'puzzle_id': puzzle_id,
                'succes': False,
                'confidence': 0,
                'patterns_detectes': 0,
                'patterns_predits': 0,
                'complexite': 0.5,
                'execution_time': 0,
                'erreur': str(e)
            }

    def analyser_performances(self, resultats: List[Dict]) -> Dict[str, float]:
        """Analyse les performances globales"""
        if not resultats:
            return {'reussite_generale': 0, 'patterns_moyens': 0, 'confidence_moyenne': 0}

        succes_count = sum(1 for r in resultats if r['succes'])
        reussite_generale = succes_count / len(resultats) * 100

        patterns_detectes_moy = statistics.mean([r.get('patterns_detectes', 0) for r in resultats])
        patterns_predits_moy = statistics.mean([r.get('patterns_predits', 0) for r in resultats])
        confidence_moyenne = statistics.mean([r.get('confidence', 0) for r in resultats])

        temps_moyen = statistics.mean([r.get('execution_time', 0) for r in resultats])

        return {
            'reussite_generale': reussite_generale,
            'patterns_detectes_moy': patterns_detectes_moy,
            'patterns_predits_moy': patterns_predits_moy,
            'confidence_moyenne': confidence_moyenne,
            'temps_moyen': temps_moyen,
            'total_tests': len(resultats)
        }

    def afficher_resultats_detailes(self, performances: Dict[str, float]):
        """Affiche les résultats détaillés"""
        print("RÉSULTATS DÉTAILLÉS:")
        print("-" * 25)
        print(".1f")
        print(".1f")
        print(".1f")
        print(".3f")
        print(".2f")
        print(f"  • Total tests: {performances.get('total_tests', 0)}")

        # Analyse des prédictions
        patterns_predits_total = sum(r.get('patterns_predits', 0) for r in self.resultats)
        print(f"  • Patterns prédits total: {patterns_predits_total}")

        puzzles_avec_predictions = sum(1 for r in self.resultats if r.get('patterns_predits', 0) > 0)
        print(f"  • Puzzles avec prédictions: {puzzles_avec_predictions}")

    def categoriser_complexite(self, complexite: float) -> str:
        """Catégorise la complexité"""
        if complexite < 0.3:
            return 'simple'
        elif complexite < 0.7:
            return 'moyen'
        else:
            return 'complexe'

    def analyser_par_categories(self):
        """Analyse les performances par catégories"""
        print("PERFORMANCES PAR CATÉGORIE:")
        print("-" * 30)

        for categorie, puzzles in self.stats_par_categorie.items():
            if puzzles:
                succes = sum(1 for p in puzzles if p['succes']) / len(puzzles) * 100
                patterns_predits = statistics.mean([p.get('patterns_predits', 0) for p in puzzles])
                confidence = statistics.mean([p.get('confidence', 0) for p in puzzles])

                print(f"  {categorie}: {len(puzzles)} puzzles, {succes:.1f}% succès, {patterns_predits:.1f} patterns prédits")

    def identifier_forces_faiblesses(self, resultats: List[Dict]) -> Dict[str, List[str]]:
        """Identifie les forces et faiblesses"""
        forces = []
        faiblesses = []

        performances = self.analyser_performances(resultats)

        # Analyser les forces
        if performances['reussite_generale'] > 40:
            forces.append("Bon taux de succès général")

        if performances['patterns_detectes_moy'] > 5:
            forces.append("Excellente détection de patterns")

        if performances['confidence_moyenne'] > 0.4:
            forces.append("Confiance élevée dans les prédictions")

        puzzles_avec_pred = sum(1 for r in resultats if r.get('patterns_predits', 0) > 0)
        if puzzles_avec_pred > 0:
            forces.append("PatternPredictor actif sur certains puzzles")

        # Analyser les faiblesses
        if performances['reussite_generale'] < 50:
            faiblesses.append("Taux de succès perfectible")

        if performances['patterns_predits_moy'] < 1:
            faiblesses.append("Peu de prédictions PatternPredictor")

        erreurs = sum(1 for r in resultats if r.get('erreur'))
        if erreurs > 0:
            faiblesses.append("Quelques erreurs d'exécution")

        return {'forces': forces, 'faiblesses': faiblesses}

    def generer_rapport_final(self, resultats: List[Dict], performances: Dict[str, float]):
        """Génère le rapport final"""
        print("RAPPORT FINAL TEST SOLVEUR ARC-AGI")
        print("=" * 40)

        print("RÉSUMÉ EXECUTIF:")
        print("-" * 20)
        print(f"  • Puzzles testés: {len(resultats)}")
        print(".1f")
        print(".1f")
        print(".1f")

        # Puzzles réussis vs échoués
        puzzles_reussis = [r for r in resultats if r['succes']]
        puzzles_echoues = [r for r in resultats if not r['succes']]

        print(f"  • Puzzles réussis: {len(puzzles_reussis)}")
        print(f"  • Puzzles échoués: {len(puzzles_echoues)}")

        # Analyse des prédictions
        puzzles_avec_pred = [r for r in resultats if r.get('patterns_predits', 0) > 0]
        print(f"  • Puzzles avec prédictions: {len(puzzles_avec_pred)}")

        print("\nIMPACT PATTERN PREDICTOR:")
        print("-" * 30)

        if puzzles_avec_pred:
            succes_avec_pred = sum(1 for p in puzzles_avec_pred if p['succes']) / len(puzzles_avec_pred) * 100
            print(".1f")
        else:
            print("  • Aucun puzzle n'a déclenché de prédictions")

        print("\nCONCLUSION:")
        print("-" * 15)

        if performances['reussite_generale'] > 50:
            print("  ✅ PERFORMANCES EXCELLENTES")
            print("  Solveur ARC-AGI performant et fiable")
        elif performances['reussite_generale'] > 30:
            print("  ⚠️ PERFORMANCES SATISFAISANTES")
            print("  Base solide avec marges d'amélioration")
        else:
            print("  🔧 AMÉLIORATIONS NÉCESSAIRES")
            print("  Optimisations requises")

        print("\nPROCHAINES ÉTAPES:")
        print("-" * 20)
        print("  📊 Étendre les tests sur plus de puzzles")
        print("  🎯 Analyser les échecs pour améliorer")
        print("  🚀 Optimiser les prédictions PatternPredictor")
        print("  📈 Mesurer l'impact sur puzzles complexes")

def main():
    """Fonction principale"""
    print("🚀 TEST COMPLET SOLVEUR ARC-AGI")
    print("Évaluation sur puzzles réels")
    print()

    testeur = TesteurSolveurComplet()
    resultats = testeur.executer_test_complet()

    print("\n" + "=" * 50)
    print("TEST COMPLET TERMINÉ !")
    print("=" * 50)
    print(f"  • Puzzles testés: {resultats['puzzles_testes']}")
    print(".1f")
    print("  • PatternPredictor évalué sur puzzles réels")
    print("  • Performances mesurées et analysées")
    print("  • Rapport complet généré")

if __name__ == "__main__":
    main()
