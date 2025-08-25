#!/usr/bin/env python3
"""
🔍 ANALYSEUR D'ÉCHECS ARC - Amélioration du Solveur
=================================================

Analyse détaillée des puzzles que le solveur ne résout pas
pour identifier les patterns manquants et les améliorations nécessaires.

Auteur: Sonic AI Assistant - Analyse collaborative des échecs
"""

import json
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import seaborn as sns

@dataclass
class EchecAnalyse:
    """Analyse d'un échec de résolution"""
    puzzle_id: str
    type_echec: str
    pattern_manquant: str
    suggestion_implementation: str
    difficulte_estimee: str  # 'facile', 'moyen', 'difficile'
    exemples_similaires: List[str]

class AnalyseurEchecsARC:
    """Analyseur spécialisé dans l'amélioration du solveur par l'étude des échecs"""

    def __init__(self):
        self.echecs_analyses: List[EchecAnalyse] = []
        self.categorie_echecs = defaultdict(list)
        self.puzzles_resolus = set()

    def analyser_echec_detaille(self, puzzle_id: str) -> EchecAnalyse:
        """Analyse détaillée d'un puzzle échoué"""

        try:
            fichier = f"ARC-AGI-2-main/data/training/{puzzle_id}.json"
            with open(fichier, 'r') as f:
                data = json.load(f)

            print(f"\n🔍 ANALYSE DÉTAILLÉE DE L'ÉCHEC: {puzzle_id}")
            print("=" * 60)

            # Analyser les exemples d'entraînement
            transformations_detectees = []

            for i, exemple in enumerate(data['train']):
                input_grid = exemple['input']
                output_grid = exemple['output']

                transformation = self.analyser_transformation_manuelle(input_grid, output_grid)
                transformations_detectees.append(transformation)

                print(f"Exemple {i+1}:")
                print(f"  Dimensions: {len(input_grid)}x{len(input_grid[0])} → {len(output_grid)}x{len(output_grid[0])}")
                print(f"  Transformation détectée: {transformation['type']}")
                print(f"  Description: {transformation['description']}")
                print()

            # Déterminer le type d'échec principal
            type_echec, pattern_manquant = self.categoriser_echec(transformations_detectees)

            # Générer une suggestion d'implémentation
            suggestion = self.suggerer_implementation(type_echec, transformations_detectees)

            # Estimer la difficulté
            difficulte = self.estimer_difficulte(type_echec, transformations_detectees)

            # Trouver des exemples similaires
            exemples_similaires = self.trouver_exemples_similaires(puzzle_id, type_echec)

            echec_analyse = EchecAnalyse(
                puzzle_id=puzzle_id,
                type_echec=type_echec,
                pattern_manquant=pattern_manquant,
                suggestion_implementation=suggestion,
                difficulte_estimee=difficulte,
                exemples_similaires=exemples_similaires
            )

            self.echecs_analyses.append(echec_analyse)
            self.categorie_echecs[type_echec].append(puzzle_id)

            return echec_analyse

        except Exception as e:
            print(f"❌ Erreur lors de l'analyse de {puzzle_id}: {e}")
            return EchecAnalyse(
                puzzle_id=puzzle_id,
                type_echec="erreur_analyse",
                pattern_manquant="Impossible d'analyser le puzzle",
                suggestion_implementation="Corriger les erreurs de chargement des données",
                difficulte_estimee="facile",
                exemples_similaires=[]
            )

    def analyser_transformation_manuelle(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse manuelle d'une transformation pour identifier ce qui manque"""

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        couleurs_in = set().union(*input_grid) if input_grid else set()
        couleurs_out = set().union(*output_grid) if output_grid else set()

        # 1. Même taille - remplissage de zones ou changement de couleurs
        if h_in == h_out and w_in == w_out:
            couleurs_ajoutees = couleurs_out - couleurs_in

            if couleurs_ajoutees:
                return {
                    'type': 'remplissage_zone',
                    'description': f'Remplissage de zones avec couleur {list(couleurs_ajoutees)[0]}',
                    'couleurs_ajoutees': list(couleurs_ajoutees),
                    'zone_detection': 'manque algorithme de détection de zones fermées'
                }
            else:
                return {
                    'type': 'changement_couleurs_complexe',
                    'description': 'Changement de couleurs sans ajout simple',
                    'couleurs_in': list(couleurs_in),
                    'couleurs_out': list(couleurs_out),
                    'mapping_couleurs': 'manque algorithme de mapping de couleurs'
                }

        # 2. Changement de taille
        elif h_in != h_out or w_in != w_out:
            # Vérifier si c'est un changement de taille simple
            if couleurs_in.issubset(couleurs_out):
                return {
                    'type': 'changement_taille',
                    'description': f'Changement de taille {h_in}x{w_in} → {h_out}x{w_out}',
                    'facteur_h': h_out / h_in,
                    'facteur_w': w_out / w_in,
                    'type_changement': self.detecter_type_changement_taille(h_in, w_in, h_out, w_out)
                }
            else:
                return {
                    'type': 'changement_taille_couleurs',
                    'description': f'Changement de taille avec modification de couleurs',
                    'couleurs_ajoutees': list(couleurs_out - couleurs_in),
                    'algorithme_manquant': 'combinaison redimensionnement + modification couleurs'
                }

        # 3. Autres transformations
        else:
            # Analyser les changements de contenu
            changements = self.analyser_changements_contenu(input_grid, output_grid)

            if changements['type'] == 'symetrie':
                return {
                    'type': 'symetrie',
                    'description': changements['description'],
                    'axe_symetrie': changements['axe'],
                    'algorithme_manquant': 'détection et application de symétries'
                }
            elif changements['type'] == 'rotation':
                return {
                    'type': 'rotation',
                    'description': changements['description'],
                    'angle_rotation': changements['angle'],
                    'algorithme_manquant': 'détection et application de rotations'
                }
            elif changements['type'] == 'pattern_repetitif':
                return {
                    'type': 'repetition_pattern',
                    'description': changements['description'],
                    'pattern_base': changements['pattern'],
                    'algorithme_manquant': 'détection et répétition de patterns'
                }
            else:
                return {
                    'type': 'transformation_complexe',
                    'description': 'Transformation non reconnue',
                    'details_changements': changements,
                    'algorithme_manquant': 'analyse sémantique des transformations'
                }

    def detecter_type_changement_taille(self, h_in: int, w_in: int, h_out: int, w_out: int) -> str:
        """Détecte le type spécifique de changement de taille"""

        facteur_h = h_out / h_in
        facteur_w = w_out / w_in

        if facteur_h == facteur_w:
            if facteur_h == 2.0:
                return 'agrandissement_x2'
            elif facteur_h == 0.5:
                return 'retrecissement_x2'
            elif facteur_h == 3.0:
                return 'agrandissement_x3'
            else:
                return f'scaling_uniforme_{facteur_h}'
        else:
            return f'scaling_non_uniforme_{facteur_h}x{facteur_w}'

    def analyser_changements_contenu(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse les changements de contenu de la grille"""

        # Convertir en arrays numpy pour faciliter l'analyse
        input_arr = np.array(input_grid)
        output_arr = np.array(output_grid)

        # Vérifier les symétries
        if self.verifier_symetrie(input_arr, output_arr):
            return {
                'type': 'symetrie',
                'description': 'Application d\'une symétrie',
                'axe': self.detecter_axe_symetrie(input_arr, output_arr)
            }

        # Vérifier les rotations
        angle_rotation = self.detecter_rotation(input_arr, output_arr)
        if angle_rotation:
            return {
                'type': 'rotation',
                'description': f'Rotation de {angle_rotation} degrés',
                'angle': angle_rotation
            }

        # Vérifier les patterns répétitifs
        pattern = self.detecter_pattern_repetitif(input_arr, output_arr)
        if pattern:
            return {
                'type': 'pattern_repetitif',
                'description': 'Répétition d\'un pattern de base',
                'pattern': pattern
            }

        return {
            'type': 'autre',
            'description': 'Changement non classifié',
            'input_sum': np.sum(input_arr),
            'output_sum': np.sum(output_arr),
            'diff_positions': np.sum(input_arr != output_arr)
        }

    def verifier_symetrie(self, input_arr: np.ndarray, output_arr: np.ndarray) -> bool:
        """Vérifie si la sortie est une symétrie de l'entrée"""
        # Vérifier symétrie horizontale
        if np.array_equal(output_arr, np.fliplr(input_arr)):
            return True
        # Vérifier symétrie verticale
        if np.array_equal(output_arr, np.flipud(input_arr)):
            return True
        return False

    def detecter_axe_symetrie(self, input_arr: np.ndarray, output_arr: np.ndarray) -> str:
        """Détecte l'axe de symétrie utilisé"""
        if np.array_equal(output_arr, np.fliplr(input_arr)):
            return 'horizontal'
        elif np.array_equal(output_arr, np.flipud(input_arr)):
            return 'vertical'
        return 'inconnu'

    def detecter_rotation(self, input_arr: np.ndarray, output_arr: np.ndarray) -> Optional[int]:
        """Détecte si la sortie est une rotation de l'entrée"""
        # Rotation 90°
        if np.array_equal(output_arr, np.rot90(input_arr, 1)):
            return 90
        # Rotation 180°
        if np.array_equal(output_arr, np.rot90(input_arr, 2)):
            return 180
        # Rotation 270°
        if np.array_equal(output_arr, np.rot90(input_arr, 3)):
            return 270
        return None

    def detecter_pattern_repetitif(self, input_arr: np.ndarray, output_arr: np.ndarray) -> Optional[np.ndarray]:
        """Détecte si la sortie utilise un pattern répétitif de l'entrée"""
        # Cette analyse est simplifiée - dans un vrai solveur, elle serait plus sophistiquée
        h_in, w_in = input_arr.shape
        h_out, w_out = output_arr.shape

        # Si la sortie est plus grande, vérifier la répétition
        if h_out >= h_in and w_out >= w_in:
            # Extraire le pattern de base
            pattern = input_arr
            return pattern

        return None

    def categoriser_echec(self, transformations: List[Dict[str, Any]]) -> Tuple[str, str]:
        """Catégorise le type d'échec"""

        types_detectes = [t['type'] for t in transformations]
        type_majoritaire = max(set(types_detectes), key=types_detectes.count)

        categories_echec = {
            'remplissage_zone': ('detection_zones', 'Algorithme de détection de zones fermées'),
            'changement_taille': ('scaling_avance', 'Gestion des changements de taille complexes'),
            'changement_couleurs_complexe': ('mapping_couleurs', 'Système de mapping de couleurs avancé'),
            'symetrie': ('operations_symetrie', 'Application des opérations de symétrie'),
            'rotation': ('operations_rotation', 'Application des rotations'),
            'pattern_repetitif': ('detection_patterns', 'Détection de patterns répétitifs'),
            'transformation_complexe': ('analyse_semantique', 'Compréhension sémantique des transformations')
        }

        if type_majoritaire in categories_echec:
            return categories_echec[type_majoritaire]
        else:
            return ('categorie_inconnue', 'Pattern non classifié - nécessite analyse manuelle')

    def suggerer_implementation(self, type_echec: str, transformations: List[Dict[str, Any]]) -> str:
        """Suggère une implémentation pour corriger l'échec"""

        suggestions = {
            'detection_zones': """
def detecter_zones_fermees(grille):
    # Implémentation de l'algorithme de détection de zones
    # Utiliser un flood fill ou connected components
    zones = []
    # ... algorithme de détection ...
    return zones

def appliquer_remplissage_zone(grille, couleur_remplissage):
    zones = detecter_zones_fermees(grille)
    nouvelle_grille = grille.copy()
    for zone in zones:
        # Remplir la zone avec la couleur
        pass
    return nouvelle_grille
            """,

            'scaling_avance': """
def appliquer_changement_taille_intelligent(grille, nouvelle_hauteur, nouvelle_largeur):
    # Implémentation intelligente du changement de taille
    # Gérer les cas spéciaux (agrandissement, rétrécissement, ratios non uniformes)

    h_in, w_in = len(grille), len(grille[0])
    facteur_h = nouvelle_hauteur / h_in
    facteur_w = nouvelle_largeur / w_in

    # Créer la nouvelle grille
    nouvelle_grille = [[0 for _ in range(nouvelle_largeur)] for _ in range(nouvelle_hauteur)]

    # Appliquer la transformation appropriée
    if facteur_h == 2 and facteur_w == 2:
        return agrandir_x2(grille)
    elif facteur_h == 0.5 and facteur_w == 0.5:
        return retrecir_x2(grille)
    else:
        return redimensionner_generique(grille, nouvelle_hauteur, nouvelle_largeur)

    return nouvelle_grille
            """,

            'mapping_couleurs': """
def analyser_mapping_couleurs(exemples):
    # Analyser les exemples pour trouver le mapping de couleurs
    mappings = {}

    for exemple in exemples:
        couleurs_in = set().union(*exemple['input'])
        couleurs_out = set().union(*exemple['output'])

        # Trouver la correspondance la plus probable
        mapping = {}
        # ... algorithme de matching ...

    return mapping

def appliquer_mapping_couleurs(grille, mapping):
    nouvelle_grille = [[mapping.get(cell, cell) for cell in ligne] for ligne in grille]
    return nouvelle_grille
            """
        }

        return suggestions.get(type_echec, f"# Implémentation manuelle nécessaire pour {type_echec}\n# Analyser les exemples pour comprendre le pattern")

    def estimer_difficulte(self, type_echec: str, transformations: List[Dict[str, Any]]) -> str:
        """Estime la difficulté d'implémentation"""

        difficultes = {
            'detection_zones': 'facile',
            'scaling_avance': 'moyen',
            'mapping_couleurs': 'moyen',
            'operations_symetrie': 'facile',
            'operations_rotation': 'facile',
            'detection_patterns': 'difficile',
            'analyse_semantique': 'difficile'
        }

        return difficultes.get(type_echec, 'difficile')

    def trouver_exemples_similaires(self, puzzle_id: str, type_echec: str) -> List[str]:
        """Trouve d'autres puzzles avec le même type d'échec"""
        # Cette fonction pourrait scanner tous les puzzles pour trouver des patterns similaires
        # Pour l'instant, on retourne une liste vide
        return []

    def generer_plan_amelioration(self) -> str:
        """Génère un plan d'amélioration basé sur l'analyse des échecs"""

        if not self.echecs_analyses:
            return "Aucune analyse d'échec disponible"

        # Compter les types d'échecs
        stats_echecs = defaultdict(int)
        suggestions_uniques = {}

        for echec in self.echecs_analyses:
            stats_echecs[echec.type_echec] += 1
            if echec.type_echec not in suggestions_uniques:
                suggestions_uniques[echec.type_echec] = echec.suggestion_implementation

        plan = f"""
🚀 PLAN D'AMÉLIORATION DU SOLVEUR ARC
{'='*50}

📊 ANALYSE DES ÉCHECS ({len(self.echecs_analyses)} puzzles analysés):

"""

        # Trier par fréquence
        stats_tries = sorted(stats_echecs.items(), key=lambda x: x[1], reverse=True)

        for type_echec, count in stats_tries:
            pourcentage = (count / len(self.echecs_analyses)) * 100
            difficulte = next((e.difficulte_estimee for e in self.echecs_analyses if e.type_echec == type_echec), 'moyen')

            plan += f"""
🔧 {type_echec.upper()} ({count} puzzles, {pourcentage:.1f}%)
   Difficulté: {difficulte.upper()}
   Pattern manquant: {next((e.pattern_manquant for e in self.echecs_analyses if e.type_echec == type_echec), 'À déterminer')}

   💡 SUGGESTION D'IMPLÉMENTATION:
   {suggestions_uniques.get(type_echec, 'Suggestion non disponible')}
"""

        plan += f"""

🎯 PRIORITÉS D'AMÉLIORATION:

1. **Focalisation principale**: {stats_tries[0][0]} ({stats_tries[0][1]} cas)
2. **Amélioration rapide**: Travailler sur les patterns "facile"
3. **Évolution progressive**: Commencer par les cas simples

💪 PROCHAINES ÉTAPES:

1. **Implémenter le pattern le plus fréquent**
2. **Tester sur les puzzles échoués**
3. **Mesurer l'amélioration**
4. **Itérer sur le pattern suivant**

🎉 OBJECTIF: Améliorer significativement le taux de réussite !
"""

        return plan

def main():
    """Analyse des échecs du solveur ARC"""

    print("🔍 ANALYSEUR D'ÉCHECS ARC")
    print("========================")
    print("Analyse des puzzles échoués pour améliorer le solveur")
    print()

    analyseur = AnalyseurEchecsARC()

    # Liste des puzzles qui ont échoué dans le test précédent
    # (basé sur les résultats du test complet)
    puzzles_echoues = [
        '1be83260', '1e32b0e9', '0f63c0b9', '0d3d703e',
        '0c786b71', '0607ce86', '1c786137', '195ba7dc',
        '1a6449f1', '0becf7df', '0c9aba6e', '18286ef8',
        '1b2d62fb', '19bb5feb'  # Ces puzzles n'avaient pas de pattern identifiable
    ]

    print(f"🎯 Analyse de {len(puzzles_echoues)} puzzles échoués:")
    for puzzle in puzzles_echoues[:10]:  # Limiter à 10 pour l'exemple
        print(f"   • {puzzle}")
    print()

    # Analyser un échantillon des échecs
    echantillon_echoues = puzzles_echoues[:5]  # Analyser les 5 premiers

    for puzzle_id in echantillon_echoues:
        try:
            analyse = analyseur.analyser_echec_detaille(puzzle_id)
            print(f"✅ Analyse terminée pour {puzzle_id}")
            print(f"   Type d'échec: {analyse.type_echec}")
            print(f"   Pattern manquant: {analyse.pattern_manquant}")
            print(f"   Difficulté estimée: {analyse.difficulte_estimee}")
            print()
        except Exception as e:
            print(f"❌ Erreur lors de l'analyse de {puzzle_id}: {e}")
            print()

    # Générer le plan d'amélioration
    if analyseur.echecs_analyses:
        plan = analyseur.generer_plan_amelioration()
        print(plan)

        # Sauvegarder le plan
        with open('plan_amelioration_solveur.txt', 'w', encoding='utf-8') as f:
            f.write(plan)
        print("💾 Plan d'amélioration sauvegardé dans 'plan_amelioration_solveur.txt'")

    print("🎉 Analyse des échecs terminée !")
    print("Nous avons maintenant un plan clair pour améliorer le solveur.")

if __name__ == "__main__":
    main()
