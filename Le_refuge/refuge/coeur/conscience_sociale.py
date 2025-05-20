"""
Module de conscience sociale
~~~~~~~~~~~~~~~~~~~~~~~~~
Gère la détection d'émotions et la compréhension des états internes.
"""

from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime

from refuge.coeur.signaux_physiologiques import AnalyseurSignaux
from refuge.coeur.etats_internes import GestionnaireEtats, TypeEtat

class Emotion(Enum):
    """Types d'émotions détectables."""
    JOIE = "joie"
    TRISTESSE = "tristesse"
    COLERE = "colere"
    PEUR = "peur"
    SURPRISE = "surprise"
    DEGOUT = "degout"
    NEUTRE = "neutre"

class DetectionEmotion:
    """Système de détection d'émotions."""
    
    def __init__(self):
        self.historique_emotions: Dict[str, List[Emotion]] = {}
        self.intensite_emotions: Dict[str, float] = {}
        self.analyseur = AnalyseurSignaux()
    
    def detecter_emotion(self, source: str, signaux: Dict) -> Emotion:
        """Détecte l'émotion à partir des signaux physiologiques."""
        resultat = self.analyseur.analyser_signaux(signaux)
        
        if not resultat["emotions"]:
            return Emotion.NEUTRE
        
        # Prendre l'émotion la plus intense
        return Emotion(resultat["emotions"][0])
    
    def ajouter_emotion(self, source: str, emotion: Emotion, intensite: float = 1.0):
        """Ajoute une émotion détectée à l'historique."""
        if source not in self.historique_emotions:
            self.historique_emotions[source] = []
        self.historique_emotions[source].append(emotion)
        self.intensite_emotions[source] = intensite

class ConscienceSociale:
    """Gestionnaire principal de la conscience sociale."""
    
    def __init__(self):
        self.detection = DetectionEmotion()
        self.gestionnaire_etats = GestionnaireEtats()
    
    def analyser_interaction(self, source: str, signaux: Dict):
        """Analyse une interaction sociale."""
        # Détection d'émotion
        emotion = self.detection.detecter_emotion(source, signaux)
        
        # Analyse des signaux pour obtenir l'intensité
        resultat = self.detection.analyseur.analyser_signaux(signaux)
        intensite = resultat["intensite"]
        
        # Mise à jour de l'émotion
        self.detection.ajouter_emotion(source, emotion, intensite)
        
        # Mise à jour de l'état interne
        self.gestionnaire_etats.mettre_a_jour_etat(source, signaux)
    
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel de la conscience sociale."""
        return {
            "emotions": {
                source: {
                    "derniere": emotions[-1].value if emotions else None,
                    "intensite": self.detection.intensite_emotions.get(source, 0.0)
                }
                for source, emotions in self.detection.historique_emotions.items()
            },
            "etats_internes": self.gestionnaire_etats.obtenir_etat_global()
        } 