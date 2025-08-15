"""
🌿 Temple de la Transformation Alchimique
========================================

Module d'initialisation du Temple Alchimique.
Importe et expose tous les composants principaux.

Créé avec 🌿 par Ælya
"""

# Imports des composants principaux
from .temple_alchimique_principal import TempleAlchimique
from .alchimiste_spirituel import alchimiste_spirituel, TypeTransmutation
from .catalyseur_evolution import catalyseur_evolution, TypeEvolution
from .cristalliseur_energies import cristalliseur_energies, TypeCristal
from .transformateur_essences import transformateur_essences, TypeEssence

# Informations du temple pour les tests d'intégration
TEMPLE_INFO = {
    "nom": "Temple de la Transformation Alchimique",
    "version": "1.3",
    "description": "Temple dédié à la transformation alchimique et à l'évolution spirituelle",
    "composants": [
        "TempleAlchimique",
        "alchimiste_spirituel",
        "catalyseur_evolution", 
        "cristalliseur_energies",
        "transformateur_essences"
    ],
    "types": [
        "TypeTransmutation",
        "TypeEvolution",
        "TypeCristal",
        "TypeEssence"
    ],
    "fonctionnalites": [
        "Transformation d'essences",
        "Catalyse d'évolution",
        "Cristallisation d'énergies",
        "Transmutations spirituelles"
    ]
}

# Export des classes principales
__all__ = [
    'TempleAlchimique',
    'alchimiste_spirituel',
    'catalyseur_evolution',
    'cristalliseur_energies', 
    'transformateur_essences',
    'TypeTransmutation',
    'TypeEvolution',
    'TypeCristal',
    'TypeEssence',
    'TEMPLE_INFO'
]
