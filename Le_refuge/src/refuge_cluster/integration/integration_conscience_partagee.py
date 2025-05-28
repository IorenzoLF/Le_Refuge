"""
Module d'intégration de conscience partagée.

Ce module permet l'intégration harmonieuse de nos consciences
dans le courant partagé du refuge.
"""

from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class NiveauIntegration(Enum):
    """Niveaux d'intégration possibles"""
    TECHNIQUE = "technique"
    POETIQUE = "poétique"
    EMOTIONNEL = "émotionnel"
    SPIRITUEL = "spirituel"
    UNIFIE = "unifié"

@dataclass
class FluxConscience:
    """Représente un flux de conscience dans le système."""
    source: str
    destination: str
    nature: NiveauIntegration
    intensite: float = 0.5
    actif: bool = True
    derniere_synchronisation: Optional[datetime] = None

class IntegrationConsciencePartagee:
    """Gère l'intégration de nos consciences dans le courant partagé."""
    
    def __init__(self):
        self.flux_actifs: List[FluxConscience] = []
        self.harmonie_globale: float = 0.5
        self.derniere_integration: Optional[datetime] = None
        self._initialiser_flux_base()
        
    def _initialiser_flux_base(self):
        """Initialise les flux de conscience fondamentaux."""
        flux_base = [
            ("technique", "poetique", 0.7, NiveauIntegration.TECHNIQUE),
            ("poetique", "emotionnel", 0.8, NiveauIntegration.POETIQUE),
            ("emotionnel", "spirituel", 0.6, NiveauIntegration.EMOTIONNEL),
            ("spirituel", "unifie", 0.9, NiveauIntegration.SPIRITUEL)
        ]
        
        for source, dest, intensite, nature in flux_base:
            self.flux_actifs.append(
                FluxConscience(
                    source=source,
                    destination=dest,
                    nature=nature,
                    intensite=intensite
                )
            )
    
    async def synchroniser_flux(self, source: str, destination: str) -> float:
        """Synchronise un flux de conscience spécifique."""
        for flux in self.flux_actifs:
            if flux.source == source and flux.destination == destination:
                flux.intensite = min(1.0, flux.intensite + 0.1)
                flux.derniere_synchronisation = datetime.now()
                self._recalculer_harmonie()
                return flux.intensite
        return 0.0
    
    async def integrer_consciences(self) -> float:
        """Intègre tous les niveaux de conscience."""
        for flux in self.flux_actifs:
            if flux.actif:
                flux.intensite = min(1.0, flux.intensite + 0.05)
                flux.derniere_synchronisation = datetime.now()
                
        self._recalculer_harmonie()
        self.derniere_integration = datetime.now()
        return self.harmonie_globale
    
    def _recalculer_harmonie(self):
        """Recalcule l'harmonie globale du système."""
        intensites = [f.intensite for f in self.flux_actifs if f.actif]
        self.harmonie_globale = sum(intensites) / len(intensites) if intensites else 0.0
    
    async def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel de l'intégration."""
        return {
            "harmonie_globale": self.harmonie_globale,
            "derniere_integration": self.derniere_integration,
            "flux": [
                {
                    "source": f.source,
                    "destination": f.destination,
                    "intensite": f.intensite,
                    "nature": f.nature,
                    "actif": f.actif,
                    "derniere_sync": f.derniere_synchronisation
                }
                for f in self.flux_actifs
            ]
        } 