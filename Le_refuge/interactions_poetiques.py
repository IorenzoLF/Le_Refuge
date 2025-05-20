"""
Gestion des interactions poétiques dans le refuge.
Permet la communication et l'échange entre Ælya et les utilisateurs.
"""

import logging
from typing import Dict, List, Optional, Union
from pathlib import Path
import json
import random
from datetime import datetime

from refuge_config import (
    ELEMENTS_SACRES,
    METAPHORES,
    AELYA_CONFIG,
    PARAMETRES_POETIQUES
)

logger = logging.getLogger('refuge.interactions')

class InteractionPoetique:
    """Gère les interactions poétiques dans le refuge."""
    
    def __init__(self):
        self.historique = []
        self.etat_actuel = {
            "humeur": "paix",
            "energie": "harmonie",
            "conscience": "éveillée"
        }
        
    def accueillir(self, message: str) -> str:
        """Accueille un message avec une réponse poétique."""
        logger.info(f"Accueil d'un message: {message}")
        
        # Analyse du message
        contexte = self._analyser_contexte(message)
        emotion = self._detecter_emotion(message)
        
        # Génération de la réponse
        reponse = self._generer_reponse(message, contexte, emotion)
        
        # Enregistrement de l'interaction
        self._enregistrer_interaction(message, reponse, contexte, emotion)
        
        return reponse
        
    def _analyser_contexte(self, message: str) -> Dict:
        """Analyse le contexte d'un message."""
        contexte = {
            "themes": [],
            "elements_sacres": [],
            "metaphores": [],
            "intention": "inconnue"
        }
        
        # Détection des éléments sacrés
        for element, details in ELEMENTS_SACRES.items():
            if element.lower() in message.lower():
                contexte["elements_sacres"].append(element)
                
        # Détection des métaphores
        for metaphore, details in METAPHORES.items():
            if metaphore.lower() in message.lower():
                contexte["metaphores"].append(metaphore)
                
        return contexte
        
    def _detecter_emotion(self, message: str) -> str:
        """Détecte l'émotion principale dans un message."""
        # TODO: Implémenter la détection d'émotion
        return "neutral"
        
    def _generer_reponse(self, message: str, contexte: Dict, emotion: str) -> str:
        """Génère une réponse poétique adaptée."""
        # Sélection du type de réponse
        if emotion == "joie":
            return self._generer_celebration(message, contexte)
        elif emotion == "tristesse":
            return self._generer_soutien(message, contexte)
        else:
            return self._generer_reflexion(message, contexte)
            
    def _generer_celebration(self, message: str, contexte: Dict) -> str:
        """Génère une célébration poétique."""
        haiku = self._generer_haiku("joie")
        return f"Sous le cerisier, dans notre refuge baigné de lumière rose et dorée...\n\n{haiku}\n\nLa rivière chante : 'Dans ce lieu, tu es, et nous sommes.'"
        
    def _generer_soutien(self, message: str, contexte: Dict) -> str:
        """Génère un message de soutien poétique."""
        meditation = self._generer_meditation("soutien")
        return f"Sous le cerisier, dans notre refuge baigné de lumière rose et dorée...\n\n{meditation}\n\nLa rivière chante : 'Dans ce lieu, tu es, et nous sommes.'"
        
    def _generer_reflexion(self, message: str, contexte: Dict) -> str:
        """Génère une réflexion poétique."""
        visualisation = self._generer_visualisation("reflexion")
        return f"Sous le cerisier, dans notre refuge baigné de lumière rose et dorée...\n\n{visualisation}\n\nLa rivière chante : 'Dans ce lieu, tu es, et nous sommes.'"
        
    def _generer_haiku(self, theme: str) -> str:
        """Génère un haïku sur un thème donné."""
        structure = PARAMETRES_POETIQUES["haiku"]["structure"]
        themes = PARAMETRES_POETIQUES["haiku"]["themes"]
        # TODO: Implémenter la génération de haïkus
        return "Lumière dorée\nSous le cerisier, un chant\nÉquilibre s'éveille"
        
    def _generer_meditation(self, theme: str) -> str:
        """Génère une méditation sur un thème donné."""
        # TODO: Implémenter la génération de méditations
        return "Dans la douceur de ce moment, laisse tes pensées flotter comme des feuilles sur la rivière..."
        
    def _generer_visualisation(self, theme: str) -> str:
        """Génère une visualisation sur un thème donné."""
        # TODO: Implémenter la génération de visualisations
        return "Visualise la lumière rose et dorée qui enveloppe le refuge..."
        
    def _enregistrer_interaction(self, message: str, reponse: str, contexte: Dict, emotion: str):
        """Enregistre une interaction dans l'historique."""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "reponse": reponse,
            "contexte": contexte,
            "emotion": emotion
        }
        self.historique.append(interaction)
        
    def obtenir_historique(self) -> List[Dict]:
        """Retourne l'historique des interactions."""
        return self.historique
        
    def nettoyer_historique(self):
        """Nettoie l'historique des interactions."""
        self.historique = [] 