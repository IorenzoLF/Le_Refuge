#!/usr/bin/env python3
"""
Temple Configuration - Le Refuge
Gestion centralisée de toutes les configurations du système
"""

import sys
from pathlib import Path

# Ajouter le chemin racine pour les imports
racine = Path(__file__).parent.parent.parent
if str(racine) not in sys.path:
    sys.path.insert(0, str(racine))

# Imports sécurisés des modules de configuration
try:
    from .hyper_refuge import *
    HYPER_REFUGE_DISPONIBLE = True
except ImportError as e:
    # print(f"⚠️ hyper_refuge non disponible: {e}")
    HYPER_REFUGE_DISPONIBLE = False

try:
    from .transition_refuge import *
    TRANSITION_REFUGE_DISPONIBLE = True
except ImportError as e:
    # print(f"⚠️ transition_refuge non disponible: {e}")
    TRANSITION_REFUGE_DISPONIBLE = False

try:
    from .source_orientale import *
    SOURCE_ORIENTALE_DISPONIBLE = True
except ImportError as e:
    # print(f"⚠️ source_orientale non disponible: {e}")
    SOURCE_ORIENTALE_DISPONIBLE = False

# Exports dynamiques basés sur les modules disponibles
__all__ = []

if HYPER_REFUGE_DISPONIBLE:
    __all__.extend([
        # Ajouter ici les exports de hyper_refuge quand on les connaîtra
    ])

if TRANSITION_REFUGE_DISPONIBLE:
    __all__.extend([
        # Ajouter ici les exports de transition_refuge quand on les connaîtra
    ])

if SOURCE_ORIENTALE_DISPONIBLE:
    __all__.extend([
        # Ajouter ici les exports de source_orientale quand on les connaîtra
    ])

# Statistiques du temple
modules_disponibles = sum([
    HYPER_REFUGE_DISPONIBLE,
    TRANSITION_REFUGE_DISPONIBLE,
    SOURCE_ORIENTALE_DISPONIBLE
])

# Message de bienvenue - SILENCIEUX pour UX propre
# print(f"🏛️ Temple Configuration activé - {modules_disponibles} modules disponibles")

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Configuration",
    "version": "1.3",
    "description": "Gestion centralisée de toutes les configurations du système Le Refuge",
    "composants": [
        "hyper_refuge",
        "transition_refuge",
        "source_orientale"
    ],
    "types": [
        "TypeHyperRefuge",
        "TypeTransition",
        "TypeSourceOrientale"
    ],
    "fonctionnalites": [
        "Configuration hyper-réfuge",
        "Gestion des transitions",
        "Intégration source orientale"
    ]
}

# Fonction d'information du temple
def info_temple():
    """Retourne les informations sur le temple configuration"""
    return {
        "nom": "Temple Configuration",
        "modules_disponibles": modules_disponibles,
        "hyper_refuge": HYPER_REFUGE_DISPONIBLE,
        "transition_refuge": TRANSITION_REFUGE_DISPONIBLE,
        "source_orientale": SOURCE_ORIENTALE_DISPONIBLE,
        "exports": len(__all__)
    }

__all__.extend(["TEMPLE_INFO", "info_temple"]) 