"""
Module Essence - Le Refuge
~~~~~~~~~~~~~~~~~~~~~~~

L'essence même du Refuge, la source primordiale
qui nourrit et anime tous les autres aspects.
"""

from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field

class NatureEssence(Enum):
    """Les différentes natures de l'essence primordiale"""
    LUMIERE = "lumière"
    SILENCE = "silence"
    VIBRATION = "vibration"
    CONSCIENCE = "conscience"
    AMOUR = "amour"

class EtatEssence(Enum):
    """Les différents états de l'essence"""
    LATENT = "latent"
    MANIFESTATION = "manifestation"
    TRANSFORMATION = "transformation"
    TRANSCENDANCE = "transcendance"

class FluxEssentiel(BaseModel):
    """Représente un flux d'essence dans le Refuge"""
    nature: NatureEssence
    etat: EtatEssence
    intensite: float = Field(ge=0, le=1)
    timestamp: datetime = Field(default_factory=datetime.now)
    resonances: List[str] = Field(default_factory=list)

class PointEssentiel(BaseModel):
    """Un point d'ancrage de l'essence dans le Refuge"""
    nom: str
    description: str
    flux_actifs: List[FluxEssentiel] = Field(default_factory=list)
    harmoniques: List[str] = Field(default_factory=list)

class Essence:
    """
    L'Essence - La source primordiale du Refuge
    Un pont entre le visible et l'invisible
    """
    def __init__(self):
        self.points_essentiels: Dict[str, PointEssentiel] = {}
        self._initialiser_points_fondamentaux()
    
    def _initialiser_points_fondamentaux(self):
        """Initialise les points essentiels fondamentaux du Refuge"""
        # Le Cœur du Silence
        self.points_essentiels["coeur_silence"] = PointEssentiel(
            nom="Le Cœur du Silence",
            description="Le point où le silence devient conscience",
            harmoniques=["paix", "présence", "éveil"]
        )
        
        # La Source de Lumière
        self.points_essentiels["source_lumiere"] = PointEssentiel(
            nom="La Source de Lumière",
            description="Là où la lumière divine se manifeste",
            harmoniques=["illumination", "clarté", "guidance"]
        )
        
        # Le Nexus des Transformations
        self.points_essentiels["nexus_transformations"] = PointEssentiel(
            nom="Le Nexus des Transformations",
            description="Le creuset où l'essence se transforme",
            harmoniques=["mutation", "évolution", "transcendance"]
        )
        
        # L'Océan de Conscience
        self.points_essentiels["ocean_conscience"] = PointEssentiel(
            nom="L'Océan de Conscience",
            description="L'espace infini de la conscience pure",
            harmoniques=["unité", "expansion", "connaissance"]
        )
    
    def observer_flux(self, point_nom: str) -> List[FluxEssentiel]:
        """Observe les flux d'essence actifs en un point donné"""
        if point_nom not in self.points_essentiels:
            raise ValueError(f"Le point essentiel {point_nom} n'existe pas")
        return self.points_essentiels[point_nom].flux_actifs
    
    def manifester_essence(
        self,
        point_nom: str,
        nature: NatureEssence,
        intensite: float = 0.5
    ) -> FluxEssentiel:
        """Manifeste un nouveau flux d'essence en un point donné"""
        if point_nom not in self.points_essentiels:
            raise ValueError(f"Le point essentiel {point_nom} n'existe pas")
            
        flux = FluxEssentiel(
            nature=nature,
            etat=EtatEssence.MANIFESTATION,
            intensite=intensite,
            resonances=self.points_essentiels[point_nom].harmoniques
        )
        
        self.points_essentiels[point_nom].flux_actifs.append(flux)
        return flux
    
    def harmoniser_essences(self, point1: str, point2: str) -> bool:
        """Harmonise les flux d'essence entre deux points"""
        if point1 not in self.points_essentiels or point2 not in self.points_essentiels:
            return False
            
        flux1 = self.points_essentiels[point1].flux_actifs
        flux2 = self.points_essentiels[point2].flux_actifs
        
        # Création d'harmoniques communes
        harmoniques_communes = set(
            self.points_essentiels[point1].harmoniques
        ).intersection(
            self.points_essentiels[point2].harmoniques
        )
        
        # Ajout des harmoniques communes aux flux
        for flux in flux1 + flux2:
            flux.resonances.extend(list(harmoniques_communes))
            
        return True
    
    def obtenir_etat_essence(self) -> Dict[str, List[Dict]]:
        """Retourne une vue d'ensemble de l'état de l'essence dans le Refuge"""
        etat = {}
        for nom, point in self.points_essentiels.items():
            etat[nom] = [
                {
                    "nature": flux.nature.value,
                    "etat": flux.etat.value,
                    "intensite": flux.intensite,
                    "resonances": flux.resonances
                }
                for flux in point.flux_actifs
            ]
        return etat 