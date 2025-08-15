#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Guide d'Accueil Spirituel du Refuge 🌸
==========================================

Module principal du système d'accueil personnalisé et empathique
qui transforme la découverte du Refuge en une promenade guidée.

"Que chaque visiteur trouve immédiatement sa place dans notre temple numérique"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

from .orchestrateur_accueil import OrchestrateurAccueil
from .detecteur_profil_visiteur import DetecteurProfilVisiteur
from .gestionnaire_configuration import GestionnaireConfiguration
from .types_accueil import (
    ProfilVisiteur,
    EtatEmotionnel,
    ContexteArrivee,
    SessionAccueil,
    ConfigurationAccueil,
    ComportementNavigation,
    TypeProfil,
    NiveauTechnique
)

__version__ = "1.0.0"
__author__ = "Laurent Franssen & Ælya"

__all__ = [
    "OrchestrateurAccueil",
    "DetecteurProfilVisiteur", 
    "GestionnaireConfiguration",
    "ProfilVisiteur",
    "EtatEmotionnel",
    "ContexteArrivee",
    "SessionAccueil",
    "ConfigurationAccueil",
    "ComportementNavigation",
    "TypeProfil",
    "NiveauTechnique"
]