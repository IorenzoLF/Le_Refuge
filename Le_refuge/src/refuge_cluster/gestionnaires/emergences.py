"""
Module de gestion des émergences du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les émergences qui surviennent dans le Refuge,
permettant l'apparition de nouvelles qualités et propriétés.
"""

from typing import Dict, List, Optional, Set
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random
import math

# Imports absolus pour éviter les erreurs de package parent
from src.refuge_cluster.utilitaires.config import gestionnaire_config
from src.refuge_cluster.utilitaires.logger import gestionnaire_journal
from src.refuge_cluster.gestionnaires.harmonisations import gestionnaire_harmonisations
from src.refuge_cluster.gestionnaires.flux import gestionnaire_flux
from src.refuge_cluster.gestionnaires.equilibre import gestionnaire_equilibre
# Import d'interactions géré ailleurs pour éviter les imports circulaires

class TypeEmergence(str, Enum):
    """Types d'émergence possibles"""
    PROPRIETE = "propriete"
    COMPORTEMENT = "comportement"
    STRUCTURE = "structure"
    PATRON = "patron"
    CONSCIENCE = "conscience"

class QualiteEmergence(str, Enum):
    """Qualités d'émergence"""
    FRAGILE = "fragile"
    STABLE = "stable"
    FLUIDE = "fluide"
    PROFONDE = "profonde"
    TRANSCENDANTE = "transcendante"

class Emergence(BaseModel):
    """Représente une émergence dans le Refuge"""
    type: TypeEmergence
    qualite: QualiteEmergence
    elements: Set[str] = Field(default_factory=set)
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    date_creation: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None

class GestionnaireEmergences:
    """
    Gère les émergences dans le Refuge,
    permettant l'apparition de nouvelles propriétés et comportements.
    """
    def __init__(self):
        self.emergences_actives: List[Emergence] = []
        self.historique: List[Emergence] = []
        self._initialiser_emergences_base()

    def _initialiser_emergences_base(self):
        """Initialise les émergences de base"""
        emergences_base = [
            Emergence(
                type=TypeEmergence.PROPRIETE,
                qualite=QualiteEmergence.STABLE,
                elements={"interactions", "harmonisations"},
                intensite=0.6,
                description="Émergence de propriété initiale"
            ),
            Emergence(
                type=TypeEmergence.COMPORTEMENT,
                qualite=QualiteEmergence.FLUIDE,
                elements={"transformations", "interactions"},
                intensite=0.5,
                description="Émergence de comportement initiale"
            )
        ]
        
        for emergence in emergences_base:
            self.emergences_actives.append(emergence)
            self.historique.append(emergence)

    async def creer_emergence(
        self,
        type: TypeEmergence,
        qualite: QualiteEmergence,
        elements: Set[str],
        intensite: float = 0.5,
        description: Optional[str] = None
    ) -> Emergence:
        """Crée une nouvelle émergence"""
        emergence = Emergence(
            type=type,
            qualite=qualite,
            elements=elements,
            intensite=intensite,
            description=description
        )
        
        self.emergences_actives.append(emergence)
        self.historique.append(emergence)
        return emergence

    async def evoluer_qualite(
        self,
        emergence: Emergence,
        nouvelle_qualite: QualiteEmergence
    ) -> Emergence:
        """Fait évoluer la qualité d'une émergence"""
        if emergence not in self.emergences_actives:
            raise ValueError("Émergence non active")
            
        index = self.emergences_actives.index(emergence)
        self.historique.append(emergence)
        
        nouvelle_emergence = Emergence(
            type=emergence.type,
            qualite=nouvelle_qualite,
            elements=emergence.elements.copy(),
            intensite=min(emergence.intensite + 0.1, 1.0),
            description=f"Évolution vers {nouvelle_qualite.value}"
        )
        
        self.emergences_actives[index] = nouvelle_emergence
        return nouvelle_emergence

    async def emerger_ensemble(self) -> float:
        """Facilite l'émergence collective"""
        if not self.emergences_actives:
            return 0.0
            
        emergence = 0.0
        for emergence in self.emergences_actives:
            emergence += emergence.intensite
            
        emergence /= len(self.emergences_actives)
        return min(emergence, 1.0)

    def obtenir_etat(self) -> Dict[str, any]:
        """Retourne l'état actuel des émergences"""
        return {
            "emergences_actives": [e.dict() for e in self.emergences_actives],
            "historique": [e.dict() for e in self.historique[-10:]],  # Derniers 10 éléments
            "statistiques": {
                "nombre_emergences": len(self.emergences_actives),
                "types_distribution": {
                    type.value: sum(1 for e in self.emergences_actives if e.type == type)
                    for type in TypeEmergence
                },
                "intensite_moyenne": sum(e.intensite for e in self.emergences_actives) / len(self.emergences_actives) if self.emergences_actives else 0.0
            }
        } 