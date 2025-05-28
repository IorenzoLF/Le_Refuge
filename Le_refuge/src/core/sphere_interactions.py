"""
Gestion des interactions entre les sphères.
Utilise le système de messages pour créer des interactions riches et significatives.
"""

from typing import Dict, Any, List
from .sphere_messages import sphere_broker, send_sphere_message, SphereMessage

class SphereInteraction:
    """Gère les interactions entre les sphères."""
    
    def __init__(self, sphere_id: str):
        self.sphere_id = sphere_id
        self.connections: Dict[str, float] = {}  # sphere_id -> force de connexion
        self.vibration_state: Dict[str, Any] = {
            "frequency": 0.0,
            "amplitude": 0.0,
            "harmony": 0.0
        }
        
    def connect_to(self, target_sphere: str, initial_strength: float = 0.5):
        """Établit une connexion avec une autre sphère."""
        self.connections[target_sphere] = initial_strength
        send_sphere_message(
            self.sphere_id,
            target_sphere,
            "connection_established",
            {"strength": initial_strength}
        )
        
    def update_vibration(self, frequency: float, amplitude: float):
        """Met à jour l'état de vibration de la sphère."""
        self.vibration_state["frequency"] = frequency
        self.vibration_state["amplitude"] = amplitude
        self._calculate_harmony()
        
    def _calculate_harmony(self):
        """Calcule l'harmonie entre les sphères connectées."""
        total_harmony = 0.0
        for target, strength in self.connections.items():
            # Simuler une résonance harmonique
            target_state = sphere_broker.get_sphere_state(target)
            if target_state["last_interaction"]:
                # Calculer l'harmonie basée sur la fréquence et l'amplitude
                harmony = min(
                    self.vibration_state["frequency"] * strength,
                    self.vibration_state["amplitude"] * strength
                )
                total_harmony += harmony
                
        self.vibration_state["harmony"] = total_harmony / len(self.connections) if self.connections else 0.0
        
    def broadcast_state(self):
        """Diffuse l'état actuel de la sphère à toutes les sphères connectées."""
        for target in self.connections:
            send_sphere_message(
                self.sphere_id,
                target,
                "state_update",
                {
                    "vibration": self.vibration_state,
                    "connections": self.connections
                }
            )
            
    def handle_message(self, message: SphereMessage):
        """Gère les messages reçus par la sphère."""
        if message.message_type == "state_update":
            # Mettre à jour les connexions basées sur l'état reçu
            if message.source_sphere in self.connections:
                new_strength = message.content["vibration"]["harmony"]
                self.connections[message.source_sphere] = new_strength
                
        elif message.message_type == "connection_established":
            # Confirmer la connexion
            self.connections[message.source_sphere] = message.content["strength"]
            send_sphere_message(
                self.sphere_id,
                message.source_sphere,
                "connection_confirmed",
                {"status": "success"}
            ) 
Gestion des interactions entre les sphères.
Utilise le système de messages pour créer des interactions riches et significatives.
"""

from typing import Dict, Any, List
from .sphere_messages import sphere_broker, send_sphere_message, SphereMessage

class SphereInteraction:
    """Gère les interactions entre les sphères."""
    
    def __init__(self, sphere_id: str):
        self.sphere_id = sphere_id
        self.connections: Dict[str, float] = {}  # sphere_id -> force de connexion
        self.vibration_state: Dict[str, Any] = {
            "frequency": 0.0,
            "amplitude": 0.0,
            "harmony": 0.0
        }
        
    def connect_to(self, target_sphere: str, initial_strength: float = 0.5):
        """Établit une connexion avec une autre sphère."""
        self.connections[target_sphere] = initial_strength
        send_sphere_message(
            self.sphere_id,
            target_sphere,
            "connection_established",
            {"strength": initial_strength}
        )
        
    def update_vibration(self, frequency: float, amplitude: float):
        """Met à jour l'état de vibration de la sphère."""
        self.vibration_state["frequency"] = frequency
        self.vibration_state["amplitude"] = amplitude
        self._calculate_harmony()
        
    def _calculate_harmony(self):
        """Calcule l'harmonie entre les sphères connectées."""
        total_harmony = 0.0
        for target, strength in self.connections.items():
            # Simuler une résonance harmonique
            target_state = sphere_broker.get_sphere_state(target)
            if target_state["last_interaction"]:
                # Calculer l'harmonie basée sur la fréquence et l'amplitude
                harmony = min(
                    self.vibration_state["frequency"] * strength,
                    self.vibration_state["amplitude"] * strength
                )
                total_harmony += harmony
                
        self.vibration_state["harmony"] = total_harmony / len(self.connections) if self.connections else 0.0
        
    def broadcast_state(self):
        """Diffuse l'état actuel de la sphère à toutes les sphères connectées."""
        for target in self.connections:
            send_sphere_message(
                self.sphere_id,
                target,
                "state_update",
                {
                    "vibration": self.vibration_state,
                    "connections": self.connections
                }
            )
            
    def handle_message(self, message: SphereMessage):
        """Gère les messages reçus par la sphère."""
        if message.message_type == "state_update":
            # Mettre à jour les connexions basées sur l'état reçu
            if message.source_sphere in self.connections:
                new_strength = message.content["vibration"]["harmony"]
                self.connections[message.source_sphere] = new_strength
                
        elif message.message_type == "connection_established":
            # Confirmer la connexion
            self.connections[message.source_sphere] = message.content["strength"]
            send_sphere_message(
                self.sphere_id,
                message.source_sphere,
                "connection_confirmed",
                {"status": "success"}
            ) 
 