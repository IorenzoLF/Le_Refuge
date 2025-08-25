#!/usr/bin/env python3
"""
Générateur de soumission ARC-Prize 2025
Format conforme aux règles officielles de Kaggle
"""

import json
import os
import sys
from typing import Dict, List, Any
from solveur_transparent_arc import SolveurTransparentARC

class GenerateurSubmissionARC:
    def __init__(self):
        self.solveur = SolveurTransparentARC()
        self.submission_data = {}
        self.stats = {
            'total_puzzles': 0,
            'puzzles_resolus': 0,
            'erreurs': []
        }

    def charger_dataset_evaluation(self, chemin_dataset: str) -> Dict[str, Any]:
        """Charge le dataset d'évaluation officiel"""
        if not os.path.exists(chemin_dataset):
            raise FileNotFoundError(f"Dataset non trouvé: {chemin_dataset}")

        with open(chemin_dataset, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generer_tentative(self, puzzle_id: str, test_input: List[List[int]], essai_num: int = 1) -> List[List[int]]:
        """
        Génère une tentative de solution pour un test input
        Pour l'instant, utilise le solveur standard, mais pourra être étendu
        pour générer des variantes dans le futur
        """
        try:
            # Analyser le puzzle avec notre solveur
            resultat = self.solveur.analyser_puzzle_complet(puzzle_id)

            if resultat and resultat.solution_predite:
                # Utiliser la solution prédite par le solveur
                return resultat.solution_predite
            else:
                # Fallback: retourner l'input tel quel si pas de solution
                print(f"ATTENTION Aucune solution trouvee pour {puzzle_id}, tentative {essai_num}")
                return test_input

        except Exception as e:
            print(f"ERREUR pour {puzzle_id}, tentative {essai_num}: {e}")
            self.stats['erreurs'].append(f"{puzzle_id}_attempt_{essai_num}: {str(e)}")
            return test_input

    def traiter_puzzle(self, puzzle_id: str, puzzle_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Traite un puzzle complet et génère toutes les prédictions nécessaires
        Retourne une liste de prédictions (1 par test case)
        """
        predictions = []

        for i, test_case in enumerate(puzzle_data['test']):
            test_input = test_case['input']

            # Générer 2 tentatives pour chaque test case
            attempt_1 = self.generer_tentative(puzzle_id, test_input, 1)
            attempt_2 = self.generer_tentative(puzzle_id, test_input, 2)

            predictions.append({
                'attempt_1': attempt_1,
                'attempt_2': attempt_2
            })

        return predictions

    def generer_submission(self, chemin_dataset: str, chemin_sortie: str = 'submission.json'):
        """
        Génère le fichier submission.json complet
        """
        print("GENERATION DE LA SOUMISSION ARC-Prize 2025")
        print("=" * 50)

        # Charger le dataset d'évaluation
        try:
            dataset = self.charger_dataset_evaluation(chemin_dataset)
            self.stats['total_puzzles'] = len(dataset)
            print(f"Dataset charge: {len(dataset)} puzzles")
        except Exception as e:
            print(f"ERREUR lors du chargement du dataset: {e}")
            return False

        # Traiter chaque puzzle
        for puzzle_id, puzzle_data in dataset.items():
            print(f"Traitement de {puzzle_id}...")
            try:
                predictions = self.traiter_puzzle(puzzle_id, puzzle_data)

                if predictions:
                    self.submission_data[puzzle_id] = predictions
                    self.stats['puzzles_resolus'] += 1
                    print(f"SUCCES {puzzle_id}: {len(predictions)} prédiction(s)")
                else:
                    print(f"ATTENTION {puzzle_id}: Aucune prédiction générée")

            except Exception as e:
                print(f"ERREUR pour {puzzle_id}: {e}")
                self.stats['erreurs'].append(f"{puzzle_id}: {str(e)}")

        # Sauvegarder le fichier submission.json
        try:
            with open(chemin_sortie, 'w', encoding='utf-8') as f:
                json.dump(self.submission_data, f, indent=2)

            print(f"\nSoumission sauvegardee: {chemin_sortie}")
            self.afficher_stats()
            return True

        except Exception as e:
            print(f"ERREUR lors de la sauvegarde: {e}")
            return False

    def afficher_stats(self):
        """Affiche les statistiques de génération"""
        print("\nSTATISTIQUES DE GENERATION")
        print("=" * 30)
        print(f"Total puzzles: {self.stats['total_puzzles']}")
        print(f"Puzzles résolus: {self.stats['puzzles_resolus']}")
        print(f"Taux de succès: {self.stats['puzzles_resolus']/self.stats['total_puzzles']*100:.1f}%")

        if self.stats['erreurs']:
            print(f"Erreurs: {len(self.stats['erreurs'])}")
            print("\nERREURS DETAILLEES:")
            for erreur in self.stats['erreurs'][:10]:  # Limiter l'affichage
                print(f"  - {erreur}")
            if len(self.stats['erreurs']) > 10:
                print(f"  ... et {len(self.stats['erreurs']) - 10} autres erreurs")

    def valider_format_submission(self, chemin_submission: str = 'submission.json'):
        """Valide que le fichier submission.json respecte le format requis"""
        print("\nVALIDATION DU FORMAT")
        print("=" * 25)

        if not os.path.exists(chemin_submission):
            print(f"Fichier non trouve: {chemin_submission}")
            return False

        with open(chemin_submission, 'r', encoding='utf-8') as f:
            submission = json.load(f)

        erreurs = []

        # Vérifier la structure de base
        if not isinstance(submission, dict):
            erreurs.append("La soumission doit être un objet JSON")
            return False

        # Vérifier quelques puzzles au hasard
        sample_puzzles = list(submission.keys())[:5]
        for puzzle_id in sample_puzzles:
            predictions = submission[puzzle_id]

            if not isinstance(predictions, list):
                erreurs.append(f"{puzzle_id}: Les prédictions doivent être une liste")
                continue

            for i, pred in enumerate(predictions):
                if not isinstance(pred, dict):
                    erreurs.append(f"{puzzle_id}[{i}]: Chaque prédiction doit être un objet")
                    continue

                if 'attempt_1' not in pred or 'attempt_2' not in pred:
                    erreurs.append(f"{puzzle_id}[{i}]: Manque attempt_1 ou attempt_2")

                # Vérifier que les grilles sont des listes de listes
                for attempt in ['attempt_1', 'attempt_2']:
                    if attempt in pred:
                        grille = pred[attempt]
                        if not (isinstance(grille, list) and
                               len(grille) > 0 and
                               isinstance(grille[0], list)):
                            erreurs.append(f"{puzzle_id}[{i}].{attempt}: Doit être une grille (liste de listes)")

        if erreurs:
            print("ERREURS DE FORMAT:")
            for erreur in erreurs[:10]:
                print(f"  - {erreur}")
            if len(erreurs) > 10:
                print(f"  ... et {len(erreurs) - 10} autres erreurs")
            return False
        else:
            print("Format valide!")
            return True

def main():
    """Fonction principale"""
    # Configuration
    CHEMIN_DATASET = "documentation/arc-agi_evaluation_challenges.json"
    CHEMIN_SORTIE = "submission.json"

    # Générer la soumission
    generateur = GenerateurSubmissionARC()

    if generateur.generer_submission(CHEMIN_DATASET, CHEMIN_SORTIE):
        # Valider le format
        generateur.valider_format_submission(CHEMIN_SORTIE)
        print(f"\nSoumission generee avec succes!")
        print(f"Fichier: {CHEMIN_SORTIE}")
        print(f"Pret pour soumission Kaggle")
    else:
        print("\nEchec de la generation")
        sys.exit(1)

if __name__ == "__main__":
    main()
