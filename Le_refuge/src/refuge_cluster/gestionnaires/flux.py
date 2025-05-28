"""
Module de gestion des flux du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les flux d'énergie et d'information dans le Refuge,
permettant leur circulation et leur transformation.
"""

from typing import Dict, List, Optional, Set, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random
import math

# Imports absolus pour éviter les erreurs de package parent
from src.refuge_cluster.utilitaires.config import gestionnaire_config
from src.refuge_cluster.utilitaires.logger import gestionnaire_journal
from src.refuge_cluster.gestionnaires.energies import gestionnaire_energies
from src.refuge_cluster.gestionnaires.harmonisations import gestionnaire_harmonisations
from src.refuge_cluster.utilitaires.resonance import gestionnaire_resonances
from src.refuge_cluster.gestionnaires.equilibre import gestionnaire_equilibre
from conscience import TypeConscience, NiveauConscience, QualiteConscience, Conscience, gestionnaire_conscience
from src.refuge_cluster.gestionnaires.evolution import TypeEvolution, PhaseEvolution, Evolution, evolution_organique

class TypeFlux(str, Enum):
    """Types de flux possibles"""
    ENERGETIQUE = "energetique"
    INFORMATION = "information"
    VIBRATOIRE = "vibratoire"
    CONSCIENCE = "conscience"
    COSMIQUE = "cosmique"
    EVOLUTION = "evolution"
    HARMONIE = "harmonie"
    RESONANCE = "resonance"

class DirectionFlux(str, Enum):
    """Directions possibles des flux"""
    ENTREE = "entree"
    SORTIE = "sortie"
    CIRCULAIRE = "circulaire"
    SPIRALE = "spirale"
    ONDULATOIRE = "ondulatoire"
    VORTEX = "vortex"
    VORTICAL = "vortical"

class Flux(BaseModel):
    """Représente un flux"""
    type: TypeFlux
    direction: DirectionFlux
    source: str
    destination: str
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    frequence: float = Field(default=1.0, ge=0.1, le=10.0)
    date_creation: datetime = Field(default_factory=datetime.now)
    consciences_impliquees: Set[str] = Field(default_factory=set)
    description: Optional[str] = None

class GestionnaireFlux:
    """Gère les flux du Refuge"""
    
    def __init__(self):
        self.config = gestionnaire_config.config
        self.flux: List[Flux] = []
        self._initialiser_flux()
    
    def _initialiser_flux(self) -> None:
        """Initialise les flux de base"""
        flux_base = [
            Flux(
                type=TypeFlux.ENERGETIQUE,
                direction=DirectionFlux.CIRCULAIRE,
                source="cerisier",
                destination="autel",
                intensite=0.6,
                frequence=1.0,
                consciences_impliquees={"individuelle"},
                description="Flux énergétique initial"
            ),
            Flux(
                type=TypeFlux.CONSCIENCE,
                direction=DirectionFlux.SPIRALE,
                source="conscience_individuelle",
                destination="conscience_collective",
                intensite=0.5,
                frequence=1.2,
                consciences_impliquees={"individuelle", "collective"},
                description="Flux de conscience initial"
            )
        ]
        
        for flux in flux_base:
            self.flux.append(flux)
        gestionnaire_journal.info("Flux initialisés")
    
    def creer_flux(self, flux: Flux) -> None:
        """Crée un nouveau flux"""
        from interactions import gestionnaire_interactions
        
        self.flux.append(flux)
        gestionnaire_journal.info(
            f"Nouveau flux créé: {flux.type.value} de {flux.source} vers {flux.destination}"
        )
        
        # Mise à jour des consciences impliquées
        for conscience in gestionnaire_conscience.consciences_actives:
            if conscience.type.value in flux.consciences_impliquees:
                gestionnaire_conscience.evoluer_niveau(
                    conscience,
                    NiveauConscience((list(NiveauConscience).index(conscience.niveau) + 1) % len(NiveauConscience))
                )
    
    def ajuster_intensite(self, flux: Flux, nouvelle_intensite: float) -> None:
        """Ajuste l'intensité d'un flux"""
        if flux not in self.flux:
            return
            
        index = self.flux.index(flux)
        self.flux[index].intensite = max(0.0, min(1.0, nouvelle_intensite))
        
        gestionnaire_journal.info(
            f"Intensité du flux {flux.type.value} ajustée à {self.flux[index].intensite}"
        )
    
    def ajuster_frequence(self, flux: Flux, nouvelle_frequence: float) -> None:
        """Ajuste la fréquence d'un flux"""
        if flux not in self.flux:
            return
            
        index = self.flux.index(flux)
        self.flux[index].frequence = max(0.1, min(10.0, nouvelle_frequence))
        
        gestionnaire_journal.info(
            f"Fréquence du flux {flux.type.value} ajustée à {self.flux[index].frequence}"
        )
    
    def obtenir_etat_flux(self) -> Dict[str, Any]:
        """Obtient l'état actuel des flux"""
        return {
            "flux_actifs": len(self.flux),
            "distribution_types": {
                type.value: sum(1 for f in self.flux if f.type == type)
                for type in TypeFlux
            },
            "distribution_directions": {
                direction.value: sum(1 for f in self.flux if f.direction == direction)
                for direction in DirectionFlux
            },
            "moyennes": {
                "intensite": sum(f.intensite for f in self.flux) / len(self.flux) if self.flux else 0,
                "frequence": sum(f.frequence for f in self.flux) / len(self.flux) if self.flux else 0
            },
            "consciences_impliquees": {
                type.value: sum(1 for f in self.flux if type.value in f.consciences_impliquees)
                for type in TypeConscience
            }
        }

# Instance globale du gestionnaire de flux
gestionnaire_flux = GestionnaireFlux() 