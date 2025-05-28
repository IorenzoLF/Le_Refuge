"""
Configuration du Refuge
~~~~~~~~~~~~~~~~~~~~~

Gestion de la configuration globale du Refuge.
"""

from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Config:
    """Configuration globale du Refuge"""
    version: str = "0.1.0"
    debug: bool = False
    log_level: str = "INFO"
    max_spheres: int = 10
    max_elements: int = 50
    max_connexions: int = 100

class GestionnaireConfig:
    """Gestionnaire de la configuration du Refuge"""
    def __init__(self):
        self.config = Config()
    
    def charger_config(self, config_dict: Dict[str, Any]) -> None:
        """Charge la configuration depuis un dictionnaire"""
        for key, value in config_dict.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)

# Instance globale du gestionnaire de configuration
gestionnaire_config = GestionnaireConfig() 