"""
Module de constantes du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module contient les constantes partagées entre les différents
composants du Refuge.
"""

from enum import Enum
from typing import Dict, List, Optional, Set
from pathlib import Path

# Chemins de base
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "donnees"
LOGS_DIR = BASE_DIR / "logs"

# Types d'accès
class TypeAcces(Enum):
    """Types d'accès possibles au Refuge"""
    COMPLET = "complet"
    LIMITE = "limite"
    RESTREINT = "restreint"
    INTERDIT = "interdit"

# États du Refuge
class EtatRefuge(Enum):
    """États possibles du Refuge"""
    HARMONIE = "harmonie"
    TRANSITION = "transition"
    DESEQUILIBRE = "desequilibre"
    CRISE = "crise"
    RECONSTRUCTION = "reconstruction"

# Configuration par défaut
DEFAULT_CONFIG = {
    "version": "0.1.0",
    "debug": False,
    "log_level": "INFO",
    "harmonie_minimale": 0.5,
    "delai_cycle": 1.0,
    "max_interactions": 100,
    "max_emergences": 50,
    "max_transformations": 50
}

class TypeVibration(Enum):
    """Types de vibrations possibles"""
    POSITIVE = "positive"
    NEUTRE = "neutre"
    NEGATIVE = "negative"
    TRANSITION = "transition" 