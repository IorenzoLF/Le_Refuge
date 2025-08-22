#!/usr/bin/env python3
"""
TEST COMPLET SUR LES 1000 PUZZLES D'ENTRAÎNEMENT ARC-AGI
Évaluation réaliste des performances avant soumission
"""

import json
import os
import time
import random
from typing import Dict, List, Any, Tuple
from solveur_transparent_arc import SolveurTransparentARC, ResultatAnalyse

class Testeur1000Puzzles:
    """Testeur complet sur les 1000 puzzles d'entraînement"""

    def __init__(self):
        self.solveur = SolveurTransparentARC()
        self.resultats = {
            'total_puzzles': 0,
            'succes': 0,
            'echec': 0,
            'erreurs': 0,
            'patterns_detectes': {},
            'temps_total': 0,
            'puzzles_par_pattern': {},
            'erreurs_detaillees': []
        }

    def charger_tous_les_puzzles(self) -> Dict[str, Any]:
        """Charge tous les puzzles d'entraînement"""
        dataset_path = "ARC-AGI-2-main/data/training"

        if not os.path.exists(dataset_path):
            print("Dataset d'entraînement non trouvé!")
            return {}

        puzzles = {}
        fichiers = os.listdir(dataset_path)

        print(f"Chargement de {len(fichiers)} puzzles...")

        for i, fichier in enumerate(fichiers):
            if fichier.endswith('.json'):
                puzzle_id = fichier.replace('.json', '')
                try:
                    with open(os.path.join(dataset_path, fichier), 'r') as f:
                        puzzles[puzzle_id] = json.load(f)

                    if i % 100 == 0:
                        print(f"  Chargé {i+1}/{len(fichiers)} puzzles")

                except Exception as e:
                    print(f"Erreur chargement {puzzle_id}: {e}")

        return puzzles

    def tester_puzzle_rapide(self, puzzle_id: str, puzzle_data: Dict[str, Any]) -> Tuple[bool, str, float]:
        """Test rapide d'un puzzle pour l'évaluation massive"""
        try:
            # Test seulement avec les exemples d'entraînement (pas de prédiction complète)
            analyse = self.solveur.analyser_puzzle_complet(puzzle_id)

            if analyse and analyse.pattern_trouve:
                pattern = analyse.pattern_type
                confiance = analyse.confiance
                return True, pattern, confiance
            else:
                return False, None, 0.0

        except Exception as e:
            self.resultats['erreurs_detaillees'].append(f"{puzzle_id}: {str(e)}")
            return False, None, 0.0

    def executer_test_complet(self):
        """Exécute le test complet sur tous les puzzles"""
        print(" TEST COMPLET SUR 1000 PUZZLES ARC-AGI")
        print("=" * 50)

        # Charger tous les puzzles
        puzzles = self.charger_tous_les_puzzles()

        if not puzzles:
            print(" Aucun puzzle chargé!")
            return

        self.resultats['total_puzzles'] = len(puzzles)
        print(f" {len(puzzles)} puzzles chargés")

        # Tester chaque puzzle
        print("\n Début des tests...")
        debut_total = time.time()

        for i, (puzzle_id, puzzle_data) in enumerate(puzzles.items(), 1):
            if i % 50 == 0:
                progress = (i / len(puzzles)) * 100
                elapsed = time.time() - debut_total
                avg_time = elapsed / i
                remaining = avg_time * (len(puzzles) - i)
                print(f"  {i:3d}/{len(puzzles)} ({progress:5.1f}%) - {elapsed:.0f}s écoulés, ~{remaining:.0f}s restants")

            # Test du puzzle
            succes, pattern, confiance = self.tester_puzzle_rapide(puzzle_id, puzzle_data)

            if succes:
                self.resultats['succes'] += 1
                if pattern:
                    # Compter les patterns
                    if pattern not in self.resultats['patterns_detectes']:
                        self.resultats['patterns_detectes'][pattern] = 0
                    self.resultats['patterns_detectes'][pattern] += 1

                    # Grouper par pattern
                    if pattern not in self.resultats['puzzles_par_pattern']:
                        self.resultats['puzzles_par_pattern'][pattern] = []
                    self.resultats['puzzles_par_pattern'][pattern].append((puzzle_id, confiance))
            else:
                self.resultats['echec'] += 1

        self.resultats['temps_total'] = time.time() - debut_total
        self.afficher_resultats()

    def afficher_resultats(self):
        """Affiche les résultats complets"""
        print(f"\n" + "=" * 60)
        print(" RÉSULTATS TEST 1000 PUZZLES")
        print("=" * 60)

        total = self.resultats['total_puzzles']
        succes = self.resultats['succes']
        echec = self.resultats['echec']
        erreurs = len(self.resultats['erreurs_detaillees'])

        print(f"Total puzzles: {total}")
        print(f"Succès (patterns détectés): {succes} ({succes/total*100:.1f}%)")
        print(f"Échecs (pas de pattern): {echec} ({echec/total*100:.1f}%)")
        print(f"Erreurs de code: {erreurs}")
        print(f"Temps total: {self.resultats['temps_total']:.1f} secondes")
        print(f"Temps moyen par puzzle: {self.resultats['temps_total']/total*1000:.1f} ms")

        # Analyse des patterns
        print(f"\n ANALYSE DES PATTERNS DÉTECTÉS")
        print("-" * 40)

        patterns = self.resultats['patterns_detectes']
        if patterns:
            # Trier par fréquence
            patterns_tries = sorted(patterns.items(), key=lambda x: x[1], reverse=True)

            for pattern, count in patterns_tries:
                percentage = count / succes * 100
                print(f"{pattern:20s}: {count:3d} ({percentage:5.1f}%)")

                # Analyser la confiance moyenne pour ce pattern
                if pattern in self.resultats['puzzles_par_pattern']:
                    confiances = [conf for _, conf in self.resultats['puzzles_par_pattern'][pattern]]
                    if confiances:
                        conf_moyenne = sum(confiances) / len(confiances)
                        print(f"{'':20s}    Confiance moyenne: {conf_moyenne:.1%}")

        # Puzzles non couverts
        print(f"\n PUZZLES NON COUVERTS ({echec} puzzles)")
        print("-" * 40)

        if echec > 0:
            print(f"Pourcentage non couvert: {echec/total*100:.1f}%")

            # Échantillon d'erreurs si trop nombreuses
            if erreurs > 0 and erreurs <= 10:
                print(f"Erreurs de code ({erreurs}):")
                for erreur in self.resultats['erreurs_detaillees']:
                    print(f"  - {erreur}")
            elif erreurs > 10:
                print(f"Erreurs de code ({erreurs}) - trop nombreuses pour lister")

        # Évaluation pour ARC-Prize
        print(f"\n ÉVALUATION ARC-PRIZE 2025")
        print("-" * 40)

        score_estime = succes / total * 100
        print(f"Score estimé: {score_estime:.1f}%")

        if score_estime >= 85:
            print(" POTENTIEL GRAND PRIX ($700K)!")
            print("   Score suffisant pour les 85% requis")
        elif score_estime >= 50:
            print(" PARTICIPATION VALIDE")
            print("   Score suffisant pour participer")
        else:
            print("  AMÉLIORATIONS NÉCESSAIRES")
            print("   Score insuffisant pour être compétitif")

        # Recommandations
        print(f"\n RECOMMANDATIONS")
        print("-" * 20)

        if echec > 0:
            print(f"1. Analyser les {echec} puzzles non couverts")
            print("2. Identifier les patterns manquants")
            print("3. Implémenter les nouveaux patterns")

        if erreurs > 0:
            print(f"4. Corriger les {erreurs} erreurs de code")
            print("5. Améliorer la robustesse du solveur")

        if score_estime < 85:
            print("6. Optimiser les patterns existants")
            print("7. Améliorer la détection de patterns")

        print(f"\n⏱  PROCHAINES ÉTAPES:")
        if score_estime >= 50:
            print(" Prêt pour tests supplémentaires")
        else:
            print(" Améliorations urgentes requises")

    def sauvegarder_resultats(self, filename: str = "resultats_test_1000.json"):
        """Sauvegarde les résultats complets"""
        resultats_sauvegarde = {
            'resume': {
                'total_puzzles': self.resultats['total_puzzles'],
                'succes': self.resultats['succes'],
                'echec': self.resultats['echec'],
                'erreurs': len(self.resultats['erreurs_detaillees']),
                'score_pourcentage': self.resultats['succes'] / self.resultats['total_puzzles'] * 100,
                'temps_total_secondes': self.resultats['temps_total']
            },
            'patterns_detectes': self.resultats['patterns_detectes'],
            'erreurs_detaillees': self.resultats['erreurs_detaillees'][:50]  # Limiter pour éviter fichier trop gros
        }

        with open(filename, 'w') as f:
            json.dump(resultats_sauvegarde, f, indent=2)

        print(f" Résultats sauvegardés dans {filename}")

def main():
    """Fonction principale"""
    print(" LANCEMENT TEST COMPLET 1000 PUZZLES")
    print("  Cette opération peut prendre plusieurs minutes...")

    testeur = Testeur1000Puzzles()

    try:
        testeur.executer_test_complet()
        testeur.sauvegarder_resultats()

    except KeyboardInterrupt:
        print("\n⏹  Test interrompu par l'utilisateur")
        testeur.afficher_resultats()
        testeur.sauvegarder_resultats("resultats_test_interrompu.json")

    except Exception as e:
        print(f"\n Erreur fatale: {e}")
        testeur.sauvegarder_resultats("resultats_test_erreur.json")

if __name__ == "__main__":
    main()
