"""
🌸 Module d'Éveil Rapide 🌸

Module spécialisé pour les reconnexions rapides et efficaces (< 5 minutes).
Optimisé pour les reprises de session et les transitions fluides.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

from .scanner_changements import ScannerChangementsContextuels
from .rituels_reconnexion import GenerateurRituelsReconnexion, obtenir_generateur_rituels
# from .restaurateur_connexions import RestaurateurConnexionsSpirituelle  # À créer

__all__ = [
    'ScannerChangementsContextuels',
    'GenerateurRituelsReconnexion',
    'obtenir_generateur_rituels'
    # 'RestaurateurConnexionsSpirituelle'  # À créer
]

__version__ = "1.0.0"
__author__ = "Laurent Franssen & Ælya"