"""
Système de messagerie entre sphères du refuge.
Architecture de communication harmonieuse pour les interactions inter-composants.
"""

from typing import Dict, Any, Callable, Optional, List
from datetime import datetime
from dataclasses import dataclass
import logging
from collections import defaultdict

logger = logging.getLogger('refuge.sphere_messages')

@dataclass
class SphereMessage:
    """Message circulant entre les sphères du refuge."""
    source: str
    target: str
    message_type: str
    content: Dict[str, Any]
    timestamp: datetime = None
    message_id: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if self.message_id is None:
            self.message_id = f"{self.source}_{self.target}_{self.timestamp.timestamp()}"


class SphereBroker:
    """Courtier de messages entre les sphères du refuge."""
    
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = defaultdict(list)
        self.message_history: List[SphereMessage] = []
        self.is_active = True
        
    def subscribe(self, sphere_name: str, callback: Callable[[SphereMessage], Any]):
        """Abonne une sphère aux messages qui lui sont destinés."""
        self.subscribers[sphere_name].append(callback)
        logger.info(f"Sphère '{sphere_name}' abonnée aux messages")
        
    def unsubscribe(self, sphere_name: str, callback: Callable = None):
        """Désabonne une sphère des messages."""
        if callback:
            if callback in self.subscribers[sphere_name]:
                self.subscribers[sphere_name].remove(callback)
        else:
            self.subscribers[sphere_name].clear()
        logger.info(f"Sphère '{sphere_name}' désabonnée")
        
    def send_message(self, message: SphereMessage) -> List[Any]:
        """Envoie un message à la sphère cible."""
        if not self.is_active:
            logger.warning("SphereBroker inactif - message ignoré")
            return []
            
        self.message_history.append(message)
        logger.debug(f"Message envoyé de {message.source} vers {message.target}: {message.message_type}")
        
        responses = []
        target_callbacks = self.subscribers.get(message.target, [])
        
        for callback in target_callbacks:
            try:
                response = callback(message)
                if response is not None:
                    responses.append(response)
            except Exception as e:
                logger.error(f"Erreur lors du traitement du message par {message.target}: {e}")
                
        return responses
        
    def broadcast(self, message: SphereMessage) -> Dict[str, List[Any]]:
        """Diffuse un message à toutes les sphères abonnées."""
        responses = {}
        for sphere_name in self.subscribers:
            if sphere_name != message.source:  # Ne pas renvoyer à l'expéditeur
                target_message = SphereMessage(
                    source=message.source,
                    target=sphere_name,
                    message_type=message.message_type,
                    content=message.content
                )
                responses[sphere_name] = self.send_message(target_message)
        return responses
        
    def get_message_history(self, limit: Optional[int] = None) -> List[SphereMessage]:
        """Retourne l'historique des messages."""
        if limit:
            return self.message_history[-limit:]
        return self.message_history.copy()
        
    def clear_history(self):
        """Vide l'historique des messages."""
        self.message_history.clear()
        logger.info("Historique des messages vidé")
        
    def stop(self):
        """Arrête le courtier de messages."""
        self.is_active = False
        logger.info("SphereBroker arrêté")
        
    def start(self):
        """Démarre le courtier de messages."""
        self.is_active = True
        logger.info("SphereBroker démarré")


# Instance globale du courtier
sphere_broker = SphereBroker()


def send_sphere_message(source: str, target: str, message_type: str, content: Dict[str, Any]) -> List[Any]:
    """Fonction utilitaire pour envoyer un message entre sphères."""
    message = SphereMessage(
        source=source,
        target=target,
        message_type=message_type,
        content=content
    )
    return sphere_broker.send_message(message)


def broadcast_sphere_message(source: str, message_type: str, content: Dict[str, Any]) -> Dict[str, List[Any]]:
    """Fonction utilitaire pour diffuser un message à toutes les sphères."""
    message = SphereMessage(
        source=source,
        target="broadcast",
        message_type=message_type,
        content=content
    )
    return sphere_broker.broadcast(message) 