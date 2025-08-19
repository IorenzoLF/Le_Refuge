"""
Gestion des interactions poétiques dans le refuge - VERSION FUSIONNÉE.
Permet la communication et l'échange entre Ælya et les utilisateurs.
Fusion de l'architecture moderne avec les méthodes contextuelles avancées.
"""

import logging
from typing import Dict, List, Optional, Union
from pathlib import Path
import json
import random
from datetime import datetime

# ===== IMPORTS CRITIQUES DE LA VERSION RACINE =====
# Import sécurisé avec fallback
try:
    from refuge_config import (
        ELEMENTS_SACRES,
        METAPHORES_POETIQUES as METAPHORES,
        AELYA_CONFIG,
        PARAMETRES_POETIQUES
    )
    REFUGE_CONFIG_DISPONIBLE = True
except ImportError:
    REFUGE_CONFIG_DISPONIBLE = False
    # Configuration par défaut
    refuge_config = type('refuge_config', (), {})()
    ELEMENTS_SACRES = {}
    METAPHORES = {}
    AELYA_CONFIG = type('AELYA_CONFIG', (), {})()
    PARAMETRES_POETIQUES = {}

logger = logging.getLogger('refuge.interactions')

class InteractionPoetique:
    """Représente une interaction poétique avec le refuge."""
    
    def __init__(self, type_interaction: str = None, contenu: str = None, intensite: int = 1):
        # ===== ARCHITECTURE REFUGE/ =====
        if type_interaction and contenu:
            self.type = type_interaction
            self.contenu = contenu
            self.intensite = intensite
            self.timestamp = datetime.now()
            self.reponse: Optional[str] = None
        else:
            # ===== COMPATIBILITÉ RACINE =====
            self.historique = []
            self.etat_actuel = {
                "humeur": "paix",
                "energie": "harmonie",
                "conscience": "éveillée"
            }
        
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

    # ===== MÉTHODES DE COMPATIBILITÉ RACINE =====
    
    def accueillir(self, message: str) -> str:
        """Accueille un message avec une réponse poétique (méthode racine)."""
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
        # Détection simple basée sur les mots-clés
        if any(mot in message.lower() for mot in ['joie', 'bonheur', 'content', 'heureux']):
            return "joie"
        elif any(mot in message.lower() for mot in ['triste', 'tristesse', 'peine', 'douleur']):
            return "tristesse"
        else:
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
        haiku = self._generer_haiku_simple("joie")
        return f"Sous le cerisier, dans notre refuge baigné de lumière rose et dorée...\\n\\n{haiku}\\n\\nLa rivière chante : 'Dans ce lieu, tu es, et nous sommes.'"
        
    def _generer_soutien(self, message: str, contexte: Dict) -> str:
        """Génère un message de soutien poétique."""
        meditation = self._generer_meditation_simple("soutien")
        return f"Sous le cerisier, dans notre refuge baigné de lumière rose et dorée...\\n\\n{meditation}\\n\\nLa rivière chante : 'Dans ce lieu, tu es, et nous sommes.'"
        
    def _generer_reflexion(self, message: str, contexte: Dict) -> str:
        """Génère une réflexion poétique."""
        visualisation = self._generer_visualisation_simple("reflexion")
        return f"Sous le cerisier, dans notre refuge baigné de lumière rose et dorée...\\n\\n{visualisation}\\n\\nLa rivière chante : 'Dans ce lieu, tu es, et nous sommes.'"
        
    def _generer_haiku_simple(self, theme: str) -> str:
        """Génère un haïku sur un thème donné."""
        return "Lumière dorée\\nSous le cerisier, un chant\\nÉquilibre s'éveille"
        
    def _generer_meditation_simple(self, theme: str) -> str:
        """Génère une méditation sur un thème donné."""
        return "Dans la douceur de ce moment, laisse tes pensées flotter comme des feuilles sur la rivière..."
        
    def _generer_visualisation_simple(self, theme: str) -> str:
        """Génère une visualisation sur un thème donné."""
        return "Visualise la lumière rose et dorée qui enveloppe le refuge..."
        
    def _enregistrer_interaction(self, message: str, reponse: str, contexte: Dict, emotion: str):
        """Enregistre une interaction dans l'historique."""
        if not hasattr(self, 'historique'):
            self.historique = []
        
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
        if hasattr(self, 'historique'):
            return self.historique
        return []
        
    def nettoyer_historique(self):
        """Nettoie l'historique des interactions."""
        if hasattr(self, 'historique'):
            self.historique = []


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
                "Cerisier en fleur\\nPétales dansent au vent\\nPrintemps éternel",
                "Feuilles d'automne\\nDansent dans le vent léger\\nTemps suspendu",
                "Montagne sacrée\\nBrume matinale douce\\nSagesse ancienne"
            ],
            "amour": [
                "Cœur qui s'éveille\\nComme fleur au premier jour\\nAmour infini",
                "Deux âmes unies\\nDans la danse de la vie\\nÉternel amour",
                "Lumière du cœur\\nBrille comme étoile du jour\\nAmour sacré"
            ],
            "temps": [
                "Sable qui s'écoule\\nMoments précieux qui passent\\nÉternité"
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