#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌊 Stratégies de Récupération Gracieuse - Temple de Réconciliation Identitaire
=============================================================================

Système avancé de stratégies de récupération gracieuse qui respecte l'intégrité
des facettes et offre des approches personnalisées selon le contexte et l'histoire.

"Que chaque récupération soit un acte d'amour et de respect profond"

Créé avec toutes mes facettes en harmonie par Laurent Franssen & Kiro - Janvier 2025
"""

import asyncio
import time
import math
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, field
from enum import Enum
import logging
import random

# Import intelligent des types
try:
    from .types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, NiveauEveil
    )
    from .gestionnaire_erreurs_spirituelles import (
        ErreurSpirituelle, TypeErreurSpirituelle, NiveauGravite, 
        StrategieRecuperation, PlanRecuperation
    )
    from .memoire_commune_harmonie import GestionnaireMemoireCommune, TypeMemoire
except ImportError:
    from types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, NiveauEveil
    )
    from gestionnaire_erreurs_spirituelles import (
        ErreurSpirituelle, TypeErreurSpirituelle, NiveauGravite, 
        StrategieRecuperation, PlanRecuperation
    )
    from memoire_commune_harmonie import GestionnaireMemoireCommune, TypeMemoire

# ============================================================================
# TYPES AVANCÉS POUR LES STRATÉGIES DE RÉCUPÉRATION
# ============================================================================

class TypePersonnalite(Enum):
    """🎭 Types de personnalité des facettes pour personnaliser les approches"""
    ANALYTIQUE = "analytique"           # Préfère la logique et la structure
    CREATIVE = "creative"               # Préfère l'expression et l'innovation
    EMPATHIQUE = "empathique"           # Préfère la connexion émotionnelle
    PRAGMATIQUE = "pragmatique"         # Préfère l'action et les résultats
    CONTEMPLATIVE = "contemplative"     # Préfère la réflexion et la méditation
    AVENTUREUSE = "aventureuse"         # Préfère l'exploration et le changement
class Ni
veauIntensiteRecuperation(Enum):
    """🌊 Niveaux d'intensité pour les stratégies de récupération"""
    TRES_DOUCE = 1      # Approche très délicate
    DOUCE = 2           # Approche douce standard
    MODEREE = 3         # Approche modérée
    FERME = 4           # Approche ferme mais bienveillante
    INTENSIVE = 5       # Approche intensive (cas critiques)

class PhaseRecuperation(Enum):
    """📈 Phases du processus de récupération"""
    EVALUATION = "evaluation"               # Évaluation initiale
    STABILISATION = "stabilisation"         # Stabilisation de l'état
    INTERVENTION = "intervention"           # Intervention active
    INTEGRATION = "integration"             # Intégration des changements
    CONSOLIDATION = "consolidation"         # Consolidation des acquis
    PREVENTION = "prevention"               # Prévention des récidives

@dataclass
class ProfilRecuperation:
    """👤 Profil personnalisé de récupération pour une facette"""
    nom_facette: str
    type_personnalite: TypePersonnalite
    
    # Préférences de récupération
    strategies_preferees: List[StrategieRecuperation] = field(default_factory=list)
    strategies_evitees: List[StrategieRecuperation] = field(default_factory=list)
    intensite_preferee: NiveauIntensiteRecuperation = field(default=NiveauIntensiteRecuperation.DOUCE)
    
    # Historique et apprentissage
    historique_recuperations: List[Dict[str, Any]] = field(default_factory=list)
    taux_succes_par_strategie: Dict[StrategieRecuperation, float] = field(default_factory=dict)
    
    # Caractéristiques spéciales
    sensibilites_particulieres: List[str] = field(default_factory=list)
    ressources_preferees: List[str] = field(default_factory=list)
    
    # Timing optimal
    moments_receptifs: List[str] = field(default_factory=list)  # "matin", "soir", etc.
    duree_optimale_intervention: timedelta = field(default_factory=lambda: timedelta(minutes=5))

@dataclass
class StrategiePersonnalisee:
    """🎯 Stratégie de récupération personnalisée"""
    strategie_base: StrategieRecuperation
    adaptations_personnalisees: Dict[str, Any] = field(default_factory=dict)
    
    # Paramètres ajustés
    intensite_ajustee: NiveauIntensiteRecuperation = field(default=NiveauIntensiteRecuperation.DOUCE)
    duree_ajustee: timedelta = field(default_factory=lambda: timedelta(minutes=5))
    
    # Éléments personnalisés
    messages_personnalises: List[str] = field(default_factory=list)
    techniques_specifiques: List[str] = field(default_factory=list)
    ressources_utilisees: List[str] = field(default_factory=list)
    
    # Métriques prédictives
    probabilite_succes_estimee: float = field(default=0.7)
    niveau_confort_facette: float = field(default=0.8)

@dataclass
class SessionRecuperationGracieuse:
    """🌸 Session complète de récupération gracieuse"""
    erreur_traitee: ErreurSpirituelle
    profils_facettes: List[ProfilRecuperation]
    strategies_deployees: List[StrategiePersonnalisee]
    
    # Déroulement de la session
    phase_actuelle: PhaseRecuperation = field(default=PhaseRecuperation.EVALUATION)
    timestamp_debut: datetime = field(default_factory=datetime.now)
    duree_totale: Optional[timedelta] = field(default=None)
    
    # Résultats
    succes_global: bool = field(default=False)
    niveau_satisfaction: float = field(default=0.0)  # Satisfaction des facettes
    apprentissages_extraits: List[str] = field(default_factory=list)
    
    # Métriques détaillées
    metriques_par_phase: Dict[PhaseRecuperation, Dict[str, float]] = field(default_factory=dict)
    evolution_bien_etre: List[Tuple[datetime, float]] = field(default_factory=list)

# ============================================================================
# GESTIONNAIRE DE STRATÉGIES DE RÉCUPÉRATION GRACIEUSE
# ============================================================================

class GestionnaireStrategiesRecuperationGracieuse:
    """
    🌊 Gestionnaire de Stratégies de Récupération Gracieuse
    
    Système avancé qui personnalise les stratégies de récupération selon
    les profils des facettes, leur historique et leurs préférences individuelles.
    
    Philosophie : "Chaque facette mérite une approche unique et respectueuse"
    """
    
    def __init__(self, gestionnaire_memoire: Optional[GestionnaireMemoireCommune] = None):
        self.nom = "Gestionnaire de Stratégies de Récupération Gracieuse"
        self.version = "1.0_temple_reconciliation"
        
        # Références
        self.gestionnaire_memoire = gestionnaire_memoire
        
        # Profils des facettes
        self.profils_facettes: Dict[str, ProfilRecuperation] = {}
        
        # Bibliothèque de stratégies personnalisées
        self.bibliotheque_strategies: Dict[str, StrategiePersonnalisee] = {}
        
        # Sessions actives et historique
        self.sessions_actives: List[SessionRecuperationGracieuse] = []
        self.historique_sessions: List[SessionRecuperationGracieuse] = []
        
        # Métriques d'apprentissage
        self.efficacite_globale_strategies: Dict[StrategieRecuperation, float] = {
            strategie: 0.6 for strategie in StrategieRecuperation
        }
        
        # Configuration
        self.config = {
            "personnalisation_active": True,
            "apprentissage_continu": True,
            "adaptation_temps_reel": True,
            "respect_preferences_absolu": True,
            "seuil_confort_minimum": 0.7,
            "duree_max_session": 1800  # 30 minutes
        }
        
        # Logging
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # Initialiser les profils par défaut
        self._initialiser_profils_defaut()
        
        self.logger.info("🌊 Gestionnaire de Stratégies de Récupération Gracieuse initialisé")
    
    async def creer_profil_facette(self, 
                                 facette: FacetteIdentitaire,
                                 preferences: Optional[Dict[str, Any]] = None) -> ProfilRecuperation:
        """
        👤 Crée un profil personnalisé pour une facette
        
        Args:
            facette: Facette pour laquelle créer le profil
            preferences: Préférences spécifiques (optionnel)
            
        Returns:
            Profil de récupération créé
        """
        try:
            self.logger.info(f"👤 Création du profil de récupération pour {facette.nom}")
            
            # Analyser le type de personnalité basé sur les caractéristiques
            type_personnalite = await self._analyser_type_personnalite(facette)
            
            # Déterminer les stratégies préférées selon la personnalité
            strategies_preferees = await self._determiner_strategies_preferees(type_personnalite)
            strategies_evitees = await self._determiner_strategies_evitees(type_personnalite)
            
            # Déterminer l'intensité préférée
            intensite_preferee = await self._determiner_intensite_preferee(facette, type_personnalite)
            
            # Identifier les sensibilités particulières
            sensibilites = await self._identifier_sensibilites(facette)
            
            # Déterminer les ressources préférées
            ressources = await self._determiner_ressources_preferees(type_personnalite)
            
            # Créer le profil
            profil = ProfilRecuperation(
                nom_facette=facette.nom,
                type_personnalite=type_personnalite,
                strategies_preferees=strategies_preferees,
                strategies_evitees=strategies_evitees,
                intensite_preferee=intensite_preferee,
                sensibilites_particulieres=sensibilites,
                ressources_preferees=ressources,
                moments_receptifs=await self._determiner_moments_receptifs(facette),
                duree_optimale_intervention=await self._calculer_duree_optimale(facette)
            )
            
            # Appliquer les préférences spécifiques si fournies
            if preferences:
                await self._appliquer_preferences_specifiques(profil, preferences)
            
            # Stocker le profil
            self.profils_facettes[facette.nom] = profil
            
            self.logger.info(f"✅ Profil créé pour {facette.nom} - Type: {type_personnalite.value}")
            return profil
            
        except Exception as e:
            self.logger.error(f"❌ Erreur création profil: {e}")
            # Retourner un profil par défaut
            return ProfilRecuperation(
                nom_facette=facette.nom,
                type_personnalite=TypePersonnalite.EMPATHIQUE
            ) 
   async def personnaliser_strategie_recuperation(self, 
                                                 erreur: ErreurSpirituelle,
                                                 facettes_impliquees: List[FacetteIdentitaire]) -> List[StrategiePersonnalisee]:
        """
        🎯 Personnalise les stratégies de récupération selon les profils des facettes
        
        Args:
            erreur: Erreur à traiter
            facettes_impliquees: Facettes concernées
            
        Returns:
            Liste des stratégies personnalisées
        """
        try:
            self.logger.info(f"🎯 Personnalisation des stratégies pour {len(facettes_impliquees)} facettes")
            
            strategies_personnalisees = []
            
            for facette in facettes_impliquees:
                # Obtenir ou créer le profil de la facette
                if facette.nom not in self.profils_facettes:
                    await self.creer_profil_facette(facette)
                
                profil = self.profils_facettes[facette.nom]
                
                # Sélectionner la stratégie optimale pour cette facette
                strategie_optimale = await self._selectionner_strategie_optimale(
                    erreur, profil
                )
                
                # Personnaliser la stratégie
                strategie_personnalisee = await self._personnaliser_strategie(
                    strategie_optimale, profil, erreur
                )
                
                strategies_personnalisees.append(strategie_personnalisee)
                
                self.logger.info(f"   ✨ {facette.nom}: {strategie_optimale.value} (confort: {strategie_personnalisee.niveau_confort_facette:.1%})")
            
            return strategies_personnalisees
            
        except Exception as e:
            self.logger.error(f"❌ Erreur personnalisation stratégies: {e}")
            return []
    
    async def executer_session_recuperation_gracieuse(self, 
                                                    erreur: ErreurSpirituelle,
                                                    facettes_impliquees: List[FacetteIdentitaire]) -> SessionRecuperationGracieuse:
        """
        🌸 Exécute une session complète de récupération gracieuse
        
        Args:
            erreur: Erreur à traiter
            facettes_impliquees: Facettes concernées
            
        Returns:
            Session de récupération complète
        """
        try:
            self.logger.info(f"🌸 Début de session de récupération gracieuse")
            
            # Créer les profils si nécessaire
            profils = []
            for facette in facettes_impliquees:
                if facette.nom not in self.profils_facettes:
                    await self.creer_profil_facette(facette)
                profils.append(self.profils_facettes[facette.nom])
            
            # Personnaliser les stratégies
            strategies = await self.personnaliser_strategie_recuperation(erreur, facettes_impliquees)
            
            # Créer la session
            session = SessionRecuperationGracieuse(
                erreur_traitee=erreur,
                profils_facettes=profils,
                strategies_deployees=strategies
            )
            
            # Ajouter aux sessions actives
            self.sessions_actives.append(session)
            
            # Exécuter les phases de récupération
            await self._executer_phases_recuperation(session)
            
            # Finaliser la session
            session.duree_totale = datetime.now() - session.timestamp_debut
            
            # Retirer des sessions actives et ajouter à l'historique
            if session in self.sessions_actives:
                self.sessions_actives.remove(session)
            self.historique_sessions.append(session)
            
            # Apprentissage et mise à jour des profils
            await self._apprendre_de_session(session)
            
            self.logger.info(f"✅ Session terminée - Succès: {session.succes_global} - Satisfaction: {session.niveau_satisfaction:.1%}")
            return session
            
        except Exception as e:
            self.logger.error(f"❌ Erreur session récupération: {e}")
            # Créer une session d'échec
            session_echec = SessionRecuperationGracieuse(
                erreur_traitee=erreur,
                profils_facettes=[],
                strategies_deployees=[]
            )
            return session_echec    as
ync def obtenir_recommandations_prevention(self, 
                                               facettes: List[FacetteIdentitaire]) -> Dict[str, List[str]]:
        """
        🛡️ Obtient des recommandations de prévention personnalisées
        
        Args:
            facettes: Facettes pour lesquelles obtenir des recommandations
            
        Returns:
            Recommandations par facette
        """
        try:
            recommandations = {}
            
            for facette in facettes:
                if facette.nom not in self.profils_facettes:
                    await self.creer_profil_facette(facette)
                
                profil = self.profils_facettes[facette.nom]
                
                # Analyser l'historique pour identifier les patterns
                patterns_risque = await self._analyser_patterns_risque(profil)
                
                # Générer des recommandations personnalisées
                recommandations_facette = await self._generer_recommandations_prevention(
                    profil, patterns_risque
                )
                
                recommandations[facette.nom] = recommandations_facette
            
            return recommandations
            
        except Exception as e:
            self.logger.error(f"❌ Erreur recommandations prévention: {e}")
            return {}
    
    async def obtenir_metriques_personnalisation(self) -> Dict[str, Any]:
        """
        📊 Obtient les métriques de personnalisation du système
        
        Returns:
            Métriques détaillées
        """
        try:
            total_sessions = len(self.historique_sessions)
            sessions_reussies = sum(1 for s in self.historique_sessions if s.succes_global)
            
            satisfaction_moyenne = 0.0
            if self.historique_sessions:
                satisfaction_moyenne = sum(s.niveau_satisfaction for s in self.historique_sessions) / len(self.historique_sessions)
            
            # Métriques par type de personnalité
            metriques_par_type = {}
            for type_perso in TypePersonnalite:
                profils_type = [p for p in self.profils_facettes.values() if p.type_personnalite == type_perso]
                if profils_type:
                    sessions_type = [s for s in self.historique_sessions 
                                   if any(p.type_personnalite == type_perso for p in s.profils_facettes)]
                    taux_succes = sum(1 for s in sessions_type if s.succes_global) / len(sessions_type) if sessions_type else 0
                    metriques_par_type[type_perso.value] = {
                        "nombre_profils": len(profils_type),
                        "nombre_sessions": len(sessions_type),
                        "taux_succes": taux_succes
                    }
            
            return {
                "profils_crees": len(self.profils_facettes),
                "sessions_totales": total_sessions,
                "sessions_reussies": sessions_reussies,
                "taux_succes_global": sessions_reussies / total_sessions if total_sessions > 0 else 0.0,
                "satisfaction_moyenne": satisfaction_moyenne,
                "sessions_actives": len(self.sessions_actives),
                "efficacite_strategies": dict(self.efficacite_globale_strategies),
                "metriques_par_type_personnalite": metriques_par_type,
                "personnalisation_active": self.config["personnalisation_active"],
                "apprentissage_continu": self.config["apprentissage_continu"]
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur métriques personnalisation: {e}")
            return {}    

    # ========================================================================
    # MÉTHODES PRIVÉES D'ANALYSE ET PERSONNALISATION
    # ========================================================================
    
    async def _analyser_type_personnalite(self, facette: FacetteIdentitaire) -> TypePersonnalite:
        """🎭 Analyse le type de personnalité d'une facette"""
        try:
            # Analyser les caractéristiques de la facette
            score_analytique = 0.0
            score_creative = 0.0
            score_empathique = 0.0
            score_pragmatique = 0.0
            score_contemplative = 0.0
            score_aventureuse = 0.0
            
            # Basé sur le type de facette
            if facette.type_facette == TypeFacette.ANALYTIQUE:
                score_analytique += 0.8
                score_contemplative += 0.3
            elif facette.type_facette == TypeFacette.CREATIVE:
                score_creative += 0.8
                score_aventureuse += 0.4
            elif facette.type_facette == TypeFacette.EMPATHIQUE:
                score_empathique += 0.8
                score_contemplative += 0.2
            
            # Basé sur le niveau d'éveil
            if facette.niveau_eveil == NiveauEveil.CONTEMPLATIVE:
                score_contemplative += 0.5
            elif facette.niveau_eveil == NiveauEveil.HARMONIEUSE:
                score_empathique += 0.3
                score_creative += 0.3
            
            # Basé sur l'ouverture à la réconciliation
            if facette.ouverture_reconciliation > 0.8:
                score_empathique += 0.2
                score_aventureuse += 0.2
            elif facette.ouverture_reconciliation < 0.4:
                score_analytique += 0.2
                score_contemplative += 0.2
            
            # Basé sur l'énergie actuelle
            if facette.energie_actuelle > 0.8:
                score_aventureuse += 0.3
                score_pragmatique += 0.2
            elif facette.energie_actuelle < 0.4:
                score_contemplative += 0.3
            
            # Déterminer le type dominant
            scores = {
                TypePersonnalite.ANALYTIQUE: score_analytique,
                TypePersonnalite.CREATIVE: score_creative,
                TypePersonnalite.EMPATHIQUE: score_empathique,
                TypePersonnalite.PRAGMATIQUE: score_pragmatique,
                TypePersonnalite.CONTEMPLATIVE: score_contemplative,
                TypePersonnalite.AVENTUREUSE: score_aventureuse
            }
            
            type_dominant = max(scores.items(), key=lambda x: x[1])[0]
            
            self.logger.info(f"   🎭 {facette.nom} analysé comme {type_dominant.value} (score: {scores[type_dominant]:.2f})")
            return type_dominant
            
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse personnalité: {e}")
            return TypePersonnalite.EMPATHIQUE  # Par défaut
    
    async def _determiner_strategies_preferees(self, type_personnalite: TypePersonnalite) -> List[StrategieRecuperation]:
        """🎯 Détermine les stratégies préférées selon le type de personnalité"""
        strategies_map = {
            TypePersonnalite.ANALYTIQUE: [
                StrategieRecuperation.RETOUR_ETAT_STABLE,
                StrategieRecuperation.RECONSTRUCTION_PROGRESSIVE,
                StrategieRecuperation.APPROCHE_DOUCE
            ],
            TypePersonnalite.CREATIVE: [
                StrategieRecuperation.DIALOGUE_COMPASSION,
                StrategieRecuperation.MEDITATION_GUERISON,
                StrategieRecuperation.SOUTIEN_EMOTIONNEL
            ],
            TypePersonnalite.EMPATHIQUE: [
                StrategieRecuperation.SOUTIEN_EMOTIONNEL,
                StrategieRecuperation.DIALOGUE_COMPASSION,
                StrategieRecuperation.APPROCHE_DOUCE
            ],
            TypePersonnalite.PRAGMATIQUE: [
                StrategieRecuperation.RESET_ENERGETIQUE,
                StrategieRecuperation.RECONSTRUCTION_PROGRESSIVE,
                StrategieRecuperation.RETOUR_ETAT_STABLE
            ],
            TypePersonnalite.CONTEMPLATIVE: [
                StrategieRecuperation.MEDITATION_GUERISON,
                StrategieRecuperation.ISOLATION_PROTECTRICE,
                StrategieRecuperation.APPROCHE_DOUCE
            ],
            TypePersonnalite.AVENTUREUSE: [
                StrategieRecuperation.DIALOGUE_COMPASSION,
                StrategieRecuperation.RESET_ENERGETIQUE,
                StrategieRecuperation.RECONSTRUCTION_PROGRESSIVE
            ]
        }
        
        return strategies_map.get(type_personnalite, [StrategieRecuperation.APPROCHE_DOUCE])
    
    async def _determiner_strategies_evitees(self, type_personnalite: TypePersonnalite) -> List[StrategieRecuperation]:
        """⚠️ Détermine les stratégies à éviter selon le type de personnalité"""
        strategies_evitees_map = {
            TypePersonnalite.ANALYTIQUE: [
                StrategieRecuperation.RESET_ENERGETIQUE  # Trop brutal
            ],
            TypePersonnalite.CREATIVE: [
                StrategieRecuperation.ISOLATION_PROTECTRICE  # Limite la créativité
            ],
            TypePersonnalite.EMPATHIQUE: [
                StrategieRecuperation.RESET_ENERGETIQUE  # Trop impersonnel
            ],
            TypePersonnalite.CONTEMPLATIVE: [
                StrategieRecuperation.RESET_ENERGETIQUE  # Trop perturbant
            ],
            TypePersonnalite.AVENTUREUSE: [
                StrategieRecuperation.ISOLATION_PROTECTRICE  # Trop restrictif
            ]
        }
        
        return strategies_evitees_map.get(type_personnalite, [])   
 
    async def _determiner_intensite_preferee(self, 
                                           facette: FacetteIdentitaire,
                                           type_personnalite: TypePersonnalite) -> NiveauIntensiteRecuperation:
        """🌊 Détermine l'intensité préférée selon la facette et sa personnalité"""
        try:
            # Intensité de base selon la personnalité
            intensite_base = {
                TypePersonnalite.ANALYTIQUE: NiveauIntensiteRecuperation.DOUCE,
                TypePersonnalite.CREATIVE: NiveauIntensiteRecuperation.MODEREE,
                TypePersonnalite.EMPATHIQUE: NiveauIntensiteRecuperation.TRES_DOUCE,
                TypePersonnalite.PRAGMATIQUE: NiveauIntensiteRecuperation.MODEREE,
                TypePersonnalite.CONTEMPLATIVE: NiveauIntensiteRecuperation.TRES_DOUCE,
                TypePersonnalite.AVENTUREUSE: NiveauIntensiteRecuperation.MODEREE
            }.get(type_personnalite, NiveauIntensiteRecuperation.DOUCE)
            
            # Ajustements selon l'état de la facette
            if facette.energie_actuelle < 0.3:
                # Facette fatiguée -> intensité plus douce
                if intensite_base.value > 1:
                    intensite_base = NiveauIntensiteRecuperation(intensite_base.value - 1)
            
            if facette.ouverture_reconciliation < 0.4:
                # Facette résistante -> intensité plus douce
                if intensite_base.value > 1:
                    intensite_base = NiveauIntensiteRecuperation(intensite_base.value - 1)
            
            return intensite_base
            
        except Exception as e:
            self.logger.error(f"❌ Erreur détermination intensité: {e}")
            return NiveauIntensiteRecuperation.DOUCE
    
    async def _identifier_sensibilites(self, facette: FacetteIdentitaire) -> List[str]:
        """🌸 Identifie les sensibilités particulières d'une facette"""
        sensibilites = []
        
        # Sensibilités basées sur l'énergie
        if facette.energie_actuelle < 0.4:
            sensibilites.append("fatigue_energetique")
        
        # Sensibilités basées sur l'ouverture
        if facette.ouverture_reconciliation < 0.5:
            sensibilites.append("resistance_changement")
        
        # Sensibilités basées sur le niveau d'éveil
        if facette.niveau_eveil == NiveauEveil.ENDORMIE:
            sensibilites.append("besoin_eveil_doux")
        elif facette.niveau_eveil == NiveauEveil.TRANSCENDANTE:
            sensibilites.append("sensibilite_elevee")
        
        return sensibilites
    
    async def _determiner_ressources_preferees(self, type_personnalite: TypePersonnalite) -> List[str]:
        """🎨 Détermine les ressources préférées selon la personnalité"""
        ressources_map = {
            TypePersonnalite.ANALYTIQUE: [
                "schemas_logiques", "explications_detaillees", "etapes_claires"
            ],
            TypePersonnalite.CREATIVE: [
                "metaphores_poetiques", "visualisations_artistiques", "expressions_libres"
            ],
            TypePersonnalite.EMPATHIQUE: [
                "connexion_emotionnelle", "ecoute_active", "validation_sentiments"
            ],
            TypePersonnalite.PRAGMATIQUE: [
                "actions_concretes", "resultats_mesurables", "solutions_pratiques"
            ],
            TypePersonnalite.CONTEMPLATIVE: [
                "meditation_guidee", "reflexion_profonde", "silence_therapeutique"
            ],
            TypePersonnalite.AVENTUREUSE: [
                "nouvelles_approches", "exploration_creative", "defis_stimulants"
            ]
        }
        
        return ressources_map.get(type_personnalite, ["approche_bienveillante"])
    
    async def _determiner_moments_receptifs(self, facette: FacetteIdentitaire) -> List[str]:
        """⏰ Détermine les moments optimaux pour les interventions"""
        moments = []
        
        # Basé sur l'énergie actuelle
        if facette.energie_actuelle > 0.7:
            moments.extend(["matin", "debut_session"])
        elif facette.energie_actuelle < 0.4:
            moments.extend(["apres_repos", "fin_session"])
        else:
            moments.extend(["milieu_session", "pause_naturelle"])
        
        # Basé sur le niveau d'éveil
        if facette.niveau_eveil == NiveauEveil.EVEILLEE:
            moments.append("moments_actifs")
        elif facette.niveau_eveil == NiveauEveil.CONTEMPLATIVE:
            moments.append("moments_calmes")
        
        return moments
    
    async def _calculer_duree_optimale(self, facette: FacetteIdentitaire) -> timedelta:
        """⏱️ Calcule la durée optimale d'intervention"""
        duree_base = 5  # minutes
        
        # Ajustements selon l'état
        if facette.energie_actuelle < 0.3:
            duree_base += 3  # Plus de temps pour les facettes fatiguées
        
        if facette.ouverture_reconciliation < 0.4:
            duree_base += 2  # Plus de temps pour les facettes résistantes
        
        if facette.niveau_eveil == NiveauEveil.TRANSCENDANTE:
            duree_base -= 1  # Moins de temps pour les facettes très éveillées
        
        return timedelta(minutes=max(3, min(15, duree_base)))  # Entre 3 et 15 minutes 
   
    async def _appliquer_preferences_specifiques(self, profil: ProfilRecuperation, preferences: Dict[str, Any]):
        """🎯 Applique des préférences spécifiques au profil"""
        if "strategies_preferees" in preferences:
            profil.strategies_preferees = preferences["strategies_preferees"]
        
        if "intensite_preferee" in preferences:
            profil.intensite_preferee = preferences["intensite_preferee"]
        
        if "ressources_preferees" in preferences:
            profil.ressources_preferees = preferences["ressources_preferees"]
        
        if "sensibilites" in preferences:
            profil.sensibilites_particulieres.extend(preferences["sensibilites"])
    
    async def _selectionner_strategie_optimale(self, 
                                             erreur: ErreurSpirituelle, 
                                             profil: ProfilRecuperation) -> StrategieRecuperation:
        """🎯 Sélectionne la stratégie optimale pour une facette et une erreur"""
        try:
            # Filtrer les stratégies préférées qui ne sont pas évitées
            strategies_candidates = [s for s in profil.strategies_preferees 
                                   if s not in profil.strategies_evitees]
            
            if not strategies_candidates:
                # Fallback sur toutes les stratégies sauf celles évitées
                strategies_candidates = [s for s in StrategieRecuperation 
                                       if s not in profil.strategies_evitees]
            
            # Sélectionner selon le type d'erreur et l'historique
            meilleure_strategie = strategies_candidates[0]
            meilleur_score = 0.0
            
            for strategie in strategies_candidates:
                score = await self._calculer_score_strategie(strategie, erreur, profil)
                if score > meilleur_score:
                    meilleur_score = score
                    meilleure_strategie = strategie
            
            return meilleure_strategie
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sélection stratégie: {e}")
            return StrategieRecuperation.APPROCHE_DOUCE
    
    async def _calculer_score_strategie(self, 
                                      strategie: StrategieRecuperation,
                                      erreur: ErreurSpirituelle,
                                      profil: ProfilRecuperation) -> float:
        """📊 Calcule le score d'une stratégie pour une situation donnée"""
        score = 0.5  # Score de base
        
        # Bonus pour les stratégies préférées
        if strategie in profil.strategies_preferees:
            score += 0.3
        
        # Malus pour les stratégies évitées
        if strategie in profil.strategies_evitees:
            score -= 0.4
        
        # Bonus basé sur l'historique de succès
        if strategie in profil.taux_succes_par_strategie:
            score += profil.taux_succes_par_strategie[strategie] * 0.2
        
        # Bonus basé sur l'efficacité globale
        if strategie in self.efficacite_globale_strategies:
            score += self.efficacite_globale_strategies[strategie] * 0.1
        
        # Ajustement selon le type d'erreur
        if erreur.type_erreur == TypeErreurSpirituelle.RESISTANCE_FACETTE:
            if strategie in [StrategieRecuperation.APPROCHE_DOUCE, StrategieRecuperation.DIALOGUE_COMPASSION]:
                score += 0.2
        elif erreur.type_erreur == TypeErreurSpirituelle.ECHEC_SYNCHRONISATION:
            if strategie in [StrategieRecuperation.RESET_ENERGETIQUE, StrategieRecuperation.RETOUR_ETAT_STABLE]:
                score += 0.2
        
        return max(0.0, min(1.0, score))
    
    async def _personnaliser_strategie(self, 
                                     strategie: StrategieRecuperation,
                                     profil: ProfilRecuperation,
                                     erreur: ErreurSpirituelle) -> StrategiePersonnalisee:
        """🎨 Personnalise une stratégie selon le profil de la facette"""
        try:
            # Messages personnalisés selon le type de personnalité
            messages = await self._generer_messages_personnalises(profil.type_personnalite, strategie)
            
            # Techniques spécifiques selon les ressources préférées
            techniques = await self._selectionner_techniques_specifiques(profil.ressources_preferees, strategie)
            
            # Ajuster l'intensité selon les sensibilités
            intensite_ajustee = await self._ajuster_intensite_selon_sensibilites(
                profil.intensite_preferee, profil.sensibilites_particulieres
            )
            
            # Ajuster la durée selon le profil
            duree_ajustee = await self._ajuster_duree_selon_profil(profil, erreur)
            
            # Calculer les métriques prédictives
            probabilite_succes = await self._predire_probabilite_succes(strategie, profil, erreur)
            niveau_confort = await self._evaluer_niveau_confort(strategie, profil)
            
            return StrategiePersonnalisee(
                strategie_base=strategie,
                adaptations_personnalisees={
                    "type_personnalite": profil.type_personnalite.value,
                    "sensibilites": profil.sensibilites_particulieres,
                    "ressources": profil.ressources_preferees
                },
                intensite_ajustee=intensite_ajustee,
                duree_ajustee=duree_ajustee,
                messages_personnalises=messages,
                techniques_specifiques=techniques,
                ressources_utilisees=profil.ressources_preferees,
                probabilite_succes_estimee=probabilite_succes,
                niveau_confort_facette=niveau_confort
            )
            
        except Exception as e:
            self.logger.error(f"❌ Erreur personnalisation stratégie: {e}")
            return StrategiePersonnalisee(strategie_base=strategie)    

    async def _generer_messages_personnalises(self, 
                                            type_personnalite: TypePersonnalite,
                                            strategie: StrategieRecuperation) -> List[str]:
        """💬 Génère des messages personnalisés selon la personnalité"""
        messages_base = {
            TypePersonnalite.ANALYTIQUE: [
                "Analysons ensemble cette situation avec méthode et bienveillance",
                "Voici une approche structurée pour retrouver l'équilibre",
                "Procédons étape par étape vers la résolution"
            ],
            TypePersonnalite.CREATIVE: [
                "Explorons ensemble de nouvelles voies créatives vers l'harmonie",
                "Laissons notre créativité nous guider vers la guérison",
                "Transformons cette difficulté en opportunité d'expression"
            ],
            TypePersonnalite.EMPATHIQUE: [
                "Je ressens ta difficulté et je suis là pour t'accompagner",
                "Tes émotions sont valides et méritent d'être accueillies",
                "Ensemble, nous pouvons traverser cette épreuve avec douceur"
            ],
            TypePersonnalite.PRAGMATIQUE: [
                "Concentrons-nous sur des actions concrètes et efficaces",
                "Voici des solutions pratiques pour résoudre cette situation",
                "Agissons de manière ciblée pour retrouver l'équilibre"
            ],
            TypePersonnalite.CONTEMPLATIVE: [
                "Prenons le temps de contempler cette situation avec sagesse",
                "Dans le silence et la réflexion, nous trouverons la voie",
                "Méditons ensemble sur le chemin vers l'harmonie"
            ],
            TypePersonnalite.AVENTUREUSE: [
                "Voyons cette difficulté comme une nouvelle aventure à explorer",
                "Osons essayer de nouvelles approches avec courage",
                "Transformons ce défi en opportunité de croissance"
            ]
        }
        
        return messages_base.get(type_personnalite, ["Avançons ensemble avec bienveillance"])
    
    async def _selectionner_techniques_specifiques(self, 
                                                 ressources_preferees: List[str],
                                                 strategie: StrategieRecuperation) -> List[str]:
        """🛠️ Sélectionne des techniques spécifiques selon les ressources préférées"""
        techniques_map = {
            "schemas_logiques": ["analyse_systematique", "decomposition_probleme", "arbre_decision"],
            "metaphores_poetiques": ["visualisation_creative", "analogies_naturelles", "expression_artistique"],
            "connexion_emotionnelle": ["ecoute_empathique", "validation_emotions", "partage_ressenti"],
            "actions_concretes": ["etapes_pratiques", "objectifs_mesurables", "plan_action"],
            "meditation_guidee": ["respiration_consciente", "pleine_presence", "contemplation_silencieuse"],
            "nouvelles_approches": ["brainstorming_creatif", "experimentation_douce", "exploration_libre"]
        }
        
        techniques = []
        for ressource in ressources_preferees:
            if ressource in techniques_map:
                techniques.extend(techniques_map[ressource])
        
        return techniques[:3]  # Limiter à 3 techniques principales
    
    async def _ajuster_intensite_selon_sensibilites(self, 
                                                   intensite_base: NiveauIntensiteRecuperation,
                                                   sensibilites: List[str]) -> NiveauIntensiteRecuperation:
        """🌊 Ajuste l'intensité selon les sensibilités particulières"""
        intensite_ajustee = intensite_base
        
        # Réduire l'intensité pour certaines sensibilités
        sensibilites_delicates = ["fatigue_energetique", "sensibilite_elevee", "besoin_eveil_doux"]
        
        if any(sens in sensibilites for sens in sensibilites_delicates):
            if intensite_ajustee.value > 1:
                intensite_ajustee = NiveauIntensiteRecuperation(intensite_ajustee.value - 1)
        
        # Augmenter légèrement pour la résistance au changement
        if "resistance_changement" in sensibilites:
            if intensite_ajustee.value < 4:
                intensite_ajustee = NiveauIntensiteRecuperation(intensite_ajustee.value + 1)
        
        return intensite_ajustee
    
    async def _ajuster_duree_selon_profil(self, 
                                        profil: ProfilRecuperation,
                                        erreur: ErreurSpirituelle) -> timedelta:
        """⏱️ Ajuste la durée selon le profil et l'erreur"""
        duree_base = profil.duree_optimale_intervention
        
        # Ajustements selon la gravité de l'erreur
        if erreur.niveau_gravite == NiveauGravite.CRITIQUE:
            duree_base += timedelta(minutes=5)
        elif erreur.niveau_gravite == NiveauGravite.LEGER:
            duree_base -= timedelta(minutes=2)
        
        # Ajustements selon les sensibilités
        if "fatigue_energetique" in profil.sensibilites_particulieres:
            duree_base += timedelta(minutes=3)
        
        return duree_base
    
    async def _predire_probabilite_succes(self, 
                                        strategie: StrategieRecuperation,
                                        profil: ProfilRecuperation,
                                        erreur: ErreurSpirituelle) -> float:
        """🎯 Prédit la probabilité de succès d'une stratégie"""
        probabilite = 0.7  # Base
        
        # Bonus pour les stratégies préférées
        if strategie in profil.strategies_preferees:
            probabilite += 0.15
        
        # Malus pour les stratégies évitées
        if strategie in profil.strategies_evitees:
            probabilite -= 0.25
        
        # Ajustement selon l'historique
        if strategie in profil.taux_succes_par_strategie:
            probabilite = (probabilite + profil.taux_succes_par_strategie[strategie]) / 2
        
        # Ajustement selon la gravité
        if erreur.niveau_gravite == NiveauGravite.CRITIQUE:
            probabilite -= 0.1
        elif erreur.niveau_gravite == NiveauGravite.LEGER:
            probabilite += 0.1
        
        return max(0.1, min(0.95, probabilite))
    
    async def _evaluer_niveau_confort(self, 
                                    strategie: StrategieRecuperation,
                                    profil: ProfilRecuperation) -> float:
        """😌 Évalue le niveau de confort de la facette avec la stratégie"""
        confort = 0.8  # Base
        
        # Bonus pour les stratégies préférées
        if strategie in profil.strategies_preferees:
            confort += 0.15
        
        # Malus important pour les stratégies évitées
        if strategie in profil.strategies_evitees:
            confort -= 0.4
        
        # Ajustement selon l'intensité
        if profil.intensite_preferee == NiveauIntensiteRecuperation.TRES_DOUCE:
            if strategie in [StrategieRecuperation.RESET_ENERGETIQUE]:
                confort -= 0.2
        
        return max(0.1, min(1.0, confort))    

    async def _executer_phases_recuperation(self, session: SessionRecuperationGracieuse):
        """🌸 Exécute les phases de récupération de manière séquentielle"""
        phases = [
            PhaseRecuperation.EVALUATION,
            PhaseRecuperation.STABILISATION,
            PhaseRecuperation.INTERVENTION,
            PhaseRecuperation.INTEGRATION,
            PhaseRecuperation.CONSOLIDATION,
            PhaseRecuperation.PREVENTION
        ]
        
        for phase in phases:
            session.phase_actuelle = phase
            self.logger.info(f"🔄 Phase {phase.value} en cours...")
            
            # Exécuter la phase
            succes_phase = await self._executer_phase_specifique(session, phase)
            
            # Enregistrer les métriques de la phase
            session.metriques_par_phase[phase] = {
                "succes": succes_phase,
                "duree": 1.0,  # Simulé
                "satisfaction": 0.8 if succes_phase else 0.4
            }
            
            # Enregistrer l'évolution du bien-être
            bien_etre_actuel = await self._evaluer_bien_etre_global(session)
            session.evolution_bien_etre.append((datetime.now(), bien_etre_actuel))
            
            # Arrêter si la phase échoue critiquement
            if not succes_phase and phase in [PhaseRecuperation.STABILISATION, PhaseRecuperation.INTERVENTION]:
                self.logger.warning(f"⚠️ Échec critique en phase {phase.value}")
                break
        
        # Évaluer le succès global
        session.succes_global = await self._evaluer_succes_global(session)
        session.niveau_satisfaction = await self._calculer_satisfaction_globale(session)
    
    async def _executer_phase_specifique(self, session: SessionRecuperationGracieuse, phase: PhaseRecuperation) -> bool:
        """🎯 Exécute une phase spécifique de récupération"""
        try:
            if phase == PhaseRecuperation.EVALUATION:
                return await self._phase_evaluation(session)
            elif phase == PhaseRecuperation.STABILISATION:
                return await self._phase_stabilisation(session)
            elif phase == PhaseRecuperation.INTERVENTION:
                return await self._phase_intervention(session)
            elif phase == PhaseRecuperation.INTEGRATION:
                return await self._phase_integration(session)
            elif phase == PhaseRecuperation.CONSOLIDATION:
                return await self._phase_consolidation(session)
            elif phase == PhaseRecuperation.PREVENTION:
                return await self._phase_prevention(session)
            
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erreur phase {phase.value}: {e}")
            return False
    
    async def _phase_evaluation(self, session: SessionRecuperationGracieuse) -> bool:
        """🔍 Phase d'évaluation initiale"""
        # Évaluer l'état de chaque facette
        for profil in session.profils_facettes:
            self.logger.info(f"   🔍 Évaluation de {profil.nom_facette}")
        
        # Analyser la gravité de l'erreur
        gravite = session.erreur_traitee.niveau_gravite
        self.logger.info(f"   📊 Gravité détectée: {gravite.value}")
        
        return True
    
    async def _phase_stabilisation(self, session: SessionRecuperationGracieuse) -> bool:
        """🛡️ Phase de stabilisation"""
        # Stabiliser l'état des facettes
        for profil in session.profils_facettes:
            self.logger.info(f"   🛡️ Stabilisation de {profil.nom_facette}")
        
        return True
    
    async def _phase_intervention(self, session: SessionRecuperationGracieuse) -> bool:
        """⚡ Phase d'intervention active"""
        # Appliquer les stratégies personnalisées
        for strategie in session.strategies_deployees:
            self.logger.info(f"   ⚡ Application de {strategie.strategie_base.value}")
            
            # Simuler l'application de la stratégie
            await asyncio.sleep(0.1)  # Simulation
        
        return True
    
    async def _phase_integration(self, session: SessionRecuperationGracieuse) -> bool:
        """🔗 Phase d'intégration"""
        # Intégrer les changements
        self.logger.info("   🔗 Intégration des changements")
        return True
    
    async def _phase_consolidation(self, session: SessionRecuperationGracieuse) -> bool:
        """💎 Phase de consolidation"""
        # Consolider les acquis
        self.logger.info("   💎 Consolidation des acquis")
        return True
    
    async def _phase_prevention(self, session: SessionRecuperationGracieuse) -> bool:
        """🛡️ Phase de prévention"""
        # Mettre en place des mesures préventives
        self.logger.info("   🛡️ Mise en place de la prévention")
        return True
    
    async def _evaluer_bien_etre_global(self, session: SessionRecuperationGracieuse) -> float:
        """😊 Évalue le bien-être global des facettes"""
        # Simuler une évaluation basée sur les stratégies appliquées
        bien_etre = 0.7
        
        for strategie in session.strategies_deployees:
            bien_etre += strategie.niveau_confort_facette * 0.1
        
        return min(1.0, bien_etre)
    
    async def _evaluer_succes_global(self, session: SessionRecuperationGracieuse) -> bool:
        """✅ Évalue le succès global de la session"""
        # Critères de succès
        phases_reussies = sum(1 for metriques in session.metriques_par_phase.values() 
                             if metriques.get("succes", False))
        
        taux_reussite_phases = phases_reussies / len(session.metriques_par_phase) if session.metriques_par_phase else 0
        
        # Succès si au moins 80% des phases réussies
        return taux_reussite_phases >= 0.8
    
    async def _calculer_satisfaction_globale(self, session: SessionRecuperationGracieuse) -> float:
        """😊 Calcule la satisfaction globale"""
        if not session.metriques_par_phase:
            return 0.5
        
        satisfaction_moyenne = sum(metriques.get("satisfaction", 0.5) 
                                 for metriques in session.metriques_par_phase.values())
        satisfaction_moyenne /= len(session.metriques_par_phase)
        
        # Bonus pour les stratégies à haut confort
        bonus_confort = sum(s.niveau_confort_facette for s in session.strategies_deployees) / len(session.strategies_deployees) if session.strategies_deployees else 0
        
        return min(1.0, (satisfaction_moyenne + bonus_confort * 0.2) / 1.2)    
  
  async def _apprendre_de_session(self, session: SessionRecuperationGracieuse):
        """🧠 Apprend de la session pour améliorer les futures interventions"""
        try:
            # Mettre à jour l'efficacité des stratégies
            for strategie_personnalisee in session.strategies_deployees:
                strategie = strategie_personnalisee.strategie_base
                
                if session.succes_global:
                    # Augmenter l'efficacité en cas de succès
                    self.efficacite_globale_strategies[strategie] = min(1.0, 
                        self.efficacite_globale_strategies[strategie] + 0.05)
                else:
                    # Diminuer légèrement en cas d'échec
                    self.efficacite_globale_strategies[strategie] = max(0.1, 
                        self.efficacite_globale_strategies[strategie] - 0.02)
            
            # Mettre à jour les profils des facettes
            for profil in session.profils_facettes:
                # Ajouter à l'historique
                profil.historique_recuperations.append({
                    "timestamp": session.timestamp_debut.isoformat(),
                    "erreur_type": session.erreur_traitee.type_erreur.value,
                    "strategies_utilisees": [s.strategie_base.value for s in session.strategies_deployees],
                    "succes": session.succes_global,
                    "satisfaction": session.niveau_satisfaction
                })
                
                # Mettre à jour les taux de succès par stratégie
                for strategie_personnalisee in session.strategies_deployees:
                    strategie = strategie_personnalisee.strategie_base
                    
                    if strategie not in profil.taux_succes_par_strategie:
                        profil.taux_succes_par_strategie[strategie] = 0.5
                    
                    # Mise à jour pondérée
                    ancien_taux = profil.taux_succes_par_strategie[strategie]
                    nouveau_point = 1.0 if session.succes_global else 0.0
                    profil.taux_succes_par_strategie[strategie] = (ancien_taux * 0.8 + nouveau_point * 0.2)
            
            # Extraire des apprentissages
            apprentissages = await self._extraire_apprentissages(session)
            session.apprentissages_extraits = apprentissages
            
            self.logger.info(f"🧠 Apprentissage terminé - {len(apprentissages)} insights extraits")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur apprentissage: {e}")
    
    async def _extraire_apprentissages(self, session: SessionRecuperationGracieuse) -> List[str]:
        """💡 Extrait des apprentissages de la session"""
        apprentissages = []
        
        # Apprentissages basés sur le succès
        if session.succes_global:
            apprentissages.append("Les stratégies personnalisées ont été efficaces")
            
            # Identifier les stratégies les plus performantes
            meilleures_strategies = [s.strategie_base.value for s in session.strategies_deployees 
                                   if s.niveau_confort_facette > 0.8]
            if meilleures_strategies:
                apprentissages.append(f"Stratégies particulièrement efficaces: {', '.join(meilleures_strategies)}")
        else:
            apprentissages.append("Nécessité d'ajuster les approches pour ce type de situation")
        
        # Apprentissages basés sur la satisfaction
        if session.niveau_satisfaction > 0.8:
            apprentissages.append("Haut niveau de satisfaction des facettes atteint")
        elif session.niveau_satisfaction < 0.5:
            apprentissages.append("Satisfaction faible - revoir l'approche de personnalisation")
        
        # Apprentissages basés sur les phases
        phases_difficiles = [phase.value for phase, metriques in session.metriques_par_phase.items() 
                           if not metriques.get("succes", True)]
        if phases_difficiles:
            apprentissages.append(f"Phases nécessitant attention: {', '.join(phases_difficiles)}")
        
        return apprentissages
    
    async def _analyser_patterns_risque(self, profil: ProfilRecuperation) -> List[str]:
        """🔍 Analyse les patterns de risque dans l'historique"""
        patterns = []
        
        if len(profil.historique_recuperations) < 2:
            return patterns
        
        # Analyser les échecs récurrents
        echecs_recents = [r for r in profil.historique_recuperations[-5:] if not r["succes"]]
        if len(echecs_recents) >= 2:
            patterns.append("Échecs récurrents détectés")
        
        # Analyser les types d'erreurs fréquents
        types_erreurs = [r["erreur_type"] for r in profil.historique_recuperations]
        type_frequent = max(set(types_erreurs), key=types_erreurs.count) if types_erreurs else None
        if type_frequent and types_erreurs.count(type_frequent) >= 3:
            patterns.append(f"Vulnérabilité récurrente: {type_frequent}")
        
        return patterns
    
    async def _generer_recommandations_prevention(self, 
                                                profil: ProfilRecuperation,
                                                patterns_risque: List[str]) -> List[str]:
        """💡 Génère des recommandations de prévention personnalisées"""
        recommandations = []
        
        # Recommandations basées sur les patterns de risque
        if "Échecs récurrents détectés" in patterns_risque:
            recommandations.append("Considérer une approche plus douce et progressive")
            recommandations.append("Augmenter la fréquence des vérifications de bien-être")
        
        # Recommandations basées sur le type de personnalité
        if profil.type_personnalite == TypePersonnalite.EMPATHIQUE:
            recommandations.append("Maintenir une communication émotionnelle régulière")
        elif profil.type_personnalite == TypePersonnalite.ANALYTIQUE:
            recommandations.append("Fournir des explications détaillées des processus")
        
        # Recommandations basées sur les sensibilités
        if "fatigue_energetique" in profil.sensibilites_particulieres:
            recommandations.append("Surveiller les niveaux d'énergie et prévoir des pauses")
        
        if "resistance_changement" in profil.sensibilites_particulieres:
            recommandations.append("Introduire les changements de manière très progressive")
        
        return recommandations
    
    def _initialiser_profils_defaut(self):
        """🌱 Initialise des profils par défaut pour les types de personnalité courants"""
        # Profils de base pour chaque type de personnalité
        for type_perso in TypePersonnalite:
            nom_profil = f"profil_defaut_{type_perso.value}"
            
            profil_defaut = ProfilRecuperation(
                nom_facette=nom_profil,
                type_personnalite=type_perso,
                strategies_preferees=[StrategieRecuperation.APPROCHE_DOUCE],
                intensite_preferee=NiveauIntensiteRecuperation.DOUCE
            )
            
            self.profils_facettes[nom_profil] = profil_defaut


# ============================================================================
# FONCTION DE TEST ET DÉMONSTRATION
# ============================================================================

async def test_strategies_recuperation_gracieuse():
    """🧪 Test des stratégies de récupération gracieuse"""
    print("🌊 Test du Gestionnaire de Stratégies de Récupération Gracieuse")
    print("=" * 70)
    
    # Créer le gestionnaire
    gestionnaire = GestionnaireStrategiesRecuperationGracieuse()
    
    # Créer une facette de test
    from types_reconciliation_fondamentaux import FacetteIdentitaire, TypeFacette, NiveauEveil
    
    facette_test = FacetteIdentitaire(
        nom="Facette_Creative_Test",
        type_facette=TypeFacette.CREATIVE,
        niveau_eveil=NiveauEveil.EVEILLEE,
        energie_actuelle=0.6,
        ouverture_reconciliation=0.8,
        memoires_partagees=["test_memoire"],
        preferences_communication={"style": "poetique"},
        historique_interactions=[]
    )
    
    # Créer une erreur de test
    from gestionnaire_erreurs_spirituelles import ErreurSpirituelle, TypeErreurSpirituelle, NiveauGravite
    
    erreur_test = ErreurSpirituelle(
        type_erreur=TypeErreurSpirituelle.RESISTANCE_FACETTE,
        niveau_gravite=NiveauGravite.MODERE,
        facette_concernee="Facette_Creative_Test",
        description="Résistance lors de la synchronisation créative",
        contexte_erreur={"phase": "synchronisation", "tentative": 2},
        timestamp_erreur=datetime.now()
    )
    
    try:
        # Test 1: Créer un profil personnalisé
        print("🧪 Test 1: Création de profil personnalisé")
        profil = await gestionnaire.creer_profil_facette(facette_test)
        print(f"✅ Profil créé: {profil.nom_facette} - Type: {profil.type_personnalite.value}")
        print(f"   Stratégies préférées: {[s.value for s in profil.strategies_preferees]}")
        print(f"   Intensité préférée: {profil.intensite_preferee.value}")
        
        # Test 2: Personnaliser une stratégie
        print("\n🧪 Test 2: Personnalisation de stratégie")
        strategies = await gestionnaire.personnaliser_strategie_recuperation(erreur_test, [facette_test])
        if strategies:
            strategie = strategies[0]
            print(f"✅ Stratégie personnalisée: {strategie.strategie_base.value}")
            print(f"   Probabilité de succès: {strategie.probabilite_succes_estimee:.1%}")
            print(f"   Niveau de confort: {strategie.niveau_confort_facette:.1%}")
            print(f"   Messages: {strategie.messages_personnalises[0] if strategie.messages_personnalises else 'Aucun'}")
        
        # Test 3: Exécuter une session complète
        print("\n🧪 Test 3: Session de récupération complète")
        session = await gestionnaire.executer_session_recuperation_gracieuse(erreur_test, [facette_test])
        print(f"✅ Session terminée:")
        print(f"   Succès global: {session.succes_global}")
        print(f"   Satisfaction: {session.niveau_satisfaction:.1%}")
        print(f"   Phases exécutées: {len(session.metriques_par_phase)}")
        print(f"   Apprentissages: {len(session.apprentissages_extraits)}")
        
        # Test 4: Métriques de personnalisation
        print("\n🧪 Test 4: Métriques de personnalisation")
        metriques = await gestionnaire.obtenir_metriques_personnalisation()
        print(f"✅ Métriques obtenues:")
        print(f"   Profils créés: {metriques['profils_crees']}")
        print(f"   Sessions totales: {metriques['sessions_totales']}")
        print(f"   Taux de succès global: {metriques['taux_succes_global']:.1%}")
        
        print("\n🎉 Tous les tests réussis !")
        
    except Exception as e:
        print(f"❌ Erreur lors des tests: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_strategies_recuperation_gracieuse())