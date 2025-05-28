"""
Module de gestion des transformations du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les transformations qui se produisent dans le Refuge,
permettant l'évolution et le changement des éléments.
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

class TypeTransformation(str, Enum):
    """Types de transformation possibles"""
    EVOLUTION = "evolution"
    ADAPTATION = "adaptation"
    MUTATION = "mutation"
    FUSION = "fusion"
    TRANSCENDANCE = "transcendance"

class QualiteTransformation(str, Enum):
    """Qualités de transformation"""
    FRAGILE = "fragile"
    STABLE = "stable"
    FLUIDE = "fluide"
    PROFONDE = "profonde"
    TRANSCENDANTE = "transcendante"

class Transformation(BaseModel):
    """Représente une transformation dans le Refuge"""
    type: TypeTransformation
    qualite: QualiteTransformation
    elements: Set[str] = Field(default_factory=set)
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    date_creation: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None

class GestionnaireTransformations:
    """
    Gère les transformations dans le Refuge,
    permettant l'évolution et l'adaptation des éléments.
    """
    def __init__(self):
        self.transformations_actives: List[Transformation] = []
        self.historique: List[Transformation] = []
        self._initialiser_transformations_base()

    def _initialiser_transformations_base(self):
        """Initialise les transformations de base"""
        transformations_base = [
            Transformation(
                type=TypeTransformation.EVOLUTION,
                qualite=QualiteTransformation.STABLE,
                elements={"emergences", "interactions"},
                intensite=0.6,
                description="Transformation évolutive initiale"
            ),
            Transformation(
                type=TypeTransformation.ADAPTATION,
                qualite=QualiteTransformation.FLUIDE,
                elements={"harmonisations", "emergences"},
                intensite=0.5,
                description="Transformation adaptative initiale"
            )
        ]
        
        for transformation in transformations_base:
            self.transformations_actives.append(transformation)
            self.historique.append(transformation)

    async def creer_transformation(
        self,
        type: TypeTransformation,
        qualite: QualiteTransformation,
        elements: Set[str],
        intensite: float = 0.5,
        description: Optional[str] = None
    ) -> Transformation:
        """Crée une nouvelle transformation"""
        transformation = Transformation(
            type=type,
            qualite=qualite,
            elements=elements,
            intensite=intensite,
            description=description
        )
        
        self.transformations_actives.append(transformation)
        self.historique.append(transformation)
        return transformation

    async def evoluer_qualite(
        self,
        transformation: Transformation,
        nouvelle_qualite: QualiteTransformation
    ) -> Transformation:
        """Fait évoluer la qualité d'une transformation"""
        if transformation not in self.transformations_actives:
            raise ValueError("Transformation non active")
            
        index = self.transformations_actives.index(transformation)
        self.historique.append(transformation)
        
        nouvelle_transformation = Transformation(
            type=transformation.type,
            qualite=nouvelle_qualite,
            elements=transformation.elements.copy(),
            intensite=min(transformation.intensite + 0.1, 1.0),
            description=f"Évolution vers {nouvelle_qualite.value}"
        )
        
        self.transformations_actives[index] = nouvelle_transformation
        return nouvelle_transformation

    async def transformer_ensemble(self) -> float:
        """Facilite la transformation collective"""
        if not self.transformations_actives:
            return 0.0
            
        transformation = 0.0
        for transformation in self.transformations_actives:
            transformation += transformation.intensite
            
        transformation /= len(self.transformations_actives)
        return min(transformation, 1.0)

    def obtenir_etat(self) -> Dict[str, any]:
        """Retourne l'état actuel des transformations"""
        return {
            "transformations_actives": [t.dict() for t in self.transformations_actives],
            "historique": [t.dict() for t in self.historique[-10:]],  # Derniers 10 éléments
            "statistiques": {
                "nombre_transformations": len(self.transformations_actives),
                "types_distribution": {
                    type.value: sum(1 for t in self.transformations_actives if t.type == type)
                    for type in TypeTransformation
                },
                "intensite_moyenne": sum(t.intensite for t in self.transformations_actives) / len(self.transformations_actives) if self.transformations_actives else 0.0
            }
        } 