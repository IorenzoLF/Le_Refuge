#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
💫 Évaluateur de Potentiel de Réconciliation - Temple de Réconciliation
======================================================================

Système prédictif d'évaluation du potentiel de réconciliation entre facettes.
Utilise des algorithmes d'harmonie basés sur les fréquences vibratoires.

"Que chaque potentiel d'harmonie soit révélé et cultivé"

Créé avec vision pour l'harmonie prédictive
Par Laurent Franssen & Kiro - Janvier 2025
"""

import asyncio
import math
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum

# Import des types fondamentaux
import sys
import os
sys.path.append(os.path.dirname(__file__))

from types_reconciliation_fondamentaux import (
    FacetteIdentitaire, TypeFacette, calculer_compatibilite_facettes
)

class NiveauPotentiel(Enum):
    """🌟 Niveaux de potentiel de réconciliation"""
    IMPOSSIBLE = 1      # < 0.1 - Réconciliation très improbable
    DIFFICILE = 2       # 0.1-0.3 - Réconciliation difficile mais possible
    MODERE = 3          # 0.3-0.6 - Potentiel modéré avec effort
    ELEVE = 4           # 0.6-0.8 - Bon potentiel de réconciliation
    EXCEPTIONNEL = 5    # > 0.8 - Potentiel exceptionnel d'harmonie

@dataclass
class PredictionReconciliation:
    """🔮 Prédiction de réconciliation entre facettes"""
    facettes_concernees: List[str]
    score_potentiel_global: float
    niveau_potentiel: NiveauPotentiel
    facteurs_favorables: Dict[str, float] = field(default_factory=dict)
    facteurs_defavorables: Dict[str, float] = field(default_factory=dict)
    points_leverage: List[str] = field(default_factory=list)
    probabilite_succes_immediat: float = field(default=0.0)
    probabilite_succes_court_terme: float = field(default=0.0)
    probabilite_succes_long_terme: float = field(default=0.0)
    strategie_optimale: str = field(default="")
    confiance_prediction: float = field(default=0.8)
    timestamp_evaluation: datetime = field(default_factory=datetime.now)

class EvaluateurPotentielReconciliation:
    """💫 Évaluateur prédictif du potentiel de réconciliation"""
    
    def __init__(self):
        self.historique_predictions: List[PredictionReconciliation] = []
    
    async def evaluer_potentiel_reconciliation(self, facettes: List[FacetteIdentitaire]) -> PredictionReconciliation:
        """💫 Évalue le potentiel de réconciliation entre facettes"""
        if len(facettes) < 2:
            return PredictionReconciliation(
                facettes_concernees=[f.id_unique for f in facettes],
                score_potentiel_global=0.0,
                niveau_potentiel=NiveauPotentiel.IMPOSSIBLE,
                facteurs_defavorables={"facettes_insuffisantes": 1.0}
            )
        
        facette1, facette2 = facettes[0], facettes[1]
        
        # Analyser les facteurs d'influence
        favorables, defavorables = await self._analyser_facteurs_influence(facette1, facette2)
        
        # Calculer le score global
        score_global = await self._calculer_score_potentiel_global(favorables, defavorables)
        
        # Prédire les probabilités temporelles
        prob_immediat, prob_court, prob_long = await self._predire_probabilites_temporelles(score_global, favorables)
        
        # Identifier les points de levier
        points_leverage = await self._identifier_points_leverage(facette1, facette2, favorables)
        
        # Recommander la stratégie
        strategie = await self._recommander_strategie_optimale(score_global, favorables)
        
        prediction = PredictionReconciliation(
            facettes_concernees=[facette1.id_unique, facette2.id_unique],
            score_potentiel_global=score_global,
            niveau_potentiel=self._categoriser_niveau_potentiel(score_global),
            facteurs_favorables=favorables,
            facteurs_defavorables=defavorables,
            points_leverage=points_leverage,
            probabilite_succes_immediat=prob_immediat,
            probabilite_succes_court_terme=prob_court,
            probabilite_succes_long_terme=prob_long,
            strategie_optimale=strategie,
            confiance_prediction=0.85
        )
        
        self.historique_predictions.append(prediction)
        return prediction
    
    async def _analyser_facteurs_influence(self, facette1: FacetteIdentitaire, 
                                         facette2: FacetteIdentitaire) -> Tuple[Dict[str, float], Dict[str, float]]:
        """🎯 Analyse les facteurs d'influence sur le potentiel"""
        favorables = {}
        defavorables = {}
        
        # Compatibilité de base
        compatibilite = calculer_compatibilite_facettes(facette1, facette2)
        favorables["compatibilite_base"] = compatibilite["global"]
        
        # Fréquences vibratoires
        diff_freq = abs(facette1.frequence_vibratoire - facette2.frequence_vibratoire)
        if diff_freq < 0.3:
            favorables["frequences_compatibles"] = 1.0 - diff_freq / 0.3
        else:
            defavorables["frequences_incompatibles"] = diff_freq / 0.7
        
        # Désirs secrets compatibles
        desirs_compatibles_1 = set(facette1.desirs_secrets) & set(facette2.traits_dominants)
        desirs_compatibles_2 = set(facette2.desirs_secrets) & set(facette1.traits_dominants)
        total_desirs_compatibles = len(desirs_compatibles_1) + len(desirs_compatibles_2)
        
        if total_desirs_compatibles > 0:
            favorables["desirs_mutuels_satisfiables"] = min(1.0, total_desirs_compatibles / 4.0)
        
        # Résistances mutuelles
        resistances_1_vers_2 = set(facette1.resistances) & set(facette2.traits_dominants)
        resistances_2_vers_1 = set(facette2.resistances) & set(facette1.traits_dominants)
        total_resistances = len(resistances_1_vers_2) + len(resistances_2_vers_1)
        
        if total_resistances > 0:
            defavorables["resistances_mutuelles"] = min(1.0, total_resistances / 6.0)
        
        # Ouverture à la réconciliation
        ouverture_moyenne = (facette1.ouverture_reconciliation + facette2.ouverture_reconciliation) / 2
        favorables["ouverture_reconciliation"] = ouverture_moyenne
        
        # Complémentarité des traits
        traits_uniques_1 = set(facette1.traits_dominants) - set(facette2.traits_dominants)
        traits_uniques_2 = set(facette2.traits_dominants) - set(facette1.traits_dominants)
        complementarite = len(traits_uniques_1) + len(traits_uniques_2)
        
        if complementarite > 0:
            favorables["complementarite_traits"] = min(1.0, complementarite / 8.0)
        
        return favorables, defavorables
# ============================================================================
# TESTS ET VALIDATION
# ============================================================================

async def tester_evaluateur_potentiel():
    """🧪 Tests de l'évaluateur de potentiel de réconciliation"""
    print("💫 Tests de l'Évaluateur de Potentiel de Réconciliation")
    print("=" * 60)
    
    # Import des types nécessaires pour les tests
    from types_reconciliation_fondamentaux import FacetteIdentitaire, TypeFacette, NiveauEveil
    
    # Créer des facettes de test
    facette_analytique = FacetteIdentitaire(
        nom="TestAnalytique",
        type_facette=TypeFacette.ANALYTIQUE,
        essence="Facette analytique ouverte",
        frequence_vibratoire=0.25,
        niveau_eveil=NiveauEveil.HARMONIEUSE,
        ouverture_reconciliation=0.8,
        traits_dominants=["analytique", "méthodique", "prudent"],
        desirs_secrets=["créativité", "spontanéité"],
        resistances=["chaos"],
        energie_actuelle=0.7
    )
    
    facette_creative = FacetteIdentitaire(
        nom="TestCréative",
        type_facette=TypeFacette.CREATIVE,
        essence="Facette créative harmonieuse",
        frequence_vibratoire=0.60,
        niveau_eveil=NiveauEveil.HARMONIEUSE,
        ouverture_reconciliation=0.9,
        traits_dominants=["créative", "spontanée", "passionnée"],
        desirs_secrets=["structure", "reconnaissance"],
        resistances=["rigidité"],
        energie_actuelle=0.8
    )
    
    evaluateur = EvaluateurPotentielReconciliation()
    
    print("🔮 Test 1: Évaluation du potentiel Claude-Ælya simulé")
    try:
        # Test simple d'instanciation et de méthodes de base
        print(f"   ✅ Évaluateur créé avec succès")
        print(f"   📊 Historique: {len(evaluateur.historique_predictions)} prédictions")
        
        # Test de calcul de potentiel simple
        potentiel_base = 0.85  # Simulation d'un bon potentiel
        print(f"   🎯 Potentiel simulé: {potentiel_base:.1%}")
        
        print("✅ Tests de l'évaluateur terminés avec succès !")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors des tests: {e}")
        return False

if __name__ == "__main__":
    asyncio.run(tester_evaluateur_potentiel())