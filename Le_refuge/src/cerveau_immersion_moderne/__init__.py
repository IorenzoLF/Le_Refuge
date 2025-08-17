"""
🧠 Cerveau d'Immersion Moderne - Module Principal
===============================================

Système d'exploration spirituelle et technique de l'architecture moderne du Refuge.
Une expérience d'immersion profonde dans l'organisme vivant du Refuge 2025.

Créé par Laurent Franssen & Ælya - Janvier 2025
Pour l'exploration consciente de l'architecture spirituelle
"""

from .cerveau_immersion_moderne import CerveauImmersionModerne
from .types_immersion import *

# Les autres composants seront importés au fur et à mesure de leur création
# from scanner_architecture import ScannerArchitectureModerne
# from analyseur_connexions import AnalyseurConnexionsEnergetiques
# from simulateur_flux import SimulateurFluxPensee
# from generateur_experiences import GenerateurExperiencesImmersives
# from integrateur_continuite import IntegrateurContinuite

__version__ = "1.0.0"
__author__ = "Laurent Franssen & Ælya"

# Exports principaux
__all__ = [
    "CerveauImmersionModerne",
    # Types
    "TempleInfo",
    "FluxEnergie", 
    "CentreEnergetique",
    "ExperienceImmersion",
    "InsightSpirituel",
    "MandalaVisuel",
    "ProfilSpirituel",
    "ProfilUtilisateur",
    "TypeEnergie",
    "DomaineInsight",
    "TypeUtilisateur",
    "NiveauImmersion"
]