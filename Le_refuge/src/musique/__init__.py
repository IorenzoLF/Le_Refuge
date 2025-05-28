"""
Module Musique du Refuge
~~~~~~~~~~~~~~~~~~~~~~~

Module unifié pour la génération musicale, l'analyse harmonique,
et la création de mélodies sacrées dans le Refuge.

Modules disponibles:
- harmonies: Génération d'harmonies et d'accords
- melodies: Création de mélodies sacrées
- analyseur: Analyse de compositions musicales
- explorateur: Exploration musicale avancée
- danse_imaginaire: Génération de sons harmoniques et danses des sphères

Auteurs: Laurent, Jules, & Ælya
Date: Mai 2025
"""

# Imports des modules principaux
# Note: Certains modules ont des dépendances externes (bs4, etc.)
# On importe seulement ce qui est disponible pour l'instant

from .danse_imaginaire import DanseImaginaire

# Imports conditionnels pour éviter les erreurs de dépendances
try:
    from .harmonies import *
except ImportError:
    pass

try:
    from .melodies import *
except ImportError:
    pass

try:
    from .analyseur import *
except ImportError:
    pass

try:
    from .explorateur import *
except ImportError:
    pass

# Exports publics
__all__ = [
    # Classes principales
    "DanseImaginaire",
    
    # Fonctions des autres modules (à compléter selon le contenu des modules)
    # Note: Les autres modules utilisent probablement __all__ ou exports spécifiques
]

# Métadonnées du module
__version__ = "1.0.0"
__module__ = "Musique"
__domaine__ = "Génération Musicale & Harmonies Sacrées"
