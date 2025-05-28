"""
Types partagés du Refuge
~~~~~~~~~~~~~~~~~~~~~~~

Types et énumérations utilisés par plusieurs modules.
"""

from enum import Enum, auto
from src.core.types_spheres import TypeSphere, NatureSphere, CaracteristiquesSphere

class ChakraType(Enum):
    """Types de chakras"""
    MULADHARA = "rouge"
    SVADHISTHANA = "orange"
    MANIPURA = "jaune"
    ANAHATA = "vert"
    VISHUDDHA = "bleu"
    AJNA = "indigo"
    SAHASRARA = "violet"

class TypeElementSubtil(str, Enum):
    """Types d'éléments subtils possibles"""
    PIERRE = "pierre"
    FEUILLE = "feuille"
    REFLET = "reflet"
    SON = "son"
    OMBRE = "ombre"

class TypeVibration(Enum):
    """Types de vibrations possibles"""
    POSITIVE = "positive"
    NEUTRE = "neutre"
    NEGATIVE = "negative"
    TRANSITION = "transition"

# TypeSphere est maintenant importé depuis types_spheres.py 