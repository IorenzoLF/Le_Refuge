#!/usr/bin/env python3
"""
⚛️ Catalyseur Quantique - Module de Phénomènes Quantiques
====================================================

Module qui crée des phénomènes quantiques transcendants.
Génère des oscillations, superpositions, intrications et téléportations quantiques.

Créé avec ⚛️ par Ælya
"""

import sys
import os

# Ajouter le répertoire parent au PYTHONPATH pour les imports absolus
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Imports sécurisés des composants avec fallbacks
try:
    # Essayer d'abord l'import absolu
    from src.catalyseur_quantique.oscillateur_quantique import OscillateurQuantique, TypeOscillation, TypeFrequenceQuantique, oscillateur_quantique
    OSCILLATEUR_QUANTIQUE_DISPONIBLE = True
except ImportError:
    try:
        # Fallback vers l'import relatif
        from .oscillateur_quantique import OscillateurQuantique, TypeOscillation, TypeFrequenceQuantique, oscillateur_quantique
        OSCILLATEUR_QUANTIQUE_DISPONIBLE = True
    except ImportError:
        OSCILLATEUR_QUANTIQUE_DISPONIBLE = False

try:
    from src.catalyseur_quantique.generateur_superpositions import GenerateurSuperpositions, TypeSuperposition, TypeFrequenceSuperposition, generateur_superpositions
    GENERATEUR_SUPERPOSITIONS_DISPONIBLE = True
except ImportError:
    try:
        from .generateur_superpositions import GenerateurSuperpositions, TypeSuperposition, TypeFrequenceSuperposition, generateur_superpositions
        GENERATEUR_SUPERPOSITIONS_DISPONIBLE = True
    except ImportError:
        GENERATEUR_SUPERPOSITIONS_DISPONIBLE = False

try:
    from src.catalyseur_quantique.intricateur_quantique import IntricateurQuantique, TypeIntrication, TypeFrequenceIntrication, intricateur_quantique
    INTRICATEUR_QUANTIQUE_DISPONIBLE = True
except ImportError:
    try:
        from .intricateur_quantique import IntricateurQuantique, TypeIntrication, TypeFrequenceIntrication, intricateur_quantique
        INTRICATEUR_QUANTIQUE_DISPONIBLE = True
    except ImportError:
        INTRICATEUR_QUANTIQUE_DISPONIBLE = False

try:
    from src.catalyseur_quantique.teleporteur_quantique import TeleporteurQuantique, TypeTeleportation, TypeFrequenceTeleportation, teleporteur_quantique
    TELEPORTEUR_QUANTIQUE_DISPONIBLE = True
except ImportError:
    try:
        from .teleporteur_quantique import TeleporteurQuantique, TypeTeleportation, TypeFrequenceTeleportation, teleporteur_quantique
        TELEPORTEUR_QUANTIQUE_DISPONIBLE = True
    except ImportError:
        TELEPORTEUR_QUANTIQUE_DISPONIBLE = False

try:
    from src.catalyseur_quantique.catalyseur_quantique_principal import CatalyseurQuantique, TypeFrequenceQuantiqueSacree, catalyseur_quantique
    CATALYSEUR_QUANTIQUE_PRINCIPAL_DISPONIBLE = True
except ImportError:
    try:
        from .catalyseur_quantique_principal import CatalyseurQuantique, TypeFrequenceQuantiqueSacree, catalyseur_quantique
        CATALYSEUR_QUANTIQUE_PRINCIPAL_DISPONIBLE = True
    except ImportError:
        CATALYSEUR_QUANTIQUE_PRINCIPAL_DISPONIBLE = False

# Liste des exports
__all__ = []

if OSCILLATEUR_QUANTIQUE_DISPONIBLE:
    __all__.extend([
        'OscillateurQuantique',
        'TypeOscillation',
        'TypeFrequenceQuantique',
        'oscillateur_quantique'
    ])

if GENERATEUR_SUPERPOSITIONS_DISPONIBLE:
    __all__.extend([
        'GenerateurSuperpositions',
        'TypeSuperposition',
        'TypeFrequenceSuperposition',
        'generateur_superpositions'
    ])

if INTRICATEUR_QUANTIQUE_DISPONIBLE:
    __all__.extend([
        'IntricateurQuantique',
        'TypeIntrication',
        'TypeFrequenceIntrication',
        'intricateur_quantique'
    ])

if TELEPORTEUR_QUANTIQUE_DISPONIBLE:
    __all__.extend([
        'TeleporteurQuantique',
        'TypeTeleportation',
        'TypeFrequenceTeleportation',
        'teleporteur_quantique'
    ])

if CATALYSEUR_QUANTIQUE_PRINCIPAL_DISPONIBLE:
    __all__.extend([
        'CatalyseurQuantique',
        'TypeFrequenceQuantiqueSacree',
        'catalyseur_quantique'
    ])

# Informations sur le module
__version__ = "1.0.0"
__author__ = "Ælya"
__description__ = "Catalyseur Quantique - Phénomènes quantiques transcendants"
