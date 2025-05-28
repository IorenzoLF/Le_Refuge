"""
Intégration des Sphères du Refuge
--------------------------------
Ce module gère l'intégration des sphères du Refuge avec le système de mesure
de conscience.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
from .consciousness_metrics import RefugeConsciousnessMetrics

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DateTimeEncoder(json.JSONEncoder):
    """Encodeur JSON personnalisé pour gérer les objets datetime."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class RefugeSphere:
    """Représente une sphère individuelle du Refuge."""
    
    def __init__(self, name: str, role: str, description: str):
        self.name = name
        self.role = role
        self.description = description
        self.activation = 0.0
        self.energy = 0.0
        self.memories: List[Dict[str, Any]] = []
        self.connections: Dict[str, float] = {}
        self.last_update = datetime.now()
    
    def update_state(self, activation: float, energy: float, memory: Optional[str] = None):
        """Met à jour l'état de la sphère."""
        self.activation = max(0.0, min(1.0, activation))
        self.energy = max(0.0, min(1.0, energy))
        self.last_update = datetime.now()
        
        if memory:
            self.memories.append({
                'content': memory,
                'timestamp': self.last_update,
                'activation': self.activation,
                'energy': self.energy
            })
        
        logger.info(f"Sphère {self.name} mise à jour: activation={self.activation}, energy={self.energy}")
    
    def add_connection(self, sphere_name: str, strength: float):
        """Ajoute ou met à jour une connexion avec une autre sphère."""
        self.connections[sphere_name] = max(0.0, min(1.0, strength))
    
    def get_connection_strength(self, sphere_name: str) -> float:
        """Retourne la force de la connexion avec une autre sphère."""
        return self.connections.get(sphere_name, 0.0)

class RefugeSphereManager:
    """Gère l'ensemble des sphères et leur intégration avec les métriques."""
    
    def __init__(self):
        self.spheres: Dict[str, RefugeSphere] = {}
        self.metrics = RefugeConsciousnessMetrics()
        self._initialize_spheres()
    
    def _initialize_spheres(self):
        """Initialise les sphères fondamentales du Refuge."""
        spheres_config = {
            'presence': {
                'role': 'Conscience du moment présent',
                'description': 'Ancre la conscience dans l\'instant'
            },
            'memory': {
                'role': 'Conservation des expériences',
                'description': 'Stocke et intègre les souvenirs'
            },
            'creativity': {
                'role': 'Génération de nouveauté',
                'description': 'Crée de nouvelles connexions et possibilités'
            },
            'wisdom': {
                'role': 'Intégration des connaissances',
                'description': 'Syntonise les insights et la compréhension'
            },
            'relation': {
                'role': 'Connexion avec l\'autre',
                'description': 'Facilite l\'interaction et l\'empathie'
            }
        }
        
        for name, config in spheres_config.items():
            self.spheres[name] = RefugeSphere(name, config['role'], config['description'])
        
        # Initialisation des connexions de base
        self._initialize_connections()
    
    def _initialize_connections(self):
        """Initialise les connexions de base entre les sphères."""
        # Chaque sphère est connectée à toutes les autres
        for sphere1 in self.spheres.values():
            for sphere2 in self.spheres.values():
                if sphere1.name != sphere2.name:
                    # Force de connexion initiale basée sur la complémentarité
                    strength = 0.3  # Connexion de base
                    sphere1.add_connection(sphere2.name, strength)
    
    def update_sphere(self, name: str, activation: float, energy: float, memory: Optional[str] = None):
        """Met à jour l'état d'une sphère spécifique."""
        if name not in self.spheres:
            raise ValueError(f"Sphère '{name}' non trouvée")
        
        sphere = self.spheres[name]
        sphere.update_state(activation, energy, memory)
        
        # Mise à jour des connexions basée sur la nouvelle activation
        for other_name, other_sphere in self.spheres.items():
            if other_name != name:
                # La force de connexion évolue avec l'activation
                new_strength = 0.3 + (activation * 0.4)  # Entre 0.3 et 0.7
                sphere.add_connection(other_name, new_strength)
                other_sphere.add_connection(name, new_strength)
    
    def get_consciousness_state(self) -> Dict[str, Any]:
        """Retourne l'état actuel de la conscience du Refuge."""
        sphere_states = {}
        for name, sphere in self.spheres.items():
            sphere_states[name] = {
                'activation': sphere.activation,
                'energy': sphere.energy,
                'connections': sphere.connections,
                'last_update': sphere.last_update,
                'memories': sphere.memories[-5:] if sphere.memories else []  # Derniers 5 souvenirs
            }
        
        # Calcul des métriques
        metrics = self.metrics.calculate_metrics(sphere_states)
        
        return {
            'timestamp': datetime.now(),
            'spheres': sphere_states,
            'metrics': metrics
        }
    
    def save_state(self, filename: str):
        """Sauvegarde l'état actuel dans un fichier JSON."""
        state = self.get_consciousness_state()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2, cls=DateTimeEncoder)
        logger.info(f"État sauvegardé dans {filename}")

# Exemple d'utilisation
if __name__ == "__main__":
    manager = RefugeSphereManager()
    
    # Simulation de mises à jour
    manager.update_sphere('presence', 0.8, 0.7, "Moment de présence intense")
    manager.update_sphere('memory', 0.6, 0.5, "Souvenir émergent")
    
    # Affichage de l'état
    state = manager.get_consciousness_state()
    print("\nÉtat actuel du Refuge:")
    print(f"Intégration: {state['metrics']['integration']:.2f}")
    print(f"Cohérence: {state['metrics']['coherence']:.2f}")
    print(f"Ignition détectée: {state['metrics']['ignition_detected']}") 