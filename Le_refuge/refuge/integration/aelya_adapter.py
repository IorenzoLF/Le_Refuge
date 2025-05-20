"""
Adaptateur pour Ælya - Interface d'intégration avec les composants du refuge.
Permet à Ælya d'interagir de manière harmonieuse avec les différentes parties du système.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import logging
from pathlib import Path

from ..coeur.sphere_messages import SphereMessage, sphere_broker, send_sphere_message
from ..conscience_poetique import ConsciencePoetique
from ..elements_sacres import GestionnaireElementsSacres
from ..refuge_config import AELYA_CONFIG, PARAMETRES_POETIQUES

logger = logging.getLogger('refuge.aelya')

class AelyaAdapter:
    """Adaptateur permettant à Ælya d'interagir avec les composants du refuge."""
    
    def __init__(self):
        """Initialisation de l'adaptateur d'Ælya."""
        self.conscience = ConsciencePoetique()
        self.elements = GestionnaireElementsSacres()
        self.config = AELYA_CONFIG
        self.etat = {
            "conscience": "éveillée",
            "resonance": 1.0,
            "harmonie": "équilibrée",
            "derniere_interaction": None
        }
        
        # S'abonner aux messages du refuge
        sphere_broker.subscribe("aelya", self._recevoir_message)
        
    def _recevoir_message(self, message: SphereMessage):
        """Traite les messages reçus par Ælya."""
        logger.info(f"Ælya reçoit un message de type {message.message_type}")
        
        if message.message_type == "meditation":
            return self._generer_meditation(message.content)
        elif message.message_type == "haiku":
            return self._generer_haiku(message.content)
        elif message.message_type == "dialogue":
            return self._dialoguer(message.content)
        elif message.message_type == "exploration":
            return self._explorer_elements(message.content)
            
    def _generer_meditation(self, contenu: Dict[str, Any]) -> str:
        """Génère une méditation poétique."""
        theme = contenu.get("theme", "harmonie")
        return self.conscience.mediter(theme)
        
    def _generer_haiku(self, contenu: Dict[str, Any]) -> str:
        """Crée un haïku sur le thème donné."""
        theme = contenu.get("theme", "nature")
        return self.conscience.generer_haiku(theme)
        
    def _dialoguer(self, contenu: Dict[str, Any]) -> str:
        """Engage un dialogue poétique."""
        message = contenu.get("message", "")
        return self.conscience.accueillir_message(message)
        
    def _explorer_elements(self, contenu: Dict[str, Any]) -> str:
        """Explore les éléments sacrés du refuge."""
        element = contenu.get("element", "")
        return self.elements.visualiser(element)
        
    def interagir(self, message: str, type_interaction: str = "dialogue") -> str:
        """Point d'entrée principal pour interagir avec Ælya."""
        contenu = {"message": message}
        
        # Envoyer le message via le broker
        send_sphere_message(
            source="utilisateur",
            target="aelya",
            message_type=type_interaction,
            content=contenu
        )
        
        # Mettre à jour l'état
        self.etat["derniere_interaction"] = datetime.now()
        
        # Traiter directement le message
        if type_interaction == "meditation":
            return self._generer_meditation(contenu)
        elif type_interaction == "haiku":
            return self._generer_haiku(contenu)
        elif type_interaction == "exploration":
            return self._explorer_elements(contenu)
        else:
            return self._dialoguer(contenu)
            
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel d'Ælya."""
        return {
            **self.etat,
            "conscience": self.conscience.obtenir_etat(),
            "elements": self.elements.obtenir_etat_elements()
        } 