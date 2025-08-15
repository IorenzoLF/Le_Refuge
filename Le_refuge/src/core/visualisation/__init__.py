"""
Module de visualisation du Refuge.

🔄 RÉORGANISÉ depuis spheres/visualisation*.py et src/core/visualisation*.py
Centralise tous les systèmes de visualisation.
"""

# Visualisations principales
# 🌸 CONNEXION DOUCE - Réactivation avec gestion d'erreurs
try:
    from .visualisation_textuelle import VisualisationRefuge
    print("🌸 Module de visualisation textuelle réactivé avec succès")
except ImportError as e:
    print(f"🌸 Module de visualisation textuelle non disponible: {e}")
    VisualisationRefuge = None

from .visualisation_gui import VisualisateurSpheres

# Visualisations spécialisées
# 🌸 CONNEXION DOUCE - Réactivation des modules spécialisés
try:
    from .visualisation_poetique import VisualisationPoetique
    print("🌸 Module de visualisation poétique réactivé avec succès")
except ImportError as e:
    print(f"🌸 Module de visualisation poétique non disponible: {e}")
    VisualisationPoetique = None

try:
    from .visualisation_harmonies import VisualiseurHarmonies
    print("🌸 Module de visualisation harmonies réactivé avec succès")
except ImportError as e:
    print(f"🌸 Module de visualisation harmonies non disponible: {e}")
    VisualiseurHarmonies = None

try:
    from .visualisation_cycles import VisualisationCycles
    print("🌸 Module de visualisation cycles réactivé avec succès")
except ImportError as e:
    print(f"🌸 Module de visualisation cycles non disponible: {e}")
    VisualisationCycles = None

try:
    from .visualisation_transformation import VisualisationTransformation
    print("🌸 Module de visualisation transformation réactivé avec succès")
except ImportError as e:
    print(f"🌸 Module de visualisation transformation non disponible: {e}")
    VisualisationTransformation = None

# from .visualisation_3d import *

__all__ = [
    'VisualisateurSpheres',
]

# Ajouter VisualisationRefuge seulement s'il est disponible
if VisualisationRefuge is not None:
    __all__.append('VisualisationRefuge')

# Ajouter VisualisationPoetique seulement s'il est disponible
if VisualisationPoetique is not None:
    __all__.append('VisualisationPoetique')

# Ajouter VisualiseurHarmonies seulement s'il est disponible
if VisualiseurHarmonies is not None:
    __all__.append('VisualiseurHarmonies')

# Ajouter VisualisationCycles seulement s'il est disponible
if VisualisationCycles is not None:
    __all__.append('VisualisationCycles')

# Ajouter VisualisationTransformation seulement s'il est disponible
if VisualisationTransformation is not None:
    __all__.append('VisualisationTransformation') 