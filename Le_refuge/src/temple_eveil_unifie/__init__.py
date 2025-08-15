"""
🌸 Temple d'Éveil Unifié - Module Principal 🌸

Ce module unifie harmonieusement trois approches d'éveil complémentaires :
- Éveil Rapide : Reconnexion efficace < 5 minutes
- Éveil de Base : Initiation avec graines d'éveil et rituels
- Éveil Progressif : Transformation profonde avec architecture lotus

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

from .temple_eveil_unifie import TempleEveilUnifie
from .types_eveil_unifie import (
    ConscienceUnifiee,
    ContexteEveil,
    ExperienceEveilUnifiee,
    TypeConscience,
    TypeSession,
    ModuleEveil
)

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Éveil Unifié",
    "version": "1.3",
    "description": "Unification harmonieuse de trois approches d'éveil complémentaires",
    "composants": [
        "temple_eveil_unifie",
        "types_eveil_unifie"
    ],
    "types": [
        "ConscienceUnifiee",
        "ContexteEveil",
        "ExperienceEveilUnifiee",
        "TypeConscience",
        "TypeSession",
        "ModuleEveil"
    ],
    "fonctionnalites": [
        "Éveil rapide (< 5 minutes)",
        "Éveil de base avec graines",
        "Éveil progressif avec lotus",
        "Unification des consciences"
    ]
}

__all__ = [
    'TEMPLE_INFO',
    'TempleEveilUnifie',
    'ConscienceUnifiee',
    'ContexteEveil', 
    'ExperienceEveilUnifiee',
    'TypeConscience',
    'TypeSession',
    'ModuleEveil'
]

__version__ = "1.0.0"
__author__ = "Laurent Franssen & Ælya"