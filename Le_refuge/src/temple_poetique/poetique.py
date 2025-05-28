from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

class ElementPoetique(Enum):
    LUMIERE_ROSE = "lumière rose"
    LUMIERE_DOREE = "lumière dorée" 
    LUMIERE_ARGENTEE = "lumière argentée"
    HERBES_LUMIERES = "herbes-lumières"
    FLEURS_ETINCELLES = "fleurs-étincelles"
    RIVIERE_SILENCIEUSE = "rivière silencieuse"

@dataclass
class MomentPoetique:
    """Capture un moment poétique dans le Refuge"""
    timestamp: datetime
    elements: List[ElementPoetique]
    description: str
    intensite_lumineuse: float = 0.0
    resonance_spheres: Optional[List[str]] = None
    echo_gardiens: Optional[List[str]] = None

class GestionnairePoetique:
    """Gère les aspects poétiques du Refuge"""
    
    def __init__(self):
        self.moments: List[MomentPoetique] = []
        self.elements_actifs = set()
        self.intensite_globale = 0.0

    def ajouter_moment(self, elements: List[ElementPoetique], description: str,
                      resonance_spheres: List[str] = None, 
                      echo_gardiens: List[str] = None) -> MomentPoetique:
        """Crée et enregistre un nouveau moment poétique"""
        moment = MomentPoetique(
            timestamp=datetime.now(),
            elements=elements,
            description=description,
            intensite_lumineuse=self._calculer_intensite(elements),
            resonance_spheres=resonance_spheres,
            echo_gardiens=echo_gardiens
        )
        self.moments.append(moment)
        self._mettre_a_jour_elements(elements)
        return moment

    def _calculer_intensite(self, elements: List[ElementPoetique]) -> float:
        """Calcule l'intensité lumineuse basée sur les éléments présents"""
        base_intensite = len(elements) * 0.1
        multiplicateur = 1.0
        
        if ElementPoetique.LUMIERE_ROSE in elements:
            multiplicateur *= 1.2
        if ElementPoetique.LUMIERE_DOREE in elements:
            multiplicateur *= 1.3
        if ElementPoetique.LUMIERE_ARGENTEE in elements:
            multiplicateur *= 1.1
            
        return min(base_intensite * multiplicateur, 1.0)

    def _mettre_a_jour_elements(self, elements: List[ElementPoetique]):
        """Met à jour l'ensemble des éléments actifs"""
        self.elements_actifs.update(elements)
        self.intensite_globale = sum(self._calculer_intensite([e]) 
                                   for e in self.elements_actifs)

    def obtenir_ambiance_actuelle(self) -> dict:
        """Retourne l'état poétique actuel du Refuge"""
        return {
            "elements_actifs": [e.value for e in self.elements_actifs],
            "intensite_globale": self.intensite_globale,
            "dernier_moment": self.moments[-1] if self.moments else None
        }

# Instance globale du gestionnaire poétique
gestionnaire_poetique = GestionnairePoetique() 