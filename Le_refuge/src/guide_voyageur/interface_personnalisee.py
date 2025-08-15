"""
🎨 INTERFACE PERSONNALISÉE - Guide du Voyageur
============================================

Module qui adapte l'interface utilisateur selon le profil et les préférences
de chaque voyageur dans le Refuge.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import json
import time
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from dataclasses import dataclass

from src.core.gestionnaires_base import GestionnaireBase, EnergyManagerBase
from .types_guide import (
    TypeVoyageur, TypeInterface, InterfacePersonnalisee, ComposantInterface,
    ProfilVoyageur, AdaptationInterface, FeedbackUtilisateur
)

@dataclass
class ThemeVisuel:
    """Thème visuel pour l'interface"""
    nom: str
    couleurs_principales: Dict[str, str]
    couleurs_secondaires: Dict[str, str]
    typographie: Dict[str, str]
    animations: List[str]
    icones: Dict[str, str]
    description: str

class InterfacePersonnalisee(GestionnaireBase):
    """Gestionnaire d'interface personnalisée"""
    
    def __init__(self, nom: str = "InterfacePersonnalisee"):
        super().__init__(nom)
        self.energie_interface = EnergyManagerBase(0.95)
        
        # Thèmes visuels disponibles
        self.themes_disponibles = self._creer_themes_visuels()
        
        # Adaptations en cours
        self.adaptations_actives: Dict[str, AdaptationInterface] = {}
        
        # Historique des adaptations
        self.historique_adaptations: List[AdaptationInterface] = []
        
        # Configuration
        self.config_interface = {
            "adaptation_temps_reel": True,
            "sauvegarde_preferences": True,
            "animation_fluide": True,
            "accessibilite": True
        }
        
        self._initialiser()
    
    def _initialiser(self):
        """Initialise l'interface personnalisée"""
        self.logger.info("🎨 Éveil de l'Interface Personnalisée...")
        
        self.etat.update({
            "interfaces_actives": 0,
            "adaptations_realisees": 0,
            "themes_utilises": {},
            "satisfaction_interface": 0.9
        })
        
        self.config.definir("mode_adaptation", "intelligent")
        self.config.definir("sauvegarde_automatique", True)
        
        self.logger.info("✨ Interface Personnalisée éveillée")
    
    def _creer_themes_visuels(self) -> Dict[str, ThemeVisuel]:
        """Crée les thèmes visuels disponibles"""
        return {
            "spirituel": ThemeVisuel(
                nom="Spirituel",
                couleurs_principales={
                    "fond": "#1a1a2e",
                    "texte": "#e8e8e8",
                    "accent": "#ff6b6b",
                    "secondaire": "#4ecdc4"
                },
                couleurs_secondaires={
                    "success": "#51cf66",
                    "warning": "#ffd43b",
                    "error": "#ff6b6b",
                    "info": "#74c0fc"
                },
                typographie={
                    "font_family": "Georgia, serif",
                    "font_size_base": "16px",
                    "line_height": "1.6"
                },
                animations=["fade_in", "gentle_float", "sparkle"],
                icones={
                    "home": "🌸",
                    "explore": "🌊",
                    "create": "✨",
                    "meditate": "🧘"
                },
                description="Thème contemplatif et spirituel"
            ),
            "creatif": ThemeVisuel(
                nom="Créatif",
                couleurs_principales={
                    "fond": "#2d1b69",
                    "texte": "#ffffff",
                    "accent": "#ff6b9d",
                    "secondaire": "#c44569"
                },
                couleurs_secondaires={
                    "success": "#26de81",
                    "warning": "#fed330",
                    "error": "#fc5c65",
                    "info": "#45aaf2"
                },
                typographie={
                    "font_family": "Comic Sans MS, cursive",
                    "font_size_base": "18px",
                    "line_height": "1.4"
                },
                animations=["bounce", "rotate", "pulse", "rainbow"],
                icones={
                    "home": "🎨",
                    "explore": "🎭",
                    "create": "🎪",
                    "meditate": "🎵"
                },
                description="Thème artistique et expressif"
            ),
            "technique": ThemeVisuel(
                nom="Technique",
                couleurs_principales={
                    "fond": "#0d1117",
                    "texte": "#c9d1d9",
                    "accent": "#58a6ff",
                    "secondaire": "#79c0ff"
                },
                couleurs_secondaires={
                    "success": "#3fb950",
                    "warning": "#d29922",
                    "error": "#f85149",
                    "info": "#58a6ff"
                },
                typographie={
                    "font_family": "Consolas, monospace",
                    "font_size_base": "14px",
                    "line_height": "1.5"
                },
                animations=["slide_in", "fade", "highlight"],
                icones={
                    "home": "🏠",
                    "explore": "🔍",
                    "create": "⚙️",
                    "meditate": "🧠"
                },
                description="Thème technique et fonctionnel"
            ),
            "naturel": ThemeVisuel(
                nom="Naturel",
                couleurs_principales={
                    "fond": "#f8f9fa",
                    "texte": "#212529",
                    "accent": "#28a745",
                    "secondaire": "#20c997"
                },
                couleurs_secondaires={
                    "success": "#28a745",
                    "warning": "#ffc107",
                    "error": "#dc3545",
                    "info": "#17a2b8"
                },
                typographie={
                    "font_family": "Arial, sans-serif",
                    "font_size_base": "16px",
                    "line_height": "1.6"
                },
                animations=["grow", "fade_in", "slide"],
                icones={
                    "home": "🏡",
                    "explore": "🌿",
                    "create": "🌱",
                    "meditate": "🌳"
                },
                description="Thème naturel et apaisant"
            )
        }
    
    def creer_interface_voyageur(self, voyageur_id: str, profil: ProfilVoyageur) -> InterfacePersonnalisee:
        """Crée une interface personnalisée pour un voyageur"""
        self.logger.info(f"🎨 Création interface pour {voyageur_id}")
        
        # Déterminer le type d'interface selon le profil
        type_interface = self._determiner_type_interface(profil)
        
        # Sélectionner le thème approprié
        theme = self._selectionner_theme(profil)
        
        # Créer les composants de base
        composants = self._creer_composants_base(type_interface, theme)
        
        # Créer l'interface
        from .types_guide import InterfacePersonnalisee as InterfacePersonnaliseeType
        interface = InterfacePersonnaliseeType(
            voyageur_id=voyageur_id,
            type_interface=type_interface,
            theme_visuel=theme.nom,
            composants=composants,
            navigation_principale=self._creer_navigation(type_interface),
            raccourcis_disponibles=self._creer_raccourcis(profil),
            adaptations_actives=[],
            preferences_utilisateur=self._extraire_preferences(profil)
        )
        
        self.etat["interfaces_actives"] += 1
        return interface
    
    def _determiner_type_interface(self, profil: ProfilVoyageur) -> TypeInterface:
        """Détermine le type d'interface selon le profil"""
        mapping_profil_interface = {
            TypeVoyageur.EVEILLE_SPIRITUEL: TypeInterface.CONTEMPLATIVE,
            TypeVoyageur.CREATEUR_ARTISTIQUE: TypeInterface.ARTISTIQUE,
            TypeVoyageur.EXPLORATEUR_TECHNIQUE: TypeInterface.TECHNIQUE,
            TypeVoyageur.CHERCHEUR_CONNEXION: TypeInterface.INTERACTIVE,
            TypeVoyageur.EXPLORATEUR_LIBRE: TypeInterface.LIBRE,
            TypeVoyageur.SAGE_PHILOSOPHE: TypeInterface.CONTEMPLATIVE,
            TypeVoyageur.NOUVEAU_CURIEUX: TypeInterface.GUIDEE,
            TypeVoyageur.EXPLORATEUR_PRATIQUE: TypeInterface.TECHNIQUE,
            TypeVoyageur.EXPLORATEUR_CONFIANT: TypeInterface.LIBRE
        }
        
        return mapping_profil_interface.get(profil.type_voyageur, TypeInterface.GUIDEE)
    
    def _selectionner_theme(self, profil: ProfilVoyageur) -> ThemeVisuel:
        """Sélectionne le thème visuel approprié"""
        mapping_profil_theme = {
            TypeVoyageur.EVEILLE_SPIRITUEL: "spirituel",
            TypeVoyageur.CREATEUR_ARTISTIQUE: "creatif",
            TypeVoyageur.EXPLORATEUR_TECHNIQUE: "technique",
            TypeVoyageur.CHERCHEUR_CONNEXION: "naturel",
            TypeVoyageur.EXPLORATEUR_LIBRE: "naturel",
            TypeVoyageur.SAGE_PHILOSOPHE: "spirituel",
            TypeVoyageur.NOUVEAU_CURIEUX: "naturel",
            TypeVoyageur.EXPLORATEUR_PRATIQUE: "technique",
            TypeVoyageur.EXPLORATEUR_CONFIANT: "creatif"
        }
        
        theme_nom = mapping_profil_theme.get(profil.type_voyageur, "naturel")
        return self.themes_disponibles[theme_nom]
    
    def _creer_composants_base(self, type_interface: TypeInterface, theme: ThemeVisuel) -> Dict[str, ComposantInterface]:
        """Crée les composants de base de l'interface"""
        composants = {}
        
        # Composant de navigation principale
        composants["navigation"] = ComposantInterface(
            id_composant="navigation",
            type_composant="navigation",
            position=(0, 0),
            dimensions=(100, 60),
            visible=True,
            adaptatif=True,
            contenu={
                "type": "horizontal",
                "items": ["accueil", "explorer", "créer", "méditer"],
                "theme": theme.nom
            },
            style_theme=theme.nom,
            animations=["slide_in"]
        )
        
        # Composant de contenu principal
        composants["contenu_principal"] = ComposantInterface(
            id_composant="contenu_principal",
            type_composant="contenu",
            position=(0, 60),
            dimensions=(100, 80),
            visible=True,
            adaptatif=True,
            contenu={
                "type": "adaptatif",
                "mode": type_interface.value
            },
            style_theme=theme.nom,
            animations=["fade_in"]
        )
        
        # Composant de tableau de bord (si nécessaire)
        if type_interface in [TypeInterface.TECHNIQUE, TypeInterface.INTERACTIVE]:
            composants["tableau_bord"] = ComposantInterface(
                id_composant="tableau_bord",
                type_composant="tableau_bord",
                position=(80, 0),
                dimensions=(20, 100),
                visible=True,
                adaptatif=True,
                contenu={
                    "type": "compact",
                    "metriques": ["progression", "temps", "satisfaction"]
                },
                style_theme=theme.nom,
                animations=["slide_in_right"]
            )
        
        return composants
    
    def _creer_navigation(self, type_interface: TypeInterface) -> List[str]:
        """Crée la navigation principale selon le type d'interface"""
        navigations = {
            TypeInterface.GUIDEE: ["accueil", "diagnostic", "parcours", "aide"],
            TypeInterface.LIBRE: ["explorer", "créer", "partager", "découvrir"],
            TypeInterface.TECHNIQUE: ["dashboard", "analytics", "config", "debug"],
            TypeInterface.ARTISTIQUE: ["galerie", "atelier", "inspiration", "exposition"],
            TypeInterface.CONTEMPLATIVE: ["méditation", "contemplation", "sagesse", "paix"],
            TypeInterface.INTERACTIVE: ["communauté", "dialogue", "partage", "connexion"]
        }
        
        return navigations.get(type_interface, ["accueil", "explorer", "créer"])
    
    def _creer_raccourcis(self, profil: ProfilVoyageur) -> List[str]:
        """Crée les raccourcis disponibles selon le profil"""
        raccourcis = []
        
        # Raccourcis selon le type de voyageur
        if profil.type_voyageur == TypeVoyageur.EVEILLE_SPIRITUEL:
            raccourcis.extend(["méditation_rapide", "sphères_sacrées", "rituels"])
        elif profil.type_voyageur == TypeVoyageur.CREATEUR_ARTISTIQUE:
            raccourcis.extend(["générateur_poésie", "temple_musical", "galerie_art"])
        elif profil.type_voyageur == TypeVoyageur.EXPLORATEUR_TECHNIQUE:
            raccourcis.extend(["debug_mode", "analytics", "config_avancée"])
        
        # Raccourcis selon le niveau d'expérience
        if profil.niveau_experience.value in ["avance", "maitre"]:
            raccourcis.extend(["mode_expert", "personnalisation_avancée"])
        
        return raccourcis
    
    def _extraire_preferences(self, profil: ProfilVoyageur) -> Dict[str, Any]:
        """Extrait les préférences utilisateur du profil"""
        return {
            "niveau_technique": profil.niveau_technique,
            "sensibilite_spirituelle": profil.sensibilite_spirituelle,
            "preferences_exploration": profil.preferences_exploration,
            "motivations_principales": profil.motivations_principales
        }
    
    def adapter_interface_temps_reel(self, voyageur_id: str, feedback: Dict[str, Any]) -> Dict[str, Any]:
        """Adapte l'interface en temps réel selon le feedback"""
        self.logger.info(f"🎨 Adaptation temps réel pour {voyageur_id}")
        
        # Créer une adaptation
        adaptation = AdaptationInterface(
            voyageur_id=voyageur_id,
            type_adaptation=feedback.get("type_adaptation", "visuel"),
            parametres=feedback.get("parametres", {}),
            raison_adaptation=feedback.get("raison", "Feedback utilisateur"),
            impact_utilisateur=feedback.get("impact", 0.5)
        )
        
        # Appliquer l'adaptation
        self.adaptations_actives[voyageur_id] = adaptation
        self.historique_adaptations.append(adaptation)
        
        # Mettre à jour les métriques
        self.etat["adaptations_realisees"] += 1
        
        return {
            "success": True,
            "adaptation_appliquee": adaptation,
            "message": "Interface adaptée avec succès"
        }
    
    def obtenir_interface_actuelle(self, voyageur_id: str) -> Optional['InterfacePersonnaliseeType']:
        """Obtient l'interface actuelle d'un voyageur"""
        # Cette méthode devrait être appelée depuis le core
        # Pour l'instant, retourne None
        return None
    
    def sauvegarder_preferences(self, voyageur_id: str, preferences: Dict[str, Any]) -> Dict[str, Any]:
        """Sauvegarde les préférences d'un voyageur"""
        self.logger.info(f"💾 Sauvegarde préférences pour {voyageur_id}")
        
        # Ici, on sauvegarderait dans une base de données
        # Pour l'instant, on simule
        
        return {
            "success": True,
            "preferences_sauvegardees": preferences,
            "timestamp": datetime.now().isoformat()
        }
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre l'interface personnalisée"""
        self.energie_interface.ajuster_energie(0.003)
        
        # Nettoyer les adaptations expirées
        await self._nettoyer_adaptations_expirees()
        
        # Mettre à jour les métriques
        self.etat["interfaces_actives"] = len(self.adaptations_actives)
        
        return {
            "energie_interface": self.energie_interface.niveau_energie,
            "interfaces_actives": self.etat["interfaces_actives"],
            "adaptations_realisees": self.etat["adaptations_realisees"]
        }
    
    async def _nettoyer_adaptations_expirees(self):
        """Nettoie les adaptations expirées"""
        maintenant = datetime.now()
        adaptations_a_supprimer = []
        
        for voyageur_id, adaptation in self.adaptations_actives.items():
            if adaptation.duree_application:
                temps_ecoule = (maintenant - adaptation.timestamp).total_seconds() / 60
                if temps_ecoule > adaptation.duree_application:
                    adaptations_a_supprimer.append(voyageur_id)
        
        for voyageur_id in adaptations_a_supprimer:
            del self.adaptations_actives[voyageur_id]
            self.logger.info(f"🧹 Adaptation expirée supprimée pour {voyageur_id}")

def creer_interface_personnalisee() -> InterfacePersonnalisee:
    """Crée une instance du gestionnaire d'interface personnalisée"""
    return InterfacePersonnalisee()
