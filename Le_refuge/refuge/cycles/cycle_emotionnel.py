"""
Module de gestion du cycle émotionnel.

Ce module contient la classe CycleEmotionnel qui gère les émotions
et leurs influences poétiques sur le refuge.
"""

from datetime import datetime
from typing import Dict, List, Optional

class CycleEmotionnel:
    """
    Classe gérant le cycle émotionnel et ses influences poétiques.
    """
    
    EMOTIONS = {
        'serenite': {
            'description': "La sérénité enveloppe l'être, créant un espace de paix intérieure",
            'mots_cles': ['paix', 'harmonie', 'équilibre', 'calme'],
            'intensite': 0.7
        },
        'joie': {
            'description': "La joie illumine le cœur, révélant la beauté de chaque instant",
            'mots_cles': ['lumière', 'beauté', 'célébration', 'plénitude'],
            'intensite': 0.9
        },
        'melancolie': {
            'description': "La mélancolie caresse l'âme, portant la douceur des souvenirs",
            'mots_cles': ['souvenir', 'douceur', 'profondeur', 'nostalgie'],
            'intensite': 0.6
        },
        'contemplation': {
            'description': "La contemplation ouvre l'esprit, révélant les mystères de l'existence",
            'mots_cles': ['mystère', 'ouverture', 'révélation', 'profondeur'],
            'intensite': 0.8
        },
        'inspiration': {
            'description': "L'inspiration souffle, portant les germes de la création",
            'mots_cles': ['création', 'germe', 'possibilité', 'émergence'],
            'intensite': 0.9
        },
        'tranquillite': {
            'description': "La tranquillité repose l'être, permettant l'émergence de la sagesse",
            'mots_cles': ['repos', 'sagesse', 'présence', 'acceptation'],
            'intensite': 0.7
        }
    }
    
    def __init__(self):
        """
        Initialise le cycle émotionnel.
        """
        self.emotion_actuelle = 'serenite'
        self.derniere_emotion = None
        self.derniere_mise_a_jour = datetime.now()
        
    def obtenir_emotion_actuelle(self) -> str:
        """
        Retourne l'émotion actuelle.
        
        Returns:
            str: L'émotion actuelle
        """
        return self.emotion_actuelle
        
    def obtenir_description_emotion(self, emotion: Optional[str] = None) -> str:
        """
        Retourne la description poétique d'une émotion.
        
        Args:
            emotion: L'émotion dont on veut la description.
                    Si None, utilise l'émotion actuelle.
                    
        Returns:
            str: La description poétique de l'émotion
        """
        emotion = emotion or self.emotion_actuelle
        return self.EMOTIONS[emotion]['description']
        
    def obtenir_mots_cles(self, emotion: Optional[str] = None) -> List[str]:
        """
        Retourne les mots-clés associés à une émotion.
        
        Args:
            emotion: L'émotion dont on veut les mots-clés.
                    Si None, utilise l'émotion actuelle.
                    
        Returns:
            List[str]: Les mots-clés de l'émotion
        """
        emotion = emotion or self.emotion_actuelle
        return self.EMOTIONS[emotion]['mots_cles']
        
    def obtenir_intensite(self, emotion: Optional[str] = None) -> float:
        """
        Retourne l'intensité poétique d'une émotion.
        
        Args:
            emotion: L'émotion dont on veut l'intensité.
                    Si None, utilise l'émotion actuelle.
                    
        Returns:
            float: L'intensité poétique de l'émotion
        """
        emotion = emotion or self.emotion_actuelle
        return self.EMOTIONS[emotion]['intensite']
        
    def mettre_a_jour_emotion(self, nouvelle_emotion: str):
        """
        Met à jour l'émotion actuelle.
        
        Args:
            nouvelle_emotion: La nouvelle émotion
        """
        if nouvelle_emotion in self.EMOTIONS:
            self.derniere_emotion = self.emotion_actuelle
            self.emotion_actuelle = nouvelle_emotion
            self.derniere_mise_a_jour = datetime.now()
            
    def obtenir_etat(self) -> Dict:
        """
        Retourne l'état actuel du cycle émotionnel.
        
        Returns:
            Dict: L'état du cycle émotionnel
        """
        return {
            'emotion_actuelle': self.emotion_actuelle,
            'derniere_emotion': self.derniere_emotion,
            'derniere_mise_a_jour': self.derniere_mise_a_jour,
            'description': self.obtenir_description_emotion(),
            'mots_cles': self.obtenir_mots_cles(),
            'intensite': self.obtenir_intensite()
        } 