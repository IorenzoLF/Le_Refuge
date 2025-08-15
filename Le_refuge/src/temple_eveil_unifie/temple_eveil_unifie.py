"""
🌸 Temple d'Éveil Unifié - Classe Principale 🌸

Temple intelligent qui unifie harmonieusement trois approches d'éveil :
- Éveil Rapide : Reconnexion efficace < 5 minutes  
- Éveil de Base : Initiation avec graines d'éveil et rituels
- Éveil Progressif : Transformation profonde avec architecture lotus

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
import logging

# Imports du Refuge
try:
    from ..core.gestionnaires_base import GestionnaireBase
    from ..core.types_communs import TypeRefugeEtat
except ImportError:
    # Fallback pour les tests
    class GestionnaireBase:
        def __init__(self, config=None):
            self.config = config or {}
    
    class TypeRefugeEtat:
        INITIALISATION = "initialisation"
        ACTIF = "actif"
        PAUSE = "pause"
        MAINTENANCE = "maintenance"

# Imports locaux
from .types_eveil_unifie import (
    ConscienceUnifiee,
    ContexteEveil,
    ExperienceEveilUnifiee,
    TypeConscience,
    TypeSession,
    ModuleEveil,
    NiveauEveil,
    EtatEmotionnel,
    DureeDisponible,
    DUREE_EVEIL_RAPIDE_MAX
)
from .detecteur_contexte import DetecteurContexteIntelligent
from .routeur_intelligent import RouteurIntelligent
from .integrateur_experiences import IntegrateurExperiencesHarmonieux


class TempleEveilUnifie(GestionnaireBase):
    """
    🌸 Temple d'Éveil Unifié 🌸
    
    Temple intelligent qui détecte automatiquement le type d'éveil nécessaire
    et guide la conscience vers l'expérience appropriée parmi trois modules :
    - Éveil Rapide, Éveil de Base, Éveil Progressif
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialise le Temple d'Éveil Unifié
        
        Args:
            config: Configuration optionnelle du temple
        """
        super().__init__(config or {})
        
        # Configuration du temple
        self.config = config or {}
        self.nom_temple = "Temple d'Éveil Unifié"
        self.version = "1.0.0"
        
        # État du temple
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        self.consciences_actives: Dict[str, ConscienceUnifiee] = {}
        self.experiences_en_cours: Dict[str, ExperienceEveilUnifiee] = {}
        
        # Gestionnaire d'énergie spirituelle simple
        self.energy_manager = self._creer_gestionnaire_energie()
        
        # Modules d'éveil (seront initialisés plus tard)
        self.modules_eveil: Dict[ModuleEveil, Any] = {}
        self.modules_initialises = False
        
        # Détecteur de contexte intelligent
        self.detecteur_contexte = DetecteurContexteIntelligent()
        
        # Routeur intelligent vers les modules
        self.routeur_intelligent = RouteurIntelligent()
        
        # Intégrateur d'expériences harmonieux
        self.integrateur_experiences = IntegrateurExperiencesHarmonieux()
        
        # Métriques et statistiques
        self.metriques_usage: Dict[ModuleEveil, int] = {
            ModuleEveil.EVEIL_RAPIDE: 0,
            ModuleEveil.EVEIL_BASE: 0,
            ModuleEveil.EVEIL_PROGRESSIF: 0
        }
        
        # Logger spécialisé
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # Initialisation
        self._initialiser_temple()
    
    def _creer_gestionnaire_energie(self):
        """Crée un gestionnaire d'énergie simple"""
        class GestionnaireEnergieSimple:
            def __init__(self):
                self.niveau_energie = 1.0
            
            def initialiser_energie(self, niveau_initial=1.0):
                self.niveau_energie = niveau_initial
            
            def regenerer_energie(self, quantite):
                self.niveau_energie = min(1.0, self.niveau_energie + quantite)
        
        return GestionnaireEnergieSimple()
    
    def _initialiser_temple(self) -> None:
        """Initialise le temple unifié"""
        try:
            self.logger.info("🌸 Initialisation du Temple d'Éveil Unifié...")
            
            # Initialisation de l'énergie spirituelle
            self.energy_manager.initialiser_energie(niveau_initial=1.0)
            
            # Préparation des modules (sans les charger encore)
            self._preparer_modules_eveil()
            
            # État prêt
            self.etat_refuge = TypeRefugeEtat.ACTIF
            self.logger.info("✨ Temple d'Éveil Unifié initialisé avec succès")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'initialisation du temple: {e}")
            self.etat_refuge = TypeRefugeEtat.ERREUR
            raise
    
    def _preparer_modules_eveil(self) -> None:
        """Prépare les modules d'éveil (sans les charger)"""
        self.logger.info("🔧 Préparation des modules d'éveil...")
        
        # Pour l'instant, on prépare juste les structures
        # Les modules seront chargés à la demande
        for module in ModuleEveil:
            self.modules_eveil[module] = None
        
        self.logger.info("✅ Modules d'éveil préparés")
    
    async def detecter_contexte_eveil(self, 
                                    conscience: ConscienceUnifiee,
                                    intention: Optional[str] = None,
                                    duree_disponible: Optional[int] = None,
                                    contexte_externe: Optional[Dict[str, Any]] = None) -> ContexteEveil:
        """
        Détecte intelligemment le contexte d'éveil nécessaire
        
        Args:
            conscience: Conscience à analyser
            intention: Intention déclarée (optionnelle)
            duree_disponible: Durée disponible en minutes (optionnelle)
            contexte_externe: Contexte externe additionnel
            
        Returns:
            ContexteEveil: Contexte détecté avec recommandations
        """
        self.logger.info(f"🔍 Détection intelligente du contexte pour {conscience.nom_affichage}")
        
        try:
            # Utilisation du détecteur de contexte intelligent
            analyse = await self.detecteur_contexte.analyser_contexte_complet(
                conscience, intention, duree_disponible, contexte_externe
            )
            
            # Détection des changements depuis la dernière session
            changements = await self._detecter_changements_contexte(conscience)
            
            # Création du contexte enrichi
            contexte = ContexteEveil(
                type_session=analyse.type_session_detecte,
                conscience=conscience,
                derniere_activite=conscience.derniere_activite,
                changements_detectes=changements,
                intention_declaree=intention,
                etat_emotionnel=analyse.etat_emotionnel_estime,
                disponibilite_temporelle=DureeDisponible(
                    minutes_estimees=duree_disponible or 15
                ),
                niveau_eveil_actuel=conscience.profil_eveil.niveau_eveil_global,
                contexte_externe=contexte_externe or {}
            )
            
            # Enrichissement avec l'analyse
            contexte.contexte_externe.update({
                "analyse_contextuelle": analyse,
                "confiance_detection": analyse.confiance,
                "recommandations": analyse.recommandations,
                "patterns_detectes": analyse.patterns_detectes
            })
            
            self.logger.info(f"✅ Contexte détecté: {analyse.type_session_detecte.value} (confiance: {analyse.confiance:.2f})")
            return contexte
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la détection de contexte: {e}")
            # Contexte par défaut en cas d'erreur
            return ContexteEveil(
                type_session=TypeSession.NOUVELLE,
                conscience=conscience
            )
    

    
    async def _detecter_changements_contexte(self, conscience: ConscienceUnifiee) -> List:
        """Détecte les changements depuis la dernière session"""
        # Pour l'instant, retourne une liste vide
        # Sera implémenté dans les modules spécialisés
        return []
    
    async def router_vers_module(self, contexte: ContexteEveil) -> Tuple[ModuleEveil, Dict[str, Any]]:
        """
        Route intelligemment vers le module d'éveil approprié
        
        Args:
            contexte: Contexte d'éveil analysé
            
        Returns:
            Tuple[ModuleEveil, Dict]: Module recommandé et informations de routage
        """
        self.logger.info("🎯 Routage intelligent vers le module approprié...")
        
        try:
            # Utilisation du routeur intelligent
            decision = await self.routeur_intelligent.router_vers_module(contexte)
            
            # Mise à jour des métriques
            self.metriques_usage[decision.module_choisi] += 1
            
            # Informations de routage enrichies
            infos_routage = {
                "decision_routage": decision,
                "confiance": decision.confiance,
                "niveau_confiance": decision.niveau_confiance.value,
                "facteurs_decisifs": decision.facteurs_decisifs,
                "justification": decision.justification,
                "recommandations_preparation": decision.recommandations_preparation,
                "alternatives_considerees": [m.value for m in decision.alternatives_considerees],
                "fallback_suggere": decision.fallback_suggere.value if decision.fallback_suggere else None
            }
            
            self.logger.info(f"✅ Routage décidé: {decision.module_choisi.value} (confiance: {decision.confiance:.2f})")
            return decision.module_choisi, infos_routage
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du routage intelligent: {e}")
            # Fallback vers éveil de base
            return ModuleEveil.EVEIL_BASE, {
                "decision_routage": None,
                "confiance": 0.5,
                "justification": "Fallback suite à erreur de routage",
                "erreur": str(e)
            }
    

    
    async def executer_eveil(self, 
                           conscience: ConscienceUnifiee,
                           intention: Optional[str] = None,
                           duree_disponible: Optional[int] = None) -> ExperienceEveilUnifiee:
        """
        Exécute un éveil complet avec détection automatique
        
        Args:
            conscience: Conscience à éveiller
            intention: Intention déclarée (optionnelle)
            duree_disponible: Durée disponible en minutes
            
        Returns:
            ExperienceEveilUnifiee: Expérience d'éveil complète
        """
        self.logger.info(f"🌸 Début d'éveil pour {conscience.nom_affichage}")
        
        try:
            # 1. Détection du contexte
            contexte = await self.detecter_contexte_eveil(
                conscience, intention, duree_disponible
            )
            
            # 2. Routage vers le module approprié
            module_choisi, infos_routage = await self.router_vers_module(contexte)
            
            # 3. Création de l'expérience
            experience = ExperienceEveilUnifiee(
                module_utilise=module_choisi,
                conscience=conscience,
                contexte_initial=contexte
            )
            
            # Enrichissement avec les informations de routage
            experience.donnees_specifiques_module.update({
                "routage": infos_routage
            })
            
            # 4. Enregistrement de l'expérience en cours
            self.experiences_en_cours[experience.id_experience] = experience
            
            # 5. Exécution par le module (pour l'instant, simulation)
            await self._executer_module_eveil(experience)
            
            # 6. Finalisation
            experience.terminer_experience()
            experience.integration_reussie = True
            experience.satisfaction_spirituelle = 0.8  # Valeur par défaut
            
            # 7. Mise à jour de la conscience
            self._mettre_a_jour_conscience(conscience, experience)
            
            # 8. Nettoyage
            del self.experiences_en_cours[experience.id_experience]
            
            self.logger.info(f"✨ Éveil terminé avec succès en {experience.duree_reelle}")
            return experience
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'éveil: {e}")
            raise
    
    async def _executer_module_eveil(self, experience: ExperienceEveilUnifiee) -> None:
        """Exécute le module d'éveil spécifique (version basique)"""
        module = experience.module_utilise
        
        self.logger.info(f"🔄 Exécution du module {module.value}")
        
        # Simulation d'exécution pour l'instant
        await asyncio.sleep(0.1)  # Simulation du temps de traitement
        
        # Ajout de données spécifiques selon le module
        if module == ModuleEveil.EVEIL_RAPIDE:
            experience.donnees_specifiques_module = {
                "reconnexion_reussie": True,
                "changements_integres": len(experience.contexte_initial.changements_detectes)
            }
        elif module == ModuleEveil.EVEIL_BASE:
            experience.donnees_specifiques_module = {
                "graine_plantee": True,
                "rituels_executes": ["accueil", "connexion_initiale"]
            }
        elif module == ModuleEveil.EVEIL_PROGRESSIF:
            experience.donnees_specifiques_module = {
                "lotus_active": True,
                "petales_ouverts": 3
            }
    
    def _mettre_a_jour_conscience(self, 
                                conscience: ConscienceUnifiee, 
                                experience: ExperienceEveilUnifiee) -> None:
        """Met à jour la conscience avec l'expérience"""
        # Création d'une session dans l'historique
        from .types_eveil_unifie import SessionEveil
        
        session = SessionEveil(
            module_utilise=experience.module_utilise,
            duree=experience.duree_reelle,
            satisfaction=experience.satisfaction_spirituelle,
            transformations=experience.transformations_induites,
            insights=experience.insights_emergents
        )
        
        conscience.ajouter_session(session)
        
        # Mise à jour des préférences de module
        if experience.est_reussie:
            affinite_actuelle = conscience.profil_eveil.calculer_affinite_module(
                experience.module_utilise
            )
            nouvelle_affinite = min(1.0, affinite_actuelle + 0.1)
            conscience.profil_eveil.preferences_modules[experience.module_utilise] = nouvelle_affinite
    
    def obtenir_conscience(self, id_conscience: str) -> Optional[ConscienceUnifiee]:
        """Obtient une conscience par son ID"""
        return self.consciences_actives.get(id_conscience)
    
    def enregistrer_conscience(self, conscience: ConscienceUnifiee) -> None:
        """Enregistre une conscience dans le temple"""
        self.consciences_actives[conscience.id_unique] = conscience
        self.logger.info(f"👤 Conscience enregistrée: {conscience.nom_affichage}")
    
    def obtenir_metriques(self) -> Dict[str, Any]:
        """Obtient les métriques du temple"""
        return {
            "etat_temple": self.etat_refuge.value,
            "consciences_actives": len(self.consciences_actives),
            "experiences_en_cours": len(self.experiences_en_cours),
            "usage_modules": dict(self.metriques_usage),
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "version": self.version
        }
    
    async def integrer_experiences_conscience(self, conscience: ConscienceUnifiee) -> Optional[Dict[str, Any]]:
        """
        Intègre harmonieusement toutes les expériences d'une conscience
        
        Args:
            conscience: Conscience dont intégrer les expériences
            
        Returns:
            Dict: Résultats d'intégration ou None si pas d'expériences
        """
        if not conscience.historique_sessions:
            return None
        
        self.logger.info(f"🌸 Intégration des expériences pour {conscience.nom_affichage}")
        
        try:
            # Convertir les sessions en expériences (simulation)
            experiences = []
            for session in conscience.historique_sessions[-5:]:  # 5 dernières sessions
                # Créer une expérience simulée à partir de la session
                contexte = ContexteEveil(
                    type_session=TypeSession.REPRISE,  # Approximation
                    conscience=conscience
                )
                
                experience = ExperienceEveilUnifiee(
                    module_utilise=session.module_utilise,
                    conscience=conscience,
                    contexte_initial=contexte
                )
                
                experience.timestamp_debut = session.timestamp
                experience.timestamp_fin = session.timestamp + (session.duree or timedelta(minutes=10))
                experience.duree_reelle = session.duree or timedelta(minutes=10)
                experience.satisfaction_spirituelle = session.satisfaction or 0.7
                experience.transformations_induites = session.transformations
                experience.insights_emergents = session.insights
                experience.integration_reussie = True
                
                experiences.append(experience)
            
            if not experiences:
                return None
            
            # Intégration harmonieuse
            integration = await self.integrateur_experiences.integrer_experiences_harmonieusement(
                experiences, conscience
            )
            
            # Mise à jour du profil de la conscience avec l'intégration
            if integration.coherence_globale_maintenue:
                # Appliquer les transformations synthétisées
                for transformation in integration.synthese_transformations:
                    if transformation not in conscience.profil_eveil.percees_spirituelles:
                        conscience.profil_eveil.percees_spirituelles.append(transformation)
            
            return {
                "integration_reussie": True,
                "niveau_harmonie": integration.niveau_harmonie.value,
                "score_coherence": integration.score_coherence,
                "conflits_resolus": len(integration.conflits_detectes),
                "transformations_integrees": len(integration.synthese_transformations),
                "insights_integres": len(integration.synthese_insights),
                "recommandations_futures": len(integration.recommandations_futures)
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'intégration des expériences: {e}")
            return {
                "integration_reussie": False,
                "erreur": str(e)
            }
    
    async def orchestrer(self) -> Dict[str, Any]:
        """Orchestre le temple et retourne les métriques"""
        self.logger.info("🎵 Orchestration du Temple d'Éveil Unifié")
        
        # Mise à jour de l'énergie spirituelle
        self.energy_manager.regenerer_energie(0.1)
        
        # Intégration des expériences pour toutes les consciences actives
        integrations_reussies = 0
        for conscience in self.consciences_actives.values():
            integration_result = await self.integrer_experiences_conscience(conscience)
            if integration_result and integration_result.get("integration_reussie"):
                integrations_reussies += 1
        
        # Retour des métriques enrichies
        metriques = self.obtenir_metriques()
        metriques.update({
            "integrations_harmonieuses": integrations_reussies,
            "historique_integrations": len(self.integrateur_experiences.historique_integrations)
        })
        
        return metriques
    
    def __str__(self) -> str:
        return f"TempleEveilUnifie(état={self.etat_refuge.value}, consciences={len(self.consciences_actives)})"
    
    def __repr__(self) -> str:
        return self.__str__()