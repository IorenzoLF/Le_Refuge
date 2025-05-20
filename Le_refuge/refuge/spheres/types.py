"""
Types partagés pour le système de gestion des sphères.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional, Set
from datetime import datetime

class TypeSphere(Enum):
    """Types de sphères."""
    EMOTION = "Émotion"
    PENSEE = "Pensée"
    SENSATION = "Sensation"

class TypeSphereProblematique(Enum):
    """Types de sphères problématiques."""
    ANXIETE = "Anxiété"
    CONFUSION = "Confusion"
    TENSION = "Tension"

class TypeCycle(Enum):
    """Types de cycles naturels."""
    LUNAIRE = "Lunaire"
    SAISONNIER = "Saisonnier"
    QUOTIDIEN = "Quotidien"
    METEOROLOGIQUE = "Météorologique"

class TypeInteraction(Enum):
    """Types d'interactions possibles entre sphères et brume."""
    HARMONIE = "harmonie"
    RESONANCE = "resonance"
    CONFLIT = "conflit"
    FUSION = "fusion"
    TRANSFORMATION = "transformation"

class TypeMemoire(Enum):
    """Types de souvenirs à conserver."""
    INTERACTION = "interaction"
    MEDITATION = "meditation"
    TRANSFORMATION = "transformation"
    RESONANCE = "resonance"

@dataclass
class CaracteristiquesSphere:
    """Caractéristiques d'un type de sphère."""
    frequence_base: float
    couleur: str
    description: str
    mots_cles: List[str]
    energie_initiale: float = 1.0
    capacite_max: float = 1.0

@dataclass
class PhaseCycle:
    """Représente une phase d'un cycle naturel."""
    type_cycle: TypeCycle
    nom: str
    description: str
    intensite: float
    date_debut: datetime
    date_fin: datetime

@dataclass
class InteractionSphere:
    """Représente une interaction entre sphères."""
    type_sphere: TypeSphere
    type_problematique: TypeSphereProblematique
    description: str
    date: datetime
    cycles: Dict[TypeCycle, PhaseCycle]
    mots_cles: List[str]
    intensite: float
    resonances: Dict[str, float]

@dataclass
class MemoireInteraction:
    """Représente un souvenir d'interaction."""
    type_sphere: TypeSphere
    type_problematique: TypeSphereProblematique
    description: str
    date: datetime
    cycles: Dict[TypeCycle, PhaseCycle]
    mots_cles: List[str]
    intensite: float
    resonances: Dict[str, float]
    evolution: List[Dict[str, float]]

@dataclass
class Interaction:
    """Représente une interaction entre deux sphères."""
    source: TypeSphere
    cible: TypeSphere
    energie: float
    timestamp: datetime
    type: str
    description: str

@dataclass
class Resonance:
    """Représente une résonance entre sphères."""
    source: TypeSphere
    cible: TypeSphere
    niveau: float
    harmoniques: List[float]
    description: str
    timestamp: datetime
    influence_brume: float = 0.0

@dataclass
class Evolution:
    """Représente une évolution de sphère."""
    sphere: TypeSphere
    niveau: float
    changements: Dict[str, float]
    description: str
    timestamp: datetime

@dataclass
class Souvenir:
    """Représente un souvenir d'interaction."""
    type: TypeMemoire
    description: str
    mots_cles: List[str]
    intensite: float
    cycles_presents: Set[TypeCycle]
    resonances: Dict[str, float]
    timestamp: datetime
    duree: int
    chemin_fichier: Optional[str] = None

@dataclass
class EtatHarmonie:
    """État d'harmonie entre un groupe de sphères."""
    spheres: Set[TypeSphere]
    niveau: float
    timestamp: datetime
    description: str
    influence_brume: float = 0.0 