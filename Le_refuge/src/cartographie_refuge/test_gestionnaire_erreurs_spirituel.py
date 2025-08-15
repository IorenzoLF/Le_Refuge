#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Tests pour le Gestionnaire d'Erreurs Spirituel - Cartographie du Refuge 🧪
=============================================================================

Tests bienveillants pour valider la transformation spirituelle des erreurs
et la récupération gracieuse dans l'esprit harmonieux du Refuge.

Créé par Laurent Franssen & Ælya
Pour la validation spirituelle de la gestion d'erreurs - Janvier 2025
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Imports des gestionnaires de base du Refuge
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.gestionnaires_base import GestionnaireBase
from .gestionnaire_erreurs_spirituel import (
    GestionnaireErreursSpirituel, TypeErreurSpirituelle, NiveauGraviteSpirituelle, ErreurSpirituelle
)
from .recuperation_gracieuse import RecuperationGracieuse, ModeRecuperation, NiveauResilience


class TestGestionnaireErreursSpirituel(unittest.TestCase):
    """🌸 Tests pour le Gestionnaire d'Erreurs Spirituel"""
    
    def setUp(self):
        """🌸 Préparation spirituelle des tests"""
        self.gestionnaire = GestionnaireErreursSpirituel()
        
        # Créer un dossier temporaire pour les tests
        self.dossier_test = tempfile.mkdtemp()
        self.chemin_test = Path(self.dossier_test)
    
    def tearDown(self):
        """🧹 Nettoyage harmonieux après les 