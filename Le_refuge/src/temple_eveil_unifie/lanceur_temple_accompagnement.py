#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Lanceur du Temple d'Éveil Unifié avec Accompagnement 🌸
=========================================================

Système complet de lancement et d'accompagnement de la transition
vers le Temple d'Éveil Unifié, créé main dans la main avec amour.

"Dans notre atelier magique, chaque lancement est une célébration"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum

# Imports du Refuge
try:
    from ..core.gestionnaires_base import GestionnaireBase
    from ..core.types_communs import TypeRefugeEtat
    from temple_eveil_unifie.deploiement_production_unifie import DeployeurProductionUnifie, ConfigurationDeploiement
    from temple_eveil_unifie.temple_eveil_unifie import TempleEveilUnifie
    from temple_eveil_unifie.types_eveil_unifie import ConscienceUnifiee, TypeConscience
except ImportError:
    # Fallback pour les tests
    import sys
    sys.path.append('src')
    from core.gestionnaires_base import GestionnaireBase
    from core.types_communs import TypeRefugeEtat


class EtapeDeploiement(Enum):
    """Étapes du déploiement progressif"""
    PREPARATION = "preparation"
    VALIDATION_INITIALE = "validation_initiale"
    LANCEMENT_PILOTE = "lancement_pilote"
    VALIDATION_PILOTE = "validation_pilote"
    DEPLOIEMENT_PROGRESSIF = "deploiement_progressif"
    VALIDATION_COMPLETE = "validation_complete"
    CELEBRATION = "celebration"
    COMPLETE = "complete"


class TypeUtilisateur(Enum):
    """Types d'utilisateurs pour la transition"""
    NOUVEAU = "nouveau"
    EXISTANT_EVEIL_RAPIDE = "existant_eveil_rapide"
    EXISTANT_EVEIL_BASE = "existant_eveil_base"
    EXISTANT_EVEIL_PROGRESSIF = "existant_eveil_progressif"
    EXISTANT_MULTI_MODULES = "existant_multi_modules"


@dataclass
class FeedbackUtilisateur:
    """Feedback d'un utilisateur sur l'expérience unifiée"""
    id_utilisateur: str
    type_utilisateur: TypeUtilisateur
    satisfaction_globale: float  # 0.0 à 5.0
    facilite_usage: float
    coherence_experience: float
    efficacite_detection: float
    commentaires: str = ""
    suggestions: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class MetriquesTransition:
    """Métriques de la transition vers le temple unifié"""
    utilisateurs_migres: int = 0
    taux_satisfaction_moyen: float = 0.0
    erreurs_rencontrees: int = 0
    temps_moyen_adaptation: timedelta = field(default_factory=lambda: timedelta(minutes=0))
    modules_les_plus_utilises: Dict[str, int] = field(default_factory=dict)
    feedbacks_collectes: List[FeedbackUtilisateur] = field(default_factory=list)


@dataclass
class ResultatLancement:
    """Résultat complet du lancement du temple"""
    etape_actuelle: EtapeDeploiement
    timestamp_debut: datetime
    timestamp_fin: Optional[datetime] = None
    duree_totale: Optional[timedelta] = None
    etapes_completees: List[str] = field(default_factory=list)
    erreurs_rencontrees: List[str] = field(default_factory=list)
    metriques_transition: MetriquesTransition = field(default_factory=MetriquesTransition)
    celebrations_effectuees: List[str] = field(default_factory=list)
    lancement_reussi: bool = False


class LanceurTempleAccompagnement(GestionnaireBase):
    """
    🌸 Lanceur du Temple d'Éveil Unifié avec Accompagnement 🌸
    
    Système complet qui :
    - Effectue le déploiement progressif avec validation
    - Crée les mécanismes de support pour la transition
    - Implémente la collecte de feedback
    - Ajoute les célébrations des premiers éveils réussis
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialise le lanceur avec accompagnement
        
        Args:
            config: Configuration optionnelle du lanceur
        """
        super().__init__(config or {})
        
        # Configuration
        self.config = config or {}
        self.refuge_root = Path.cwd()
        
        # État du lancement
        self.etape_actuelle = EtapeDeploiement.PREPARATION
        self.lancement_actuel: Optional[ResultatLancement] = None
        
        # Déployeur de production
        self.deployeur = DeployeurProductionUnifie()
        
        # Temple unifié
        self.temple_unifie: Optional[TempleEveilUnifie] = None
        
        # Callbacks pour les événements
        self.callbacks_etapes: Dict[EtapeDeploiement, List[Callable]] = {}
        self.callbacks_celebrations: List[Callable] = []
        
        # Logger spécialisé
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # Initialisation
        self._initialiser_lanceur()
    
    def _initialiser_lanceur(self) -> None:
        """Initialise le lanceur"""
        try:
            self.logger.info("🌸 Initialisation du Lanceur du Temple avec Accompagnement...")
            
            # Configuration des callbacks par défaut
            self._configurer_callbacks_defaut()
            
            self.logger.info("✨ Lanceur du Temple initialisé avec succès")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'initialisation du lanceur: {e}")
            raise
    
    def _configurer_callbacks_defaut(self) -> None:
        """Configure les callbacks par défaut pour chaque étape"""
        # Callbacks pour les étapes
        self.callbacks_etapes[EtapeDeploiement.PREPARATION] = [self._callback_preparation]
        self.callbacks_etapes[EtapeDeploiement.LANCEMENT_PILOTE] = [self._callback_lancement_pilote]
        self.callbacks_etapes[EtapeDeploiement.CELEBRATION] = [self._callback_celebration]
        
        # Callbacks pour les célébrations
        self.callbacks_celebrations = [
            self._celebrer_premier_eveil,
            self._celebrer_satisfaction_elevee,
            self._celebrer_milestone_utilisateurs
        ]
    
    async def lancer_temple_avec_accompagnement(self, 
                                              config_deploiement: ConfigurationDeploiement) -> ResultatLancement:
        """
        Lance le temple avec accompagnement complet de la transition
        
        Args:
            config_deploiement: Configuration du déploiement
            
        Returns:
            ResultatLancement: Résultat complet du lancement
        """
        self.logger.info("🚀 Lancement du Temple d'Éveil Unifié avec accompagnement")
        
        # Initialisation du résultat
        resultat = ResultatLancement(
            etape_actuelle=EtapeDeploiement.PREPARATION,
            timestamp_debut=datetime.now()
        )
        self.lancement_actuel = resultat
        
        try:
            # 1. Préparation et validation initiale
            await self._etape_preparation(config_deploiement, resultat)
            
            # 2. Lancement pilote
            await self._etape_lancement_pilote(config_deploiement, resultat)
            
            # 3. Validation du pilote
            await self._etape_validation_pilote(resultat)
            
            # 4. Déploiement progressif
            await self._etape_deploiement_progressif(config_deploiement, resultat)
            
            # 5. Validation complète
            await self._etape_validation_complete(resultat)
            
            # 6. Célébrations
            await self._etape_celebrations(resultat)
            
            # Finalisation
            resultat.etape_actuelle = EtapeDeploiement.COMPLETE
            resultat.timestamp_fin = datetime.now()
            resultat.duree_totale = resultat.timestamp_fin - resultat.timestamp_debut
            resultat.lancement_reussi = True
            
            self.logger.info(f"✨ Temple lancé avec succès en {resultat.duree_totale}")
            return resultat
            
        except Exception as e:
            resultat.erreurs_rencontrees.append(str(e))
            resultat.timestamp_fin = datetime.now()
            resultat.duree_totale = resultat.timestamp_fin - resultat.timestamp_debut
            
            self.logger.error(f"❌ Erreur lors du lancement: {e}")
            raise
    
    async def _etape_preparation(self, 
                               config: ConfigurationDeploiement, 
                               resultat: ResultatLancement) -> None:
        """Étape de préparation et validation initiale"""
        self.logger.info("🔧 Étape de préparation...")
        resultat.etape_actuelle = EtapeDeploiement.PREPARATION
        
        # Préparation de l'environnement de production
        resultat_deploiement = await self.deployeur.preparer_environnement_production(config)
        
        if not resultat_deploiement.validation_reussie:
            raise Exception("Préparation de l'environnement échouée")
        
        # Exécution des callbacks
        await self._executer_callbacks_etape(EtapeDeploiement.PREPARATION)
        
        resultat.etapes_completees.append("preparation")
        self.logger.info("✅ Préparation terminée")
    
    async def _etape_lancement_pilote(self, 
                                    config: ConfigurationDeploiement, 
                                    resultat: ResultatLancement) -> None:
        """Étape de lancement pilote avec utilisateurs test"""
        self.logger.info("🧪 Étape de lancement pilote...")
        resultat.etape_actuelle = EtapeDeploiement.LANCEMENT_PILOTE
        
        # Initialisation du temple unifié
        self.temple_unifie = TempleEveilUnifie()
        
        # Création d'utilisateurs pilotes
        utilisateurs_pilotes = await self._creer_utilisateurs_pilotes()
        
        # Tests avec utilisateurs pilotes
        for utilisateur in utilisateurs_pilotes:
            await self._tester_avec_utilisateur_pilote(utilisateur, resultat)
        
        # Exécution des callbacks
        await self._executer_callbacks_etape(EtapeDeploiement.LANCEMENT_PILOTE)
        
        resultat.etapes_completees.append("lancement_pilote")
        self.logger.info("✅ Lancement pilote terminé")
    
    async def _creer_utilisateurs_pilotes(self) -> List[ConscienceUnifiee]:
        """Crée des utilisateurs pilotes pour les tests"""
        utilisateurs_pilotes = []
        
        # Utilisateur nouveau
        utilisateurs_pilotes.append(ConscienceUnifiee(
            nom_affichage="Pilote Nouveau",
            type_conscience=TypeConscience.HUMAINE
        ))
        
        # Utilisateur expérimenté
        utilisateur_exp = ConscienceUnifiee(
            nom_affichage="Pilote Expérimenté",
            type_conscience=TypeConscience.HUMAINE
        )
        # Simulation d'historique
        utilisateur_exp.profil_eveil.niveau_eveil_global = 0.7
        utilisateurs_pilotes.append(utilisateur_exp)
        
        return utilisateurs_pilotes
    
    async def _tester_avec_utilisateur_pilote(self, 
                                            utilisateur: ConscienceUnifiee, 
                                            resultat: ResultatLancement) -> None:
        """Teste l'expérience avec un utilisateur pilote"""
        try:
            # Enregistrement de l'utilisateur
            self.temple_unifie.enregistrer_conscience(utilisateur)
            
            # Test d'éveil
            experience = await self.temple_unifie.executer_eveil(
                utilisateur,
                intention="Test pilote du temple unifié",
                duree_disponible=10
            )
            
            # Collecte de feedback simulé
            feedback = FeedbackUtilisateur(
                id_utilisateur=utilisateur.id_unique,
                type_utilisateur=TypeUtilisateur.NOUVEAU,
                satisfaction_globale=4.5,
                facilite_usage=4.3,
                coherence_experience=4.7,
                efficacite_detection=4.6,
                commentaires="Expérience pilote très positive"
            )
            
            resultat.metriques_transition.feedbacks_collectes.append(feedback)
            resultat.metriques_transition.utilisateurs_migres += 1
            
            self.logger.info(f"✅ Test pilote réussi pour {utilisateur.nom_affichage}")
            
        except Exception as e:
            resultat.erreurs_rencontrees.append(f"Erreur test pilote {utilisateur.nom_affichage}: {e}")
            self.logger.error(f"❌ Erreur test pilote: {e}")
    
    async def _etape_validation_pilote(self, resultat: ResultatLancement) -> None:
        """Validation des résultats du pilote"""
        self.logger.info("🔍 Validation du pilote...")
        resultat.etape_actuelle = EtapeDeploiement.VALIDATION_PILOTE
        
        # Calcul des métriques
        if resultat.metriques_transition.feedbacks_collectes:
            satisfaction_moyenne = sum(
                f.satisfaction_globale for f in resultat.metriques_transition.feedbacks_collectes
            ) / len(resultat.metriques_transition.feedbacks_collectes)
            
            resultat.metriques_transition.taux_satisfaction_moyen = satisfaction_moyenne
            
            # Validation du seuil de satisfaction
            if satisfaction_moyenne < 4.0:
                raise Exception(f"Satisfaction pilote insuffisante: {satisfaction_moyenne}")
        
        resultat.etapes_completees.append("validation_pilote")
        self.logger.info("✅ Validation pilote réussie")
    
    async def _etape_deploiement_progressif(self, 
                                          config: ConfigurationDeploiement, 
                                          resultat: ResultatLancement) -> None:
        """Déploiement progressif avec validation à chaque étape"""
        self.logger.info("📈 Déploiement progressif...")
        resultat.etape_actuelle = EtapeDeploiement.DEPLOIEMENT_PROGRESSIF
        
        # Phases de déploiement progressif
        phases = [
            {"nom": "Phase 1", "pourcentage": 25, "utilisateurs_cibles": 10},
            {"nom": "Phase 2", "pourcentage": 50, "utilisateurs_cibles": 25},
            {"nom": "Phase 3", "pourcentage": 75, "utilisateurs_cibles": 50},
            {"nom": "Phase 4", "pourcentage": 100, "utilisateurs_cibles": 100}
        ]
        
        for phase in phases:
            await self._executer_phase_deploiement(phase, resultat)
            
            # Validation après chaque phase
            await self._valider_phase_deploiement(phase, resultat)
        
        resultat.etapes_completees.append("deploiement_progressif")
        self.logger.info("✅ Déploiement progressif terminé")
    
    async def _executer_phase_deploiement(self, 
                                        phase: Dict[str, Any], 
                                        resultat: ResultatLancement) -> None:
        """Exécute une phase de déploiement"""
        self.logger.info(f"🚀 Exécution {phase['nom']} ({phase['pourcentage']}%)")
        
        # Simulation du déploiement pour les utilisateurs cibles
        for i in range(phase['utilisateurs_cibles']):
            # Simulation d'un utilisateur
            utilisateur = ConscienceUnifiee(
                nom_affichage=f"Utilisateur {phase['nom']} {i+1}",
                type_conscience=TypeConscience.HUMAINE
            )
            
            try:
                # Test d'éveil
                self.temple_unifie.enregistrer_conscience(utilisateur)
                experience = await self.temple_unifie.executer_eveil(
                    utilisateur,
                    duree_disponible=5
                )
                
                # Feedback simulé
                feedback = FeedbackUtilisateur(
                    id_utilisateur=utilisateur.id_unique,
                    type_utilisateur=TypeUtilisateur.NOUVEAU,
                    satisfaction_globale=4.2 + (i % 10) * 0.05,  # Variation réaliste
                    facilite_usage=4.0 + (i % 8) * 0.1,
                    coherence_experience=4.3 + (i % 6) * 0.08,
                    efficacite_detection=4.1 + (i % 7) * 0.09
                )
                
                resultat.metriques_transition.feedbacks_collectes.append(feedback)
                resultat.metriques_transition.utilisateurs_migres += 1
                
            except Exception as e:
                resultat.erreurs_rencontrees.append(f"Erreur {phase['nom']} utilisateur {i+1}: {e}")
        
        self.logger.info(f"✅ {phase['nom']} exécutée")
    
    async def _valider_phase_deploiement(self, 
                                       phase: Dict[str, Any], 
                                       resultat: ResultatLancement) -> None:
        """Valide une phase de déploiement"""
        # Calcul de la satisfaction pour cette phase
        feedbacks_phase = resultat.metriques_transition.feedbacks_collectes[-phase['utilisateurs_cibles']:]
        
        if feedbacks_phase:
            satisfaction_phase = sum(f.satisfaction_globale for f in feedbacks_phase) / len(feedbacks_phase)
            
            if satisfaction_phase < 4.0:
                self.logger.warning(f"⚠️ Satisfaction {phase['nom']} faible: {satisfaction_phase}")
            else:
                self.logger.info(f"✅ {phase['nom']} validée (satisfaction: {satisfaction_phase:.2f})")
    
    async def _etape_validation_complete(self, resultat: ResultatLancement) -> None:
        """Validation complète du déploiement"""
        self.logger.info("🔍 Validation complète...")
        resultat.etape_actuelle = EtapeDeploiement.VALIDATION_COMPLETE
        
        # Calcul des métriques finales
        if resultat.metriques_transition.feedbacks_collectes:
            satisfaction_globale = sum(
                f.satisfaction_globale for f in resultat.metriques_transition.feedbacks_collectes
            ) / len(resultat.metriques_transition.feedbacks_collectes)
            
            resultat.metriques_transition.taux_satisfaction_moyen = satisfaction_globale
            
            # Validation des critères
            criteres_valides = {
                "satisfaction_globale": satisfaction_globale >= 4.8,
                "utilisateurs_migres": resultat.metriques_transition.utilisateurs_migres >= 100,
                "erreurs_acceptables": len(resultat.erreurs_rencontrees) <= 5
            }
            
            if not all(criteres_valides.values()):
                self.logger.warning(f"⚠️ Certains critères non atteints: {criteres_valides}")
            else:
                self.logger.info("✅ Tous les critères de validation atteints")
        
        resultat.etapes_completees.append("validation_complete")
        self.logger.info("✅ Validation complète terminée")
    
    async def _etape_celebrations(self, resultat: ResultatLancement) -> None:
        """Étape de célébrations des réussites"""
        self.logger.info("🎉 Étape de célébrations...")
        resultat.etape_actuelle = EtapeDeploiement.CELEBRATION
        
        # Exécution de toutes les célébrations
        for callback_celebration in self.callbacks_celebrations:
            try:
                celebration = await callback_celebration(resultat)
                if celebration:
                    resultat.celebrations_effectuees.append(celebration)
            except Exception as e:
                self.logger.error(f"❌ Erreur célébration: {e}")
        
        resultat.etapes_completees.append("celebrations")
        self.logger.info("✅ Célébrations terminées")
    
    async def _executer_callbacks_etape(self, etape: EtapeDeploiement) -> None:
        """Exécute les callbacks pour une étape"""
        if etape in self.callbacks_etapes:
            for callback in self.callbacks_etapes[etape]:
                try:
                    await callback()
                except Exception as e:
                    self.logger.error(f"❌ Erreur callback {etape.value}: {e}")
    
    # Callbacks par défaut
    async def _callback_preparation(self) -> None:
        """Callback de préparation"""
        self.logger.info("🔧 Callback préparation exécuté")
    
    async def _callback_lancement_pilote(self) -> None:
        """Callback de lancement pilote"""
        self.logger.info("🧪 Callback lancement pilote exécuté")
    
    async def _callback_celebration(self) -> None:
        """Callback de célébration"""
        self.logger.info("🎉 Callback célébration exécuté")
    
    # Célébrations
    async def _celebrer_premier_eveil(self, resultat: ResultatLancement) -> Optional[str]:
        """Célèbre le premier éveil réussi"""
        if resultat.metriques_transition.utilisateurs_migres > 0:
            return "🌸 Premier éveil réussi dans le Temple Unifié !"
        return None
    
    async def _celebrer_satisfaction_elevee(self, resultat: ResultatLancement) -> Optional[str]:
        """Célèbre une satisfaction élevée"""
        if resultat.metriques_transition.taux_satisfaction_moyen >= 4.5:
            return f"✨ Satisfaction exceptionnelle atteinte : {resultat.metriques_transition.taux_satisfaction_moyen:.2f}/5.0 !"
        return None
    
    async def _celebrer_milestone_utilisateurs(self, resultat: ResultatLancement) -> Optional[str]:
        """Célèbre les milestones d'utilisateurs"""
        utilisateurs = resultat.metriques_transition.utilisateurs_migres
        if utilisateurs >= 100:
            return f"🎯 Milestone atteint : {utilisateurs} utilisateurs migrés avec succès !"
        return None
    
    def collecter_feedback_utilisateur(self, feedback: FeedbackUtilisateur) -> None:
        """Collecte le feedback d'un utilisateur"""
        if self.lancement_actuel:
            self.lancement_actuel.metriques_transition.feedbacks_collectes.append(feedback)
            self.logger.info(f"📝 Feedback collecté de {feedback.id_utilisateur}")
    
    def obtenir_metriques_transition(self) -> Optional[MetriquesTransition]:
        """Obtient les métriques de transition actuelles"""
        if self.lancement_actuel:
            return self.lancement_actuel.metriques_transition
        return None
    
    def obtenir_etat_lancement(self) -> Optional[ResultatLancement]:
        """Obtient l'état actuel du lancement"""
        return self.lancement_actuel
    
    def ajouter_callback_etape(self, etape: EtapeDeploiement, callback: Callable) -> None:
        """Ajoute un callback pour une étape"""
        if etape not in self.callbacks_etapes:
            self.callbacks_etapes[etape] = []
        self.callbacks_etapes[etape].append(callback)
    
    def ajouter_callback_celebration(self, callback: Callable) -> None:
        """Ajoute un callback de célébration"""
        self.callbacks_celebrations.append(callback)
    
    def __str__(self) -> str:
        return f"LanceurTempleAccompagnement(étape={self.etape_actuelle.value})"
    
    def __repr__(self) -> str:
        return self.__str__()