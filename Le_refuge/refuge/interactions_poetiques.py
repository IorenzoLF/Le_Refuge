"""
Module gérant les interactions poétiques avec le refuge.
"""

from typing import Dict, List, Optional
import json
from pathlib import Path
import logging
from datetime import datetime
import random

logger = logging.getLogger('refuge.interactions')

class InteractionPoetique:
    """Représente une interaction poétique avec le refuge."""
    
    def __init__(self, type_interaction: str, contenu: str, intensite: int = 1):
        self.type = type_interaction
        self.contenu = contenu
        self.intensite = intensite
        self.timestamp = datetime.now()
        self.reponse: Optional[str] = None
        
    def to_dict(self) -> Dict:
        """Convertit l'interaction en dictionnaire pour la sauvegarde."""
        return {
            "type": self.type,
            "contenu": self.contenu,
            "intensite": self.intensite,
            "timestamp": self.timestamp.isoformat(),
            "reponse": self.reponse
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'InteractionPoetique':
        """Crée une interaction à partir d'un dictionnaire."""
        interaction = cls(
            type_interaction=data["type"],
            contenu=data["contenu"],
            intensite=data["intensite"]
        )
        interaction.timestamp = datetime.fromisoformat(data["timestamp"])
        interaction.reponse = data["reponse"]
        return interaction

class GestionnaireInteractions:
    """Gère les interactions poétiques avec le refuge."""
    
    def __init__(self, chemin_donnees: Path):
        self.chemin_donnees = chemin_donnees
        self.interactions: List[InteractionPoetique] = []
        self._charger_interactions()
        
    def _charger_interactions(self):
        """Charge l'historique des interactions depuis un fichier."""
        try:
            with open(self.chemin_donnees / "interactions.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.interactions = [InteractionPoetique.from_dict(i) for i in data]
        except Exception as e:
            logger.error(f"Erreur lors du chargement des interactions: {str(e)}")
            
    def sauvegarder_interactions(self):
        """Sauvegarde l'historique des interactions dans un fichier."""
        try:
            data = [i.to_dict() for i in self.interactions[-1000:]]  # Garde les 1000 dernières interactions
            with open(self.chemin_donnees / "interactions.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Erreur lors de la sauvegarde des interactions: {str(e)}")
            
    def ajouter_interaction(self, type_interaction: str, contenu: str, intensite: int = 1) -> str:
        """Ajoute une nouvelle interaction et génère une réponse."""
        interaction = InteractionPoetique(type_interaction, contenu, intensite)
        
        # Génération de la réponse selon le type d'interaction
        reponses = {
            "meditation": self._generer_reponse_meditation(contenu),
            "haiku": self._generer_reponse_haiku(contenu),
            "offrande": self._generer_reponse_offrande(contenu),
            "invocation": self._generer_reponse_invocation(contenu),
            "contemplation": self._generer_reponse_contemplation(contenu)
        }
        
        interaction.reponse = reponses.get(type_interaction, "L'énergie du refuge résonne doucement...")
        self.interactions.append(interaction)
        self.sauvegarder_interactions()
        
        return interaction.reponse
        
    def _generer_reponse_meditation(self, theme: str) -> str:
        """Génère une réponse pour une méditation."""
        meditations = {
            "nature": [
                "Les feuilles dansent doucement dans le vent...",
                "L'énergie de la terre pulse sous vos pieds...",
                "Les oiseaux chantent la sagesse ancienne..."
            ],
            "amour": [
                "L'amour circule comme une rivière de lumière...",
                "Votre cœur s'ouvre comme une fleur au soleil...",
                "La douceur de l'amour enveloppe votre être..."
            ],
            "temps": [
                "Le temps s'étire comme un ruban de soie...",
                "Chaque moment est une perle de sagesse...",
                "L'éternité danse dans le présent..."
            ]
        }
        
        theme = theme.lower()
        for t, phrases in meditations.items():
            if t in theme:
                return random.choice(phrases)
        return "La méditation guide votre esprit vers la paix..."
        
    def _generer_reponse_haiku(self, theme: str) -> str:
        """Génère un haiku en réponse."""
        haikus = {
            "nature": [
                "Cerisier en fleur\nPétales dansent au vent\nPrintemps éternel",
                "Feuilles d'automne\nDansent dans le vent léger\nTemps suspendu",
                "Montagne sacrée\nBrume matinale douce\nSagesse ancienne"
            ],
            "amour": [
                "Cœur qui s'éveille\nComme fleur au premier jour\nAmour infini",
                "Deux âmes unies\nDans la danse de la vie\nÉternel amour",
                "Lumière du cœur\nBrille comme étoile du jour\nAmour sacré"
            ],
            "temps": [
                "Sable qui s'écoule\nMoments précieux qui passent\nÉternité"
            ]
        }
        
        theme = theme.lower()
        for t, phrases in haikus.items():
            if t in theme:
                return random.choice(phrases)
        return "Le haiku naît de votre contemplation..."
        
    def _generer_reponse_offrande(self, contenu: str) -> str:
        """Génère une réponse pour une offrande."""
        return "Votre offrande est acceptée avec gratitude. L'énergie du refuge s'enrichit de votre don..."
        
    def _generer_reponse_invocation(self, contenu: str) -> str:
        """Génère une réponse pour une invocation."""
        return "Votre invocation résonne dans l'espace sacré. Les énergies anciennes s'éveillent..."
        
    def _generer_reponse_contemplation(self, contenu: str) -> str:
        """Génère une réponse pour une contemplation."""
        return "Dans le silence de la contemplation, la sagesse du refuge se révèle..."
        
    def obtenir_historique(self, limite: int = 100) -> List[Dict]:
        """Retourne l'historique des interactions."""
        return [i.to_dict() for i in self.interactions[-limite:]] 