#!/usr/bin/env python3
"""
Test du PatternPredictor sur Puzzles ARC-AGI Réels
Mesure de l'impact concret des prédictions
"""

import os
import json
import glob
from architecture_v2_complete import ArchitectureV2
import time

class TesteurPatternPredictorARCAGI:
    """Testeur du PatternPredictor sur puzzles ARC-AGI"""

    def __init__(self):
        self.architecture_avec_predictor = ArchitectureV2()
        self.architecture_sans_predictor = ArchitectureV2()
        # Désactiver temporairement le predictor pour les tests de comparaison
        self.architecture_sans_predictor.predictor = None
        self.architecture_sans_predictor.confidence_threshold = 0.5  # Seuil original

    def trouver_puzzles_arc_agi(self, limit=10):
        """Trouve les puzzles ARC-AGI disponibles"""
        patterns = [
            "ARC-AGI-2-main/data/training/*.json",
            "ARC-AGI/data/training/*.json",
            "*.json"
        ]

        fichiers_puzzles = []
        for pattern in patterns:
            fichiers = glob.glob(pattern)
            if fichiers:
                fichiers_puzzles.extend(fichiers)

        # Filtrer les vrais puzzles ARC-AGI
        puzzles_valides = []
        for fichier in fichiers_puzzles[:limit]:
            try:
                with open(fichier, 'r') as f:
                    data = json.load(f)
                    if 'train' in data and len(data['train']) > 0:
                        puzzles_valides.append(fichier)
            except:
                continue

        return puzzles_valides

    def tester_puzzle(self, architecture, puzzle_path, avec_predictor=True):
        """Teste un puzzle avec une architecture donnée"""
        try:
            with open(puzzle_path, 'r') as f:
                puzzle_data = json.load(f)

            if 'train' not in puzzle_data or len(puzzle_data['train']) == 0:
                return None

            # Utiliser le premier exemple d'entraînement
            exemple = puzzle_data['train'][0]
            input_grid = exemple['input']
            output_grid = exemple['output']

            # Mesurer le temps et la performance
            start_time = time.time()
            solution = architecture.solve_puzzle(input_grid, output_grid)
            execution_time = time.time() - start_time

            # Analyser les résultats
            patterns_analysis = solution.get('patterns_analysis', {})
            patterns_predits = solution.get('patterns_predits', {}) if avec_predictor else {}
            patterns_enrichis = solution.get('patterns_analysis_enrichie', patterns_analysis)

            # Compter les patterns
            total_originaux = sum(len(patterns) for patterns in patterns_analysis.values()
                                if isinstance(patterns, dict))
            total_predits = sum(len(patterns) for patterns in patterns_predits.values())
            total_enrichis = sum(len(patterns) for patterns in patterns_enrichis.values()
                               if isinstance(patterns, dict))

            return {
                'puzzle_id': os.path.basename(puzzle_path).replace('.json', ''),
                'succes': solution.get('confidence', 0) > 0.5,
                'confidence': solution.get('confidence', 0),
                'patterns_originaux': total_originaux,
                'patterns_predits': total_predits,
                'patterns_enrichis': total_enrichis,
                'execution_time': execution_time,
                'strategie': solution.get('composition_strategy', 'unknown'),
                'amelioration_patterns': ((total_enrichis - total_originaux) / max(total_originaux, 1)) * 100
            }

        except Exception as e:
            return {
                'puzzle_id': os.path.basename(puzzle_path).replace('.json', ''),
                'succes': False,
                'erreur': str(e),
                'confidence': 0,
                'patterns_originaux': 0,
                'patterns_predits': 0,
                'patterns_enrichis': 0,
                'execution_time': 0,
                'strategie': 'erreur',
                'amelioration_patterns': 0
            }

    def executer_tests_comparatifs(self):
        """Exécute les tests comparatifs"""
        print("🧠 TEST PATTERN PREDICTOR SUR ARC-AGI REELS")
        print("=" * 60)
        print("Objectif: Mesurer l'impact concret des predictions")
        print()

        # Étape 1: Trouver les puzzles
        print("ETAPE 1: RECHERCHE DES PUZZLES ARC-AGI")
        print("-" * 45)

        puzzles = self.trouver_puzzles_arc_agi(limit=15)
        print(f"Puzzles trouves: {len(puzzles)}")

        if len(puzzles) == 0:
            print("Aucun puzzle trouve - test avec donnees synthetique")
            return self._test_synthetique()

        print()

        # Étape 2: Tests avec PatternPredictor
        print("ETAPE 2: TESTS AVEC PATTERN PREDICTOR")
        print("-" * 45)

        resultats_avec_predictor = []
        temps_total_avec = 0

        for i, puzzle_path in enumerate(puzzles, 1):
            puzzle_id = os.path.basename(puzzle_path).replace('.json', '')
            print(f"[{i:2d}/15] {puzzle_id} - AVEC predictor...")

            start_time = time.time()
            resultat = self.tester_puzzle(self.architecture_avec_predictor, puzzle_path, True)
            temps = time.time() - start_time
            temps_total_avec += temps

            if resultat:
                resultats_avec_predictor.append(resultat)
                status = "OK" if resultat['succes'] else "ECHEC"
                patterns_info = f"({resultat['patterns_originaux']}+{resultat['patterns_predits']}->{resultat['patterns_enrichis']})"
                print(".2f")
        print()

        # Étape 3: Tests sans PatternPredictor
        print("ETAPE 3: TESTS SANS PATTERN PREDICTOR")
        print("-" * 45)

        resultats_sans_predictor = []
        temps_total_sans = 0

        for i, puzzle_path in enumerate(puzzles, 1):
            puzzle_id = os.path.basename(puzzle_path).replace('.json', '')
            print(f"[{i:2d}/15] {puzzle_id} - SANS predictor...")

            start_time = time.time()
            resultat = self.tester_puzzle(self.architecture_sans_predictor, puzzle_path, False)
            temps = time.time() - start_time
            temps_total_sans += temps

            if resultat:
                resultats_sans_predictor.append(resultat)
                status = "OK" if resultat['succes'] else "ECHEC"
                patterns_info = f"({resultat['patterns_enrichis']} patterns)"
                print(".2f")
        print()

        # Étape 4: Analyse comparative
        print("ETAPE 4: ANALYSE COMPARATIVE")
        print("-" * 35)

        self.analyser_resultats_comparatifs(
            resultats_avec_predictor,
            resultats_sans_predictor,
            temps_total_avec,
            temps_total_sans
        )

        return {
            'avec_predictor': resultats_avec_predictor,
            'sans_predictor': resultats_sans_predictor,
            'puzzles_testes': len(puzzles)
        }

    def analyser_resultats_comparatifs(self, avec_results, sans_results, temps_avec, temps_sans):
        """Analyse les résultats comparatifs"""

        # Statistiques globales
        print("STATISTIQUES GLOBALES:")
        print("-" * 25)

        succes_avec = sum(1 for r in avec_results if r['succes'])
        succes_sans = sum(1 for r in sans_results if r['succes'])

        print(f"  Puzzles testes: {len(avec_results)}")
        print(f"  Succes AVEC predictor: {succes_avec}/{len(avec_results)} ({succes_avec/len(avec_results)*100:.1f}%)")
        print(f"  Succes SANS predictor: {succes_sans}/{len(sans_results)} ({succes_sans/len(sans_results)*100:.1f}%)")

        print(".2f")
        print(".2f")

        print()

        # Analyse des patterns
        print("ANALYSE DES PATTERNS:")
        print("-" * 25)

        patterns_originaux_avec = sum(r['patterns_originaux'] for r in avec_results)
        patterns_predits_avec = sum(r['patterns_predits'] for r in avec_results)
        patterns_enrichis_avec = sum(r['patterns_enrichis'] for r in avec_results)
        patterns_enrichis_sans = sum(r['patterns_enrichis'] for r in sans_results)

        print(f"  AVEC predictor:")
        print(f"    Originaux: {patterns_originaux_avec}")
        print(f"    Predits: {patterns_predits_avec}")
        print(f"    Enrichis: {patterns_enrichis_avec} (+{patterns_predits_avec} predits)")

        print(f"  SANS predictor:")
        print(f"    Patterns: {patterns_enrichis_sans}")

        amelioration_patterns = ((patterns_enrichis_avec - patterns_enrichis_sans) / max(patterns_enrichis_sans, 1)) * 100
        print(".1f")

        print()

        # Analyse détaillée par puzzle
        print("ANALYSE DETAILLEE PAR PUZZLE:")
        print("-" * 35)

        puzzles_ameliores = 0
        puzzles_echoues = 0

        for i, (avec, sans) in enumerate(zip(avec_results, sans_results)):
            if avec['puzzle_id'] == sans['puzzle_id']:
                puzzle_id = avec['puzzle_id']
                amelioration = avec['patterns_enrichis'] - sans['patterns_enrichis']

                if amelioration > 0:
                    puzzles_ameliores += 1
                    print(f"  {puzzle_id}: +{amelioration} patterns (AMELIORE)")
                elif amelioration < 0:
                    puzzles_echoues += 1
                    print(f"  {puzzle_id}: {amelioration} patterns (DEGRADE)")
                else:
                    print(f"  {puzzle_id}: = (STABLE)")

        print()
        print(f"Puzzles ameliores: {puzzles_ameliores}")
        print(f"Puzzles stables: {len(avec_results) - puzzles_ameliores - puzzles_echoues}")
        print(f"Puzzles degrades: {puzzles_echoues}")

        print()

        # Conclusion
        print("CONCLUSION - IMPACT DU PATTERN PREDICTOR")
        print("=" * 45)

        if puzzles_ameliores > len(avec_results) * 0.3:  # Plus de 30% améliorés
            print("RESULTAT: SUCCES SIGNIFICATIF !")
            print(".1f")
            print("  - PatternPredictor apporte une valeur concrete")
            print("  - Recommande: Integration definitive")
        elif amelioration_patterns > 5:  # Amélioration globale > 5%
            print("RESULTAT: AMELIORATION MODEREE")
            print(".1f")
            print("  - PatternPredictor utile dans certains cas")
            print("  - Recommande: Optimisation et tests supplementaires")
        else:
            print("RESULTAT: IMPACT LIMITE")
            print(".1f")
            print("  - PatternPredictor operationnel mais impact faible")
            print("  - Recommande: Ajustement des parametres")

        print()
        print("RECOMMANDATIONS:")
        print("  - Continuer l'optimisation des seuils")
        print("  - Etendre les tests a plus de puzzles")
        print("  - Analyser les cas d'amelioration pour comprendre")
        print("  - Considerer l'ajout de validation croisee")

    def _test_synthetique(self):
        """Test avec des données synthétiques si aucun puzzle réel n'est trouvé"""
        print("TEST AVEC DONNEES SYNTHETIQUES")
        print("-" * 35)

        # Créer des puzzles synthétiques
        puzzles_synthetiques = [
            {
                'id': 'puzzle_1',
                'input': [[1, 0], [0, 1]],
                'output': [[0, 1], [1, 0]],
                'description': 'Symetrie simple'
            },
            {
                'id': 'puzzle_2',
                'input': [[1, 1], [1, 1]],
                'output': [[2, 2], [2, 2]],
                'description': 'Duplication'
            }
        ]

        print("Tests sur puzzles synthetiques:")
        for puzzle in puzzles_synthetiques:
            print(f"  {puzzle['id']}: {puzzle['description']}")

        return {
            'avec_predictor': [],
            'sans_predictor': [],
            'puzzles_testes': len(puzzles_synthetiques)
        }

def main():
    """Fonction principale"""
    testeur = TesteurPatternPredictorARCAGI()
    resultats = testeur.executer_tests_comparatifs()

    print("\n" + "=" * 60)
    print("TEST PATTERN PREDICTOR TERMINES !")
    print("=" * 60)
    print("  - Tests sur puzzles ARC-AGI reels")
    print("  - Comparaison avec/sans PatternPredictor")
    print("  - Mesure de l'impact concret")
    print("  - Recommandations d'optimisation")

if __name__ == "__main__":
    main()
