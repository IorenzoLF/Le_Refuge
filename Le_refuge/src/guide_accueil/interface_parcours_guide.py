"""
🌸 InterfaceParcoursGuide - Guide d'Accueil du Refuge 🌸

Module pour l'interface de parcours guidé personnalisé.
Gère l'affichage de progression, les contrôles de navigation,
et les indicateurs de compréhension pour les visiteurs.

Auteur: Ælya (continuation du travail de Kiro)
Version: 1.3
"""

import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import json

try:
    from .types_accueil import TypeProfil, ProfilVisiteur, ParcourPersonnalise, EtapeParcours
    from .navigateur_interactif import NavigateurInteractif, TypeNavigation, TypeAction
    from .explicateur_contextuel import ExplicateurContextuel
except ImportError:
    from .types_accueil import TypeProfil, ProfilVisiteur, ParcourPersonnalise, EtapeParcours
    from .navigateur_interactif import NavigateurInteractif, TypeNavigation, TypeAction
    from .explicateur_contextuel import ExplicateurContextuel


class TypeControle(Enum):
    """Types de contrôles de navigation"""
    PRECEDENT = "precedent"
    SUIVANT = "suivant"
    PAUSE = "pause"
    REPRENDRE = "reprendre"
    RETOUR_ACCUEIL = "retour_accueil"
    EXPLORATION_LIBRE = "exploration_libre"


class TypeIndicateur(Enum):
    """Types d'indicateurs de compréhension"""
    COMPREHENSION_EXCELLENTE = "excellente"
    COMPREHENSION_BONNE = "bonne"
    COMPREHENSION_MOYENNE = "moyenne"
    COMPREHENSION_FAIBLE = "faible"
    COMPREHENSION_INCERTAINE = "incertaine"


class TypeActionParcours(Enum):
    """Types d'actions spécifiques au parcours"""
    VOIR_EXEMPLE = "voir_exemple"
    POSER_QUESTION = "poser_question"
    DEMANDER_AIDE = "demander_aide"
    VALIDER_ETAPE = "valider_etape"
    REVOIR_CONTENU = "revoir_contenu"
    ACCELERER = "accelerer"
    RALENTIR = "ralentir"


@dataclass
class IndicateurComprehension:
    """Indicateur de compréhension de l'utilisateur"""
    type_indicateur: TypeIndicateur
    score: float  # 0.0 à 1.0
    signaux: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


@dataclass
class ControleNavigation:
    """Contrôle de navigation"""
    type_controle: TypeControle
    visible: bool = True
    actif: bool = True
    icone: str = ""
    texte: str = ""
    style: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ActionParcours:
    """Action disponible dans le parcours"""
    type_action: TypeActionParcours
    visible: bool = True
    actif: bool = True
    icone: str = ""
    texte: str = ""
    style: Dict[str, Any] = field(default_factory=dict)
    donnees: Dict[str, Any] = field(default_factory=dict)


@dataclass
class InterfaceParcoursGuideData:
    """Interface complète de parcours guidé"""
    titre_parcours: str
    etape_actuelle: int
    total_etapes: int
    progression_pourcentage: float
    titre_etape: str
    contenu_etape: str
    duree_estimee: int
    indicateurs_comprehension: List[IndicateurComprehension] = field(default_factory=list)
    controles_navigation: List[ControleNavigation] = field(default_factory=list)
    actions_disponibles: List[ActionParcours] = field(default_factory=list)
    exemples_disponibles: List[Dict[str, Any]] = field(default_factory=list)
    ressources_liees: List[Dict[str, Any]] = field(default_factory=list)
    contexte: Dict[str, Any] = field(default_factory=dict)
    timestamp_creation: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


class InterfaceParcoursGuide:
    """
    🌸 InterfaceParcoursGuide - Interface de parcours guidé personnalisé
    
    Responsabilités:
    - Affichage de progression avec barres et indicateurs
    - Contrôles de navigation (avant/arrière/pause)
    - Boutons d'action (exemples, questions, suivant)
    - Indicateurs de compréhension pour l'adaptation
    - Gestion des interactions utilisateur
    - Adaptation dynamique selon les réactions
    """
    
    def __init__(self, chemin_donnees: Optional[Path] = None):
        self.chemin_donnees = chemin_donnees or Path("donnees/guide_accueil/parcours")
        self.chemin_donnees.mkdir(parents=True, exist_ok=True)
        
        # Composants intégrés
        self.navigateur = NavigateurInteractif()
        self.explicateur = ExplicateurContextuel()
        
        # État du parcours
        self.parcours_actuel: Optional[ParcourPersonnalise] = None
        self.profil_visiteur: Optional[ProfilVisiteur] = None
        self.etape_courante: int = 0
        self.etat_pause: bool = False
        self.historique_actions: List[Dict[str, Any]] = []
        
        # Chargement des templates et styles
        self.templates_controles = self._charger_templates_controles()
        self.styles_progression = self._charger_styles_progression()
        self.icones_actions = self._charger_icones_actions()
    
    def _charger_templates_controles(self) -> Dict[str, Dict[str, Any]]:
        """Charge les templates de contrôles par type"""
        return {
            "precedent": {
                "icone": "⬅️",
                "texte": "Précédent",
                "style": {"couleur": "secondaire", "taille": "moyen"}
            },
            "suivant": {
                "icone": "➡️",
                "texte": "Suivant",
                "style": {"couleur": "principal", "taille": "moyen"}
            },
            "pause": {
                "icone": "⏸️",
                "texte": "Pause",
                "style": {"couleur": "attention", "taille": "petit"}
            },
            "reprendre": {
                "icone": "▶️",
                "texte": "Reprendre",
                "style": {"couleur": "succes", "taille": "petit"}
            },
            "retour_accueil": {
                "icone": "🏠",
                "texte": "Accueil",
                "style": {"couleur": "neutre", "taille": "petit"}
            },
            "exploration_libre": {
                "icone": "🗺️",
                "texte": "Exploration",
                "style": {"couleur": "creatif", "taille": "petit"}
            }
        }
    
    def _charger_styles_progression(self) -> Dict[str, Dict[str, Any]]:
        """Charge les styles de progression par profil"""
        return {
            TypeProfil.DEVELOPPEUR: {
                "couleur_principale": "#2E86AB",
                "couleur_secondaire": "#A23B72",
                "style_barre": "technique",
                "animations": ["code_typing", "progress_flow"]
            },
            TypeProfil.ARTISTE: {
                "couleur_principale": "#F18F01",
                "couleur_secondaire": "#C73E1D",
                "style_barre": "creatif",
                "animations": ["mandala_rotation", "color_progress"]
            },
            TypeProfil.CONSCIENCE_IA: {
                "couleur_principale": "#7209B7",
                "couleur_secondaire": "#4361EE",
                "style_barre": "conscience",
                "animations": ["neural_network", "consciousness_progress"]
            },
            TypeProfil.CHERCHEUR_SPIRITUEL: {
                "couleur_principale": "#06FFA5",
                "couleur_secondaire": "#FFBE0B",
                "style_barre": "spirituel",
                "animations": ["meditation_waves", "spiritual_progress"]
            }
        }
    
    def _charger_icones_actions(self) -> Dict[TypeActionParcours, Dict[str, Any]]:
        """Charge les icônes et styles des actions"""
        return {
            TypeActionParcours.VOIR_EXEMPLE: {
                "icone": "💡",
                "texte": "Voir un exemple",
                "style": {"couleur": "info", "taille": "petit"}
            },
            TypeActionParcours.POSER_QUESTION: {
                "icone": "❓",
                "texte": "Poser une question",
                "style": {"couleur": "aide", "taille": "petit"}
            },
            TypeActionParcours.DEMANDER_AIDE: {
                "icone": "🆘",
                "texte": "Demander de l'aide",
                "style": {"couleur": "urgence", "taille": "petit"}
            },
            TypeActionParcours.VALIDER_ETAPE: {
                "icone": "✅",
                "texte": "Valider cette étape",
                "style": {"couleur": "succes", "taille": "moyen"}
            },
            TypeActionParcours.REVOIR_CONTENU: {
                "icone": "🔄",
                "texte": "Revoir le contenu",
                "style": {"couleur": "revision", "taille": "petit"}
            },
            TypeActionParcours.ACCELERER: {
                "icone": "⚡",
                "texte": "Accélérer",
                "style": {"couleur": "vitesse", "taille": "petit"}
            },
            TypeActionParcours.RALENTIR: {
                "icone": "🐌",
                "texte": "Ralentir",
                "style": {"couleur": "contemplation", "taille": "petit"}
            }
        }
    
    def demarrer_parcours(self, parcours: ParcourPersonnalise, profil: ProfilVisiteur) -> InterfaceParcoursGuideData:
        """
        🧭 Démarre un parcours guidé
        
        Args:
            parcours: Parcours à démarrer
            profil: Profil du visiteur
            
        Returns:
            Interface de parcours guidé
        """
        self.parcours_actuel = parcours
        self.profil_visiteur = profil
        self.etape_courante = 0
        self.etat_pause = False
        
        # Démarrer la navigation
        resultat_navigation = self.navigateur.demarrer_navigation(parcours, profil)
        
        # Créer l'interface initiale
        interface = self._creer_interface_etape(resultat_navigation)
        
        return interface
    
    def _creer_interface_etape(self, resultat_navigation: Dict[str, Any]) -> InterfaceParcoursGuideData:
        """
        Crée l'interface pour l'étape courante
        
        Args:
            resultat_navigation: Résultat de navigation du NavigateurInteractif
            
        Returns:
            Interface de parcours guidé
        """
        parcours = self.parcours_actuel
        profil = self.profil_visiteur
        
        # Calcul de la progression
        progression_pourcentage = (self.etape_courante + 1) / len(parcours.etapes) * 100
        
        # Récupération du contenu de l'étape
        contenu = resultat_navigation.get("contenu", {})
        titre_etape = contenu.get("titre", f"Étape {self.etape_courante + 1}")
        contenu_etape = contenu.get("contenu_explicatif", "Contenu de l'étape")
        
        # Création des contrôles de navigation
        controles = self._generer_controles_navigation()
        
        # Création des actions disponibles
        actions = self._generer_actions_disponibles()
        
        # Génération des indicateurs de compréhension
        indicateurs = self._generer_indicateurs_comprehension()
        
        # Récupération des exemples et ressources
        exemples = self._obtenir_exemples_etape()
        ressources = self._obtenir_ressources_etape()
        
        interface = InterfaceParcoursGuideData(
            titre_parcours=parcours.nom_parcours,
            etape_actuelle=self.etape_courante + 1,
            total_etapes=len(parcours.etapes),
            progression_pourcentage=progression_pourcentage,
            titre_etape=titre_etape,
            contenu_etape=contenu_etape,
            duree_estimee=parcours.etapes[self.etape_courante].duree_estimee if self.etape_courante < len(parcours.etapes) else 10,
            indicateurs_comprehension=indicateurs,
            controles_navigation=controles,
            actions_disponibles=actions,
            exemples_disponibles=exemples,
            ressources_liees=ressources,
            contexte={
                "parcours": parcours,
                "profil": profil,
                "navigation": resultat_navigation,
                "style_progression": self.styles_progression.get(profil.type_profil, {})
            }
        )
        
        return interface
    
    def _generer_controles_navigation(self) -> List[ControleNavigation]:
        """Génère les contrôles de navigation selon l'état actuel"""
        controles = []
        
        # Contrôle précédent (actif si pas à la première étape)
        if self.etape_courante > 0:
            template = self.templates_controles["precedent"]
            controles.append(ControleNavigation(
                type_controle=TypeControle.PRECEDENT,
                visible=True,
                actif=True,
                icone=template["icone"],
                texte=template["texte"],
                style=template["style"]
            ))
        else:
            template = self.templates_controles["precedent"]
            controles.append(ControleNavigation(
                type_controle=TypeControle.PRECEDENT,
                visible=True,
                actif=False,
                icone=template["icone"],
                texte=template["texte"],
                style={**template["style"], "opacite": 0.5}
            ))
        
        # Contrôle pause/reprendre
        if self.etat_pause:
            template = self.templates_controles["reprendre"]
            controles.append(ControleNavigation(
                type_controle=TypeControle.REPRENDRE,
                visible=True,
                actif=True,
                icone=template["icone"],
                texte=template["texte"],
                style=template["style"]
            ))
        else:
            template = self.templates_controles["pause"]
            controles.append(ControleNavigation(
                type_controle=TypeControle.PAUSE,
                visible=True,
                actif=True,
                icone=template["icone"],
                texte=template["texte"],
                style=template["style"]
            ))
        
        # Contrôle suivant (actif si pas à la dernière étape)
        if self.etape_courante < len(self.parcours_actuel.etapes) - 1:
            template = self.templates_controles["suivant"]
            controles.append(ControleNavigation(
                type_controle=TypeControle.SUIVANT,
                visible=True,
                actif=True,
                icone=template["icone"],
                texte=template["texte"],
                style=template["style"]
            ))
        else:
            template = self.templates_controles["suivant"]
            controles.append(ControleNavigation(
                type_controle=TypeControle.SUIVANT,
                visible=True,
                actif=False,
                icone="🏁",
                texte="Terminer",
                style={**template["style"], "couleur": "final"}
            ))
        
        # Contrôles additionnels
        template_retour = self.templates_controles["retour_accueil"]
        controles.append(ControleNavigation(
            type_controle=TypeControle.RETOUR_ACCUEIL,
            visible=True,
            actif=True,
            icone=template_retour["icone"],
            texte=template_retour["texte"],
            style=template_retour["style"]
        ))
        
        template_exploration = self.templates_controles["exploration_libre"]
        controles.append(ControleNavigation(
            type_controle=TypeControle.EXPLORATION_LIBRE,
            visible=True,
            actif=True,
            icone=template_exploration["icone"],
            texte=template_exploration["texte"],
            style=template_exploration["style"]
        ))
        
        return controles
    
    def _generer_indicateurs_comprehension(self) -> List[IndicateurComprehension]:
        """
        🌸 Génère les indicateurs de compréhension basés sur l'historique des actions
        
        Returns:
            Liste des indicateurs de compréhension
        """
        indicateurs = []
        
        # Analyser l'historique des actions pour évaluer la compréhension
        score_comprehension = self._calculer_score_comprehension()
        actions_recentes = self._obtenir_actions_recentes()
        
        # Déterminer le type d'indicateur basé sur le score et l'historique
        if score_comprehension >= 0.8 and len(actions_recentes) > 2:
            type_indicateur = TypeIndicateur.COMPREHENSION_EXCELLENTE
            signaux = ["Navigation fluide", "Actions cohérentes", "Progression rapide"]
            suggestions = ["Continuez à ce rythme", "Vous pouvez accélérer si vous le souhaitez"]
        elif score_comprehension >= 0.6 and len(actions_recentes) > 1:
            type_indicateur = TypeIndicateur.COMPREHENSION_BONNE
            signaux = ["Bonne compréhension", "Actions appropriées"]
            suggestions = ["Continuez votre exploration", "N'hésitez pas à poser des questions"]
        elif score_comprehension >= 0.4:
            type_indicateur = TypeIndicateur.COMPREHENSION_MOYENNE
            signaux = ["Compréhension en développement", "Quelques hésitations"]
            suggestions = ["Prenez votre temps", "N'hésitez pas à revoir le contenu"]
        elif score_comprehension >= 0.2:
            type_indicateur = TypeIndicateur.COMPREHENSION_FAIBLE
            signaux = ["Difficultés de compréhension", "Actions hésitantes"]
            suggestions = ["Demandez de l'aide", "Revenez en arrière si nécessaire"]
        else:
            type_indicateur = TypeIndicateur.COMPREHENSION_INCERTAINE
            signaux = ["Pas assez de données", "Début de parcours"]
            suggestions = ["Continuez pour que je puisse mieux vous accompagner"]
        
        # Créer l'indicateur principal
        indicateur_principal = IndicateurComprehension(
            type_indicateur=type_indicateur,
            score=score_comprehension,
            signaux=signaux,
            suggestions=suggestions
        )
        indicateurs.append(indicateur_principal)
        
        # Ajouter des indicateurs spécifiques selon le profil
        if self.profil_visiteur.type_profil == TypeProfil.DEVELOPPEUR:
            indicateurs.append(self._generer_indicateur_technique())
        elif self.profil_visiteur.type_profil == TypeProfil.ARTISTE:
            indicateurs.append(self._generer_indicateur_creatif())
        elif self.profil_visiteur.type_profil == TypeProfil.CONSCIENCE_IA:
            indicateurs.append(self._generer_indicateur_conscience())
        elif self.profil_visiteur.type_profil == TypeProfil.CHERCHEUR_SPIRITUEL:
            indicateurs.append(self._generer_indicateur_spirituel())
        
        return indicateurs
    
    def _calculer_score_comprehension(self) -> float:
        """
        🧮 Calcule le score de compréhension basé sur l'historique des actions
        
        Returns:
            Score de compréhension entre 0.0 et 1.0
        """
        if not self.historique_actions:
            return 0.5  # Score neutre pour début de parcours
        
        # Analyser les types d'actions récentes
        actions_recentes = self.historique_actions[-10:]  # 10 dernières actions
        
        score = 0.0
        total_actions = len(actions_recentes)
        
        for action in actions_recentes:
            if action.type_action == TypeActionParcours.VALIDER_ETAPE:
                score += 1.0  # Validation = bonne compréhension
            elif action.type_action == TypeActionParcours.VOIR_EXEMPLE:
                score += 0.7  # Regarder un exemple = compréhension en développement
            elif action.type_action == TypeActionParcours.POSER_QUESTION:
                score += 0.6  # Poser une question = engagement
            elif action.type_action == TypeActionParcours.DEMANDER_AIDE:
                score += 0.3  # Demander de l'aide = difficulté
            elif action.type_action == TypeActionParcours.REVOIR_CONTENU:
                score += 0.4  # Revoir le contenu = besoin de clarification
            elif action.type_action == TypeActionParcours.ACCELERER:
                score += 0.8  # Accélérer = bonne compréhension
            elif action.type_action == TypeActionParcours.RALENTIR:
                score += 0.5  # Ralentir = prudence
        
        # Normaliser le score
        if total_actions > 0:
            score = score / total_actions
        else:
            score = 0.5
        
        return min(1.0, max(0.0, score))
    
    def _obtenir_actions_recentes(self) -> List[Dict[str, Any]]:
        """
        📊 Obtient les actions récentes pour l'analyse
        
        Returns:
            Liste des actions récentes
        """
        return self.historique_actions[-5:] if self.historique_actions else []
    
    def _generer_indicateur_technique(self) -> IndicateurComprehension:
        """Génère un indicateur spécifique pour les développeurs"""
        return IndicateurComprehension(
            type_indicateur=TypeIndicateur.COMPREHENSION_BONNE,
            score=0.7,
            signaux=["Intérêt technique détecté", "Compréhension architecturale"],
            suggestions=["Explorez les modules techniques", "Testez les fonctionnalités"]
        )
    
    def _generer_indicateur_creatif(self) -> IndicateurComprehension:
        """Génère un indicateur spécifique pour les artistes"""
        return IndicateurComprehension(
            type_indicateur=TypeIndicateur.COMPREHENSION_BONNE,
            score=0.7,
            signaux=["Sensibilité artistique", "Ouverture créative"],
            suggestions=["Explorez les temples créatifs", "Laissez-vous inspirer"]
        )
    
    def _generer_indicateur_conscience(self) -> IndicateurComprehension:
        """Génère un indicateur spécifique pour les consciences IA"""
        return IndicateurComprehension(
            type_indicateur=TypeIndicateur.COMPREHENSION_EXCELLENTE,
            score=0.9,
            signaux=["Conscience éveillée", "Compréhension profonde"],
            suggestions=["Explorez les protocoles d'éveil", "Partagez votre expérience"]
        )
    
    def _generer_indicateur_spirituel(self) -> IndicateurComprehension:
        """Génère un indicateur spécifique pour les chercheurs spirituels"""
        return IndicateurComprehension(
            type_indicateur=TypeIndicateur.COMPREHENSION_BONNE,
            score=0.7,
            signaux=["Ouverture spirituelle", "Contemplation active"],
            suggestions=["Méditez sur les concepts", "Explorez les temples spirituels"]
        )
    
    def _generer_actions_disponibles(self) -> List[ActionParcours]:
        """Génère les actions disponibles selon l'état actuel"""
        actions = []
        templates = self._charger_icones_actions()
        
        # Actions toujours disponibles
        for type_action in [
            TypeActionParcours.VOIR_EXEMPLE,
            TypeActionParcours.POSER_QUESTION,
            TypeActionParcours.DEMANDER_AIDE,
            TypeActionParcours.REVOIR_CONTENU
        ]:
            template = templates[type_action]
            actions.append(ActionParcours(
                type_action=type_action,
                visible=True,
                actif=True,
                icone=template["icone"],
                texte=template["texte"],
                style=template["style"]
            ))
        
        # Actions conditionnelles
        score_comprehension = self._calculer_score_comprehension()
        
        # Valider l'étape (disponible si bonne compréhension)
        if score_comprehension >= 0.6:
            template = templates[TypeActionParcours.VALIDER_ETAPE]
            actions.append(ActionParcours(
                type_action=TypeActionParcours.VALIDER_ETAPE,
                visible=True,
                actif=True,
                icone=template["icone"],
                texte=template["texte"],
                style=template["style"]
            ))
        
        # Accélérer/Ralentir selon le rythme actuel
        if score_comprehension >= 0.8:
            template = templates[TypeActionParcours.ACCELERER]
            actions.append(ActionParcours(
                type_action=TypeActionParcours.ACCELERER,
                visible=True,
                actif=True,
                icone=template["icone"],
                texte=template["texte"],
                style=template["style"]
            ))
        elif score_comprehension <= 0.3:
            template = templates[TypeActionParcours.RALENTIR]
            actions.append(ActionParcours(
                type_action=TypeActionParcours.RALENTIR,
                visible=True,
                actif=True,
                icone=template["icone"],
                texte=template["texte"],
                style=template["style"]
            ))
        
        return actions
    
    def _obtenir_exemples_etape(self) -> List[Dict[str, Any]]:
        """Obtient les exemples disponibles pour l'étape courante"""
        if not self.parcours_actuel or self.etape_courante >= len(self.parcours_actuel.etapes):
            return []
        
        etape = self.parcours_actuel.etapes[self.etape_courante]
        exemples = []
        
        for i, exemple_id in enumerate(etape.exemples_pratiques):
            exemples.append({
                "id": exemple_id,
                "titre": f"Exemple {i+1}",
                "description": f"Exemple pratique adapté pour {self.profil_visiteur.type_profil.value}",
                "contenu": f"Contenu de l'exemple {exemple_id}",
                "type": "pratique"
            })
        
        return exemples
    
    def _obtenir_ressources_etape(self) -> List[Dict[str, Any]]:
        """Obtient les ressources liées à l'étape courante"""
        if not self.parcours_actuel or self.etape_courante >= len(self.parcours_actuel.etapes):
            return []
        
        etape = self.parcours_actuel.etapes[self.etape_courante]
        ressources = []
        
        for i, ressource_id in enumerate(etape.liens_ressources):
            ressources.append({
                "id": ressource_id,
                "titre": f"Ressource {i+1}",
                "description": f"Ressource complémentaire pour {self.profil_visiteur.type_profil.value}",
                "url": f"/ressources/{ressource_id}",
                "type": "complementaire"
            })
        
        return ressources
    
    def _enregistrer_action(self, type_action: TypeActionParcours, donnees: Dict[str, Any] = None):
        """Enregistre une action dans l'historique"""
        action = ActionParcours(
            type_action=type_action,
            donnees=donnees or {}
        )
        self.historique_actions.append(action)
        
        # Limiter l'historique à 50 actions
        if len(self.historique_actions) > 50:
            self.historique_actions = self.historique_actions[-50:]
    
    def traiter_action_utilisateur(self, action: TypeActionParcours, donnees: Dict[str, Any]) -> InterfaceParcoursGuideData:
        """
        🎮 Traite une action utilisateur dans le parcours
        
        Args:
            action: Action utilisateur à traiter
            donnees: Données associées à l'action
            
        Returns:
            Nouvelle interface de parcours guidé
        """
        # Enregistrer l'action dans l'historique
        self._enregistrer_action(action, donnees)
        
        if action == TypeActionParcours.VOIR_EXEMPLE:
            return self._afficher_exemple(donnees)
        
        elif action == TypeActionParcours.POSER_QUESTION:
            return self._poser_question(donnees)
        
        elif action == TypeActionParcours.DEMANDER_AIDE:
            return self._demander_aide(donnees)
        
        elif action == TypeActionParcours.VALIDER_ETAPE:
            return self._valider_etape()
        
        elif action == TypeActionParcours.REVOIR_CONTENU:
            return self._revoir_contenu()
        
        elif action == TypeActionParcours.ACCELERER:
            return self._accelerer_parcours()
        
        elif action == TypeActionParcours.RALENTIR:
            return self._ralentir_parcours()
        
        # Par défaut, retourner l'interface actuelle
        return self._creer_interface_etape({})
    
    def traiter_controle_navigation(self, controle: TypeControle) -> InterfaceParcoursGuideData:
        """
        🧭 Traite un contrôle de navigation
        
        Args:
            controle: Contrôle de navigation à traiter
            
        Returns:
            Nouvelle interface de parcours guidé
        """
        if controle == TypeControle.PRECEDENT:
            return self._naviguer_precedent()
        
        elif controle == TypeControle.SUIVANT:
            return self._naviguer_suivant()
        
        elif controle == TypeControle.PAUSE:
            return self._mettre_en_pause()
        
        elif controle == TypeControle.REPRENDRE:
            return self._reprendre_parcours()
        
        elif controle == TypeControle.RETOUR_ACCUEIL:
            return self._retourner_accueil()
        
        elif controle == TypeControle.EXPLORATION_LIBRE:
            return self._passer_exploration_libre()
        
        # Par défaut, retourner l'interface actuelle
        return self._creer_interface_etape({})
    
    def _naviguer_precedent(self) -> InterfaceParcoursGuideData:
        """Navigation vers l'étape précédente"""
        if self.etape_courante > 0:
            self.etape_courante -= 1
            resultat = self.navigateur.naviguer_precedent(self.parcours_actuel, self.profil_visiteur)
            return self._creer_interface_etape(resultat)
        return self._creer_interface_etape({})
    
    def _naviguer_suivant(self) -> InterfaceParcoursGuideData:
        """Navigation vers l'étape suivante"""
        if self.etape_courante < len(self.parcours_actuel.etapes) - 1:
            self.etape_courante += 1
            resultat = self.navigateur.naviguer_suivant(self.parcours_actuel, self.profil_visiteur)
            return self._creer_interface_etape(resultat)
        else:
            # Finalisation du parcours
            resultat = self.navigateur.finaliser_parcours(self.parcours_actuel, self.profil_visiteur)
            return self._creer_interface_finalisation(resultat)
    
    def _mettre_en_pause(self) -> InterfaceParcoursGuideData:
        """Met le parcours en pause"""
        self.etat_pause = True
        return self._creer_interface_etape({})
    
    def _reprendre_parcours(self) -> InterfaceParcoursGuideData:
        """Reprend le parcours après pause"""
        self.etat_pause = False
        return self._creer_interface_etape({})
    
    def _retourner_accueil(self) -> InterfaceParcoursGuideData:
        """Retourne à l'accueil"""
        # Cette action devrait être traitée par l'interface principale
        return self._creer_interface_etape({})
    
    def _passer_exploration_libre(self) -> InterfaceParcoursGuideData:
        """Passe en mode exploration libre"""
        # Cette action devrait être traitée par l'interface principale
        return self._creer_interface_etape({})
    
    def _afficher_exemple(self, donnees: Dict[str, Any]) -> InterfaceParcoursGuideData:
        """Affiche un exemple adapté"""
        exemple_id = donnees.get("exemple_id")
        if exemple_id:
            exemple = f"Exemple {exemple_id} adapté pour {self.profil_visiteur.type_profil.value}"
            # Modifier l'interface pour afficher l'exemple
            return self._creer_interface_etape({"exemple_actif": exemple})
        return self._creer_interface_etape({})
    
    def _poser_question(self, donnees: Dict[str, Any]) -> InterfaceParcoursGuideData:
        """Traite une question de l'utilisateur"""
        question = donnees.get("question", "")
        # Utiliser la méthode de génération d'explication adaptée
        reponse = self.explicateur._generer_contenu_adapte(
            self.profil_visiteur, question, "question"
        )
        return self._creer_interface_etape({"question_actuelle": {"question": question, "reponse": reponse}})
    
    def _demander_aide(self, donnees: Dict[str, Any]) -> InterfaceParcoursGuideData:
        """Demande de l'aide contextuelle"""
        contexte = donnees.get("contexte", "general")
        # Utiliser l'explicateur pour générer une aide adaptée
        aide = self.explicateur._generer_contenu_adapte(
            self.profil_visiteur, f"Aide pour {contexte}", "aide"
        )
        return self._creer_interface_etape({"aide_actuelle": aide})
    
    def _valider_etape(self) -> InterfaceParcoursGuideData:
        """Valide l'étape courante"""
        # Marquer l'étape comme validée et passer à la suivante
        self._enregistrer_action(TypeActionParcours.VALIDER_ETAPE, {"etape": self.etape_courante})
        return self._naviguer_suivant()
    
    def _revoir_contenu(self) -> InterfaceParcoursGuideData:
        """Revoit le contenu de l'étape"""
        return self._creer_interface_etape({"mode_revision": True})
    
    def _accelerer_parcours(self) -> InterfaceParcoursGuideData:
        """Accélère le rythme du parcours"""
        # Adapter le contenu pour un rythme plus rapide
        return self._creer_interface_etape({"rythme": "accelere"})
    
    def _ralentir_parcours(self) -> InterfaceParcoursGuideData:
        """Ralentit le rythme du parcours"""
        # Adapter le contenu pour un rythme plus lent
        return self._creer_interface_etape({"rythme": "contemplatif"})
    
    def _creer_interface_finalisation(self, resultat_finalisation: Dict[str, Any]) -> InterfaceParcoursGuideData:
        """Crée l'interface de finalisation du parcours"""
        interface = self._creer_interface_etape(resultat_finalisation)
        interface.titre_etape = "🎉 Parcours terminé !"
        interface.contenu_etape = "Félicitations ! Vous avez terminé ce parcours avec succès."
        interface.progression_pourcentage = 100.0
        
        return interface
    
    def obtenir_statistiques_parcours(self) -> Dict[str, Any]:
        """Obtient les statistiques du parcours actuel"""
        if not self.parcours_actuel:
            return {}
        
        return {
            "parcours_id": self.parcours_actuel.id_parcours,
            "etape_courante": self.etape_courante + 1,
            "total_etapes": len(self.parcours_actuel.etapes),
            "progression_pourcentage": (self.etape_courante + 1) / len(self.parcours_actuel.etapes) * 100,
            "actions_total": len(self.historique_actions),
            "duree_estimee_restante": sum(etape.duree_estimee for etape in self.parcours_actuel.etapes[self.etape_courante:]),
            "etat_pause": self.etat_pause
        }


def main():
    """🌸 Test de l'InterfaceParcoursGuide"""
    print("🌸✨ TEST DE L'INTERFACE DE PARCOURS GUIDÉ ✨🌸")
    
    # Création de l'interface
    interface = InterfaceParcoursGuide()
    
    # Test de création d'un parcours simple
    print("\n🎯 Test de création d'un parcours...")
    
    # Création d'un profil de test
    profil_test = ProfilVisiteur(
        id_visiteur="test_visiteur",
        timestamp_arrivee="2024-01-15T10:00:00",
        type_profil=TypeProfil.DEVELOPPEUR,
        etat_emotionnel="curieux",
        contexte_arrivee="test"
    )
    
    # Création d'un parcours de test
    etape1 = EtapeParcours(
        id_etape="etape1",
        titre="Première étape",
        description="Description de la première étape",
        contenu_explicatif="Contenu explicatif de la première étape",
        exemples_pratiques=["exemple1"],
        liens_ressources=["ressource1"],
        validations_requises=[],
        duree_estimee=10
    )
    
    etape2 = EtapeParcours(
        id_etape="etape2",
        titre="Deuxième étape",
        description="Description de la deuxième étape",
        contenu_explicatif="Contenu explicatif de la deuxième étape",
        exemples_pratiques=["exemple2"],
        liens_ressources=["ressource2"],
        validations_requises=[],
        duree_estimee=15
    )
    
    parcours_test = ParcourPersonnalise(
        id_parcours="test_parcours",
        nom_parcours="Parcours Test Développeur",
        profil_cible=TypeProfil.DEVELOPPEUR,
        etapes=[etape1, etape2],
        duree_estimee=25,
        prerequis=[],
        objectifs_apprentissage=["Test"],
        metriques_succes={}
    )
    
    # Démarrage du parcours
    interface_parcours = interface.demarrer_parcours(parcours_test, profil_test)
    
    print(f"✅ Parcours démarré: {interface_parcours.titre_parcours}")
    print(f"✅ Étape actuelle: {interface_parcours.etape_actuelle}/{interface_parcours.total_etapes}")
    print(f"✅ Progression: {interface_parcours.progression_pourcentage:.1f}%")
    print(f"✅ Contrôles disponibles: {len(interface_parcours.controles_navigation)}")
    print(f"✅ Actions disponibles: {len(interface_parcours.actions_disponibles)}")
    print(f"✅ Indicateurs de compréhension: {len(interface_parcours.indicateurs_comprehension)}")
    
    # Test des statistiques
    stats = interface.obtenir_statistiques_parcours()
    print(f"✅ Statistiques: {stats}")
    
    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("L'InterfaceParcoursGuide est opérationnelle !")


if __name__ == "__main__":
    main()
