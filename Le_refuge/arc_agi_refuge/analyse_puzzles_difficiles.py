#!/usr/bin/env python3
"""
Analyse des Puzzles Difficiles ARC-AGI
Identification et résolution des cas complexes
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import statistics
import time
from typing import Dict, List, Any
from collections import defaultdict

class AnalyseurPuzzlesDifficiles:
    """Analyseur spécialisé pour puzzles difficiles"""

    def __init__(self):
        # Version normale pour identifier les difficultés
        self.solveur_normal = ArchitectureV2()
        self.solveur_normal.confidence_threshold = 0.5  # Seuil normal
        self.solveur_normal.overfitting_threshold = 0.3  # Seuil normal

        # Version ultra-permissive pour PatternPredictor
        self.solveur_predictor = ArchitectureV2()
        self.solveur_predictor.confidence_threshold = 0.01  # Ultra-permissif
        self.solveur_predictor.overfitting_threshold = 0.95  # Ultra-tolérant
        self.solveur_predictor.verbose = False

        self.puzzles_difficiles = []
        self.resultats_comparaison = []

    def executer_analyse_difficiles(self):
        """Exécute l'analyse complète des puzzles difficiles"""
        print("🔍 ANALYSE DES PUZZLES DIFFICILES ARC-AGI")
        print("=" * 50)
        print("Identification des cas complexes et potentiel du PatternPredictor")
        print()

        # Étape 1: Collecte et pré-sélection des puzzles
        print("ETAPE 1: COLLECTE DES PUZZLES CANDIDATS")
        print("-" * 45)

        puzzles_candidats = self.collecter_puzzles_candidats()
        print(f"Puzzles candidats collectés: {len(puzzles_candidats)}")

        # Étape 2: Test avec solveur normal
        print("ETAPE 2: TEST AVEC SOLVEUR NORMAL")
        print("-" * 35)

        puzzles_difficiles = self.identifier_puzzles_difficiles(puzzles_candidats)
        print(f"Puzzles difficiles identifiés: {len(puzzles_difficiles)}")

        # Étape 3: Analyse détaillée des puzzles difficiles
        print("ETAPE 3: ANALYSE DÉTAILLÉE")
        print("-" * 30)

        analyse_detaillee = self.analyser_puzzles_difficiles_detail(puzzles_difficiles)
        self.afficher_analyse_detaillee(analyse_detaillee)
        print()

        # Étape 4: Test avec PatternPredictor activé
        print("ETAPE 4: TEST AVEC PATTERN PREDICTOR")
        print("-" * 40)

        resultats_predictor = self.tester_pattern_predictor(puzzles_difficiles)
        print(f"Tests PatternPredictor terminés: {len(resultats_predictor)} puzzles")
        print()

        # Étape 5: Comparaison et impact
        print("ETAPE 5: COMPARAISON ET IMPACT")
        print("-" * 32)

        impact_predictor = self.comparer_impact_predictor(puzzles_difficiles, resultats_predictor)
        self.afficher_impact_predictor(impact_predictor)
        print()

        # Étape 6: Recommandations
        print("ETAPE 6: RECOMMANDATIONS")
        print("-" * 25)

        recommandations = self.generer_recommandations(analyse_detaillee, impact_predictor)
        self.afficher_recommandations(recommandations)

        return {
            'puzzles_difficiles': puzzles_difficiles,
            'analyse_detaillee': analyse_detaillee,
            'resultats_predictor': resultats_predictor,
            'impact_predictor': impact_predictor,
            'recommandations': recommandations
        }

    def collecter_puzzles_candidats(self) -> List[str]:
        """Collecte les puzzles candidats pour l'analyse"""
        print("  Recherche de puzzles dans toutes les sources...")

        patterns = [
            "ARC-AGI-2-main/data/training/*.json",
            "ARC-AGI/data/training/*.json",
            "*/data/training/*.json",
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

        # Éliminer les doublons et limiter pour performance
        puzzles_uniques = list(set(puzzles))
        puzzles_candidats = puzzles_uniques[:100]  # Limiter à 100 pour analyse

        print(f"  Puzzles uniques trouvés: {len(puzzles_uniques)}")
        print(f"  Puzzles sélectionnés pour analyse: {len(puzzles_candidats)}")

        return puzzles_candidats

    def identifier_puzzles_difficiles(self, puzzles: List[str]) -> List[Dict]:
        """Identifie les puzzles difficiles avec le solveur normal"""
        print("  Test des puzzles avec solveur normal...")

        puzzles_difficiles = []

        for i, puzzle_path in enumerate(puzzles, 1):
            puzzle_id = puzzle_path.split('/')[-1].split('\\')[-1].replace('.json', '')

            try:
                with open(puzzle_path, 'r') as f:
                    puzzle_data = json.load(f)

                if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                    exemple = puzzle_data['train'][0]
                    input_grid = exemple.get('input', [])
                    output_grid = exemple.get('output', [])

                    if input_grid and output_grid:
                        # Test avec solveur normal
                        solution = self.solveur_normal.solve_puzzle(input_grid, output_grid)
                        confidence = solution.get('confidence', 0)
                        succes = confidence > 0.5

                        if not succes:  # Puzzle difficile = échec avec solveur normal
                            complexite = self.estimer_complexite_puzzle_rapide(puzzle_path)

                            puzzle_info = {
                                'path': puzzle_path,
                                'puzzle_id': puzzle_id,
                                'complexite': complexite,
                                'confidence_normal': confidence,
                                'succes_normal': succes,
                                'patterns_detectes_normal': self.compter_patterns(solution.get('patterns_analysis', {}))
                            }

                            puzzles_difficiles.append(puzzle_info)

            except Exception as e:
                print(f"    Erreur avec {puzzle_id}: {e}")

            # Affichage de progression
            if i % 20 == 0:
                print(f"    Progress: {i}/{len(puzzles)} puzzles testés")

        print(f"  Puzzles difficiles trouvés: {len(puzzles_difficiles)}")
        return puzzles_difficiles

    def analyser_puzzles_difficiles_detail(self, puzzles_difficiles: List[Dict]) -> Dict[str, Any]:
        """Analyse détaillée des puzzles difficiles"""
        print("  Analyse détaillée des puzzles difficiles...")

        if not puzzles_difficiles:
            return {'message': 'Aucun puzzle difficile trouvé'}

        # Statistiques de base
        complexites = [p['complexite'] for p in puzzles_difficiles]
        moy_complexite = statistics.mean(complexites)
        med_complexite = statistics.median(complexites)

        # Distribution par niveau de difficulté
        distribution = {'très_facile': 0, 'facile': 0, 'moyen': 0, 'difficile': 0, 'très_difficile': 0}

        for puzzle in puzzles_difficiles:
            comp = puzzle['complexite']
            if comp < 0.2:
                distribution['très_facile'] += 1
            elif comp < 0.4:
                distribution['facile'] += 1
            elif comp < 0.6:
                distribution['moyen'] += 1
            elif comp < 0.8:
                distribution['difficile'] += 1
            else:
                distribution['très_difficile'] += 1

        # Top 5 puzzles les plus difficiles
        puzzles_tries = sorted(puzzles_difficiles, key=lambda x: x['complexite'], reverse=True)
        top_difficiles = puzzles_tries[:5]

        return {
            'total': len(puzzles_difficiles),
            'complexite_moyenne': moy_complexite,
            'complexite_mediane': med_complexite,
            'distribution': distribution,
            'top_difficiles': top_difficiles
        }

    def afficher_analyse_detaillee(self, analyse: Dict[str, Any]):
        """Affiche l'analyse détaillée"""
        print("ANALYSE DÉTAILLÉE DES PUZZLES DIFFICILES:")
        print("-" * 45)

        if 'message' in analyse:
            print(f"  {analyse['message']}")
            return

        print(f"  Total puzzles difficiles: {analyse['total']}")
        print(".2f")
        print(".2f")

        print("\n  DISTRIBUTION PAR DIFFICULTÉ:")
        print("  • Très facile (<0.2):", analyse['distribution']['très_facile'])
        print("  • Facile (0.2-0.4):", analyse['distribution']['facile'])
        print("  • Moyen (0.4-0.6):", analyse['distribution']['moyen'])
        print("  • Difficile (0.6-0.8):", analyse['distribution']['difficile'])
        print("  • Très difficile (>0.8):", analyse['distribution']['très_difficile'])


        print("\n  TOP 5 PUZZLES LES PLUS DIFFICILES:")
        for i, puzzle in enumerate(analyse['top_difficiles'], 1):
            print(f"    {i}. {puzzle['puzzle_id']} - Complexité: {puzzle.get('complexite', 0):.2f}")

    def tester_pattern_predictor(self, puzzles_difficiles: List[Dict]) -> List[Dict]:
        """Test les puzzles difficiles avec PatternPredictor"""
        print("  Test avec PatternPredictor activé...")

        resultats = []

        for i, puzzle in enumerate(puzzles_difficiles, 1):
            puzzle_path = puzzle['path']
            puzzle_id = puzzle['puzzle_id']

            try:
                with open(puzzle_path, 'r') as f:
                    puzzle_data = json.load(f)

                if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                    exemple = puzzle_data['train'][0]
                    input_grid = exemple.get('input', [])
                    output_grid = exemple.get('output', [])

                    if input_grid and output_grid:
                        # Test avec solveur PatternPredictor
                        solution = self.solveur_predictor.solve_puzzle(input_grid, output_grid)
                        confidence = solution.get('confidence', 0)
                        succes = confidence > 0.5

                        patterns_predits = solution.get('patterns_predits', {})
                        total_patterns_predits = sum(len(patterns) for patterns in patterns_predits.values())

                        resultat = {
                            'puzzle_id': puzzle_id,
                            'complexite': puzzle['complexite'],
                            'confidence_normal': puzzle['confidence_normal'],
                            'confidence_predictor': confidence,
                            'succes_normal': puzzle['succes_normal'],
                            'succes_predictor': succes,
                            'patterns_detectes_normal': puzzle['patterns_detectes_normal'],
                            'patterns_predits': total_patterns_predits,
                            'amelioration_confidence': confidence - puzzle['confidence_normal'],
                            'amelioration_succes': succes and not puzzle['succes_normal']
                        }

                        resultats.append(resultat)

            except Exception as e:
                print(f"    Erreur PatternPredictor sur {puzzle_id}: {e}")

            # Progress
            if i % 10 == 0:
                print(f"    Progress PatternPredictor: {i}/{len(puzzles_difficiles)}")

        return resultats

    def comparer_impact_predictor(self, puzzles_difficiles: List[Dict], resultats_predictor: List[Dict]) -> Dict[str, Any]:
        """Compare l'impact du PatternPredictor"""
        print("  Analyse de l'impact du PatternPredictor...")

        if not resultats_predictor:
            return {'message': 'Aucun résultat PatternPredictor'}

        # Statistiques globales
        succes_normal = sum(1 for p in puzzles_difficiles if p['succes_normal']) / len(puzzles_difficiles) * 100
        succes_predictor = sum(1 for r in resultats_predictor if r['succes_predictor']) / len(resultats_predictor) * 100

        ameliorations_succes = [r for r in resultats_predictor if r['amelioration_succes']]
        ameliorations_confidence = [r for r in resultats_predictor if r['amelioration_confidence'] > 0]

        patterns_predits_total = sum(r['patterns_predits'] for r in resultats_predictor)

        return {
            'succes_normal': succes_normal,
            'succes_predictor': succes_predictor,
            'amelioration_succes_count': len(ameliorations_succes),
            'amelioration_confidence_count': len(ameliorations_confidence),
            'patterns_predits_total': patterns_predits_total,
            'puzzles_avec_predictions': sum(1 for r in resultats_predictor if r['patterns_predits'] > 0)
        }

    def afficher_impact_predictor(self, impact: Dict[str, Any]):
        """Affiche l'impact du PatternPredictor"""
        print("IMPACT DU PATTERN PREDICTOR:")
        print("-" * 32)

        if 'message' in impact:
            print(f"  {impact['message']}")
            return

        print(".1f")
        print(".1f")

        if impact['succes_predictor'] > impact['succes_normal']:
            amelioration = impact['succes_predictor'] - impact['succes_normal']
            print("+.1f"        elif impact['succes_predictor'] < impact['succes_normal']:
            degradation = impact['succes_normal'] - impact['succes_predictor']
            print("-.1f"        else:
            print("  ⚖️ Aucun changement dans le taux de succès")

        print(f"  Puzzles avec amélioration de succès: {impact['amelioration_succes_count']}")
        print(f"  Puzzles avec amélioration de confiance: {impact['amelioration_confidence_count']}")
        print(f"  Puzzles avec prédictions: {impact['puzzles_avec_predictions']}")
        print(f"  Total patterns prédits: {impact['patterns_predits_total']}")

        if impact['puzzles_avec_predictions'] > 0:
            
print(""
  🎉 PATTERN PREDICTOR ACTIF SUR PUZZLES DIFFICILES!")
            print("  Le système prédit sur les cas complexes"
        else:
            
print(""
  ⚠️ PATTERN PREDICTOR INACTIF MÊME SUR PUZZLES DIFFICILES")
            print("  Aucune prédiction même avec seuils ultra-permissifs"

    def generer_recommandations(self, analyse: Dict[str, Any], impact: Dict[str, Any]) -> List[Dict]:
        """Génère des recommandations"""
        recommandations = []

        if 'message' not in analyse:
            # Recommandations basées sur l'analyse
            if analyse['complexite_moyenne'] > 0.7:
                recommandations.append({
                    'type': 'complexité',
                    'priorite': 'haute',
                    'action': 'Les puzzles sont très complexes - focus sur simplification'
                })

            if analyse['distribution']['très_difficile'] > 10:
                recommandations.append({
                    'type': 'distribution',
                    'priorite': 'moyenne',
                    'action': 'Beaucoup de puzzles très difficiles - segmentation nécessaire'
                })

        if 'message' not in impact:
            # Recommandations basées sur l'impact
            if impact['puzzles_avec_predictions'] > 0:
                recommandations.append({
                    'type': 'pattern_predictor',
                    'priorite': 'haute',
                    'action': 'PatternPredictor actif - optimiser et étendre'
                })
            else:
                recommandations.append({
                    'type': 'pattern_predictor',
                    'priorite': 'critique',
                    'action': 'PatternPredictor inactif - diagnostic nécessaire'
                })

            if impact['amelioration_succes_count'] > 0:
                recommandations.append({
                    'type': 'amelioration',
                    'priorite': 'haute',
                    'action': 'Améliorations mesurées - analyser les cas réussis'
                })

        # Recommandations générales
        recommandations.append({
            'type': 'general',
            'priorite': 'moyenne',
            'action': 'Collecter plus de puzzles difficiles pour entraînement'
        })

        recommandations.append({
            'type': 'general',
            'priorite': 'moyenne',
            'action': 'Créer des puzzles de test spécifiques pour PatternPredictor'
        })

        return recommandations

    def afficher_recommandations(self, recommandations: List[Dict]):
        """Affiche les recommandations"""
        print("RECOMMANDATIONS:")
        print("-" * 18)

        # Grouper par priorité
        par_priorite = defaultdict(list)
        for rec in recommandations:
            par_priorite[rec['priorite']].append(rec)

        for priorite in ['critique', 'haute', 'moyenne', 'basse']:
            if priorite in par_priorite:
                print(f"\n  {priorite.upper()}:")
                for rec in par_priorite[priorite]:
                    print(f"    • {rec['action']}")

    def estimer_complexite_puzzle_rapide(self, puzzle_path: str) -> float:
        """Estime rapidement la complexité"""
        try:
            with open(puzzle_path, 'r') as f:
                data = json.load(f)

            if 'train' in data and len(data['train']) > 0:
                exemple = data['train'][0]
                input_grid = exemple.get('input', [])
                output_grid = exemple.get('output', [])

                if not input_grid or not output_grid:
                    return 0.5

                taille_input = len(input_grid) * len(input_grid[0]) if input_grid and input_grid[0] else 0
                taille_output = len(output_grid) * len(output_grid[0]) if output_grid and output_grid[0] else 0

                couleurs_uniques = len(set())
                for row in input_grid:
                    if row:
                        couleurs_uniques.update(row)

                ratio_taille = taille_output / taille_input if taille_input > 0 else 1.0

                complexite = (
                    min(taille_input / 150, 1.0) * 0.3 +
                    min(couleurs_uniques / 8, 1.0) * 0.3 +
                    abs(ratio_taille - 1.0) * 0.4
                )

                return min(complexite, 1.0)
        except:
            pass

        return 0.5

    def compter_patterns(self, patterns_analysis: Dict[str, Any]) -> int:
        """Compte le nombre total de patterns détectés"""
        if not patterns_analysis:
            return 0

        total = 0
        for categorie, patterns in patterns_analysis.items():
            if isinstance(patterns, dict):
                total += len(patterns)

        return total

def main():
    """Fonction principale"""
    print("🔍 ANALYSE DES PUZZLES DIFFICILES")
    print("Identification et résolution des cas complexes")
    print()

    analyseur = AnalyseurPuzzlesDifficiles()
    resultats = analyseur.executer_analyse_difficiles()

    print("\n" + "=" * 50)
    print("ANALYSE DES PUZZLES DIFFICILES TERMINÉE !")
    print("=" * 50)
    print(f"  • Puzzles difficiles analysés: {len(resultats.get('puzzles_difficiles', []))}")
    print(f"  • PatternPredictor testé: {len(resultats.get('resultats_predictor', []))}")
    print("  • Recommandations générées pour optimisation")

if __name__ == "__main__":
    main()
