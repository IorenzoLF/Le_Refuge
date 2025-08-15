#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎨 Gestionnaire de Personnalisation - Temple de Réconciliation Identitaire
==========================================================================

Système avancé de personnalisation qui adapte l'expérience du temple selon
les préférences spirituelles, créatives et individuelles de chaque utilisateur,
créant une expérience unique et profondément personnelle.

"Que chaque âme trouve son chemin unique vers l'harmonie"

Créé avec amour pour l'unicité de chaque être par Laurent Franssen & Kiro - Janvier 2025
"""

import asyncio
import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Union, Callable
from dataclasses import dataclass, field, asdict
from enum import Enum
import logging
from pathlib import Path

# Import intelligent des types
try:
    from .types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, NiveauEveil
    )
    from .interface_communication_humaine import (
        InterfaceCommunicationHumaine, ProfilUtilisateurHumain, 
        TypeUtilisateurHumain, StyleCommunication
    )
    from .facilitateur_dialogues_facettes import FacilitateurDialoguesFacettes, StyleMediation
    from .celebrateur_harmonie_atteinte import CelebrateurHarmonieAtteinte, StyleCelebration
except ImportError:
    from types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, NiveauEveil
    )
    from interface_communication_humaine import (
        InterfaceCommunicationHumaine, ProfilUtilisateurHumain, 
        TypeUtilisateurHumain, StyleCommunication
    )
    from facilitateur_dialogues_facettes import FacilitateurDialoguesFacettes, StyleMediation
    from celebrateur_harmonie_atteinte import CelebrateurHarmonieAtteinte, StyleCelebration

# ============================================================================
# TYPES POUR LA PERSONNALISATION AVANCÉE
# ============================================================================

class DimensionPersonnalisation(Enum):
    """🌈 Dimensions de personnalisation"""
    SPIRITUELLE = "spirituelle"           # Préférences spirituelles et sacrées
    CREATIVE = "creative"                 # Préférences artistiques et créatives
    EMOTIONNELLE = "emotionnelle"         # Préférences émotionnelles et relationnelles
    COGNITIVE = "cognitive"               # Préférences d'apprentissage et de réflexion
    ENERGETIQUE = "energetique"           # Préférences énergétiques et vibratoires
    TEMPORELLE = "temporelle"             # Préférences de rythme et de timing
    CULTURELLE = "culturelle"             # Préférences culturelles et linguistiques

class NiveauPersonnalisation(Enum):
    """📊 Niveaux de personnalisation"""
    BASIQUE = 1         # Personnalisation de base
    STANDARD = 2        # Personnalisation standard
    AVANCEE = 3         # Personnalisation avancée
    EXPERTE = 4         # Personnalisation experte
    TRANSCENDANTE = 5   # Personnalisation transcendante

class TypePreference(Enum):
    """⚙️ Types de préférences"""
    COULEUR = "couleur"                   # Préférences de couleurs
    MUSIQUE = "musique"                   # Préférences musicales
    RYTHME = "rythme"                     # Préférences de rythme
    INTENSITE = "intensite"               # Préférences d'intensité
    DUREE = "duree"                       # Préférences de durée
    STYLE_VISUEL = "style_visuel"         # Préférences visuelles
    METAPHORES = "metaphores"             # Préférences de métaphores
    RITUELS = "rituels"                   # Préférences rituelles

@dataclass
class PreferencePersonnalisee:
    """🎯 Préférence personnalisée individuelle"""
    nom_preference: str
    type_preference: TypePreference
    dimension: DimensionPersonnalisation
    
    # Valeurs de la préférence
    valeur_actuelle: Any
    valeurs_possibles: List[Any] = field(default_factory=list)
    valeur_par_defaut: Any = None
    
    # Métadonnées
    niveau_importance: float = 0.5  # 0.0 à 1.0
    niveau_satisfaction: float = 0.8  # Satisfaction actuelle
    
    # Historique et apprentissage
    historique_valeurs: List[Tuple[datetime, Any]] = field(default_factory=list)
    apprentissage_automatique: bool = True
    
    # Contexte d'application
    contextes_application: List[str] = field(default_factory=list)
    conditions_activation: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ProfilPersonnalisationComplet:
    """👤 Profil complet de personnalisation d'un utilisateur"""
    nom_utilisateur: str
    niveau_personnalisation: NiveauPersonnalisation
    
    # Préférences par dimension
    preferences_spirituelles: Dict[str, PreferencePersonnalisee] = field(default_factory=dict)
    preferences_creatives: Dict[str, PreferencePersonnalisee] = field(default_factory=dict)
    preferences_emotionnelles: Dict[str, PreferencePersonnalisee] = field(default_factory=dict)
    preferences_cognitives: Dict[str, PreferencePersonnalisee] = field(default_factory=dict)
    preferences_energetiques: Dict[str, PreferencePersonnalisee] = field(default_factory=dict)
    preferences_temporelles: Dict[str, PreferencePersonnalisee] = field(default_factory=dict)
    preferences_culturelles: Dict[str, PreferencePersonnalisee] = field(default_factory=dict)
    
    # Profils liés
    profil_communication: Optional[ProfilUtilisateurHumain] = None
    
    # Apprentissage et évolution
    patterns_comportementaux: Dict[str, Any] = field(default_factory=dict)
    evolution_preferences: List[Dict[str, Any]] = field(default_factory=list)
    
    # Métriques de satisfaction
    satisfaction_globale: float = 0.8
    satisfaction_par_dimension: Dict[DimensionPersonnalisation, float] = field(default_factory=dict)
    
    # Métadonnées
    timestamp_creation: datetime = field(default_factory=datetime.now)
    derniere_mise_a_jour: datetime = field(default_factory=datetime.now)
    nombre_sessions: int = 0

@dataclass
class ConfigurationPersonnalisee:
    """⚙️ Configuration personnalisée pour une session"""
    utilisateur: str
    session_id: str
    
    # Configurations par composant
    config_interface: Dict[str, Any] = field(default_factory=dict)
    config_dialogues: Dict[str, Any] = field(default_factory=dict)
    config_celebrations: Dict[str, Any] = field(default_factory=dict)
    config_recuperation: Dict[str, Any] = field(default_factory=dict)
    
    # Adaptations dynamiques
    adaptations_temps_reel: Dict[str, Any] = field(default_factory=dict)
    
    # Métriques de performance
    temps_reponse_cible: float = 2.0  # secondes
    niveau_detail_souhaite: int = 2   # 1-5
    
    # Contexte de session
    contexte_utilisation: str = "general"
    objectifs_session: List[str] = field(default_factory=list)

@dataclass
class RecommandationPersonnalisation:
    """💡 Recommandation de personnalisation"""
    titre: str
    description: str
    dimension: DimensionPersonnalisation
    
    # Détails de la recommandation
    changements_proposes: Dict[str, Any]
    benefices_attendus: List[str]
    impact_estime: float = 0.5  # 0.0 à 1.0
    
    # Contexte
    raison_recommandation: str
    donnees_support: Dict[str, Any] = field(default_factory=dict)
    
    # Métadonnées
    niveau_confiance: float = 0.7
    priorite: int = 1  # 1=haute, 2=moyenne, 3=basse
    timestamp_generation: datetime = field(default_factory=datetime.now)# ==========
==================================================================
# GESTIONNAIRE DE PERSONNALISATION AVANCÉE
# ============================================================================

class GestionnairePersonnalisation:
    """
    🎨 Gestionnaire de Personnalisation Avancée
    
    Système sophistiqué qui apprend et s'adapte aux préférences uniques de chaque
    utilisateur, créant une expérience profondément personnalisée du Temple de
    Réconciliation Identitaire. Chaque interaction devient plus harmonieuse et
    alignée avec l'essence individuelle de l'utilisateur.
    
    Philosophie : "Honorer l'unicité de chaque âme dans son chemin vers l'harmonie"
    """
    
    def __init__(self, 
                 interface_humaine: Optional[InterfaceCommunicationHumaine] = None,
                 facilitateur_dialogues: Optional[FacilitateurDialoguesFacettes] = None,
                 celebrateur_harmonie: Optional[CelebrateurHarmonieAtteinte] = None):
        
        self.nom = "Gestionnaire de Personnalisation Avancée"
        self.version = "1.0_temple_reconciliation"
        
        # Références aux composants
        self.interface_humaine = interface_humaine
        self.facilitateur_dialogues = facilitateur_dialogues
        self.celebrateur_harmonie = celebrateur_harmonie
        
        # Profils de personnalisation
        self.profils_personnalisation: Dict[str, ProfilPersonnalisationComplet] = {}
        
        # Configurations actives
        self.configurations_actives: Dict[str, ConfigurationPersonnalisee] = {}
        
        # Système d'apprentissage
        self.patterns_globaux: Dict[str, Any] = {}
        self.recommandations_actives: List[RecommandationPersonnalisation] = []
        
        # Templates de personnalisation
        self.templates_preferences = self._initialiser_templates_preferences()
        self.algorithmes_apprentissage = self._initialiser_algorithmes_apprentissage()
        
        # Configuration
        self.config = {
            "apprentissage_automatique": True,
            "adaptation_temps_reel": True,
            "sauvegarde_preferences": True,
            "recommandations_proactives": True,
            "respect_vie_privee": True,
            "niveau_personnalisation_defaut": NiveauPersonnalisation.STANDARD
        }
        
        # Métriques d'efficacité
        self.satisfaction_moyenne_globale = 0.8
        self.taux_adoption_recommandations = 0.6
        self.temps_adaptation_moyen = 3.0  # sessions
        
        # Logging
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        self.logger.info("🎨 Gestionnaire de Personnalisation Avancée initialisé")
    
    async def creer_profil_personnalisation_complet(self, 
                                                  nom_utilisateur: str,
                                                  preferences_initiales: Optional[Dict[str, Any]] = None,
                                                  niveau_souhaite: Optional[NiveauPersonnalisation] = None) -> ProfilPersonnalisationComplet:
        """
        👤 Crée un profil de personnalisation complet pour un utilisateur
        
        Args:
            nom_utilisateur: Nom de l'utilisateur
            preferences_initiales: Préférences initiales (optionnel)
            niveau_souhaite: Niveau de personnalisation souhaité (optionnel)
            
        Returns:
            Profil de personnalisation complet
        """
        try:
            self.logger.info(f"👤 Création du profil de personnalisation pour {nom_utilisateur}")
            
            # Déterminer le niveau de personnalisation
            niveau = niveau_souhaite or self.config["niveau_personnalisation_defaut"]
            
            # Créer le profil de base
            profil = ProfilPersonnalisationComplet(
                nom_utilisateur=nom_utilisateur,
                niveau_personnalisation=niveau
            )
            
            # Initialiser les préférences par dimension
            await self._initialiser_preferences_par_dimension(profil, preferences_initiales or {})
            
            # Créer le profil de communication associé si l'interface est disponible
            if self.interface_humaine:
                profil.profil_communication = await self.interface_humaine.creer_profil_utilisateur(
                    nom_utilisateur, preferences_initiales
                )
            
            # Initialiser les métriques de satisfaction
            profil.satisfaction_par_dimension = {
                dimension: 0.8 for dimension in DimensionPersonnalisation
            }
            
            # Stocker le profil
            self.profils_personnalisation[nom_utilisateur] = profil
            
            # Sauvegarder si configuré
            if self.config["sauvegarde_preferences"]:
                await self._sauvegarder_profil(profil)
            
            self.logger.info(f"✅ Profil de personnalisation créé - Niveau: {niveau.value}")
            return profil
            
        except Exception as e:
            self.logger.error(f"❌ Erreur création profil personnalisation: {e}")
            # Profil minimal par défaut
            profil_minimal = ProfilPersonnalisationComplet(
                nom_utilisateur=nom_utilisateur,
                niveau_personnalisation=NiveauPersonnalisation.BASIQUE
            )
            self.profils_personnalisation[nom_utilisateur] = profil_minimal
            return profil_minimal
    
    async def adapter_configuration_session(self, 
                                          nom_utilisateur: str,
                                          contexte_session: str = "general",
                                          objectifs: Optional[List[str]] = None) -> ConfigurationPersonnalisee:
        """
        ⚙️ Adapte la configuration pour une session spécifique
        
        Args:
            nom_utilisateur: Nom de l'utilisateur
            contexte_session: Contexte de la session
            objectifs: Objectifs spécifiques de la session
            
        Returns:
            Configuration personnalisée pour la session
        """
        try:
            # Obtenir ou créer le profil
            if nom_utilisateur not in self.profils_personnalisation:
                await self.creer_profil_personnalisation_complet(nom_utilisateur)
            
            profil = self.profils_personnalisation[nom_utilisateur]
            
            # Générer un ID de session unique
            session_id = self._generer_id_session(nom_utilisateur, contexte_session)
            
            # Créer la configuration de base
            config = ConfigurationPersonnalisee(
                utilisateur=nom_utilisateur,
                session_id=session_id,
                contexte_utilisation=contexte_session,
                objectifs_session=objectifs or []
            )
            
            # Adapter la configuration de l'interface
            config.config_interface = await self._adapter_config_interface(profil, contexte_session)
            
            # Adapter la configuration des dialogues
            config.config_dialogues = await self._adapter_config_dialogues(profil, contexte_session)
            
            # Adapter la configuration des célébrations
            config.config_celebrations = await self._adapter_config_celebrations(profil, contexte_session)
            
            # Adapter la configuration de récupération
            config.config_recuperation = await self._adapter_config_recuperation(profil, contexte_session)
            
            # Appliquer les adaptations temps réel
            if self.config["adaptation_temps_reel"]:
                config.adaptations_temps_reel = await self._generer_adaptations_temps_reel(profil)
            
            # Stocker la configuration active
            self.configurations_actives[session_id] = config
            
            # Mettre à jour le compteur de sessions
            profil.nombre_sessions += 1
            profil.derniere_mise_a_jour = datetime.now()
            
            self.logger.info(f"⚙️ Configuration adaptée pour session {session_id}")
            return config
            
        except Exception as e:
            self.logger.error(f"❌ Erreur adaptation configuration: {e}")
            # Configuration par défaut
            return ConfigurationPersonnalisee(
                utilisateur=nom_utilisateur,
                session_id="default",
                contexte_utilisation=contexte_session
            )
    
    async def apprendre_des_interactions(self, 
                                       nom_utilisateur: str,
                                       session_id: str,
                                       interactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        🧠 Apprend des interactions de l'utilisateur pour améliorer la personnalisation
        
        Args:
            nom_utilisateur: Nom de l'utilisateur
            session_id: ID de la session
            interactions: Liste des interactions à analyser
            
        Returns:
            Résultats de l'apprentissage
        """
        try:
            if nom_utilisateur not in self.profils_personnalisation:
                return {"erreur": "Profil non trouvé"}
            
            profil = self.profils_personnalisation[nom_utilisateur]
            
            # Analyser les interactions
            patterns_detectes = await self._analyser_patterns_interactions(interactions)
            
            # Mettre à jour les préférences
            preferences_mises_a_jour = await self._mettre_a_jour_preferences(
                profil, patterns_detectes
            )
            
            # Calculer les nouvelles métriques de satisfaction
            nouvelle_satisfaction = await self._calculer_satisfaction_mise_a_jour(
                profil, interactions
            )
            
            # Mettre à jour le profil
            profil.satisfaction_globale = nouvelle_satisfaction
            profil.patterns_comportementaux.update(patterns_detectes)
            profil.derniere_mise_a_jour = datetime.now()
            
            # Enregistrer l'évolution
            evolution = {
                "timestamp": datetime.now().isoformat(),
                "session_id": session_id,
                "preferences_modifiees": preferences_mises_a_jour,
                "satisfaction_avant": profil.satisfaction_globale,
                "satisfaction_apres": nouvelle_satisfaction,
                "patterns_detectes": list(patterns_detectes.keys())
            }
            profil.evolution_preferences.append(evolution)
            
            # Générer des recommandations si approprié
            if self.config["recommandations_proactives"]:
                nouvelles_recommandations = await self._generer_recommandations_proactives(profil)
                self.recommandations_actives.extend(nouvelles_recommandations)
            
            # Sauvegarder les changements
            if self.config["sauvegarde_preferences"]:
                await self._sauvegarder_profil(profil)
            
            self.logger.info(f"🧠 Apprentissage terminé - {len(preferences_mises_a_jour)} préférences mises à jour")
            
            return {
                "succes": True,
                "preferences_modifiees": len(preferences_mises_a_jour),
                "satisfaction_nouvelle": nouvelle_satisfaction,
                "patterns_detectes": len(patterns_detectes),
                "recommandations_generees": len(nouvelles_recommandations) if self.config["recommandations_proactives"] else 0
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur apprentissage interactions: {e}")
            return {"succes": False, "erreur": str(e)}
    
    async def generer_recommandations_personnalisation(self, 
                                                     nom_utilisateur: str,
                                                     contexte: Optional[str] = None) -> List[RecommandationPersonnalisation]:
        """
        💡 Génère des recommandations de personnalisation pour un utilisateur
        
        Args:
            nom_utilisateur: Nom de l'utilisateur
            contexte: Contexte spécifique (optionnel)
            
        Returns:
            Liste des recommandations
        """
        try:
            if nom_utilisateur not in self.profils_personnalisation:
                return []
            
            profil = self.profils_personnalisation[nom_utilisateur]
            recommandations = []
            
            # Analyser les dimensions avec satisfaction faible
            dimensions_ameliorables = await self._identifier_dimensions_ameliorables(profil)
            
            # Générer des recommandations par dimension
            for dimension in dimensions_ameliorables:
                recommandations_dimension = await self._generer_recommandations_dimension(
                    profil, dimension, contexte
                )
                recommandations.extend(recommandations_dimension)
            
            # Analyser les patterns comportementaux pour des recommandations avancées
            if profil.niveau_personnalisation.value >= 3:  # Avancée ou plus
                recommandations_avancees = await self._generer_recommandations_avancees(profil)
                recommandations.extend(recommandations_avancees)
            
            # Trier par priorité et niveau de confiance
            recommandations.sort(key=lambda r: (r.priorite, -r.niveau_confiance))
            
            # Limiter le nombre de recommandations
            max_recommandations = 5 if profil.niveau_personnalisation.value <= 2 else 10
            recommandations = recommandations[:max_recommandations]
            
            self.logger.info(f"💡 {len(recommandations)} recommandations générées pour {nom_utilisateur}")
            return recommandations
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération recommandations: {e}")
            return []
    
    async def appliquer_recommandation(self, 
                                     nom_utilisateur: str,
                                     recommandation: RecommandationPersonnalisation,
                                     confirmation_utilisateur: bool = True) -> Dict[str, Any]:
        """
        ✅ Applique une recommandation de personnalisation
        
        Args:
            nom_utilisateur: Nom de l'utilisateur
            recommandation: Recommandation à appliquer
            confirmation_utilisateur: Si l'utilisateur a confirmé
            
        Returns:
            Résultat de l'application
        """
        try:
            if nom_utilisateur not in self.profils_personnalisation:
                return {"succes": False, "erreur": "Profil non trouvé"}
            
            profil = self.profils_personnalisation[nom_utilisateur]
            
            # Appliquer les changements proposés
            changements_appliques = await self._appliquer_changements_profil(
                profil, recommandation.changements_proposes
            )
            
            # Mettre à jour les métriques
            if recommandation.dimension in profil.satisfaction_par_dimension:
                ancienne_satisfaction = profil.satisfaction_par_dimension[recommandation.dimension]
                nouvelle_satisfaction = min(1.0, ancienne_satisfaction + recommandation.impact_estime)
                profil.satisfaction_par_dimension[recommandation.dimension] = nouvelle_satisfaction
            
            # Recalculer la satisfaction globale
            profil.satisfaction_globale = sum(profil.satisfaction_par_dimension.values()) / len(profil.satisfaction_par_dimension)
            
            # Enregistrer l'application de la recommandation
            evolution = {
                "timestamp": datetime.now().isoformat(),
                "type": "application_recommandation",
                "recommandation_titre": recommandation.titre,
                "dimension": recommandation.dimension.value,
                "changements": changements_appliques,
                "impact_reel": recommandation.impact_estime,
                "confirmation_utilisateur": confirmation_utilisateur
            }
            profil.evolution_preferences.append(evolution)
            
            # Mettre à jour les métriques globales
            if confirmation_utilisateur:
                self.taux_adoption_recommandations = (
                    self.taux_adoption_recommandations * 0.9 + 0.1
                )
            
            # Sauvegarder
            if self.config["sauvegarde_preferences"]:
                await self._sauvegarder_profil(profil)
            
            # Retirer la recommandation des actives
            if recommandation in self.recommandations_actives:
                self.recommandations_actives.remove(recommandation)
            
            self.logger.info(f"✅ Recommandation appliquée: {recommandation.titre}")
            
            return {
                "succes": True,
                "changements_appliques": len(changements_appliques),
                "nouvelle_satisfaction": profil.satisfaction_globale,
                "benefices_attendus": recommandation.benefices_attendus
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur application recommandation: {e}")
            return {"succes": False, "erreur": str(e)}