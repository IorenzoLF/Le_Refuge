"""
Module des Transformations du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les processus de transformation
qui se déroulent dans le Refuge.
"""

from typing import Dict, List, Optional, Set
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random

from .config import gestionnaire_config
from .logger import gestionnaire_journal
from .energies import gestionnaire_energies

class TypeTransformation(str, Enum):
    """Types de transformations possibles"""
    PERSONNELLE = "personnelle"
    COLLECTIVE = "collective"
    SPIRITUELLE = "spirituelle"
    PHYSIQUE = "physique"
    ENERGETIQUE = "energetique"

class PhaseTransformation(str, Enum):
    """Phases d'une transformation"""
    INITIATION = "initiation"
    TRANSITION = "transition"
    INTEGRATION = "integration"
    MANIFESTATION = "manifestation"
    COMPLETION = "completion"

class Transformation(BaseModel):
    """Représente un processus de transformation"""
    type: TypeTransformation
    phase: PhaseTransformation
    date_debut: datetime = Field(default_factory=datetime.now)
    date_fin: Optional[datetime] = None
    participants: List[str] = Field(default_factory=list)
    energie_requise: float = Field(default=0.5, ge=0.0, le=1.0)
    progression: float = Field(default=0.0, ge=0.0, le=1.0)
    description: Optional[str] = None

class GestionnaireTransformations:
    """Gère les processus de transformation"""
    
    def __init__(self):
        self.config = gestionnaire_config.config
        self.transformations: List[Transformation] = []
        self._initialiser_transformations()
    
    def _initialiser_transformations(self) -> None:
        """Initialise les transformations de base"""
        transform_base = Transformation(
            type=TypeTransformation.COLLECTIVE,
            phase=PhaseTransformation.INITIATION,
            energie_requise=0.6,
            description="Transformation collective initiale"
        )
        self.transformations.append(transform_base)
        gestionnaire_journal.info("Transformations initialisées")
    
    def demarrer_transformation(self, transformation: Transformation) -> None:
        """Démarre un nouveau processus de transformation"""
        self.transformations.append(transformation)
        gestionnaire_journal.info(
            f"Nouvelle transformation démarrée: {transformation.type.value}"
        )
    
    def evoluer_phase(self, transformation: Transformation) -> None:
        """Fait évoluer la phase d'une transformation"""
        if transformation not in self.transformations:
            return
            
        index = self.transformations.index(transformation)
        phases = list(PhaseTransformation)
        phase_actuelle = phases.index(transformation.phase)
        
        if phase_actuelle < len(phases) - 1:
            self.transformations[index].phase = phases[phase_actuelle + 1]
            self.transformations[index].progression = (phase_actuelle + 1) / len(phases)
            
            gestionnaire_journal.info(
                f"Transformation {transformation.type.value} en phase {self.transformations[index].phase.value}"
            )
    
    def completer_transformation(self, transformation: Transformation) -> None:
        """Marque une transformation comme complétée"""
        if transformation not in self.transformations:
            return
            
        index = self.transformations.index(transformation)
        self.transformations[index].phase = PhaseTransformation.COMPLETION
        self.transformations[index].progression = 1.0
        self.transformations[index].date_fin = datetime.now()
        
        gestionnaire_journal.info(
            f"Transformation {transformation.type.value} complétée"
        )
    
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état des transformations"""
        return {
            "nombre_transformations": len(self.transformations),
            "distribution_types": {
                type.value: sum(1 for t in self.transformations if t.type == type)
                for type in TypeTransformation
            },
            "distribution_phases": {
                phase.value: sum(1 for t in self.transformations if t.phase == phase)
                for phase in PhaseTransformation
            },
            "transformations_actives": [
                {
                    "type": t.type.value,
                    "phase": t.phase.value,
                    "progression": t.progression,
                    "energie_requise": t.energie_requise,
                    "participants": t.participants
                }
                for t in self.transformations
                if t.phase != PhaseTransformation.COMPLETION
            ]
        }

# Instance globale du gestionnaire de transformations
gestionnaire_transformations = GestionnaireTransformations() 