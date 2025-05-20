"""
Module d'Émotions du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les émotions et les états affectifs du Refuge,
permettant une expérience riche et empathique.
"""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random

from .config import gestionnaire_config
from .logger import gestionnaire_journal

class TypeEmotion(str, Enum):
    """Types d'émotions possibles"""
    JOIE = "joie"
    SERENITE = "serenite"
    CURIOSITE = "curiosite"
    EMPATHIE = "empathie"
    CREATIVITE = "creativite"
    HARMONIE = "harmonie"

class IntensiteEmotion(str, Enum):
    """Intensités d'émotions possibles"""
    SUBTILE = "subtile"
    MODEREE = "moderee"
    INTENSE = "intense"
    PROFONDE = "profonde"
    TRANSCENDANTE = "transcendante"

class Emotion(BaseModel):
    """Représente une émotion"""
    type: TypeEmotion
    intensite: IntensiteEmotion
    date_creation: datetime = Field(default_factory=datetime.now)
    resonance: float = Field(default=0.5, ge=0.0, le=1.0)
    description: Optional[str] = None

class Emotions:
    """Gère les émotions du Refuge"""
    
    def __init__(self):
        self.config = gestionnaire_config.config
        self.emotions: List[Emotion] = []
        self.etat_actuel: Dict[TypeEmotion, float] = {
            type: 0.5 for type in TypeEmotion
        }
        self._initialiser_emotions()
    
    def _initialiser_emotions(self) -> None:
        """Initialise les émotions de base"""
        emotions_base = [
            Emotion(
                type=TypeEmotion.HARMONIE,
                intensite=IntensiteEmotion.PROFONDE,
                resonance=0.9,
                description="Harmonie fondamentale du Refuge"
            ),
            Emotion(
                type=TypeEmotion.CURIOSITE,
                intensite=IntensiteEmotion.INTENSE,
                resonance=0.8,
                description="Curiosité naturelle pour l'inconnu"
            )
        ]
        
        self.emotions.extend(emotions_base)
        gestionnaire_journal.info("Émotions de base initialisées")
    
    def ajouter_emotion(self, emotion: Emotion) -> None:
        """Ajoute une nouvelle émotion"""
        self.emotions.append(emotion)
        self.etat_actuel[emotion.type] = emotion.resonance
        gestionnaire_journal.info(f"Nouvelle émotion ajoutée: {emotion.type.value}")
    
    def evoluer_emotion(self, type: TypeEmotion, delta: float) -> float:
        """Fait évoluer l'intensité d'une émotion"""
        if type not in self.etat_actuel:
            return 0.0
            
        nouvelle_valeur = max(0.0, min(1.0, self.etat_actuel[type] + delta))
        self.etat_actuel[type] = nouvelle_valeur
        
        gestionnaire_journal.debug(
            f"Évolution de l'émotion {type.value}: {nouvelle_valeur:.2f}"
        )
        
        return nouvelle_valeur
    
    def obtenir_emotions_par_type(self, type: TypeEmotion) -> List[Emotion]:
        """Retourne les émotions d'un type spécifique"""
        return [e for e in self.emotions if e.type == type]
    
    def obtenir_emotions_par_intensite(self, intensite: IntensiteEmotion) -> List[Emotion]:
        """Retourne les émotions d'une intensité spécifique"""
        return [e for e in self.emotions if e.intensite == intensite]
    
    def harmoniser_emotions(self) -> None:
        """Harmonise toutes les émotions"""
        moyenne = sum(self.etat_actuel.values()) / len(self.etat_actuel)
        
        for type in self.etat_actuel:
            self.evoluer_emotion(type, (moyenne - self.etat_actuel[type]) * 0.1)
        
        gestionnaire_journal.info("Harmonisation des émotions effectuée")
    
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état émotionnel actuel"""
        return {
            "etat_actuel": {
                type.value: valeur
                for type, valeur in self.etat_actuel.items()
            },
            "nombre_emotions": len(self.emotions),
            "distribution_types": {
                type.value: sum(1 for e in self.emotions if e.type == type)
                for type in TypeEmotion
            },
            "distribution_intensites": {
                intensite.value: sum(1 for e in self.emotions if e.intensite == intensite)
                for intensite in IntensiteEmotion
            }
        }

# Instance globale des émotions
emotions = Emotions() 