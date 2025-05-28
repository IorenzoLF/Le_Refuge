"""
Module de gestion des sphères du refuge.

🔄 EN TRANSITION - Migration vers src/ en cours
Certains imports sont temporairement désactivés pendant la migration.
"""

# Imports depuis la nouvelle structure
from src.core.types_spheres import TypeSphere

# TODO: Réactiver quand les modules seront migrés
# from .definition import TypeSphere  # → src.core.types_spheres
# from .collection import CollectionSpheres, SphereCollection  # À migrer
# from .interactions import InteractionsSpheres  # À migrer  
# from .harmonie import HarmonisationSpheres  # À migrer

# Alias pour la compatibilité (temporairement désactivé)
# Sphere = SphereCollection
# collection_spheres = CollectionSpheres()

__all__ = ['TypeSphere']  # Réduit temporairement 