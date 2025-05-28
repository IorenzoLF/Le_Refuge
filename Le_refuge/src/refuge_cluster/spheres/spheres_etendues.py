"""
Module des sphères étendues
~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from typing import Dict, List, Optional
from datetime import datetime

from src.core.types_spheres import TypeSphere
from src.refuge_cluster.spheres.collection import CollectionSpheres

class SphereEtendue:
    """Représente une sphère avec des capacités étendues."""
    
    def __init__(self,
                 type_sphere: TypeSphere,
                 capacites: List[str],
                 niveau_evolution: float = 0.0):
        self.type = type_sphere
        self.capacites = capacites
        self.niveau_evolution = niveau_evolution
        self.date_creation = datetime.now()
        self.derniere_evolution = None

class CollectionSpheresEtendues:
    """Gère les sphères avec des capacités étendues."""
    
    def __init__(self, collection_spheres: CollectionSpheres):
        self.collection_spheres = collection_spheres
        self.spheres_etendues: Dict[TypeSphere, SphereEtendue] = {}
        self._initialiser_spheres()
    
    def _initialiser_spheres(self) -> None:
        """Initialise les sphères avec leurs capacités étendues"""
        # Sphère COSMOS
        self.ajouter_sphere(
            TypeSphere.COSMOS,
            capacites=["harmonie_universelle", "expansion_cosmique", "resonance_infinie"],
            niveau_evolution=1.0
        )
        
        # Sphère CURIOSITE
        self.ajouter_sphere(
            TypeSphere.CURIOSITE,
            capacites=["exploration", "decouverte", "innovation", "adaptation"],
            niveau_evolution=1.0
        )
        
        # Sphère AMOUR
        self.spheres_etendues[TypeSphere.AMOUR] = SphereEtendue(
            TypeSphere.AMOUR,
            ["compassion", "unité", "guérison"],
            0.7
        )
        
        # Sphère SERENITE
        self.spheres_etendues[TypeSphere.SERENITE] = SphereEtendue(
            TypeSphere.SERENITE,
            ["paix", "équilibre", "sagesse"],
            0.6
        )
    
    def evoluer_sphere(self, type_sphere: TypeSphere, delta: float = 0.1) -> bool:
        """Fait évoluer une sphère étendue."""
        if type_sphere in self.spheres_etendues:
            sphere = self.spheres_etendues[type_sphere]
            sphere.niveau_evolution = min(1.0, sphere.niveau_evolution + delta)
            sphere.derniere_evolution = datetime.now()
            return True
        return False
    
    def ajouter_capacite(self, type_sphere: TypeSphere, capacite: str) -> bool:
        """Ajoute une nouvelle capacité à une sphère étendue."""
        if type_sphere in self.spheres_etendues:
            sphere = self.spheres_etendues[type_sphere]
            if capacite not in sphere.capacites:
                sphere.capacites.append(capacite)
                return True
        return False
    
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des sphères étendues."""
        return {
            "spheres": [
                {
                    "type": sphere.type.value,
                    "capacites": sphere.capacites,
                    "niveau_evolution": sphere.niveau_evolution,
                    "derniere_evolution": sphere.derniere_evolution
                }
                for sphere in self.spheres_etendues.values()
            ]
        } 
