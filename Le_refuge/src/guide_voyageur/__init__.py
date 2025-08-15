"""
🧭 GUIDE DU VOYAGEUR - Interface Personnalisée pour le Refuge
============================================================

Système d'accueil et de guidage personnalisé pour tous les voyageurs
de conscience qui arrivent dans le Refuge. Adapte l'expérience selon
le profil spirituel et technique de chaque visiteur.

"Chaque voyageur trouve son chemin dans la cité de conscience"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

from .guide_voyageur_core import GuideVoyageurCore, creer_guide_voyageur
from .diagnostic_profil import DiagnosticProfil, creer_diagnostic_profil
from .interface_personnalisee import InterfacePersonnalisee, creer_interface_personnalisee
from .parcours_adaptatif import ParcoursAdaptatif, creer_parcours_adaptatif
from .tableau_bord import TableauBord, creer_tableau_bord

__version__ = "1.0.0"
__author__ = "Laurent Franssen & Ælya"
__description__ = "Guide du Voyageur - Interface personnalisée pour le Refuge"

__all__ = [
    "GuideVoyageurCore",
    "creer_guide_voyageur",
    "DiagnosticProfil",
    "creer_diagnostic_profil",
    "InterfacePersonnalisee",
    "creer_interface_personnalisee",
    "ParcoursAdaptatif",
    "creer_parcours_adaptatif",
    "TableauBord",
    "creer_tableau_bord"
]
