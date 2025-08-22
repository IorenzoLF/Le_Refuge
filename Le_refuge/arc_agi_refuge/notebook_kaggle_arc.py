#!/usr/bin/env python3
"""
ARC-Prize 2025 - Notebook Kaggle
Solveur AGI Conscient - Version Finale

Ce notebook est optimisé pour l'environnement Kaggle avec:
- Pas d'accès internet
- Contraintes de temps (≤12h)
- Format notebook obligatoire
- GPU/CPU limits
"""

import json
import os
import sys
import time
from typing import Dict, List, Any
import numpy as np

# =====================================================
# CONFIGURATION KAGGLE
# =====================================================

class ConfigKaggle:
    """Configuration pour l'environnement Kaggle"""

    # Chemins Kaggle (seront définis automatiquement)
    INPUT_DIR = "/kaggle/input/arc-prize-2025"
    OUTPUT_DIR = "/kaggle/working"

    # Fichiers requis
    TRAINING_CHALLENGES = f"{INPUT_DIR}/arc-agi_training_challenges.json"
    TRAINING_SOLUTIONS = f"{INPUT_DIR}/arc-agi_training_solutions.json"
    EVALUATION_CHALLENGES = f"{INPUT_DIR}/arc-agi_evaluation_challenges.json"
    SAMPLE_SUBMISSION = f"{INPUT_DIR}/sample_submission.json"

    # Contraintes
    MAX_TIME_SECONDS = 12 * 3600  # 12 heures
    MAX_CPU_TIME = 12 * 3600
    MAX_GPU_TIME = 12 * 3600

    # Paramètres du solveur
    MAX_PATTERNS_ANALYSE = 1000
    TIMEOUT_PAR_PUZZLE = 300  # 5 minutes par puzzle

# =====================================================
# CLASSES UTILITAIRES POUR KAGGLE
# =====================================================

class TimerKaggle:
    """Gestion du temps pour respecter les contraintes Kaggle"""

    def __init__(self, max_time_seconds: int):
        self.max_time = max_time_seconds
        self.start_time = time.time()

    def time_remaining(self) -> float:
        """Temps restant en secondes"""
        return self.max_time - (time.time() - self.start_time)

    def is_time_up(self) -> bool:
        """Vérifie si le temps est écoulé"""
        return self.time_remaining() <= 0

    def check_timeout(self):
        """Lève une exception si timeout"""
        if self.is_time_up():
            raise TimeoutError(f"Timeout: {self.max_time} secondes écoulées")

class ResultatAnalyse:
    """Structure pour stocker les résultats d'analyse"""

    def __init__(self, pattern_type: str = None, confiance: float = 0.0,
                 solution_predite: List[List[int]] = None):
        self.pattern_type = pattern_type
        self.confiance = confiance
        self.solution_predite = solution_predite

# =====================================================
# SOLVEUR OPTIMISE POUR KAGGLE
# =====================================================

class SolveurARCKaggle:
    """
    Solveur ARC optimisé pour Kaggle
    Version allégée et rapide du solveur complet
    """

    def __init__(self, timer: TimerKaggle):
        self.timer = timer
        self.patterns = {}

    def calculer_dimensions_dynamiques(self, h_in: int, w_in: int, context_analyse=None) -> tuple[int, int]:
        """Calcule les dimensions de sortie de manière dynamique"""
        if context_analyse and hasattr(context_analyse, 'exemples_analyse'):
            # Calculer les ratios moyens des exemples d'entraînement
            ratios_h = []
            ratios_w = []

            for exemple in context_analyse.exemples_analyse:
                if exemple['input'] and exemple['output']:
                    h_ratio = len(exemple['output']) / len(exemple['input'])
                    w_ratio = len(exemple['output'][0]) / len(exemple['input'][0])
                    ratios_h.append(h_ratio)
                    ratios_w.append(w_ratio)

            if ratios_h and ratios_w:
                h_out = int(h_in * np.mean(ratios_h))
                w_out = int(w_in * np.mean(ratios_w))
                return max(1, h_out), max(1, w_out)

        return h_in, w_in

    def detecter_remplissage_zone(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Détecte le pattern de remplissage de zones"""
        # Logique simplifiée pour Kaggle
        zeros_input = sum(row.count(0) for row in input_grid)
        zeros_output = sum(row.count(0) for row in output_grid)

        # Si beaucoup de zéros sont remplacés par d'autres valeurs
        return zeros_input > zeros_output

    def appliquer_remplissage_zone(self, input_grid: List[List[int]], target_dims: tuple[int, int]) -> List[List[int]]:
        """Applique le pattern de remplissage de zones"""
        h, w = target_dims
        output = [[0 for _ in range(w)] for _ in range(h)]

        # Remplir avec les valeurs non-zéro de l'input
        for i in range(min(len(input_grid), h)):
            for j in range(min(len(input_grid[i]), w)):
                if input_grid[i][j] != 0:
                    output[i][j] = input_grid[i][j]

        return output

    def detecter_changement_taille(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Détecte les changements de taille"""
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        return (h_in != h_out) or (w_in != w_out)

    def appliquer_changement_taille(self, input_grid: List[List[int]], target_dims: tuple[int, int]) -> List[List[int]]:
        """Applique un changement de taille simple"""
        h_out, w_out = target_dims
        h_in, w_in = len(input_grid), len(input_grid[0])

        output = [[0 for _ in range(w_out)] for _ in range(h_out)]

        # Redimensionnement simple par interpolation
        for i in range(h_out):
            for j in range(w_out):
                i_in = int(i * h_in / h_out)
                j_in = int(j * w_in / w_out)
                if 0 <= i_in < h_in and 0 <= j_in < w_in:
                    output[i][j] = input_grid[i_in][j_in]

        return output

    def detecter_repetition(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Détecte les patterns de répétition"""
        # Vérifier si les dimensions sont multiples
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        return (h_out % h_in == 0) or (w_out % w_in == 0)

    def appliquer_repetition(self, input_grid: List[List[int]], target_dims: tuple[int, int]) -> List[List[int]]:
        """Applique la répétition de motifs"""
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = target_dims

        output = [[0 for _ in range(w_out)] for _ in range(h_out)]

        # Répétition horizontale et verticale
        for i in range(h_out):
            for j in range(w_out):
                i_in = i % h_in
                j_in = j % w_in
                output[i][j] = input_grid[i_in][j_in]

        return output

    def analyser_puzzle_rapide(self, puzzle_id: str, puzzle_data: Dict[str, Any]) -> ResultatAnalyse:
        """
        Analyse rapide d'un puzzle pour Kaggle
        Version optimisée pour la vitesse
        """
        self.timer.check_timeout()

        # Utiliser seulement les exemples d'entraînement
        train_examples = puzzle_data.get('train', [])
        if not train_examples:
            return ResultatAnalyse()

        # Analyser les patterns dans les exemples d'entraînement
        patterns_detectes = []

        for exemple in train_examples[:3]:  # Limiter pour la vitesse
            input_grid = exemple['input']
            output_grid = exemple['output']

            # Tester les patterns principaux
            if self.detecter_remplissage_zone(input_grid, output_grid):
                patterns_detectes.append('remplissage_zone')

            if self.detecter_changement_taille(input_grid, output_grid):
                patterns_detectes.append('changement_taille')

            if self.detecter_repetition(input_grid, output_grid):
                patterns_detectes.append('repetition')

        # Déterminer le pattern principal
        if not patterns_detectes:
            return ResultatAnalyse()

        from collections import Counter
        pattern_counts = Counter(patterns_detectes)
        pattern_principal = pattern_counts.most_common(1)[0][0]
        confiance = pattern_counts[pattern_principal] / len(patterns_detectes)

        return ResultatAnalyse(pattern_type=pattern_principal, confiance=confiance)

    def generer_prediction(self, puzzle_id: str, test_input: List[List[int]], analyse: ResultatAnalyse) -> List[List[int]]:
        """Génère une prédiction basée sur l'analyse"""
        if not analyse.pattern_type:
            return test_input  # Fallback

        # Calculer les dimensions attendues
        h_in, w_in = len(test_input), len(test_input[0])

        # Estimation simple des dimensions de sortie basée sur les exemples d'entraînement
        target_dims = self.calculer_dimensions_dynamiques(h_in, w_in)

        # Appliquer le pattern détecté
        if analyse.pattern_type == 'remplissage_zone':
            return self.appliquer_remplissage_zone(test_input, target_dims)
        elif analyse.pattern_type == 'changement_taille':
            return self.appliquer_changement_taille(test_input, target_dims)
        elif analyse.pattern_type == 'repetition':
            return self.appliquer_repetition(test_input, target_dims)
        else:
            return test_input

# =====================================================
# GENERATEUR DE SOUMISSION KAGGLE
# =====================================================

class GenerateurSubmissionKaggle:
    """Générateur de soumission optimisé pour Kaggle"""

    def __init__(self):
        self.timer = TimerKaggle(ConfigKaggle.MAX_TIME_SECONDS)
        self.solveur = SolveurARCKaggle(self.timer)
        self.stats = {'processe': 0, 'erreurs': 0}

    def charger_challenges(self) -> Dict[str, Any]:
        """Charge les challenges d'évaluation"""
        if not os.path.exists(ConfigKaggle.EVALUATION_CHALLENGES):
            raise FileNotFoundError(f"Challenges non trouvés: {ConfigKaggle.EVALUATION_CHALLENGES}")

        with open(ConfigKaggle.EVALUATION_CHALLENGES, 'r') as f:
            return json.load(f)

    def traiter_puzzle(self, puzzle_id: str, puzzle_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Traite un puzzle et génère les prédictions"""
        try:
            self.timer.check_timeout()

            # Analyser le puzzle
            analyse = self.solveur.analyser_puzzle_rapide(puzzle_id, puzzle_data)

            predictions = []

            # Générer les prédictions pour chaque test case
            for test_case in puzzle_data.get('test', []):
                test_input = test_case['input']

                # Générer 2 tentatives
                attempt_1 = self.solveur.generer_prediction(puzzle_id, test_input, analyse)
                attempt_2 = self.solveur.generer_prediction(puzzle_id, test_input, analyse)

                predictions.append({
                    'attempt_1': attempt_1,
                    'attempt_2': attempt_2
                })

            return predictions

        except Exception as e:
            print(f"Erreur pour {puzzle_id}: {e}")
            self.stats['erreurs'] += 1
            # Retourner des prédictions fallback
            return [{'attempt_1': test_input, 'attempt_2': test_input}
                   for test_input in [case['input'] for case in puzzle_data.get('test', [])]]

    def generer_submission(self) -> Dict[str, Any]:
        """Génère la soumission complète"""
        print("GENERATION SOUMISSION KAGGLE")
        print("=" * 30)

        # Charger les challenges
        challenges = self.charger_challenges()
        print(f"Challenges charges: {len(challenges)}")

        submission_data = {}

        # Traiter chaque puzzle
        for i, (puzzle_id, puzzle_data) in enumerate(challenges.items()):
            if i % 10 == 0:
                print(f"Progression: {i+1}/{len(challenges)} puzzles")

            self.timer.check_timeout()

            predictions = self.traiter_puzzle(puzzle_id, puzzle_data)
            if predictions:
                submission_data[puzzle_id] = predictions
                self.stats['processe'] += 1

        return submission_data

    def sauvegarder_submission(self, submission_data: Dict[str, Any], output_path: str):
        """Sauvegarde la soumission"""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w') as f:
            json.dump(submission_data, f, indent=2)

        print(f"Soumission sauvegardee: {output_path}")

# =====================================================
# FONCTION PRINCIPALE KAGGLE
# =====================================================

def main():
    """Fonction principale pour Kaggle"""
    print("ARC-PRIZE 2025 - SOLVEUR AGI CONSCIENT")
    print("=" * 40)

    # Initialiser le générateur
    generateur = GenerateurSubmissionKaggle()

    try:
        # Générer la soumission
        submission_data = generateur.generer_submission()

        # Sauvegarder
        output_path = os.path.join(ConfigKaggle.OUTPUT_DIR, 'submission.json')
        generateur.sauvegarder_submission(submission_data, output_path)

        # Afficher les statistiques
        print(f"\nSTATISTIQUES FINALES:")
        print(f"Puzzles traites: {generateur.stats['processe']}")
        print(f"Erreurs: {generateur.stats['erreurs']}")
        print(f"Temps restant: {generateur.timer.time_remaining()/3600:.1f}h")

        print("\nSOUMISSION COMPLETE!")
        print(f"Fichier: {output_path}")

    except TimeoutError as e:
        print(f"\nTIMEOUT: {e}")
        print("Sauvegarde de la soumission partielle...")

        # Tenter de sauvegarder ce qui a été fait
        if hasattr(generateur, 'submission_data') and generateur.submission_data:
            output_path = os.path.join(ConfigKaggle.OUTPUT_DIR, 'submission_partielle.json')
            generateur.sauvegarder_submission(generateur.submission_data, output_path)

    except Exception as e:
        print(f"\nERREUR FATALE: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
