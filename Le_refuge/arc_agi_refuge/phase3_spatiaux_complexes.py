#!/usr/bin/env python3
"""
🌀 Phase 3: Patterns Spatiaux Complexes
Module pour gérer les transformations spatiales complexes identifiées dans l'audit (27.5% des puzzles)
"""

from typing import List, Dict, Any, Tuple, Set
from collections import Counter, defaultdict
import numpy as np

class GestionnairePatternsSpatiaux:
    def __init__(self):
        self.confiance_minimale = 0.6

    def detecter_pattern_spatial(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """
        Détecte les patterns spatiaux complexes (transformations 2D non-linéaires)
        """
        # Vérifier si c'est un cas simple déjà couvert
        if self._est_cas_simple(input_grid, output_grid):
            return {'detecte': False, 'raison': 'cas simple déjà couvert'}

        # Analyser le type de transformation spatiale
        type_spatial = self._classifier_transformation_spatiale(input_grid, output_grid)

        if type_spatial == 'symetrie_avancee':
            return self._analyser_symetrie_avancee(input_grid, output_grid)
        elif type_spatial == 'rotation_complexe':
            return self._analyser_rotation_complexe(input_grid, output_grid)
        elif type_spatial == 'deformation_grille':
            return self._analyser_deformation_grille(input_grid, output_grid)
        elif type_spatial == 'remplissage_intelligent':
            return self._analyser_remplissage_intelligent(input_grid, output_grid)
        elif type_spatial == 'transformation_morphologique':
            return self._analyser_transformation_morphologique(input_grid, output_grid)

        return {'detecte': False, 'raison': 'pattern spatial non reconnu'}

    def _est_cas_simple(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> bool:
        """Vérifie si c'est un cas déjà couvert par les patterns existants"""
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        # Cas simples déjà couverts:
        # 1. Même dimensions et même couleurs = déjà géré
        # 2. Changement de dimensions simple = déjà géré
        # 3. Patterns diagonaux = déjà géré
        couleurs_in = set()
        couleurs_out = set()

        for row in input_grid:
            couleurs_in.update(row)
        for row in output_grid:
            couleurs_out.update(row)

        # Si dimensions et couleurs identiques = probablement déjà géré
        if (h_in, w_in) == (h_out, w_out) and couleurs_in == couleurs_out:
            return True

        # Si changement de dimensions simple = déjà géré
        if couleurs_in == couleurs_out and h_out > 0 and w_out > 0:
            ratio_h = h_out / h_in if h_in > 0 else 0
            ratio_w = w_out / w_in if w_in > 0 else 0
            if ratio_h == ratio_w and ratio_h in [0.5, 2, 4]:
                return True

        return False

    def _classifier_transformation_spatiale(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> str:
        """Classifie le type de transformation spatiale"""
        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        # Analyser les positions des éléments non-zéro
        positions_in = []
        positions_out = []

        for i in range(h_in):
            for j in range(w_in):
                if input_grid[i][j] != 0:
                    positions_in.append((i, j, input_grid[i][j]))

        for i in range(h_out):
            for j in range(w_out):
                if output_grid[i][j] != 0:
                    positions_out.append((i, j, output_grid[i][j]))

        # Si même nombre d'éléments, analyser les transformations
        if len(positions_in) == len(positions_out):
            # Vérifier si c'est une symétrie complexe
            if self._detecte_symetrie_complexe(positions_in, positions_out):
                return 'symetrie_avancee'

            # Vérifier si c'est une rotation complexe
            if self._detecte_rotation_complexe(positions_in, positions_out):
                return 'rotation_complexe'

            # Vérifier si c'est une déformation de grille
            if self._detecte_deformation_grille(positions_in, positions_out):
                return 'deformation_grille'

        # Si nombre d'éléments différent, analyser les remplissages
        if len(positions_out) > len(positions_in):
            return 'remplissage_intelligent'

        # Cas général
        return 'transformation_morphologique'

    def _detecte_symetrie_complexe(self, positions_in: List[Tuple], positions_out: List[Tuple]) -> bool:
        """Détecte les symétries complexes (non-linéaires)"""
        if len(positions_in) != len(positions_out):
            return False

        # Analyser les transformations de coordonnées
        transformations = []
        for (i_in, j_in, val_in), (i_out, j_out, val_out) in zip(positions_in, positions_out):
            if val_in == val_out:  # Même valeur
                transformations.append(((i_in, j_in), (i_out, j_out)))

        if len(transformations) < 3:  # Pas assez de points
            return False

        # Vérifier si c'est une transformation non-linéaire
        # (plus complexe qu'une simple translation, rotation, ou symétrie de base)
        linear_transforms = self._compter_transformations_lineaires(transformations)

        # Si moins de 80% des transformations sont linéaires = transformation complexe
        return linear_transforms / len(transformations) < 0.8

    def _detecte_rotation_complexe(self, positions_in: List[Tuple], positions_out: List[Tuple]) -> bool:
        """Détecte les rotations complexes (non 90/180/270 degrés)"""
        if len(positions_in) != len(positions_out):
            return False

        # Calculer les angles de rotation
        angles = []
        for (i_in, j_in, val_in), (i_out, j_out, val_out) in zip(positions_in, positions_out):
            if val_in == val_out:
                # Calculer l'angle entre les deux points par rapport au centre
                centre_in = (len(positions_in) // 2, len(positions_in) // 2)  # Approximation
                centre_out = (len(positions_out) // 2, len(positions_out) // 2)

                angle_in = np.arctan2(i_in - centre_in[0], j_in - centre_in[1])
                angle_out = np.arctan2(i_out - centre_out[0], j_out - centre_out[1])

                angle_diff = (angle_out - angle_in) * 180 / np.pi
                angles.append(angle_diff)

        if not angles:
            return False

        # Si les angles ne sont pas multiples de 90° = rotation complexe
        angles_non_standard = [a for a in angles if abs(a % 90) > 10]
        return len(angles_non_standard) / len(angles) > 0.5

    def _detecte_deformation_grille(self, positions_in: List[Tuple], positions_out: List[Tuple]) -> bool:
        """Détecte les déformations de grille (stretching, warping)"""
        if len(positions_in) != len(positions_out):
            return False

        # Analyser les ratios de transformation
        ratios_i = []
        ratios_j = []

        for (i_in, j_in, val_in), (i_out, j_out, val_out) in zip(positions_in, positions_out):
            if val_in == val_out and i_in != 0 and j_in != 0:
                ratios_i.append(i_out / i_in)
                ratios_j.append(j_out / j_in)

        if len(ratios_i) < 3 or len(ratios_j) < 3:
            return False

        # Si les ratios varient beaucoup = déformation
        variance_i = np.var(ratios_i)
        variance_j = np.var(ratios_j)

        return variance_i > 0.5 or variance_j > 0.5

    def _compter_transformations_lineaires(self, transformations: List[Tuple]) -> int:
        """Compte les transformations linéaires simples"""
        linear_count = 0

        for (pos_in, pos_out) in transformations:
            i_in, j_in = pos_in
            i_out, j_out = pos_out

            # Vérifier les transformations linéaires de base
            is_translation = abs(i_out - i_in) == abs(j_out - j_in) == 0
            is_reflection = (i_out == i_in and j_out == -j_in) or (i_out == -i_in and j_out == j_in)
            is_rotation_90 = (i_out == -j_in and j_out == i_in)
            is_rotation_180 = (i_out == -i_in and j_out == -j_in)
            is_rotation_270 = (i_out == j_in and j_out == -i_in)

            if any([is_translation, is_reflection, is_rotation_90, is_rotation_180, is_rotation_270]):
                linear_count += 1

        return linear_count

    def _analyser_symetrie_avancee(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse une symétrie avancée"""
        confiance = 0.7
        explication = "Symétrie avancée détectée - transformation non-linéaire"

        return {
            'detecte': True,
            'type': 'symetrie_avancee',
            'confiance': confiance,
            'explication': explication
        }

    def _analyser_rotation_complexe(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse une rotation complexe"""
        confiance = 0.75
        explication = "Rotation complexe détectée - angle non-standard"

        return {
            'detecte': True,
            'type': 'rotation_complexe',
            'confiance': confiance,
            'explication': explication
        }

    def _analyser_deformation_grille(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse une déformation de grille"""
        confiance = 0.65
        explication = "Déformation de grille détectée - transformation non-uniforme"

        return {
            'detecte': True,
            'type': 'deformation_grille',
            'confiance': confiance,
            'explication': explication
        }

    def _analyser_remplissage_intelligent(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse un remplissage intelligent"""
        # Compter les éléments ajoutés
        elements_in = sum(1 for row in input_grid for cell in row if cell != 0)
        elements_out = sum(1 for row in output_grid for cell in row if cell != 0)
        elements_ajoutes = elements_out - elements_in

        confiance = min(0.8, 0.5 + (elements_ajoutes / 50))  # Plus d'éléments = plus de confiance
        explication = f"Remplissage intelligent détecté - {elements_ajoutes} éléments ajoutés"

        return {
            'detecte': True,
            'type': 'remplissage_intelligent',
            'confiance': confiance,
            'elements_ajoutes': elements_ajoutes,
            'explication': explication
        }

    def _analyser_transformation_morphologique(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse une transformation morphologique générale"""
        confiance = 0.6
        explication = "Transformation morphologique complexe détectée"

        return {
            'detecte': True,
            'type': 'transformation_morphologique',
            'confiance': confiance,
            'explication': explication
        }

    def appliquer_pattern_spatial(self, input_grid: List[List[int]], pattern_spatial: Dict[str, Any]) -> List[List[int]]:
        """Applique un pattern spatial complexe"""
        if pattern_spatial['type'] == 'symetrie_avancee':
            return self._appliquer_symetrie_avancee(input_grid, pattern_spatial)
        elif pattern_spatial['type'] == 'rotation_complexe':
            return self._appliquer_rotation_complexe(input_grid, pattern_spatial)
        elif pattern_spatial['type'] == 'deformation_grille':
            return self._appliquer_deformation_grille(input_grid, pattern_spatial)
        elif pattern_spatial['type'] == 'remplissage_intelligent':
            return self._appliquer_remplissage_intelligent(input_grid, pattern_spatial)
        elif pattern_spatial['type'] == 'transformation_morphologique':
            return self._appliquer_transformation_morphologique(input_grid, pattern_spatial)

        return input_grid

    def _appliquer_symetrie_avancee(self, input_grid: List[List[int]], pattern: Dict[str, Any]) -> List[List[int]]:
        """Applique une symétrie avancée"""
        # Version simplifiée: appliquer une symétrie de base
        return input_grid  # TODO: Implémenter la vraie logique

    def _appliquer_rotation_complexe(self, input_grid: List[List[int]], pattern: Dict[str, Any]) -> List[List[int]]:
        """Applique une rotation complexe"""
        # Version simplifiée
        return input_grid  # TODO: Implémenter la vraie logique

    def _appliquer_deformation_grille(self, input_grid: List[List[int]], pattern: Dict[str, Any]) -> List[List[int]]:
        """Applique une déformation de grille"""
        # Version simplifiée
        return input_grid  # TODO: Implémenter la vraie logique

    def _appliquer_remplissage_intelligent(self, input_grid: List[List[int]], pattern: Dict[str, Any]) -> List[List[int]]:
        """Applique un remplissage intelligent"""
        # Ajouter des éléments dans les zones vides de manière intelligente
        grille_resultat = [row[:] for row in input_grid]

        # Chercher les couleurs existantes pour le remplissage
        couleurs_existantes = set()
        for row in input_grid:
            couleurs_existantes.update(row)
        couleurs_existantes.discard(0)  # Retirer le vide

        if couleurs_existantes:
            couleur_remplissage = min(couleurs_existantes)  # Prendre la plus petite couleur

            # Remplir les positions vides intelligemment
            h, w = len(grille_resultat), len(grille_resultat[0])
            for i in range(h):
                for j in range(w):
                    if grille_resultat[i][j] == 0:
                        # Remplir avec la couleur de remplissage
                        grille_resultat[i][j] = couleur_remplissage

        return grille_resultat

    def _appliquer_transformation_morphologique(self, input_grid: List[List[int]], pattern: Dict[str, Any]) -> List[List[int]]:
        """Applique une transformation morphologique générale"""
        # Version basique: retourner l'input tel quel
        return input_grid  # TODO: Implémenter la vraie logique

# Instance globale
gestionnaire_spatiaux = GestionnairePatternsSpatiaux()

def detecter_pattern_spatial(input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
    """Fonction principale pour détecter les patterns spatiaux complexes"""
    return gestionnaire_spatiaux.detecter_pattern_spatial(input_grid, output_grid)

def appliquer_pattern_spatial(input_grid: List[List[int]], pattern_spatial: Dict[str, Any]) -> List[List[int]]:
    """Fonction principale pour appliquer les patterns spatiaux complexes"""
    return gestionnaire_spatiaux.appliquer_pattern_spatial(input_grid, pattern_spatial)

if __name__ == "__main__":
    print("=== TEST PATTERNS SPATIAUX COMPLEXES ===")

    # Test 1: Remplissage intelligent
    input1 = [[1, 0, 3], [0, 1, 0], [3, 0, 1]]
    output1 = [[1, 2, 3], [2, 1, 2], [3, 2, 1]]

    pattern1 = detecter_pattern_spatial(input1, output1)
    print(f"Remplissage intelligent détecté: {pattern1['detecte']}")
    if pattern1['detecte']:
        print(f"Type: {pattern1['type']}")
        print(".1%")
        print(f"Explication: {pattern1['explication']}")

        # Appliquer le pattern
        resultat = appliquer_pattern_spatial(input1, pattern1)
        print(f"Résultat: {resultat}")

    # Test 2: Déformation de grille
    input2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output2 = [[1, 0, 2, 0, 3], [0, 4, 0, 5, 0], [7, 0, 8, 0, 9]]  # Grille étirée

    pattern2 = detecter_pattern_spatial(input2, output2)
    print(f"\nDéformation de grille détectée: {pattern2['detecte']}")
    if pattern2['detecte']:
        print(f"Type: {pattern2['type']}")
        print(".1%")
        print(f"Explication: {pattern2['explication']}")
