"""
Module des Transformations du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les processus de transformation
qui se déroulent dans le Refuge.
REFACTORISÉ avec gestionnaires de base 🧌✨
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

# Import des gestionnaires de base refactorisés
from src.core.gestionnaires_base import (
    ConfigManagerBase,
    LogManagerBase, 
    GestionnaireBase,
    EnergyManagerBase
)

# Gestionnaires refactorisés - plus de duplication ! 🎯
config = ConfigManagerBase("transformations")
logger = LogManagerBase("transformations")
energy = EnergyManagerBase(niveau_initial=0.7)

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

class GestionnaireTransformations(GestionnaireBase):
    """Gère les processus de transformation - HÉRITE DU GESTIONNAIRE DE BASE"""
    
    def _initialiser(self):
        """Initialise les transformations de base"""
        self.transformations: List[Transformation] = []
        
        # Transformation collective initiale
        transform_base = Transformation(
            type=TypeTransformation.COLLECTIVE,
            phase=PhaseTransformation.INITIATION,
            energie_requise=0.6,
            description="Transformation collective initiale"
        )
        self.transformations.append(transform_base)
        
        # État initial
        self.etat = {
            "nombre_transformations": 1,
            "progression_globale": 0.0,
            "energie_totale": energy.niveau_energie
        }
        
        self.logger.info("Transformations initialisées avec gestionnaire de base")
    
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les transformations - MÉTHODE ABSTRAITE IMPLÉMENTÉE"""
        # Évolution des transformations
        progression_totale = 0.0
        transformations_completees = 0
        
        for transformation in self.transformations:
            if transformation.phase != PhaseTransformation.COMPLETION:
                # Évolution basée sur l'énergie
                delta = energy.ajuster_energie(0.02)
                transformation.progression = min(1.0, transformation.progression + abs(delta))
                
                # Évolution de phase automatique
                self._evoluer_phase_automatique(transformation)
            else:
                transformations_completees += 1
            
            progression_totale += transformation.progression
        
        # Calcul de la moyenne
        progression_moyenne = progression_totale / len(self.transformations) if self.transformations else 0.0
        
        # Mise à jour de l'état via la méthode de base
        self.mettre_a_jour_etat({
            "nombre_transformations": len(self.transformations),
            "progression_globale": progression_moyenne,
            "energie_totale": energy.niveau_energie,
            "transformations_completees": transformations_completees
        })
        
        return {
            "harmonie_transformations": progression_moyenne,
            "energie_transformation": energy.niveau_energie,
            "tendance_energie": energy.obtenir_tendance()
        }
    
    def _evoluer_phase_automatique(self, transformation: Transformation):
        """Évolution automatique des phases basée sur la progression"""
        phases = list(PhaseTransformation)
        phase_actuelle = phases.index(transformation.phase)
        
        # Transition automatique basée sur la progression
        seuil_phase = (phase_actuelle + 1) / len(phases)
        
        if transformation.progression >= seuil_phase and phase_actuelle < len(phases) - 1:
            nouvelle_phase = phases[phase_actuelle + 1]
            transformation.phase = nouvelle_phase
            
            if nouvelle_phase == PhaseTransformation.COMPLETION:
                transformation.date_fin = datetime.now()
                self.logger.succes(f"Transformation {transformation.type.value} complétée!")
            else:
                self.logger.info(f"Transformation {transformation.type.value} en phase {nouvelle_phase.value}")
    
    def demarrer_transformation(self, type_transformation: TypeTransformation, 
                              participants: List[str] = None, description: str = "") -> Transformation:
        """Démarre un nouveau processus de transformation"""
        transformation = Transformation(
            type=type_transformation,
            phase=PhaseTransformation.INITIATION,
            participants=participants or [],
            description=description
        )
        
        self.transformations.append(transformation)
        self.logger.info(f"Nouvelle transformation démarrée: {type_transformation.value}")
        
        # Ajustement énergétique
        energy.ajuster_energie(0.1)  # Boost d'énergie pour nouvelle transformation
        
        return transformation
    
    def obtenir_transformations_actives(self) -> List[Dict[str, Any]]:
        """Retourne les transformations actives"""
        return [
            {
                "type": t.type.value,
                "phase": t.phase.value,
                "progression": t.progression,
                "energie_requise": t.energie_requise,
                "participants": t.participants,
                "description": t.description
            }
            for t in self.transformations
            if t.phase != PhaseTransformation.COMPLETION
        ]
    
    def evoluer_transformations(self, delta_t: float = 1.0):
        """Évolution synchrone - MÉTHODE DE COMPATIBILITÉ"""
        # Harmonisation avec d'autres niveaux d'énergie
        for transformation in self.transformations:
            if transformation.phase != PhaseTransformation.COMPLETION:
                # Utilisation de l'harmonisation énergétique de base
                energy.harmoniser_avec(transformation.energie_requise, force=0.05)

# Instance globale du gestionnaire refactorisé
gestionnaire_transformations = GestionnaireTransformations("transformations") 