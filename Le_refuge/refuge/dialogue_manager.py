"""
Module de gestion du dialogue utilisant ParlAI pour enrichir les capacités conversationnelles du Refuge.

Ce module sert d'interface entre le Refuge et ParlAI, permettant d'utiliser les modèles
et datasets de ParlAI tout en maintenant la cohérence avec l'architecture du Refuge.
"""

import os
from typing import Dict, List, Optional, Tuple

from parlai.core.agents import Agent, create_agent_from_model_file
from parlai.core.message import Message
from parlai.core.opt import Opt
from parlai.core.params import ParlaiParser
from parlai.core.worlds import World

class DialogueManager:
    """Gestionnaire de dialogue utilisant ParlAI."""
    
    def __init__(self, model_path: Optional[str] = None):
        """
        Initialise le gestionnaire de dialogue.
        
        Args:
            model_path: Chemin vers un modèle pré-entraîné ParlAI.
                       Si None, utilise le modèle par défaut.
        """
        self.parser = ParlaiParser(True, True)
        self.opt = self.parser.parse_args([])
        
        # Configuration par défaut si aucun modèle n'est spécifié
        if model_path is None:
            self.opt['model'] = 'transformer/generator'
            self.opt['model_file'] = 'zoo:blender/blender_90M/model'
        else:
            self.opt['model_file'] = model_path
            
        self.agent = create_agent_from_model_file(self.opt['model_file'])
        self.context: List[Dict] = []
        
    def reset(self):
        """Réinitialise le contexte de la conversation."""
        self.context = []
        self.agent.reset()
        
    def add_context(self, text: str, speaker: str = "human"):
        """
        Ajoute du contexte à la conversation.
        
        Args:
            text: Le texte à ajouter au contexte
            speaker: L'identifiant du locuteur ("human" ou "assistant")
        """
        self.context.append({
            "text": text,
            "speaker": speaker
        })
        
    def respond(self, text: str) -> str:
        """
        Génère une réponse à partir du texte d'entrée.
        
        Args:
            text: Le texte d'entrée auquel répondre
            
        Returns:
            La réponse générée par le modèle
        """
        # Ajoute l'entrée au contexte
        self.add_context(text)
        
        # Prépare le message pour ParlAI
        message = Message({
            'text': text,
            'episode_done': False
        })
        
        # Obtient la réponse du modèle
        self.agent.observe(message)
        response = self.agent.act()
        
        # Ajoute la réponse au contexte
        self.add_context(response['text'], speaker="assistant")
        
        return response['text']
    
    def get_context(self) -> List[Dict]:
        """
        Retourne le contexte actuel de la conversation.
        
        Returns:
            La liste des messages dans le contexte
        """
        return self.context
    
    def save_conversation(self, path: str):
        """
        Sauvegarde la conversation actuelle dans un fichier.
        
        Args:
            path: Le chemin où sauvegarder la conversation
        """
        with open(path, 'w', encoding='utf-8') as f:
            for message in self.context:
                f.write(f"{message['speaker']}: {message['text']}\n")
                
    @classmethod
    def load_from_config(cls, config_path: str) -> 'DialogueManager':
        """
        Crée une instance à partir d'un fichier de configuration.
        
        Args:
            config_path: Chemin vers le fichier de configuration
            
        Returns:
            Une nouvelle instance de DialogueManager
        """
        # TODO: Implémenter le chargement depuis un fichier de configuration
        return cls() 