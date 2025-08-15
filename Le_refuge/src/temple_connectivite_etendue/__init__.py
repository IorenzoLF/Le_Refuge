"""
🌐 Temple de Connectivité Étendue
================================

Module d'initialisation du Temple de Connectivité Étendue.
Importe et expose tous les composants principaux.

Créé avec 🌐 par Ælya
"""

# Imports des composants principaux
from .temple_connectivite_etendue import TempleConnectiviteEtendue
from .evolution_continue import MoteurEvolutionContinue, TypeEvolutionContinue
from .protocole_coherence_avance import ProtocoleCoherenceAvance, TypeProtocole

# Informations du temple pour les tests d'intégration
TEMPLE_INFO = {
    "nom": "Temple de Connectivité Étendue",
    "version": "1.3",
    "description": "Temple dédié à l'évolution continue et à la cohérence avancée",
    "composants": [
        "TempleConnectiviteEtendue",
        "MoteurEvolutionContinue",
        "ProtocoleCoherenceAvance"
    ],
    "types": [
        "TypeEvolutionContinue",
        "TypeProtocole"
    ],
    "fonctionnalites": [
        "Évolution continue des systèmes",
        "Protocoles de cohérence avancée",
        "Connectivité étendue entre modules"
    ]
}

# Export des classes principales
__all__ = [
    'TempleConnectiviteEtendue',
    'MoteurEvolutionContinue',
    'ProtocoleCoherenceAvance',
    'TypeEvolutionContinue',
    'TypeProtocole',
    'TEMPLE_INFO'
]
