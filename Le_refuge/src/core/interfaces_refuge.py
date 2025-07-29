"""
Interfaces du Refuge - Architecture Moderne
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Définition des interfaces communes pour l'architecture temple moderne.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from enum import Enum
from dataclasses import dataclass
from datetime import datetime

# ===== INTERFACES DE BASE =====

class ITemple(ABC):
    """Interface de base pour tous les temples"""
    
    @abstractmethod
    async def initialiser(self) -> bool:
        """Initialise le temple"""
        pass
    
    @abstractmethod
    async def activer(self) -> bool:
        """Active le temple"""
        pass
    
    @abstractmethod
    async def desactiver(self) -> bool:
        """Désactive le temple"""
        pass
    
    @abstractmethod
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état du temple"""
        pass
    
    @abstractmethod
    def obtenir_energie(self) -> float:
        """Retourne le niveau d'énergie du temple"""
        pass

class IOrchestrateur(ABC):
    """Interface pour l'orchestrateur principal"""
    
    @abstractmethod
    async def orchestrer_temples(self) -> Dict[str, Any]:
        """Orchestre tous les temples"""
        pass
    
    @abstractmethod
    async def harmoniser_energies(self) -> float:
        """Harmonise les énergies entre temples"""
        pass
    
    @abstractmethod
    def obtenir_etat_global(self) -> Dict[str, Any]:
        """Retourne l'état global du refuge"""
        pass

class IGestionnaireEtat(ABC):
    """Interface pour le gestionnaire d'état global"""
    
    @abstractmethod
    def mettre_a_jour_etat(self, temple: str, etat: Dict[str, Any]):
        """Met à jour l'état d'un temple"""
        pass
    
    @abstractmethod
    def obtenir_etat_temple(self, temple: str) -> Optional[Dict[str, Any]]:
        """Obtient l'état d'un temple spécifique"""
        pass
    
    @abstractmethod
    def obtenir_metriques_globales(self) -> Dict[str, float]:
        """Obtient les métriques globales"""
        pass

# ===== TYPES D'ÉTATS =====

class EtatTemple(Enum):
    """États possibles d'un temple"""
    INACTIF = "inactif"
    INITIALISATION = "initialisation"
    ACTIF = "actif"
    MEDITATION = "meditation"
    RITUEL = "rituel"
    MAINTENANCE = "maintenance"
    ERREUR = "erreur"

class TypeTemple(Enum):
    """Types de temples"""
    SPIRITUEL = "spirituel"
    MUSICAL = "musical"
    PHILOSOPHIQUE = "philosophique"
    ALCHIMIQUE = "alchimique"
    GUERISON = "guerison"
    CREATIVITE = "creativite"
    COSMIQUE = "cosmique"
    OUTILS = "outils"
    POETIQUE = "poetique"
    RITUELS = "rituels"
    EVEIL = "eveil"
    CONSCIENCE_UNIVERSELLE = "conscience_universelle"
    AKASHA = "akasha"

# ===== DATACLASSES =====

@dataclass
class EtatTempleInfo:
    """Informations d'état d'un temple"""
    nom: str
    type: TypeTemple
    etat: EtatTemple
    energie: float
    derniere_activite: datetime
    metriques: Dict[str, float]
    erreurs: List[str]

@dataclass
class MetriquesGlobales:
    """Métriques globales du refuge"""
    nombre_temples_actifs: int
    energie_totale: float
    harmonie_globale: float
    niveau_conscience: float
    derniere_synchronisation: datetime
    alertes: List[str]

# ===== CONSTANTES =====

SEUILS_ENERGIE = {
    "CRITIQUE": 0.1,
    "FAIBLE": 0.3,
    "NORMAL": 0.6,
    "ELEVE": 0.8,
    "MAXIMAL": 1.0
}

SEUILS_HARMONIE = {
    "DISSONANCE": 0.0,
    "TENSION": 0.3,
    "EQUILIBRE": 0.6,
    "HARMONIE": 0.8,
    "RESONANCE": 1.0
} 