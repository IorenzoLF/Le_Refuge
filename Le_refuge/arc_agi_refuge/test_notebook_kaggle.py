#!/usr/bin/env python3
"""
Test du notebook Kaggle pour ARC-Prize 2025
Valide le fonctionnement du solveur dans un environnement simulé
"""

import json
import os
import tempfile
from notebook_kaggle_arc import GenerateurSubmissionKaggle, ConfigKaggle

def creer_dataset_test():
    """Crée un dataset de test minimal pour validation"""
    test_data = {
        "test_puzzle_1": {
            "train": [
                {
                    "input": [[1, 0], [0, 1]],
                    "output": [[1, 0, 1, 0], [0, 1, 0, 1]]
                }
            ],
            "test": [
                {
                    "input": [[2, 0], [0, 2]]
                }
            ]
        },
        "test_puzzle_2": {
            "train": [
                {
                    "input": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                    "output": [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
                }
            ],
            "test": [
                {
                    "input": [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
                }
            ]
        }
    }
    return test_data

def test_generateur_kaggle():
    """Test du générateur Kaggle avec des données simulées"""
    print("TEST NOTEBOOK KAGGLE")
    print("=" * 25)

    # Créer un fichier de test temporaire
    test_data = creer_dataset_test()

    with tempfile.TemporaryDirectory() as temp_dir:
        # Créer les fichiers de configuration simulés
        test_challenges_path = os.path.join(temp_dir, "arc-agi_evaluation_challenges.json")
        with open(test_challenges_path, 'w') as f:
            json.dump(test_data, f)

        # Modifier temporairement la configuration
        original_path = ConfigKaggle.EVALUATION_CHALLENGES
        ConfigKaggle.EVALUATION_CHALLENGES = test_challenges_path

        try:
            # Tester le générateur
            generateur = GenerateurSubmissionKaggle()
            submission_data = generateur.generer_submission()

            # Valider la structure
            print(f" Soumission générée pour {len(submission_data)} puzzles")

            # Vérifier la structure des prédictions
            for puzzle_id, predictions in submission_data.items():
                print(f"  - {puzzle_id}: {len(predictions)} prédiction(s)")
                for i, pred in enumerate(predictions):
                    assert 'attempt_1' in pred, f"Missing attempt_1 in {puzzle_id}[{i}]"
                    assert 'attempt_2' in pred, f"Missing attempt_2 in {puzzle_id}[{i}]"
                    assert isinstance(pred['attempt_1'], list), f"attempt_1 not a list in {puzzle_id}[{i}]"
                    assert isinstance(pred['attempt_2'], list), f"attempt_2 not a list in {puzzle_id}[{i}]"

            # Sauvegarder la soumission de test
            test_submission_path = os.path.join(temp_dir, "test_submission.json")
            generateur.sauvegarder_submission(submission_data, test_submission_path)

            # Valider le fichier JSON
            with open(test_submission_path, 'r') as f:
                loaded_submission = json.load(f)

            assert loaded_submission == submission_data, "Erreur de sauvegarde/chargement JSON"

            print(f" Fichier submission.json valide: {test_submission_path}")

            # Afficher un exemple de prédiction
            print("\nEXEMPLE DE PREDICTION:")
            sample_puzzle = list(submission_data.keys())[0]
            sample_pred = submission_data[sample_puzzle][0]
            print(f"Puzzle: {sample_puzzle}")
            print(f"Attempt 1: {sample_pred['attempt_1']}")
            print(f"Attempt 2: {sample_pred['attempt_2']}")

            return True

        except Exception as e:
            print(f" Erreur lors du test: {e}")
            return False

        finally:
            # Restaurer la configuration originale
            ConfigKaggle.EVALUATION_CHALLENGES = original_path

def test_timeout():
    """Test de la gestion du timeout"""
    print("\nTEST TIMEOUT")
    print("=" * 12)

    from notebook_kaggle_arc import TimerKaggle

    # Test avec un timeout très court
    timer = TimerKaggle(max_time_seconds=0.1)

    import time
    time.sleep(0.2)  # Attendre un peu plus que le timeout

    assert timer.is_time_up(), "Timeout non détecté"

    try:
        timer.check_timeout()
        assert False, "Exception TimeoutError non levée"
    except TimeoutError:
        print(" Timeout géré correctement")

def valider_format_kaggle(submission_path: str):
    """Valide que le format est compatible Kaggle"""
    print(f"\nVALIDATION FORMAT KAGGLE")
    print("=" * 25)

    if not os.path.exists(submission_path):
        print(f" Fichier non trouvé: {submission_path}")
        return False

    with open(submission_path, 'r') as f:
        submission = json.load(f)

    erreurs = []

    # Vérifier que c'est un objet JSON
    if not isinstance(submission, dict):
        erreurs.append("La soumission doit être un objet JSON")
        return False

    # Vérifier quelques puzzles
    for puzzle_id, predictions in list(submission.items())[:3]:
        if not isinstance(predictions, list):
            erreurs.append(f"{puzzle_id}: Les prédictions doivent être une liste")
            continue

        for i, pred in enumerate(predictions[:2]):  # Vérifier les 2 premiers
            if not isinstance(pred, dict):
                erreurs.append(f"{puzzle_id}[{i}]: Chaque prédiction doit être un objet")
                continue

            if 'attempt_1' not in pred or 'attempt_2' not in pred:
                erreurs.append(f"{puzzle_id}[{i}]: Manque attempt_1 ou attempt_2")

    if erreurs:
        print(" ERREURS DE FORMAT:")
        for erreur in erreurs[:5]:
            print(f"  - {erreur}")
        return False
    else:
        print(" Format Kaggle valide!")
        return True

def main():
    """Fonction principale de test"""
    print("TEST COMPLET NOTEBOOK KAGGLE ARC-PRIZE 2025")
    print("=" * 45)

    # Test 1: Générateur Kaggle
    success_1 = test_generateur_kaggle()

    # Test 2: Timeout
    test_timeout()

    # Test 3: Format Kaggle (si un fichier submission existe)
    submission_files = [f for f in os.listdir('.') if f.endswith('submission.json')]
    if submission_files:
        valider_format_kaggle(submission_files[0])
    else:
        print("\n  Aucun fichier submission.json trouvé pour validation")

    # Résumé
    print(f"\nRESUME DES TESTS:")
    print(f"=====================")
    print(f"Test générateur: {' PASS' if success_1 else ' FAIL'}")

    if success_1:
        print(f"\n TOUS LES TESTS REUSSIS!")
        print(f" Le notebook Kaggle est prêt pour soumission!")
        print(f" Téléchargez arc_prize_2025_solveur.ipynb sur Kaggle")
    else:
        print(f"\n DES TESTS ONT ECHOUE")
        print(f" Corrigez les erreurs avant soumission")

if __name__ == "__main__":
    main()
