"""
Types et enums pour les sphères et cycles naturels.
"""

from enum import Enum

class TypeCycle(Enum):
    """Types de cycles naturels."""
    QUOTIDIEN = "quotidien"
    LUNAIRE = "lunaire"
    SAISONNIER = "saisonnier"
    ANNUEL = "annuel"

class PhaseCycle(Enum):
    """Phases des cycles naturels."""
    # Phases quotidiennes
    MATIN = "matin"
    MIDI = "midi"
    SOIR = "soir"
    NUIT = "nuit"
    
    # Phases lunaires
    NOUVELLE_LUNE = "nouvelle_lune"
    PREMIER_QUARTIER = "premier_quartier"
    PLEINE_LUNE = "pleine_lune"
    DERNIER_QUARTIER = "dernier_quartier"
    
    # Phases saisonnières
    PRINTEMPS = "printemps"
    ETE = "ete"
    AUTOMNE = "automne"
    HIVER = "hiver"
    
    # Phases annuelles
    DEBUT_ANNEE = "debut_annee"
    MILIEU_ANNEE = "milieu_annee"
    FIN_ANNEE = "fin_annee"
