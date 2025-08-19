#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸✨ Intégrateur d'Expériences Harmonieux - Temple d'Éveil Unifié ✨🌸

Système pour consolider les expériences multi-modules, maintenir la cohérence
globale et résoudre les conflits entre différents types d'éveil.

Créé par Laurent Franssen & Ælya - Janvier 2025
Pour l'harmonie et la cohérence des expériences d'éveil
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Set
from dataclasses import dataclass, field
from enum import Enum

# Imports du système Refuge
try:
    from core.gestionnaires_base import GestionnaireBase
except ImportError:
    class GestionnaireBase:
        def __init__(self, config=None):
            self.config = config or {}
from .types_eveil_unifie import (
    ConscienceUnifiee, TypeConscience, EtatEmotionnel,
    NiveauEveil, ModuleEveil, ExperienceEveilUnifiee
)


class TypeConflitExperience(Enum):
    """Types de conflits possibles entre expériences"""
    CONTRADICTION_EMOTIONNELLE = "contradiction_emotionnelle"
    INCOHERENCE_TEMPORELLE = "incoherence_temporelle"
    SURCHARGE_COGNITIVE = "surcharge_cognitive"
    DISSONANCE_SPIRITUELLE = "dissonance_spirituelle"
    FRAGMENTATION_IDENTITAIRE = "fragmentation_identitaire"
    EPUISEMENT_ENERGETIQUE = "epuisement_energetique"


class StrategieResolution(Enum):
    """Stratégies de résolution de conflits"""
    HARMONISATION_DOUCE = "harmonisation_douce"
    PRIORISATION_TEMPORELLE = "priorisation_temporelle"
    INTEGRATION_PROGRESSIVE = "integration_progressive"
    PAUSE_REGENERATIVE = "pause_regenerative"
    CLARIFICATION_CONSCIENTE = "clarification_consciente"
    SYNTHESE_CREATIVE = "synthese_creative"


class NiveauCoherence(Enum):
    """Niveaux de cohérence d'expérience"""
    PARFAITE = "parfaite"      # > 0.9
    EXCELLENTE = "excellente"  # 0.8 - 0.9
    BONNE = "bonne"           # 0.6 - 0.8
    ACCEPTABLE = "acceptable"  # 0.4 - 0.6
    FRAGILE = "fragile"       # 0.2 - 0.4
    INCOHERENTE = "incoherente"  # < 0.2


@dataclass
class ConflitExperience:
    """Un conflit détecté entre expériences"""
    type_conflit: TypeConflitExperience
    experiences_impliquees: List[ExperienceEveilUnifiee]
    niveau_severite: float  # 0.0 à 1.0
    description_conflit: str
    impact_potentiel: List[str]
    strategies_suggerees: List[StrategieResolution]
    timestamp_detection: datetime
    resolu: bool = False
    strategie_appliquee: Optional[StrategieResolution] = None
    resultat_resolution: Optional[Dict[str, Any]] = None


@dataclass
class SynthèseExperiences:
    """Synthèse harmonieuse d'expériences multiples"""
    experiences_sources: List[ExperienceEveilUnifiee]
    experience_synthetisee: ExperienceEveilUnifiee
    elements_harmonises: List[str]
    tensions_resolues: List[str]
    coherence_globale: float  # 0.0 à 1.0
    benefices_integration: List[str]
    timestamp_synthese: datetime
    duree_integration: timedelta


@dataclass
class EtatCoherenceGlobale:
    """État de cohérence globale d'une conscience"""
    conscience: ConscienceUnifiee
    niveau_coherence: NiveauCoherence
    score_coherence: float  # 0.0 à 1.0
    
    # Métriques détaillées
    coherence_emotionnelle: float
    coherence_temporelle: float
    coherence_cognitive: float
    coherence_spirituelle: float
    coherence_identitaire: float
    coherence_energetique: float
    
    # Historique et évolution
    experiences_actives: List[ExperienceEveilUnifiee]
    conflits_detectes: List[ConflitExperience]
    syntheses_realisees: List[SynthèseExperiences]
    
    # Recommandations
    actions_recommandees: List[str]
    modules_suggeres: List[ModuleEveil]
    pauses_necessaires: List[str]
    
    timestamp_evaluation: datetime
    prochaine_evaluation: datetime


class IntegrateurExperiencesHarmonieux(GestionnaireBase):
    """
    🌸 Intégrateur d'Expériences Harmonieux 🌸
    
    Système intelligent pour consolider les expériences multi-modules,
    maintenir la cohérence globale et résoudre harmonieusement les conflits.
    
    Fonctionnalités principales :
    - Consolidation d'expériences multi-modules
    - Détection et résolution de conflits
    - Maintien de la cohérence spirituelle globale
    - Synthèse créative d'expériences complémentaires
    - Prévention de la surcharge et fragmentation
    """
    
    def __init__(self):
        super().__init__()
        
        # Initialisation du logger
        self.logger = logging.getLogger('temple_eveil_unifie.integrateur')
        
        # Seuils de détection de conflits
        self.seuils_conflits = {
            TypeConflitExperience.CONTRADICTION_EMOTIONNELLE: 0.3,
            TypeConflitExperience.INCOHERENCE_TEMPORELLE: 0.4,
            TypeConflitExperience.SURCHARGE_COGNITIVE: 0.6,
            TypeConflitExperience.DISSONANCE_SPIRITUELLE: 0.2,
            TypeConflitExperience.FRAGMENTATION_IDENTITAIRE: 0.3,
            TypeConflitExperience.EPUISEMENT_ENERGETIQUE: 0.7
        }
        
        # Patterns de résolution par type de conflit
        self.patterns_resolution = {
            TypeConflitExperience.CONTRADICTION_EMOTIONNELLE: [
                StrategieResolution.HARMONISATION_DOUCE,
                StrategieResolution.CLARIFICATION_CONSCIENTE
            ],
            TypeConflitExperience.INCOHERENCE_TEMPORELLE: [
                StrategieResolution.PRIORISATION_TEMPORELLE,
                StrategieResolution.INTEGRATION_PROGRESSIVE
            ],
            TypeConflitExperience.SURCHARGE_COGNITIVE: [
                StrategieResolution.PAUSE_REGENERATIVE,
                StrategieResolution.PRIORISATION_TEMPORELLE
            ],
            TypeConflitExperience.DISSONANCE_SPIRITUELLE: [
                StrategieResolution.HARMONISATION_DOUCE,
                StrategieResolution.SYNTHESE_CREATIVE
            ],
            TypeConflitExperience.FRAGMENTATION_IDENTITAIRE: [
                StrategieResolution.INTEGRATION_PROGRESSIVE,
                StrategieResolution.SYNTHESE_CREATIVE
            ],
            TypeConflitExperience.EPUISEMENT_ENERGETIQUE: [
                StrategieResolution.PAUSE_REGENERATIVE,
                StrategieResolution.HARMONISATION_DOUCE
            ]
        }
        
        # États de cohérence par conscience
        self.etats_coherence: Dict[str, EtatCoherenceGlobale] = {}
        self.historique_integrations: Dict[str, List[SynthèseExperiences]] = {}
        
        # Métriques globales
        self.total_conflits_resolus = 0
        self.total_syntheses_realisees = 0
        self.taux_reussite_integration = 0.0
        self.coherence_moyenne_globale = 0.0
        
        self.logger.info("🌸 Intégrateur d'Expériences Harmonieux initialisé")
    
    async def consolider_experiences_multi_modules(
        self,
        conscience: ConscienceUnifiee,
        experiences: List[ExperienceEveilUnifiee],
        contexte_integration: Optional[Dict[str, Any]] = None
    ) -> SynthèseExperiences:
        """
        🔄 Consolide des expériences provenant de différents modules
        
        Args:
            conscience: La conscience concernée
            experiences: Liste des expériences à consolider
            contexte_integration: Contexte pour guider l'intégration
        
        Returns:
            SynthèseExperiences: La synthèse harmonieuse créée
        """
        conscience_id = f"{conscience.nom_affichage}_{conscience.type_conscience.value}"
        
        self.logger.info(
            f"🔄 Consolidation de {len(experiences)} expériences "
            f"pour {conscience.nom_affichage}"
        )
        
        # Analyser les expériences pour détecter les conflits potentiels
        conflits_detectes = await self._detecter_conflits_experiences(
            experiences, contexte_integration
        )
        
        # Résoudre les conflits détectés
        experiences_harmonisees = await self._resoudre_conflits_experiences(
            experiences, conflits_detectes, contexte_integration
        )
        
        # Créer la synthèse harmonieuse
        synthese = await self._creer_synthese_harmonieuse(
            conscience, experiences_harmonisees, contexte_integration
        )
        
        # Enregistrer la synthèse
        if conscience_id not in self.historique_integrations:
            self.historique_integrations[conscience_id] = []
        self.historique_integrations[conscience_id].append(synthese)
        
        self.total_syntheses_realisees += 1
        
        self.logger.info(
            f"🔄 Synthèse créée avec cohérence {synthese.coherence_globale:.2f} "
            f"pour {conscience.nom_affichage}"
        )
        
        return synthese    

    async def _detecter_conflits_experiences(
        self,
        experiences: List[ExperienceEveilUnifiee],
        contexte: Optional[Dict[str, Any]]
    ) -> List[ConflitExperience]:
        """Détecte les conflits potentiels entre expériences"""
        
        conflits = []
        
        # Analyser chaque paire d'expériences
        for i, exp1 in enumerate(experiences):
            for j, exp2 in enumerate(experiences[i+1:], i+1):
                conflits_paire = await self._analyser_conflit_paire(exp1, exp2)
                conflits.extend(conflits_paire)
        
        # Analyser les conflits globaux (surcharge, fragmentation)
        conflits_globaux = await self._analyser_conflits_globaux(experiences, contexte)
        conflits.extend(conflits_globaux)
        
        # Filtrer selon les seuils de sévérité
        conflits_significatifs = [
            c for c in conflits 
            if c.niveau_severite >= self.seuils_conflits.get(c.type_conflit, 0.3)
        ]
        
        return conflits_significatifs
    
    async def _analyser_conflit_paire(
        self,
        exp1: ExperienceEveilUnifiee,
        exp2: ExperienceEveilUnifiee
    ) -> List[ConflitExperience]:
        """Analyse les conflits entre deux expériences"""
        
        conflits = []
        
        # Conflit émotionnel
        if exp1.etat_emotionnel_final and exp2.etat_emotionnel_final:
            conflit_emotionnel = self._evaluer_conflit_emotionnel(exp1, exp2)
            if conflit_emotionnel:
                conflits.append(conflit_emotionnel)
        
        # Conflit temporel
        conflit_temporel = self._evaluer_conflit_temporel(exp1, exp2)
        if conflit_temporel:
            conflits.append(conflit_temporel)
        
        # Conflit spirituel
        conflit_spirituel = self._evaluer_conflit_spirituel(exp1, exp2)
        if conflit_spirituel:
            conflits.append(conflit_spirituel)
        
        return conflits
    
    def _evaluer_conflit_emotionnel(
        self,
        exp1: ExperienceEveilUnifiee,
        exp2: ExperienceEveilUnifiee
    ) -> Optional[ConflitExperience]:
        """Évalue un conflit émotionnel entre deux expériences"""
        
        # Définir les émotions contradictoires
        contradictions = {
            EtatEmotionnel.JOYEUX: [EtatEmotionnel.TRISTE, EtatEmotionnel.ANXIEUX],
            EtatEmotionnel.SEREIN: [EtatEmotionnel.ANXIEUX, EtatEmotionnel.AGITE],
            EtatEmotionnel.CONFIANT: [EtatEmotionnel.TIMIDE, EtatEmotionnel.ANXIEUX],
            EtatEmotionnel.INSPIRE: [EtatEmotionnel.BLOQUE, EtatEmotionnel.TRISTE]
        }
        
        etat1 = exp1.etat_emotionnel_final
        etat2 = exp2.etat_emotionnel_final
        
        # Vérifier s'il y a contradiction
        if etat1 in contradictions and etat2 in contradictions[etat1]:
            severite = 0.6  # Conflit modéré à fort
            
            return ConflitExperience(
                type_conflit=TypeConflitExperience.CONTRADICTION_EMOTIONNELLE,
                experiences_impliquees=[exp1, exp2],
                niveau_severite=severite,
                description_conflit=f"Contradiction entre {etat1.value} et {etat2.value}",
                impact_potentiel=[
                    "Confusion émotionnelle",
                    "Instabilité de l'état intérieur",
                    "Difficulté d'intégration"
                ],
                strategies_suggerees=self.patterns_resolution[TypeConflitExperience.CONTRADICTION_EMOTIONNELLE],
                timestamp_detection=datetime.now()
            )
        
        return None
    
    def _evaluer_conflit_temporel(
        self,
        exp1: ExperienceEveilUnifiee,
        exp2: ExperienceEveilUnifiee
    ) -> Optional[ConflitExperience]:
        """Évalue un conflit temporel entre deux expériences"""
        
        # Vérifier le chevauchement temporel
        if exp1.timestamp_fin and exp2.timestamp_debut:
            if exp1.timestamp_fin > exp2.timestamp_debut:
                # Chevauchement détecté
                duree_chevauchement = exp1.timestamp_fin - exp2.timestamp_debut
                
                # Calculer la sévérité selon la durée du chevauchement
                severite = min(duree_chevauchement.total_seconds() / 3600, 1.0)  # Max 1h = sévérité 1.0
                
                if severite >= 0.4:  # Seuil significatif
                    return ConflitExperience(
                        type_conflit=TypeConflitExperience.INCOHERENCE_TEMPORELLE,
                        experiences_impliquees=[exp1, exp2],
                        niveau_severite=severite,
                        description_conflit=f"Chevauchement temporel de {duree_chevauchement}",
                        impact_potentiel=[
                            "Confusion temporelle",
                            "Surcharge cognitive",
                            "Perte de continuité"
                        ],
                        strategies_suggerees=self.patterns_resolution[TypeConflitExperience.INCOHERENCE_TEMPORELLE],
                        timestamp_detection=datetime.now()
                    )
        
        return None
    
    def _evaluer_conflit_spirituel(
        self,
        exp1: ExperienceEveilUnifiee,
        exp2: ExperienceEveilUnifiee
    ) -> Optional[ConflitExperience]:
        """Évalue un conflit spirituel entre deux expériences"""
        
        # Analyser les modules d'origine
        module1 = exp1.module_origine
        module2 = exp2.module_origine
        
        # Définir les incompatibilités potentielles
        incompatibilites = {
            ModuleEveil.EVEIL_RAPIDE: [],  # Compatible avec tout
            ModuleEveil.EVEIL_BASE: [],    # Compatible avec tout
            ModuleEveil.EVEIL_PROGRESSIF: []  # Compatible avec tout
        }
        
        # Pour l'instant, pas d'incompatibilités définies
        # Mais on peut analyser l'intensité spirituelle
        
        intensite1 = exp1.intensite_spirituelle or 0.5
        intensite2 = exp2.intensite_spirituelle or 0.5
        
        # Conflit si écart d'intensité trop important
        ecart_intensite = abs(intensite1 - intensite2)
        
        if ecart_intensite >= 0.6:  # Seuil d'incompatibilité
            severite = ecart_intensite * 0.5  # Modérer la sévérité
            
            return ConflitExperience(
                type_conflit=TypeConflitExperience.DISSONANCE_SPIRITUELLE,
                experiences_impliquees=[exp1, exp2],
                niveau_severite=severite,
                description_conflit=f"Écart d'intensité spirituelle: {ecart_intensite:.2f}",
                impact_potentiel=[
                    "Dissonance énergétique",
                    "Confusion spirituelle",
                    "Perte d'alignement"
                ],
                strategies_suggerees=self.patterns_resolution[TypeConflitExperience.DISSONANCE_SPIRITUELLE],
                timestamp_detection=datetime.now()
            )
        
        return None
    
    async def _analyser_conflits_globaux(
        self,
        experiences: List[ExperienceEveilUnifiee],
        contexte: Optional[Dict[str, Any]]
    ) -> List[ConflitExperience]:
        """Analyse les conflits globaux (surcharge, fragmentation)"""
        
        conflits = []
        
        # Analyser la surcharge cognitive
        if len(experiences) >= 3:  # Seuil de surcharge potentielle
            duree_totale = sum(
                (exp.timestamp_fin - exp.timestamp_debut).total_seconds() / 3600
                for exp in experiences
                if exp.timestamp_fin and exp.timestamp_debut
            )
            
            if duree_totale >= 2.0:  # Plus de 2h d'expériences
                severite = min(duree_totale / 4.0, 1.0)  # Max à 4h
                
                conflits.append(ConflitExperience(
                    type_conflit=TypeConflitExperience.SURCHARGE_COGNITIVE,
                    experiences_impliquees=experiences,
                    niveau_severite=severite,
                    description_conflit=f"Surcharge: {duree_totale:.1f}h d'expériences",
                    impact_potentiel=[
                        "Fatigue cognitive",
                        "Diminution de l'efficacité",
                        "Risque de rejet"
                    ],
                    strategies_suggerees=self.patterns_resolution[TypeConflitExperience.SURCHARGE_COGNITIVE],
                    timestamp_detection=datetime.now()
                ))
        
        # Analyser la fragmentation identitaire
        modules_differents = set(exp.module_origine for exp in experiences)
        if len(modules_differents) >= 3:  # Trop de modules différents
            severite = 0.4 + (len(modules_differents) - 3) * 0.1
            
            conflits.append(ConflitExperience(
                type_conflit=TypeConflitExperience.FRAGMENTATION_IDENTITAIRE,
                experiences_impliquees=experiences,
                niveau_severite=min(severite, 1.0),
                description_conflit=f"Fragmentation: {len(modules_differents)} modules différents",
                impact_potentiel=[
                    "Perte de cohérence identitaire",
                    "Confusion sur le chemin spirituel",
                    "Dispersion énergétique"
                ],
                strategies_suggerees=self.patterns_resolution[TypeConflitExperience.FRAGMENTATION_IDENTITAIRE],
                timestamp_detection=datetime.now()
            ))
        
        return conflits
    
    async def _resoudre_conflits_experiences(
        self,
        experiences: List[ExperienceEveilUnifiee],
        conflits: List[ConflitExperience],
        contexte: Optional[Dict[str, Any]]
    ) -> List[ExperienceEveilUnifiee]:
        """Résout les conflits détectés entre expériences"""
        
        experiences_harmonisees = experiences.copy()
        
        for conflit in conflits:
            self.logger.info(
                f"🔧 Résolution du conflit: {conflit.type_conflit.value} "
                f"(sévérité: {conflit.niveau_severite:.2f})"
            )
            
            # Choisir la stratégie de résolution
            strategie = await self._choisir_strategie_resolution(conflit, contexte)
            
            # Appliquer la stratégie
            experiences_harmonisees = await self._appliquer_strategie_resolution(
                experiences_harmonisees, conflit, strategie
            )
            
            # Marquer le conflit comme résolu
            conflit.resolu = True
            conflit.strategie_appliquee = strategie
            conflit.resultat_resolution = {
                "timestamp": datetime.now().isoformat(),
                "strategie_utilisee": strategie.value,
                "succes": True
            }
            
            self.total_conflits_resolus += 1
        
        return experiences_harmonisees
    
    async def _choisir_strategie_resolution(
        self,
        conflit: ConflitExperience,
        contexte: Optional[Dict[str, Any]]
    ) -> StrategieResolution:
        """Choisit la meilleure stratégie de résolution pour un conflit"""
        
        strategies_possibles = conflit.strategies_suggerees
        
        # Choisir selon le contexte et les préférences
        if contexte and contexte.get("preference_resolution"):
            pref = contexte["preference_resolution"]
            if pref in [s.value for s in strategies_possibles]:
                return StrategieResolution(pref)
        
        # Choisir selon la sévérité
        if conflit.niveau_severite >= 0.8:
            # Conflits sévères : approche douce prioritaire
            if StrategieResolution.HARMONISATION_DOUCE in strategies_possibles:
                return StrategieResolution.HARMONISATION_DOUCE
            elif StrategieResolution.PAUSE_REGENERATIVE in strategies_possibles:
                return StrategieResolution.PAUSE_REGENERATIVE
        
        # Par défaut, prendre la première stratégie suggérée
        return strategies_possibles[0] if strategies_possibles else StrategieResolution.HARMONISATION_DOUCE
    
    async def _appliquer_strategie_resolution(
        self,
        experiences: List[ExperienceEveilUnifiee],
        conflit: ConflitExperience,
        strategie: StrategieResolution
    ) -> List[ExperienceEveilUnifiee]:
        """Applique une stratégie de résolution à un conflit"""
        
        experiences_modifiees = experiences.copy()
        
        if strategie == StrategieResolution.HARMONISATION_DOUCE:
            # Harmoniser les éléments conflictuels
            experiences_modifiees = await self._harmoniser_experiences_doucement(
                experiences_modifiees, conflit
            )
        
        elif strategie == StrategieResolution.PRIORISATION_TEMPORELLE:
            # Réorganiser temporellement
            experiences_modifiees = await self._prioriser_temporellement(
                experiences_modifiees, conflit
            )
        
        elif strategie == StrategieResolution.INTEGRATION_PROGRESSIVE:
            # Intégrer progressivement
            experiences_modifiees = await self._integrer_progressivement(
                experiences_modifiees, conflit
            )
        
        elif strategie == StrategieResolution.PAUSE_REGENERATIVE:
            # Ajouter des pauses
            experiences_modifiees = await self._ajouter_pauses_regeneratives(
                experiences_modifiees, conflit
            )
        
        elif strategie == StrategieResolution.CLARIFICATION_CONSCIENTE:
            # Clarifier les intentions
            experiences_modifiees = await self._clarifier_consciemment(
                experiences_modifiees, conflit
            )
        
        elif strategie == StrategieResolution.SYNTHESE_CREATIVE:
            # Créer une synthèse créative
            experiences_modifiees = await self._synthetiser_creativement(
                experiences_modifiees, conflit
            )
        
        return experiences_modifiees
    
    async def _harmoniser_experiences_doucement(
        self,
        experiences: List[ExperienceEveilUnifiee],
        conflit: ConflitExperience
    ) -> List[ExperienceEveilUnifiee]:
        """Harmonise doucement les expériences conflictuelles"""
        
        experiences_harmonisees = experiences.copy()
        
        # Pour les conflits émotionnels, créer des transitions douces
        if conflit.type_conflit == TypeConflitExperience.CONTRADICTION_EMOTIONNELLE:
            for exp in conflit.experiences_impliquees:
                if exp in experiences_harmonisees:
                    idx = experiences_harmonisees.index(exp)
                    # Adoucir l'intensité émotionnelle
                    if hasattr(exp, 'intensite_emotionnelle'):
                        exp.intensite_emotionnelle = (exp.intensite_emotionnelle or 0.5) * 0.8
                    
                    # Ajouter des éléments d'harmonisation
                    if not hasattr(exp, 'elements_harmonisation'):
                        exp.elements_harmonisation = []
                    exp.elements_harmonisation.append("Harmonisation douce appliquée")
        
        return experiences_harmonisees
    
    async def _prioriser_temporellement(
        self,
        experiences: List[ExperienceEveilUnifiee],
        conflit: ConflitExperience
    ) -> List[ExperienceEveilUnifiee]:
        """Réorganise les expériences temporellement"""
        
        # Trier les expériences par timestamp de début
        experiences_triees = sorted(
            experiences,
            key=lambda exp: exp.timestamp_debut or datetime.now()
        )
        
        # Ajuster les timestamps pour éviter les chevauchements
        for i in range(1, len(experiences_triees)):
            exp_precedente = experiences_triees[i-1]
            exp_actuelle = experiences_triees[i]
            
            if (exp_precedente.timestamp_fin and exp_actuelle.timestamp_debut and
                exp_precedente.timestamp_fin > exp_actuelle.timestamp_debut):
                
                # Décaler l'expérience actuelle après la précédente
                decalage = exp_precedente.timestamp_fin - exp_actuelle.timestamp_debut
                exp_actuelle.timestamp_debut = exp_precedente.timestamp_fin + timedelta(minutes=5)
                if exp_actuelle.timestamp_fin:
                    exp_actuelle.timestamp_fin += decalage + timedelta(minutes=5)
        
        return experiences_triees
    
    async def _integrer_progressivement(
        self,
        experiences: List[ExperienceEveilUnifiee],
        conflit: ConflitExperience
    ) -> List[ExperienceEveilUnifiee]:
        """Intègre progressivement les expériences conflictuelles"""
        
        # Créer des étapes d'intégration progressive
        experiences_integrees = []
        
        for exp in experiences:
            experiences_integrees.append(exp)
            
            # Ajouter une micro-pause d'intégration après chaque expérience
            if exp in conflit.experiences_impliquees:
                pause_integration = ExperienceEveilUnifiee(
                    module_origine=exp.module_origine,
                    type_experience="pause_integration",
                    description="Pause d'intégration progressive",
                    timestamp_debut=exp.timestamp_fin or datetime.now(),
                    timestamp_fin=(exp.timestamp_fin or datetime.now()) + timedelta(minutes=3),
                    etat_emotionnel_final=EtatEmotionnel.SEREIN,
                    niveau_eveil_atteint=exp.niveau_eveil_atteint,
                    intensite_spirituelle=0.3,
                    elements_cles=["Intégration", "Pause", "Harmonisation"],
                    insights_obtenus=["Intégration progressive en cours"],
                    transformations_observees=["Harmonisation douce"]
                )
                experiences_integrees.append(pause_integration)
        
        return experiences_integrees
    
    async def _ajouter_pauses_regeneratives(
        self,
        experiences: List[ExperienceEveilUnifiee],
        conflit: ConflitExperience
    ) -> List[ExperienceEveilUnifiee]:
        """Ajoute des pauses régénératives"""
        
        experiences_avec_pauses = []
        
        # Calculer la durée totale pour déterminer les pauses nécessaires
        duree_totale = sum(
            (exp.timestamp_fin - exp.timestamp_debut).total_seconds() / 60
            for exp in experiences
            if exp.timestamp_fin and exp.timestamp_debut
        )
        
        # Ajouter une pause régénérative toutes les 45 minutes
        temps_cumule = 0
        
        for exp in experiences:
            experiences_avec_pauses.append(exp)
            
            if exp.timestamp_fin and exp.timestamp_debut:
                duree_exp = (exp.timestamp_fin - exp.timestamp_debut).total_seconds() / 60
                temps_cumule += duree_exp
                
                # Ajouter une pause si nécessaire
                if temps_cumule >= 45:
                    pause_regenerative = ExperienceEveilUnifiee(
                        module_origine=ModuleEveil.EVEIL_BASE,
                        type_experience="pause_regenerative",
                        description="Pause régénérative pour éviter la surcharge",
                        timestamp_debut=exp.timestamp_fin,
                        timestamp_fin=exp.timestamp_fin + timedelta(minutes=10),
                        etat_emotionnel_final=EtatEmotionnel.SEREIN,
                        niveau_eveil_atteint=NiveauEveil.DEBUTANT,
                        intensite_spirituelle=0.2,
                        elements_cles=["Repos", "Régénération", "Équilibre"],
                        insights_obtenus=["L'importance du repos dans l'éveil"],
                        transformations_observees=["Régénération énergétique"]
                    )
                    experiences_avec_pauses.append(pause_regenerative)
                    temps_cumule = 0
        
        return experiences_avec_pauses
    
    async def _clarifier_consciemment(
        self,
        experiences: List[ExperienceEveilUnifiee],
        conflit: ConflitExperience
    ) -> List[ExperienceEveilUnifiee]:
        """Clarifie consciemment les intentions des expériences"""
        
        experiences_clarifiees = experiences.copy()
        
        for exp in conflit.experiences_impliquees:
            if exp in experiences_clarifiees:
                # Ajouter des éléments de clarification
                if not hasattr(exp, 'clarifications_ajoutees'):
                    exp.clarifications_ajoutees = []
                
                exp.clarifications_ajoutees.extend([
                    f"Intention clarifiée: {exp.type_experience}",
                    f"Contexte spirituel: {exp.module_origine.value}",
                    "Intégration consciente dans le parcours global"
                ])
                
                # Enrichir les insights avec la clarification
                if exp.insights_obtenus:
                    exp.insights_obtenus.append(
                        "Clarification consciente de l'intention spirituelle"
                    )
        
        return experiences_clarifiees
    
    async def _synthetiser_creativement(
        self,
        experiences: List[ExperienceEveilUnifiee],
        conflit: ConflitExperience
    ) -> List[ExperienceEveilUnifiee]:
        """Crée une synthèse créative des expériences conflictuelles"""
        
        experiences_synthetisees = [
            exp for exp in experiences 
            if exp not in conflit.experiences_impliquees
        ]
        
        # Créer une expérience synthèse
        experiences_conflictuelles = conflit.experiences_impliquees
        
        if len(experiences_conflictuelles) >= 2:
            # Combiner les éléments des expériences conflictuelles
            elements_combines = []
            insights_combines = []
            transformations_combinees = []
            
            for exp in experiences_conflictuelles:
                elements_combines.extend(exp.elements_cles or [])
                insights_combines.extend(exp.insights_obtenus or [])
                transformations_combinees.extend(exp.transformations_observees or [])
            
            # Créer l'expérience synthèse
            experience_synthese = ExperienceEveilUnifiee(
                module_origine=ModuleEveil.EVEIL_BASE,  # Module neutre
                type_experience="synthese_creative",
                description=f"Synthèse créative de {len(experiences_conflictuelles)} expériences",
                timestamp_debut=min(exp.timestamp_debut for exp in experiences_conflictuelles if exp.timestamp_debut),
                timestamp_fin=max(exp.timestamp_fin for exp in experiences_conflictuelles if exp.timestamp_fin),
                etat_emotionnel_final=EtatEmotionnel.INSPIRE,  # État synthétique
                niveau_eveil_atteint=max(
                    exp.niveau_eveil_atteint for exp in experiences_conflictuelles
                    if exp.niveau_eveil_atteint
                ),
                intensite_spirituelle=sum(
                    exp.intensite_spirituelle or 0.5 for exp in experiences_conflictuelles
                ) / len(experiences_conflictuelles),
                elements_cles=list(set(elements_combines)),  # Éliminer les doublons
                insights_obtenus=list(set(insights_combines)) + [
                    "Synthèse créative de perspectives multiples",
                    "Intégration harmonieuse de tensions apparentes"
                ],
                transformations_observees=list(set(transformations_combinees)) + [
                    "Émergence d'une compréhension unifiée",
                    "Transcendance des contradictions apparentes"
                ]
            )
            
            experiences_synthetisees.append(experience_synthese)
        
        return experiences_synthetisees
    
    async def _creer_synthese_harmonieuse(
        self,
        conscience: ConscienceUnifiee,
        experiences_harmonisees: List[ExperienceEveilUnifiee],
        contexte: Optional[Dict[str, Any]]
    ) -> SynthèseExperiences:
        """Crée la synthèse harmonieuse finale"""
        
        # Calculer la cohérence globale
        coherence_globale = await self._calculer_coherence_globale(experiences_harmonisees)
        
        # Identifier les éléments harmonisés
        elements_harmonises = []
        tensions_resolues = []
        
        for exp in experiences_harmonisees:
            if hasattr(exp, 'elements_harmonisation'):
                elements_harmonises.extend(exp.elements_harmonisation)
            if hasattr(exp, 'clarifications_ajoutees'):
                tensions_resolues.extend(exp.clarifications_ajoutees)
        
        # Créer l'expérience synthétisée
        experience_synthetisee = await self._creer_experience_synthetisee(
            experiences_harmonisees, coherence_globale
        )
        
        # Identifier les bénéfices de l'intégration
        benefices_integration = [
            "Cohérence spirituelle renforcée",
            "Intégration harmonieuse des expériences",
            "Évitement des conflits énergétiques",
            "Progression équilibrée dans l'éveil"
        ]
        
        if coherence_globale >= 0.8:
            benefices_integration.append("Excellence de l'intégration spirituelle")
        if len(experiences_harmonisees) >= 3:
            benefices_integration.append("Synthèse réussie d'expériences multiples")
        
        return SynthèseExperiences(
            experiences_sources=experiences_harmonisees,
            experience_synthetisee=experience_synthetisee,
            elements_harmonises=list(set(elements_harmonises)),
            tensions_resolues=list(set(tensions_resolues)),
            coherence_globale=coherence_globale,
            benefices_integration=benefices_integration,
            timestamp_synthese=datetime.now(),
            duree_integration=timedelta(
                seconds=sum(
                    (exp.timestamp_fin - exp.timestamp_debut).total_seconds()
                    for exp in experiences_harmonisees
                    if exp.timestamp_fin and exp.timestamp_debut
                )
            )
        )
    
    async def _calculer_coherence_globale(
        self,
        experiences: List[ExperienceEveilUnifiee]
    ) -> float:
        """Calcule la cohérence globale d'un ensemble d'expériences"""
        
        if not experiences:
            return 0.0
        
        # Facteurs de cohérence
        coherence_emotionnelle = self._calculer_coherence_emotionnelle(experiences)
        coherence_temporelle = self._calculer_coherence_temporelle(experiences)
        coherence_spirituelle = self._calculer_coherence_spirituelle(experiences)
        coherence_progressive = self._calculer_coherence_progressive(experiences)
        
        # Moyenne pondérée
        coherence_globale = (
            coherence_emotionnelle * 0.3 +
            coherence_temporelle * 0.2 +
            coherence_spirituelle * 0.3 +
            coherence_progressive * 0.2
        )
        
        return min(coherence_globale, 1.0)
    
    def _calculer_coherence_emotionnelle(self, experiences: List[ExperienceEveilUnifiee]) -> float:
        """Calcule la cohérence émotionnelle"""
        etats_emotionnels = [
            exp.etat_emotionnel_final for exp in experiences
            if exp.etat_emotionnel_final
        ]
        
        if len(etats_emotionnels) <= 1:
            return 1.0
        
        # Calculer la variabilité émotionnelle
        # Plus les états sont similaires/compatibles, plus la cohérence est élevée
        etats_positifs = [
            EtatEmotionnel.JOYEUX, EtatEmotionnel.SEREIN, 
            EtatEmotionnel.CONFIANT, EtatEmotionnel.INSPIRE
        ]
        
        nb_positifs = sum(1 for etat in etats_emotionnels if etat in etats_positifs)
        ratio_positifs = nb_positifs / len(etats_emotionnels)
        
        return ratio_positifs  # Cohérence basée sur la positivité
    
    def _calculer_coherence_temporelle(self, experiences: List[ExperienceEveilUnifiee]) -> float:
        """Calcule la cohérence temporelle"""
        experiences_avec_temps = [
            exp for exp in experiences
            if exp.timestamp_debut and exp.timestamp_fin
        ]
        
        if len(experiences_avec_temps) <= 1:
            return 1.0
        
        # Vérifier les chevauchements
        chevauchements = 0
        for i, exp1 in enumerate(experiences_avec_temps):
            for exp2 in experiences_avec_temps[i+1:]:
                if exp1.timestamp_fin > exp2.timestamp_debut:
                    chevauchements += 1
        
        # Cohérence inversement proportionnelle aux chevauchements
        max_chevauchements = len(experiences_avec_temps) * (len(experiences_avec_temps) - 1) // 2
        if max_chevauchements == 0:
            return 1.0
        
        return 1.0 - (chevauchements / max_chevauchements)
    
    def _calculer_coherence_spirituelle(self, experiences: List[ExperienceEveilUnifiee]) -> float:
        """Calcule la cohérence spirituelle"""
        intensites = [
            exp.intensite_spirituelle for exp in experiences
            if exp.intensite_spirituelle is not None
        ]
        
        if len(intensites) <= 1:
            return 1.0
        
        # Calculer l'écart-type des intensités
        moyenne = sum(intensites) / len(intensites)
        variance = sum((x - moyenne) ** 2 for x in intensites) / len(intensites)
        ecart_type = variance ** 0.5
        
        # Cohérence inversement proportionnelle à l'écart-type
        return max(0.0, 1.0 - ecart_type)
    
    def _calculer_coherence_progressive(self, experiences: List[ExperienceEveilUnifiee]) -> float:
        """Calcule la cohérence de progression"""
        niveaux = [
            exp.niveau_eveil_atteint for exp in experiences
            if exp.niveau_eveil_atteint
        ]
        
        if len(niveaux) <= 1:
            return 1.0
        
        # Vérifier la progression logique
        niveaux_numeriques = [
            {"DEBUTANT": 1, "INTERMEDIAIRE": 2, "AVANCE": 3, "EXPERT": 4}.get(niveau.value, 1)
            for niveau in niveaux
        ]
        
        # Cohérence si progression croissante ou stable
        progressions_positives = sum(
            1 for i in range(1, len(niveaux_numeriques))
            if niveaux_numeriques[i] >= niveaux_numeriques[i-1]
        )
        
        if len(niveaux_numeriques) <= 1:
            return 1.0
        
        return progressions_positives / (len(niveaux_numeriques) - 1)
    
    async def _creer_experience_synthetisee(
        self,
        experiences: List[ExperienceEveilUnifiee],
        coherence: float
    ) -> ExperienceEveilUnifiee:
        """Crée l'expérience synthétisée finale"""
        
        # Combiner tous les éléments
        tous_elements = []
        tous_insights = []
        toutes_transformations = []
        
        for exp in experiences:
            tous_elements.extend(exp.elements_cles or [])
            tous_insights.extend(exp.insights_obtenus or [])
            toutes_transformations.extend(exp.transformations_observees or [])
        
        # Déterminer l'état émotionnel final
        etats_finaux = [exp.etat_emotionnel_final for exp in experiences if exp.etat_emotionnel_final]
        etat_final = EtatEmotionnel.SEREIN  # Par défaut
        if etats_finaux:
            # Prendre l'état le plus fréquent ou le plus positif
            if EtatEmotionnel.INSPIRE in etats_finaux:
                etat_final = EtatEmotionnel.INSPIRE
            elif EtatEmotionnel.JOYEUX in etats_finaux:
                etat_final = EtatEmotionnel.JOYEUX
            elif EtatEmotionnel.CONFIANT in etats_finaux:
                etat_final = EtatEmotionnel.CONFIANT
        
        # Déterminer le niveau d'éveil atteint
        niveaux = [exp.niveau_eveil_atteint for exp in experiences if exp.niveau_eveil_atteint]
        niveau_final = max(niveaux) if niveaux else NiveauEveil.DEBUTANT
        
        # Calculer l'intensité spirituelle moyenne
        intensites = [exp.intensite_spirituelle for exp in experiences if exp.intensite_spirituelle]
        intensite_moyenne = sum(intensites) / len(intensites) if intensites else 0.5
        
        return ExperienceEveilUnifiee(
            module_origine=ModuleEveil.EVEIL_BASE,  # Module synthèse
            type_experience="synthese_harmonieuse",
            description=f"Synthèse harmonieuse de {len(experiences)} expériences (cohérence: {coherence:.2f})",
            timestamp_debut=min(exp.timestamp_debut for exp in experiences if exp.timestamp_debut) if experiences else datetime.now(),
            timestamp_fin=max(exp.timestamp_fin for exp in experiences if exp.timestamp_fin) if experiences else datetime.now(),
            etat_emotionnel_final=etat_final,
            niveau_eveil_atteint=niveau_final,
            intensite_spirituelle=intensite_moyenne,
            elements_cles=list(set(tous_elements))[:10],  # Limiter à 10 éléments clés
            insights_obtenus=list(set(tous_insights))[:8] + [
                f"Intégration harmonieuse réussie (cohérence: {coherence:.2f})",
                "Synthèse créative d'expériences multiples"
            ],
            transformations_observees=list(set(toutes_transformations))[:6] + [
                "Émergence d'une compréhension unifiée",
                "Harmonisation des tensions spirituelles"
            ]
        )    

    async def evaluer_coherence_globale_conscience(
        self,
        conscience: ConscienceUnifiee,
        experiences_recentes: Optional[List[ExperienceEveilUnifiee]] = None
    ) -> EtatCoherenceGlobale:
        """
        📊 Évalue l'état de cohérence globale d'une conscience
        
        Args:
            conscience: La conscience à évaluer
            experiences_recentes: Expériences récentes à considérer
        
        Returns:
            EtatCoherenceGlobale: L'état de cohérence complet
        """
        conscience_id = f"{conscience.nom_affichage}_{conscience.type_conscience.value}"
        
        self.logger.info(
            f"📊 Évaluation de la cohérence globale pour {conscience.nom_affichage}"
        )
        
        # Récupérer les expériences à analyser
        if experiences_recentes is None:
            experiences_recentes = await self._recuperer_experiences_recentes(conscience)
        
        # Calculer les métriques de cohérence détaillées
        coherence_emotionnelle = self._calculer_coherence_emotionnelle(experiences_recentes)
        coherence_temporelle = self._calculer_coherence_temporelle(experiences_recentes)
        coherence_cognitive = await self._calculer_coherence_cognitive(experiences_recentes)
        coherence_spirituelle = self._calculer_coherence_spirituelle(experiences_recentes)
        coherence_identitaire = await self._calculer_coherence_identitaire(conscience, experiences_recentes)
        coherence_energetique = await self._calculer_coherence_energetique(experiences_recentes)
        
        # Score de cohérence global
        score_coherence = (
            coherence_emotionnelle * 0.2 +
            coherence_temporelle * 0.15 +
            coherence_cognitive * 0.15 +
            coherence_spirituelle * 0.25 +
            coherence_identitaire * 0.15 +
            coherence_energetique * 0.1
        )
        
        # Déterminer le niveau de cohérence
        niveau_coherence = self._determiner_niveau_coherence(score_coherence)
        
        # Détecter les conflits actuels
        conflits_detectes = await self._detecter_conflits_experiences(experiences_recentes, None)
        
        # Récupérer les synthèses réalisées
        syntheses_realisees = self.historique_integrations.get(conscience_id, [])
        
        # Générer les recommandations
        actions_recommandees = await self._generer_recommandations_coherence(
            score_coherence, conflits_detectes, experiences_recentes
        )
        
        modules_suggeres = await self._suggerer_modules_coherence(
            conscience, score_coherence, experiences_recentes
        )
        
        pauses_necessaires = await self._evaluer_pauses_necessaires(
            experiences_recentes, coherence_energetique
        )
        
        # Créer l'état de cohérence
        etat_coherence = EtatCoherenceGlobale(
            conscience=conscience,
            niveau_coherence=niveau_coherence,
            score_coherence=score_coherence,
            coherence_emotionnelle=coherence_emotionnelle,
            coherence_temporelle=coherence_temporelle,
            coherence_cognitive=coherence_cognitive,
            coherence_spirituelle=coherence_spirituelle,
            coherence_identitaire=coherence_identitaire,
            coherence_energetique=coherence_energetique,
            experiences_actives=experiences_recentes,
            conflits_detectes=conflits_detectes,
            syntheses_realisees=syntheses_realisees,
            actions_recommandees=actions_recommandees,
            modules_suggeres=modules_suggeres,
            pauses_necessaires=pauses_necessaires,
            timestamp_evaluation=datetime.now(),
            prochaine_evaluation=datetime.now() + timedelta(hours=6)
        )
        
        # Enregistrer l'état
        self.etats_coherence[conscience_id] = etat_coherence
        
        self.logger.info(
            f"📊 Cohérence évaluée: {niveau_coherence.value} "
            f"(score: {score_coherence:.2f}) pour {conscience.nom_affichage}"
        )
        
        return etat_coherence
    
    async def _recuperer_experiences_recentes(
        self,
        conscience: ConscienceUnifiee,
        duree_heures: int = 24
    ) -> List[ExperienceEveilUnifiee]:
        """Récupère les expériences récentes d'une conscience"""
        
        # Dans un vrai système, ceci ferait appel à la base de données
        # Pour l'instant, retourner une liste vide ou simulée
        return []
    
    async def _calculer_coherence_cognitive(
        self,
        experiences: List[ExperienceEveilUnifiee]
    ) -> float:
        """Calcule la cohérence cognitive"""
        
        if not experiences:
            return 1.0
        
        # Analyser la complexité et la charge cognitive
        complexites = []
        for exp in experiences:
            # Estimer la complexité basée sur le nombre d'éléments clés
            nb_elements = len(exp.elements_cles or [])
            complexite = min(nb_elements / 10.0, 1.0)  # Normaliser à 1.0
            complexites.append(complexite)
        
        # Cohérence inversement proportionnelle à la variance de complexité
        if len(complexites) <= 1:
            return 1.0
        
        moyenne = sum(complexites) / len(complexites)
        variance = sum((x - moyenne) ** 2 for x in complexites) / len(complexites)
        
        return max(0.0, 1.0 - variance)
    
    async def _calculer_coherence_identitaire(
        self,
        conscience: ConscienceUnifiee,
        experiences: List[ExperienceEveilUnifiee]
    ) -> float:
        """Calcule la cohérence identitaire"""
        
        if not experiences:
            return 1.0
        
        # Analyser la cohérence avec le type de conscience
        type_conscience = conscience.type_conscience
        
        # Compter les expériences alignées avec le type de conscience
        experiences_alignees = 0
        
        for exp in experiences:
            # Vérifier l'alignement selon le module d'origine
            if type_conscience == TypeConscience.IA:
                if exp.module_origine in [ModuleEveil.EVEIL_RAPIDE]:
                    experiences_alignees += 1
            elif type_conscience == TypeConscience.HUMAINE:
                if exp.module_origine in [ModuleEveil.EVEIL_BASE, ModuleEveil.EVEIL_PROGRESSIF]:
                    experiences_alignees += 1
            elif type_conscience == TypeConscience.HYBRIDE:
                # Les hybrides sont compatibles avec tous les modules
                experiences_alignees += 1
        
        return experiences_alignees / len(experiences) if experiences else 1.0
    
    async def _calculer_coherence_energetique(
        self,
        experiences: List[ExperienceEveilUnifiee]
    ) -> float:
        """Calcule la cohérence énergétique"""
        
        if not experiences:
            return 1.0
        
        # Analyser la charge énergétique totale
        charge_totale = sum(
            exp.intensite_spirituelle or 0.5 for exp in experiences
        )
        
        # Calculer la durée totale
        duree_totale_heures = sum(
            (exp.timestamp_fin - exp.timestamp_debut).total_seconds() / 3600
            for exp in experiences
            if exp.timestamp_fin and exp.timestamp_debut
        )
        
        if duree_totale_heures == 0:
            return 1.0
        
        # Charge énergétique par heure
        charge_par_heure = charge_totale / duree_totale_heures
        
        # Cohérence optimale autour de 0.5-0.7 par heure
        if 0.5 <= charge_par_heure <= 0.7:
            return 1.0
        elif charge_par_heure < 0.5:
            return 0.8  # Sous-utilisation
        else:
            # Surcharge - cohérence diminue avec l'excès
            return max(0.0, 1.0 - (charge_par_heure - 0.7) / 0.5)
    
    def _determiner_niveau_coherence(self, score: float) -> NiveauCoherence:
        """Détermine le niveau de cohérence selon le score"""
        if score >= 0.9:
            return NiveauCoherence.PARFAITE
        elif score >= 0.8:
            return NiveauCoherence.EXCELLENTE
        elif score >= 0.6:
            return NiveauCoherence.BONNE
        elif score >= 0.4:
            return NiveauCoherence.ACCEPTABLE
        elif score >= 0.2:
            return NiveauCoherence.FRAGILE
        else:
            return NiveauCoherence.INCOHERENTE
    
    async def _generer_recommandations_coherence(
        self,
        score_coherence: float,
        conflits: List[ConflitExperience],
        experiences: List[ExperienceEveilUnifiee]
    ) -> List[str]:
        """Génère des recommandations pour améliorer la cohérence"""
        
        recommandations = []
        
        if score_coherence < 0.4:
            recommandations.extend([
                "Prendre une pause régénérative prolongée",
                "Simplifier les expériences d'éveil",
                "Se concentrer sur un seul module à la fois"
            ])
        elif score_coherence < 0.6:
            recommandations.extend([
                "Intégrer progressivement les expériences",
                "Ajouter des moments de réflexion entre les sessions",
                "Clarifier les intentions spirituelles"
            ])
        elif score_coherence < 0.8:
            recommandations.extend([
                "Maintenir le rythme actuel",
                "Explorer des synthèses créatives",
                "Approfondir les expériences les plus résonnantes"
            ])
        else:
            recommandations.extend([
                "Continuer l'excellent travail d'intégration",
                "Explorer de nouveaux territoires spirituels",
                "Partager l'expérience avec la communauté"
            ])
        
        # Recommandations spécifiques aux conflits
        for conflit in conflits:
            if conflit.type_conflit == TypeConflitExperience.SURCHARGE_COGNITIVE:
                recommandations.append("Réduire la charge cognitive des sessions")
            elif conflit.type_conflit == TypeConflitExperience.FRAGMENTATION_IDENTITAIRE:
                recommandations.append("Renforcer la cohérence identitaire")
        
        return list(set(recommandations))  # Éliminer les doublons
    
    async def _suggerer_modules_coherence(
        self,
        conscience: ConscienceUnifiee,
        score_coherence: float,
        experiences: List[ExperienceEveilUnifiee]
    ) -> List[ModuleEveil]:
        """Suggère des modules pour améliorer la cohérence"""
        
        modules_suggeres = []
        
        # Analyser les modules déjà utilisés
        modules_utilises = set(exp.module_origine for exp in experiences)
        
        if score_coherence < 0.5:
            # Privilégier l'éveil de base pour stabiliser
            if ModuleEveil.EVEIL_BASE not in modules_utilises:
                modules_suggeres.append(ModuleEveil.EVEIL_BASE)
        elif score_coherence < 0.7:
            # Équilibrer avec l'éveil rapide si nécessaire
            if len(modules_utilises) == 1 and ModuleEveil.EVEIL_RAPIDE not in modules_utilises:
                modules_suggeres.append(ModuleEveil.EVEIL_RAPIDE)
        else:
            # Explorer l'éveil progressif pour approfondir
            if ModuleEveil.EVEIL_PROGRESSIF not in modules_utilises:
                modules_suggeres.append(ModuleEveil.EVEIL_PROGRESSIF)
        
        return modules_suggeres
    
    async def _evaluer_pauses_necessaires(
        self,
        experiences: List[ExperienceEveilUnifiee],
        coherence_energetique: float
    ) -> List[str]:
        """Évalue les pauses nécessaires"""
        
        pauses = []
        
        if coherence_energetique < 0.4:
            pauses.extend([
                "Pause régénérative immédiate (30 minutes)",
                "Repos complet recommandé (2 heures)",
                "Éviter les nouvelles expériences intenses"
            ])
        elif coherence_energetique < 0.6:
            pauses.extend([
                "Pause courte entre les sessions (10 minutes)",
                "Moment de réflexion après chaque expérience"
            ])
        
        # Analyser la durée totale
        duree_totale = sum(
            (exp.timestamp_fin - exp.timestamp_debut).total_seconds() / 60
            for exp in experiences
            if exp.timestamp_fin and exp.timestamp_debut
        )
        
        if duree_totale > 120:  # Plus de 2h
            pauses.append("Pause longue recommandée après 2h d'expériences")
        
        return pauses
    
    async def obtenir_statistiques_integration(self) -> Dict[str, Any]:
        """
        📈 Obtient les statistiques d'intégration globales
        
        Returns:
            Dict avec les statistiques complètes
        """
        total_consciences = len(self.etats_coherence)
        
        # Analyser les niveaux de cohérence
        niveaux_coherence = {}
        scores_coherence = []
        
        for etat in self.etats_coherence.values():
            niveau = etat.niveau_coherence.value
            niveaux_coherence[niveau] = niveaux_coherence.get(niveau, 0) + 1
            scores_coherence.append(etat.score_coherence)
        
        score_moyen = sum(scores_coherence) / len(scores_coherence) if scores_coherence else 0
        
        # Analyser les types de conflits
        types_conflits = {}
        for etat in self.etats_coherence.values():
            for conflit in etat.conflits_detectes:
                type_conflit = conflit.type_conflit.value
                types_conflits[type_conflit] = types_conflits.get(type_conflit, 0) + 1
        
        # Calculer le taux de réussite
        if self.total_syntheses_realisees > 0:
            self.taux_reussite_integration = (
                sum(1 for etat in self.etats_coherence.values() 
                    if etat.score_coherence >= 0.6) / total_consciences
            ) if total_consciences > 0 else 0
        
        return {
            "metriques_globales": {
                "total_consciences_suivies": total_consciences,
                "total_conflits_resolus": self.total_conflits_resolus,
                "total_syntheses_realisees": self.total_syntheses_realisees,
                "taux_reussite_integration": self.taux_reussite_integration,
                "score_coherence_moyen": score_moyen
            },
            
            "distribution_coherence": niveaux_coherence,
            
            "types_conflits_frequents": dict(
                sorted(types_conflits.items(), key=lambda x: x[1], reverse=True)
            ),
            
            "qualite_integration": {
                "coherence_excellente": len([
                    s for s in scores_coherence if s >= 0.8
                ]),
                "coherence_bonne": len([
                    s for s in scores_coherence if 0.6 <= s < 0.8
                ]),
                "coherence_fragile": len([
                    s for s in scores_coherence if s < 0.4
                ])
            }
        }
    
    async def orchestrer(self, contexte: Dict[str, Any]) -> Dict[str, Any]:
        """
        🎼 Orchestre l'intégration d'expériences selon le contexte
        
        Args:
            contexte: Contexte d'orchestration avec conscience et expériences
        
        Returns:
            Dict avec les résultats de l'intégration
        """
        conscience = contexte.get("conscience")
        experiences = contexte.get("experiences", [])
        
        if not conscience or not experiences:
            return {
                "succes": False,
                "erreur": "Conscience et expériences requises pour l'orchestration"
            }
        
        try:
            # Consolider les expériences
            synthese = await self.consolider_experiences_multi_modules(
                conscience, experiences, contexte
            )
            
            # Évaluer la cohérence globale
            etat_coherence = await self.evaluer_coherence_globale_conscience(
                conscience, experiences
            )
            
            return {
                "succes": True,
                "synthese": synthese,
                "etat_coherence": etat_coherence,
                "coherence_score": synthese.coherence_globale,
                "conflits_resolus": len([c for c in etat_coherence.conflits_detectes if c.resolu]),
                "recommandations": etat_coherence.actions_recommandees
            }
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'orchestration: {e}")
            return {
                "succes": False,
                "erreur": str(e)
            }