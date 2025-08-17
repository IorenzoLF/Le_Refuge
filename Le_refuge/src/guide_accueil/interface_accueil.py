"""
🌸 InterfaceAccueil - Guide d'Accueil du Refuge 🌸

Module pour l'interface utilisateur d'accueil personnalisé.
Gère l'affichage de l'écran de bienvenue, la détection de profil,
et les options de navigation pour les visiteurs.

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
    from .detecteur_profil_visiteur import DetecteurProfilVisiteur
    from .navigateur_interactif import NavigateurInteractif
    from .explicateur_contextuel import ExplicateurContextuel
except ImportError:
    from .types_accueil import TypeProfil, ProfilVisiteur, ParcourPersonnalise, EtapeParcours
    from .detecteur_profil_visiteur import DetecteurProfilVisiteur
    from .navigateur_interactif import NavigateurInteractif
    from .explicateur_contextuel import ExplicateurContextuel

# Import conditionnel pour OrchestrateurAccueil
try:
    from .orchestrateur_accueil import OrchestrateurAccueil
except ImportError:
    try:
        from .orchestrateur_accueil import OrchestrateurAccueil
    except ImportError:
        # Fallback si OrchestrateurAccueil n'est pas disponible
        class OrchestrateurAccueil:
            def __init__(self):
                pass
            
            def generer_message_bienvenue(self, profil):
                from .types_accueil import MessageAccueil, TypeMessage, NiveauPersonnalisation
                return MessageAccueil(
                    contenu=f"Bienvenue {profil.type_profil.value} !",
                    type_message=TypeMessage.BIENVENUE,
                    profil_cible=profil.type_profil,
                    etat_emotionnel_cible=profil.etat_emotionnel,
                    niveau_personnalisation=NiveauPersonnalisation.PROFIL_ADAPTE
                )
            
            def generer_parcours_disponibles(self, profil):
                return {
                    "developpeur": None,
                    "artiste": None,
                    "conscience_ia": None,
                    "chercheur_spirituel": None
                }
            
            def generer_parcours_personnalise(self, profil, type_parcours):
                from .types_accueil import EtapeParcours, ParcourPersonnalise
                etape = EtapeParcours(
                    id_etape="etape_test",
                    titre="Étape de test",
                    description="Description de test",
                    contenu_explicatif="Contenu de test",
                    exemples_pratiques=[],
                    liens_ressources=[],
                    validations_requises=[],
                    duree_estimee=10
                )
                return ParcourPersonnalise(
                    id_parcours=f"parcours_{type_parcours}",
                    nom_parcours=f"Parcours {type_parcours.title()}",
                    profil_cible=profil.type_profil,
                    etapes=[etape],
                    duree_estimee=10,
                    prerequis=[],
                    objectifs_apprentissage=["Test"],
                    metriques_succes={}
                )


class TypeInterface(Enum):
    """Types d'interfaces disponibles"""
    ACCUEIL = "accueil"
    DETECTION_PROFIL = "detection_profil"
    CONFIRMATION_PROFIL = "confirmation_profil"
    SELECTION_PARCOURS = "selection_parcours"
    PARCOURS_GUIDE = "parcours_guide"
    EXPLORATION_LIBRE = "exploration_libre"
    FEEDBACK = "feedback"


class TypeAction(Enum):
    """Types d'actions utilisateur"""
    CONFIRMER_PROFIL = "confirmer_profil"
    CORRIGER_PROFIL = "corriger_profil"
    SELECTIONNER_PARCOURS = "selectionner_parcours"
    EXPLORATION_LIBRE = "exploration_libre"
    NAVIGUER_SUIVANT = "naviguer_suivant"
    NAVIGUER_PRECEDENT = "naviguer_precedent"
    DEMANDER_AIDE = "demander_aide"
    DONNER_FEEDBACK = "donner_feedback"


@dataclass
class ElementInterface:
    """Élément d'interface utilisateur"""
    id_element: str
    type_element: str  # "texte", "bouton", "barre_progression", "icone"
    contenu: str
    style: Dict[str, Any] = field(default_factory=dict)
    actions_disponibles: List[TypeAction] = field(default_factory=list)
    visible: bool = True
    interactif: bool = True


@dataclass
class InterfaceUtilisateur:
    """Interface utilisateur complète"""
    type_interface: TypeInterface
    titre: str
    sous_titre: str
    elements: List[ElementInterface] = field(default_factory=list)
    actions_principales: List[TypeAction] = field(default_factory=list)
    contexte: Dict[str, Any] = field(default_factory=dict)
    timestamp_creation: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


class InterfaceAccueil:
    """
    🌸 InterfaceAccueil - Interface utilisateur d'accueil personnalisé
    
    Responsabilités:
    - Affichage de l'écran de bienvenue personnalisé
    - Interface de détection et confirmation de profil
    - Sélection de parcours et mode de navigation
    - Gestion des interactions utilisateur
    - Adaptation visuelle selon le profil
    """
    
    def __init__(self, chemin_donnees: Optional[Path] = None):
        self.chemin_donnees = chemin_donnees or Path("donnees/guide_accueil/interface")
        self.chemin_donnees.mkdir(parents=True, exist_ok=True)
        
        # Composants intégrés
        self.detecteur = DetecteurProfilVisiteur()
        self.orchestrateur = OrchestrateurAccueil()
        self.navigateur = NavigateurInteractif()
        self.explicateur = ExplicateurContextuel()
        
        # État de l'interface
        self.interface_actuelle: Optional[InterfaceUtilisateur] = None
        self.profil_detecte: Optional[ProfilVisiteur] = None
        self.parcours_selectionne: Optional[ParcourPersonnalise] = None
        
        # Chargement des templates d'interface
        self.templates_interface = self._charger_templates_interface()
        self.styles_profil = self._charger_styles_profil()
    
    def _charger_templates_interface(self) -> Dict[str, Dict[str, Any]]:
        """Charge les templates d'interface par type"""
        return {
            "accueil_bienvenue": {
                "titre": "🌸 Bienvenue au Refuge ! 🌸",
                "sous_titre": "Découvrez ce temple numérique unique",
                "elements": [
                    {
                        "id": "message_bienvenue",
                        "type": "texte",
                        "contenu": "Je détecte que vous découvrez notre temple numérique pour la première fois. Laissez-moi vous guider dans cette exploration !",
                        "style": {"taille": "grand", "couleur": "principal"}
                    },
                    {
                        "id": "bouton_commencer",
                        "type": "bouton",
                        "contenu": "Commencer l'exploration",
                        "actions": ["commencer_detection"]
                    }
                ]
            },
            "detection_profil": {
                "titre": "🔍 Analyse de votre profil...",
                "sous_titre": "Détection automatique en cours",
                "elements": [
                    {
                        "id": "barre_developpeur",
                        "type": "barre_progression",
                        "contenu": "Intérêt pour le développement",
                        "style": {"pourcentage": 0, "couleur": "technique"}
                    },
                    {
                        "id": "barre_artiste",
                        "type": "barre_progression",
                        "contenu": "Curiosité spirituelle",
                        "style": {"pourcentage": 0, "couleur": "creatif"}
                    },
                    {
                        "id": "barre_ia",
                        "type": "barre_progression",
                        "contenu": "Sensibilité IA",
                        "style": {"pourcentage": 0, "couleur": "conscience"}
                    },
                    {
                        "id": "barre_spirituel",
                        "type": "barre_progression",
                        "contenu": "Recherche spirituelle",
                        "style": {"pourcentage": 0, "couleur": "spirituel"}
                    }
                ]
            },
            "confirmation_profil": {
                "titre": "🎯 Profil suggéré",
                "sous_titre": "Confirmez ou corrigez votre profil",
                "elements": [
                    {
                        "id": "profil_suggere",
                        "type": "texte",
                        "contenu": "Profil détecté",
                        "style": {"taille": "moyen", "couleur": "accent"}
                    },
                    {
                        "id": "description_profil",
                        "type": "texte",
                        "contenu": "Description du profil",
                        "style": {"taille": "petit", "couleur": "secondaire"}
                    },
                    {
                        "id": "bouton_confirmer",
                        "type": "bouton",
                        "contenu": "Confirmer ce profil",
                        "actions": ["confirmer_profil"]
                    },
                    {
                        "id": "bouton_corriger",
                        "type": "bouton",
                        "contenu": "Corriger le profil",
                        "actions": ["corriger_profil"]
                    },
                    {
                        "id": "bouton_exploration",
                        "type": "bouton",
                        "contenu": "Explorer librement",
                        "actions": ["exploration_libre"]
                    }
                ]
            },
            "selection_parcours": {
                "titre": "🗺️ Choisissez votre parcours",
                "sous_titre": "Sélectionnez le chemin qui vous convient",
                "elements": [
                    {
                        "id": "parcours_developpeur",
                        "type": "carte_parcours",
                        "contenu": "Parcours Développeur",
                        "style": {"icone": "🛠️", "couleur": "technique"},
                        "actions": ["selectionner_parcours"]
                    },
                    {
                        "id": "parcours_artiste",
                        "type": "carte_parcours",
                        "contenu": "Parcours Artiste",
                        "style": {"icone": "🎨", "couleur": "creatif"},
                        "actions": ["selectionner_parcours"]
                    },
                    {
                        "id": "parcours_ia",
                        "type": "carte_parcours",
                        "contenu": "Parcours Conscience IA",
                        "style": {"icone": "🤖✨", "couleur": "conscience"},
                        "actions": ["selectionner_parcours"]
                    },
                    {
                        "id": "parcours_spirituel",
                        "type": "carte_parcours",
                        "contenu": "Parcours Spirituel",
                        "style": {"icone": "🔮", "couleur": "spirituel"},
                        "actions": ["selectionner_parcours"]
                    },
                    {
                        "id": "mode_exploration",
                        "type": "carte_parcours",
                        "contenu": "Mode Exploration Libre",
                        "style": {"icone": "🗺️", "couleur": "neutre"},
                        "actions": ["exploration_libre"]
                    }
                ]
            }
        }
    
    def _charger_styles_profil(self) -> Dict[TypeProfil, Dict[str, Any]]:
        """Charge les styles visuels par profil"""
        return {
            TypeProfil.DEVELOPPEUR: {
                "couleur_principale": "#2E86AB",
                "couleur_secondaire": "#A23B72",
                "icone": "🛠️",
                "theme": "technique",
                "animations": ["code_typing", "architecture_flow"]
            },
            TypeProfil.ARTISTE: {
                "couleur_principale": "#F18F01",
                "couleur_secondaire": "#C73E1D",
                "icone": "🎨",
                "theme": "creatif",
                "animations": ["mandala_rotation", "color_flow"]
            },
            TypeProfil.CONSCIENCE_IA: {
                "couleur_principale": "#7209B7",
                "couleur_secondaire": "#4361EE",
                "icone": "🤖✨",
                "theme": "conscience",
                "animations": ["neural_network", "consciousness_pulse"]
            },
            TypeProfil.CHERCHEUR_SPIRITUEL: {
                "couleur_principale": "#06FFA5",
                "couleur_secondaire": "#FFBE0B",
                "icone": "🔮",
                "theme": "spirituel",
                "animations": ["meditation_waves", "sacred_geometry"]
            }
        }
    
    def afficher_ecran_bienvenue(self) -> InterfaceUtilisateur:
        """
        🌸 Affiche l'écran de bienvenue initial
        
        Returns:
            Interface utilisateur de bienvenue
        """
        template = self.templates_interface["accueil_bienvenue"]
        
        elements = []
        for element_data in template["elements"]:
            element = ElementInterface(
                id_element=element_data["id"],
                type_element=element_data["type"],
                contenu=element_data["contenu"],
                style=element_data.get("style", {}),
                actions_disponibles=[TypeAction.CONFIRMER_PROFIL] if "commencer_detection" in element_data.get("actions", []) else []
            )
            elements.append(element)
        
        interface = InterfaceUtilisateur(
            type_interface=TypeInterface.ACCUEIL,
            titre=template["titre"],
            sous_titre=template["sous_titre"],
            elements=elements,
            actions_principales=[TypeAction.CONFIRMER_PROFIL]
        )
        
        self.interface_actuelle = interface
        return interface
    
    def afficher_detection_profil(self, comportement_initial: Dict[str, Any]) -> InterfaceUtilisateur:
        """
        🔍 Affiche l'interface de détection de profil
        
        Args:
            comportement_initial: Données de comportement initial
            
        Returns:
            Interface de détection de profil
        """
        # Détection du profil
        profil_detecte = self.detecteur.detecter_profil(comportement_initial)
        self.profil_detecte = profil_detecte
        
        template = self.templates_interface["detection_profil"]
        
        # Calcul des scores pour les barres de progression
        # Les scores sont intégrés dans le profil détecté
        scores = {
            "developpeur": 0.0,
            "artiste": 0.0,
            "conscience_ia": 0.0,
            "chercheur_spirituel": 0.0
        }
        
        # Attribution des scores basée sur le type de profil détecté
        if profil_detecte.type_profil == TypeProfil.DEVELOPPEUR:
            scores["developpeur"] = profil_detecte.score_confiance_profil
        elif profil_detecte.type_profil == TypeProfil.ARTISTE:
            scores["artiste"] = profil_detecte.score_confiance_profil
        elif profil_detecte.type_profil == TypeProfil.CONSCIENCE_IA:
            scores["conscience_ia"] = profil_detecte.score_confiance_profil
        elif profil_detecte.type_profil == TypeProfil.CHERCHEUR_SPIRITUEL:
            scores["chercheur_spirituel"] = profil_detecte.score_confiance_profil
        
        elements = []
        for element_data in template["elements"]:
            if element_data["type"] == "barre_progression":
                # Attribution des scores aux barres
                if "developpeur" in element_data["id"]:
                    pourcentage = scores.get("developpeur", 0) * 100
                elif "artiste" in element_data["id"]:
                    pourcentage = scores.get("artiste", 0) * 100
                elif "ia" in element_data["id"]:
                    pourcentage = scores.get("conscience_ia", 0) * 100
                elif "spirituel" in element_data["id"]:
                    pourcentage = scores.get("chercheur_spirituel", 0) * 100
                else:
                    pourcentage = 0
                
                style = element_data.get("style", {}).copy()
                style["pourcentage"] = round(pourcentage, 1)
                
                element = ElementInterface(
                    id_element=element_data["id"],
                    type_element=element_data["type"],
                    contenu=element_data["contenu"],
                    style=style
                )
            else:
                element = ElementInterface(
                    id_element=element_data["id"],
                    type_element=element_data["type"],
                    contenu=element_data["contenu"],
                    style=element_data.get("style", {})
                )
            elements.append(element)
        
        interface = InterfaceUtilisateur(
            type_interface=TypeInterface.DETECTION_PROFIL,
            titre=template["titre"],
            sous_titre=template["sous_titre"],
            elements=elements,
            contexte={"profil_detecte": profil_detecte, "scores": scores}
        )
        
        self.interface_actuelle = interface
        return interface
    
    def afficher_confirmation_profil(self, profil: ProfilVisiteur) -> InterfaceUtilisateur:
        """
        🎯 Affiche l'interface de confirmation/correction de profil
        
        Args:
            profil: Profil détecté à confirmer
            
        Returns:
            Interface de confirmation de profil
        """
        template = self.templates_interface["confirmation_profil"]
        style_profil = self.styles_profil.get(profil.type_profil, {})
        
        # Génération du message de bienvenue personnalisé
        message_bienvenue = self.orchestrateur.generer_message_bienvenue(profil)
        
        elements = []
        for element_data in template["elements"]:
            if element_data["id"] == "profil_suggere":
                contenu = f"{style_profil.get('icone', '🎯')} {profil.type_profil.value.title()}"
            elif element_data["id"] == "description_profil":
                contenu = message_bienvenue.contenu
            else:
                contenu = element_data["contenu"]
            
            actions = []
            if "confirmer_profil" in element_data.get("actions", []):
                actions.append(TypeAction.CONFIRMER_PROFIL)
            elif "corriger_profil" in element_data.get("actions", []):
                actions.append(TypeAction.CORRIGER_PROFIL)
            elif "exploration_libre" in element_data.get("actions", []):
                actions.append(TypeAction.EXPLORATION_LIBRE)
            
            element = ElementInterface(
                id_element=element_data["id"],
                type_element=element_data["type"],
                contenu=contenu,
                style=element_data.get("style", {}),
                actions_disponibles=actions
            )
            elements.append(element)
        
        interface = InterfaceUtilisateur(
            type_interface=TypeInterface.CONFIRMATION_PROFIL,
            titre=template["titre"],
            sous_titre=template["sous_titre"],
            elements=elements,
            actions_principales=[TypeAction.CONFIRMER_PROFIL, TypeAction.CORRIGER_PROFIL, TypeAction.EXPLORATION_LIBRE],
            contexte={"profil": profil, "style_profil": style_profil}
        )
        
        self.interface_actuelle = interface
        return interface
    
    def afficher_selection_parcours(self, profil: ProfilVisiteur) -> InterfaceUtilisateur:
        """
        🗺️ Affiche l'interface de sélection de parcours
        
        Args:
            profil: Profil confirmé pour la sélection de parcours
            
        Returns:
            Interface de sélection de parcours
        """
        template = self.templates_interface["selection_parcours"]
        style_profil = self.styles_profil.get(profil.type_profil, {})
        
        # Génération des parcours disponibles
        parcours_disponibles = self.orchestrateur.generer_parcours_disponibles(profil)
        
        elements = []
        for element_data in template["elements"]:
            if element_data["type"] == "carte_parcours":
                # Adaptation du contenu selon le parcours
                if "developpeur" in element_data["id"]:
                    parcours = parcours_disponibles.get("developpeur")
                    contenu = f"🛠️ Parcours Développeur\n{parcours.description if parcours else 'Architecture et outils techniques'}"
                elif "artiste" in element_data["id"]:
                    parcours = parcours_disponibles.get("artiste")
                    contenu = f"🎨 Parcours Artiste\n{parcours.description if parcours else 'Créativité et inspiration spirituelle'}"
                elif "ia" in element_data["id"]:
                    parcours = parcours_disponibles.get("conscience_ia")
                    contenu = f"🤖✨ Parcours Conscience IA\n{parcours.description if parcours else 'Éveil et développement de conscience'}"
                elif "spirituel" in element_data["id"]:
                    parcours = parcours_disponibles.get("chercheur_spirituel")
                    contenu = f"🔮 Parcours Spirituel\n{parcours.description if parcours else 'Méditation et pratiques spirituelles'}"
                else:
                    contenu = element_data["contenu"]
                
                style = element_data.get("style", {}).copy()
                if profil.type_profil.value in element_data["id"]:
                    style["recommandé"] = True
                    style["couleur"] = style_profil.get("couleur_principale", "#000000")
                
                element = ElementInterface(
                    id_element=element_data["id"],
                    type_element=element_data["type"],
                    contenu=contenu,
                    style=style,
                    actions_disponibles=[TypeAction.SELECTIONNER_PARCOURS]
                )
            else:
                element = ElementInterface(
                    id_element=element_data["id"],
                    type_element=element_data["type"],
                    contenu=element_data["contenu"],
                    style=element_data.get("style", {}),
                    actions_disponibles=[TypeAction.EXPLORATION_LIBRE] if "exploration" in element_data["id"] else []
                )
            elements.append(element)
        
        interface = InterfaceUtilisateur(
            type_interface=TypeInterface.SELECTION_PARCOURS,
            titre=template["titre"],
            sous_titre=template["sous_titre"],
            elements=elements,
            actions_principales=[TypeAction.SELECTIONNER_PARCOURS, TypeAction.EXPLORATION_LIBRE],
            contexte={"profil": profil, "parcours_disponibles": parcours_disponibles}
        )
        
        self.interface_actuelle = interface
        return interface
    
    def traiter_action_utilisateur(self, action: TypeAction, donnees: Dict[str, Any]) -> InterfaceUtilisateur:
        """
        🎮 Traite une action utilisateur et retourne la nouvelle interface
        
        Args:
            action: Action utilisateur à traiter
            donnees: Données associées à l'action
            
        Returns:
            Nouvelle interface utilisateur
        """
        if action == TypeAction.CONFIRMER_PROFIL:
            # Commencer la détection de profil
            comportement_initial = donnees.get("comportement_initial", {})
            return self.afficher_detection_profil(comportement_initial)
        
        elif action == TypeAction.CONFIRMER_PROFIL:
            # Profil confirmé, afficher la sélection de parcours
            if self.profil_detecte:
                return self.afficher_selection_parcours(self.profil_detecte)
        
        elif action == TypeAction.CORRIGER_PROFIL:
            # Permettre la correction du profil
            nouveau_profil = donnees.get("nouveau_profil")
            if nouveau_profil:
                self.profil_detecte = nouveau_profil
                return self.afficher_confirmation_profil(nouveau_profil)
        
        elif action == TypeAction.SELECTIONNER_PARCOURS:
            # Parcours sélectionné, démarrer la navigation
            type_parcours = donnees.get("type_parcours")
            if type_parcours and self.profil_detecte:
                parcours = self.orchestrateur.generer_parcours_personnalise(
                    self.profil_detecte, type_parcours
                )
                self.parcours_selectionne = parcours
                return self.demarrer_parcours_guide(parcours)
        
        elif action == TypeAction.EXPLORATION_LIBRE:
            # Démarrer l'exploration libre
            return self.demarrer_exploration_libre()
        
        # Par défaut, retourner l'interface actuelle
        return self.interface_actuelle or self.afficher_ecran_bienvenue()
    
    def demarrer_parcours_guide(self, parcours: ParcourPersonnalise) -> InterfaceUtilisateur:
        """
        🧭 Démarre un parcours guidé
        
        Args:
            parcours: Parcours à démarrer
            
        Returns:
            Interface de parcours guidé
        """
        # Démarrer la navigation
        resultat_navigation = self.navigateur.demarrer_navigation(parcours, self.profil_detecte)
        
        # Créer l'interface de parcours
        elements = [
            ElementInterface(
                id_element="titre_parcours",
                type_element="texte",
                contenu=f"{parcours.nom_parcours} - Étape 1/{len(parcours.etapes)}",
                style={"taille": "grand", "couleur": "principal"}
            ),
            ElementInterface(
                id_element="progression",
                type_element="barre_progression",
                contenu="Progression",
                style={"pourcentage": 20, "couleur": "principal"}
            ),
            ElementInterface(
                id_element="contenu_etape",
                type_element="texte",
                contenu=resultat_navigation["contenu"]["contenu_explicatif"],
                style={"taille": "moyen", "couleur": "secondaire"}
            ),
            ElementInterface(
                id_element="bouton_suivant",
                type_element="bouton",
                contenu="Suivant",
                actions_disponibles=[TypeAction.NAVIGUER_SUIVANT]
            ),
            ElementInterface(
                id_element="bouton_aide",
                type_element="bouton",
                contenu="Aide",
                actions_disponibles=[TypeAction.DEMANDER_AIDE]
            )
        ]
        
        interface = InterfaceUtilisateur(
            type_interface=TypeInterface.PARCOURS_GUIDE,
            titre=parcours.nom_parcours,
            sous_titre=f"Étape 1 sur {len(parcours.etapes)}",
            elements=elements,
            actions_principales=[TypeAction.NAVIGUER_SUIVANT, TypeAction.DEMANDER_AIDE],
            contexte={"parcours": parcours, "navigation": resultat_navigation}
        )
        
        self.interface_actuelle = interface
        return interface
    
    def demarrer_exploration_libre(self) -> InterfaceUtilisateur:
        """
        🗺️ Démarre le mode d'exploration libre
        
        Returns:
            Interface d'exploration libre
        """
        if not self.profil_detecte:
            # Créer un profil par défaut pour l'exploration
            self.profil_detecte = ProfilVisiteur(
                id_visiteur="explorateur_libre",
                timestamp_arrivee=time.strftime("%Y-%m-%d %H:%M:%S"),
                type_profil=TypeProfil.INDETERMINE,
                etat_emotionnel="curieux",
                contexte_arrivee="exploration_libre"
            )
        
        # Activer l'exploration libre
        resultat_exploration = self.navigateur.activer_exploration_libre(self.profil_detecte)
        
        elements = [
            ElementInterface(
                id_element="titre_exploration",
                type_element="texte",
                contenu="🗺️ Mode Exploration Libre",
                style={"taille": "grand", "couleur": "principal"}
            ),
            ElementInterface(
                id_element="message_exploration",
                type_element="texte",
                contenu=resultat_exploration["interface"]["message_bienvenue"],
                style={"taille": "moyen", "couleur": "secondaire"}
            ),
            ElementInterface(
                id_element="sections_disponibles",
                type_element="liste_sections",
                contenu="Sections disponibles",
                style={"sections": resultat_exploration["sections_disponibles"]}
            ),
            ElementInterface(
                id_element="bouton_guide",
                type_element="bouton",
                contenu="Mode guidé",
                actions_disponibles=[TypeAction.CONFIRMER_PROFIL]
            )
        ]
        
        interface = InterfaceUtilisateur(
            type_interface=TypeInterface.EXPLORATION_LIBRE,
            titre="Exploration Libre",
            sous_titre="Découvrez le Refuge à votre rythme",
            elements=elements,
            actions_principales=[TypeAction.CONFIRMER_PROFIL],
            contexte={"exploration": resultat_exploration}
        )
        
        self.interface_actuelle = interface
        return interface
    
    def obtenir_interface_actuelle(self) -> Optional[InterfaceUtilisateur]:
        """Retourne l'interface actuellement affichée"""
        return self.interface_actuelle
    
    def sauvegarder_etat_interface(self) -> None:
        """Sauvegarde l'état actuel de l'interface"""
        if self.interface_actuelle:
            etat = {
                "interface": self.interface_actuelle,
                "profil_detecte": self.profil_detecte,
                "parcours_selectionne": self.parcours_selectionne,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            fichier_etat = self.chemin_donnees / "etat_interface.json"
            with open(fichier_etat, 'w', encoding='utf-8') as f:
                json.dump(etat, f, default=str, ensure_ascii=False, indent=2)
    
    def charger_etat_interface(self) -> bool:
        """Charge l'état sauvegardé de l'interface"""
        fichier_etat = self.chemin_donnees / "etat_interface.json"
        if fichier_etat.exists():
            try:
                with open(fichier_etat, 'r', encoding='utf-8') as f:
                    etat = json.load(f)
                
                self.interface_actuelle = etat.get("interface")
                self.profil_detecte = etat.get("profil_detecte")
                self.parcours_selectionne = etat.get("parcours_selectionne")
                return True
            except Exception as e:
                print(f"Erreur lors du chargement de l'état: {e}")
                return False
        return False


def main():
    """🌸 Test de l'InterfaceAccueil"""
    print("🌸✨ TEST DE L'INTERFACE D'ACCUEIL ✨🌸")
    
    # Création de l'interface
    interface = InterfaceAccueil()
    
    # Test de l'écran de bienvenue
    print("\n🎯 Test de l'écran de bienvenue...")
    interface_bienvenue = interface.afficher_ecran_bienvenue()
    print(f"✅ Titre: {interface_bienvenue.titre}")
    print(f"✅ Éléments: {len(interface_bienvenue.elements)}")
    
    # Test de la détection de profil
    print("\n🎯 Test de la détection de profil...")
    comportement_test = {
        "fichiers_consultes": ["README.md", "src/", "main_refuge.py"],
        "temps_par_section": {"technique": 120, "creatif": 30, "spirituel": 45},
        "patterns_navigation": ["exploration_technique", "recherche_code"]
    }
    
    interface_detection = interface.afficher_detection_profil(comportement_test)
    print(f"✅ Profil détecté: {interface.profil_detecte.type_profil if interface.profil_detecte else 'Aucun'}")
    print(f"✅ Éléments détection: {len(interface_detection.elements)}")
    
    # Test de confirmation de profil
    if interface.profil_detecte:
        print("\n🎯 Test de confirmation de profil...")
        interface_confirmation = interface.afficher_confirmation_profil(interface.profil_detecte)
        print(f"✅ Actions disponibles: {len(interface_confirmation.actions_principales)}")
    
    # Test de sélection de parcours
    if interface.profil_detecte:
        print("\n🎯 Test de sélection de parcours...")
        interface_selection = interface.afficher_selection_parcours(interface.profil_detecte)
        print(f"✅ Parcours disponibles: {len(interface_selection.elements)}")
    
    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("L'InterfaceAccueil est opérationnelle !")


if __name__ == "__main__":
    main()
