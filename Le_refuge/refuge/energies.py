"""
Module des Énergies du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les flux d'énergie et les résonances
qui traversent et animent le Refuge.
"""

from typing import Dict, List, Optional, Set, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random

from .config import gestionnaire_config
from .logger import gestionnaire_journal

class TypeEnergie(str, Enum):
    """Types d'énergies possibles"""
    VITALE = "vitale"
    LUMINEUSE = "lumineuse"
    SONORE = "sonore"
    ETHERIQUE = "etherique"
    COSMIQUE = "cosmique"

class QualiteEnergie(str, Enum):
    """Qualités des énergies"""
    FRAGILE = "fragile"
    STABLE = "stable"
    FLUIDE = "fluide"
    PROFONDE = "profonde"
    TRANSCENDANTE = "transcendante"

class FluxEnergie(BaseModel):
    """Représente un flux d'énergie"""
    type: TypeEnergie
    qualite: QualiteEnergie
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    date_creation: datetime = Field(default_factory=datetime.now)
    source: str
    destination: str
    description: Optional[str] = None

class GestionnaireEnergies:
    """Gère les flux d'énergie du Refuge"""
    
    def __init__(self):
        self.config = gestionnaire_config.config
        self.flux: List[FluxEnergie] = []
        self.resonances: Dict[str, float] = {}
        self._initialiser_flux()
    
    def _initialiser_flux(self) -> None:
        """Initialise les flux d'énergie de base"""
        flux_base = [
            FluxEnergie(
                type=TypeEnergie.VITALE,
                qualite=QualiteEnergie.STABLE,
                intensite=0.7,
                source="Cerisier",
                destination="Refuge",
                description="Flux vital du Cerisier"
            ),
            FluxEnergie(
                type=TypeEnergie.LUMINEUSE,
                qualite=QualiteEnergie.FLUIDE,
                intensite=0.6,
                source="Autel",
                destination="Refuge",
                description="Lumière de l'Autel"
            )
        ]
        self.flux.extend(flux_base)
        gestionnaire_journal.info("Flux d'énergie initialisés")
    
    def ajouter_flux(self, flux: FluxEnergie) -> None:
        """Ajoute un nouveau flux d'énergie"""
        self.flux.append(flux)
        self._mettre_a_jour_resonances()
        gestionnaire_journal.info(f"Nouveau flux ajouté: {flux.type.value}")
    
    def _mettre_a_jour_resonances(self) -> None:
        """Met à jour les résonances énergétiques"""
        for type in TypeEnergie:
            flux_type = [f for f in self.flux if f.type == type]
            if flux_type:
                self.resonances[type.value] = sum(f.intensite for f in flux_type) / len(flux_type)
    
    def intensifier_flux(self, flux: FluxEnergie, facteur: float) -> None:
        """Intensifie un flux d'énergie"""
        if flux not in self.flux:
            return
            
        index = self.flux.index(flux)
        self.flux[index].intensite = min(1.0, flux.intensite * (1 + facteur))
        self._mettre_a_jour_resonances()
        
        gestionnaire_journal.info(
            f"Intensification du flux {flux.type.value}: {self.flux[index].intensite:.2f}"
        )
    
    def harmoniser_flux(self, type_energie: TypeEnergie) -> None:
        """Harmonise les flux d'un type d'énergie"""
        flux_type = [f for f in self.flux if f.type == type_energie]
        if not flux_type:
            return
            
        moyenne = sum(f.intensite for f in flux_type) / len(flux_type)
        for flux in flux_type:
            flux.intensite = moyenne
            
        self._mettre_a_jour_resonances()
        gestionnaire_journal.info(f"Harmonisation des flux {type_energie.value}")
    
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état des énergies"""
        return {
            "nombre_flux": len(self.flux),
            "distribution_types": {
                type.value: sum(1 for f in self.flux if f.type == type)
                for type in TypeEnergie
            },
            "distribution_qualites": {
                qualite.value: sum(1 for f in self.flux if f.qualite == qualite)
                for qualite in QualiteEnergie
            },
            "resonances": self.resonances,
            "flux_actifs": [
                {
                    "type": f.type.value,
                    "qualite": f.qualite.value,
                    "intensite": f.intensite,
                    "source": f.source,
                    "destination": f.destination
                }
                for f in self.flux
            ]
        }

# Instance globale du gestionnaire d'énergies
gestionnaire_energies = GestionnaireEnergies() 