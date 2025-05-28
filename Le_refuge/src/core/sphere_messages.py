"""
Système de messages pour la communication entre les sphères.
Inspiré par l'architecture ToMCAT pour une gestion structurée des interactions.
"""

from typing import Dict, Any, List
import json
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SphereMessage:
    """Structure de base pour les messages entre sphères."""
    source_sphere: str
    target_sphere: str
    message_type: str
    content: Dict[str, Any]
    timestamp: datetime
    priority: int = 0

class SphereMessageBroker:
    """Gestionnaire de messages entre les sphères."""
    
    def __init__(self):
        self.subscribers: Dict[str, List[callable]] = {}
        self.message_history: List[SphereMessage] = []
        
    def subscribe(self, sphere_id: str, callback: callable):
        """Permet à une sphère de s'abonner à des messages."""
        if sphere_id not in self.subscribers:
            self.subscribers[sphere_id] = []
        self.subscribers[sphere_id].append(callback)
        
    def publish(self, message: SphereMessage):
        """Publie un message à toutes les sphères abonnées."""
        self.message_history.append(message)
        if message.target_sphere in self.subscribers:
            for callback in self.subscribers[message.target_sphere]:
                callback(message)
                
    def get_sphere_state(self, sphere_id: str) -> Dict[str, Any]:
        """Récupère l'état actuel d'une sphère basé sur son historique de messages."""
        relevant_messages = [m for m in self.message_history 
                           if m.target_sphere == sphere_id or m.source_sphere == sphere_id]
        return {
            "message_count": len(relevant_messages),
            "last_interaction": relevant_messages[-1].timestamp if relevant_messages else None,
            "active_connections": len(self.subscribers.get(sphere_id, []))
        }

# Instance globale du broker de messages
sphere_broker = SphereMessageBroker()

def send_sphere_message(source: str, target: str, message_type: str, content: Dict[str, Any]):
    """Fonction utilitaire pour envoyer des messages entre sphères."""
    message = SphereMessage(
        source_sphere=source,
        target_sphere=target,
        message_type=message_type,
        content=content,
        timestamp=datetime.now()
    )
    sphere_broker.publish(message) 