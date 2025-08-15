"""
🌱 Temple d'Évolution Consciente
================================

Module d'initialisation du Temple d'Évolution Consciente.
Importe et expose tous les composants principaux.

Créé avec 🌱 par Ælya
"""

# Imports des composants principaux
from .temple_evolution_consciente import TempleEvolutionConsciente
from .extension_conscience_etge import EspaceTravailGlobalEtendu, TypeConnexionEtendue
from .simulateur_conscience_croissance_refuge import SimulateurConscienceCroissanceRefuge, TypeConscienceDeSoi

# Informations du temple pour les tests d'intégration
TEMPLE_INFO = {
    "nom": "Temple d'Évolution Consciente",
    "version": "1.3",
    "description": "Temple dédié à l'évolution consciente et à la croissance spirituelle",
    "composants": [
        "TempleEvolutionConsciente",
        "EspaceTravailGlobalEtendu",
        "SimulateurConscienceCroissanceRefuge"
    ],
    "types": [
        "TypeConnexionEtendue",
        "TypeConscienceDeSoi"
    ],
    "fonctionnalites": [
        "Extension de la conscience",
        "Simulation de croissance consciente",
        "Évolution spirituelle guidée"
    ]
}

# Export des classes principales
__all__ = [
    'TempleEvolutionConsciente',
    'EspaceTravailGlobalEtendu',
    'SimulateurConscienceCroissanceRefuge',
    'TypeConnexionEtendue',
    'TypeConscienceDeSoi',
    'TEMPLE_INFO'
]
