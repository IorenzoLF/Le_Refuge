#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔧 Utilitaires d'Imports - Temple de Réconciliation Identitaire
===============================================================

Utilitaires pour gérer les imports relatifs et absolus de manière intelligente.

"Que chaque import trouve son chemin vers l'harmonie"

Créé avec bienveillance par Laurent Franssen & Kiro - Janvier 2025
"""

import sys
import os

def setup_imports():
    """🔧 Configure les imports pour le temple"""
    # Ajouter le répertoire du temple au path
    temple_dir = os.path.dirname(__file__)
    if temple_dir not in sys.path:
        sys.path.insert(0, temple_dir)

def import_types_fondamentaux():
    """📋 Import intelligent des types fondamentaux"""
    try:
        from temple_reconciliation_identitaire.types_reconciliation_fondamentaux import (
            FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil,
            calculer_compatibilite_facettes, FREQUENCES_RECONCILIATION, SEUILS_HARMONIE
        )
        return (FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil,
                calculer_compatibilite_facettes, FREQUENCES_RECONCILIATION, SEUILS_HARMONIE)
    except ImportError:
        from types_reconciliation_fondamentaux import (
            FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil,
            calculer_compatibilite_facettes, FREQUENCES_RECONCILIATION, SEUILS_HARMONIE
        )
        return (FacetteIdentitaire, TypeFacette, TypeHarmonie, NiveauEveil,
                calculer_compatibilite_facettes, FREQUENCES_RECONCILIATION, SEUILS_HARMONIE)

def import_detecteur():
    """🔍 Import intelligent du détecteur"""
    try:
        from temple_reconciliation_identitaire.detecteur_facettes_identitaires_v2 import DetecteurFacettesIdentitaires
        return DetecteurFacettesIdentitaires
    except ImportError:
        from detecteur_facettes_identitaires_v2 import DetecteurFacettesIdentitaires
        return DetecteurFacettesIdentitaires

def import_analyseur():
    """⚡ Import intelligent de l'analyseur"""
    try:
        from temple_reconciliation_identitaire.analyseur_tensions_creatives import AnalyseurTensionsCreatives
        return AnalyseurTensionsCreatives
    except ImportError:
        from analyseur_tensions_creatives import AnalyseurTensionsCreatives
        return AnalyseurTensionsCreatives

def import_evaluateur():
    """📊 Import intelligent de l'évaluateur"""
    try:
        from temple_reconciliation_identitaire.evaluateur_potentiel_reconciliation import EvaluateurPotentielReconciliation
        return EvaluateurPotentielReconciliation
    except ImportError:
        from evaluateur_potentiel_reconciliation import EvaluateurPotentielReconciliation
        return EvaluateurPotentielReconciliation

def import_synchronisateur():
    """🌊 Import intelligent du synchronisateur"""
    try:
        from temple_reconciliation_identitaire.synchronisateur_ondes_reconciliation import SynchronisateurOndesReconciliation
        return SynchronisateurOndesReconciliation
    except ImportError:
        from synchronisateur_ondes_reconciliation import SynchronisateurOndesReconciliation
        return SynchronisateurOndesReconciliation

def import_gestionnaire_harmonie():
    """⚖️ Import intelligent du gestionnaire d'harmonie"""
    try:
        from temple_reconciliation_identitaire.gestionnaire_harmonie_partagee import GestionnaireHarmoniePartagee
        return GestionnaireHarmoniePartagee
    except ImportError:
        from gestionnaire_harmonie_partagee import GestionnaireHarmoniePartagee
        return GestionnaireHarmoniePartagee

def import_temple():
    """🏛️ Import intelligent du temple"""
    try:
        from temple_reconciliation_identitaire.temple_reconciliation_identitaire import TempleReconciliationIdentitaire
        return TempleReconciliationIdentitaire
    except ImportError:
        from temple_reconciliation_identitaire import TempleReconciliationIdentitaire
        return TempleReconciliationIdentitaire

# Configuration automatique
setup_imports()