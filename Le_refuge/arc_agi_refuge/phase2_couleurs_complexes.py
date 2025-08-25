#!/usr/bin/env python3
"""
🎨 Phase 2: Gestion des Couleurs Complexes
Module pour gérer les transformations de couleurs identifiées dans l'audit (47.5% des puzzles)
"""

from typing import List, Dict, Any, Tuple, Set
from collections import Counter, defaultdict
import numpy as np

class GestionnaireCouleursComplexes:
    def __init__(self):
        self.confiance_minimale = 0.7

    def detecter_pattern_couleurs(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """
        Détecte les patterns complexes de transformation de couleurs
        """
        couleurs_in = set()
        couleurs_out = set()

        for row in input_grid:
            couleurs_in.update(row)
        for row in output_grid:
            couleurs_out.update(row)

        # Si même nombre de couleurs, pas de transformation complexe
        if len(couleurs_in) == len(couleurs_out) and couleurs_in == couleurs_out:
            return {'detecte': False, 'raison': 'même ensemble de couleurs'}

        # Analyser le type de transformation de couleurs
        type_transformation = self._classifier_transformation_couleurs(couleurs_in, couleurs_out)

        if type_transformation == 'remplacement_simple':
            return self._analyser_remplacement_simple(input_grid, output_grid, couleurs_in, couleurs_out)
        elif type_transformation == 'ajout_couleurs':
            return self._analyser_ajout_couleurs(input_grid, output_grid, couleurs_in, couleurs_out)
        elif type_transformation == 'suppression_couleurs':
            return self._analyser_suppression_couleurs(input_grid, output_grid, couleurs_in, couleurs_out)
        elif type_transformation == 'remplacement_multiple':
            return self._analyser_remplacement_multiple(input_grid, output_grid, couleurs_in, couleurs_out)
        elif type_transformation == 'transformation_conditionnelle':
            return self._analyser_transformation_conditionnelle(input_grid, output_grid)

        return {'detecte': False, 'raison': 'pattern de couleurs non reconnu'}

    def _classifier_transformation_couleurs(self, couleurs_in: Set[int], couleurs_out: Set[int]) -> str:
        """Classifie le type de transformation de couleurs"""
        couleurs_ajoutees = couleurs_out - couleurs_in
        couleurs_supprimees = couleurs_in - couleurs_out
        couleurs_conservees = couleurs_in & couleurs_out

        # Si des couleurs sont ajoutées mais aucune supprimée
        if couleurs_ajoutees and not couleurs_supprimees:
            return 'ajout_couleurs'

        # Si des couleurs sont supprimées mais aucune ajoutée
        if couleurs_supprimees and not couleurs_ajoutees:
            return 'suppression_couleurs'

        # Si même nombre de couleurs mais différentes
        if len(couleurs_in) == len(couleurs_out) and couleurs_in != couleurs_out:
            return 'remplacement_simple'

        # Si nombre de couleurs différent dans les deux sens
        if couleurs_ajoutees and couleurs_supprimees:
            return 'remplacement_multiple'

        # Cas complexe - transformation conditionnelle
        return 'transformation_conditionnelle'

    def _analyser_remplacement_simple(self, input_grid: List[List[int]], output_grid: List[List[int]],
                                    couleurs_in: Set[int], couleurs_out: Set[int]) -> Dict[str, Any]:
        """Analyse un remplacement simple de couleurs"""
        # Créer mapping couleur_in → couleur_out
        mapping_couleurs = {}
        confiance_mapping = {}

        for couleur_in in couleurs_in:
            positions_in = [(i, j) for i, row in enumerate(input_grid) for j, val in enumerate(row) if val == couleur_in]
            if not positions_in:
                continue

            # Voir quelle couleur sortante correspond
            couleurs_correspondantes = []
            for i, j in positions_in:
                if i < len(output_grid) and j < len(output_grid[0]):
                    couleurs_correspondantes.append(output_grid[i][j])

            if couleurs_correspondantes:
                couleur_principale = Counter(couleurs_correspondantes).most_common(1)[0]
                mapping_couleurs[couleur_in] = couleur_principale[0]
                confiance_mapping[couleur_in] = couleur_principale[1] / len(couleurs_correspondantes)

        # Calculer confiance globale
        if confiance_mapping:
            confiance_moyenne = sum(confiance_mapping.values()) / len(confiance_mapping)
        else:
            confiance_moyenne = 0

        return {
            'detecte': True,
            'type': 'remplacement_simple',
            'mapping_couleurs': mapping_couleurs,
            'confiance_mapping': confiance_mapping,
            'confiance': confiance_moyenne,
            'explication': f"Remplacement simple de {len(mapping_couleurs)} couleurs avec {confiance_moyenne:.1%} de cohérence"
        }

    def _analyser_ajout_couleurs(self, input_grid: List[List[int]], output_grid: List[List[int]],
                               couleurs_in: Set[int], couleurs_out: Set[int]) -> Dict[str, Any]:
        """Analyse l'ajout de nouvelles couleurs"""
        couleurs_ajoutees = couleurs_out - couleurs_in

        # Analyser où sont placées les nouvelles couleurs
        positions_nouvelles_couleurs = defaultdict(list)

        for i in range(len(output_grid)):
            for j in range(len(output_grid[0])):
                if output_grid[i][j] in couleurs_ajoutees:
                    positions_nouvelles_couleurs[output_grid[i][j]].append((i, j))

        # Analyser la régularité du placement
        regularite_placement = {}
        for couleur, positions in positions_nouvelles_couleurs.items():
            if len(positions) > 1:
                # Calculer la régularité spatiale
                rows = [pos[0] for pos in positions]
                cols = [pos[1] for pos in positions]
                regularite_rows = 1.0 - (len(set(rows)) - 1) / len(rows) if len(rows) > 1 else 1.0
                regularite_cols = 1.0 - (len(set(cols)) - 1) / len(cols) if len(cols) > 1 else 1.0
                regularite_placement[couleur] = (regularite_rows + regularite_cols) / 2
            else:
                regularite_placement[couleur] = 1.0

        # Calculer confiance
        confiance_moyenne = sum(regularite_placement.values()) / len(regularite_placement) if regularite_placement else 0

        return {
            'detecte': True,
            'type': 'ajout_couleurs',
            'couleurs_ajoutees': list(couleurs_ajoutees),
            'positions_nouvelles_couleurs': dict(positions_nouvelles_couleurs),
            'regularite_placement': regularite_placement,
            'confiance': confiance_moyenne,
            'explication': f"Ajout de {len(couleurs_ajoutees)} nouvelles couleurs avec {confiance_moyenne:.1%} de régularité"
        }

    def _analyser_suppression_couleurs(self, input_grid: List[List[int]], output_grid: List[List[int]],
                                     couleurs_in: Set[int], couleurs_out: Set[int]) -> Dict[str, Any]:
        """Analyse la suppression de couleurs"""
        couleurs_supprimees = couleurs_in - couleurs_out

        # Vérifier que les couleurs supprimées sont bien absentes de la sortie
        couleurs_trouvees = set()
        for row in output_grid:
            couleurs_trouvees.update(row)

        couleurs_reellement_supprimees = couleurs_supprimees - couleurs_trouvees
        taux_suppression = len(couleurs_reellement_supprimees) / len(couleurs_supprimees) if couleurs_supprimees else 0

        return {
            'detecte': True,
            'type': 'suppression_couleurs',
            'couleurs_supprimees': list(couleurs_supprimees),
            'couleurs_reellement_supprimees': list(couleurs_reellement_supprimees),
            'taux_suppression': taux_suppression,
            'confiance': taux_suppression,
            'explication': f"Suppression de {len(couleurs_supprimees)} couleurs avec {taux_suppression:.1%} de succès"
        }

    def _analyser_remplacement_multiple(self, input_grid: List[List[int]], output_grid: List[List[int]],
                                      couleurs_in: Set[int], couleurs_out: Set[int]) -> Dict[str, Any]:
        """Analyse un remplacement multiple de couleurs"""
        # Cas complexe - version simplifiée pour l'instant
        return {
            'detecte': True,
            'type': 'remplacement_multiple',
            'confiance': 0.6,
            'explication': "Remplacement multiple de couleurs détecté - pattern complexe"
        }

    def _analyser_transformation_conditionnelle(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """Analyse une transformation conditionnelle de couleurs"""
        # Cas très complexe - version basique pour l'instant
        return {
            'detecte': True,
            'type': 'transformation_conditionnelle',
            'confiance': 0.5,
            'explication': "Transformation conditionnelle de couleurs détectée - pattern très complexe"
        }

    def appliquer_pattern_couleurs(self, input_grid: List[List[int]], pattern_couleurs: Dict[str, Any]) -> List[List[int]]:
        """Applique un pattern de transformation de couleurs"""
        if pattern_couleurs['type'] == 'remplacement_simple':
            return self._appliquer_remplacement_simple(input_grid, pattern_couleurs)
        elif pattern_couleurs['type'] == 'ajout_couleurs':
            return self._appliquer_ajout_couleurs(input_grid, pattern_couleurs)
        elif pattern_couleurs['type'] == 'suppression_couleurs':
            return self._appliquer_suppression_couleurs(input_grid, pattern_couleurs)

        # Pour les patterns complexes non implémentés, retourner l'input tel quel
        return input_grid

    def _appliquer_remplacement_simple(self, input_grid: List[List[int]], pattern: Dict[str, Any]) -> List[List[int]]:
        """Applique un remplacement simple de couleurs"""
        mapping = pattern['mapping_couleurs']
        grille_resultat = []

        for i, row in enumerate(input_grid):
            nouvelle_row = []
            for j, val in enumerate(row):
                nouvelle_row.append(mapping.get(val, val))  # Garder la valeur si pas dans mapping
            grille_resultat.append(nouvelle_row)

        return grille_resultat

    def _appliquer_ajout_couleurs(self, input_grid: List[List[int]], pattern: Dict[str, Any]) -> List[List[int]]:
        """Applique l'ajout de couleurs"""
        # Version simplifiée: ajouter des couleurs à des positions vides
        grille_resultat = [row[:] for row in input_grid]  # Copie

        # Ajouter les couleurs à des positions stratégiques
        couleurs_ajoutees = pattern.get('couleurs_ajoutees', [])
        if couleurs_ajoutees:
            couleur_ajoutee = couleurs_ajoutees[0]  # Prendre la première couleur

            # Ajouter à des positions vides
            for i in range(len(grille_resultat)):
                for j in range(len(grille_resultat[0])):
                    if grille_resultat[i][j] == 0:  # Position vide
                        grille_resultat[i][j] = couleur_ajoutee
                        break
                else:
                    continue
                break

        return grille_resultat

    def _appliquer_suppression_couleurs(self, input_grid: List[List[int]], pattern: Dict[str, Any]) -> List[List[int]]:
        """Applique la suppression de couleurs"""
        couleurs_a_supprimer = set(pattern.get('couleurs_supprimees', []))
        grille_resultat = []

        for row in input_grid:
            nouvelle_row = [0 if val in couleurs_a_supprimer else val for val in row]
            grille_resultat.append(nouvelle_row)

        return grille_resultat

# Instance globale
gestionnaire_couleurs = GestionnaireCouleursComplexes()

def detecter_pattern_couleurs(input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
    """Fonction principale pour détecter les patterns de couleurs complexes"""
    return gestionnaire_couleurs.detecter_pattern_couleurs(input_grid, output_grid)

def appliquer_pattern_couleurs(input_grid: List[List[int]], pattern_couleurs: Dict[str, Any]) -> List[List[int]]:
    """Fonction principale pour appliquer les patterns de couleurs complexes"""
    return gestionnaire_couleurs.appliquer_pattern_couleurs(input_grid, pattern_couleurs)

if __name__ == "__main__":
    print("=== TEST PATTERNS COULEURS COMPLEXES ===")

    # Test 1: Remplacement simple
    input1 = [[1, 2, 3], [4, 1, 2], [3, 4, 1]]
    output1 = [[5, 6, 7], [8, 5, 6], [7, 8, 5]]

    pattern1 = detecter_pattern_couleurs(input1, output1)
    print(f"Remplacement simple détecté: {pattern1['detecte']}")
    if pattern1['detecte']:
        print(f"Type: {pattern1['type']}")
        print(".1%")
        print(f"Mapping: {pattern1.get('mapping_couleurs', {})}")

    # Test 2: Ajout de couleurs
    input2 = [[1, 0, 3], [0, 1, 0], [3, 0, 1]]
    output2 = [[1, 2, 3], [2, 1, 2], [3, 2, 1]]

    pattern2 = detecter_pattern_couleurs(input2, output2)
    print(f"\nAjout de couleurs détecté: {pattern2['detecte']}")
    if pattern2['detecte']:
        print(f"Type: {pattern2['type']}")
        print(".1%")
        print(f"Couleurs ajoutées: {pattern2.get('couleurs_ajoutees', [])}")
