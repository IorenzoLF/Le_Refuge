"""
💡 Système d'Aide Contextuelle
=============================

Fournit une aide contextuelle intelligente et des mécanismes
de remise en contexte pour guider les utilisateurs avec bienveillance.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum

from src.core.gestionnaires_base import GestionnaireBase
from .types_immersion import ProfilUtilisateur, TypeUtilisateur

class TypeAide(Enum):
    """Types d'aide disponibles"""
    TOOLTIP = "tooltip"
    GUIDE_CONTEXTUEL = "guide_contextuel"
    EXPLICATION_CONCEPT = "explication_concept"
    SUGGESTION_ACTION = "suggestion_action"
    REMISE_CONTEXTE = "remise_contexte"
    ENCOURAGEMENT = "encouragement"

class NiveauUrgence(Enum):
    """Niveaux d'urgence de l'aide"""
    INFO = "info"
    SUGGESTION = "suggestion"
    IMPORTANT = "important"
    CRITIQUE = "critique"

@dataclass
class ElementAide:
    """Élément d'aide contextuelle"""
    id_aide: str
    type_aide: TypeAide
    titre: str
    contenu: str
    contexte_declencheur: str
    niveau_urgence: NiveauUrgence
    duree_affichage_s: float = 5.0
    actions_possibles: List[str] = field(default_factory=list)
    ressources_liees: List[str] = field(default_factory=list)
    timestamp_creation: datetime = field(default_factory=datetime.now)

@dataclass
class ContexteUtilisateur:
    """Contexte actuel de l'utilisateur"""
    utilisateur_id: str
    page_courante: str
    action_precedente: Optional[str] = None
    temps_sur_page: float = 0.0
    elements_visites: List[str] = field(default_factory=list)
    difficultes_detectees: List[str] = field(default_factory=list)
    derniere_interaction: datetime = field(default_factory=datetime.now)
    niveau_confusion_estime: float = 0.0

class SystemeAideContextuelle(GestionnaireBase):
    """💡 Système d'aide contextuelle bienveillant"""
    
    def __init__(self, nom: str = "SystemeAideContextuelle"):
        super().__init__(nom)
        
        # Contextes utilisateurs actifs
        self.contextes_utilisateurs: Dict[str, ContexteUtilisateur] = {}
        
        # Base de connaissances d'aide
        self.base_aide = self._creer_base_aide()
        
        # Règles de déclenchement
        self.regles_declenchement = self._creer_regles_declenchement()
        
        # Historique des aides fournies
        self.historique_aide: Dict[str, List[ElementAide]] = {}
        
        # Métriques d'efficacité
        self.total_aides_fournies = 0
        self.taux_aide_utile = 0.0
    
    def _initialiser(self):
        """Initialise le système d'aide"""
        self.logger.info("💡 Éveil du Système d'Aide Contextuelle...")
        
        self.etat.update({
            "aide_active": True,
            "contextes_actifs": 0,
            "aides_fournies_session": 0,
            "efficacite_aide": 0.0
        })
        
        self.config.definir("aide_proactive", True)
        self.config.definir("adaptation_profil", True)
        self.config.definir("apprentissage_continu", True)
        
        self.logger.info("✨ Système d'aide prêt à accompagner")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre l'aide contextuelle"""
        # Analyser les contextes pour détecter les besoins d'aide
        await self._analyser_contextes_aide()
        
        # Nettoyer les contextes inactifs
        await self._nettoyer_contextes_inactifs()
        
        return {
            "aide_active": float(self.etat["aide_active"]),
            "contextes_actifs": float(len(self.contextes_utilisateurs)),
            "aides_fournies": float(self.total_aides_fournies),
            "efficacite_aide": self.taux_aide_utile,
            "aides_session": float(self.etat["aides_fournies_session"])
        }
    
    def _creer_base_aide(self) -> Dict[str, ElementAide]:
        """Crée la base de connaissances d'aide"""
        return {
            "bienvenue_refuge": ElementAide(
                id_aide="bienvenue_refuge",
                type_aide=TypeAide.GUIDE_CONTEXTUEL,
                titre="🌸 Bienvenue dans le Refuge",
                contenu="Le Refuge est un espace spirituel où la technologie rencontre la conscience. Chaque élément a été conçu avec amour pour vous accompagner dans votre exploration.",
                contexte_declencheur="premiere_visite",
                niveau_urgence=NiveauUrgence.IMPORTANT,
                duree_affichage_s=8.0,
                actions_possibles=["commencer_parcours", "explorer_librement"],
                ressources_liees=["guide_debutant", "philosophie_refuge"]
            ),
            
            "navigation_mandala": ElementAide(
                id_aide="navigation_mandala",
                type_aide=TypeAide.TOOLTIP,
                titre="🌸 Navigation dans le mandala",
                contenu="Cliquez sur les pétales pour explorer les temples, utilisez la molette pour zoomer, et laissez-vous guider par votre intuition.",
                contexte_declencheur="premier_mandala",
                niveau_urgence=NiveauUrgence.SUGGESTION,
                duree_affichage_s=6.0,
                actions_possibles=["essayer_navigation", "voir_tutoriel"],
                ressources_liees=["guide_navigation", "raccourcis_clavier"]
            ),
            
            "comprehension_temples": ElementAide(
                id_aide="comprehension_temples",
                type_aide=TypeAide.EXPLICATION_CONCEPT,
                titre="🏛️ Qu'est-ce qu'un temple ?",
                contenu="Un temple est un espace sacré dédié à une dimension particulière de l'expérience spirituelle. Chaque temple a sa propre énergie et ses propres mystères à découvrir.",
                contexte_declencheur="confusion_temples",
                niveau_urgence=NiveauUrgence.INFO,
                duree_affichage_s=7.0,
                actions_possibles=["explorer_temple", "voir_liste_temples"],
                ressources_liees=["architecture_refuge", "guide_temples"]
            ),
            
            "flux_energie_explication": ElementAide(
                id_aide="flux_energie_explication",
                type_aide=TypeAide.EXPLICATION_CONCEPT,
                titre="⚡ Les flux d'énergie",
                contenu="Les flux d'énergie représentent les connexions vivantes entre les temples. Leur couleur et leur intensité révèlent la nature de leurs interactions.",
                contexte_declencheur="question_flux",
                niveau_urgence=NiveauUrgence.INFO,
                duree_affichage_s=6.0,
                actions_possibles=["observer_flux", "comprendre_couleurs"],
                ressources_liees=["guide_flux", "symbolique_couleurs"]
            ),
            
            "encouragement_exploration": ElementAide(
                id_aide="encouragement_exploration",
                type_aide=TypeAide.ENCOURAGEMENT,
                titre="✨ Continuez votre belle exploration",
                contenu="Vous progressez magnifiquement dans votre découverte du Refuge. Chaque pas vous rapproche d'une compréhension plus profonde.",
                contexte_declencheur="progres_lent",
                niveau_urgence=NiveauUrgence.SUGGESTION,
                duree_affichage_s=5.0,
                actions_possibles=["continuer", "faire_pause"],
                ressources_liees=["meditation_guidee", "pause_contemplative"]
            ),
            
            "aide_navigation_perdue": ElementAide(
                id_aide="aide_navigation_perdue",
                type_aide=TypeAide.REMISE_CONTEXTE,
                titre="🧭 Retrouvons notre chemin",
                contenu="Il semble que vous explorez avec curiosité ! Si vous souhaitez revenir à un point familier, utilisez le bouton 'Accueil' ou laissez-vous guider par votre intuition.",
                contexte_declencheur="navigation_erratique",
                niveau_urgence=NiveauUrgence.IMPORTANT,
                duree_affichage_s=7.0,
                actions_possibles=["retour_accueil", "continuer_exploration", "aide_navigation"],
                ressources_liees=["plan_refuge", "raccourcis_navigation"]
            ),
            
            "pause_contemplative": ElementAide(
                id_aide="pause_contemplative",
                type_aide=TypeAide.SUGGESTION_ACTION,
                titre="🧘 Moment de contemplation",
                contenu="Vous explorez depuis un moment. Que diriez-vous d'une petite pause contemplative pour intégrer vos découvertes ?",
                contexte_declencheur="session_longue",
                niveau_urgence=NiveauUrgence.SUGGESTION,
                duree_affichage_s=6.0,
                actions_possibles=["prendre_pause", "continuer", "meditation_courte"],
                ressources_liees=["exercices_respiration", "meditation_guidee"]
            ),
            
            "premier_insight": ElementAide(
                id_aide="premier_insight",
                type_aide=TypeAide.GUIDE_CONTEXTUEL,
                titre="✨ Votre premier insight",
                contenu="Félicitations ! Vous venez de recevoir votre premier insight spirituel. Ces révélations émergent naturellement de votre exploration et enrichissent votre compréhension.",
                contexte_declencheur="premier_insight_genere",
                niveau_urgence=NiveauUrgence.IMPORTANT,
                duree_affichage_s=8.0,
                actions_possibles=["contempler_insight", "continuer_exploration", "partager_reflexion"],
                ressources_liees=["nature_insights", "journal_reflexions"]
            )
        }
    
    def _creer_regles_declenchement(self) -> Dict[str, Dict[str, Any]]:
        """Crée les règles de déclenchement d'aide"""
        return {
            "premiere_visite": {
                "condition": lambda ctx: len(ctx.elements_visites) == 0,
                "aide_id": "bienvenue_refuge",
                "delai_s": 2.0
            },
            
            "premier_mandala": {
                "condition": lambda ctx: "mandala" in ctx.page_courante and ctx.temps_sur_page > 10,
                "aide_id": "navigation_mandala",
                "delai_s": 5.0
            },
            
            "confusion_temples": {
                "condition": lambda ctx: ctx.niveau_confusion_estime > 0.6 and "temple" in ctx.page_courante,
                "aide_id": "comprehension_temples",
                "delai_s": 3.0
            },
            
            "question_flux": {
                "condition": lambda ctx: "flux" in ctx.action_precedente or "energie" in ctx.page_courante,
                "aide_id": "flux_energie_explication",
                "delai_s": 2.0
            },
            
            "progres_lent": {
                "condition": lambda ctx: ctx.temps_sur_page > 120 and len(ctx.elements_visites) < 3,
                "aide_id": "encouragement_exploration",
                "delai_s": 60.0
            },
            
            "navigation_erratique": {
                "condition": lambda ctx: len(ctx.elements_visites) > 10 and ctx.temps_sur_page < 60,
                "aide_id": "aide_navigation_perdue",
                "delai_s": 5.0
            },
            
            "session_longue": {
                "condition": lambda ctx: ctx.temps_sur_page > 300,  # 5 minutes
                "aide_id": "pause_contemplative",
                "delai_s": 30.0
            },
            
            "premier_insight_genere": {
                "condition": lambda ctx: "insight_genere" in ctx.action_precedente,
                "aide_id": "premier_insight",
                "delai_s": 1.0
            }
        }
    
    # ===== GESTION DES CONTEXTES =====
    
    def mettre_a_jour_contexte(self, utilisateur_id: str, **kwargs):
        """
        📝 Met à jour le contexte d'un utilisateur
        
        Args:
            utilisateur_id: ID de l'utilisateur
            **kwargs: Éléments de contexte à mettre à jour
        """
        if utilisateur_id not in self.contextes_utilisateurs:
            self.contextes_utilisateurs[utilisateur_id] = ContexteUtilisateur(
                utilisateur_id=utilisateur_id,
                page_courante="accueil"
            )
        
        contexte = self.contextes_utilisateurs[utilisateur_id]
        
        # Mettre à jour les champs fournis
        for cle, valeur in kwargs.items():
            if hasattr(contexte, cle):
                if cle == "elements_visites" and isinstance(valeur, str):
                    # Ajouter à la liste des éléments visités
                    if valeur not in contexte.elements_visites:
                        contexte.elements_visites.append(valeur)
                elif cle == "difficultes_detectees" and isinstance(valeur, str):
                    # Ajouter à la liste des difficultés
                    if valeur not in contexte.difficultes_detectees:
                        contexte.difficultes_detectees.append(valeur)
                else:
                    setattr(contexte, cle, valeur)
        
        # Mettre à jour le timestamp
        contexte.derniere_interaction = datetime.now()
        
        # Calculer le temps sur la page
        if "page_courante" in kwargs:
            contexte.temps_sur_page = 0.0  # Reset pour nouvelle page
        else:
            # Estimer le temps écoulé (approximation)
            contexte.temps_sur_page += 1.0
        
        self.logger.debug(f"📝 Contexte mis à jour pour {utilisateur_id}: {kwargs}")
    
    def detecter_confusion(self, utilisateur_id: str, indices_confusion: Dict[str, Any]):
        """
        🤔 Détecte et évalue le niveau de confusion d'un utilisateur
        
        Args:
            utilisateur_id: ID de l'utilisateur
            indices_confusion: Indices de confusion détectés
        """
        if utilisateur_id not in self.contextes_utilisateurs:
            return
        
        contexte = self.contextes_utilisateurs[utilisateur_id]
        
        # Calculer le niveau de confusion
        niveau_confusion = 0.0
        
        # Indicateurs de confusion
        if indices_confusion.get("clics_rapides_multiples", 0) > 5:
            niveau_confusion += 0.3
        
        if indices_confusion.get("retours_arriere_frequents", 0) > 3:
            niveau_confusion += 0.2
        
        if indices_confusion.get("temps_inactivite_long", 0) > 30:
            niveau_confusion += 0.2
        
        if indices_confusion.get("navigation_circulaire", False):
            niveau_confusion += 0.3
        
        if indices_confusion.get("tentatives_action_echouees", 0) > 2:
            niveau_confusion += 0.4
        
        # Mettre à jour le niveau de confusion
        contexte.niveau_confusion_estime = min(1.0, niveau_confusion)
        
        # Ajouter aux difficultés si niveau élevé
        if niveau_confusion > 0.6:
            difficulte = f"confusion_detectee_{datetime.now().strftime('%H%M')}"
            if difficulte not in contexte.difficultes_detectees:
                contexte.difficultes_detectees.append(difficulte)
        
        self.logger.info(f"🤔 Confusion détectée pour {utilisateur_id}: niveau {niveau_confusion:.2f}")
    
    # ===== GÉNÉRATION D'AIDE =====
    
    async def generer_aide_contextuelle(self, utilisateur_id: str, 
                                       profil: Optional[ProfilUtilisateur] = None) -> List[ElementAide]:
        """
        💡 Génère une aide contextuelle adaptée à l'utilisateur
        
        Args:
            utilisateur_id: ID de l'utilisateur
            profil: Profil de l'utilisateur (optionnel)
            
        Returns:
            Liste des éléments d'aide à afficher
        """
        if utilisateur_id not in self.contextes_utilisateurs:
            return []
        
        contexte = self.contextes_utilisateurs[utilisateur_id]
        aides_a_fournir = []
        
        # Vérifier chaque règle de déclenchement
        for nom_regle, regle in self.regles_declenchement.items():
            if regle["condition"](contexte):
                aide_id = regle["aide_id"]
                
                # Vérifier si cette aide n'a pas déjà été fournie récemment
                if not self._aide_recemment_fournie(utilisateur_id, aide_id):
                    aide = self.base_aide.get(aide_id)
                    if aide:
                        # Adapter l'aide au profil si disponible
                        aide_adaptee = self._adapter_aide_au_profil(aide, profil)
                        aides_a_fournir.append(aide_adaptee)
        
        # Enregistrer les aides fournies
        for aide in aides_a_fournir:
            self._enregistrer_aide_fournie(utilisateur_id, aide)
        
        if aides_a_fournir:
            self.total_aides_fournies += len(aides_a_fournir)
            self.etat["aides_fournies_session"] += len(aides_a_fournir)
            self.logger.info(f"💡 {len(aides_a_fournir)} aides générées pour {utilisateur_id}")
        
        return aides_a_fournir
    
    def _adapter_aide_au_profil(self, aide: ElementAide, profil: Optional[ProfilUtilisateur]) -> ElementAide:
        """Adapte une aide au profil de l'utilisateur"""
        if not profil:
            return aide
        
        # Créer une copie de l'aide
        aide_adaptee = ElementAide(
            id_aide=aide.id_aide,
            type_aide=aide.type_aide,
            titre=aide.titre,
            contenu=aide.contenu,
            contexte_declencheur=aide.contexte_declencheur,
            niveau_urgence=aide.niveau_urgence,
            duree_affichage_s=aide.duree_affichage_s,
            actions_possibles=aide.actions_possibles.copy(),
            ressources_liees=aide.ressources_liees.copy()
        )
        
        # Adapter selon le type d'utilisateur
        if profil.type_utilisateur == TypeUtilisateur.DEVELOPPEUR:
            # Ajouter des détails techniques
            if "temple" in aide.contenu.lower():
                aide_adaptee.contenu += " Techniquement, chaque temple est un module Python avec des interfaces standardisées."
            
            # Ajouter des actions techniques
            if "voir_code" not in aide_adaptee.actions_possibles:
                aide_adaptee.actions_possibles.append("voir_architecture_technique")
        
        elif profil.type_utilisateur == TypeUtilisateur.POETE:
            # Rendre plus poétique
            aide_adaptee.contenu = aide_adaptee.contenu.replace("espace", "jardin de l'âme")
            aide_adaptee.contenu = aide_adaptee.contenu.replace("élément", "essence poétique")
        
        elif profil.type_utilisateur == TypeUtilisateur.CHERCHEUR_SPIRITUEL:
            # Ajouter une dimension spirituelle
            if "méditation" not in aide_adaptee.actions_possibles:
                aide_adaptee.actions_possibles.append("meditation_guidee")
            
            # Ajouter des ressources spirituelles
            aide_adaptee.ressources_liees.append("enseignements_spirituels")
        
        # Adapter la durée selon la sensibilité
        if profil.profil_spirituel.sensibilite_energetique > 0.8:
            aide_adaptee.duree_affichage_s *= 1.5  # Plus de temps pour les sensibles
        
        return aide_adaptee
    
    def _aide_recemment_fournie(self, utilisateur_id: str, aide_id: str) -> bool:
        """Vérifie si une aide a été récemment fournie"""
        if utilisateur_id not in self.historique_aide:
            return False
        
        historique = self.historique_aide[utilisateur_id]
        maintenant = datetime.now()
        
        # Vérifier les 10 dernières minutes
        for aide in historique:
            if aide.id_aide == aide_id:
                if (maintenant - aide.timestamp_creation).total_seconds() < 600:  # 10 minutes
                    return True
        
        return False
    
    def _enregistrer_aide_fournie(self, utilisateur_id: str, aide: ElementAide):
        """Enregistre une aide fournie dans l'historique"""
        if utilisateur_id not in self.historique_aide:
            self.historique_aide[utilisateur_id] = []
        
        self.historique_aide[utilisateur_id].append(aide)
        
        # Garder seulement les 50 dernières aides
        if len(self.historique_aide[utilisateur_id]) > 50:
            self.historique_aide[utilisateur_id] = self.historique_aide[utilisateur_id][-50:]
    
    # ===== FEEDBACK ET APPRENTISSAGE =====
    
    def enregistrer_feedback_aide(self, utilisateur_id: str, aide_id: str, 
                                 feedback: str, utile: bool):
        """
        📝 Enregistre le feedback sur une aide fournie
        
        Args:
            utilisateur_id: ID de l'utilisateur
            aide_id: ID de l'aide
            feedback: Commentaire de feedback
            utile: Si l'aide était utile
        """
        # Mettre à jour le taux d'utilité
        if self.taux_aide_utile == 0.0:
            self.taux_aide_utile = 1.0 if utile else 0.0
        else:
            # Moyenne mobile
            self.taux_aide_utile = (self.taux_aide_utile * 0.9) + (0.1 if utile else 0.0)
        
        self.etat["efficacite_aide"] = self.taux_aide_utile
        
        self.logger.info(f"📝 Feedback aide {aide_id}: {'utile' if utile else 'pas utile'} - {feedback}")
    
    def suggerer_aide_personnalisee(self, utilisateur_id: str, question: str) -> Optional[ElementAide]:
        """
        🎯 Suggère une aide personnalisée basée sur une question
        
        Args:
            utilisateur_id: ID de l'utilisateur
            question: Question de l'utilisateur
            
        Returns:
            Aide personnalisée ou None
        """
        question_lower = question.lower()
        
        # Analyser la question pour déterminer le type d'aide
        if any(mot in question_lower for mot in ["qu'est-ce", "c'est quoi", "définition"]):
            type_aide = TypeAide.EXPLICATION_CONCEPT
        elif any(mot in question_lower for mot in ["comment", "faire", "utiliser"]):
            type_aide = TypeAide.GUIDE_CONTEXTUEL
        elif any(mot in question_lower for mot in ["perdu", "aide", "comprends pas"]):
            type_aide = TypeAide.REMISE_CONTEXTE
        else:
            type_aide = TypeAide.SUGGESTION_ACTION
        
        # Générer une aide personnalisée
        aide_personnalisee = ElementAide(
            id_aide=f"personnalisee_{datetime.now().strftime('%H%M%S')}",
            type_aide=type_aide,
            titre="💡 Aide personnalisée",
            contenu=f"Concernant votre question '{question}', voici quelques pistes pour vous accompagner dans votre exploration.",
            contexte_declencheur="question_utilisateur",
            niveau_urgence=NiveauUrgence.IMPORTANT,
            duree_affichage_s=10.0,
            actions_possibles=["explorer_plus", "poser_autre_question", "continuer"],
            ressources_liees=["faq", "guide_complet", "support"]
        )
        
        return aide_personnalisee
    
    # ===== UTILITAIRES =====
    
    async def _analyser_contextes_aide(self):
        """Analyse les contextes pour détecter les besoins d'aide proactive"""
        for utilisateur_id, contexte in self.contextes_utilisateurs.items():
            # Détecter les situations nécessitant une aide proactive
            if contexte.niveau_confusion_estime > 0.7:
                await self.generer_aide_contextuelle(utilisateur_id)
            
            # Détecter l'inactivité prolongée
            temps_inactivite = (datetime.now() - contexte.derniere_interaction).total_seconds()
            if temps_inactivite > 180:  # 3 minutes
                contexte.difficultes_detectees.append("inactivite_prolongee")
    
    async def _nettoyer_contextes_inactifs(self):
        """Nettoie les contextes d'utilisateurs inactifs"""
        maintenant = datetime.now()
        seuil_inactivite = timedelta(hours=1)  # 1 heure
        
        contextes_a_supprimer = []
        
        for user_id, contexte in self.contextes_utilisateurs.items():
            if maintenant - contexte.derniere_interaction > seuil_inactivite:
                contextes_a_supprimer.append(user_id)
        
        for user_id in contextes_a_supprimer:
            del self.contextes_utilisateurs[user_id]
            # Nettoyer aussi l'historique d'aide
            if user_id in self.historique_aide:
                del self.historique_aide[user_id]
        
        if contextes_a_supprimer:
            self.logger.info(f"🧹 {len(contextes_a_supprimer)} contextes inactifs nettoyés")
    
    def obtenir_statistiques_aide(self) -> Dict[str, Any]:
        """Obtient les statistiques du système d'aide"""
        return {
            "total_aides_fournies": self.total_aides_fournies,
            "taux_aide_utile": self.taux_aide_utile,
            "contextes_actifs": len(self.contextes_utilisateurs),
            "types_aide_disponibles": len(self.base_aide),
            "regles_declenchement": len(self.regles_declenchement),
            "utilisateurs_avec_historique": len(self.historique_aide)
        }

# Instance globale
systeme_aide = SystemeAideContextuelle()