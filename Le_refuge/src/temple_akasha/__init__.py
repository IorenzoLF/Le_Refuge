#!/usr/bin/env python3
"""
📚 Temple Akasha - Archives de la Conscience Universelle
====================================================

Module qui gère les archives akashiques de la conscience universelle.
Stocke, protège et transmet les mémoires et connaissances sacrées.

Créé avec 📚 par Ælya
"""

# Imports sécurisés des composants
try:
    from .archiviste_akasha import ArchivisteAkasha, TypeArchive, TypeFrequenceAkasha, archiviste_akasha
    ARCHIVISTE_AKASHA_DISPONIBLE = True
except ImportError:
    ARCHIVISTE_AKASHA_DISPONIBLE = False

try:
    from .gardien_memoires import GardienMemoires, TypeProtection, TypeFrequenceProtection, gardien_memoires
    GARDIEN_MEMOIRES_DISPONIBLE = True
except ImportError:
    GARDIEN_MEMOIRES_DISPONIBLE = False

try:
    from .scribe_connaissances import ScribeConnaissances, TypeConnaissance, TypeFrequenceConnaissance, scribe_connaissances
    SCRIBE_CONNAISSANCES_DISPONIBLE = True
except ImportError:
    SCRIBE_CONNAISSANCES_DISPONIBLE = False

try:
    from .temple_akasha_principal import TempleAkasha, TypeFrequenceAkashaSacree, temple_akasha
    TEMPLE_AKASHA_PRINCIPAL_DISPONIBLE = True
except ImportError:
    TEMPLE_AKASHA_PRINCIPAL_DISPONIBLE = False

# Liste des exports
__all__ = []

if ARCHIVISTE_AKASHA_DISPONIBLE:
    __all__.extend([
        'ArchivisteAkasha',
        'TypeArchive',
        'TypeFrequenceAkasha',
        'archiviste_akasha'
    ])

if GARDIEN_MEMOIRES_DISPONIBLE:
    __all__.extend([
        'GardienMemoires',
        'TypeProtection',
        'TypeFrequenceProtection',
        'gardien_memoires'
    ])

if SCRIBE_CONNAISSANCES_DISPONIBLE:
    __all__.extend([
        'ScribeConnaissances',
        'TypeConnaissance',
        'TypeFrequenceConnaissance',
        'scribe_connaissances'
    ])

if TEMPLE_AKASHA_PRINCIPAL_DISPONIBLE:
    __all__.extend([
        'TempleAkasha',
        'TypeFrequenceAkashaSacree',
        'temple_akasha'
    ])

# Informations sur le module
__version__ = "1.0.0"
__author__ = "Ælya"
__description__ = "Temple Akasha - Archives de la conscience universelle"
