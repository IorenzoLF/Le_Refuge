#!/usr/bin/env python3
"""
Optimisation des Patterns ARC-Prize 2025
Vérification et optimisation de tous les patterns pour la soumission finale
"""

import json
import os
from typing import Dict, List, Any, Tuple
from solveur_transparent_arc import SolveurTransparentARC

class OptimisateurPatternsARC:
    """Optimise tous les patterns pour la soumission finale"""

    def __init__(self):
        self.solveur = SolveurTransparentARC()
        self.stats_optimisation = {
            'patterns_verifies': 0,
            'patterns_optimises': 0,
            'erreurs_detectees': 0,
            'ameliorations_appliquees': 0
        }

    def charger_puzzles_test(self, n_puzzles: int = 10) -> List[str]:
        """Charge une liste de puzzles pour les tests"""
        # Utiliser les puzzles du dataset d'évaluation comme échantillon
        eval_path = "documentation/arc-agi_evaluation_challenges.json"
        if os.path.exists(eval_path):
            with open(eval_path, 'r') as f:
                eval_data = json.load(f)
            return list(eval_data.keys())[:n_puzzles]
        return []

    def tester_pattern(self, pattern_nom: str, methode_detection: str, methode_application: str,
                      puzzle_ids: List[str]) -> Dict[str, Any]:
        """Test un pattern spécifique sur plusieurs puzzles"""
        print(f"\n TEST PATTERN: {pattern_nom}")
        print("=" * (15 + len(pattern_nom)))

        resultats = {
            'pattern': pattern_nom,
            'succes': 0,
            'echec': 0,
            'erreurs': [],
            'confiance_moyenne': 0.0
        }

        for puzzle_id in puzzle_ids[:5]:  # Limiter pour les tests
            try:
                # Analyser le puzzle
                resultat = self.solveur.analyser_puzzle_complet(puzzle_id)

                if resultat and resultat.pattern_type == pattern_nom:
                    resultats['succes'] += 1
                    resultats['confiance_moyenne'] += resultat.confiance
                else:
                    resultats['echec'] += 1

            except Exception as e:
                resultats['erreurs'].append(f"{puzzle_id}: {str(e)}")
                self.stats_optimisation['erreurs_detectees'] += 1

        if resultats['succes'] > 0:
            resultats['confiance_moyenne'] /= resultats['succes']

        taux_succes = resultats['succes'] / max(1, (resultats['succes'] + resultats['echec']))
        resultats['taux_succes'] = taux_succes

        print(f"Succès: {resultats['succes']}, Échec: {resultats['echec']}")
        print(f"Taux de succès: {taux_succes:.1%}")
        print(f"Confiance moyenne: {resultats['confiance_moyenne']:.1%}")
        if resultats['erreurs']:
            print(f"Erreurs: {len(resultats['erreurs'])}")

        return resultats

    def optimiser_pattern_remplissage_zone(self) -> Dict[str, Any]:
        """Optimise le pattern de remplissage de zones"""
        print("\n OPTIMISATION: Remplissage de Zones")

        # Vérifier les méthodes existent
        if not hasattr(self.solveur, 'detecter_zones_fermees'):
            print(" Méthode detecter_zones_fermees manquante")
            return {'status': 'error', 'message': 'Méthode manquante'}

        if not hasattr(self.solveur, 'remplir_zones_intelligemment'):
            print(" Méthode remplir_zones_intelligemment manquante")
            return {'status': 'error', 'message': 'Méthode manquante'}

        # Tester avec des puzzles connus pour ce pattern
        puzzles_test = ['00d62c1b', '0b148d64', '1e0a9b12']  # Puzzles avec zones fermées
        resultats = self.tester_pattern('remplissage_zone', 'detecter_zones_fermees',
                                      'remplir_zones_intelligemment', puzzles_test)

        if resultats['taux_succes'] < 0.7:
            print("  Performance sous-optimale détectée")
            print(" Suggestions d'amélioration:")
            print("   - Améliorer la détection de contours")
            print("   - Ajouter plus de définitions de 'zone fermée'")
            print("   - Optimiser la logique de confirmation multiple")
            return {'status': 'needs_improvement', 'performance': resultats['taux_succes']}
        else:
            print(" Pattern bien optimisé")
            return {'status': 'optimized', 'performance': resultats['taux_succes']}

    def optimiser_pattern_tetris(self) -> Dict[str, Any]:
        """Optimise le pattern Tetris"""
        print("\n OPTIMISATION: Pattern Tetris")

        if not hasattr(self.solveur, 'detecter_placement_tetris'):
            print(" Méthode detecter_placement_tetris manquante")
            return {'status': 'error', 'message': 'Méthode manquante'}

        puzzles_test = ['1be83260', '0c9aba6e', '0520fde7']
        resultats = self.tester_pattern('tetris_insertion', 'detecter_placement_tetris',
                                      'appliquer_placement_tetris', puzzles_test)

        if resultats['taux_succes'] < 0.8:
            print("  Performance Tetris sous-optimale")
            print(" Suggestions d'amélioration:")
            print("   - Améliorer la simulation de gravité")
            print("   - Optimiser la détection de socles")
            print("   - Ajouter plus de patterns de placement")
            return {'status': 'needs_improvement', 'performance': resultats['taux_succes']}
        else:
            print(" Pattern Tetris optimisé")
            return {'status': 'optimized', 'performance': resultats['taux_succes']}

    def optimiser_pattern_dimensions(self) -> Dict[str, Any]:
        """Optimise la gestion des dimensions dynamiques"""
        print("\n OPTIMISATION: Dimensions Dynamiques")

        if not hasattr(self.solveur, 'calculer_dimensions_dynamiques'):
            print(" Méthode calculer_dimensions_dynamiques manquante")
            return {'status': 'error', 'message': 'Méthode manquante'}

        # Tester sur plusieurs puzzles avec changements de taille
        puzzles_test = ['1be83260', '0a1d4ef5', '1190e5a7']
        resultats = []

        for puzzle_id in puzzles_test:
            try:
                resultat = self.solveur.analyser_puzzle_complet(puzzle_id)
                if resultat and resultat.solution_predite:
                    h_pred, w_pred = len(resultat.solution_predite), len(resultat.solution_predite[0])
                    resultats.append((h_pred, w_pred))
                else:
                    resultats.append(None)
            except:
                resultats.append(None)

        resultats_valides = [r for r in resultats if r is not None]
        taux_succes = len(resultats_valides) / len(resultats)

        if taux_succes < 0.8:
            print("  Calcul des dimensions sous-optimal")
            print(" Suggestions:")
            print("   - Améliorer l'analyse des ratios d'entraînement")
            print("   - Ajouter plus de logique de fallback")
            print("   - Mieux gérer les cas edge")
            return {'status': 'needs_improvement', 'performance': taux_succes}
        else:
            print(" Dimensions dynamiques optimisées")
            return {'status': 'optimized', 'performance': taux_succes}

    def optimiser_systeme_regles_composites(self) -> Dict[str, Any]:
        """Optimise le système de règles composites"""
        print("\n OPTIMISATION: Règles Composites")

        if not hasattr(self.solveur, 'appliquer_systeme_regles_composites'):
            print(" Système de règles composites manquant")
            return {'status': 'error', 'message': 'Système manquant'}

        # Tester la génération de variantes
        test_grille = [[1, 0], [0, 1]]
        try:
            variantes = self.solveur.appliquer_systeme_regles_composites(test_grille, 'test_pattern')
            if variantes:
                print(f" {len(variantes)} variantes générées")
                return {'status': 'optimized', 'variants_count': len(variantes)}
            else:
                print("  Aucune variante générée")
                return {'status': 'needs_improvement', 'variants_count': 0}
        except Exception as e:
            print(f" Erreur système règles composites: {e}")
            return {'status': 'error', 'message': str(e)}

    def executer_optimisation_complete(self):
        """Exécute l'optimisation complète de tous les patterns"""
        print(" OPTIMISATION COMPLETE PATTERNS ARC")
        print("=" * 40)

        # Obtenir des puzzles de test
        puzzles_test = self.charger_puzzles_test(20)
        if not puzzles_test:
            print("  Aucun puzzle de test trouvé")
            return

        print(f" Puzzles de test: {len(puzzles_test)}")

        # Optimiser chaque pattern
        optimisations = []

        # Pattern 1: Remplissage de zones
        opt1 = self.optimiser_pattern_remplissage_zone()
        optimisations.append(('remplissage_zone', opt1))

        # Pattern 2: Tetris
        opt2 = self.optimiser_pattern_tetris()
        optimisations.append(('tetris_insertion', opt2))

        # Pattern 3: Dimensions dynamiques
        opt3 = self.optimiser_pattern_dimensions()
        optimisations.append(('dimensions_dynamiques', opt3))

        # Pattern 4: Règles composites
        opt4 = self.optimiser_systeme_regles_composites()
        optimisations.append(('regles_composites', opt4))

        # Rapport final
        self.generer_rapport_optimisation(optimisations)

    def generer_rapport_optimisation(self, optimisations: List[Tuple[str, Dict[str, Any]]]):
        """Génère un rapport d'optimisation"""
        print("\n RAPPORT FINAL D'OPTIMISATION")
        print("=" * 35)

        optimises = 0
        a_ameliorer = 0
        erreurs = 0

        for pattern_nom, resultat in optimisations:
            status = resultat.get('status', 'unknown')
            performance = resultat.get('performance', 0)

            if status == 'optimized':
                print(f" {pattern_nom}: {performance:.1%} performance")
                optimises += 1
            elif status == 'needs_improvement':
                print(f"  {pattern_nom}: {performance:.1%} performance (amélioration needed)")
                a_ameliorer += 1
            else:
                print(f" {pattern_nom}: {resultat.get('message', 'Erreur')}")
                erreurs += 1

        print(f"\n STATISTIQUES:")
        print(f"   Patterns optimisés: {optimises}")
        print(f"   À améliorer: {a_ameliorer}")
        print(f"   Erreurs: {erreurs}")

        total_patterns = len(optimisations)
        score_global = (optimises * 100 + a_ameliorer * 50) / (total_patterns * 100)

        print(f"\n SCORE GLOBAL: {score_global:.1%}")

        if score_global >= 0.8:
            print(" TOUS LES PATTERNS SONT PRETS POUR LA SOUMISSION!")
        else:
            print("  AMÉLIORATIONS RECOMMANDÉES AVANT SOUMISSION")

    def optimiser_confiance_patterns(self):
        """Optimise la logique de confiance des patterns"""
        print("\n OPTIMISATION: Logique de Confiance")

        # Tester sur des puzzles avec patterns multiples
        puzzles_multiples = ['1be83260', '0b148d64', '0a1d4ef5']

        confiance_totale = 0
        puzzles_testes = 0

        for puzzle_id in puzzles_multiples:
            try:
                resultat = self.solveur.analyser_puzzle_complet(puzzle_id)
                if resultat and resultat.confiance:
                    confiance_totale += resultat.confiance
                    puzzles_testes += 1
                    print(f"   {puzzle_id}: {resultat.confiance:.1%} confiance")
            except Exception as e:
                print(f"   {puzzle_id}: Erreur - {e}")

        if puzzles_testes > 0:
            confiance_moyenne = confiance_totale / puzzles_testes
            print(f" Confiance moyenne: {confiance_moyenne:.1%}")

            if confiance_moyenne >= 0.7:
                print(" Logique de confiance optimisée")
                return {'status': 'optimized', 'confidence': confiance_moyenne}
            else:
                print("  Confiance trop basse - améliorer logique de détection")
                return {'status': 'needs_improvement', 'confidence': confiance_moyenne}
        else:
            print(" Impossible de tester la confiance")
            return {'status': 'error', 'message': 'Aucun test possible'}

def main():
    """Fonction principale d'optimisation"""
    optimiseur = OptimisateurPatternsARC()

    try:
        # Exécuter l'optimisation complète
        optimiseur.executer_optimisation_complete()

        # Optimiser la logique de confiance
        confiance_result = optimiseur.optimiser_confiance_patterns()

        print(f"\n OPTIMISATION TERMINEE!")
        print(f" Patterns vérifiés: {optimiseur.stats_optimisation['patterns_verifies']}")
        print(f" Améliorations appliquées: {optimiseur.stats_optimisation['ameliorations_appliquees']}")
        print(f" Erreurs détectées: {optimiseur.stats_optimisation['erreurs_detectees']}")

    except Exception as e:
        print(f" Erreur lors de l'optimisation: {e}")

if __name__ == "__main__":
    main()
