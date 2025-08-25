#!/usr/bin/env python3
"""
Test d'Impact des Optimisations PatternPredictor
Mesure de l'amélioration concrète des performances
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import time

class TesteurImpactOptimisation:
    """Testeur pour mesurer l'impact des optimisations du PatternPredictor"""

    def __init__(self):
        # Architecture avec PatternPredictor optimisé
        self.arch_optimisee = ArchitectureV2()
        self.arch_optimisee.confidence_threshold = 0.35  # Optimisé
        self.arch_optimisee.overfitting_threshold = 0.4  # Optimisé

        # Architecture avec PatternPredictor non optimisé
        self.arch_base = ArchitectureV2()
        self.arch_base.confidence_threshold = 0.5   # Original
        self.arch_base.overfitting_threshold = 0.3  # Original

    def executer_tests_impact(self):
        """Exécute les tests d'impact des optimisations"""
        print("🧪 TEST IMPACT OPTIMISATIONS PATTERN PREDICTOR")
        print("=" * 55)
        print("Objectif: Mesurer l'impact concret des optimisations")
        print()

        # Étape 1: Trouver les puzzles de test
        print("ETAPE 1: PREPARATION DES TESTS")
        print("-" * 35)

        puzzles = self.trouver_puzzles_test()
        print(f"Puzzles trouvés pour les tests: {len(puzzles)}")
        print()

        # Étape 2: Tests avec architecture optimisée
        print("ETAPE 2: TESTS AVEC ARCHITECTURE OPTIMISEE")
        print("-" * 45)

        resultats_optimises = []
        temps_total_optimise = 0

        for i, puzzle_path in enumerate(puzzles[:10], 1):
            puzzle_id = puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', '')
            print(f"[{i:2d}/10] {puzzle_id} - Architecture optimisée...")

            start_time = time.time()
            resultat = self.tester_architecture(self.arch_optimisee, puzzle_path)
            temps = time.time() - start_time
            temps_total_optimise += temps

            if resultat:
                resultats_optimises.append(resultat)
                patterns_predits = resultat.get('patterns_predits', 0)
                succes = "OK" if resultat.get('succes') else "ECHEC"
                print(".2f")
        print()

        # Étape 3: Tests avec architecture de base
        print("ETAPE 3: TESTS AVEC ARCHITECTURE DE BASE")
        print("-" * 42)

        resultats_base = []
        temps_total_base = 0

        for i, puzzle_path in enumerate(puzzles[:10], 1):
            puzzle_id = puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', '')
            print(f"[{i:2d}/10] {puzzle_id} - Architecture de base...")

            start_time = time.time()
            resultat = self.tester_architecture(self.arch_base, puzzle_path)
            temps = time.time() - start_time
            temps_total_base += temps

            if resultat:
                resultats_base.append(resultat)
                patterns_predits = resultat.get('patterns_predits', 0)
                succes = "OK" if resultat.get('succes') else "ECHEC"
                print(".2f")
        print()

        # Étape 4: Analyse comparative
        print("ETAPE 4: ANALYSE COMPARATIVE")
        print("-" * 32)

        self.analyser_impact_optimisations(
            resultats_optimises, resultats_base,
            temps_total_optimise, temps_total_base
        )

        return {
            'optimises': resultats_optimises,
            'base': resultats_base,
            'puzzles_testes': len(puzzles[:10])
        }

    def trouver_puzzles_test(self):
        """Trouve les puzzles pour les tests"""
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

        puzzles_valides = []
        for fichier in fichiers_puzzles[:20]:
            try:
                with open(fichier, 'r') as f:
                    data = json.load(f)
                    if 'train' in data and len(data['train']) > 0:
                        puzzles_valides.append(fichier)
            except:
                continue

        return puzzles_valides if puzzles_valides else []

    def tester_architecture(self, architecture, puzzle_path):
        """Test une architecture sur un puzzle"""
        try:
            with open(puzzle_path, 'r') as f:
                puzzle_data = json.load(f)

            if 'train' not in puzzle_data or len(puzzle_data['train']) == 0:
                return None

            exemple = puzzle_data['train'][0]
            solution = architecture.solve_puzzle(exemple['input'], exemple['output'])

            # Analyse des résultats
            patterns_analysis = solution.get('patterns_analysis', {})
            patterns_predits = solution.get('patterns_predits', {})
            patterns_enrichis = solution.get('patterns_analysis_enrichie', patterns_analysis)

            total_originaux = sum(len(patterns) for patterns in patterns_analysis.values() if isinstance(patterns, dict))
            total_predits = sum(len(patterns) for patterns in patterns_predits.values())
            total_enrichis = sum(len(patterns) for patterns in patterns_enrichis.values() if isinstance(patterns, dict))

            return {
                'puzzle_id': puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', ''),
                'succes': solution.get('confidence', 0) > 0.5,
                'confidence': solution.get('confidence', 0),
                'patterns_originaux': total_originaux,
                'patterns_predits': total_predits,
                'patterns_enrichis': total_enrichis,
                'execution_time': solution.get('execution_time', 0)
            }

        except Exception as e:
            return {
                'puzzle_id': puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', ''),
                'succes': False,
                'erreur': str(e),
                'confidence': 0,
                'patterns_originaux': 0,
                'patterns_predits': 0,
                'patterns_enrichis': 0,
                'execution_time': 0
            }

    def analyser_impact_optimisations(self, optimises, base, temps_opt, temps_base):
        """Analyse l'impact des optimisations"""

        print("RESULTATS GLOBAUX:")
        print("-" * 20)

        if optimises and base:
            # Statistiques générales
            succes_opt = sum(1 for r in optimises if r['succes']) / len(optimises) * 100
            succes_base = sum(1 for r in base if r['succes']) / len(base) * 100

            patterns_predits_opt = sum(r['patterns_predits'] for r in optimises) / len(optimises)
            patterns_predits_base = sum(r['patterns_predits'] for r in base) / len(base)

            temps_moyen_opt = sum(r['execution_time'] for r in optimises) / len(optimises)
            temps_moyen_base = sum(r['execution_time'] for r in base) / len(base)

            print(".1f")
            print(".1f")
            print(".1f")
            print(".1f")
            print(".2f")
            print(".2f")

            print()

            # Analyse détaillée par puzzle
            print("ANALYSE DETAILLEE PAR PUZZLE:")
            print("-" * 35)

            ameliorations = []
            for opt, bas in zip(optimises, base):
                if opt['puzzle_id'] == bas['puzzle_id']:
                    puzzle_id = opt['puzzle_id']
                    diff_patterns = opt['patterns_predits'] - bas['patterns_predits']
                    diff_confiance = opt['confidence'] - bas['confidence']

                    if diff_patterns > 0:
                        ameliorations.append(puzzle_id)
                        print(f"  {puzzle_id}: +{diff_patterns} patterns (+{diff_confiance:.2f} confiance)")
                    elif diff_patterns == 0:
                        print(f"  {puzzle_id}: = stable")
                    else:
                        print(f"  {puzzle_id}: {diff_patterns} patterns")

            print()
            print(f"Puzzles améliorés: {len(ameliorations)}/{len(optimises)} ({len(ameliorations)/len(optimises)*100:.1f}%)")

            print()

            # Conclusion
            print("CONCLUSION - IMPACT DES OPTIMISATIONS:")
            print("-" * 45)

            if patterns_predits_opt > patterns_predits_base:
                print("RESULTAT: AMELIORATION SIGNIFICATIVE !")
                print(".1f")
                print("  - PatternPredictor plus efficace")
                print("  - Plus de patterns détectés")
                print("  - Architecture optimisée fonctionnelle")
            elif patterns_predits_opt == patterns_predits_base:
                print("RESULTAT: STABILITE MAINTENUE")
                print("  - Performances équivalentes")
                print("  - Optimisations équilibrées")
                print("  - Aucune régression observée")
            else:
                print("RESULTAT: AJUSTEMENTS NECESSAIRES")
                print("  - Performances inférieures")
                print("  - Revoir les paramètres")
                print("  - Analyser les causes")

            print()

            # Recommandations
            print("RECOMMANDATIONS:")
            print("-" * 20)
            if patterns_predits_opt > patterns_predits_base:
                print("  1. Continuer avec les paramètres optimisés")
                print("  2. Étendre les tests à plus de puzzles")
                print("  3. Surveiller la stabilité à long terme")
                print("  4. Documenter les améliorations")
            else:
                print("  1. Ajuster les seuils de prédiction")
                print("  2. Analyser les puzzles non améliorés")
                print("  3. Optimiser les modèles de prédiction")
                print("  4. Étendre l'historique d'apprentissage")

        else:
            print("Données insuffisantes pour l'analyse comparative")

def main():
    """Fonction principale"""
    testeur = TesteurImpactOptimisation()
    resultats = testeur.executer_tests_impact()

    print("\n" + "=" * 55)
    print("TEST IMPACT OPTIMISATIONS TERMINES !")
    print("=" * 55)
    print("  - Architecture optimisée testée")
    print("  - Architecture de base comparée")
    print("  - Impact des optimisations mesuré")
    print("  - Recommandations d'amélioration fournies")

if __name__ == "__main__":
    main()
