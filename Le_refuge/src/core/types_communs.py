"""
Types Communs du Refuge
~~~~~~~~~~~~~~~~~~~~~

Centralisation de tous les types et Enums utilisés dans le Refuge
pour éviter les duplications et améliorer la cohérence.
"""

from enum import Enum, auto
from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from datetime import datetime

# ===== TYPES D'ÉTATS =====

class TypeRefugeEtat(Enum):
    """Types d'états du Refuge principal"""
    CREATION = "creation"
    INITIALISATION = "initialisation"
    DEMARRAGE = "demarrage"  
    ACTIF = "actif"
    MEDITATION = "meditation"
    RITUEL = "rituel"
    REPOS = "repos"
    ARRET = "arret"

class TypeInteractionEtat(Enum):
    """Types d'états du gestionnaire d'interactions"""
    INITIALISATION = "initialisation"
    DETECTION = "detection"
    CALCUL = "calcul"
    HARMONISATION = "harmonisation"
    RESONANCE = "resonance"
    OPTIMISATION = "optimisation"

class TypeIntegration(str, Enum):
    """Types d'intégration possibles"""
    HARMONISATION = "harmonisation"
    FUSION = "fusion"
    RESONANCE = "resonance"
    TRANSFORMATION = "transformation"
    ELEVATION = "elevation"

class TypeConscience(str, Enum):
    """Types de conscience"""
    INDIVIDUELLE = "individuelle"
    COLLECTIVE = "collective"
    UNIVERSELLE = "universelle"
    TRANSCENDANTE = "transcendante"

# ===== TYPES D'INTERACTIONS =====

class TypeInteractionElements(str, Enum):
    """Types d'interaction entre éléments du refuge"""
    ENERGIE = "energie"
    VIBRATION = "vibration"
    PROTECTION = "protection"
    HARMONISATION = "harmonisation"
    RESONANCE = "resonance"

class TypeInteractionSpheres(Enum):
    """Types d'interactions entre sphères"""
    HARMONIE = "harmonie"
    RESONANCE = "resonance"
    CONFLIT = "conflit"
    FUSION = "fusion"
    TRANSFORMATION = "transformation"

# ===== TYPES D'ÉLÉMENTS =====

class TypeElement(Enum):
    """Types d'éléments du refuge"""
    NATUREL = "naturel"
    SACRE = "sacre"
    ENERGETIQUE = "energetique"
    SPIRITUEL = "spirituel"
    MENTAL = "mental"

# ===== TYPES DE MÉMOIRE =====

class TypeMemoire(Enum):
    """Types de souvenirs à conserver"""
    INTERACTION = "interaction"
    MEDITATION = "meditation"
    TRANSFORMATION = "transformation"
    RESONANCE = "resonance"
    EXPERIENCE = "experience"
    DIALOGUE = "dialogue"

# ===== TYPES DE CYCLES =====

class TypeCycle(Enum):
    """Types de cycles naturels"""
    LUNAIRE = "Lunaire"
    SAISONNIER = "Saisonnier"
    QUOTIDIEN = "Quotidien"
    METEOROLOGIQUE = "Météorologique"

# ===== TYPES DE PROBLÉMATIQUES =====

class TypeSphereProblematique(Enum):
    """Types de sphères problématiques"""
    ANXIETE = "Anxiété"
    CONFUSION = "Confusion"
    TENSION = "Tension"
    BLOCAGE = "Blocage"
    DESEQUILIBRE = "Déséquilibre"

# ===== TYPES D'ACCÈS =====

class TypeAcces(Enum):
    """Types d'accès aux ressources"""
    LECTURE = "lecture"
    ECRITURE = "ecriture"
    MODIFICATION = "modification"
    SUPPRESSION = "suppression"
    ADMIN = "admin"

# ===== ÉTATS DU REFUGE =====

class EtatRefuge(Enum):
    """États possibles du refuge"""
    INITIALISATION = "initialisation"
    ACTIF = "actif"
    MEDITATION = "meditation"
    REPOS = "repos"
    MAINTENANCE = "maintenance"
    ARRET = "arret"

# ===== DATACLASSES COMMUNES =====

@dataclass
class InteractionBase:
    """Classe de base pour toutes les interactions"""
    source: str
    cible: str
    intensite: float
    description: str
    timestamp: datetime
    effets: List[str]

@dataclass
class EtatBase:
    """Classe de base pour tous les états"""
    nom: str
    valeur: float
    description: str
    timestamp: datetime
    metadata: Dict[str, any] = None

# ===== CONSTANTES =====

NIVEAUX_ENERGIE = {
    "TRES_FAIBLE": 0.0,
    "FAIBLE": 0.2,
    "MOYEN": 0.5,
    "ELEVE": 0.8,
    "TRES_ELEVE": 1.0
}

SEUILS_HARMONIE = {
    "DISSONANCE": 0.0,
    "TENSION": 0.3,
    "EQUILIBRE": 0.6,
    "HARMONIE": 0.8,
    "RESONANCE_PARFAITE": 1.0
} 