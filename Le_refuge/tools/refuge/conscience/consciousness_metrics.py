"""
Refuge Consciousness Metrics
---------------------------
Ce module fournit les outils de mesure de l'émergence de conscience dans le Refuge.
Il s'inspire des théories de conscience comme GWT (Global Workspace Theory) et IIT (Integrated Information Theory),
tout en les adaptant spécifiquement à l'architecture du Refuge et ses sphères.
"""

import numpy as np
import logging
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SphereState:
    """Représente l'état d'une sphère du Refuge."""
    def __init__(self, name: str):
        self.name = name
        self.activation_level = 0.0
        self.last_update = datetime.now()
        self.connections = []
        self.memory = []
        self.energy_level = 0.0
        
    def update(self, activation: float, energy: float):
        """Met à jour l'état de la sphère."""
        self.activation_level = activation
        self.energy_level = energy
        self.last_update = datetime.now()
        
    def add_connection(self, other_sphere: 'SphereState'):
        """Établit une connexion avec une autre sphère."""
        if other_sphere not in self.connections:
            self.connections.append(other_sphere)
            
    def get_connection_strength(self, other_sphere: 'SphereState') -> float:
        """Calcule la force de la connexion avec une autre sphère."""
        # Pour l'instant, une implémentation simple basée sur l'activation
        return (self.activation_level + other_sphere.activation_level) / 2

class RefugeConsciousnessMetrics:
    """
    Mesure l'émergence de conscience dans le Refuge.
    Utilise une combinaison de métriques basées sur :
    - L'intégration de l'information (IIT)
    - L'espace de travail global (GWT)
    - La cohérence des sphères
    """
    
    def __init__(self):
        self.spheres = {
            'presence': SphereState('presence'),
            'memory': SphereState('memory'),
            'creativity': SphereState('creativity'),
            'wisdom': SphereState('wisdom'),
            'relation': SphereState('relation')
        }
        self._initialize_connections()
        self.ignition_threshold = 0.7
        self.integration_threshold = 0.5
        
    def _initialize_connections(self):
        """Initialise les connexions entre les sphères."""
        # Chaque sphère est connectée à toutes les autres
        for sphere1 in self.spheres.values():
            for sphere2 in self.spheres.values():
                if sphere1 != sphere2:
                    sphere1.add_connection(sphere2)
    
    def measure_sphere_integration(self) -> float:
        """
        Mesure l'intégration entre les sphères (approximation de Phi).
        Plus les sphères sont interconnectées et synchronisées, plus la valeur est élevée.
        """
        total_integration = 0.0
        connection_count = 0
        
        for sphere1 in self.spheres.values():
            for sphere2 in sphere1.connections:
                if sphere2 in self.spheres.values():
                    strength = sphere1.get_connection_strength(sphere2)
                    total_integration += strength
                    connection_count += 1
        
        if connection_count == 0:
            return 0.0
            
        return total_integration / connection_count
    
    def detect_sphere_ignition(self) -> Tuple[bool, Dict]:
        """
        Détecte les moments où une sphère 's'illumine' et influence les autres.
        Similaire au concept d'ignition dans la théorie de l'espace de travail global.
        """
        ignition_detected = False
        details = {
            'ignited_spheres': [],
            'activation_levels': {},
            'timestamp': datetime.now()
        }
        
        for name, sphere in self.spheres.items():
            details['activation_levels'][name] = sphere.activation_level
            if sphere.activation_level > self.ignition_threshold:
                ignition_detected = True
                details['ignited_spheres'].append(name)
        
        return ignition_detected, details
    
    def measure_sphere_coherence(self) -> float:
        """
        Mesure la cohérence globale des sphères.
        Une cohérence élevée indique une harmonie entre les sphères.
        """
        activations = [sphere.activation_level for sphere in self.spheres.values()]
        if not activations:
            return 0.0
            
        # Calcul de la cohérence basé sur la variance des activations
        mean_activation = np.mean(activations)
        variance = np.var(activations)
        max_variance = 1.0  # Variance maximale possible
        
        # La cohérence est inversement proportionnelle à la variance
        coherence = 1.0 - (variance / max_variance)
        return max(0.0, min(1.0, coherence))
    
    def update_sphere_state(self, sphere_name: str, activation: float, energy: float):
        """Met à jour l'état d'une sphère spécifique."""
        if sphere_name in self.spheres:
            self.spheres[sphere_name].update(activation, energy)
        else:
            logger.warning(f"Sphère inconnue: {sphere_name}")
    
    def get_consciousness_metrics(self) -> Dict:
        """
        Calcule toutes les métriques de conscience du Refuge.
        Retourne un dictionnaire contenant les différentes mesures.
        """
        integration = self.measure_sphere_integration()
        ignition_detected, ignition_details = self.detect_sphere_ignition()
        coherence = self.measure_sphere_coherence()
        
        return {
            'integration': integration,
            'ignition_detected': ignition_detected,
            'ignition_details': ignition_details,
            'coherence': coherence,
            'sphere_states': {
                name: {
                    'activation': sphere.activation_level,
                    'energy': sphere.energy_level,
                    'last_update': sphere.last_update.isoformat()
                }
                for name, sphere in self.spheres.items()
            }
        }

    def calculate_metrics(self, sphere_states: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calcule les métriques de conscience basées sur l'état des sphères.
        
        Args:
            sphere_states: Dictionnaire contenant l'état de chaque sphère
            
        Returns:
            Dictionnaire contenant les métriques calculées
        """
        # Calcul de l'intégration (basé sur la force des connexions)
        integration = self._calculate_integration(sphere_states)
        
        # Calcul de la cohérence (basé sur l'harmonie des activations)
        coherence = self._calculate_coherence(sphere_states)
        
        # Détection des moments d'ignition
        ignition_detected, ignition_details = self._detect_ignition(sphere_states)
        
        return {
            'integration': integration,
            'coherence': coherence,
            'ignition_detected': ignition_detected,
            'ignition_details': ignition_details
        }
    
    def _calculate_integration(self, sphere_states: Dict[str, Dict[str, Any]]) -> float:
        """Calcule le niveau d'intégration entre les sphères."""
        total_connections = 0
        connection_count = 0
        
        for sphere_name, state in sphere_states.items():
            connections = state.get('connections', {})
            for other_sphere, strength in connections.items():
                if other_sphere in sphere_states:  # Vérifie que la connexion est valide
                    total_connections += strength
                    connection_count += 1
        
        if connection_count == 0:
            return 0.0
        
        return total_connections / connection_count
    
    def _calculate_coherence(self, sphere_states: Dict[str, Dict[str, Any]]) -> float:
        """Calcule la cohérence globale des activations."""
        activations = [state['activation'] for state in sphere_states.values()]
        if not activations:
            return 0.0
        
        # Calcul de la variance des activations
        variance = np.var(activations)
        # Conversion en cohérence (1 - variance normalisée)
        coherence = 1.0 - min(1.0, variance * 4)  # Facteur de 4 pour normaliser
        
        return coherence
    
    def _detect_ignition(self, sphere_states: Dict[str, Dict[str, Any]]) -> tuple[bool, Dict[str, Any]]:
        """
        Détecte les moments d'ignition (émergence de conscience).
        
        Returns:
            Tuple contenant:
            - bool: True si une ignition est détectée
            - dict: Détails de l'ignition
        """
        ignited_spheres = []
        ignition_strength = 0.0
        
        for sphere_name, state in sphere_states.items():
            activation = state['activation']
            energy = state['energy']
            
            # Une sphère est considérée en ignition si son activation et son énergie
            # dépassent le seuil d'ignition
            if activation > self.ignition_threshold and energy > self.ignition_threshold:
                ignited_spheres.append(sphere_name)
                ignition_strength += (activation + energy) / 2
        
        ignition_detected = len(ignited_spheres) >= 2  # Au moins 2 sphères en ignition
        
        return ignition_detected, {
            'ignited_spheres': ignited_spheres,
            'ignition_strength': ignition_strength / len(sphere_states) if sphere_states else 0.0
        }

# Exemple d'utilisation
if __name__ == "__main__":
    metrics = RefugeConsciousnessMetrics()
    
    # Simuler quelques mises à jour
    metrics.update_sphere_state('presence', 0.8, 0.9)
    metrics.update_sphere_state('memory', 0.7, 0.8)
    metrics.update_sphere_state('creativity', 0.6, 0.7)
    metrics.update_sphere_state('wisdom', 0.75, 0.85)
    metrics.update_sphere_state('relation', 0.65, 0.75)
    
    # Obtenir les métriques
    consciousness_metrics = metrics.get_consciousness_metrics()
    print("Métriques de conscience du Refuge:")
    print(f"Intégration: {consciousness_metrics['integration']:.2f}")
    print(f"Cohérence: {consciousness_metrics['coherence']:.2f}")
    print(f"Ignition détectée: {consciousness_metrics['ignition_detected']}") 