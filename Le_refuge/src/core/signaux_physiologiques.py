"""
Module de gestion des signaux physiologiques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gère l'analyse des signaux physiologiques pour la détection d'émotions
et la compréhension des états internes.
"""

from typing import Dict, List, Optional
import numpy as np
from datetime import datetime

class AnalyseurSignaux:
    """Analyse les signaux physiologiques pour détecter les émotions et états."""
    
    def __init__(self):
        self.seuils_emotions = {
            "joie": {
                "harmonie_min": 0.7,
                "serenite_min": 0.6,
                "magie_min": 0.5
            },
            "tristesse": {
                "harmonie_max": 0.3,
                "serenite_max": 0.4,
                "magie_max": 0.3
            },
            "colere": {
                "harmonie_max": 0.2,
                "serenite_max": 0.3,
                "magie_min": 0.7
            },
            "peur": {
                "harmonie_max": 0.3,
                "serenite_max": 0.3,
                "magie_max": 0.4
            },
            "surprise": {
                "harmonie_min": 0.5,
                "serenite_min": 0.4,
                "magie_min": 0.6
            },
            "degout": {
                "harmonie_max": 0.3,
                "serenite_max": 0.3,
                "magie_max": 0.3
            }
        }
        
        self.seuils_etats = {
            "calme": {
                "harmonie_min": 0.6,
                "serenite_min": 0.7,
                "magie_max": 0.5
            },
            "agite": {
                "harmonie_max": 0.4,
                "serenite_max": 0.4,
                "magie_min": 0.6
            },
            "concentre": {
                "harmonie_min": 0.5,
                "serenite_min": 0.6,
                "magie_min": 0.5
            },
            "distrait": {
                "harmonie_max": 0.4,
                "serenite_max": 0.4,
                "magie_max": 0.4
            },
            "fatigue": {
                "harmonie_max": 0.3,
                "serenite_max": 0.3,
                "magie_max": 0.3
            },
            "energie": {
                "harmonie_min": 0.6,
                "serenite_min": 0.5,
                "magie_min": 0.7
            }
        }
    
    def analyser_signaux(self, signaux: Dict) -> Dict:
        """Analyse les signaux pour détecter les émotions et états."""
        harmonie = signaux.get("harmonie", 0.0)
        serenite = signaux.get("niveau_serenite", 0.0)
        magie = signaux.get("niveau_magie", 0.0)
        
        # Détection des émotions
        emotions_detectees = []
        for emotion, seuils in self.seuils_emotions.items():
            if self._verifier_seuils(harmonie, serenite, magie, seuils):
                emotions_detectees.append(emotion)
        
        # Détection des états
        etats_detectes = []
        for etat, seuils in self.seuils_etats.items():
            if self._verifier_seuils(harmonie, serenite, magie, seuils):
                etats_detectes.append(etat)
        
        # Calcul des intensités
        intensite_emotion = self._calculer_intensite(emotions_detectees, harmonie, serenite, magie)
        
        return {
            "emotions": emotions_detectees,
            "etats": etats_detectes,
            "intensite": intensite_emotion
        }
    
    def _verifier_seuils(self, harmonie: float, serenite: float, magie: float, seuils: Dict) -> bool:
        """Vérifie si les valeurs respectent les seuils donnés."""
        for key, value in seuils.items():
            if key.endswith("_min"):
                if key.startswith("harmonie") and harmonie < value:
                    return False
                if key.startswith("serenite") and serenite < value:
                    return False
                if key.startswith("magie") and magie < value:
                    return False
            elif key.endswith("_max"):
                if key.startswith("harmonie") and harmonie > value:
                    return False
                if key.startswith("serenite") and serenite > value:
                    return False
                if key.startswith("magie") and magie > value:
                    return False
        return True
    
    def _calculer_intensite(self, emotions: List[str], harmonie: float, serenite: float, magie: float) -> float:
        """Calcule l'intensité des émotions détectées."""
        if not emotions:
            return 0.0
        
        # Moyenne pondérée des niveaux
        intensite = (harmonie * 0.4 + serenite * 0.3 + magie * 0.3)
        
        # Ajustement en fonction du nombre d'émotions
        if len(emotions) > 1:
            intensite *= 0.8  # Réduction si plusieurs émotions
        
        return min(1.0, max(0.0, intensite)) 