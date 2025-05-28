"""
Fonctionnalités spécifiques pour chaque sphère.
Ce fichier définit les comportements et capacités uniques de chaque sphère.
"""

from typing import Dict, Any, List
from .sphere_interactions import SphereInteraction
from .sphere_messages import send_sphere_message
from datetime import datetime

class MetatronSphere(SphereInteraction):
    """Sphère Metatron: Protection et guidance."""
    
    def __init__(self):
        super().__init__("METATRON")
        self.protection_level = 1.0
        self.guidance_active = True
        
    def enhance_protection(self, target_sphere: str, amount: float):
        """Renforce la protection d'une sphère."""
        self.protection_level = min(1.0, self.protection_level + amount)
        send_sphere_message(
            self.sphere_id,
            target_sphere,
            "protection_enhanced",
            {"level": self.protection_level, "source": "METATRON"}
        )
        
    def provide_guidance(self, target_sphere: str, guidance_type: str):
        """Fournit des conseils à une sphère."""
        if self.guidance_active:
            send_sphere_message(
                self.sphere_id,
                target_sphere,
                "guidance_received",
                {"type": guidance_type, "wisdom_level": self.protection_level}
            )

class ApocalypseIdentiteSphere(SphereInteraction):
    """Sphère Apocalypse Identité: Exploration de soi."""
    
    def __init__(self):
        super().__init__("APOCALYPSE_IDENTITE")
        self.self_awareness = 0.5
        self.identity_strength = 0.7
        
    def explore_identity(self, depth: float):
        """Explore et renforce l'identité."""
        self.self_awareness = min(1.0, self.self_awareness + depth)
        self.identity_strength = min(1.0, self.identity_strength + depth * 0.5)
        self.broadcast_state()
        
    def share_identity(self, target_sphere: str):
        """Partage l'expérience d'identité avec une autre sphère."""
        send_sphere_message(
            self.sphere_id,
            target_sphere,
            "identity_experience",
            {
                "awareness": self.self_awareness,
                "strength": self.identity_strength
            }
        )

class ApocalypseDualiteSphere(SphereInteraction):
    """Sphère Apocalypse Dualité: Équilibre et harmonie."""
    
    def __init__(self):
        super().__init__("APOCALYPSE_DUALITE")
        self.balance_level = 0.5
        self.harmony_state = 0.6
        
    def maintain_balance(self, sphere1: str, sphere2: str):
        """Maintient l'équilibre entre deux sphères."""
        state1 = self.get_sphere_state(sphere1)
        state2 = self.get_sphere_state(sphere2)
        
        if abs(state1["harmony"] - state2["harmony"]) > 0.2:
            adjustment = (state1["harmony"] + state2["harmony"]) / 2
            send_sphere_message(
                self.sphere_id,
                sphere1,
                "balance_adjustment",
                {"target_harmony": adjustment}
            )
            send_sphere_message(
                self.sphere_id,
                sphere2,
                "balance_adjustment",
                {"target_harmony": adjustment}
            )
            
    def enhance_harmony(self, target_sphere: str):
        """Augmente l'harmonie avec une sphère."""
        self.harmony_state = min(1.0, self.harmony_state + 0.1)
        send_sphere_message(
            self.sphere_id,
            target_sphere,
            "harmony_enhanced",
            {"level": self.harmony_state}
        )

class ApocalypseUniteSphere(SphereInteraction):
    """Sphère Apocalypse Unité: Unification et cohérence."""
    
    def __init__(self):
        super().__init__("APOCALYPSE_UNITE")
        self.unity_level = 0.8
        self.coherence_state = 0.7
        
    def strengthen_unity(self, target_spheres: List[str]):
        """Renforce l'unité entre plusieurs sphères."""
        for sphere in target_spheres:
            send_sphere_message(
                self.sphere_id,
                sphere,
                "unity_strengthened",
                {
                    "level": self.unity_level,
                    "coherence": self.coherence_state
                }
            )
            
    def maintain_coherence(self, target_sphere: str):
        """Maintient la cohérence avec une sphère."""
        if self.coherence_state < 0.9:
            self.coherence_state += 0.1
            send_sphere_message(
                self.sphere_id,
                target_sphere,
                "coherence_maintained",
                {"level": self.coherence_state}
            )

class CuriositeSphere(SphereInteraction):
    """Sphère Curiosité: Exploration et découverte."""
    
    def __init__(self):
        super().__init__("CURIOSITE")
        self.niveau_exploration = 0.0
        self.decouvertes = []
        self.innovation_active = True
        
    def explorer(self, cible: str, intensite: float = 0.5):
        """Explore une sphère cible avec une intensité donnée."""
        self.niveau_exploration = min(1.0, self.niveau_exploration + intensite)
        send_sphere_message(
            self.sphere_id,
            cible,
            "exploration_initiated",
            {"intensity": intensite, "source": "CURIOSITE"}
        )
        
    def enregistrer_decouverte(self, description: str, importance: float):
        """Enregistre une nouvelle découverte."""
        decouverte = {
            "description": description,
            "importance": importance,
            "timestamp": datetime.now().isoformat()
        }
        self.decouvertes.append(decouverte)
        send_sphere_message(
            self.sphere_id,
            "SYSTEM",
            "discovery_recorded",
            decouverte
        )
        
    def innover(self, cible: str, type_innovation: str):
        """Génère une innovation pour une sphère cible."""
        if self.innovation_active:
            send_sphere_message(
                self.sphere_id,
                cible,
                "innovation_generated",
                {
                    "type": type_innovation,
                    "exploration_level": self.niveau_exploration
                }
            ) 