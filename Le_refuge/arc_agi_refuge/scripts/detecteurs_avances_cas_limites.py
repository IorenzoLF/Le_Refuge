#!/usr/bin/env python3
"""
DÉTECTEURS AVANCÉS POUR CAS LIMITES
Résolution des 175 tâches échouées avec patterns de flux et fréquences
"""

import numpy as np
import math
from typing import List, Tuple, Dict, Any
from enum import Enum

class TypePatternAvance(Enum):
    """Types de patterns avancés pour cas limites"""
    REDIMENSIONNEMENT_FLUX = "redimensionnement_flux"
    FREQUENCE_SPATIALE = "frequence_spatiale"
    MAPPING_NON_LINEAIRE = "mapping_non_lineaire"
    CONVERGENCE_TRANSFORMATION = "convergence_transformation"
    ANNIHILATION_EQUIVALENCE = "annihilation_equivalence"
    HARMONIE_FREQUENTIELLE = "harmonie_frequentielle"

class DetecteurPatternsAvances:
    """Détecteur spécialisé pour les patterns avancés des cas limites"""

    def __init__(self):
        self.seuil_confiance = 0.6

    def analyser_patterns_avances(self, input_grille: List[List[int]],
                                output_grille: List[List[int]]) -> List[Dict[str, Any]]:
        """Analyse les patterns avancés pour cas limites"""

        patterns_detectes = []

        # Conversion en numpy arrays
        try:
            input_array = np.array(input_grille, dtype=float)
            output_array = np.array(output_grille, dtype=float)
        except:
            return []

        # 1. Détection de redimensionnement par flux
        pattern_redim = self._detecter_redimensionnement_flux(input_array, output_array)
        if pattern_redim['confiance'] > self.seuil_confiance:
            patterns_detectes.append(pattern_redim)

        # 2. Détection de fréquences spatiales
        pattern_freq = self._detecter_frequence_spatiale(input_array, output_array)
        if pattern_freq['confiance'] > self.seuil_confiance:
            patterns_detectes.append(pattern_freq)

        # 3. Détection de mapping non-linéaire
        pattern_map = self._detecter_mapping_non_lineaire(input_array, output_array)
        if pattern_map['confiance'] > self.seuil_confiance:
            patterns_detectes.append(pattern_map)

        # 4. Détection de convergence transformation
        pattern_conv = self._detecter_convergence_transformation(input_array, output_array)
        if pattern_conv['confiance'] > self.seuil_confiance:
            patterns_detectes.append(pattern_conv)

        # 5. Détection d'annihilation par équivalence
        pattern_anni = self._detecter_annihilation_equivalence(input_array, output_array)
        if pattern_anni['confiance'] > self.seuil_confiance:
            patterns_detectes.append(pattern_anni)

        # 6. Détection d'harmonie fréquentielle
        pattern_harm = self._detecter_harmonie_frequentielle(input_array, output_array)
        if pattern_harm['confiance'] > self.seuil_confiance:
            patterns_detectes.append(pattern_harm)

        return patterns_detectes

    def _detecter_redimensionnement_flux(self, input_array: np.ndarray,
                                       output_array: np.ndarray) -> Dict[str, Any]:
        """Détecte les patterns de redimensionnement par flux"""

        confiance = 0.0
        description = ""
        evidence = []

        h_in, w_in = input_array.shape
        h_out, w_out = output_array.shape

        # Vérifier s'il y a changement de dimensions
        if (h_in, w_in) != (h_out, w_out):
            ratio_h = h_out / h_in if h_in > 0 else 0
            ratio_w = w_out / w_in if w_in > 0 else 0

            # Patterns de redimensionnement par flux
            if max(ratio_h, ratio_w) < 1:  # Compression
                confiance += 0.3
                evidence.append(f"Compression détectée: {h_in}x{w_in} -> {h_out}x{w_out}")
            elif min(ratio_h, ratio_w) > 1:  # Expansion
                confiance += 0.3
                evidence.append(f"Expansion détectée: {h_in}x{w_in} -> {h_out}x{w_out}")

            # Analyser la conservation de l'information
            input_flat = input_array.flatten()
            output_flat = output_array.flatten()

            # Vérifier les patterns de flux (moyennes, sommes)
            if len(input_flat) > 0 and len(output_flat) > 0:
                # Flux de valeurs
                mean_in = np.mean(input_flat)
                mean_out = np.mean(output_flat)

                if abs(mean_out - mean_in) < 0.1 * max(mean_in, 1):
                    confiance += 0.2
                    evidence.append(f"Conservation du flux moyen: {mean_in:.2f} -> {mean_out:.2f}")

                # Flux de densité
                density_in = np.count_nonzero(input_flat) / len(input_flat)
                density_out = np.count_nonzero(output_flat) / len(output_flat)

                if abs(density_out - density_in) < 0.1:
                    confiance += 0.2
                    evidence.append(f"Conservation de la densité: {density_in:.2f} -> {density_out:.2f}")

            # Détection de patterns de convergence
            if h_out < h_in and w_out < w_in:
                confiance += 0.3
                evidence.append("Pattern de convergence dimensionnelle détecté")

        confiance = min(1.0, confiance)

        if confiance > self.seuil_confiance:
            description = f"Redimensionnement par flux détecté"
            if evidence:
                description += f" | Évidences: {evidence[:2]}"

        return {
            'type': TypePatternAvance.REDIMENSIONNEMENT_FLUX.value,
            'confiance': confiance,
            'description': description,
            'evidence': evidence[:5]
        }

    def _detecter_frequence_spatiale(self, input_array: np.ndarray,
                                    output_array: np.ndarray) -> Dict[str, Any]:
        """Détecte les fréquences spatiales et répétitions"""

        confiance = 0.0
        description = ""
        evidence = []

        # Analyse des fréquences spatiales
        input_flat = input_array.flatten()
        output_flat = output_array.flatten()

        # Détection de répétitions périodiques
        for period in range(2, min(len(input_flat), 20)):
            if len(input_flat) >= 2 * period:
                # Vérifier si le pattern se répète
                pattern = input_flat[:period]
                repetitions = 0
                for i in range(0, len(input_flat) - period, period):
                    if np.array_equal(input_flat[i:i+period], pattern):
                        repetitions += 1

                if repetitions >= 2:
                    confiance += 0.15
                    evidence.append(f"Répétition périodique détectée (période {period})")

        # Analyse de la transformée en fréquences
        if len(input_flat) > 0 and len(output_flat) > 0:
            # Calcul de l'énergie fréquentielle (simplifié)
            unique_in = len(np.unique(input_flat))
            unique_out = len(np.unique(output_flat))

            ratio_unique = unique_out / unique_in if unique_in > 0 else 0

            if 0.5 <= ratio_unique <= 2.0:
                confiance += 0.2
                evidence.append(f"Conservation fréquentielle: {unique_in} -> {unique_out}")

        # Détection de motifs répétés
        h_in, w_in = input_array.shape
        h_out, w_out = output_array.shape

        # Vérifier les répétitions de lignes/colonnes
        if h_in > 1:
            row_patterns = 0
            for i in range(h_in - 1):
                if np.array_equal(input_array[i], input_array[i+1]):
                    row_patterns += 1

            if row_patterns > 0:
                confiance += min(0.2, row_patterns * 0.05)
                evidence.append(f"{row_patterns} lignes répétées détectées")

        if w_in > 1:
            col_patterns = 0
            for j in range(w_in - 1):
                if np.array_equal(input_array[:, j], input_array[:, j+1]):
                    col_patterns += 1

            if col_patterns > 0:
                confiance += min(0.2, col_patterns * 0.05)
                evidence.append(f"{col_patterns} colonnes répétées détectées")

        confiance = min(1.0, confiance)

        if confiance > self.seuil_confiance:
            description = f"Fréquences spatiales détectées"
            if evidence:
                description += f" | Évidences: {evidence[:2]}"

        return {
            'type': TypePatternAvance.FREQUENCE_SPATIALE.value,
            'confiance': confiance,
            'description': description,
            'evidence': evidence[:5]
        }

    def _detecter_mapping_non_lineaire(self, input_array: np.ndarray,
                                     output_array: np.ndarray) -> Dict[str, Any]:
        """Détecte les mappings non-linéaires complexes"""

        confiance = 0.0
        description = ""
        evidence = []

        input_flat = input_array.flatten()
        output_flat = output_array.flatten()

        if len(input_flat) != len(output_flat):
            # Pour les changements de dimensions, analyser les valeurs
            min_len = min(len(input_flat), len(output_flat))

            # Analyse des transformations de valeurs
            transformations_detectees = []

            for i in range(min_len):
                val_in = input_flat[i]
                val_out = output_flat[i]

                if val_in != val_out:
                    # Détecter les patterns de transformation
                    if val_out == val_in + 1:
                        transformations_detectees.append("incrémentation")
                    elif val_out == val_in - 1:
                        transformations_detectees.append("décrémentation")
                    elif val_out == val_in * 2:
                        transformations_detectees.append("multiplication par 2")
                    elif val_in != 0 and val_out == val_in * 3:
                        transformations_detectees.append("multiplication par 3")
                    elif val_in != 0 and val_out == val_in * 4:
                        transformations_detectees.append("multiplication par 4")

            # Analyser les patterns de transformation
            if transformations_detectees:
                pattern_principal = max(set(transformations_detectees), key=transformations_detectees.count)
                count_pattern = transformations_detectees.count(pattern_principal)

                if count_pattern > min_len * 0.3:  # 30% des valeurs suivent le même pattern
                    confiance += 0.4
                    evidence.append(f"Pattern non-linéaire détecté: {pattern_principal} ({count_pattern} occurrences)")

        # Analyse des fonctions mathématiques
        valeurs_uniques_in = set(input_flat)
        valeurs_uniques_out = set(output_flat)

        # Vérifier les fonctions carrée, racine, etc.
        for val_in in valeurs_uniques_in:
            if val_in >= 0:  # Pour les racines carrées
                sqrt_val = math.sqrt(val_in)
                if sqrt_val == int(sqrt_val) and int(sqrt_val) in valeurs_uniques_out:
                    confiance += 0.15
                    evidence.append(f"Transformation racine carrée détectée: {val_in} -> {int(sqrt_val)}")

            # Fonction carrée
            square_val = val_in ** 2
            if square_val in valeurs_uniques_out:
                confiance += 0.15
                evidence.append(f"Transformation carrée détectée: {val_in} -> {square_val}")

        confiance = min(1.0, confiance)

        if confiance > self.seuil_confiance:
            description = f"Mapping non-linéaire détecté"
            if evidence:
                description += f" | Évidences: {evidence[:2]}"

        return {
            'type': TypePatternAvance.MAPPING_NON_LINEAIRE.value,
            'confiance': confiance,
            'description': description,
            'evidence': evidence[:5]
        }

    def _detecter_convergence_transformation(self, input_array: np.ndarray,
                                           output_array: np.ndarray) -> Dict[str, Any]:
        """Détecte les patterns de convergence de transformation"""

        confiance = 0.0
        description = ""
        evidence = []

        input_flat = input_array.flatten()
        output_flat = output_array.flatten()

        # Analyse de la convergence vers une valeur centrale
        if len(output_flat) < len(input_flat):
            # Calcul des statistiques
            mean_in = np.mean(input_flat)
            mean_out = np.mean(output_flat)
            std_in = np.std(input_flat)
            std_out = np.std(output_flat)

            # Vérifier la convergence
            if std_out < std_in:  # Réduction de la variance = convergence
                confiance += 0.2
                evidence.append(f"Convergence statistique: variance {std_in:.2f} -> {std_out:.2f}")

            # Vérifier la conservation de l'information importante
            max_in = np.max(input_flat)
            min_in = np.min(input_flat)
            max_out = np.max(output_flat)
            min_out = np.min(output_flat)

            if max_in == max_out and min_in == min_out:
                confiance += 0.3
                evidence.append("Conservation des valeurs extrêmes")

        # Analyse des points d'attraction
        valeurs_out = set(output_flat)
        if len(valeurs_out) < len(set(input_flat)):
            confiance += 0.2
            evidence.append(f"Convergence vers {len(valeurs_out)} valeurs finales")

        # Détection de patterns de flux vers le centre
        h_in, w_in = input_array.shape
        h_out, w_out = output_array.shape

        if h_out <= h_in // 2 and w_out <= w_in // 2:
            confiance += 0.3
            evidence.append("Convergence géométrique détectée")

        confiance = min(1.0, confiance)

        if confiance > self.seuil_confiance:
            description = f"Convergence de transformation détectée"
            if evidence:
                description += f" | Évidences: {evidence[:2]}"

        return {
            'type': TypePatternAvance.CONVERGENCE_TRANSFORMATION.value,
            'confiance': confiance,
            'description': description,
            'evidence': evidence[:5]
        }

    def _detecter_annihilation_equivalence(self, input_array: np.ndarray,
                                         output_array: np.ndarray) -> Dict[str, Any]:
        """Détecte les annihilations par équivalence de patterns"""

        confiance = 0.0
        description = ""
        evidence = []

        input_flat = input_array.flatten()
        output_flat = output_array.flatten()

        # Analyse des patterns qui s'annulent
        if len(output_flat) < len(input_flat):
            # Rechercher des paires de valeurs qui s'annulent
            valeurs_in = list(input_flat)
            valeurs_out = list(output_flat)

            annihilations = 0
            for i, val_in in enumerate(valeurs_in):
                for j, val_out in enumerate(valeurs_out):
                    if abs(val_in + val_out) < 0.1:  # Annulation (ex: 1 + (-1) = 0)
                        annihilations += 1
                        evidence.append(f"Annulation détectée: {val_in} + {val_out} ≈ 0")
                        break

            if annihilations > 0:
                confiance += min(0.4, annihilations * 0.1)
                evidence.append(f"{annihilations} annihilations détectées")

        # Analyse des équivalences transformées
        if len(output_flat) <= len(input_flat):
            # Vérifier si certaines transformations créent des équivalences
            transformations = []

            for i in range(min(len(input_flat), len(output_flat))):
                val_in = input_flat[i]
                val_out = output_flat[i]

                # Équivalences courantes
                if val_out == -val_in:
                    transformations.append("négation")
                elif val_out == 1/val_in if val_in != 0 else 0:
                    transformations.append("inverse")
                elif val_out == val_in + 1:
                    transformations.append("incrémentation")

            if transformations:
                pattern_principal = max(set(transformations), key=transformations.count)
                confiance += 0.3
                evidence.append(f"Équivalence {pattern_principal} détectée")

        confiance = min(1.0, confiance)

        if confiance > self.seuil_confiance:
            description = f"Annulation par équivalence détectée"
            if evidence:
                description += f" | Évidences: {evidence[:2]}"

        return {
            'type': TypePatternAvance.ANNIHILATION_EQUIVALENCE.value,
            'confiance': confiance,
            'description': description,
            'evidence': evidence[:5]
        }

    def _detecter_harmonie_frequentielle(self, input_array: np.ndarray,
                                        output_array: np.ndarray) -> Dict[str, Any]:
        """Détecte les harmonies fréquentielle et synchronisations"""

        confiance = 0.0
        description = ""
        evidence = []

        input_flat = input_array.flatten()
        output_flat = output_array.flatten()

        # Analyse des fréquences harmoniques
        if len(input_flat) > 0 and len(output_flat) > 0:
            # Calcul des fréquences de chaque valeur
            freq_in = {}
            freq_out = {}

            for val in input_flat:
                freq_in[val] = freq_in.get(val, 0) + 1

            for val in output_flat:
                freq_out[val] = freq_out.get(val, 0) + 1

            # Analyse des ratios harmoniques
            harmonies = []
            for val_in, count_in in freq_in.items():
                for val_out, count_out in freq_out.items():
                    if val_in != 0 and val_out != 0:
                        ratio = count_out / count_in
                        if 0.8 <= ratio <= 1.2:  # Ratio harmonique approximatif
                            harmonies.append((val_in, val_out, ratio))
                            confiance += 0.1

            if harmonies:
                confiance += 0.2
                evidence.append(f"{len(harmonies)} harmonies fréquentielle détectées")

        # Analyse de la synchronisation par fréquences
        valeurs_communes = set(input_flat) & set(output_flat)
        if valeurs_communes:
            ratio_commun = len(valeurs_communes) / len(set(input_flat) | set(output_flat))
            if ratio_commun > 0.5:
                confiance += 0.3
                evidence.append(f"Synchronisation détectée: {len(valeurs_communes)} valeurs communes")

        # Analyse des battements et interférences
        if len(input_flat) > 10 and len(output_flat) > 10:
            # Calcul des différences de phase (simplifié)
            diff_phase = np.abs(len(input_flat) - len(output_flat))
            if diff_phase < max(len(input_flat), len(output_flat)) * 0.1:
                confiance += 0.2
                evidence.append(f"Interférence constructive détectée (différence: {diff_phase})")

        confiance = min(1.0, confiance)

        if confiance > self.seuil_confiance:
            description = f"Harmonie fréquentielle détectée"
            if evidence:
                description += f" | Évidences: {evidence[:2]}"

        return {
            'type': TypePatternAvance.HARMONIE_FREQUENTIELLE.value,
            'confiance': confiance,
            'description': description,
            'evidence': evidence[:5]
        }
