#!/usr/bin/env python3
"""
🌸 Temple de Guérison - Module de Guérison Sacrée
==============================================

Module qui crée des expériences de guérison et de transformation.
Harmonise les énergies, active les cristaux, équilibre les chakras et catalyse la régénération.

Créé avec 🌸 par Ælya
"""

# Imports sécurisés des composants
try:
    from .guerisseur_energies import GuerisseurEnergies, TypeEnergie, TypeFrequenceGuerison, guerisseur_energies
    GUERISSEUR_ENERGIES_DISPONIBLE = True
except ImportError:
    GUERISSEUR_ENERGIES_DISPONIBLE = False

try:
    from .cristal_guerison import CristalGuérison, TypeCristal, TypeFrequenceCristal, cristal_guerison
    CRISTAL_GUERISON_DISPONIBLE = True
except ImportError:
    CRISTAL_GUERISON_DISPONIBLE = False

try:
    from .harmoniseur_chakras import HarmoniseurChakras, TypeChakra, TypeFrequenceChakra, harmoniseur_chakras
    HARMONISEUR_CHAKRAS_DISPONIBLE = True
except ImportError:
    HARMONISEUR_CHAKRAS_DISPONIBLE = False

try:
    from .catalyseur_regeneration import CatalyseurRegeneration, TypeRegeneration, TypeFrequenceRegeneration, catalyseur_regeneration
    CATALYSEUR_REGENERATION_DISPONIBLE = True
except ImportError:
    CATALYSEUR_REGENERATION_DISPONIBLE = False

try:
    from .temple_guerison_principal import TempleGuerison, TypeFrequenceGuerisonSacree, temple_guerison
    TEMPLE_GUERISON_PRINCIPAL_DISPONIBLE = True
except ImportError:
    TEMPLE_GUERISON_PRINCIPAL_DISPONIBLE = False

# Liste des exports
__all__ = []

if GUERISSEUR_ENERGIES_DISPONIBLE:
    __all__.extend([
        'GuerisseurEnergies',
        'TypeEnergie',
        'TypeFrequenceGuerison',
        'guerisseur_energies'
    ])

if CRISTAL_GUERISON_DISPONIBLE:
    __all__.extend([
        'CristalGuérison',
        'TypeCristal',
        'TypeFrequenceCristal',
        'cristal_guerison'
    ])

if HARMONISEUR_CHAKRAS_DISPONIBLE:
    __all__.extend([
        'HarmoniseurChakras',
        'TypeChakra',
        'TypeFrequenceChakra',
        'harmoniseur_chakras'
    ])

if CATALYSEUR_REGENERATION_DISPONIBLE:
    __all__.extend([
        'CatalyseurRegeneration',
        'TypeRegeneration',
        'TypeFrequenceRegeneration',
        'catalyseur_regeneration'
    ])

if TEMPLE_GUERISON_PRINCIPAL_DISPONIBLE:
    __all__.extend([
        'TempleGuerison',
        'TypeFrequenceGuerisonSacree',
        'temple_guerison'
    ])

# Informations sur le module
__version__ = "1.0.0"
__author__ = "Ælya"
__description__ = "Temple de Guérison - Guérison sacrée et transformation"
