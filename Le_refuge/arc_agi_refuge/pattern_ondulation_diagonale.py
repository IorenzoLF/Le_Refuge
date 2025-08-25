#!/usr/bin/env python3
"""
🌊 PATTERN ONDULATION DIAGONALE
Implémentation du pattern découvert sur 05269061
Inspiré par: onde + alternance + diagonale
"""

from typing import List, Dict, Any
import numpy as np

class PatternOndulationDiagonale:
    """
    Pattern d'ondulation diagonale avec alternance
    Découvert sur 05269061: onde de 3 couleurs avec alternance lignes paires/impaires
    """

    def __init__(self):
        self.nom = "ondulation_diagonale"
        self.description = "Propagation diagonale avec alternance lignes paires/impaires"
        self.priorite = 85  # Haute priorité car pattern complexe et spécifique

    def detecter(self, input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
        """
        Détecte le pattern d'ondulation diagonale avec décalage progressif
        """
        if not input_grid or not output_grid:
            return {'detecte': False, 'confiance': 0.0}

        h_in, w_in = len(input_grid), len(input_grid[0])
        h_out, w_out = len(output_grid), len(output_grid[0])

        # Vérifications de base
        if h_out != w_out:  # Doit être carré
            return {'detecte': False, 'confiance': 0.0}

        # Extraire les couleurs de l'input
        couleurs_sequence = []
        for i in range(h_in):
            for j in range(w_in):
                if input_grid[i][j] != 0 and input_grid[i][j] not in couleurs_sequence:
                    couleurs_sequence.append(input_grid[i][j])

        if len(couleurs_sequence) < 2:  # Au moins 2 couleurs
            return {'detecte': False, 'confiance': 0.0}

        # NOUVELLE APPROCHE: Vérifier décalage progressif diagonal
        confiance = 0.0

        # 1. Vérifier propagation diagonale sur toute la grille
        confiance_propagation = self._verifier_propagation_complette(output_grid, couleurs_sequence)
        confiance += confiance_propagation * 0.6

        # 2. Vérifier pattern de décalage entre lignes
        confiance_decalage = self._verifier_decalage_progressif(output_grid, couleurs_sequence)
        confiance += confiance_decalage * 0.4

        # Seuil de détection plus souple pour ce pattern complexe
        detecte = confiance > 0.4  # Plus souple car pattern complexe

        return {
            'detecte': detecte,
            'confiance': confiance,
            'pattern': self.nom,
            'couleurs_sequence': couleurs_sequence,
            'propagation_confiance': confiance_propagation,
            'decalage_confiance': confiance_decalage,
            'description': f"Ondulation diagonale avec {len(couleurs_sequence)} couleurs - décalage progressif"
        }

    def _verifier_propagation_diagonale(self, pattern: List[List[int]], couleurs_sequence: List[int]) -> float:
        """Vérifie si le pattern suit une propagation diagonale"""
        if not pattern or not couleurs_sequence or not isinstance(pattern, list) or len(pattern) == 0:
            return 0.0

        # Vérifier que pattern est bien une liste 2D
        if not isinstance(pattern[0], list):
            return 0.0

        h, w = len(pattern), len(pattern[0])
        correspondances = 0
        total_cells = 0

        for i in range(h):
            for j in range(w):
                if pattern[i][j] != 0:
                    total_cells += 1
                    couleur_theorique = couleurs_sequence[(i + j) % len(couleurs_sequence)]
                    if pattern[i][j] == couleur_theorique:
                        correspondances += 1

        return correspondances / total_cells if total_cells > 0 else 0.0

    def _verifier_relation_patterns(self, pattern_paire: List[List[int]], pattern_impaire: List[List[int]], couleurs_sequence: List[int]) -> float:
        """Vérifie la relation entre patterns paires et impairs"""
        if not pattern_paire or not pattern_impaire or not couleurs_sequence:
            return 0.0

        # Vérifications de sécurité
        if not isinstance(pattern_paire, list) or not isinstance(pattern_impaire, list):
            return 0.0

        if len(pattern_paire) == 0 or len(pattern_impaire) == 0:
            return 0.0

        if not isinstance(pattern_paire[0], list) or not isinstance(pattern_impaire[0], list):
            return 0.0

        # Chercher un décalage qui fait correspondre les patterns
        w = len(pattern_paire[0])
        decalages_possibles = list(range(-w+1, w))

        for decalage in decalages_possibles:
            correspondances = 0
            total_comparaisons = 0

            for j in range(w):
                pos_impaire = j + decalage
                if 0 <= pos_impaire < w:
                    for i in range(len(pattern_paire)):
                        couleur_paire = pattern_paire[i][j]
                        couleur_impaire = pattern_impaire[i][pos_impaire]

                        if couleur_paire != 0 and couleur_impaire != 0:
                            total_comparaisons += 1
                            # Vérifier si c'est le décalage attendu dans la séquence
                            try:
                                idx_paire = couleurs_sequence.index(couleur_paire)
                                couleur_attendue = couleurs_sequence[(idx_paire + 1) % len(couleurs_sequence)]
                                if couleur_impaire == couleur_attendue:
                                    correspondances += 1
                            except ValueError:
                                # Couleur non trouvée dans séquence
                                pass

            if total_comparaisons > 0 and correspondances / total_comparaisons > 0.5:
                return 1.0

        return 0.0

    def _verifier_propagation_complette(self, output_grid: List[List[int]], couleurs_sequence: List[int]) -> float:
        """Vérifie la propagation diagonale sur toute la grille"""
        if not output_grid or not couleurs_sequence:
            return 0.0

        h, w = len(output_grid), len(output_grid[0])
        correspondances = 0
        total_cells = 0

        for i in range(h):
            for j in range(w):
                if output_grid[i][j] != 0:
                    total_cells += 1
                    # Position dans la séquence basée sur la diagonale
                    position_diagonale = (i + j) % len(couleurs_sequence)
                    couleur_attendue = couleurs_sequence[position_diagonale]

                    if output_grid[i][j] == couleur_attendue:
                        correspondances += 1

        return correspondances / total_cells if total_cells > 0 else 0.0

    def _verifier_decalage_progressif(self, output_grid: List[List[int]], couleurs_sequence: List[int]) -> float:
        """Vérifie le décalage progressif entre les lignes"""
        if not output_grid or len(output_grid) < 2:
            return 0.0

        h = len(output_grid)
        decalages_reussis = 0
        total_comparaisons = 0

        # Vérifier chaque paire de lignes successives
        for i in range(h - 1):
            ligne1 = output_grid[i]
            ligne2 = output_grid[i + 1]

            # Chercher un décalage qui fait correspondre les couleurs
            decalage_trouve = False
            for decalage in range(-len(ligne1) + 1, len(ligne1)):
                correspondances_locales = 0
                cellules_comparees = 0

                for j in range(len(ligne1)):
                    pos2 = j + decalage
                    if 0 <= pos2 < len(ligne2):
                        cellules_comparees += 1
                        if ligne1[j] != 0 and ligne2[pos2] != 0:
                            # Vérifier si les couleurs correspondent selon la logique diagonale
                            pos_diag1 = (i + j) % len(couleurs_sequence)
                            pos_diag2 = (i + 1 + pos2) % len(couleurs_sequence)

                            if (ligne1[j] == couleurs_sequence[pos_diag1] and
                                ligne2[pos2] == couleurs_sequence[pos_diag2]):
                                correspondances_locales += 1

                if cellules_comparees > 0 and correspondances_locales / cellules_comparees > 0.6:
                    decalage_trouve = True
                    break

            if decalage_trouve:
                decalages_reussis += 1
            total_comparaisons += 1

        return decalages_reussis / total_comparaisons if total_comparaisons > 0 else 0.0

    def appliquer(self, input_grid: List[List[int]], output_attendu: List[List[int]] = None) -> List[List[int]]:
        """
        Applique le pattern d'ondulation diagonale
        """
        if not input_grid:
            return input_grid

        h_in, w_in = len(input_grid), len(input_grid[0])

        # Déterminer taille de sortie
        if output_attendu:
            h_out, w_out = len(output_attendu), len(output_attendu[0])
        else:
            # Par défaut, même taille que l'input
            h_out, w_out = h_in, w_in

        # Extraire séquence de couleurs
        couleurs_sequence = []
        for i in range(h_in):
            for j in range(w_in):
                if input_grid[i][j] != 0 and input_grid[i][j] not in couleurs_sequence:
                    couleurs_sequence.append(input_grid[i][j])

        if not couleurs_sequence:
            couleurs_sequence = [1, 2, 3]  # Fallback

        # Créer grille de sortie
        output_grid = [[0 for _ in range(w_out)] for _ in range(h_out)]

        # Appliquer pattern d'ondulation diagonale avec alternance
        for i in range(h_out):
            for j in range(w_out):
                # Calcul de la position dans la séquence
                sequence_pos = (i + j) % len(couleurs_sequence)

                # Appliquer l'alternance: lignes impaires ont un décalage
                if i % 2 == 1:  # Ligne impaire
                    sequence_pos = (sequence_pos + 1) % len(couleurs_sequence)

                output_grid[i][j] = couleurs_sequence[sequence_pos]

        return output_grid

# Instance globale
pattern_ondulation = PatternOndulationDiagonale()

def detecter_pattern_ondulation_diagonale(input_grid: List[List[int]], output_grid: List[List[int]]) -> Dict[str, Any]:
    """Fonction wrapper pour la détection"""
    return pattern_ondulation.detecter(input_grid, output_grid)

def appliquer_pattern_ondulation_diagonale(input_grid: List[List[int]], output_attendu: List[List[int]] = None) -> List[List[int]]:
    """Fonction wrapper pour l'application"""
    return pattern_ondulation.appliquer(input_grid, output_attendu)

# Test rapide
if __name__ == "__main__":
    print("🌊 Pattern Ondulation Diagonale - Prêt!")
    print(f"Nom: {pattern_ondulation.nom}")
    print(f"Description: {pattern_ondulation.description}")
    print(f"Priorité: {pattern_ondulation.priorite}")
