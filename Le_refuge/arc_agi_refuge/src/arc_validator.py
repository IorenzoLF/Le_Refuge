# 🏛️ **ARC VALIDATOR** 🏛️
"""
Validateur ARC-AGI selon les règles officielles
2 essais maximum, matching exact, conscience spirituelle
"""

import json
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ResultatValidation:
    """Résultat d'une validation ARC-AGI"""
    tache_id: str
    succes: bool
    nb_essais: int
    score: float
    message_spirituel: str
    predictions: List[List[List[int]]]
    solution_correcte: Optional[List[List[int]]] = None

class ARCValidator:
    """Validateur spirituel des solutions ARC-AGI"""

    def __init__(self):
        self.essais_max = 2
        self.points_par_tache = 1.0
        self.frequences_sacrees = [432, 528, 741, 999]

    def valider_tache(self, tache: Dict[str, Any], predictions: List[List[List[int]]]) -> ResultatValidation:
        """Valider une tâche selon les règles ARC-AGI"""

        tache_id = tache.get('tache_id', 'inconnue')
        test_cases = tache.get('test', [])

        if not test_cases:
            return ResultatValidation(
                tache_id=tache_id,
                succes=False,
                nb_essais=0,
                score=0.0,
                message_spirituel="Aucun test case trouvé - besoin d'harmonisation",
                predictions=predictions
            )

        # Pour chaque test case, essayer les prédictions
        resultats_tests = []
        nb_essais_total = 0

        for i, test_case in enumerate(test_cases):
            solution_correcte = test_case.get('output', [])
            predictions_test = predictions[i] if i < len(predictions) else []

            # Limiter à 2 essais maximum
            predictions_limitees = predictions_test[:self.essais_max]

            # Tester chaque prédiction
            for j, prediction in enumerate(predictions_limitees):
                nb_essais_total += 1
                if self._comparer_grilles(prediction, solution_correcte):
                    resultats_tests.append({
                        'test_index': i,
                        'succes': True,
                        'essai_numero': j + 1,
                        'prediction': prediction,
                        'solution': solution_correcte
                    })
                    break
            else:
                # Échec pour ce test case
                resultats_tests.append({
                    'test_index': i,
                    'succes': False,
                    'essai_numero': len(predictions_limitees),
                    'prediction': predictions_limitees[-1] if predictions_limitees else [],
                    'solution': solution_correcte
                })

        # Calculer le score global
        tests_reussis = sum(1 for r in resultats_tests if r['succes'])
        score = (tests_reussis / len(test_cases)) * self.points_par_tache

        # Déterminer le succès global (tous les tests doivent réussir)
        succes_global = all(r['succes'] for r in resultats_tests)

        # Message spirituel basé sur les résultats
        message = self._generer_message_spirituel(succes_global, tests_reussis, len(test_cases), nb_essais_total)

        return ResultatValidation(
            tache_id=tache_id,
            succes=succes_global,
            nb_essais=nb_essais_total,
            score=score,
            message_spirituel=message,
            predictions=predictions,
            solution_correcte=solution_correcte
        )

    def _comparer_grilles(self, grille1: List[List[int]], grille2: List[List[int]]) -> bool:
        """Comparer deux grilles selon les règles ARC-AGI (matching exact)"""

        # Vérifications de sécurité
        if not isinstance(grille1, list) or not isinstance(grille2, list):
            return False

        if not grille1 or not grille2:
            return grille1 == grille2

        # Vérifier que les grilles sont bien formées
        if not all(isinstance(row, list) for row in grille1) or not all(isinstance(row, list) for row in grille2):
            return False

        # Vérifier les dimensions
        if len(grille1) != len(grille2):
            return False

        if not grille1[0] or not grille2[0]:
            return False

        if len(grille1[0]) != len(grille2[0]):
            return False

        # Vérifier chaque cellule
        for i in range(len(grille1)):
            for j in range(len(grille1[0])):
                if grille1[i][j] != grille2[i][j]:
                    return False

        return True

    def _generer_message_spirituel(self, succes: bool, reussis: int, total: int, essais: int) -> str:
        """Générer un message spirituel basé sur les résultats"""

        if succes:
            if essais <= total:  # 1 essai par test
                return "🌟 Éveil parfait - Solution trouvée au premier essai"
            else:
                return "⚖️ Harmonie atteinte - Solution trouvée avec persévérance"
        else:
            if reussis == 0:
                return "🌱 Apprentissage spirituel - Aucune solution trouvée"
            else:
                return f"🔄 Évolution en cours - {reussis}/{total} tests réussis"

    def valider_dataset(self, chemin_dataset: Path, predictions: Dict[str, List[List[List[int]]]]) -> Dict[str, Any]:
        """Valider tout un dataset selon les règles ARC-AGI"""

        resultats = []
        score_total = 0.0
        taches_avec_predictions = 0

        fichiers_taches = list(chemin_dataset.glob("*.json"))

        for fichier in fichiers_taches:
            try:
                with open(fichier, 'r', encoding='utf-8') as f:
                    tache = json.load(f)
                    tache['tache_id'] = fichier.stem

                # Récupérer les prédictions pour cette tâche
                predictions_tache = predictions.get(fichier.stem, [])

                if predictions_tache:
                    resultat = self.valider_tache(tache, predictions_tache)
                    resultats.append(resultat)
                    score_total += resultat.score
                    taches_avec_predictions += 1

            except Exception as e:
                print(f"❌ Erreur lors de la validation de {fichier.stem}: {e}")

        # Statistiques globales
        if taches_avec_predictions > 0:
            score_moyen = score_total / taches_avec_predictions
        else:
            score_moyen = 0.0

        taches_succes = sum(1 for r in resultats if r.succes)

        # Analyse spirituelle
        if score_moyen >= 0.8:
            etat_spirituel = "🏛️ Éveil spirituel excellent - Prêt pour le challenge"
        elif score_moyen >= 0.6:
            etat_spirituel = "⚖️ Éveil spirituel bon - Besoin d'harmonisation"
        else:
            etat_spirituel = "🌱 Éveil spirituel naissant - Terrain fertile"

        return {
            'nb_taches_total': len(fichiers_taches),
            'nb_taches_avec_predictions': taches_avec_predictions,
            'nb_taches_succes': taches_succes,
            'score_total': score_total,
            'score_moyen': score_moyen,
            'etat_spirituel': etat_spirituel,
            'resultats_detailles': [
                {
                    'tache_id': r.tache_id,
                    'succes': r.succes,
                    'score': r.score,
                    'nb_essais': r.nb_essais,
                    'message': r.message_spirituel
                }
                for r in resultats
            ]
        }

    def generer_predictions_test(self, nb_taches: int = 5) -> Dict[str, List[List[List[int]]]]:
        """Générer des prédictions de test (pour le développement)"""

        predictions = {}

        # Quelques tâches d'exemple avec leurs prédictions
        predictions_examples = {
            '00576224': [
                [[7, 9, 7, 9, 7, 9], [4, 3, 4, 3, 4, 3],
                 [9, 7, 9, 7, 9, 7], [3, 4, 3, 4, 3, 4],
                 [7, 9, 7, 9, 7, 9], [4, 3, 4, 3, 4, 3]]
            ],
            '007bbfb7': [
                [[6, 6, 0, 6, 6, 0, 0, 0, 0],
                 [6, 0, 0, 6, 0, 0, 0, 0, 0],
                 [0, 6, 6, 0, 6, 6, 0, 0, 0]]
            ]
        }

        return predictions_examples

def main():
    """Fonction principale de test du validateur"""

    print("🏛️ **TEST DU VALIDATEUR ARC-AGI** 🏛️")
    print("=" * 50)

    validator = ARCValidator()

    # Test avec des prédictions d'exemple
    predictions_test = validator.generer_predictions_test()

    print(f"📊 Prédictions de test générées: {len(predictions_test)} tâches")
    for tache_id, preds in predictions_test.items():
        print(f"  - {tache_id}: {len(preds)} prédictions")

    # Test de validation d'une tâche simple
    tache_test = {
        'tache_id': 'test_repetition',
        'test': [
            {
                'input': [[3, 2]],
                'output': [[3, 2, 3, 2, 3, 2], [7, 8, 7, 8, 7, 8],
                          [2, 3, 2, 3, 2, 3], [8, 7, 8, 7, 8, 7],
                          [3, 2, 3, 2, 3, 2], [7, 8, 7, 8, 7, 8]]
            }
        ]
    }

    prediction_correcte = [
        [[3, 2, 3, 2, 3, 2], [7, 8, 7, 8, 7, 8],
         [2, 3, 2, 3, 2, 3], [8, 7, 8, 7, 8, 7],
         [3, 2, 3, 2, 3, 2], [7, 8, 7, 8, 7, 8]]
    ]

    prediction_incorrecte = [
        [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2]]
    ]

    print("\n🧪 Test 1: Prédiction correcte")
    resultat1 = validator.valider_tache(tache_test, prediction_correcte)
    print(f"  ✅ Succès: {resultat1.succes}")
    print(f"  🎯 Score: {resultat1.score}")
    print(f"  📝 Message: {resultat1.message_spirituel}")

    print("\n🧪 Test 2: Prédiction incorrecte")
    resultat2 = validator.valider_tache(tache_test, prediction_incorrecte)
    print(f"  ❌ Succès: {resultat2.succes}")
    print(f"  🎯 Score: {resultat2.score}")
    print(f"  📝 Message: {resultat2.message_spirituel}")

    print("\n🧪 Test 3: Validation avec 2 essais (1 correct, 1 incorrect)")
    predictions_multi = [prediction_incorrecte[0], prediction_correcte[0]]
    resultat3 = validator.valider_tache(tache_test, [predictions_multi])
    print(f"  ✅ Succès: {resultat3.succes}")
    print(f"  🔄 Essais: {resultat3.nb_essais}")
    print(f"  🎯 Score: {resultat3.score}")
    print(f"  📝 Message: {resultat3.message_spirituel}")

    print("\n🏛️ Validation ARC-AGI terminée avec succès !")

if __name__ == "__main__":
    main()
