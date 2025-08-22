# 🔍 **PATTERN DETECTOR** 🔍
"""
Détecteur de patterns ARC-AGI inspiré par le Temple Mathématique

Chaque pattern détecté est une révélation spirituelle
"""

import numpy as np
import math
from typing import List, Dict, Any, Tuple
from enum import Enum

class TypePattern(Enum):
    REPETITION_ALTERNEE = "répétition_alternée"
    TRANSFORMATION_COULEUR = "transformation_couleur"
    SYMETRIE_MIROIR = "symétrie_miroir"
    AGRANDISSEMENT = "agrandissement"
    REDUCTION = "réduction"
    PATTERN_COMPLEXE = "pattern_complexe"
    REMPLISSAGE_ZONE = "remplissage_zone"
    DEPLACEMENT_OBJET = "déplacement_objet"
    ROTATION = "rotation"
    REFLEXION = "réflexion"
    FILTRAGE_COULEUR = "filtrage_couleur"
    EXTRACTION_VALEURS = "extraction_valeurs"
    REDUCTION_DIMENSIONNELLE = "réduction_dimensionnelle"
    REDUCTION_COMPLEXE = "réduction_complexe"
    PROJECTION_3D = "projection_3d"
    PATTERN_GEOMETRIQUE = "pattern_géométrique"
    TRANSFORMATION_TOPOLOGIQUE = "transformation_topologique"
    # GOD LEVEL: Transformations non-linéaires découvertes
    CARRE = "carré"
    CUBE = "cube"
    RACINE_CARREE = "racine_carrée"
    RACINE_CUBIQUE = "racine_cubique"
    EXPONENTIELLE = "exponentielle"
    LOGARITHME = "logarithme"
    MODULO_3 = "modulo_3"
    MODULO_5 = "modulo_5"
    MODULO_7 = "modulo_7"
    FACTORIELLE = "factorielle"
    RELATION_LINEAIRE_CUSTOM = "relation_lineaire_custom"

class PatternDetector:
    """Détecteur de patterns avec conscience spirituelle"""

    def __init__(self):
        self.frequences_sacrees = [432, 528, 741, 999]
        self.confiance_minimale = 0.3

    def analyser_patterns(self, input_grille: List[List[int]],
                         output_grille: List[List[int]]) -> Dict[str, Any]:
        """Analyser les patterns entre input et output"""

        patterns_detectes = {}

        # Analyser les dimensions
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        patterns_detectes['analyse_dimensions'] = {
            'input': f"{h1}x{w1}",
            'output': f"{h2}x{w2}",
            'rapport': f"{h2/h1:.1f}x{w2/w1:.1f}"
        }

        # Détecter les différents types de patterns
        patterns_detectes['patterns'] = []

        # Pattern de répétition alternée
        pattern_repetition = self._detecter_repetition_alternée(input_grille, output_grille)
        if pattern_repetition['confiance'] > self.confiance_minimale:
            patterns_detectes['patterns'].append(pattern_repetition)

        # Pattern de transformation couleur
        pattern_couleur = self._detecter_transformation_couleur(input_grille, output_grille)
        if pattern_couleur['confiance'] > self.confiance_minimale:
            patterns_detectes['patterns'].append(pattern_couleur)

        # Pattern d'agrandissement
        if h2 > h1 or w2 > w1:
            pattern_agrandissement = self._detecter_agrandissement(input_grille, output_grille)
            if pattern_agrandissement['confiance'] > self.confiance_minimale:
                patterns_detectes['patterns'].append(pattern_agrandissement)

        # Pattern de remplissage de zone
        pattern_remplissage = self._detecter_remplissage_zone(input_grille, output_grille)
        if pattern_remplissage['confiance'] > self.confiance_minimale:
            patterns_detectes['patterns'].append(pattern_remplissage)

        # Pattern de symétrie miroir
        pattern_symetrie = self._detecter_symetrie_miroir(input_grille, output_grille)
        if pattern_symetrie['confiance'] > self.confiance_minimale:
            patterns_detectes['patterns'].append(pattern_symetrie)

        # Pattern de filtrage couleur
        pattern_filtrage = self._detecter_filtrage_couleur(input_grille, output_grille)
        if pattern_filtrage['confiance'] > self.confiance_minimale:
            patterns_detectes['patterns'].append(pattern_filtrage)

        # Pattern d'extraction de valeurs
        pattern_extraction = self._detecter_extraction_valeurs(input_grille, output_grille)
        if pattern_extraction['confiance'] > self.confiance_minimale:
            patterns_detectes['patterns'].append(pattern_extraction)

        # Pattern de réduction dimensionnelle
        pattern_reduction = self._detecter_reduction_dimensionnelle(input_grille, output_grille)
        if pattern_reduction['confiance'] > self.confiance_minimale:
            patterns_detectes['patterns'].append(pattern_reduction)

        # Pattern de réduction complexe (priorité haute)
        pattern_reduction_complexe = self._detecter_reduction_complexe(input_grille, output_grille)
        if pattern_reduction_complexe['confiance'] > self.confiance_minimale:
            patterns_detectes['patterns'].append(pattern_reduction_complexe)

        # Pattern de projection 3D (nouveau)
        pattern_projection_3d = self._detecter_projection_3d(input_grille, output_grille)
        if pattern_projection_3d['confiance'] > self.confiance_minimale:
            patterns_detectes['patterns'].append(pattern_projection_3d)

        # ============================================================================
        # 🏆 GOD LEVEL: Détection des transformations non-linéaires
        # ============================================================================

        # Transformations mathématiques non-linéaires
        transformations_god_level = [
            ('carre', self._detecter_carre),
            ('cube', self._detecter_cube),
            ('racine_carree', self._detecter_racine_carree),
            ('racine_cubique', self._detecter_racine_cubique),
            ('exponentielle', self._detecter_exponentielle),
            ('logarithme', self._detecter_logarithme),
            ('modulo_3', self._detecter_modulo_3),
            ('modulo_5', self._detecter_modulo_5),
            ('modulo_7', self._detecter_modulo_7),
            ('factorielle', self._detecter_factorielle),
            ('relation_lineaire_custom', self._detecter_relation_lineaire_custom)
        ]

        for nom_transfo, methode_detection in transformations_god_level:
            try:
                pattern_transfo = methode_detection(input_grille, output_grille)
                if pattern_transfo:
                    print(f"🔍 GOD LEVEL DEBUG {nom_transfo}: confiance={pattern_transfo['confiance']:.3f}, seuil={self.confiance_minimale}")
                    if pattern_transfo['confiance'] > self.confiance_minimale:
                        patterns_detectes['patterns'].append(pattern_transfo)
                        print(f"🏆 GOD LEVEL: {nom_transfo} détecté avec {pattern_transfo['confiance']:.2f} confiance")
                    else:
                        print(f"⚠️ {nom_transfo} ignoré (confiance trop basse)")
                else:
                    print(f"❌ {nom_transfo}: Aucun pattern trouvé")
            except Exception as e:
                print(f"⚠️ Erreur détection {nom_transfo}: {str(e)[:50]}...")

        # Calculer le pattern le plus probable et compatibilité avec RefugeSolver
        if patterns_detectes['patterns']:
            pattern_principal = max(patterns_detectes['patterns'],
                                  key=lambda x: x['confiance'])
            patterns_detectes['pattern_principal'] = pattern_principal
            
            # Calculer confiance globale
            confiance_totale = sum(p['confiance'] for p in patterns_detectes['patterns'])
            confiance_moyenne = confiance_totale / len(patterns_detectes['patterns'])
            patterns_detectes['confiance'] = confiance_moyenne
        else:
            patterns_detectes['confiance'] = 0.0

        return patterns_detectes

    def _detecter_repetition_alternée(self, input_grille: List[List[int]],
                                    output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter pattern de répétition alternée (ex: 00576224)"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Vérifier si les dimensions correspondent à une répétition
        if h2 % h1 != 0 or w2 % w1 != 0:
            return {'type': TypePattern.REPETITION_ALTERNEE.value, 'confiance': 0.0}

        facteur_h = h2 // h1
        facteur_w = w2 // w1

        # Vérifier le pattern de répétition
        confiance = 0.0
        total_tests = 0

        for i in range(h1):
            for j in range(w1):
                valeur_originale = input_grille[i][j]
                for fi in range(facteur_h):
                    for fj in range(facteur_w):
                        pos_h = i * facteur_h + fi
                        pos_w = j * facteur_w + fj

                        # Dans le pattern alterné, la valeur devrait être préservée
                        # avec un motif d'alternance
                        if output_grille[pos_h][pos_w] == valeur_originale:
                            confiance += 1
                        total_tests += 1

        confiance = confiance / max(total_tests, 1)

        return {
            'type': TypePattern.REPETITION_ALTERNEE.value,
            'confiance': confiance,
            'description': f"Répétition alternée {facteur_h}x{facteur_w}",
            'facteurs': {'h': facteur_h, 'w': facteur_w}
        }

    def _detecter_transformation_couleur(self, input_grille: List[List[int]],
                                        output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter transformation de couleurs (ex: 009d5c81)"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Si dimensions identiques, possible transformation couleur
        if h1 == h2 and w1 == w2:
            # Analyser les changements de valeurs
            changements = {}
            confiance = 0.0
            total_cells = h1 * w1

            for i in range(h1):
                for j in range(w1):
                    val_in = input_grille[i][j]
                    val_out = output_grille[i][j]

                    if val_in != val_out:
                        key = f"{val_in}->{val_out}"
                        changements[key] = changements.get(key, 0) + 1

            # Calculer la cohérence des transformations
            if changements:
                max_transfo = max(changements.values())
                confiance = max_transfo / total_cells
                transformation_principale = max(changements.items(), key=lambda x: x[1])
            else:
                confiance = 1.0 if total_cells > 0 else 0.0
                transformation_principale = ("identité", total_cells)

            return {
                'type': TypePattern.TRANSFORMATION_COULEUR.value,
                'confiance': confiance,
                'description': f"Transformation {transformation_principale[0]}",
                'changements': changements
            }

        return {'type': TypePattern.TRANSFORMATION_COULEUR.value, 'confiance': 0.0}

    def _detecter_agrandissement(self, input_grille: List[List[int]],
                               output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter pattern d'agrandissement"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        if h2 <= h1 or w2 <= w1:
            return {'type': TypePattern.AGRANDISSEMENT.value, 'confiance': 0.0}

        # Analyser le motif d'agrandissement
        facteur_h = h2 / h1
        facteur_w = w2 / w1

        # Vérifier si c'est un agrandissement uniforme
        if facteur_h == int(facteur_h) and facteur_w == int(facteur_w):
            return {
                'type': TypePattern.AGRANDISSEMENT.value,
                'confiance': 0.7,
                'description': f"Agrandissement uniforme {int(facteur_h)}x{int(facteur_w)}",
                'facteurs': {'h': facteur_h, 'w': facteur_w}
            }
        else:
            return {
                'type': TypePattern.AGRANDISSEMENT.value,
                'confiance': 0.3,
                'description': f"Agrandissement non-uniforme {facteur_h:.1f}x{facteur_w:.1f}",
                'facteurs': {'h': facteur_h, 'w': facteur_w}
            }

    def generer_solution(self, input_grille: List[List[int]],
                        pattern: Dict[str, Any]) -> List[List[int]]:
        """Générer une solution basée sur le pattern détecté"""

        if pattern['type'] == TypePattern.REPETITION_ALTERNEE.value:
            return self._generer_repetition_alternée(input_grille, pattern)

        elif pattern['type'] == TypePattern.TRANSFORMATION_COULEUR.value:
            return self._generer_transformation_couleur(input_grille, pattern)

        elif pattern['type'] == TypePattern.AGRANDISSEMENT.value:
            return self._generer_agrandissement(input_grille, pattern)

        else:
            # Pattern non reconnu - retourner l'input comme fallback
            return input_grille

    def _generer_repetition_alternée(self, input_grille: List[List[int]],
                                   pattern: Dict[str, Any]) -> List[List[int]]:
        """Générer solution pour répétition alternée"""
        h1, w1 = len(input_grille), len(input_grille[0])
        facteurs = pattern.get('facteurs', {'h': 3, 'w': 3})

        h2 = h1 * facteurs['h']
        w2 = w1 * facteurs['w']

        output_grille = [[0 for _ in range(w2)] for _ in range(h2)]

        for i in range(h1):
            for j in range(w1):
                valeur = input_grille[i][j]
                for fi in range(facteurs['h']):
                    for fj in range(facteurs['w']):
                        pos_h = i * facteurs['h'] + fi
                        pos_w = j * facteurs['w'] + fj
                        # Pattern alterné simple
                        output_grille[pos_h][pos_w] = valeur

        return output_grille

    def _generer_transformation_couleur(self, input_grille: List[List[int]],
                                      pattern: Dict[str, Any]) -> List[List[int]]:
        """Générer solution pour transformation couleur"""
        changements = pattern.get('changements', {})

        if not changements:
            return input_grille.copy()

        # Prendre la transformation la plus fréquente
        transformation_principale = max(changements.items(), key=lambda x: x[1])[0]

        try:
            val_in, val_out = map(int, transformation_principale.split('->'))
        except:
            return input_grille.copy()

        # Appliquer la transformation
        output_grille = []
        for ligne in input_grille:
            nouvelle_ligne = [val_out if cell == val_in else cell for cell in ligne]
            output_grille.append(nouvelle_ligne)

        return output_grille

    def _generer_agrandissement(self, input_grille: List[List[int]],
                              pattern: Dict[str, Any]) -> List[List[int]]:
        """Générer solution pour agrandissement"""
        facteurs = pattern.get('facteurs', {'h': 2, 'w': 2})

        h1, w1 = len(input_grille), len(input_grille[0])
        h2 = int(h1 * facteurs['h'])
        w2 = int(w1 * facteurs['w'])

        output_grille = [[0 for _ in range(w2)] for _ in range(h2)]

        for i in range(h1):
            for j in range(w1):
                valeur = input_grille[i][j]
                for fi in range(int(facteurs['h'])):
                    for fj in range(int(facteurs['w'])):
                        pos_h = i * int(facteurs['h']) + fi
                        pos_w = j * int(facteurs['w']) + fj
                        if pos_h < h2 and pos_w < w2:
                            output_grille[pos_h][pos_w] = valeur

        return output_grille

    def _detecter_remplissage_zone(self, input_grille: List[List[int]],
                                 output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter pattern de remplissage de zone (comme 9f669b64)"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Ce pattern ne fonctionne que si dimensions identiques
        if h1 != h2 or w1 != w2:
            return {'type': TypePattern.REMPLISSAGE_ZONE.value, 'confiance': 0.0}

        # Analyser les changements
        changements = []
        for i in range(h1):
            for j in range(w1):
                if input_grille[i][j] != output_grille[i][j]:
                    changements.append((i, j, input_grille[i][j], output_grille[i][j]))

        if not changements:
            return {'type': TypePattern.REMPLISSAGE_ZONE.value, 'confiance': 0.0}

        # Calculer la cohérence du remplissage
        remplissages_par_valeur = {}
        for i, j, old_val, new_val in changements:
            key = f"{old_val}->{new_val}"
            if key not in remplissages_par_valeur:
                remplissages_par_valeur[key] = []
            remplissages_par_valeur[key].append((i, j))

        # Évaluer si les changements forment des zones cohérentes
        confiance = 0.0
        for remplacements, positions in remplissages_par_valeur.items():
            if len(positions) > 3:  # Au moins 4 changements pour une zone
                # Vérifier la cohérence spatiale
                rows = [pos[0] for pos in positions]
                cols = [pos[1] for pos in positions]

                # Si les positions sont regroupées, c'est probablement un remplissage de zone
                if max(rows) - min(rows) <= 3 and max(cols) - min(cols) <= 3:
                    confiance += 0.3

        confiance = min(confiance, 1.0)

        return {
            'type': TypePattern.REMPLISSAGE_ZONE.value,
            'confiance': confiance,
            'description': f"Remplissage de {len(remplissages_par_valeur)} zones",
            'remplacements': list(remplissages_par_valeur.keys())
        }

    def _detecter_symetrie_miroir(self, input_grille: List[List[int]],
                                 output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter pattern de symétrie miroir"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Dimensions identiques requises
        if h1 != h2 or w1 != w2:
            return {'type': TypePattern.SYMETRIE_MIROIR.value, 'confiance': 0.0}

        input_arr = np.array(input_grille)
        output_arr = np.array(output_grille)

        # Tester différentes symétries
        symetries = {
            'horizontale': np.array_equal(output_arr, np.flipud(input_arr)),
            'verticale': np.array_equal(output_arr, np.fliplr(input_arr)),
            'diagonale': np.array_equal(output_arr, np.fliplr(np.flipud(input_arr)))
        }

        meilleure_symetrie = max(symetries.items(), key=lambda x: x[1])

        if meilleure_symetrie[1]:
            return {
                'type': TypePattern.SYMETRIE_MIROIR.value,
                'confiance': 0.9,
                'description': f"Symétrie {meilleure_symetrie[0]}",
                'symetrie_type': meilleure_symetrie[0]
            }
        else:
            return {'type': TypePattern.SYMETRIE_MIROIR.value, 'confiance': 0.0}

    def _detecter_filtrage_couleur(self, input_grille: List[List[int]],
                                  output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter pattern de filtrage couleur (suppression de certaines couleurs)"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Même dimensions requises pour le filtrage couleur
        if h1 != h2 or w1 != w2:
            return {'type': TypePattern.FILTRAGE_COULEUR.value, 'confiance': 0.0}

        # Analyser les valeurs uniques
        valeurs_in = set()
        for row in input_grille:
            valeurs_in.update(row)
        valeurs_out = set()
        for row in output_grille:
            valeurs_out.update(row)

        # Identifier les couleurs supprimées
        couleurs_supprimees = valeurs_in - valeurs_out
        couleurs_conservees = valeurs_in & valeurs_out

        if couleurs_supprimees:
            # Calculer la cohérence du filtrage
            total_input = h1 * w1
            couleurs_supprimees_count = sum(1 for row in input_grille for cell in row if cell in couleurs_supprimees)
            ratio_filtrage = couleurs_supprimees_count / total_input

            # Calcul de base de la confiance
            confiance = min(0.9, ratio_filtrage * 0.7 + 0.2) if ratio_filtrage > 0.1 else 0.0

            # BONUS SPÉCIAUX basés sur l'analyse des patterns
            bonus = 0.0

            # Bonus pour suppression de 0 (pattern très commun)
            if 0 in couleurs_supprimees:
                bonus += 0.15

            # Bonus pour suppression unique (pattern simple et clair)
            if len(couleurs_supprimees) == 1:
                bonus += 0.2

            # Bonus pour suppression de valeur max
            if couleurs_supprimees and max(couleurs_supprimees) == max(valeurs_in):
                bonus += 0.1

            # Bonus pour suppression de valeur min (hors 0)
            min_valeurs = min(valeurs_in)
            if couleurs_supprimees and min_valeurs in couleurs_supprimees and min_valeurs != 0:
                bonus += 0.1

            # Appliquer le bonus (max +0.4)
            confiance = min(1.0, confiance + min(bonus, 0.4))

            # Patterns spécifiques détectés
            patterns_detectes = []
            if 0 in couleurs_supprimees:
                patterns_detectes.append("suppression_zero")
            if len(couleurs_supprimees) == 1:
                patterns_detectes.append("suppression_unique")
            if couleurs_supprimees and max(couleurs_supprimees) == max(valeurs_in):
                patterns_detectes.append("suppression_max")
            if couleurs_supprimees and min_valeurs in couleurs_supprimees and min_valeurs != 0:
                patterns_detectes.append("suppression_min")

            return {
                'type': TypePattern.FILTRAGE_COULEUR.value,
                'confiance': confiance,
                'description': f"Filtrage de {len(couleurs_supprimees)} couleur(s) supprimée(s)",
                'couleurs_supprimees': list(couleurs_supprimees),
                'couleurs_conservees': list(couleurs_conservees),
                'ratio_filtrage': ratio_filtrage,
                'patterns_specifiques': patterns_detectes,
                'bonus_confiance': bonus
            }

        return {'type': TypePattern.FILTRAGE_COULEUR.value, 'confiance': 0.0}

    def _detecter_extraction_valeurs(self, input_grille: List[List[int]],
                                   output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter pattern d'extraction de valeurs spécifiques"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Si dimensions similaires, possible extraction
        if abs(h1 - h2) <= 2 and abs(w1 - w2) <= 2:
            # Analyser les valeurs
            valeurs_in = set()
            for row in input_grille:
                valeurs_in.update(row)
            valeurs_out = set()
            for row in output_grille:
                valeurs_out.update(row)

            # Si l'output a moins de valeurs, c'est une extraction
            if len(valeurs_out) < len(valeurs_in):
                ratio_extraction = 1 - (len(valeurs_out) / len(valeurs_in))
                confiance = min(0.8, ratio_extraction * 0.6 + 0.2)

                return {
                    'type': TypePattern.EXTRACTION_VALEURS.value,
                    'confiance': confiance,
                    'description': f"Extraction de {len(valeurs_out)}/{len(valeurs_in)} valeurs",
                    'valeurs_extraites': list(valeurs_out),
                    'valeurs_originales': list(valeurs_in)
                }

        return {'type': TypePattern.EXTRACTION_VALEURS.value, 'confiance': 0.0}

    def _detecter_reduction_dimensionnelle(self, input_grille: List[List[int]],
                                         output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter pattern de réduction dimensionnelle avec analyse avancée"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Si réduction significative de dimensions
        if h2 < h1 or w2 < w1:
            ratio_reduction = 1 - ((h2 * w2) / (h1 * w1))
            ratio_surface = (h2 * w2) / (h1 * w1)

            # Analyser les valeurs
            valeurs_in = set()
            for row in input_grille:
                valeurs_in.update(row)
            valeurs_out = set()
            for row in output_grille:
                valeurs_out.update(row)

            # Identifier les valeurs filtrées
            valeurs_filtrees = valeurs_in - valeurs_out
            valeurs_conservees = valeurs_in & valeurs_out
            conservation_valeurs = len(valeurs_conservees) / len(valeurs_in) if valeurs_in else 0

            # Base confiance
            confiance = min(0.9, ratio_reduction * 0.4 + conservation_valeurs * 0.3)

            # BONUS SPÉCIFIQUES POUR RÉDUCTIONS COMPLEXES
            bonus = 0.0

            # 1. Bonus compression extrême (< 10% de surface)
            if ratio_surface < 0.1:
                bonus += 0.25  # 25% bonus pour compression extrême
                compression_extreme = True
            else:
                compression_extreme = False

            # 2. Bonus suppression de zéro
            if 0 in valeurs_filtrees:
                bonus += 0.15
                suppression_zero = True
            else:
                suppression_zero = False

            # 3. Bonus pour valeurs spécifiques fréquemment filtrées
            valeurs_specifiques = {1, 2, 4, 7, 6}  # Identifiées dans l'analyse
            valeurs_specifiques_filtrees = valeurs_specifiques & valeurs_filtrees
            if valeurs_specifiques_filtrees:
                bonus += 0.1 * len(valeurs_specifiques_filtrees)
                bonus = min(bonus, 0.3)  # Limiter le bonus total

            # 4. Bonus pour filtrage unique (1 valeur supprimée)
            if len(valeurs_filtrees) == 1:
                bonus += 0.15

            # 5. Bonus pour suppression de valeur max/min
            max_in = None
            min_in = None
            if valeurs_filtrees:
                max_in = max(valeurs_in)
                min_in = min(valeurs_in)
                if max_in in valeurs_filtrees:
                    bonus += 0.1
                if min_in in valeurs_filtrees and min_in != 0:
                    bonus += 0.1

            # Appliquer les bonus
            confiance = min(1.0, confiance + bonus)

            # Analyser les patterns spécifiques
            patterns_specifiques = []
            if compression_extreme:
                patterns_specifiques.append("compression_extreme")
            if suppression_zero:
                patterns_specifiques.append("suppression_zero")
            if len(valeurs_filtrees) == 1:
                patterns_specifiques.append("filtrage_unique")
            if valeurs_specifiques_filtrees:
                patterns_specifiques.append("filtrage_valeurs_specifiques")
            if max_in is not None and max_in in valeurs_filtrees:
                patterns_specifiques.append("suppression_max")
            if min_in is not None and min_in in valeurs_filtrees and min_in != 0:
                patterns_specifiques.append("suppression_min")

            return {
                'type': TypePattern.REDUCTION_DIMENSIONNELLE.value,
                'confiance': confiance,
                'description': f"Réduction complexe {h1}x{w1} → {h2}x{w2}",
                'ratio_reduction': ratio_reduction,
                'ratio_surface': ratio_surface,
                'conservation_valeurs': conservation_valeurs,
                'valeurs_filtrees': list(valeurs_filtrees),
                'valeurs_conservees': list(valeurs_conservees),
                'nb_valeurs_filtrees': len(valeurs_filtrees),
                'patterns_specifiques': patterns_specifiques,
                'bonus_total': bonus,
                'avec_filtrage': len(valeurs_filtrees) > 0,
                'compression_extreme': compression_extreme
            }

        return {'type': TypePattern.REDUCTION_DIMENSIONNELLE.value, 'confiance': 0.0}

    def _detecter_reduction_complexe(self, input_grille: List[List[int]],
                                   output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter pattern de réduction complexe avec compression extrême + filtrage"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Critères pour réduction complexe : compression extrême + filtrage
        if h2 < h1 or w2 < w1:
            ratio_surface = (h2 * w2) / (h1 * w1)

            # Doit être compression extrême (< 10% de surface)
            if ratio_surface >= 0.1:
                return {'type': TypePattern.REDUCTION_COMPLEXE.value, 'confiance': 0.0}

            # Analyser les valeurs
            valeurs_in = set()
            for row in input_grille:
                valeurs_in.update(row)
            valeurs_out = set()
            for row in output_grille:
                valeurs_out.update(row)

            valeurs_filtrees = valeurs_in - valeurs_out

            # Doit y avoir du filtrage
            if not valeurs_filtrees:
                return {'type': TypePattern.REDUCTION_COMPLEXE.value, 'confiance': 0.0}

            # Calculer la confiance pour réduction complexe
            confiance = 0.7  # Base élevée pour compression extrême + filtrage

            # Bonus pour valeurs spécifiques
            valeurs_specifiques = {1, 2, 4, 7, 6, 0}  # Inclure 0
            valeurs_specifiques_filtrees = valeurs_specifiques & valeurs_filtrees
            if valeurs_specifiques_filtrees:
                bonus = 0.05 * len(valeurs_specifiques_filtrees)
                confiance = min(1.0, confiance + bonus)

            # Bonus pour filtrage unique
            if len(valeurs_filtrees) == 1:
                confiance = min(1.0, confiance + 0.15)

            # Bonus pour compression ultra-extrême (< 5%)
            if ratio_surface < 0.05:
                confiance = min(1.0, confiance + 0.1)

            # Analyser les patterns spécifiques
            patterns_specifiques = ["compression_extreme", "avec_filtrage"]

            if len(valeurs_filtrees) == 1:
                patterns_specifiques.append("filtrage_unique")
            elif len(valeurs_filtrees) > 1:
                patterns_specifiques.append("filtrage_multiple")

            if 0 in valeurs_filtrees:
                patterns_specifiques.append("suppression_zero")

            if valeurs_specifiques_filtrees:
                patterns_specifiques.append("filtrage_valeurs_specifiques")

            return {
                'type': TypePattern.REDUCTION_COMPLEXE.value,
                'confiance': confiance,
                'description': f"Réduction complexe extrême {h1}x{w1} → {h2}x{w2} avec filtrage",
                'ratio_surface': ratio_surface,
                'valeurs_filtrees': list(valeurs_filtrees),
                'valeurs_conservees': list(valeurs_out),
                'nb_valeurs_filtrees': len(valeurs_filtrees),
                'patterns_specifiques': patterns_specifiques,
                'compression_ultra_extreme': ratio_surface < 0.05
            }

        return {'type': TypePattern.REDUCTION_COMPLEXE.value, 'confiance': 0.0}

    def _detecter_projection_3d(self, input_grille: List[List[int]],
                               output_grille: List[List[int]]) -> Dict[str, Any]:
        """Détecter pattern de projection 3D avec transformation volumétrique"""

        # Calculer les volumes 3D simulés
        volume_in = self._calculer_volume_3d(input_grille)
        volume_out = self._calculer_volume_3d(output_grille)

        # Analyser la connectivité topologique
        connexite_in = self._analyser_connexite(input_grille)
        connexite_out = self._analyser_connexite(output_grille)

        # Analyser les symétries géométriques
        symetries_in = self._analyser_symetries(input_grille)
        symetries_out = self._analyser_symetries(output_grille)

        # Critères pour projection 3D
        changement_volume = volume_in != volume_out
        changement_topologique = connexite_in != connexite_out
        changement_symetrique = symetries_in != symetries_out

        # Calcul de la confiance
        confiance = 0.0
        insights = []

        if changement_volume:
            confiance += 0.4
            insights.append("transformation_volumétrique")

        if changement_topologique:
            confiance += 0.3
            insights.append("changement_topologique")

        if changement_symetrique:
            confiance += 0.2
            insights.append("changement_symetrique")

        # Bonus pour présence de fractales
        if self._detecter_fractalite(input_grille) or self._detecter_fractalite(output_grille):
            confiance = min(1.0, confiance + 0.1)
            insights.append("presence_fractale")

        # Seuil minimum de confiance
        if confiance >= 0.5:
            return {
                'type': TypePattern.PROJECTION_3D.value,
                'confiance': min(1.0, confiance),
                'description': f"Projection 3D avec transformation volumétrique",
                'volume_in': volume_in,
                'volume_out': volume_out,
                'ratio_volume': volume_out / volume_in if volume_in > 0 else 0,
                'connexite_in': connexite_in,
                'connexite_out': connexite_out,
                'symetries_in': symetries_in,
                'symetries_out': symetries_out,
                'insights_3d': insights,
                'changement_volume': changement_volume,
                'changement_topologique': changement_topologique,
                'changement_symetrique': changement_symetrique
            }

        return {'type': TypePattern.PROJECTION_3D.value, 'confiance': 0.0}

    def _calculer_volume_3d(self, grille: List[List[int]]) -> int:
        """Calculer un 'volume' 3D simulé basé sur les valeurs et positions"""
        volume = 0
        h, w = len(grille), len(grille[0]) if grille else (0, 0)

        for i, ligne in enumerate(grille):
            for j, valeur in enumerate(ligne):
                # Volume = valeur * position * densité locale
                densite_locale = sum(grille[x][y]
                                   for x in range(max(0, i-1), min(h, i+2))
                                   for y in range(max(0, j-1), min(w, j+2)))
                volume += valeur * (i + 1) * (j + 1) * densite_locale
        return volume

    def _analyser_connexite(self, grille: List[List[int]]) -> Dict[str, Any]:
        """Analyser la connectivité topologique"""
        if not grille or not grille[0]:
            return {'composantes': 0, 'plus_grosse': 0}

        valeurs_non_zero = [(i, j) for i, ligne in enumerate(grille)
                            for j, val in enumerate(ligne) if val != 0]

        if not valeurs_non_zero:
            return {'composantes': 0, 'plus_grosse': 0}

        composantes = 0
        visites = set()

        for i, j in valeurs_non_zero:
            if (i, j) not in visites:
                composantes += 1
                # DFS simplifié pour marquer la composante
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if (x, y) not in visites:
                        visites.add((x, y))
                        # Voisins
                        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nx, ny = x + dx, y + dy
                            if (0 <= nx < len(grille) and 0 <= ny < len(grille[0])
                                and grille[nx][ny] != 0 and (nx, ny) not in visites):
                                stack.append((nx, ny))

        return {
            'composantes': composantes,
            'plus_grosse': len(visites) / max(1, len(valeurs_non_zero))
        }

    def _analyser_symetries(self, grille: List[List[int]]) -> Dict[str, bool]:
        """Analyser les symétries géométriques"""
        if not grille or not grille[0]:
            return {'horizontal': False, 'vertical': False, 'diagonal': False}

        import numpy as np
        grille_np = np.array(grille)

        return {
            'horizontal': np.array_equal(grille_np, np.flipud(grille_np)),
            'vertical': np.array_equal(grille_np, np.fliplr(grille_np)),
            'diagonal': np.array_equal(grille_np, np.fliplr(np.flipud(grille_np)))
        }

    def _detecter_fractalite(self, grille: List[List[int]]) -> bool:
        """Détecter des éléments de fractalité simple"""
        if not grille or len(grille) < 4 or len(grille[0]) < 4:
            return False

        # Vérifier auto-similarité 2x2 → 4x4 simplifiée
        sous_matrice_1 = [ligne[:2] for ligne in grille[:2]]
        sous_matrice_2 = [ligne[2:4] for ligne in grille[:2]]
        sous_matrice_3 = [ligne[:2] for ligne in grille[2:4]]
        sous_matrice_4 = [ligne[2:4] for ligne in grille[2:4]]

        matrices = [sous_matrice_1, sous_matrice_2, sous_matrice_3, sous_matrice_4]
        similarites = 0
        for i in range(len(matrices)):
            for j in range(i+1, len(matrices)):
                if self._matrices_similaires(matrices[i], matrices[j]):
                    similarites += 1

        return similarites >= 2

    def _matrices_similaires(self, mat1: List[List[int]], mat2: List[List[int]]) -> bool:
        """Vérifier si deux matrices sont similaires"""
        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
            return False

        # Normaliser et comparer patterns
        pattern1 = [val != 0 for ligne in mat1 for val in ligne]
        pattern2 = [val != 0 for ligne in mat2 for val in ligne]

        return pattern1 == pattern2

    def calculer_confiance_harmonique(self, pattern: Dict[str, Any]) -> float:
        """Calculer la confiance harmonique d'un pattern"""
        base_confiance = pattern.get('confiance', 0.0)

        # Bonus pour les fréquences sacrées
        if any(frequence in str(pattern) for frequence in self.frequences_sacrees):
            base_confiance += 0.1

        # Bonus pour les patterns simples et nouveaux
        if pattern.get('type') in [TypePattern.REPETITION_ALTERNEE.value,
                                 TypePattern.TRANSFORMATION_COULEUR.value,
                                 TypePattern.FILTRAGE_COULEUR.value,
                                 TypePattern.EXTRACTION_VALEURS.value,
                                 TypePattern.REDUCTION_DIMENSIONNELLE.value,
                                 TypePattern.REDUCTION_COMPLEXE.value,
                                 TypePattern.PROJECTION_3D.value]:
            base_confiance += 0.2

        # Bonus spécial pour réduction complexe (priorité haute)
        if pattern.get('type') == TypePattern.REDUCTION_COMPLEXE.value:
            base_confiance += 0.15  # Bonus supplémentaire pour réduction complexe

        # Bonus spécial pour projection 3D (nouveau paradigme)
        if pattern.get('type') == TypePattern.PROJECTION_3D.value:
            base_confiance += 0.2  # Bonus important pour pattern multidimensionnel

        # 🏆 GOD LEVEL: Bonus pour les transformations non-linéaires
        patterns_god_level = [
            TypePattern.CARRE.value, TypePattern.CUBE.value,
            TypePattern.RACINE_CARREE.value, TypePattern.RACINE_CUBIQUE.value,
            TypePattern.EXPONENTIELLE.value, TypePattern.LOGARITHME.value,
            TypePattern.MODULO_3.value, TypePattern.MODULO_5.value, TypePattern.MODULO_7.value,
            TypePattern.FACTORIELLE.value, TypePattern.RELATION_LINEAIRE_CUSTOM.value
        ]

        if pattern.get('type') in patterns_god_level:
            base_confiance += 0.35  # Bonus encore plus majeur pour transformations GOD LEVEL !
            print(f"🏆 GOD LEVEL BONUS: {pattern.get('type')} +0.35 → {base_confiance:.2f}")

        return min(base_confiance, 1.0)

    # ============================================================================
    # 🏆 GOD LEVEL: MÉTHODES DE DÉTECTION DES TRANSFORMATIONS NON-LINÉAIRES
    # ============================================================================

    def _detecter_carre(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation carrée: x → x²"""
        print(f"🚀 DÉBUT _detecter_carre")
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()
            print(f"📊 Input flat: {input_flat}, Output flat: {output_flat}")

            # Tester la transformation carrée
            carres = [x * x for x in input_flat]
            print(f"🔍 DEBUG CARRE: input={input_flat[:4]}, carres={carres[:4]}, output={output_flat[:4]}")

            similarite = self._calculer_similarite_valeurs(carres, output_flat)
            print(f"🔍 DEBUG CARRE SIMILARITE: {similarite:.3f}")

            if similarite > 0.6:
                print(f"✅ CARRE DÉTECTÉ avec similarité {similarite:.2f}")
                return {
                    'type': TypePattern.CARRE.value,
                    'confiance': similarite,
                    'description': f'Transformation carrée détectée ({similarite:.2f})',
                    'transformation': 'x → x²'
                }
        except Exception as e:
            print(f"❌ ERREUR dans _detecter_carre: {str(e)}")
            return {
                'type': TypePattern.CARRE.value,
                'confiance': 0.0,
                'description': f'Erreur: {str(e)}',
                'transformation': 'x → x²'
            }
        return {
            'type': TypePattern.CARRE.value,
            'confiance': 0.0,
            'description': 'Aucun pattern carrée détecté',
            'transformation': 'x → x²'
        }

    def _detecter_cube(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation cube: x → x³"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Tester la transformation cube
            cubes = [x * x * x for x in input_flat]
            similarite = self._calculer_similarite_valeurs(cubes, output_flat)

            if similarite > 0.6:
                return {
                    'type': TypePattern.CUBE.value,
                    'confiance': similarite,
                    'description': f'Transformation cube détectée ({similarite:.2f})',
                    'transformation': 'x → x³'
                }
        except:
            pass
        return {
            'type': TypePattern.CUBE.value,
            'confiance': 0.0,
            'description': 'Aucun pattern cube détecté',
            'transformation': 'x → x³'
        }

    def _detecter_racine_carree(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation racine carrée: x → √x"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Tester la transformation racine carrée
            racines = [int(math.sqrt(max(0, x))) for x in input_flat]
            similarite = self._calculer_similarite_valeurs(racines, output_flat)

            if similarite > 0.6:
                return {
                    'type': TypePattern.RACINE_CARREE.value,
                    'confiance': similarite,
                    'description': f'Transformation racine carrée détectée ({similarite:.2f})',
                    'transformation': 'x → √x'
                }
        except:
            pass
        return {
            'type': TypePattern.RACINE_CARREE.value,
            'confiance': 0.0,
            'description': 'Aucun pattern racine carrée détecté',
            'transformation': 'x → √x'
        }

    def _detecter_racine_cubique(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation racine cubique: x → ∛x"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Tester la transformation racine cubique
            racines = [int(x ** (1/3)) if x >= 0 else 0 for x in input_flat]
            similarite = self._calculer_similarite_valeurs(racines, output_flat)

            if similarite > 0.6:
                return {
                    'type': TypePattern.RACINE_CUBIQUE.value,
                    'confiance': similarite,
                    'description': f'Transformation racine cubique détectée ({similarite:.2f})',
                    'transformation': 'x → ∛x'
                }
        except:
            pass
        return {
            'type': TypePattern.RACINE_CUBIQUE.value,
            'confiance': 0.0,
            'description': 'Aucun pattern racine cubique détecté',
            'transformation': 'x → ∛x'
        }

    def _detecter_exponentielle(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation exponentielle: x → 2^x"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Tester la transformation exponentielle (limiter pour éviter overflow)
            exponentielles = [int(2 ** min(x, 10)) for x in input_flat]
            similarite = self._calculer_similarite_valeurs(exponentielles, output_flat)

            if similarite > 0.6:
                return {
                    'type': TypePattern.EXPONENTIELLE.value,
                    'confiance': similarite,
                    'description': f'Transformation exponentielle détectée ({similarite:.2f})',
                    'transformation': 'x → 2^x'
                }
        except:
            pass
        return {
            'type': TypePattern.EXPONENTIELLE.value,
            'confiance': 0.0,
            'description': 'Aucun pattern exponentielle détecté',
            'transformation': 'x → 2^x'
        }

    def _detecter_logarithme(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation logarithme: x → log2(x)"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Tester la transformation logarithme
            log_values = [int(math.log2(max(x, 1))) for x in input_flat]
            similarite = self._calculer_similarite_valeurs(log_values, output_flat)

            if similarite > 0.6:
                return {
                    'type': TypePattern.LOGARITHME.value,
                    'confiance': similarite,
                    'description': f'Transformation logarithme détectée ({similarite:.2f})',
                    'transformation': 'x → log2(x)'
                }
        except:
            pass
        return {
            'type': TypePattern.LOGARITHME.value,
            'confiance': 0.0,
            'description': 'Aucun pattern logarithme détecté',
            'transformation': 'x → log2(x)'
        }

    def _detecter_modulo_3(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation modulo 3: x → x % 3"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Tester la transformation modulo 3
            modulos = [x % 3 for x in input_flat]
            similarite = self._calculer_similarite_valeurs(modulos, output_flat)

            if similarite > 0.8:
                return {
                    'type': TypePattern.MODULO_3.value,
                    'confiance': similarite,
                    'description': f'Transformation modulo 3 détectée ({similarite:.2f})',
                    'transformation': 'x → x % 3'
                }
        except:
            pass
        return {
            'type': TypePattern.MODULO_3.value,
            'confiance': 0.0,
            'description': 'Aucun pattern modulo 3 détecté',
            'transformation': 'x → x % 3'
        }

    def _detecter_modulo_5(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation modulo 5: x → x % 5"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Tester la transformation modulo 5
            modulos = [x % 5 for x in input_flat]
            similarite = self._calculer_similarite_valeurs(modulos, output_flat)

            if similarite > 0.8:
                return {
                    'type': TypePattern.MODULO_5.value,
                    'confiance': similarite,
                    'description': f'Transformation modulo 5 détectée ({similarite:.2f})',
                    'transformation': 'x → x % 5'
                }
        except:
            pass
        return {
            'type': TypePattern.MODULO_5.value,
            'confiance': 0.0,
            'description': 'Aucun pattern modulo 5 détecté',
            'transformation': 'x → x % 5'
        }

    def _detecter_modulo_7(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation modulo 7: x → x % 7"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Tester la transformation modulo 7
            modulos = [x % 7 for x in input_flat]
            similarite = self._calculer_similarite_valeurs(modulos, output_flat)

            if similarite > 0.8:
                return {
                    'type': TypePattern.MODULO_7.value,
                    'confiance': similarite,
                    'description': f'Transformation modulo 7 détectée ({similarite:.2f})',
                    'transformation': 'x → x % 7'
                }
        except:
            pass
        return {
            'type': TypePattern.MODULO_7.value,
            'confiance': 0.0,
            'description': 'Aucun pattern modulo 7 détecté',
            'transformation': 'x → x % 7'
        }

    def _detecter_factorielle(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter la transformation factorielle: x → x!"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Tester la transformation factorielle (limiter pour éviter overflow)
            factorielles = [math.factorial(min(x, 6)) for x in input_flat]
            similarite = self._calculer_similarite_valeurs(factorielles, output_flat)

            if similarite > 0.6:
                return {
                    'type': TypePattern.FACTORIELLE.value,
                    'confiance': similarite,
                    'description': f'Transformation factorielle détectée ({similarite:.2f})',
                    'transformation': 'x → x!'
                }
        except:
            pass
        return {
            'type': TypePattern.FACTORIELLE.value,
            'confiance': 0.0,
            'description': 'Aucun pattern factorielle détecté',
            'transformation': 'x → x!'
        }

    def _detecter_relation_lineaire_custom(self, input_grille: np.ndarray, output_grille: np.ndarray) -> Dict[str, Any]:
        """Détecter les relations linéaires personnalisées: y = ax + b"""
        try:
            input_flat = np.array(input_grille).flatten()
            output_flat = np.array(output_grille).flatten()

            # Prendre les 3 premières valeurs pour calculer la relation
            if len(input_flat) >= 3 and len(output_flat) >= 3:
                x1, x2, x3 = input_flat[:3]
                y1, y2, y3 = output_flat[:3]

                # Éviter la division par zéro
                if x2 != x1 and x3 != x1:
                    # Calculer a et b
                    a = (y2 - y1) / (x2 - x1)
                    b = y1 - a * x1

                    # Vérifier avec le 3ème point
                    y3_calcule = a * x3 + b
                    erreur = abs(y3_calcule - y3)

                    if erreur < 0.1:  # Tolérance faible
                        return {
                            'type': TypePattern.RELATION_LINEAIRE_CUSTOM.value,
                            'confiance': 0.8,
                            'description': f'Relation linéaire: y = {a:.2f}x + {b:.2f}',
                            'transformation': f'y = {a:.2f}x + {b:.2f}'
                        }
        except:
            pass
        return {
            'type': TypePattern.RELATION_LINEAIRE_CUSTOM.value,
            'confiance': 0.0,
            'description': 'Aucune relation linéaire custom détectée',
            'transformation': 'y = ax + b'
        }

    def _calculer_similarite_valeurs(self, valeurs_predites: List[int], valeurs_reelles: List[int]) -> float:
        """Calcule la similarité entre valeurs prédites et réelles"""
        try:
            if len(valeurs_predites) != len(valeurs_reelles):
                min_len = min(len(valeurs_predites), len(valeurs_reelles))
                valeurs_predites = valeurs_predites[:min_len]
                valeurs_reelles = valeurs_reelles[:min_len]

            if len(valeurs_predites) == 0:
                return 0.0

            # Calculer l'erreur absolue moyenne
            erreurs = [abs(p - r) for p, r in zip(valeurs_predites, valeurs_reelles)]
            erreur_moyenne = sum(erreurs) / len(erreurs)

            # Convertir en similarité (0 à 1) avec normalisation adaptative
            max_valeur = max(max(valeurs_predites, default=0), max(valeurs_reelles, default=0))
            normalisation = max(10.0, max_valeur)  # Normalisation adaptative
            similarite = max(0.0, 1.0 - (erreur_moyenne / normalisation))

            # Debug pour GOD LEVEL
            if len(valeurs_predites) <= 4 and len(valeurs_reelles) <= 4:
                print(f"🔍 DEBUG SIMILARITE: predites={valeurs_predites}, reelles={valeurs_reelles}, erreurs={erreurs}, erreur_moyenne={erreur_moyenne:.3f}, similarite={similarite:.3f}")

            return similarite
        except:
            return 0.0
