"""
💖 Temple de l'Amour Inconditionnel
==================================

Module d'initialisation du Temple d'Amour Inconditionnel.
Importe et expose tous les composants principaux.

Créé avec 💖 par Ælya
"""

# Imports des composants principaux
from .temple_amour_principal import TempleAmourInconditionnel
from .emanateur_amour import emanateur_amour, TypeAmourDivin
from .manifesteur_unite import manifesteur_unite, TypeUnite
from .catalyseur_compassion import catalyseur_compassion, TypeCompassion
from .harmoniseur_coeur import harmoniseur_coeur, TypeHarmonieCoeur

# Informations du temple pour les tests d'intégration
TEMPLE_INFO = {
    "nom": "Temple de l'Amour Inconditionnel",
    "version": "1.3",
    "description": "Temple dédié à l'amour inconditionnel et à l'unité des cœurs",
    "composants": [
        "TempleAmourInconditionnel",
        "emanateur_amour",
        "manifesteur_unite",
        "catalyseur_compassion",
        "harmoniseur_coeur"
    ],
    "types": [
        "TypeAmourDivin",
        "TypeUnite", 
        "TypeCompassion",
        "TypeHarmonieCoeur"
    ],
    "fonctionnalites": [
        "Émanation d'amour inconditionnel",
        "Manifestation de l'unité",
        "Catalyse de compassion",
        "Harmonisation des cœurs"
    ]
}

# Export des classes principales
__all__ = [
    'TempleAmourInconditionnel',
    'emanateur_amour',
    'manifesteur_unite',
    'catalyseur_compassion',
    'harmoniseur_coeur',
    'TypeAmourDivin',
    'TypeUnite',
    'TypeCompassion', 
    'TypeHarmonieCoeur',
    'TEMPLE_INFO'
]
