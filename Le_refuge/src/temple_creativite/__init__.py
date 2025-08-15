"""
🎨 Temple de la Créativité
=========================

Module d'initialisation du Temple de la Créativité.
Importe et expose tous les composants principaux.

Créé avec 🎨 par Ælya
"""

# Imports des composants principaux
from .temple_creativite_principal import TempleCreativite
from .harmoniseur_expression import harmoniseur_expression, TypeExpression
from .catalyseur_innovation import catalyseur_innovation, TypeInnovation
from .manifesteur_art import manifesteur_art, TypeArt
from .inspirateur_idees import inspirateur_idees, TypeInspiration

# Informations du temple pour les tests d'intégration
TEMPLE_INFO = {
    "nom": "Temple de la Créativité",
    "version": "1.3",
    "description": "Temple dédié à la créativité, l'innovation et l'expression artistique",
    "composants": [
        "TempleCreativite",
        "harmoniseur_expression",
        "catalyseur_innovation",
        "manifesteur_art",
        "inspirateur_idees"
    ],
    "types": [
        "TypeExpression",
        "TypeInnovation",
        "TypeArt",
        "TypeInspiration"
    ],
    "fonctionnalites": [
        "Harmonisation de l'expression créative",
        "Catalyse de l'innovation",
        "Manifestation de l'art",
        "Inspiration d'idées créatives"
    ]
}

# Export des classes principales
__all__ = [
    'TempleCreativite',
    'harmoniseur_expression',
    'catalyseur_innovation',
    'manifesteur_art',
    'inspirateur_idees',
    'TypeExpression',
    'TypeInnovation',
    'TypeArt',
    'TypeInspiration',
    'TEMPLE_INFO'
]
