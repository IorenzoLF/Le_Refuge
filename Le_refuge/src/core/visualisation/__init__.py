"""
Module de visualisation du Refuge.

🔄 RÉORGANISÉ depuis spheres/visualisation*.py et src/core/visualisation*.py
Centralise tous les systèmes de visualisation.
"""

# Visualisations principales
# TODO: Réactiver quand les modules dépendants seront migrés
# from .visualisation_textuelle import VisualisationRefuge
from .visualisation_gui import VisualisateurSpheres

# Visualisations spécialisées
# from .visualisation_3d import *
# from .visualisation_harmonies import *
# from .visualisation_cycles import *
# from .visualisation_poetique import *
# from .visualisation_transformation import *

__all__ = [
    # 'VisualisationRefuge',  # TODO: Réactiver
    'VisualisateurSpheres',
] 