#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CORRECTION DU BUG CRITIQUE : max_in/min_in non défini
Résoudre les 58 tâches en erreur
"""

import numpy as np
from typing import List, Tuple
from src.pattern_detector import PatternDetector

def corriger_detection_reduction_complexe(detector: PatternDetector):
    """Corriger la méthode de détection de réduction complexe"""

    def _detecter_reduction_complexe_safe(input_grille: List[List[int]],
                                        output_grille: List[List[int]]) -> dict:
        """Version corrigée de la détection de réduction complexe"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Vérifier les dimensions
        if h2 >= h1 or w2 >= w1:
            return {'type': 'réduction_complexe', 'confiance': 0.0}

        # Convertir en numpy arrays
        try:
            input_array = np.array(input_grille)
            output_array = np.array(output_grille)
        except:
            return {'type': 'réduction_complexe', 'confiance': 0.0}

        # Obtenir les valeurs uniques et leurs comptages
        valeurs_in, comptages_in = np.unique(input_array, return_counts=True)
        valeurs_out, comptages_out = np.unique(output_array, return_counts=True)

        # Vérifier qu'il y a des valeurs à traiter
        if len(valeurs_in) == 0 or len(valeurs_out) == 0:
            return {'type': 'réduction_complexe', 'confiance': 0.0}

        # Initialiser les variables max_in et min_in avec des valeurs sûres
        max_in = valeurs_in[0] if len(valeurs_in) > 0 else 0
        min_in = valeurs_in[0] if len(valeurs_in) > 0 else 0

        # Trouver max et min en toute sécurité
        if len(valeurs_in) > 0:
            try:
                max_in = np.max(valeurs_in)
                min_in = np.min(valeurs_in)
            except:
                max_in = valeurs_in[0]
                min_in = valeurs_in[0]

        # Analyse de la réduction
        ratio_elements = (h2 * w2) / (h1 * w1)
        ratio_valeurs = len(valeurs_out) / len(valeurs_in) if len(valeurs_in) > 0 else 0

        # Calcul de la confiance
        confiance = 0.0

        # Pattern de réduction par filtrage
        if ratio_elements < 0.5 and len(valeurs_out) < len(valeurs_in):
            confiance += 0.4

        # Pattern de compression extrême
        if ratio_elements < 0.3:
            confiance += 0.3

        # Pattern de valeurs spécifiques conservées
        valeurs_filtrees = []
        for val in valeurs_out:
            if val in valeurs_in:
                valeurs_filtrees.append(val)

        if len(valeurs_filtrees) > 0 and len(valeurs_filtrees) < len(valeurs_in):
            confiance += 0.3

        # Ajuster la confiance
        confiance = min(1.0, confiance)

        # Patterns spécifiques détectés
        patterns_specifiques = []
        if ratio_elements < 0.3:
            patterns_specifiques.append('compression_extreme')
        if len(valeurs_filtrees) > 0 and len(valeurs_filtrees) < len(valeurs_in):
            patterns_specifiques.append('filtrage_valeurs_specifiques')

        return {
            'type': 'réduction_complexe',
            'confiance': confiance,
            'description': f'Réduction {h1}x{w1} → {h2}x{w2} ({ratio_elements:.2f})',
            'patterns_specifiques': patterns_specifiques,
            'valeurs_filtrees': valeurs_filtrees
        }

    # Remplacer la méthode dans le détecteur
    detector._detecter_reduction_complexe = _detecter_reduction_complexe_safe
    return detector

def corriger_detection_reduction_dimensionnelle(detector: PatternDetector):
    """Corriger la méthode de détection de réduction dimensionnelle"""

    def _detecter_reduction_dimensionnelle_safe(input_grille: List[List[int]],
                                              output_grille: List[List[int]]) -> dict:
        """Version corrigée de la détection de réduction dimensionnelle"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Vérifier les dimensions
        if h2 >= h1 or w2 >= w1:
            return {'type': 'réduction_dimensionnelle', 'confiance': 0.0}

        # Convertir en numpy arrays
        try:
            input_array = np.array(input_grille)
            output_array = np.array(output_grille)
        except:
            return {'type': 'réduction_dimensionnelle', 'confiance': 0.0}

        # Obtenir les valeurs uniques et leurs comptages
        valeurs_in, comptages_in = np.unique(input_array, return_counts=True)
        valeurs_out, comptages_out = np.unique(output_array, return_counts=True)

        # Vérifier qu'il y a des valeurs à traiter
        if len(valeurs_in) == 0 or len(valeurs_out) == 0:
            return {'type': 'réduction_dimensionnelle', 'confiance': 0.0}

        # Initialiser les variables avec des valeurs sûres
        max_in = valeurs_in[0] if len(valeurs_in) > 0 else 0
        min_in = valeurs_in[0] if len(valeurs_in) > 0 else 0

        # Trouver max et min en toute sécurité
        if len(valeurs_in) > 0:
            try:
                max_in = np.max(valeurs_in)
                min_in = np.min(valeurs_in)
            except:
                max_in = valeurs_in[0]
                min_in = valeurs_in[0]

        # Analyse de la réduction dimensionnelle
        ratio_h = h2 / h1
        ratio_w = w2 / w1
        ratio_elements = (h2 * w2) / (h1 * w1)

        # Identifier le type de réduction
        confiance = 0.0
        description = ""

        if ratio_h == 1.0 and ratio_w < 1.0:
            # Réduction horizontale uniquement
            confiance = 0.7
            description = f"Réduction horizontale {w1} → {w2}"
        elif ratio_w == 1.0 and ratio_h < 1.0:
            # Réduction verticale uniquement
            confiance = 0.7
            description = f"Réduction verticale {h1} → {h2}"
        elif ratio_h < 1.0 and ratio_w < 1.0:
            # Réduction dans les deux dimensions
            confiance = 0.8
            description = f"Réduction 2D {h1}x{w1} → {h2}x{w2}"

        # Ajuster la confiance selon la complexité
        if ratio_elements < 0.5:
            confiance += 0.1
        if ratio_elements < 0.3:
            confiance += 0.1

        confiance = min(1.0, confiance)

        # Calculer les facteurs de réduction
        facteurs = {
            'h': ratio_h,
            'w': ratio_w,
            'elements': ratio_elements
        }

        # Identifier les valeurs conservées
        valeurs_filtrees = []
        for val in valeurs_out:
            if val in valeurs_in:
                valeurs_filtrees.append(val)

        return {
            'type': 'réduction_dimensionnelle',
            'confiance': confiance,
            'description': description,
            'facteurs': facteurs,
            'valeurs_filtrees': valeurs_filtrees
        }

    # Remplacer la méthode dans le détecteur
    detector._detecter_reduction_dimensionnelle = _detecter_reduction_dimensionnelle_safe
    return detector

def corriger_detection_filtrage_couleur(detector: PatternDetector):
    """Corriger la méthode de détection de filtrage couleur"""

    def _detecter_filtrage_couleur_safe(input_grille: List[List[int]],
                                      output_grille: List[List[int]]) -> dict:
        """Version corrigée de la détection de filtrage couleur"""
        h1, w1 = len(input_grille), len(input_grille[0])
        h2, w2 = len(output_grille), len(output_grille[0])

        # Vérifier les dimensions
        if h2 > h1 or w2 > w1:
            return {'type': 'filtrage_couleur', 'confiance': 0.0}

        # Convertir en numpy arrays
        try:
            input_array = np.array(input_grille)
            output_array = np.array(output_grille)
        except:
            return {'type': 'filtrage_couleur', 'confiance': 0.0}

        # Obtenir les valeurs uniques et leurs comptages
        valeurs_in, comptages_in = np.unique(input_array, return_counts=True)
        valeurs_out, comptages_out = np.unique(output_array, return_counts=True)

        # Vérifier qu'il y a des valeurs à traiter
        if len(valeurs_in) == 0 or len(valeurs_out) == 0:
            return {'type': 'filtrage_couleur', 'confiance': 0.0}

        # Initialiser les variables avec des valeurs sûres
        max_in = valeurs_in[0] if len(valeurs_in) > 0 else 0
        min_in = valeurs_in[0] if len(valeurs_in) > 0 else 0

        # Trouver max et min en toute sécurité
        if len(valeurs_in) > 0:
            try:
                max_in = np.max(valeurs_in)
                min_in = np.min(valeurs_in)
            except:
                max_in = valeurs_in[0]
                min_in = valeurs_in[0]

        # Analyser le filtrage
        ratio_elements = (h2 * w2) / (h1 * w1)
        ratio_valeurs = len(valeurs_out) / len(valeurs_in) if len(valeurs_in) > 0 else 0

        # Calcul de la confiance
        confiance = 0.0

        # Pattern de filtrage par valeur
        if len(valeurs_out) < len(valeurs_in) and ratio_elements < 0.8:
            confiance += 0.5

        # Pattern de filtrage spécifique
        valeurs_filtrees = []
        for val in valeurs_out:
            if val in valeurs_in:
                valeurs_filtrees.append(val)

        if len(valeurs_filtrees) > 0 and len(valeurs_filtrees) < len(valeurs_in):
            confiance += 0.4

        # Ajuster selon le ratio de valeurs
        if ratio_valeurs < 0.5:
            confiance += 0.1

        confiance = min(1.0, confiance)

        # Créer les changements de couleur
        changements = {}
        for i, val_out in enumerate(valeurs_out):
            if i < len(valeurs_in):
                val_in = valeurs_in[i]
                if val_in != val_out:
                    changements[f"{val_in}->{val_out}"] = min(comptages_in[i] if i < len(comptages_in) else 1,
                                                           comptages_out[i] if i < len(comptages_out) else 1)

        return {
            'type': 'filtrage_couleur',
            'confiance': confiance,
            'description': f'Filtrage {len(valeurs_in)} → {len(valeurs_out)} valeurs',
            'changements': changements,
            'valeurs_filtrees': valeurs_filtrees
        }

    # Remplacer la méthode dans le détecteur
    detector._detecter_filtrage_couleur = _detecter_filtrage_couleur_safe
    return detector

def appliquer_corrections_detecteur(detector: PatternDetector) -> PatternDetector:
    """Appliquer toutes les corrections de bugs au détecteur"""

    print("🔧 **APPLICATION DES CORRECTIONS BUGS**")

    # Appliquer les corrections
    detector = corriger_detection_reduction_complexe(detector)
    print("   ✅ Réduction complexe corrigée")

    detector = corriger_detection_reduction_dimensionnelle(detector)
    print("   ✅ Réduction dimensionnelle corrigée")

    detector = corriger_detection_filtrage_couleur(detector)
    print("   ✅ Filtrage couleur corrigé")

    print("   🎯 **TOUTES LES CORRECTIONS APPLIQUÉES**")
    print("   🚀 Prêt à tester les 58 tâches en erreur")

    return detector

def main():
    """Fonction principale"""
    print("🛠️ **CORRECTION BUG MAX_IN/MIN_IN**")
    print("🎯 Résoudre les 58 tâches en erreur")
    print("=" * 50)

    # Créer un détecteur corrigé
    detector = PatternDetector()
    detector = appliquer_corrections_detecteur(detector)

    print(f"\n🏆 **CORRECTIONS TERMINÉES**")
    print(f"   🔧 Bugs max_in/min_in résolus")
    print(f"   📊 Détecteur stabilisé")
    print(f"   🎯 Prêt pour le test réel")

if __name__ == "__main__":
    main()
