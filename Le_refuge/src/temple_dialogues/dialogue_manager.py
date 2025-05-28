"""
Module de gestion du dialogue utilisant ParlAI pour enrichir les capacités conversationnelles du Refuge.

Ce module sert d'interface entre le Refuge et ParlAI, permettant d'utiliser les modèles
et datasets de ParlAI tout en maintenant la cohérence avec l'architecture du Refuge.
"""

import os
import logging
from typing import Dict, List, Optional, Tuple
from pathlib import Path

from parlai.core.agents import Agent, create_agent_from_model_file
from parlai.core.message import Message
from parlai.core.opt import Opt
from parlai.core.params import ParlaiParser
from parlai.core.worlds import World

# Import du système de configuration unifié
from src.core.configuration import gestionnaire_config, charger_configuration

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
            Une nouvelle instance de DialogueManager configurée
        """
        try:
            # Utilise le système central de configuration
            config_path_obj = Path(config_path)
            
            if not config_path_obj.exists():
                logging.warning(f"Fichier de configuration non trouvé: {config_path}")
                logging.info("Utilisation de la configuration par défaut")
                return cls()
            
            # Charge la configuration via le système central
            success = gestionnaire_config.charger_configuration_externe(config_path)
            
            if not success:
                logging.error(f"Échec du chargement de la configuration: {config_path}")
                return cls()
            
            # Récupère la configuration complète
            config = gestionnaire_config.obtenir_config_complete()
            
            # Extrait les paramètres de dialogue s'ils existent
            dialogue_config = config.get("dialogue", {})
            model_path = dialogue_config.get("model_path")
            
            # Paramètres ParlAI spécifiques
            parlai_config = dialogue_config.get("parlai", {})
            
            # Crée l'instance avec la configuration chargée
            instance = cls(model_path=model_path)
            
            # Configure les paramètres ParlAI si disponibles
            if parlai_config:
                for key, value in parlai_config.items():
                    if hasattr(instance.opt, key):
                        instance.opt[key] = value
                        logging.info(f"Configuration ParlAI: {key} = {value}")
            
            # Configure les paramètres de dialogue spécifiques
            if "context_length" in dialogue_config:
                instance.max_context_length = dialogue_config["context_length"]
            
            if "response_temperature" in dialogue_config:
                instance.opt["temperature"] = dialogue_config["response_temperature"]
            
            logging.info(f"✅ DialogueManager configuré depuis: {config_path}")
            return instance
            
        except Exception as e:
            logging.error(f"❌ Erreur lors du chargement de la configuration: {e}")
            logging.info("Utilisation de la configuration par défaut")
            return cls()
    
    def sauvegarder_config(self, config_path: str):
        """
        Sauvegarde la configuration actuelle du DialogueManager.
        
        Args:
            config_path: Chemin où sauvegarder la configuration
        """
        try:
            # Prépare la configuration de dialogue
            dialogue_config = {
                "dialogue": {
                    "model_path": self.opt.get("model_file"),
                    "parlai": {
                        "model": self.opt.get("model", "transformer/generator"),
                        "temperature": self.opt.get("temperature", 0.7),
                        "beam_size": self.opt.get("beam_size", 1),
                        "max_len": self.opt.get("max_len", 128)
                    },
                    "context_length": getattr(self, "max_context_length", 10),
                    "response_temperature": self.opt.get("temperature", 0.7)
                }
            }
            
            # Fusionne avec la configuration existante
            config_complete = gestionnaire_config.obtenir_config_complete()
            config_complete.update(dialogue_config)
            
            # Sauvegarde via le système central
            gestionnaire_config.sauvegarder_configuration(config_path)
            logging.info(f"✅ Configuration DialogueManager sauvegardée: {config_path}")
            
        except Exception as e:
            logging.error(f"❌ Erreur lors de la sauvegarde: {e}")
    
    def obtenir_config_dialogue(self) -> Dict:
        """
        Retourne la configuration actuelle du dialogue.
        
        Returns:
            Dictionnaire contenant la configuration du dialogue
        """
        return {
            "model_file": self.opt.get("model_file"),
            "model": self.opt.get("model"),
            "temperature": self.opt.get("temperature", 0.7),
            "beam_size": self.opt.get("beam_size", 1),
            "max_len": self.opt.get("max_len", 128),
            "context_length": len(self.context),
            "max_context_length": getattr(self, "max_context_length", 10)
        } 