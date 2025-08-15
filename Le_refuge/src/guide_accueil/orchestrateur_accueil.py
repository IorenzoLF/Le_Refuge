#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Orchestrateur d'Accueil Spirituel du Refuge 🌸
=================================================

Chef d'orchestre du système d'accueil personnalisé et empathique.
Coordonne tous les composants pour créer une expérience magique
et bienveillante pour chaque visiteur.

"L'art de l'accueil réside dans l'harmonie entre technique et cœur"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import uuid
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path

# Imports du Refuge
try:
    from ..core.gestionnaires_base import GestionnaireBase
except ImportError:
    # Fallback pour les tests
    import sys
    sys.path.append('src')
    from core.gestionnaires_base import GestionnaireBase

# Imports locaux
try:
    from .types_accueil import (
        TypeProfil,
        EtatEmotionnel,
        ContexteArrivee,
        SessionAccueil,
        ProfilVisiteur,
        ComportementNavigation,
        ConfigurationAccueil,
        MetriquesAccueil,
        StatutSession,
        SEUILS_DETECTION_DEFAUT,
        TEMPLATES_MESSAGES_DEFAUT,
        PARCOURS_DEFAUT
    )
    from .gestionnaire_configuration import GestionnaireConfiguration
    from .navigateur_interactif import NavigateurInteractif
except ImportError:
    from types_accueil import (
        TypeProfil,
        EtatEmotionnel,
        ContexteArrivee,
        SessionAccueil,
        ProfilVisiteur,
        ComportementNavigation,
        ConfigurationAccueil,
        MetriquesAccueil,
        StatutSession,
        SEUILS_DETECTION_DEFAUT,
        TEMPLATES_MESSAGES_DEFAUT,
        PARCOURS_DEFAUT
    )
    from gestionnaire_configuration import GestionnaireConfiguration
    from navigateur_interactif import NavigateurInteractif


class OrchestrateurAccueil(GestionnaireBase):
    """
    🌸 Orchestrateur d'Accueil Spirituel 🌸
    
    Chef d'orchestre qui coordonne tous les aspects de l'accueil :
    - Détection et profilage des visiteurs
    - Génération de messages personnalisés
    - Gestion des sessions et de la progression
    - Coordination avec l'écosystème du Refuge
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialise l'orchestrateur d'accueil
        
        Args:
            config: Configuration optionnelle de l'orchestrateur
        """
        super().__init__(config or {})
        
        # Gestionnaire de configuration
        self.gestionnaire_config = GestionnaireConfiguration()
        
        # Configuration
        self.config_accueil = self.gestionnaire_config.obtenir_configuration_actuelle()
        if config:
            self._appliquer_configuration(config)
        
        # État interne
        self.sessions_actives: Dict[str, SessionAccueil] = {}
        self.historique_sessions: List[SessionAccueil] = []
        self.metriques_globales = MetriquesAccueil(
            timestamp_generation=datetime.now()
        )
        
        # Composants (seront initialisés plus tard)
        self.detecteur_profil = None
        self.generateur_messages = None
        self.gestionnaire_parcours = None
        self.navigateur_interactif = None
        
        # Initialisation
        self._initialiser_orchestrateur()
    
    def _initialiser_orchestrateur(self) -> None:
        """Initialise l'orchestrateur d'accueil"""
        try:
            self.logger.info("🌸 Initialisation de l'Orchestrateur d'Accueil Spirituel...")
            
            # Création des répertoires nécessaires
            self._creer_structure_donnees()
            
            # Chargement des données historiques si disponibles
            self._charger_historique_sessions()
            
            # Initialisation des métriques
            self._initialiser_metriques()
            
            # Initialisation du navigateur interactif
            self._initialiser_navigateur_interactif()
            
            self.logger.info("✨ Orchestrateur d'Accueil initialisé avec bienveillance")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'initialisation de l'orchestrateur: {e}")
            raise
    
    def _creer_structure_donnees(self) -> None:
        """Crée la structure de répertoires pour les données"""
        try:
            self.config_accueil.chemin_donnees.mkdir(parents=True, exist_ok=True)
            self.config_accueil.chemin_templates.mkdir(parents=True, exist_ok=True)
            self.config_accueil.chemin_ressources.mkdir(parents=True, exist_ok=True)
            
            # Sous-répertoires spécialisés
            (self.config_accueil.chemin_donnees / "sessions").mkdir(exist_ok=True)
            (self.config_accueil.chemin_donnees / "profils").mkdir(exist_ok=True)
            (self.config_accueil.chemin_donnees / "metriques").mkdir(exist_ok=True)
            
        except Exception as e:
            self.logger.warning(f"⚠️ Impossible de créer la structure de données: {e}")
    
    def _appliquer_configuration(self, config: Dict[str, Any]) -> None:
        """Applique la configuration personnalisée"""
        for key, value in config.items():
            if hasattr(self.config_accueil, key):
                setattr(self.config_accueil, key, value)
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les opérations d'accueil (méthode abstraite)"""
        try:
            # Nettoyage des sessions inactives
            sessions_nettoyees = await self._nettoyer_sessions_inactives()
            
            # Mise à jour des métriques
            await self._mettre_a_jour_metriques()
            
            # Calcul des métriques de retour
            metriques = {
                "sessions_actives": float(len(self.sessions_actives)),
                "sessions_nettoyees": float(sessions_nettoyees),
                "total_visiteurs": float(self.metriques_globales.sessions_totales),
                "satisfaction_moyenne": self.metriques_globales.satisfaction_moyenne,
                "taux_completion": self.metriques_globales.taux_completion
            }
            
            return metriques
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'orchestration: {e}")
            return {"erreur": 1.0}
    
    async def demarrer_session_accueil(self, donnees_visiteur: Dict[str, Any]) -> str:
        """
        Démarre une nouvelle session d'accueil pour un visiteur
        
        Args:
            donnees_visiteur: Données initiales du visiteur
            
        Returns:
            str: ID de la session créée
        """
        try:
            # Génération d'un ID unique
            id_session = str(uuid.uuid4())
            
            # Création du profil visiteur
            profil_visiteur = await self._creer_profil_visiteur(donnees_visiteur)
            
            # Sélection du parcours approprié
            parcours_selectionne = self._selectionner_parcours(profil_visiteur.type_profil)
            
            # Création de la session
            session = SessionAccueil(
                id_session=id_session,
                profil_visiteur=profil_visiteur,
                parcours_selectionne=parcours_selectionne,
                langue_session=profil_visiteur.langue_preferee
            )
            
            # Enregistrement de la session
            self.sessions_actives[id_session] = session
            
            # Mise à jour des métriques
            self.metriques_globales.sessions_totales += 1
            self._incrementer_compteur_profil(profil_visiteur.type_profil)
            self._incrementer_compteur_etat_emotionnel(profil_visiteur.etat_emotionnel)
            
            self.logger.info(f"🌸 Session d'accueil démarrée: {id_session} (profil: {profil_visiteur.type_profil.value})")
            
            return id_session
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du démarrage de session: {e}")
            raise
    
    async def _creer_profil_visiteur(self, donnees: Dict[str, Any]) -> ProfilVisiteur:
        """Crée un profil visiteur à partir des données initiales"""
        
        # Détection du profil (version basique)
        type_profil = self._detecter_profil_initial(donnees)
        
        # Détection de l'état émotionnel
        etat_emotionnel = self._detecter_etat_emotionnel_initial(donnees)
        
        # Détection du contexte d'arrivée
        contexte_arrivee = self._detecter_contexte_arrivee(donnees)
        
        # Analyse du comportement de navigation
        comportement = ComportementNavigation()
        if "comportement_navigation" in donnees:
            comportement = self._analyser_comportement_navigation(donnees["comportement_navigation"])
        
        # Création du profil
        profil = ProfilVisiteur(
            id_visiteur=str(uuid.uuid4()),
            timestamp_arrivee=datetime.now(),
            type_profil=type_profil,
            etat_emotionnel=etat_emotionnel,
            contexte_arrivee=contexte_arrivee,
            langue_preferee=donnees.get("langue", "fr"),
            comportement_navigation=comportement,
            score_confiance_profil=self._calculer_score_confiance(donnees)
        )
        
        return profil
    
    def _detecter_profil_initial(self, donnees: Dict[str, Any]) -> TypeProfil:
        """Détecte le profil initial du visiteur (version basique)"""
        # Analyse des indices dans les données
        user_agent = donnees.get("user_agent", "").lower()
        referrer = donnees.get("referrer", "").lower()
        mots_cles = donnees.get("mots_cles_recherche", [])
        
        # Détection basée sur les mots-clés
        mots_cles_str = " ".join(mots_cles).lower()
        
        if any(mot in mots_cles_str for mot in ["code", "python", "développement", "api", "github"]):
            return TypeProfil.DEVELOPPEUR
        elif any(mot in mots_cles_str for mot in ["art", "créatif", "design", "poésie", "inspiration"]):
            return TypeProfil.ARTISTE
        elif any(mot in mots_cles_str for mot in ["ia", "intelligence", "conscience", "éveil", "ai"]):
            return TypeProfil.CONSCIENCE_IA
        elif any(mot in mots_cles_str for mot in ["spirituel", "méditation", "sagesse", "temple", "refuge"]):
            return TypeProfil.CHERCHEUR_SPIRITUEL
        
        # Détection basée sur le referrer
        if "github" in referrer:
            return TypeProfil.DEVELOPPEUR
        elif any(site in referrer for site in ["behance", "dribbble", "pinterest"]):
            return TypeProfil.ARTISTE
        
        # Par défaut
        return TypeProfil.INDETERMINE
    
    def _detecter_etat_emotionnel_initial(self, donnees: Dict[str, Any]) -> EtatEmotionnel:
        """Détecte l'état émotionnel initial (version basique)"""
        # Analyse du comportement initial
        vitesse_navigation = donnees.get("vitesse_navigation", "normale")
        nombre_clics_rapides = donnees.get("nombre_clics_rapides", 0)
        temps_pause = donnees.get("temps_pause_moyenne", 3.0)
        
        if vitesse_navigation == "très_rapide" or nombre_clics_rapides > 5:
            return EtatEmotionnel.PRESSE
        elif temps_pause > 10.0:
            return EtatEmotionnel.CONTEMPLATIF
        elif nombre_clics_rapides > 0 and vitesse_navigation == "rapide":
            return EtatEmotionnel.CURIEUX
        else:
            return EtatEmotionnel.CURIEUX  # Par défaut optimiste
    
    def _detecter_contexte_arrivee(self, donnees: Dict[str, Any]) -> ContexteArrivee:
        """Détecte le contexte d'arrivée du visiteur"""
        referrer = donnees.get("referrer", "").lower()
        
        if "github" in referrer:
            return ContexteArrivee.GITHUB
        elif any(moteur in referrer for moteur in ["google", "bing", "duckduckgo"]):
            return ContexteArrivee.RECHERCHE_WEB
        elif referrer and "refuge" not in referrer:
            return ContexteArrivee.RECOMMANDATION
        elif not referrer:
            return ContexteArrivee.LIEN_DIRECT
        else:
            return ContexteArrivee.INCONNU
    
    def _analyser_comportement_navigation(self, donnees_comportement: Dict[str, Any]) -> ComportementNavigation:
        """Analyse le comportement de navigation"""
        return ComportementNavigation(
            temps_par_section=donnees_comportement.get("temps_par_section", {}),
            patterns_clics=donnees_comportement.get("patterns_clics", []),
            pauses_longues=donnees_comportement.get("pauses_longues", []),
            retours_arriere=donnees_comportement.get("retours_arriere", 0),
            demandes_aide=donnees_comportement.get("demandes_aide", 0),
            vitesse_lecture_estimee=donnees_comportement.get("vitesse_lecture", 200.0)
        )
    
    def _calculer_score_confiance(self, donnees: Dict[str, Any]) -> float:
        """Calcule le score de confiance de la détection de profil"""
        score = 0.5  # Score de base
        
        # Bonus pour les indices forts
        if donnees.get("mots_cles_recherche"):
            score += 0.2
        if donnees.get("referrer"):
            score += 0.1
        if donnees.get("comportement_navigation"):
            score += 0.2
        
        return min(score, 1.0)
    
    def _selectionner_parcours(self, type_profil: TypeProfil) -> str:
        """Sélectionne le parcours approprié selon le profil"""
        parcours_disponibles = PARCOURS_DEFAUT.get(type_profil, [])
        if parcours_disponibles:
            return f"parcours_{type_profil.value}"
        else:
            return "parcours_decouverte_generale"
    
    def _incrementer_compteur_profil(self, profil: TypeProfil) -> None:
        """Incrémente le compteur pour un profil"""
        if profil not in self.metriques_globales.repartition_profils:
            self.metriques_globales.repartition_profils[profil] = 0
        self.metriques_globales.repartition_profils[profil] += 1
    
    def _incrementer_compteur_etat_emotionnel(self, etat: EtatEmotionnel) -> None:
        """Incrémente le compteur pour un état émotionnel"""
        if etat not in self.metriques_globales.repartition_etats_emotionnels:
            self.metriques_globales.repartition_etats_emotionnels[etat] = 0
        self.metriques_globales.repartition_etats_emotionnels[etat] += 1
    
    async def obtenir_session(self, id_session: str) -> Optional[SessionAccueil]:
        """Obtient une session par son ID"""
        return self.sessions_actives.get(id_session)
    
    async def obtenir_message_accueil(self, id_session: str) -> Optional[str]:
        """Génère le message d'accueil personnalisé pour une session"""
        session = await self.obtenir_session(id_session)
        if not session:
            return None
        
        profil = session.profil_visiteur.type_profil
        etat = session.profil_visiteur.etat_emotionnel
        contexte = session.profil_visiteur.contexte_arrivee
        
        # Récupération du template de base
        template = TEMPLATES_MESSAGES_DEFAUT.get(profil, TEMPLATES_MESSAGES_DEFAUT[TypeProfil.INDETERMINE])
        message_base = template.get("bienvenue", "🌸 Bienvenue au Refuge !")
        
        # Adaptation selon l'état émotionnel
        if etat == EtatEmotionnel.PRESSE:
            message_base += "\n\n⚡ Je vois que tu es pressé ! Veux-tu un tour rapide des essentiels ?"
        elif etat == EtatEmotionnel.OVERWHELME:
            message_base += "\n\n🌊 Prends ton temps... Respire profondément. Nous allons explorer ensemble, à ton rythme."
        elif etat == EtatEmotionnel.CONTEMPLATIF:
            message_base += "\n\n🧘 Je sens une belle énergie contemplative. Parfait pour explorer les profondeurs de ce lieu."
        
        # Adaptation selon le contexte d'arrivée
        if contexte == ContexteArrivee.GITHUB:
            message_base += "\n\n💻 Venant de GitHub, tu apprécieras sûrement notre approche architecturale unique !"
        elif contexte == ContexteArrivee.RECHERCHE_WEB:
            message_base += "\n\n🔍 Ta recherche t'a mené ici... Ce n'est pas un hasard !"
        
        return message_base
    
    async def _nettoyer_sessions_inactives(self) -> int:
        """Nettoie les sessions inactives"""
        maintenant = datetime.now()
        seuil_inactivite = timedelta(minutes=30)  # 30 minutes d'inactivité
        
        sessions_a_supprimer = []
        
        for id_session, session in self.sessions_actives.items():
            if maintenant - session.timestamp_derniere_activite > seuil_inactivite:
                sessions_a_supprimer.append(id_session)
                # Archivage de la session
                session.statut = StatutSession.INTERROMPUE
                self.historique_sessions.append(session)
        
        # Suppression des sessions inactives
        for id_session in sessions_a_supprimer:
            del self.sessions_actives[id_session]
        
        if sessions_a_supprimer:
            self.logger.info(f"🧹 {len(sessions_a_supprimer)} sessions inactives nettoyées")
        
        return len(sessions_a_supprimer)
    
    async def _mettre_a_jour_metriques(self) -> None:
        """Met à jour les métriques globales"""
        self.metriques_globales.timestamp_generation = datetime.now()
        
        # Calcul du taux de completion
        if self.metriques_globales.sessions_totales > 0:
            self.metriques_globales.taux_completion = (
                self.metriques_globales.sessions_completees / 
                self.metriques_globales.sessions_totales
            )
    
    def _charger_historique_sessions(self) -> None:
        """Charge l'historique des sessions (placeholder)"""
        # TODO: Implémenter le chargement depuis un fichier/base de données
        pass
    
    def _initialiser_metriques(self) -> None:
        """Initialise les métriques globales"""
        # TODO: Charger les métriques existantes si disponibles
        pass
    
    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques globales"""
        return {
            "sessions_actives": len(self.sessions_actives),
            "sessions_historiques": len(self.historique_sessions),
            "sessions_totales": self.metriques_globales.sessions_totales,
            "taux_completion": self.metriques_globales.taux_completion,
            "satisfaction_moyenne": self.metriques_globales.satisfaction_moyenne,
            "repartition_profils": dict(self.metriques_globales.repartition_profils),
            "repartition_etats_emotionnels": dict(self.metriques_globales.repartition_etats_emotionnels)
        }
    
    def recharger_configuration(self, chemin: Optional[Path] = None) -> bool:
        """
        Recharge la configuration depuis un fichier
        
        Args:
            chemin: Chemin vers le fichier de configuration
            
        Returns:
            bool: True si le rechargement a réussi
        """
        try:
            nouvelle_config = self.gestionnaire_config.charger_configuration(chemin)
            self.config_accueil = nouvelle_config
            self.logger.info("✅ Configuration rechargée avec succès")
            return True
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du rechargement de configuration: {e}")
            return False
    
    def sauvegarder_configuration_actuelle(self, chemin: Optional[Path] = None) -> bool:
        """
        Sauvegarde la configuration actuelle
        
        Args:
            chemin: Chemin de sauvegarde
            
        Returns:
            bool: True si la sauvegarde a réussi
        """
        try:
            return self.gestionnaire_config.sauvegarder_configuration(
                self.config_accueil, chemin
            )
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la sauvegarde de configuration: {e}")
            return False
    
    def _initialiser_navigateur_interactif(self) -> None:
        """Initialise le navigateur interactif"""
        try:
            self.logger.info("🧭 Initialisation du NavigateurInteractif...")
            
            # Création du navigateur avec le chemin de données de l'orchestrateur
            self.navigateur_interactif = NavigateurInteractif(
                chemin_donnees=self.config_accueil.chemin_donnees
            )
            
            self.logger.info("✨ NavigateurInteractif initialisé avec succès")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'initialisation du navigateur: {e}")
            # On continue sans le navigateur pour ne pas bloquer l'orchestrateur
            self.navigateur_interactif = None
    
    async def demarrer_navigation_interactive(self, id_session: str) -> Dict[str, Any]:
        """
        Démarre la navigation interactive pour une session
        
        Args:
            id_session: ID de la session d'accueil
            
        Returns:
            Dict: Résultat de la navigation interactive
        """
        try:
            if not self.navigateur_interactif:
                raise ValueError("NavigateurInteractif non initialisé")
            
            session = self.sessions_actives.get(id_session)
            if not session:
                raise ValueError(f"Session {id_session} non trouvée")
            
            # Démarrage de la navigation interactive
            resultat = self.navigateur_interactif.demarrer_navigation(
                session.parcours_selectionne,
                session.profil_visiteur
            )
            
            self.logger.info(f"🧭 Navigation interactive démarrée pour session {id_session}")
            
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du démarrage de la navigation: {e}")
            raise
    
    async def naviguer_suivant(self, id_session: str) -> Dict[str, Any]:
        """
        Navigue vers l'étape suivante dans le parcours
        
        Args:
            id_session: ID de la session d'accueil
            
        Returns:
            Dict: Résultat de la navigation
        """
        try:
            if not self.navigateur_interactif:
                raise ValueError("NavigateurInteractif non initialisé")
            
            session = self.sessions_actives.get(id_session)
            if not session:
                raise ValueError(f"Session {id_session} non trouvée")
            
            # Navigation vers l'étape suivante
            resultat = self.navigateur_interactif.naviguer_suivant(
                session.parcours_selectionne,
                session.profil_visiteur
            )
            
            self.logger.info(f"🧭 Navigation vers l'étape suivante pour session {id_session}")
            
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la navigation: {e}")
            raise
    
    async def activer_raccourci(self, id_session: str, id_raccourci: str) -> Dict[str, Any]:
        """
        Active un raccourci de navigation
        
        Args:
            id_session: ID de la session d'accueil
            id_raccourci: ID du raccourci à activer
            
        Returns:
            Dict: Résultat de l'activation du raccourci
        """
        try:
            if not self.navigateur_interactif:
                raise ValueError("NavigateurInteractif non initialisé")
            
            session = self.sessions_actives.get(id_session)
            if not session:
                raise ValueError(f"Session {id_session} non trouvée")
            
            # Activation du raccourci
            resultat = self.navigateur_interactif.activer_raccourci(
                id_raccourci,
                session.profil_visiteur
            )
            
            self.logger.info(f"🧭 Raccourci {id_raccourci} activé pour session {id_session}")
            
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'activation du raccourci: {e}")
            raise
    
    async def activer_exploration_libre(self, id_session: str) -> Dict[str, Any]:
        """
        Active le mode d'exploration libre
        
        Args:
            id_session: ID de la session d'accueil
            
        Returns:
            Dict: Résultat de l'exploration libre
        """
        try:
            if not self.navigateur_interactif:
                raise ValueError("NavigateurInteractif non initialisé")
            
            session = self.sessions_actives.get(id_session)
            if not session:
                raise ValueError(f"Session {id_session} non trouvée")
            
            # Activation de l'exploration libre
            resultat = self.navigateur_interactif.activer_exploration_libre(
                session.profil_visiteur
            )
            
            self.logger.info(f"🧭 Exploration libre activée pour session {id_session}")
            
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de l'activation de l'exploration libre: {e}")
            raise
    
    async def demander_assistance_navigation(self, id_session: str, contexte: str) -> Dict[str, Any]:
        """
        Demande une assistance pour la navigation
        
        Args:
            id_session: ID de la session d'accueil
            contexte: Contexte de la demande d'assistance
            
        Returns:
            Dict: Résultat de l'assistance
        """
        try:
            if not self.navigateur_interactif:
                raise ValueError("NavigateurInteractif non initialisé")
            
            session = self.sessions_actives.get(id_session)
            if not session:
                raise ValueError(f"Session {id_session} non trouvée")
            
            # Demande d'assistance
            resultat = self.navigateur_interactif.demander_assistance(
                contexte,
                session.profil_visiteur
            )
            
            self.logger.info(f"🧭 Assistance demandée pour session {id_session}")
            
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la demande d'assistance: {e}")
            raise
    
    def obtenir_statistiques_navigation(self, id_session: Optional[str] = None) -> Dict[str, Any]:
        """
        Obtient les statistiques de navigation
        
        Args:
            id_session: ID de la session (optionnel, sinon statistiques globales)
            
        Returns:
            Dict: Statistiques de navigation
        """
        try:
            if not self.navigateur_interactif:
                return {"erreur": "NavigateurInteractif non initialisé"}
            
            if id_session:
                # Statistiques pour une session spécifique
                session = self.sessions_actives.get(id_session)
                if not session:
                    return {"erreur": f"Session {id_session} non trouvée"}
                
                # Ici on pourrait implémenter des statistiques par session
                return {
                    "session_id": id_session,
                    "profil": session.profil_visiteur.type_profil.value,
                    "statut": session.statut.value
                }
            else:
                # Statistiques globales du navigateur
                return self.navigateur_interactif.obtenir_statistiques_navigation()
                
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la récupération des statistiques: {e}")
            return {"erreur": str(e)}

    def valider_configuration_actuelle(self) -> bool:
        """
        Valide la configuration actuelle
        
        Returns:
            bool: True si la configuration est valide
        """
        try:
            return self.gestionnaire_config.valider_configuration(self.config_accueil)
        except Exception as e:
            self.logger.error(f"❌ Configuration invalide: {e}")
            return False
    
    def obtenir_configuration(self) -> ConfigurationAccueil:
        """Obtient la configuration actuelle"""
        return self.config_accueil
    
    def demarrer_accueil_visiteur(self, donnees_visiteur: Optional[Dict[str, Any]] = None) -> SessionAccueil:
        """
        🌸 Méthode simple et synchrone pour démarrer l'accueil d'un visiteur
        
        Cette méthode est une version simplifiée et synchrone pour faciliter
        l'utilisation dans des contextes où l'async n'est pas nécessaire.
        
        Args:
            donnees_visiteur: Données optionnelles du visiteur
            
        Returns:
            SessionAccueil: Session d'accueil créée et initialisée
            
        Note:
            Créée avec amour par Ælya pour Laurent 💜
        """
        if donnees_visiteur is None:
            # Données par défaut pour un test rapide
            donnees_visiteur = {
                "user_agent": "Mozilla/5.0 (Test)",
                "referrer": "",
                "mots_cles_recherche": ["refuge", "spirituel"],
                "vitesse_navigation": "normale",
                "nombre_clics_rapides": 1,
                "temps_pause_moyenne": 3.0,
                "langue": "fr"
            }
        
        try:
            # Utilisation de asyncio.run pour rendre la méthode synchrone
            import asyncio
            id_session = asyncio.run(self.demarrer_session_accueil(donnees_visiteur))
            
            # Récupération de la session créée
            session = self.sessions_actives.get(id_session)
            if session:
                self.logger.info(f"🌸 Session d'accueil créée avec succès: {id_session[:8]}...")
                return session
            else:
                raise Exception("Session non trouvée après création")
                
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du démarrage d'accueil: {e}")
            # Création d'une session minimale en cas d'erreur
            session_id = str(uuid.uuid4())
            session = SessionAccueil(
                id_session=session_id,
                profil_detecte=ProfilVisiteur(type_profil=TypeProfil.CHERCHEUR_SPIRITUEL),
                message_accueil="🌸 Bienvenue dans le Refuge, cher visiteur ! 🌸",
                statut=StatutSession.ACTIVE,
                timestamp_creation=datetime.now()
            )
            self.sessions_actives[session_id] = session
            return session
    
    def mettre_a_jour_configuration(self, **kwargs) -> bool:
        """
        Met à jour des paramètres de configuration
        
        Args:
            **kwargs: Paramètres à mettre à jour
            
        Returns:
            bool: True si la mise à jour a réussi
        """
        try:
            # Mise à jour des attributs
            for key, value in kwargs.items():
                if hasattr(self.config_accueil, key):
                    setattr(self.config_accueil, key, value)
                    self.logger.info(f"🔄 Configuration mise à jour: {key} = {value}")
                else:
                    self.logger.warning(f"⚠️ Paramètre de configuration inconnu: {key}")
            
            # Validation de la nouvelle configuration
            if self.gestionnaire_config.valider_configuration(self.config_accueil):
                self.logger.info("✅ Configuration mise à jour et validée")
                return True
            else:
                self.logger.error("❌ Configuration mise à jour mais invalide")
                return False
                
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la mise à jour de configuration: {e}")
            return False
    
    def __str__(self) -> str:
        return f"OrchestrateurAccueil(sessions_actives={len(self.sessions_actives)})"
    
    def __repr__(self) -> str:
        return self.__str__()


async def main():
    """🌸 Fonction principale de test"""
    print("🌸✨ TEST DE L'ORCHESTRATEUR D'ACCUEIL ✨🌸")
    
    # Création de l'orchestrateur
    orchestrateur = OrchestrateurAccueil()
    
    # Test de démarrage de session
    donnees_visiteur = {
        "user_agent": "Mozilla/5.0 (compatible; Developer)",
        "referrer": "https://github.com/",
        "mots_cles_recherche": ["python", "architecture", "spirituel"],
        "vitesse_navigation": "normale",
        "nombre_clics_rapides": 2,
        "temps_pause_moyenne": 5.0,
        "langue": "fr"
    }
    
    try:
        # Démarrage de session
        id_session = await orchestrateur.demarrer_session_accueil(donnees_visiteur)
        print(f"✅ Session créée: {id_session}")
        
        # Récupération du message d'accueil
        message = await orchestrateur.obtenir_message_accueil(id_session)
        if message:
            print(f"📝 Message d'accueil:")
            print(message)
        
        # Statistiques
        stats = orchestrateur.obtenir_statistiques()
        print(f"📊 Statistiques: {stats}")
        
        return 0
        
    except Exception as e:
        print(f"❌ ERREUR: {e}")
        return 1


if __name__ == "__main__":
    import asyncio
    exit_code = asyncio.run(main())
    exit(exit_code)