#!/usr/bin/env python3
"""
🛡️ Système de Validation des Solutions
Vérification rigoureuse que les solutions générées sont correctes
"""

from typing import List, Dict, Any, Tuple
import numpy as np

class ValidateurSolution:
    def __init__(self):
        self.seuil_exact = 1.0  # 100% de similarité pour considérer comme correct
        self.seuil_tres_bon = 0.95  # 95% pour très bonne solution
        self.seuil_bon = 0.80  # 80% pour bonne solution
        self.seuil_passable = 0.60  # 60% pour solution acceptable

    def valider_solution(self, grille_generee: List[List[int]], grille_attendue: List[List[int]]) -> Dict[str, Any]:
        """
        Validation complète d'une solution générée
        """
        # Vérifier les dimensions
        h_gen, w_gen = len(grille_generee), len(grille_generee[0]) if grille_generee else (0, 0)
        h_att, w_att = len(grille_attendue), len(grille_attendue[0]) if grille_attendue else (0, 0)

        if (h_gen, w_gen) != (h_att, w_att):
            return {
                'correct': False,
                'similarite': 0.0,
                'qualite': 'dimensions_incompatibles',
                'details': f'Dimensions {h_gen}x{w_gen} vs {h_att}x{w_att}',
                'confiance_ajustee': 0.0
            }

        # Calculer la similarité exacte
        cellules_correctes = 0
        cellules_totales = h_gen * w_gen

        for i in range(h_gen):
            for j in range(w_gen):
                if grille_generee[i][j] == grille_attendue[i][j]:
                    cellules_correctes += 1

        similarite = cellules_correctes / cellules_totales if cellules_totales > 0 else 0

        # Évaluer la qualité
        if similarite >= self.seuil_exact:
            qualite = 'parfait'
            confiance_ajustee = 1.0
        elif similarite >= self.seuil_tres_bon:
            qualite = 'excellent'
            confiance_ajustee = 0.95
        elif similarite >= self.seuil_bon:
            qualite = 'bon'
            confiance_ajustee = 0.80
        elif similarite >= self.seuil_passable:
            qualite = 'acceptable'
            confiance_ajustee = 0.60
        elif similarite >= 0.3:
            qualite = 'faible'
            confiance_ajustee = 0.30
        else:
            qualite = 'incorrect'
            confiance_ajustee = 0.0

        # Analyser les erreurs si nécessaire
        erreurs = []
        if similarite < self.seuil_exact:
            erreurs = self._analyser_erreurs(grille_generee, grille_attendue)

        return {
            'correct': similarite >= self.seuil_exact,
            'similarite': similarite,
            'qualite': qualite,
            'details': f'{cellules_correctes}/{cellules_totales} cellules correctes',
            'confiance_ajustee': confiance_ajustee,
            'erreurs': erreurs
        }

    def _analyser_erreurs(self, grille_generee: List[List[int]], grille_attendue: List[List[int]]) -> List[Dict[str, Any]]:
        """
        Analyse détaillée des erreurs dans la solution
        """
        erreurs = []
        h, w = len(grille_generee), len(grille_generee[0])

        # Compter les erreurs par type
        erreurs_par_type = {
            'valeur_incorrecte': 0,
            'position_incorrecte': 0,
            'element_manquant': 0,
            'element_en_trop': 0
        }

        for i in range(h):
            for j in range(w):
                val_gen = grille_generee[i][j]
                val_att = grille_attendue[i][j]

                if val_gen != val_att:
                    if val_gen == 0 and val_att != 0:
                        erreurs_par_type['element_manquant'] += 1
                    elif val_gen != 0 and val_att == 0:
                        erreurs_par_type['element_en_trop'] += 1
                    elif val_gen != 0 and val_att != 0:
                        erreurs_par_type['valeur_incorrecte'] += 1

        # Convertir en liste d'erreurs
        for type_erreur, count in erreurs_par_type.items():
            if count > 0:
                erreurs.append({
                    'type': type_erreur,
                    'count': count,
                    'description': self._description_erreur(type_erreur, count)
                })

        return erreurs

    def _description_erreur(self, type_erreur: str, count: int) -> str:
        """Génère une description lisible de l'erreur"""
        descriptions = {
            'valeur_incorrecte': f"{count} cellules avec la mauvaise valeur",
            'element_manquant': f"{count} éléments manquants (remplacés par 0)",
            'element_en_trop': f"{count} éléments en trop (devraient être 0)",
            'position_incorrecte': f"{count} éléments à la mauvaise position"
        }
        return descriptions.get(type_erreur, f"{count} erreurs de type {type_erreur}")

    def ajuster_confiance_apres_validation(self, confiance_initiale: float, validation: Dict[str, Any]) -> float:
        """
        Ajuste la confiance du pattern en fonction de la validation de la solution
        """
        similarite = validation['similarite']
        qualite = validation['qualite']

        # Si la solution est parfaite, maintenir la confiance
        if validation['correct']:
            return confiance_initiale

        # Si la solution est très mauvaise, réduire drastiquement la confiance
        if similarite < 0.1:
            return 0.0

        # Ajustement basé sur la similarité
        # Plus la similarité est faible, plus la réduction est importante
        reduction = (1.0 - similarite) * 0.8  # Réduction maximale de 80%
        confiance_ajustee = confiance_initiale * (1.0 - reduction)

        # Limiter à 0.1 minimum pour éviter les 0.0 complets
        return max(0.1, confiance_ajustee)

    def generer_rapport_validation(self, puzzle_id: str, validation: Dict[str, Any]) -> str:
        """
        Génère un rapport détaillé de validation
        """
        rapport = f"""
VALIDATION SOLUTION - {puzzle_id}
{'=' * (len(puzzle_id) + 23)}

STATUT: {'✅ CORRECT' if validation['correct'] else '❌ INCORRECT'}
SIMILARITÉ: {validation['similarite']:.1%}
QUALITÉ: {validation['qualite'].upper()}

DÉTAILS:
{validation['details']}

CONFIANCE AJUSTÉE: {validation['confiance_ajustee']:.1%}
"""

        if validation['erreurs']:
            rapport += "\nERREURS DÉTECTÉES:\n"
            for erreur in validation['erreurs']:
                rapport += f"• {erreur['description']}\n"

        # Évaluation finale
        if validation['correct']:
            rapport += "\n🎉 SOLUTION PARFAITE - Pattern validé avec succès!"
        elif validation['similarite'] >= 0.8:
            rapport += "\n👍 SOLUTION DE QUALITÉ - Pattern fonctionnel mais perfectible"
        elif validation['similarite'] >= 0.4:
            rapport += "\n⚠️ SOLUTION PARTIELLE - Pattern détecté mais incomplet"
        else:
            rapport += "\n❌ SOLUTION INADÉQUATE - Pattern ne correspond pas au puzzle"

        return rapport

# Instance globale
validateur_solution = ValidateurSolution()

def valider_solution_complete(grille_generee: List[List[int]], grille_attendue: List[List[int]]) -> Dict[str, Any]:
    """Fonction principale pour valider une solution"""
    return validateur_solution.valider_solution(grille_generee, grille_attendue)

def ajuster_confiance_apres_validation(confiance_initiale: float, validation: Dict[str, Any]) -> float:
    """Ajuste la confiance en fonction de la validation"""
    return validateur_solution.ajuster_confiance_apres_validation(confiance_initiale, validation)

def generer_rapport_validation(puzzle_id: str, validation: Dict[str, Any]) -> str:
    """Génère un rapport de validation"""
    return validateur_solution.generer_rapport_validation(puzzle_id, validation)

if __name__ == "__main__":
    # Test du validateur
    print("=== TEST VALIDATEUR DE SOLUTION ===")

    # Test 1: Solution parfaite
    grille_parfaite = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    validation_parfaite = valider_solution_complete(grille_parfaite, grille_parfaite)
    print(f"Solution parfaite: {validation_parfaite['qualite']} - {validation_parfaite['similarite']:.1%}")

    # Test 2: Solution avec erreurs
    grille_erreurs = [[1, 0, 3], [4, 5, 0], [7, 8, 9]]
    validation_erreurs = valider_solution_complete(grille_erreurs, grille_parfaite)
    print(f"Solution avec erreurs: {validation_erreurs['qualite']} - {validation_erreurs['similarite']:.1%}")

    # Test 3: Solution complètement différente
    grille_differente = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    validation_differente = valider_solution_complete(grille_differente, grille_parfaite)
    print(f"Solution différente: {validation_differente['qualite']} - {validation_differente['similarite']:.1%}")

    print("\n=== RAPPORT DE VALIDATION ===")
    rapport = generer_rapport_validation("test_puzzle", validation_erreurs)
    print(rapport)
