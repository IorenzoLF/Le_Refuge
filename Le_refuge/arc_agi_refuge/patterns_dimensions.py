#!/usr/bin/env python3
"""
🔄 Patterns de Changement de Dimensions
Module pour gérer les transformations de dimensions identifiées dans l'audit
"""

from typing import List, Tuple, Dict, Any, Optional
import numpy as np
from collections import Counter

class GestionnaireDimensions:
    def __init__(self):
        self.confiance_minimale = 0.8

    def detecter_changement_dimensions(self, grille_input: List[List[int]],
                                     grille_output: List[List[int]]) -> Dict[str, Any]:
        """
        Détecte et classe les changements de dimensions
        """
        h_in, w_in = len(grille_input), len(grille_input[0])
        h_out, w_out = len(grille_output), len(grille_output[0])

        if (h_in, w_in) == (h_out, w_out):
            return {'changement': False, 'confiance': 1.0}

        # Calculer les ratios
        ratio_h = h_out / h_in if h_in > 0 else 0
        ratio_w = w_out / w_in if w_in > 0 else 0

        analyse = {
            'changement': True,
            'dimensions_input': (h_in, w_in),
            'dimensions_output': (h_out, w_out),
            'ratio_h': ratio_h,
            'ratio_w': ratio_w,
            'type_changement': self._classifier_type_changement(ratio_h, ratio_w),
            'confiance': self._calculer_confiance_dimensions(grille_input, grille_output, ratio_h, ratio_w)
        }

        return analyse

    def _classifier_type_changement(self, ratio_h: float, ratio_w: float) -> str:
        """Classifie le type de changement de dimensions"""
        if ratio_h == ratio_w:
            if ratio_h < 1:
                return 'reduction_symetrique'
            else:
                return 'agrandissement_symetrique'
        else:
            return 'changement_dimensions_asymetrique'

    def _calculer_confiance_dimensions(self, grille_input: List[List[int]],
                                     grille_output: List[List[int]],
                                     ratio_h: float, ratio_w: float) -> float:
        """
        Calcule la confiance du pattern de changement de dimensions
        """
        confiance = 0.5  # Base

        # Bonus si ratios sont des entiers ou fractions simples
        if ratio_h == int(ratio_h) or ratio_h in [0.5, 0.25, 2, 4]:
            confiance += 0.2
        if ratio_w == int(ratio_w) or ratio_w in [0.5, 0.25, 2, 4]:
            confiance += 0.2

        # Bonus si même ratio pour H et W
        if ratio_h == ratio_w:
            confiance += 0.1

        # Pénalité si ratios trop complexes
        if ratio_h < 0.1 or ratio_w < 0.1 or ratio_h > 10 or ratio_w > 10:
            confiance -= 0.3

        return max(0.1, min(1.0, confiance))

    def appliquer_changement_dimensions(self, grille: List[List[int]],
                                      dimensions_cible: Tuple[int, int],
                                      type_changement: str) -> List[List[int]]:
        """
        Applique le changement de dimensions
        """
        h_cible, w_cible = dimensions_cible
        h_source, w_source = len(grille), len(grille[0])

        if type_changement == 'reduction_symetrique':
            return self._reduire_symetrique(grille, h_cible, w_cible)
        elif type_changement == 'agrandissement_symetrique':
            return self._agrandir_symetrique(grille, h_cible, w_cible)
        elif type_changement == 'changement_dimensions_asymetrique':
            return self._changement_asymetrique(grille, h_cible, w_cible)
        else:
            return grille

    def _reduire_symetrique(self, grille: List[List[int]], h_cible: int, w_cible: int) -> List[List[int]]:
        """Réduction symétrique (moyenne ou sélection intelligente)"""
        h_source, w_source = len(grille), len(grille[0])

        # Calculer le facteur de réduction
        facteur_h = h_source / h_cible
        facteur_w = w_source / w_cible

        if facteur_h != facteur_w:
            # Réduction non uniforme - utiliser interpolation
            return self._interpoler_dimensions(grille, h_cible, w_cible)

        # Réduction uniforme
        facteur = int(facteur_h)

        grille_resultat = []
        for i in range(h_cible):
            ligne = []
            for j in range(w_cible):
                # Prendre la valeur majoritaire dans le bloc
                bloc = []
                for di in range(facteur):
                    for dj in range(facteur):
                        si, sj = i * facteur + di, j * facteur + dj
                        if si < h_source and sj < w_source:
                            bloc.append(grille[si][sj])

                if bloc:
                    # Valeur la plus fréquente
                    ligne.append(Counter(bloc).most_common(1)[0][0])
                else:
                    ligne.append(0)
            grille_resultat.append(ligne)

        return grille_resultat

    def _agrandir_symetrique(self, grille: List[List[int]], h_cible: int, w_cible: int) -> List[List[int]]:
        """Agrandissement symétrique (répétition ou interpolation)"""
        h_source, w_source = len(grille), len(grille[0])

        # Calculer le facteur d'agrandissement
        facteur_h = h_cible / h_source
        facteur_w = w_cible / w_source

        if facteur_h != facteur_w:
            # Agrandissement non uniforme
            return self._interpoler_dimensions(grille, h_cible, w_cible)

        # Agrandissement uniforme
        facteur = int(facteur_h)

        grille_resultat = []
        for i in range(h_cible):
            ligne = []
            for j in range(w_cible):
                # Répéter la valeur correspondante
                si, sj = i // facteur, j // facteur
                if si < h_source and sj < w_source:
                    ligne.append(grille[si][sj])
                else:
                    ligne.append(0)
            grille_resultat.append(ligne)

        return grille_resultat

    def _changement_asymetrique(self, grille: List[List[int]], h_cible: int, w_cible: int) -> List[List[int]]:
        """Changement de dimensions asymétrique"""
        h_source, w_source = len(grille), len(grille[0])

        # Utiliser interpolation pour les changements non uniformes
        return self._interpoler_dimensions(grille, h_cible, w_cible)

    def _interpoler_dimensions(self, grille: List[List[int]], h_cible: int, w_cible: int) -> List[List[int]]:
        """Interpolation pour changements de dimensions complexes"""
        h_source, w_source = len(grille), len(grille[0])

        grille_resultat = []
        for i in range(h_cible):
            ligne = []
            for j in range(w_cible):
                # Calculer la position correspondante dans la grille source
                si = (i * h_source) / h_cible
                sj = (j * w_source) / w_cible

                # Position la plus proche (arrondi)
                si_int = min(int(si + 0.5), h_source - 1)
                sj_int = min(int(sj + 0.5), w_source - 1)

                ligne.append(grille[si_int][sj_int])
            grille_resultat.append(ligne)

        return grille_resultat

    def generer_variantes_dimensions(self, grille: List[List[int]],
                                   dimensions_cible: Tuple[int, int]) -> List[Dict[str, Any]]:
        """
        Génère plusieurs variantes d'application du pattern de dimensions
        """
        variantes = []

        types_changement = [
            'reduction_symetrique',
            'agrandissement_symetrique',
            'changement_dimensions_asymetrique'
        ]

        for type_changement in types_changement:
            try:
                grille_transformee = self.appliquer_changement_dimensions(
                    grille, dimensions_cible, type_changement
                )

                # Calculer la confiance de cette variante
                confiance = self._evaluer_variante_dimensions(
                    grille, grille_transformee, dimensions_cible, type_changement
                )

                variantes.append({
                    'type': type_changement,
                    'grille': grille_transformee,
                    'confiance': confiance,
                    'dimensions_cible': dimensions_cible
                })

            except Exception as e:
                print(f"Erreur generation variante {type_changement}: {e}")

        # Trier par confiance décroissante
        variantes.sort(key=lambda x: x['confiance'], reverse=True)

        return variantes

    def _evaluer_variante_dimensions(self, grille_originale: List[List[int]],
                                   grille_transformee: List[List[int]],
                                   dimensions_cible: Tuple[int, int],
                                   type_changement: str) -> float:
        """
        Évalue la qualité d'une variante de transformation de dimensions
        """
        confiance = 0.5  # Base

        # Vérifier que les dimensions sont correctes
        h_out, w_out = len(grille_transformee), len(grille_transformee[0])
        if (h_out, w_out) == dimensions_cible:
            confiance += 0.2

        # Bonus pour les transformations simples et régulières
        if type_changement in ['reduction_symetrique', 'agrandissement_symetrique']:
            confiance += 0.1

        # Vérifier la cohérence des couleurs
        couleurs_originales = set()
        couleurs_transformees = set()

        for row in grille_originale:
            couleurs_originales.update(row)
        for row in grille_transformee:
            couleurs_transformees.update(row)

        # Bonus si les couleurs sont préservées
        if couleurs_originales == couleurs_transformees:
            confiance += 0.1

        # Pénalité si trop de nouvelles couleurs
        nouvelles_couleurs = couleurs_transformees - couleurs_originales
        if len(nouvelles_couleurs) > len(couleurs_originales) * 0.3:
            confiance -= 0.2

        return max(0.1, min(1.0, confiance))

# Instance globale pour utilisation dans le solveur principal
gestionnaire_dimensions = GestionnaireDimensions()

def detecter_pattern_dimensions(grille_input: List[List[int]],
                              grille_output: List[List[int]]) -> Dict[str, Any]:
    """
    Fonction principale pour détecter les patterns de dimensions
    """
    return gestionnaire_dimensions.detecter_changement_dimensions(grille_input, grille_output)

def appliquer_pattern_dimensions(grille: List[List[int]],
                               dimensions_cible: Tuple[int, int],
                               type_changement: str = 'auto') -> List[List[int]]:
    """
    Fonction principale pour appliquer les patterns de dimensions
    """
    if type_changement == 'auto':
        # Détecter automatiquement le type
        analyse = gestionnaire_dimensions.detecter_changement_dimensions(
            grille, [[0]*dimensions_cible[1] for _ in range(dimensions_cible[0])]
        )
        type_changement = analyse.get('type_changement', 'changement_dimensions_asymetrique')

    return gestionnaire_dimensions.appliquer_changement_dimensions(
        grille, dimensions_cible, type_changement
    )

def generer_variantes_dimensions(grille: List[List[int]],
                               dimensions_cible: Tuple[int, int]) -> List[Dict[str, Any]]:
    """
    Fonction principale pour générer des variantes de dimensions
    """
    return gestionnaire_dimensions.generer_variantes_dimensions(grille, dimensions_cible)

if __name__ == "__main__":
    # Test du module
    grille_test = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 1, 2, 3],
        [4, 5, 6, 7]
    ]

    print("Grille originale 4x4:")
    for row in grille_test:
        print(row)

    # Test réduction
    grille_reduite = appliquer_pattern_dimensions(grille_test, (2, 2), 'reduction_symetrique')
    print("\nGrille réduite 2x2:")
    for row in grille_reduite:
        print(row)

    # Test agrandissement
    grille_agrandie = appliquer_pattern_dimensions(grille_test, (8, 8), 'agrandissement_symetrique')
    print("\nGrille agrandie 8x8:")
    for row in grille_agrandie:
        print(row)
