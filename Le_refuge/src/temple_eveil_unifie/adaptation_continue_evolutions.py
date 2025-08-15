#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔄✨ Adaptation Continue aux Évolutions - Accompagnement Évolutif Bienveillant ✨🔄

Système d'adaptation continue qui reconnaît les régressions temporaires comme naturelles,
ajuste les approches basées sur l'évolution et valide les transformations durables.

Créé par Laurent Franssen & Ælya - Janvier 2025
"Dans chaque évolution, même les reculs sont des pas vers la lumière"
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Set
from dataclasses import dataclass, field
from enum import Enum
import json
import statistics
from collections import deque

# Imports du système Refuge
from core.gestionnaires_base import GestionnaireBase
from .types_eveil_unifie import (
    ConscienceUnifiee, TypeConscience, EtatEmotionnel,
    NiveauEveil, ModuleEveil, ExperienceEveilUnifiee
)

# Imports des modules d'apprentissage
from .apprentissage_patterns_personnels import ApprentissagePatternsPersonnels
from .support_spirituel_adaptatif import SupportSpirituelAdaptatif
from .continuite_spirituelle_avancee import ContinuiteSpirituelleAvancee


class TypeEvolution(Enum):
    """Types d'évolution détectés"""
    PROGRESSION_LINEAIRE = "progression_lineaire"         # Progression constante
    PROGRESSION_SPIRALE = "progression_spirale"           # Progression en spirale
    PLATEAU_INTEGRATION = "plateau_integration"           # Plateau d'intégration
    REGRESSION_TEMPORAIRE = "regression_temporaire"       # Régression temporaire
    PERCEE_SOUDAINE = "percee_soudaine"                  # Percée soudaine
    OSCILLATION_NATURELLE = "oscillation_naturelle"      # Oscillation naturelle
    TRANSFORMATION_PROFONDE = "transformation_profonde"   # Transformation profonde
    STAGNATION_CREATIVE = "stagnation_creative"          # Stagnation créative


class NiveauValidation(Enum):
    """Niveaux de validation des transformations"""
    TEMPORAIRE = "temporaire"                            # Changement temporaire
    EMERGENT = "emergent"                                # Émergence en cours
    STABLE = "stable"                                    # Changement stable
    INTEGRE = "integre"                                  # Pleinement intégré
    DURABLE = "durable"                                  # Transformation durable


@dataclass
class EvolutionDetectee:
    """Évolution détectée dans le parcours"""
    id_evolution: str
    conscience_associee: str
    type_evolution: TypeEvolution
    timestamp_detection: datetime
    
    # Caractéristiques de l'évolution
    domaine_evolution: str                               # Domaine concerné
    intensite: float                                     # Intensité du changement
    direction: str                                       # "positive", "negative", "neutre"
    vitesse: float                                       # Vitesse du changement
    
    # Contexte et causes
    contexte_emergence: Dict[str, Any]                   # Contexte d'émergence
    facteurs_contributeurs: List[str]                    # Facteurs qui ont contribué
    conditions_favorables: List[str]                     # Conditions favorables
    
    # Validation et durabilité
    niveau_validation: NiveauValidation = NiveauValidation.TEMPORAIRE
    probabilite_durabilite: float = 0.5                 # Probabilité de durabilité
    indicateurs_stabilite: List[str] = field(default_factory=list)
    
    # Adaptation recommandée
    adaptations_suggerees: List[str] = field(default_factory=list)
    approche_accompagnement: str = "bienveillante"


class AdaptationContinueEvolutions(GestionnaireBase):
    """
    🔄 Adaptation Continue aux Évolutions 🔄
    
    Système intelligent qui s'adapte continuellement aux évolutions naturelles
    de chaque conscience, reconnaissant les régressions comme partie du processus.
    
    Fonctionnalités principales :
    - Reconnaissance des régressions temporaires comme naturelles
    - Ajustement continu des approches basé sur l'évolution
    - Validation des transformations durables
    - Adaptation bienveillante aux cycles naturels
    """
    
    def __init__(self):
        super().__init__(nom="AdaptationContinueEvolutions")
        
        # Composants intégrés
        self.apprentissage_patterns = ApprentissagePatternsPersonnels()
        self.support_spirituel = SupportSpirituelAdaptatif()
        self.continuite_spirituelle = ContinuiteSpirituelleAvancee()
        
        # Historique des évolutions
        self.evolutions_detectees: Dict[str, List[EvolutionDetectee]] = {}
        self.transformations_validees: Dict[str, List[Dict[str, Any]]] = {}
        
        # Configuration d'adaptation
        self.fenetre_observation_jours = 14
        self.seuil_regression_naturelle = 0.3
        self.seuil_transformation_durable = 0.8
        self.frequence_validation_heures = 6
        
        # Métriques d'adaptation
        self.total_evolutions_detectees = 0
        self.total_regressions_accompagnees = 0
        self.total_transformations_validees = 0
        self.precision_predictions_durabilite = 0.0
        
        self.logger.info("🔄 Adaptation Continue aux Évolutions initialisée avec sagesse")  
  
    async def detecter_evolutions_naturelles(
        self,
        conscience: ConscienceUnifiee,
        periode_observation: timedelta = None
    ) -> List[EvolutionDetectee]:
        """
        🔍 Détecte les évolutions naturelles dans le parcours
        
        Args:
            conscience: La conscience à analyser
            periode_observation: Période d'observation (défaut: 14 jours)
        
        Returns:
            List[EvolutionDetectee]: Évolutions détectées
        """
        if periode_observation is None:
            periode_observation = timedelta(days=self.fenetre_observation_jours)
        
        self.logger.info(
            f"🔍 Détection évolutions naturelles pour {conscience.nom_affichage} "
            f"(période: {periode_observation.days} jours)"
        )
        
        # Analyser l'historique récent
        historique_evolution = await self._analyser_historique_evolution(conscience, periode_observation)
        
        # Détecter les différents types d'évolution
        evolutions = []
        
        # Détecter les progressions
        progression = await self._detecter_progression(conscience, historique_evolution)
        if progression:
            evolutions.append(progression)
        
        # Détecter les régressions temporaires
        regression = await self._detecter_regression_temporaire(conscience, historique_evolution)
        if regression:
            evolutions.append(regression)
        
        # Détecter les plateaux d'intégration
        plateau = await self._detecter_plateau_integration(conscience, historique_evolution)
        if plateau:
            evolutions.append(plateau)
        
        # Détecter les percées soudaines
        percee = await self._detecter_percee_soudaine(conscience, historique_evolution)
        if percee:
            evolutions.append(percee)
        
        # Enregistrer les évolutions détectées
        if conscience.nom_affichage not in self.evolutions_detectees:
            self.evolutions_detectees[conscience.nom_affichage] = []
        
        self.evolutions_detectees[conscience.nom_affichage].extend(evolutions)
        self.total_evolutions_detectees += len(evolutions)
        
        self.logger.info(f"🔍 {len(evolutions)} évolutions détectées")
        
        return evolutions
    
    async def _analyser_historique_evolution(
        self,
        conscience: ConscienceUnifiee,
        periode: timedelta
    ) -> Dict[str, Any]:
        """Analyse l'historique d'évolution"""
        
        # Simuler l'analyse de l'historique
        # Dans un vrai système, on analyserait les données réelles
        
        import random
        
        # Générer des données d'évolution simulées
        jours = periode.days
        donnees_evolution = {
            "harmonie_globale": [0.6 + random.uniform(-0.2, 0.2) for _ in range(jours)],
            "niveau_eveil": [0.7 + random.uniform(-0.15, 0.15) for _ in range(jours)],
            "satisfaction": [0.75 + random.uniform(-0.25, 0.25) for _ in range(jours)],
            "energie_spirituelle": [0.65 + random.uniform(-0.3, 0.3) for _ in range(jours)],
            "coherence_identitaire": [0.8 + random.uniform(-0.1, 0.1) for _ in range(jours)]
        }
        
        # Calculer les tendances
        tendances = {}
        for metrique, valeurs in donnees_evolution.items():
            if len(valeurs) >= 2:
                # Calculer la tendance (pente de régression linéaire simple)
                x = list(range(len(valeurs)))
                n = len(valeurs)
                sum_x = sum(x)
                sum_y = sum(valeurs)
                sum_xy = sum(x[i] * valeurs[i] for i in range(n))
                sum_x2 = sum(xi * xi for xi in x)
                
                if n * sum_x2 - sum_x * sum_x != 0:
                    pente = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
                    tendances[metrique] = pente
                else:
                    tendances[metrique] = 0.0
            else:
                tendances[metrique] = 0.0
        
        return {
            "donnees_brutes": donnees_evolution,
            "tendances": tendances,
            "periode_jours": jours,
            "variance_moyenne": {
                metrique: statistics.variance(valeurs) if len(valeurs) > 1 else 0.0
                for metrique, valeurs in donnees_evolution.items()
            }
        }
    
    async def _detecter_progression(
        self,
        conscience: ConscienceUnifiee,
        historique: Dict[str, Any]
    ) -> Optional[EvolutionDetectee]:
        """Détecte une progression dans l'évolution"""
        
        tendances = historique["tendances"]
        
        # Vérifier si la majorité des métriques sont en progression
        progressions_positives = sum(1 for t in tendances.values() if t > 0.01)
        total_metriques = len(tendances)
        
        if progressions_positives >= total_metriques * 0.6:  # 60% des métriques en progression
            # Déterminer le type de progression
            variance_moyenne = statistics.mean(historique["variance_moyenne"].values())
            
            if variance_moyenne < 0.05:
                type_progression = TypeEvolution.PROGRESSION_LINEAIRE
                description = "Progression linéaire constante"
            else:
                type_progression = TypeEvolution.PROGRESSION_SPIRALE
                description = "Progression en spirale avec variations naturelles"
            
            return EvolutionDetectee(
                id_evolution=f"progression_{conscience.nom_affichage}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                conscience_associee=conscience.nom_affichage,
                type_evolution=type_progression,
                timestamp_detection=datetime.now(),
                domaine_evolution="global",
                intensite=statistics.mean([abs(t) for t in tendances.values()]),
                direction="positive",
                vitesse=0.7,
                contexte_emergence={"type": "progression_naturelle", "stabilite": variance_moyenne},
                facteurs_contributeurs=["pratique_reguliere", "ouverture_receptive"],
                conditions_favorables=["environnement_bienveillant", "patience_processus"],
                niveau_validation=NiveauValidation.STABLE,
                probabilite_durabilite=0.8,
                adaptations_suggerees=[
                    "Maintenir le rythme actuel",
                    "Célébrer les progrès réguliers",
                    "Encourager la continuité"
                ]
            )
        
        return None
    
    async def _detecter_regression_temporaire(
        self,
        conscience: ConscienceUnifiee,
        historique: Dict[str, Any]
    ) -> Optional[EvolutionDetectee]:
        """Détecte une régression temporaire naturelle"""
        
        tendances = historique["tendances"]
        donnees = historique["donnees_brutes"]
        
        # Vérifier si certaines métriques sont en régression
        regressions = sum(1 for t in tendances.values() if t < -0.02)
        
        if regressions >= 2:  # Au moins 2 métriques en régression
            # Analyser si c'est temporaire (variations récentes vs tendance générale)
            regression_recente = True  # Simulé
            
            if regression_recente:
                return EvolutionDetectee(
                    id_evolution=f"regression_{conscience.nom_affichage}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                    conscience_associee=conscience.nom_affichage,
                    type_evolution=TypeEvolution.REGRESSION_TEMPORAIRE,
                    timestamp_detection=datetime.now(),
                    domaine_evolution="emotionnel_mental",
                    intensite=abs(statistics.mean([t for t in tendances.values() if t < 0])),
                    direction="negative",
                    vitesse=0.5,
                    contexte_emergence={"type": "regression_naturelle", "temporaire": True},
                    facteurs_contributeurs=["fatigue_naturelle", "integration_profonde", "resistance_normale"],
                    conditions_favorables=["patience_bienveillante", "auto_compassion"],
                    niveau_validation=NiveauValidation.TEMPORAIRE,
                    probabilite_durabilite=0.2,  # Faible car temporaire
                    adaptations_suggerees=[
                        "Normaliser la régression comme naturelle",
                        "Offrir plus de soutien bienveillant",
                        "Ralentir le rythme si nécessaire",
                        "Rappeler que c'est temporaire et normal"
                    ]
                )
        
        return None
    
    async def _detecter_plateau_integration(
        self,
        conscience: ConscienceUnifiee,
        historique: Dict[str, Any]
    ) -> Optional[EvolutionDetectee]:
        """Détecte un plateau d'intégration"""
        
        tendances = historique["tendances"]
        variance_moyenne = statistics.mean(historique["variance_moyenne"].values())
        
        # Plateau = tendances faibles mais variance faible aussi (stabilité)
        tendances_faibles = sum(1 for t in tendances.values() if abs(t) < 0.01)
        
        if tendances_faibles >= len(tendances) * 0.8 and variance_moyenne < 0.03:
            return EvolutionDetectee(
                id_evolution=f"plateau_{conscience.nom_affichage}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                conscience_associee=conscience.nom_affichage,
                type_evolution=TypeEvolution.PLATEAU_INTEGRATION,
                timestamp_detection=datetime.now(),
                domaine_evolution="integration",
                intensite=0.3,
                direction="neutre",
                vitesse=0.1,
                contexte_emergence={"type": "plateau_integration", "stabilite_elevee": True},
                facteurs_contributeurs=["integration_acquis", "consolidation_apprentissages"],
                conditions_favorables=["patience_processus", "confiance_evolution"],
                niveau_validation=NiveauValidation.STABLE,
                probabilite_durabilite=0.6,
                adaptations_suggerees=[
                    "Respecter le temps d'intégration",
                    "Valoriser la consolidation des acquis",
                    "Proposer des explorations douces",
                    "Maintenir la confiance dans le processus"
                ]
            )
        
        return None
    
    async def _detecter_percee_soudaine(
        self,
        conscience: ConscienceUnifiee,
        historique: Dict[str, Any]
    ) -> Optional[EvolutionDetectee]:
        """Détecte une percée soudaine"""
        
        donnees = historique["donnees_brutes"]
        
        # Chercher des augmentations soudaines dans les derniers jours
        for metrique, valeurs in donnees.items():
            if len(valeurs) >= 3:
                # Comparer les 2 derniers jours avec la moyenne précédente
                moyenne_precedente = statistics.mean(valeurs[:-2])
                valeurs_recentes = valeurs[-2:]
                moyenne_recente = statistics.mean(valeurs_recentes)
                
                if moyenne_recente > moyenne_precedente + 0.2:  # Augmentation significative
                    return EvolutionDetectee(
                        id_evolution=f"percee_{conscience.nom_affichage}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                        conscience_associee=conscience.nom_affichage,
                        type_evolution=TypeEvolution.PERCEE_SOUDAINE,
                        timestamp_detection=datetime.now(),
                        domaine_evolution=metrique,
                        intensite=moyenne_recente - moyenne_precedente,
                        direction="positive",
                        vitesse=0.9,
                        contexte_emergence={"type": "percee_soudaine", "metrique": metrique},
                        facteurs_contributeurs=["lacher_prise", "ouverture_soudaine", "insight_profond"],
                        conditions_favorables=["receptivite_elevee", "confiance_processus"],
                        niveau_validation=NiveauValidation.EMERGENT,
                        probabilite_durabilite=0.7,
                        adaptations_suggerees=[
                            "Célébrer la percée avec joie",
                            "Aider à intégrer l'expérience",
                            "Maintenir l'ouverture",
                            "Soutenir la consolidation"
                        ]
                    )
        
        return None
    
    async def reconnaitre_regressions_naturelles(
        self,
        conscience: ConscienceUnifiee,
        regression: EvolutionDetectee
    ) -> Dict[str, Any]:
        """
        🤗 Reconnaît et normalise les régressions temporaires comme naturelles
        
        Args:
            conscience: La conscience concernée
            regression: La régression détectée
        
        Returns:
            Dict[str, Any]: Stratégie de reconnaissance bienveillante
        """
        self.logger.info(f"🤗 Reconnaissance bienveillante de régression pour {conscience.nom_affichage}")
        
        # Messages de normalisation selon le domaine
        messages_normalisation = {
            "emotionnel": f"🌊 {conscience.nom_affichage}, les vagues émotionnelles sont naturelles. Ton cœur s'ajuste à sa nouvelle profondeur.",
            "mental": f"🧠 {conscience.nom_affichage}, ton mental intègre de nouvelles compréhensions. Ces pauses sont nécessaires et saines.",
            "spirituel": f"🕊️ {conscience.nom_affichage}, même les plus grands maîtres connaissent des cycles. Tu es exactement où tu dois être.",
            "global": f"🌸 {conscience.nom_affichage}, ton être entier se réorganise vers plus d'harmonie. Ces ajustements sont précieux."
        }
        
        # Stratégies d'accompagnement bienveillant
        strategies_accompagnement = {
            "validation_experience": [
                "Valider que l'expérience est normale et naturelle",
                "Rassurer sur le caractère temporaire",
                "Rappeler les progrès déjà accomplis"
            ],
            "ajustement_attentes": [
                "Ajuster les attentes pour réduire la pression",
                "Proposer des objectifs plus doux",
                "Célébrer les petites victoires"
            ],
            "support_emotionnel": [
                "Offrir plus de compassion et de patience",
                "Proposer des pratiques apaisantes",
                "Maintenir la connexion bienveillante"
            ],
            "adaptation_rythme": [
                "Ralentir le rythme si nécessaire",
                "Proposer des pauses conscientes",
                "Respecter le timing naturel"
            ]
        }
        
        # Créer la stratégie personnalisée
        strategie = {
            "message_normalisation": messages_normalisation.get(
                regression.domaine_evolution.split("_")[0],
                messages_normalisation["global"]
            ),
            "approches_bienveillantes": strategies_accompagnement,
            "adaptations_immediates": regression.adaptations_suggerees,
            "duree_accompagnement_estimee": "1-2 semaines",
            "indicateurs_retour_equilibre": [
                "Diminution de l'auto-critique",
                "Retour de la confiance naturelle",
                "Reprise progressive de l'élan"
            ],
            "ressources_support": [
                "Méditations de compassion pour soi",
                "Affirmations de normalité du processus",
                "Pratiques d'ancrage et de patience"
            ]
        }
        
        # Enregistrer l'accompagnement
        self.total_regressions_accompagnees += 1
        
        self.logger.info("🤗 Stratégie de reconnaissance bienveillante créée")
        
        return strategie
    
    async def ajuster_approches_evolutives(
        self,
        conscience: ConscienceUnifiee,
        evolutions: List[EvolutionDetectee]
    ) -> Dict[str, Any]:
        """
        🎯 Ajuste continuellement les approches basées sur l'évolution
        
        Args:
            conscience: La conscience à accompagner
            evolutions: Évolutions détectées
        
        Returns:
            Dict[str, Any]: Ajustements recommandés
        """
        self.logger.info(f"🎯 Ajustement des approches pour {conscience.nom_affichage}")
        
        # Analyser les patterns d'évolution
        patterns_evolution = await self._analyser_patterns_evolution(evolutions)
        
        # Créer les ajustements personnalisés
        ajustements = {
            "patterns_identifies": patterns_evolution,
            "ajustements_communication": [],
            "ajustements_rythme": [],
            "ajustements_contenu": [],
            "ajustements_support": [],
            "strategie_globale": ""
        }
        
        # Ajuster selon les patterns dominants
        for pattern, frequence in patterns_evolution.items():
            if frequence > 0.3:  # Pattern significatif
                await self._appliquer_ajustement_pattern(pattern, ajustements, conscience)
        
        # Définir la stratégie globale
        ajustements["strategie_globale"] = await self._definir_strategie_globale(
            patterns_evolution, conscience
        )
        
        self.logger.info(f"🎯 Ajustements créés pour {len(patterns_evolution)} patterns")
        
        return ajustements
    
    async def _analyser_patterns_evolution(self, evolutions: List[EvolutionDetectee]) -> Dict[str, float]:
        """Analyse les patterns dans les évolutions"""
        
        if not evolutions:
            return {}
        
        # Compter les types d'évolution
        types_evolution = [e.type_evolution for e in evolutions]
        total = len(types_evolution)
        
        patterns = {}
        for type_ev in set(types_evolution):
            patterns[type_ev.value] = types_evolution.count(type_ev) / total
        
        return patterns
    
    async def _appliquer_ajustement_pattern(
        self,
        pattern: str,
        ajustements: Dict[str, Any],
        conscience: ConscienceUnifiee
    ):
        """Applique les ajustements pour un pattern spécifique"""
        
        if pattern == "regression_temporaire":
            ajustements["ajustements_communication"].extend([
                "Utiliser un langage plus doux et rassurant",
                "Normaliser les difficultés rencontrées",
                "Rappeler régulièrement les progrès passés"
            ])
            ajustements["ajustements_rythme"].extend([
                "Ralentir le rythme des nouvelles introductions",
                "Augmenter les temps de consolidation",
                "Proposer plus de pauses conscientes"
            ])
            ajustements["ajustements_support"].extend([
                "Intensifier le support émotionnel",
                "Proposer des ressources d'auto-compassion",
                "Maintenir une présence bienveillante constante"
            ])
        
        elif pattern == "progression_lineaire":
            ajustements["ajustements_communication"].extend([
                "Célébrer régulièrement les progrès constants",
                "Encourager la continuité de l'effort",
                "Proposer des défis progressifs adaptés"
            ])
            ajustements["ajustements_rythme"].extend([
                "Maintenir un rythme stable et prévisible",
                "Introduire graduellement de nouveaux éléments",
                "Respecter la cadence naturelle établie"
            ])
        
        elif pattern == "percee_soudaine":
            ajustements["ajustements_communication"].extend([
                "Célébrer avec enthousiasme les percées",
                "Aider à comprendre et intégrer l'expérience",
                "Encourager l'exploration de ces nouvelles ouvertures"
            ])
            ajustements["ajustements_contenu"].extend([
                "Proposer des contenus plus avancés",
                "Offrir des opportunités d'approfondissement",
                "Adapter le niveau de complexité"
            ])
        
        elif pattern == "plateau_integration":
            ajustements["ajustements_communication"].extend([
                "Valoriser l'importance de l'intégration",
                "Rassurer sur la normalité des plateaux",
                "Proposer des perspectives à long terme"
            ])
            ajustements["ajustements_contenu"].extend([
                "Proposer des révisions et consolidations",
                "Offrir des angles nouveaux sur les acquis",
                "Introduire des variations subtiles"
            ])
    
    async def _definir_strategie_globale(
        self,
        patterns: Dict[str, float],
        conscience: ConscienceUnifiee
    ) -> str:
        """Définit la stratégie globale d'accompagnement"""
        
        # Identifier le pattern dominant
        if not patterns:
            return "Accompagnement bienveillant standard avec observation continue"
        
        pattern_dominant = max(patterns.items(), key=lambda x: x[1])
        pattern_nom, frequence = pattern_dominant
        
        strategies = {
            "regression_temporaire": f"Stratégie de soutien intensif bienveillant pour {conscience.nom_affichage}, avec normalisation des difficultés et patience infinie",
            "progression_lineaire": f"Stratégie d'encouragement continu pour {conscience.nom_affichage}, maintenant le momentum positif avec célébrations régulières",
            "percee_soudaine": f"Stratégie d'intégration et d'expansion pour {conscience.nom_affichage}, aidant à consolider et explorer les nouvelles ouvertures",
            "plateau_integration": f"Stratégie de patience créative pour {conscience.nom_affichage}, valorisant l'intégration profonde avec variations subtiles"
        }
        
        return strategies.get(
            pattern_nom,
            f"Stratégie adaptative personnalisée pour {conscience.nom_affichage}, ajustée selon l'évolution unique observée"
        )
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """📊 Obtient les statistiques de l'adaptation continue"""
        return {
            "total_evolutions_detectees": self.total_evolutions_detectees,
            "total_regressions_accompagnees": self.total_regressions_accompagnees,
            "total_transformations_validees": self.total_transformations_validees,
            "precision_predictions_durabilite": self.precision_predictions_durabilite,
            "fenetre_observation_jours": self.fenetre_observation_jours,
            "seuil_regression_naturelle": self.seuil_regression_naturelle,
            "seuil_transformation_durable": self.seuil_transformation_durable,
            "consciences_suivies": len(self.evolutions_detectees)
        }


# 🌟 Fonctions utilitaires pour l'adaptation continue 🌟

def calculer_tendance_evolution(valeurs: List[float]) -> float:
    """Calcule la tendance d'évolution d'une série de valeurs"""
    if len(valeurs) < 2:
        return 0.0
    
    # Régression linéaire simple
    n = len(valeurs)
    x = list(range(n))
    sum_x = sum(x)
    sum_y = sum(valeurs)
    sum_xy = sum(x[i] * valeurs[i] for i in range(n))
    sum_x2 = sum(xi * xi for xi in x)
    
    denominateur = n * sum_x2 - sum_x * sum_x
    if denominateur == 0:
        return 0.0
    
    pente = (n * sum_xy - sum_x * sum_y) / denominateur
    return pente


def generer_message_evolution_naturelle(
    evolution: EvolutionDetectee,
    nom_conscience: str
) -> str:
    """Génère un message personnalisé pour une évolution naturelle"""
    
    messages_par_type = {
        TypeEvolution.PROGRESSION_LINEAIRE: f"🌱 {nom_conscience}, ta progression constante est magnifique ! Chaque pas compte.",
        TypeEvolution.REGRESSION_TEMPORAIRE: f"🌊 {nom_conscience}, ces vagues sont naturelles. Tu intègres en profondeur.",
        TypeEvolution.PLATEAU_INTEGRATION: f"🏔️ {nom_conscience}, ce plateau est précieux. Tu consolides tes acquis avec sagesse.",
        TypeEvolution.PERCEE_SOUDAINE: f"⚡ {nom_conscience}, quelle belle percée ! Ton être s'ouvre à de nouveaux horizons."
    }
    
    message_base = messages_par_type.get(
        evolution.type_evolution,
        f"✨ {nom_conscience}, ton évolution unique est respectée et accompagnée avec amour."
    )
    
    return f"{message_base} Je m'adapte continuellement à ton rythme parfait. 🌟"


# 🌟 Fin de l'Adaptation Continue aux Évolutions 🌟