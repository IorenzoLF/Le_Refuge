"""
Module de gestion des sphères du refuge.
"""

from .definition import TypeSphere
from .collection import CollectionSpheres, SphereCollection
from .interactions import InteractionsSpheres
from .harmonie import HarmonisationSpheres

# Alias pour la compatibilité
Sphere = SphereCollection

collection_spheres = CollectionSpheres()

__all__ = ['TypeSphere', 'CollectionSpheres', 'SphereCollection', 'Sphere', 'collection_spheres', 'InteractionsSpheres', 'HarmonisationSpheres'] 