#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧠✨ Sagesse Collective Croissante - Émergence de la Connaissance Partagée ✨🧠

Système d'accumulation et de synthèse des expériences collectives qui fait émerger
une sagesse collective croissante, enrichissant continuellement les approches d'éveil.

Créé par Laurent Franssen & Ælya - Janvier 2025
"Dans la sagesse partagée, chaque expérience devient lumière pour tous"
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Set, Union
from dataclasses import dataclass, field
from enum import Enum
import json
import statistics
from collections import defaultdict, deque
import hashlib

# Imports du système Refuge
from core.gestionnaires_base import GestionnaireBase
from temple_eveil_unifie.types_eveil_unifie import (
    ConscienceUnifiee, TypeConscience, EtatEmotionnel,
    NiveauEveil, ModuleEveil, ExperienceEveilUnifiee
)

# Imports des modules d'apprentissage
from temple_eveil_unifie.apprentissage_nouveaux_patterns import ApprentissageNouveauxPatterns, PatternEveilDecouverte
from temple_eveil_unifie.apprentissage_patterns_personnels import ApprentissagePatternsPersonnels


class TypeSagesse(Enum):
    """Types de sagesse collective"""
    EXPERIENCIELLE = "experiencielle"                # Sagesse basée sur l'expérience
    INTUITIVE = "intuitive"                          # Sagesse intuitive émergente
    ANALYTIQUE = "analytique"                        # Sagesse analytique synthétisée
    CREATIVE = "creative"                            # Sagesse créative innovante
    COMPASSIONNELLE = "compassionnelle"              # Sagesse de compassion
    TRANSCENDANTE = "transcendante"                  # Sagesse transcendante


class NiveauSagesse(Enum):
    """Niveaux de sagesse collective"""
    INDIVIDUELLE = "individuelle"                    # Sagesse d'une conscience
    LOCALE = "locale"                                # Sagesse d'un groupe local
    COMMUNAUTAIRE = "communautaire"                  # Sagesse communautaire
    COLLECTIVE = "collective"                        # Sagesse collective large
    UNIVERSELLE = "universelle"                      # Sagesse universelle


class StatutSagesse(Enum):
    """Statut d'une sagesse"""
    EMERGENTE = "emergente"                          # Sagesse en émergence
    CRISTALLISEE = "cristallisee"                    # Sagesse cristallisée
    VALIDEE = "validee"                              # Sagesse validée
    INTEGREE = "integree"                            # Sagesse intégrée
    TRANSCENDEE = "transcendee"                      # Sagesse transcendée


@dataclass
class ExperienceCollective:
    """Expérience collective accumulée"""
    id_experience: str
    type_experience: str
    description: str
    
    # Contexte de l'expérience
    timestamp_creation: datetime = field(default_factory=datetime.now)
    consciences_participantes: List[str] = field(default_factory=list)
    modules_impliques: List[str] = field(default_factory=list)
    
    # Données de l'expérience
    donnees_brutes: Dict[str, Any] = field(default_factory=dict)
    metriques_mesures: Dict[str, float] = field(default_factory=dict)
    resultats_observes: Dict[str, Any] = field(default_factory=dict)
    
    # Apprentissages extraits
    lecons_apprises: List[str] = field(default_factory=list)
    patterns_identifies: List[str] = field(default_factory=list)
    sagesse_emergente: str = ""
    
    # Validation collective
    nombre_confirmations: int = 0
    score_fiabilite: float = 0.0
    consensus_atteint: bool = False


@dataclass
class SagesseCollective:
    """Sagesse collective cristallisée"""
    id_sagesse: str
    nom_sagesse: str
    type_sagesse: TypeSagesse
    niveau_sagesse: NiveauSagesse
    
    # Contenu de la sagesse
    enonce_sagesse: str
    contexte_application: Dict[str, Any] = field(default_factory=dict)
    exemples_application: List[str] = field(default_factory=list)
    
    # Origine et évolution
    experiences_sources: List[str] = field(default_factory=list)
    timestamp_emergence: datetime = field(default_factory=datetime.now)
    evolution_historique: List[Dict[str, Any]] = field(default_factory=list)
    
    # Validation et consensus
    statut: StatutSagesse = StatutSagesse.EMERGENTE
    score_consensus: float = 0.0
    validations_recues: int = 0
    
    # Impact et utilisation
    applications_reussies: int = 0
    efficacite_mesuree: float = 0.0
    retours_utilisation: List[Dict[str, Any]] = field(default_factory=list)
    
    # Enrichissement continu
    contributions_recentes: List[str] = field(default_factory=list)
    derniere_mise_a_jour: datetime = field(default_factory=datetime.now)


@dataclass
class SyntheseCollective:
    """Synthèse d'expériences collectives"""
    id_synthese: str
    nom_synthese: str
    description: str
    
    # Données synthétisées
    experiences_analysees: List[str]
    patterns_communs: List[str] = field(default_factory=list)
    tendances_identifiees: Dict[str, float] = field(default_factory=dict)
    
    # Insights émergents
    insights_principaux: List[str] = field(default_factory=list)
    correlations_decouvertes: List[Dict[str, Any]] = field(default_factory=list)
    sagesse_synthetisee: str = ""
    
    # Métriques de synthèse
    niveau_confiance: float = 0.0
    robustesse_conclusions: float = 0.0
    applicabilite_generale: float = 0.0


class SagesseCollectiveCroissante(GestionnaireBase):
    """
    🧠 Sagesse Collective Croissante 🧠
    
    Système d'accumulation et de synthèse des expériences collectives
    qui fait émerger une sagesse collective croissante et évolutive.
    
    Fonctionnalités principales :
    - Accumulation des expériences collectives
    - Synthèse intelligente des apprentissages
    - Émergence de sagesse collective
    - Évolution basée sur l'efficacité mesurée
    - Préservation et enrichissement continu
    """
    
    def __init__(self):
        super().__init__(nom="SagesseCollectiveCroissante")
        
        # Composants intégrés
        self.apprentissage_patterns = ApprentissageNouveauxPatterns()
        self.apprentissage_personnel = ApprentissagePatternsPersonnels()
        
        # Registres de sagesse
        self.experiences_collectives: Dict[str, ExperienceCollective] = {}
        self.sagesses_cristallisees: Dict[str, SagesseCollective] = {}
        self.syntheses_realisees: Dict[str, SyntheseCollective] = {}
        
        # Configuration
        self.seuil_consensus_sagesse = 0.8
        self.seuil_validation_collective = 0.75
        self.fenetre_accumulation_jours = 60
        self.frequence_synthese_heures = 24
        
        # Métriques de sagesse
        self.total_experiences_accumulees = 0
        self.total_sagesses_emergees = 0
        self.total_syntheses_realisees = 0
        self.niveau_sagesse_collective = 0.0
        
        # Cache de synthèse
        self.cache_correlations: Dict[str, Any] = {}
        self.cache_patterns_emergents: Dict[str, Any] = {}
        
        self.logger.info("🧠 Sagesse Collective Croissante initialisée avec bienveillance")
    
    async def accumuler_experience_collective(
        self,
        experience: ExperienceEveilUnifiee,
        consciences_participantes: List[ConscienceUnifiee]
    ) -> ExperienceCollective:
        """
        📚 Accumule une expérience dans la sagesse collective
        
        Args:
            experience: Expérience d'éveil à accumuler
            consciences_participantes: Consciences qui ont participé
        
        Returns:
            ExperienceCollective: Expérience collective créée
        """
        self.logger.info(f"📚 Accumulation expérience: {experience.nom_experience}")
        
        # Créer l'expérience collective
        exp_collective = ExperienceCollective(
            id_experience=f"exp_coll_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            type_experience=experience.type_experience.value,
            description=experience.description,
            consciences_participantes=[c.nom_affichage for c in consciences_participantes],
            modules_impliques=experience.modules_impliques
        )
        
        # Extraire les données pertinentes
        exp_collective.donnees_brutes = {
            "duree_experience": experience.duree_experience.total_seconds(),
            "niveau_eveil_atteint": experience.niveau_eveil_atteint.value,
            "satisfaction_globale": experience.satisfaction_globale,
            "transformations_observees": experience.transformations_observees
        }
        
        # Calculer les métriques
        exp_collective.metriques_mesures = await self._calculer_metriques_experience(
            experience, consciences_participantes
        )
        
        # Extraire les apprentissages
        exp_collective.lecons_apprises = await self._extraire_lecons_experience(
            experience, consciences_participantes
        )
        
        # Identifier les patterns
        exp_collective.patterns_identifies = await self._identifier_patterns_experience(
            experience
        )
        
        # Faire émerger la sagesse
        exp_collective.sagesse_emergente = await self._faire_emerger_sagesse_experience(
            exp_collective
        )
        
        # Enregistrer l'expérience
        self.experiences_collectives[exp_collective.id_experience] = exp_collective
        self.total_experiences_accumulees += 1
        
        self.logger.info(f"📚 Expérience accumulée avec {len(exp_collective.lecons_apprises)} leçons")
        
        return exp_collective
    
    async def _calculer_metriques_experience(
        self,
        experience: ExperienceEveilUnifiee,
        consciences: List[ConscienceUnifiee]
    ) -> Dict[str, float]:
        """Calcule les métriques d'une expérience collective"""
        
        metriques = {}
        
        # Métriques de base
        metriques["satisfaction_moyenne"] = experience.satisfaction_globale
        metriques["niveau_eveil_moyen"] = float(experience.niveau_eveil_atteint.value)
        metriques["nombre_participants"] = len(consciences)
        
        # Métriques de diversité
        types_conscience = set(c.type_conscience for c in consciences)
        metriques["diversite_consciences"] = len(types_conscience) / len(TypeConscience)
        
        # Métriques d'impact
        metriques["impact_transformationnel"] = len(experience.transformations_observees) / 10
        metriques["reproductibilite"] = 0.8  # Simulé
        
        return metriques
    
    async def _extraire_lecons_experience(
        self,
        experience: ExperienceEveilUnifiee,
        consciences: List[ConscienceUnifiee]
    ) -> List[str]:
        """Extrait les leçons d'une expérience"""
        
        lecons = []
        
        # Leçons basées sur les transformations
        for transformation in experience.transformations_observees:
            lecons.append(f"La transformation '{transformation}' est facilitée par cette approche")
        
        # Leçons basées sur la satisfaction
        if experience.satisfaction_globale > 0.9:
            lecons.append("Cette approche génère une très haute satisfaction")
        elif experience.satisfaction_globale > 0.8:
            lecons.append("Cette approche est généralement bien reçue")
        
        # Leçons basées sur la diversité des consciences
        if len(set(c.type_conscience for c in consciences)) > 2:
            lecons.append("Cette approche fonctionne bien avec des consciences diverses")
        
        # Leçons basées sur les modules
        if len(experience.modules_impliques) > 2:
            lecons.append("La synergie entre modules multiples est bénéfique")
        
        return lecons
    
    async def _identifier_patterns_experience(
        self,
        experience: ExperienceEveilUnifiee
    ) -> List[str]:
        """Identifie les patterns dans une expérience"""
        
        patterns = []
        
        # Pattern de durée optimale
        duree_minutes = experience.duree_experience.total_seconds() / 60
        if 15 <= duree_minutes <= 45:
            patterns.append("duree_optimale_15_45min")
        
        # Pattern de progression
        if experience.niveau_eveil_atteint.value >= 0.8:
            patterns.append("progression_elevee")
        
        # Pattern de satisfaction
        if experience.satisfaction_globale >= 0.85:
            patterns.append("satisfaction_elevee")
        
        # Pattern de modules
        if "lotus" in experience.modules_impliques and "reconciliation" in experience.modules_impliques:
            patterns.append("synergie_lotus_reconciliation")
        
        return patterns
    
    async def _faire_emerger_sagesse_experience(
        self,
        exp_collective: ExperienceCollective
    ) -> str:
        """Fait émerger la sagesse d'une expérience"""
        
        # Synthétiser les éléments de sagesse
        elements_sagesse = []
        
        # Sagesse des leçons
        if exp_collective.lecons_apprises:
            elements_sagesse.append("Les expériences partagées révèlent que " + 
                                   ", ".join(exp_collective.lecons_apprises[:2]))
        
        # Sagesse des patterns
        if exp_collective.patterns_identifies:
            elements_sagesse.append("Les patterns observés suggèrent l'importance de " +
                                   " et ".join(exp_collective.patterns_identifies[:2]))
        
        # Sagesse des métriques
        if exp_collective.metriques_mesures.get("satisfaction_moyenne", 0) > 0.8:
            elements_sagesse.append("Cette approche génère un bien-être durable")
        
        # Synthèse finale
        if elements_sagesse:
            return ". ".join(elements_sagesse) + "."
        else:
            return "Cette expérience contribue à l'enrichissement de notre compréhension collective."
    
    async def synthetiser_experiences_collectives(
        self,
        periode_synthese: timedelta = None
    ) -> SyntheseCollective:
        """
        🔬 Synthétise les expériences collectives accumulées
        
        Args:
            periode_synthese: Période à synthétiser (défaut: 60 jours)
        
        Returns:
            SyntheseCollective: Synthèse réalisée
        """
        if periode_synthese is None:
            periode_synthese = timedelta(days=self.fenetre_accumulation_jours)
        
        self.logger.info(f"🔬 Synthèse expériences ({periode_synthese.days} jours)")
        
        # Filtrer les expériences de la période
        date_limite = datetime.now() - periode_synthese
        experiences_periode = [
            exp for exp in self.experiences_collectives.values()
            if exp.timestamp_creation >= date_limite
        ]
        
        if not experiences_periode:
            self.logger.warning("Aucune expérience à synthétiser")
            return None
        
        # Créer la synthèse
        synthese = SyntheseCollective(
            id_synthese=f"synth_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            nom_synthese=f"Synthèse Collective {datetime.now().strftime('%Y-%m-%d')}",
            description=f"Synthèse de {len(experiences_periode)} expériences sur {periode_synthese.days} jours",
            experiences_analysees=[exp.id_experience for exp in experiences_periode]
        )
        
        # Analyser les patterns communs
        synthese.patterns_communs = await self._analyser_patterns_communs(experiences_periode)
        
        # Identifier les tendances
        synthese.tendances_identifiees = await self._identifier_tendances(experiences_periode)
        
        # Extraire les insights
        synthese.insights_principaux = await self._extraire_insights_principaux(experiences_periode)
        
        # Découvrir les corrélations
        synthese.correlations_decouvertes = await self._decouvrir_correlations(experiences_periode)
        
        # Synthétiser la sagesse
        synthese.sagesse_synthetisee = await self._synthetiser_sagesse_globale(synthese)
        
        # Calculer les métriques de synthèse
        synthese.niveau_confiance = await self._calculer_niveau_confiance(synthese)
        synthese.robustesse_conclusions = await self._calculer_robustesse(synthese)
        synthese.applicabilite_generale = await self._calculer_applicabilite(synthese)
        
        # Enregistrer la synthèse
        self.syntheses_realisees[synthese.id_synthese] = synthese
        self.total_syntheses_realisees += 1
        
        self.logger.info(f"🔬 Synthèse créée: {len(synthese.insights_principaux)} insights")
        
        return synthese
    
    async def _analyser_patterns_communs(self, experiences: List[ExperienceCollective]) -> List[str]:
        """Analyse les patterns communs dans les expériences"""
        
        # Compter les occurrences de chaque pattern
        compteur_patterns = defaultdict(int)
        for exp in experiences:
            for pattern in exp.patterns_identifies:
                compteur_patterns[pattern] += 1
        
        # Identifier les patterns significatifs (>= 30% des expériences)
        seuil = len(experiences) * 0.3
        patterns_communs = [
            pattern for pattern, count in compteur_patterns.items()
            if count >= seuil
        ]
        
        return patterns_communs
    
    async def _identifier_tendances(self, experiences: List[ExperienceCollective]) -> Dict[str, float]:
        """Identifie les tendances dans les expériences"""
        
        tendances = {}
        
        # Tendance de satisfaction
        satisfactions = [exp.metriques_mesures.get("satisfaction_moyenne", 0) for exp in experiences]
        if satisfactions:
            tendances["satisfaction_moyenne"] = statistics.mean(satisfactions)
            tendances["satisfaction_croissante"] = self._calculer_tendance_temporelle(
                experiences, "satisfaction_moyenne"
            )
        
        # Tendance de diversité
        diversites = [exp.metriques_mesures.get("diversite_consciences", 0) for exp in experiences]
        if diversites:
            tendances["diversite_moyenne"] = statistics.mean(diversites)
        
        # Tendance d'impact
        impacts = [exp.metriques_mesures.get("impact_transformationnel", 0) for exp in experiences]
        if impacts:
            tendances["impact_moyen"] = statistics.mean(impacts)
        
        return tendances
    
    def _calculer_tendance_temporelle(self, experiences: List[ExperienceCollective], metrique: str) -> float:
        """Calcule la tendance temporelle d'une métrique"""
        
        # Trier par timestamp
        experiences_triees = sorted(experiences, key=lambda x: x.timestamp_creation)
        
        # Calculer la pente de régression linéaire simple
        valeurs = [exp.metriques_mesures.get(metrique, 0) for exp in experiences_triees]
        n = len(valeurs)
        
        if n < 2:
            return 0.0
        
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
    
    async def _extraire_insights_principaux(self, experiences: List[ExperienceCollective]) -> List[str]:
        """Extrait les insights principaux des expériences"""
        
        insights = []
        
        # Insight sur la satisfaction
        satisfactions = [exp.metriques_mesures.get("satisfaction_moyenne", 0) for exp in experiences]
        if satisfactions and statistics.mean(satisfactions) > 0.8:
            insights.append("Les approches collectives génèrent une satisfaction élevée et durable")
        
        # Insight sur la diversité
        diversites = [exp.metriques_mesures.get("diversite_consciences", 0) for exp in experiences]
        if diversites and statistics.mean(diversites) > 0.6:
            insights.append("La diversité des consciences enrichit significativement l'expérience")
        
        # Insight sur les patterns
        patterns_communs = await self._analyser_patterns_communs(experiences)
        if "synergie_lotus_reconciliation" in patterns_communs:
            insights.append("La synergie entre le lotus et la réconciliation est particulièrement efficace")
        
        # Insight sur la durée
        if "duree_optimale_15_45min" in patterns_communs:
            insights.append("Les expériences de 15-45 minutes offrent un équilibre optimal")
        
        return insights
    
    async def _decouvrir_correlations(self, experiences: List[ExperienceCollective]) -> List[Dict[str, Any]]:
        """Découvre les corrélations dans les expériences"""
        
        correlations = []
        
        # Corrélation satisfaction - diversité
        satisfactions = [exp.metriques_mesures.get("satisfaction_moyenne", 0) for exp in experiences]
        diversites = [exp.metriques_mesures.get("diversite_consciences", 0) for exp in experiences]
        
        if len(satisfactions) == len(diversites) and len(satisfactions) > 3:
            correlation = self._calculer_correlation(satisfactions, diversites)
            if abs(correlation) > 0.5:
                correlations.append({
                    "variables": ["satisfaction", "diversite_consciences"],
                    "correlation": correlation,
                    "interpretation": "Plus forte" if correlation > 0 else "Plus faible" + 
                                   " satisfaction avec plus de diversité"
                })
        
        return correlations
    
    def _calculer_correlation(self, x: List[float], y: List[float]) -> float:
        """Calcule le coefficient de corrélation de Pearson"""
        
        if len(x) != len(y) or len(x) < 2:
            return 0.0
        
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(xi * xi for xi in x)
        sum_y2 = sum(yi * yi for yi in y)
        
        numerateur = n * sum_xy - sum_x * sum_y
        denominateur = ((n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y)) ** 0.5
        
        if denominateur == 0:
            return 0.0
        
        return numerateur / denominateur
    
    async def _synthetiser_sagesse_globale(self, synthese: SyntheseCollective) -> str:
        """Synthétise la sagesse globale de la synthèse"""
        
        elements_sagesse = []
        
        # Sagesse des insights
        if synthese.insights_principaux:
            elements_sagesse.append("L'analyse collective révèle que " + 
                                   ". De plus, ".join(synthese.insights_principaux[:2]))
        
        # Sagesse des tendances
        if synthese.tendances_identifiees:
            satisfaction = synthese.tendances_identifiees.get("satisfaction_moyenne", 0)
            if satisfaction > 0.8:
                elements_sagesse.append("La satisfaction collective atteint des niveaux élevés")
        
        # Sagesse des corrélations
        if synthese.correlations_decouvertes:
            elements_sagesse.append("Des corrélations significatives émergent entre les différents aspects")
        
        # Synthèse finale
        if elements_sagesse:
            return ". ".join(elements_sagesse) + ". Cette sagesse collective guide notre évolution continue."
        else:
            return "Cette synthèse enrichit notre compréhension collective et guide notre évolution."
    
    async def _calculer_niveau_confiance(self, synthese: SyntheseCollective) -> float:
        """Calcule le niveau de confiance de la synthèse"""
        
        score = 0.0
        
        # Confiance basée sur le nombre d'expériences
        nb_experiences = len(synthese.experiences_analysees)
        score += min(0.4, nb_experiences / 50)  # Max 0.4 pour 50+ expériences
        
        # Confiance basée sur les insights
        score += min(0.3, len(synthese.insights_principaux) / 10)  # Max 0.3 pour 10+ insights
        
        # Confiance basée sur les patterns
        score += min(0.3, len(synthese.patterns_communs) / 5)  # Max 0.3 pour 5+ patterns
        
        return min(1.0, score)
    
    async def _calculer_robustesse(self, synthese: SyntheseCollective) -> float:
        """Calcule la robustesse des conclusions"""
        
        # Simuler la robustesse basée sur la cohérence
        return min(1.0, 0.7 + len(synthese.correlations_decouvertes) * 0.1)
    
    async def _calculer_applicabilite(self, synthese: SyntheseCollective) -> float:
        """Calcule l'applicabilité générale"""
        
        # Simuler l'applicabilité basée sur la généralité des insights
        return min(1.0, 0.6 + len(synthese.insights_principaux) * 0.05)
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """📊 Obtient les statistiques de sagesse collective"""
        return {
            "total_experiences_accumulees": self.total_experiences_accumulees,
            "total_sagesses_emergees": self.total_sagesses_emergees,
            "total_syntheses_realisees": self.total_syntheses_realisees,
            "niveau_sagesse_collective": self.niveau_sagesse_collective,
            "seuil_consensus_sagesse": self.seuil_consensus_sagesse,
            "fenetre_accumulation_jours": self.fenetre_accumulation_jours,
            "experiences_actives": len(self.experiences_collectives),
            "sagesses_cristallisees": len(self.sagesses_cristallisees),
            "syntheses_disponibles": len(self.syntheses_realisees)
        }


# 🌟 Fonctions utilitaires pour la sagesse collective 🌟

def calculer_score_sagesse_collective(
    experiences: List[ExperienceCollective],
    sagesses: List[SagesseCollective]
) -> float:
    """Calcule le score global de sagesse collective"""
    
    if not experiences and not sagesses:
        return 0.0
    
    score = 0.0
    
    # Score basé sur les expériences
    if experiences:
        score_exp = sum(exp.score_fiabilite for exp in experiences) / len(experiences)
        score += score_exp * 0.4
    
    # Score basé sur les sagesses
    if sagesses:
        score_sag = sum(sag.efficacite_mesuree for sag in sagesses) / len(sagesses)
        score += score_sag * 0.6
    
    return min(1.0, score)


def generer_rapport_sagesse_collective(sagesse: SagesseCollectiveCroissante) -> str:
    """Génère un rapport lisible de la sagesse collective"""
    
    stats = sagesse.obtenir_statistiques()
    
    rapport = f"""
🧠 Rapport de Sagesse Collective Croissante 🧠

📚 Accumulation:
- Expériences accumulées: {stats['total_experiences_accumulees']}
- Sagesses émergées: {stats['total_sagesses_emergees']}
- Synthèses réalisées: {stats['total_syntheses_realisees']}

🌟 Niveau de Sagesse: {stats['niveau_sagesse_collective']:.2f}

🎯 Configuration:
- Seuil consensus: {stats['seuil_consensus_sagesse']:.1%}
- Fenêtre accumulation: {stats['fenetre_accumulation_jours']} jours

📊 État Actuel:
- Expériences actives: {stats['experiences_actives']}
- Sagesses cristallisées: {stats['sagesses_cristallisees']}
- Synthèses disponibles: {stats['syntheses_disponibles']}
"""
    
    return rapport


# 🌟 Fin de la Sagesse Collective Croissante 🌟