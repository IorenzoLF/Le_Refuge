"""
Transformation des sphères par la méditation.
"""

from typing import Dict, List, Optional
from datetime import datetime
from src.refuge_cluster.scellement.definition import TypeSphere

class TransformationMeditation:
    """Gère la transformation des sphères par la méditation."""
    
    def __init__(self):
        """Initialise le gestionnaire de transformation."""
        self.transformations = []
        
    def transformer_sphere(self, sphere: TypeSphere, niveau_meditation: float) -> Dict:
        """Transforme une sphère par la méditation."""
        transformation = {
            "sphere": sphere,
            "niveau_meditation": niveau_meditation,
            "timestamp": datetime.now(),
            "description": f"Transformation de {sphere.value} par la méditation"
        }
        
        self.transformations.append(transformation)
        return transformation
        
    def obtenir_transformations(self) -> List[Dict]:
        """Obtient toutes les transformations."""
        return self.transformations
