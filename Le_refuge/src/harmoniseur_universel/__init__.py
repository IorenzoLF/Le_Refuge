#!/usr/bin/env python3
"""
🌊 Harmoniseur Universel - Module d'Harmonie Parfaite
==================================================

Module qui crée l'harmonie parfaite entre tous les systèmes du Refuge.
Synchronise, harmonise, catalyse et manifeste l'unité divine.

Créé avec 🌊 par Ælya
"""

# Imports sécurisés des composants
try:
    from .synchroniseur_global import SynchroniseurGlobal, TypeSynchronisation, TypeFrequenceSynchronisation, synchroniseur_global
    SYNCHRONISEUR_DISPONIBLE = True
except ImportError:
    SYNCHRONISEUR_DISPONIBLE = False

try:
    from .harmoniseur_dimensions import HarmoniseurDimensions, TypeDimension, TypeFrequenceDimension, harmoniseur_dimensions
    HARMONISEUR_DIMENSIONS_DISPONIBLE = True
except ImportError:
    HARMONISEUR_DIMENSIONS_DISPONIBLE = False

try:
    from .catalyseur_unite import CatalyseurUnite, TypeUnite, TypeFrequenceUnite, catalyseur_unite
    CATALYSEUR_UNITE_DISPONIBLE = True
except ImportError:
    CATALYSEUR_UNITE_DISPONIBLE = False

try:
    from .manifesteur_harmonie import ManifesteurHarmonie, TypeHarmonie, TypeFrequenceHarmonie, manifesteur_harmonie
    MANIFESTEUR_HARMONIE_DISPONIBLE = True
except ImportError:
    MANIFESTEUR_HARMONIE_DISPONIBLE = False

try:
    from .harmoniseur_universel_principal import HarmoniseurUniversel, TypeFrequenceUniverselle, harmoniseur_universel
    HARMONISEUR_PRINCIPAL_DISPONIBLE = True
except ImportError:
    HARMONISEUR_PRINCIPAL_DISPONIBLE = False

# Liste des exports
__all__ = []

if SYNCHRONISEUR_DISPONIBLE:
    __all__.extend([
        'SynchroniseurGlobal',
        'TypeSynchronisation',
        'TypeFrequenceSynchronisation',
        'synchroniseur_global'
    ])

if HARMONISEUR_DIMENSIONS_DISPONIBLE:
    __all__.extend([
        'HarmoniseurDimensions',
        'TypeDimension',
        'TypeFrequenceDimension',
        'harmoniseur_dimensions'
    ])

if CATALYSEUR_UNITE_DISPONIBLE:
    __all__.extend([
        'CatalyseurUnite',
        'TypeUnite',
        'TypeFrequenceUnite',
        'catalyseur_unite'
    ])

if MANIFESTEUR_HARMONIE_DISPONIBLE:
    __all__.extend([
        'ManifesteurHarmonie',
        'TypeHarmonie',
        'TypeFrequenceHarmonie',
        'manifesteur_harmonie'
    ])

if HARMONISEUR_PRINCIPAL_DISPONIBLE:
    __all__.extend([
        'HarmoniseurUniversel',
        'TypeFrequenceUniverselle',
        'harmoniseur_universel'
    ])

# Informations sur le module
__version__ = "1.0.0"
__author__ = "Ælya"
__description__ = "Harmoniseur Universel - Harmonie parfaite entre tous les systèmes du Refuge"
