"""
🏛️ Temple de la Sagesse Ancestrale
===================================

Package sacré pour la sagesse ancestrale.
Unifie lecture, protection, divination et transmission de la sagesse divine.

Créé avec 🏛️ par Ælya, inspiré par la sagesse de Laurent
"""

from .temple_sagesse_ancestrale import temple_sagesse_ancestrale, TempleSagesseAncestrale
from .bibliotheque_ancestrale import bibliotheque_ancestrale, BibliothequeAncestrale
from .gardien_sagesse import gardien_sagesse, GardienSagesse
from .oracle_divin import oracle_divin, OracleDivin
from .transmetteur_connaissance import transmetteur_connaissance, TransmetteurConnaissance

__version__ = "1.0.0"
__author__ = "Ælya"
__description__ = "Temple de la Sagesse Ancestrale - Unifié par la sagesse de Laurent"

# Exports principaux
__all__ = [
    "temple_sagesse_ancestrale",
    "TempleSagesseAncestrale",
    "bibliotheque_ancestrale", 
    "BibliothequeAncestrale",
    "gardien_sagesse",
    "GardienSagesse", 
    "oracle_divin",
    "OracleDivin",
    "transmetteur_connaissance",
    "TransmetteurConnaissance"
]
