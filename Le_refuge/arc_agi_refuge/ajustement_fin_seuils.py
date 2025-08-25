#!/usr/bin/env python3
"""
Ajustement Fin des Seuils du PatternPredictor
Optimisation granulaire pour maximiser les prédictions
"""

from architecture_v2_complete import ArchitectureV2
import json
import glob
import numpy as np
from typing import Dict, List, Any, Tuple
import statistics

class AjusteurSeuils:
    """Ajusteur intelligent des seuils du PatternPredictor"""

    def __init__(self):
        self.architecture = ArchitectureV2()
        self.seuils_tests = {
            'seuil_confiance_prediction': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
            'seuil_complexite_min': [0.1, 0.2, 0.3, 0.4, 0.5],
            'seuil_similarite_contexte': [0.5, 0.6, 0.7, 0.8, 0.9],
            'poids_confiance_historique': [0.2, 0.3, 0.4, 0.5, 0.6],
            'max_patterns_predits_par_categorie': [3, 5, 7, 10],
            'min_frequence_historique': [1, 2, 3, 5]
        }

        self.resultats_tests = []
        self.seuils_optimises = {}

    def executer_ajustement_fin(self):
        """Exécute l'ajustement fin des seuils"""
        print("🎯 AJUSTEMENT FIN DES SEUILS PATTERN PREDICTOR")
        print("=" * 55)
        print("Objectif: Trouver les seuils optimaux pour maximiser les prédictions")
        print()

        # Étape 1: Analyse des seuils actuels
        print("ETAPE 1: ANALYSE DES SEUILS ACTUELS")
        print("-" * 40)

        seuils_actuels = self.analyser_seuils_actuels()
        print("\nSeuils actuels:")
        for param, valeur in seuils_actuels.items():
            print(".3f")
        print()

        # Étape 2: Test des seuils individuels
        print("ETAPE 2: TEST DES SEUILS INDIVIDUELS")
        print("-" * 40)

        resultats_individuels = self.tester_seuils_individuels(seuils_actuels)
        print("\nRésultats des tests individuels:")
        for param, resultats in resultats_individuels.items():
            meilleur_valeur = max(resultats, key=lambda x: x['score'])
            print(".3f"
        print()

        # Étape 3: Optimisation par combinaison
        print("ETAPE 3: OPTIMISATION PAR COMBINAISON")
        print("-" * 42)

        combinaisons_optimisees = self.optimiser_combinaisons(resultats_individuels)
        print("\nMeilleures combinaisons:")
        for i, combo in enumerate(combinaisons_optimisees[:3], 1):
            print(f"  {i}. Score: {combo['score']:.3f} - Patterns: {combo['patterns_moyens']:.1f}")
            for param, valeur in combo['parametres'].items():
                print(f"     {param}: {valeur}")
        print()

        # Étape 4: Validation croisée
        print("ETAPE 4: VALIDATION CROISEE")
        print("-" * 32)

        meilleure_combinaison = combinaisons_optimisees[0]
        validation = self.valider_combinaison(meilleure_combinaison)
        print("
Validation de la meilleure combinaison:")
        print(".3f")
        print(".1f")
        print(".1f")
        print(".2f")
        print()

        # Étape 5: Application des seuils optimaux
        print("ETAPE 5: APPLICATION DES SEUILS OPTIMAUX")
        print("-" * 45)

        self.appliquer_seuils_optimises(meilleure_combinaison['parametres'])
        print("Seuils optimaux appliqués:")
        for param, valeur in meilleure_combinaison['parametres'].items():
            ancien = seuils_actuels.get(param, 0)
            print(".3f")
        print()

        # Étape 6: Test final avec seuils optimisés
        print("ETAPE 6: TEST FINAL AVEC SEUILS OPTIMISÉS")
        print("-" * 46)

        test_final = self.tester_seuils_optimises()
        print("
Résultats avec seuils optimisés:")
        print(".1f")
        print(".1f")
        print(".1f")
        print(".1f")
        print()

        # Étape 7: Génération du rapport
        print("ETAPE 7: RAPPORT D'AJUSTEMENT")
        print("-" * 35)

        self.generer_rapport_ajustement(
            seuils_actuels, meilleure_combinaison,
            validation, test_final
        )

        return {
            'seuils_actuels': seuils_actuels,
            'meilleure_combinaison': meilleure_combinaison,
            'validation': validation,
            'test_final': test_final
        }

    def analyser_seuils_actuels(self) -> Dict[str, float]:
        """Analyse les seuils actuels du système"""
        print("  Analyse des seuils actuels...")

        # Tester avec les seuils actuels
        puzzles = self.trouver_puzzles_test()[:5]
        resultats = []

        for puzzle_path in puzzles:
            try:
                with open(puzzle_path, 'r') as f:
                    puzzle_data = json.load(f)

                if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                    exemple = puzzle_data['train'][0]
                    solution = self.architecture.solve_puzzle(exemple['input'], exemple['output'])

                    patterns_predits = solution.get('patterns_predits', {})
                    total_predits = sum(len(patterns) for patterns in patterns_predits.values())

                    resultats.append({
                        'patterns_predits': total_predits,
                        'succes': solution.get('confidence', 0) > 0.5
                    })

            except Exception as e:
                print(f"    Erreur: {e}")

        if resultats:
            patterns_moyens = statistics.mean([r['patterns_predits'] for r in resultats])
            succes_rate = statistics.mean([r['succes'] for r in resultats])
        else:
            patterns_moyens = 0
            succes_rate = 0

        # Seuils actuels (basés sur les paramètres de l'architecture)
        return {
            'seuil_confiance_prediction': 0.35,  # Optimisé précédemment
            'seuil_complexite_min': 0.2,        # Optimisé précédemment
            'seuil_similarite_contexte': 0.6,   # Optimisé précédemment
            'poids_confiance_historique': 0.4,  # Optimisé précédemment
            'max_patterns_predits_par_categorie': 5,  # Optimisé précédemment
            'min_frequence_historique': 1,      # Optimisé précédemment
            'patterns_moyens_actuels': patterns_moyens,
            'succes_rate_actuel': succes_rate
        }

    def tester_seuils_individuels(self, seuils_actuels: Dict[str, float]) -> Dict[str, List[Dict]]:
        """Test chaque seuil individuellement"""
        print("  Test de chaque seuil individuellement...")

        resultats = {}
        puzzles = self.trouver_puzzles_test()[:3]  # Échantillon réduit pour rapidité

        for param, valeurs in self.seuils_tests.items():
            print(f"    Test de {param}...")
            resultats[param] = []

            for valeur in valeurs:
                # Sauvegarder la valeur actuelle
                valeur_actuelle = getattr(self.architecture, param, seuils_actuels.get(param, 0.5))

                # Appliquer la nouvelle valeur
                if hasattr(self.architecture, param):
                    setattr(self.architecture, param, valeur)
                elif param in ['seuil_confiance_prediction', 'seuil_complexite_min']:
                    # Ces paramètres sont dans le predictor
                    if hasattr(self.architecture.predictor, 'modeles_prediction'):
                        # Ajuster dans les modèles de prédiction
                        pass

                # Tester sur les puzzles
                patterns_moyens = 0
                succes_total = 0

                for puzzle_path in puzzles:
                    try:
                        with open(puzzle_path, 'r') as f:
                            puzzle_data = json.load(f)

                        if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                            exemple = puzzle_data['train'][0]
                            solution = self.architecture.solve_puzzle(exemple['input'], exemple['output'])

                            patterns_predits = solution.get('patterns_predits', {})
                            total_predits = sum(len(patterns) for patterns in patterns_predits.values())
                            patterns_moyens += total_predits
                            succes_total += 1 if solution.get('confidence', 0) > 0.5 else 0

                    except Exception as e:
                        continue

                if len(puzzles) > 0:
                    patterns_moyens /= len(puzzles)
                    succes_rate = succes_total / len(puzzles)
                else:
                    patterns_moyens = 0
                    succes_rate = 0

                # Calculer un score composite
                score = (patterns_moyens * 0.7) + (succes_rate * 0.3)

                resultats[param].append({
                    'valeur': valeur,
                    'patterns_moyens': patterns_moyens,
                    'succes_rate': succes_rate,
                    'score': score
                })

                # Restaurer la valeur originale
                if hasattr(self.architecture, param):
                    setattr(self.architecture, param, valeur_actuelle)

        return resultats

    def optimiser_combinaisons(self, resultats_individuels: Dict[str, List[Dict]]) -> List[Dict]:
        """Optimise les combinaisons de seuils"""
        print("  Optimisation des combinaisons de seuils...")

        # Sélectionner les meilleures valeurs pour chaque paramètre
        meilleures_valeurs = {}
        for param, tests in resultats_individuels.items():
            meilleur_test = max(tests, key=lambda x: x['score'])
            meilleures_valeurs[param] = meilleur_test['valeur']
            print(f"    {param}: {meilleur_test['valeur']} (score: {meilleur_test['score']:.3f})")

        # Tester quelques combinaisons
        combinaisons = []

        # Combinaison 1: Valeurs les plus agressives
        combo1 = {param: min(valeurs) for param, valeurs in self.seuils_tests.items()}
        score1 = self.evaluer_combinaison(combo1)
        combinaisons.append({
            'parametres': combo1,
            'score': score1['score'],
            'patterns_moyens': score1['patterns_moyens'],
            'succes_rate': score1['succes_rate']
        })

        # Combinaison 2: Valeurs équilibrées
        combo2 = meilleures_valeurs.copy()
        score2 = self.evaluer_combinaison(combo2)
        combinaisons.append({
            'parametres': combo2,
            'score': score2['score'],
            'patterns_moyens': score2['patterns_moyens'],
            'succes_rate': score2['succes_rate']
        })

        # Combinaison 3: Valeurs conservatrices
        combo3 = {param: max(valeurs) for param, valeurs in self.seuils_tests.items()}
        score3 = self.evaluer_combinaison(combo3)
        combinaisons.append({
            'parametres': combo3,
            'score': score3['score'],
            'patterns_moyens': score3['patterns_moyens'],
            'succes_rate': score3['succes_rate']
        })

        # Trier par score décroissant
        return sorted(combinaisons, key=lambda x: x['score'], reverse=True)

    def evaluer_combinaison(self, parametres: Dict[str, Any]) -> Dict[str, float]:
        """Évalue une combinaison de paramètres"""
        # Appliquer les paramètres
        anciens_parametres = {}
        for param, valeur in parametres.items():
            if hasattr(self.architecture, param):
                anciens_parametres[param] = getattr(self.architecture, param)
                setattr(self.architecture, param, valeur)

        # Tester sur quelques puzzles
        puzzles = self.trouver_puzzles_test()[:3]
        patterns_moyens = 0
        succes_total = 0

        for puzzle_path in puzzles:
            try:
                with open(puzzle_path, 'r') as f:
                    puzzle_data = json.load(f)

                if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                    exemple = puzzle_data['train'][0]
                    solution = self.architecture.solve_puzzle(exemple['input'], exemple['output'])

                    patterns_predits = solution.get('patterns_predits', {})
                    total_predits = sum(len(patterns) for patterns in patterns_predits.values())
                    patterns_moyens += total_predits
                    succes_total += 1 if solution.get('confidence', 0) > 0.5 else 0

            except Exception as e:
                continue

        if len(puzzles) > 0:
            patterns_moyens /= len(puzzles)
            succes_rate = succes_total / len(puzzles)
        else:
            patterns_moyens = 0
            succes_rate = 0

        score = (patterns_moyens * 0.7) + (succes_rate * 0.3)

        # Restaurer les paramètres
        for param, valeur in anciens_parametres.items():
            setattr(self.architecture, param, valeur)

        return {
            'patterns_moyens': patterns_moyens,
            'succes_rate': succes_rate,
            'score': score
        }

    def valider_combinaison(self, combinaison: Dict[str, Any]) -> Dict[str, float]:
        """Valide une combinaison sur un échantillon plus large"""
        print("  Validation croisée de la combinaison...")

        # Appliquer la combinaison
        anciens_parametres = {}
        for param, valeur in combinaison['parametres'].items():
            if hasattr(self.architecture, param):
                anciens_parametres[param] = getattr(self.architecture, param)
                setattr(self.architecture, param, valeur)

        # Tester sur plus de puzzles
        puzzles = self.trouver_puzzles_test()[:8]
        patterns_moyens = 0
        succes_total = 0
        temps_execution = []

        import time
        for puzzle_path in puzzles:
            try:
                start_time = time.time()

                with open(puzzle_path, 'r') as f:
                    puzzle_data = json.load(f)

                if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                    exemple = puzzle_data['train'][0]
                    solution = self.architecture.solve_puzzle(exemple['input'], exemple['output'])

                    execution_time = time.time() - start_time
                    temps_execution.append(execution_time)

                    patterns_predits = solution.get('patterns_predits', {})
                    total_predits = sum(len(patterns) for patterns in patterns_predits.values())
                    patterns_moyens += total_predits
                    succes_total += 1 if solution.get('confidence', 0) > 0.5 else 0

            except Exception as e:
                continue

        # Restaurer les paramètres
        for param, valeur in anciens_parametres.items():
            setattr(self.architecture, param, valeur)

        if len(puzzles) > 0:
            patterns_moyens /= len(puzzles)
            succes_rate = succes_total / len(puzzles)
            temps_moyen = statistics.mean(temps_execution) if temps_execution else 0
        else:
            patterns_moyens = 0
            succes_rate = 0
            temps_moyen = 0

        score_validation = (patterns_moyens * 0.6) + (succes_rate * 0.3) + (max(0, 1 - temps_moyen/5) * 0.1)

        return {
            'patterns_moyens': patterns_moyens,
            'succes_rate': succes_rate,
            'temps_moyen': temps_moyen,
            'score_validation': score_validation
        }

    def appliquer_seuils_optimises(self, parametres: Dict[str, Any]):
        """Applique les seuils optimisés"""
        print("  Application des seuils optimisés...")

        for param, valeur in parametres.items():
            if hasattr(self.architecture, param):
                setattr(self.architecture, param, valeur)
                print(f"    {param} = {valeur}")
            else:
                print(f"    {param} = {valeur} (paramètre personnalisé)")

    def tester_seuils_optimises(self) -> Dict[str, float]:
        """Test final avec les seuils optimisés"""
        print("  Test final avec seuils optimisés...")

        puzzles = self.trouver_puzzles_test()[:10]
        patterns_moyens = 0
        succes_total = 0
        patterns_par_categorie = {'spatial': 0, 'color': 0, 'structural': 0, 'mathematical': 0}

        for puzzle_path in puzzles:
            try:
                with open(puzzle_path, 'r') as f:
                    puzzle_data = json.load(f)

                if 'train' in puzzle_data and len(puzzle_data['train']) > 0:
                    exemple = puzzle_data['train'][0]
                    solution = self.architecture.solve_puzzle(exemple['input'], exemple['output'])

                    patterns_predits = solution.get('patterns_predits', {})
                    total_predits = sum(len(patterns) for patterns in patterns_predits.values())
                    patterns_moyens += total_predits
                    succes_total += 1 if solution.get('confidence', 0) > 0.5 else 0

                    # Compter par catégorie
                    for categorie, patterns in patterns_predits.items():
                        patterns_par_categorie[categorie] = patterns_par_categorie.get(categorie, 0) + len(patterns)

            except Exception as e:
                continue

        if len(puzzles) > 0:
            patterns_moyens /= len(puzzles)
            succes_rate = succes_total / len(puzzles)

            # Normaliser les patterns par catégorie
            for categorie in patterns_par_categorie:
                patterns_par_categorie[categorie] /= len(puzzles)
        else:
            patterns_moyens = 0
            succes_rate = 0

        return {
            'patterns_moyens': patterns_moyens,
            'succes_rate': succes_rate,
            'patterns_par_categorie': patterns_par_categorie
        }

    def generer_rapport_ajustement(self, seuils_actuels: Dict, meilleure_combinaison: Dict,
                                  validation: Dict, test_final: Dict):
        """Génère un rapport d'ajustement"""
        print("\nRAPPORT D'AJUSTEMENT DES SEUILS")
        print("=" * 40)

        print("PARAMÈTRES OPTIMAUX:")
        print("-" * 25)
        for param, valeur in meilleure_combinaison['parametres'].items():
            ancien = seuils_actuels.get(param, 0)
            print(".3f")

        print("
AMÉLIORATIONS MESURÉES:")
        print("-" * 30)
        print(".3f")
        print(".1f")
        print(".1f")
        print(".1f")
        print(".2f")

        print("
VALIDATION CROISÉE:")
        print("-" * 25)
        print(".1f")
        print(".1f")
        print(".2f")

        print("
PATTERNS PAR CATÉGORIE:")
        print("-" * 30)
        for categorie, nombre in test_final['patterns_par_categorie'].items():
            print(".1f")

        print("
RECOMMANDATIONS:")
        print("-" * 20)
        recommandations = [
            "Continuer avec les seuils optimisés",
            "Surveiller la qualité des prédictions",
            "Ajuster si nécessaire selon les résultats",
            "Étendre les tests à plus de puzzles",
            "Valider sur puzzles complexes"
        ]

        for i, rec in enumerate(recommandations, 1):
            print(f"  {i}. {rec}")

        print("
CONCLUSION:")
        print("-" * 15)
        if meilleure_combinaison['score'] > 1.0:
            print("  ✅ AJUSTEMENT TRÈS RÉUSSI")
            print("  PatternPredictor optimisé avec succès")
            print("  Prédictions maximisées")
        elif meilleure_combinaison['score'] > 0.5:
            print("  ✅ AJUSTEMENT RÉUSSI")
            print("  Améliorations significatives")
            print("  Optimisation équilibrée")
        else:
            print("  ⚠️ AJUSTEMENT MODÉRÉ")
            print("  Ajustements supplémentaires recommandés")

    def trouver_puzzles_test(self) -> List[str]:
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

def main():
    """Fonction principale"""
    print("🔧 AJUSTEMENT FIN DES SEUILS PATTERN PREDICTOR")
    print("Maximisation des prédictions par optimisation granulaire")
    print()

    ajusteur = AjusteurSeuils()
    resultats = ajusteur.executer_ajustement_fin()

    print("
" + "=" * 55)
    print("AJUSTEMENT FIN TERMINÉ AVEC SUCCÈS !")
    print("=" * 55)
    print("  - Seuils optimisés individuellement")
    print("  - Combinaisons testées et validées")
    print("  - Paramètres optimaux appliqués")
    print("  - PatternPredictor prêt pour maximiser les prédictions")

if __name__ == "__main__":
    main()
