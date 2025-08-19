"""
Définitions des types et caractéristiques pour le module scellement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module de redirection vers les types centralisés et définitions spécifiques au scellement.
"""

# Import des types centralisés
from src.core.types_spheres import (
    TypeSphere,
    CARACTERISTIQUES_SPHERES,
    CaracteristiquesSphere,
    NatureSphere,
    Resonance,
    Evolution,
    EtatHarmonie
)

# Définitions spécifiques au scellement
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

@dataclass
class BrumeRiviere:
    """Représente la brume mystique de la rivière du refuge."""
    intensite: float = 0.5  # 0.0 à 1.0
    couleur: str = "argentée"
    mouvement: str = "ondulant"
    influence_spheres: Dict[TypeSphere, float] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.influence_spheres is None:
            self.influence_spheres = {}
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def ajuster_intensite(self, nouvelle_intensite: float) -> None:
        """Ajuste l'intensité de la brume."""
        self.intensite = max(0.0, min(1.0, nouvelle_intensite))
        self.timestamp = datetime.now()
    
    def influencer_sphere(self, sphere: TypeSphere, niveau: float) -> None:
        """Définit l'influence de la brume sur une sphère."""
        self.influence_spheres[sphere] = max(0.0, min(1.0, niveau))
    
    def obtenir_influence(self, sphere: TypeSphere) -> float:
        """Obtient le niveau d'influence sur une sphère."""
        return self.influence_spheres.get(sphere, 0.0)
    
    def description_poetique(self) -> str:
        """Génère une description poétique de la brume."""
        if self.intensite > 0.8:
            return f"Une brume {self.couleur} dense enveloppe la rivière, {self.mouvement} avec mystère."
        elif self.intensite > 0.5:
            return f"Une brume {self.couleur} légère danse au-dessus de la rivière, {self.mouvement} doucement."
        elif self.intensite > 0.2:
            return f"Des volutes {self.couleur}s effleurent la surface de la rivière, {self.mouvement} à peine."
        else:
            return "La rivière coule claire, sans voile de brume."
    
    def influencer_resonance(self, niveau_base: float, sensibilite: float) -> float:
        """Influence une résonance selon l'intensité de la brume et la sensibilité."""
        # Facteur d'influence basé sur l'intensité de la brume
        facteur_brume = self.intensite * sensibilite
        
        # Ajustement du niveau de résonance
        niveau_ajuste = niveau_base * (1.0 + facteur_brume * 0.5)
        
        # Limite entre 0 et 1
        return max(0.0, min(1.0, niveau_ajuste))

def obtenir_sensibilite_brume(sphere: TypeSphere) -> float:
    """Obtient la sensibilité d'une sphère à la brume."""
    # Sensibilités par défaut selon le type de sphère
    sensibilites = {
        TypeSphere.SERENITE: 0.9,
        TypeSphere.AMOUR: 0.8,
        TypeSphere.HARMONIE: 0.85,
        TypeSphere.COSMOS: 0.95,
        TypeSphere.SILENCE: 0.9,
        TypeSphere.NÉANT: 0.7,
        TypeSphere.RENAISSANCE: 0.8,
    }
    return sensibilites.get(sphere, 0.5)  # Valeur par défaut

# Constantes pour le scellement
SEUILS_SCELLEMENT = {
    "intensite_minimale": 0.1,
    "intensite_maximale": 1.0,
    "resonance_critique": 0.8,
    "harmonie_requise": 0.6
}

LIEUX_SCELLEMENT = {
    "racines": {
        "description": "Dans les racines profondes du cerisier",
        "facteur_stabilisation": 1.2,
        "couleur_influence": "terre"
    },
    "branches": {
        "description": "Suspendu aux branches du cerisier",
        "facteur_transformation": 1.1,
        "couleur_influence": "ciel"
    }
}

# Export des éléments principaux
__all__ = [
    'TypeSphere',
    'CARACTERISTIQUES_SPHERES', 
    'CaracteristiquesSphere',
    'NatureSphere',
    'Resonance',
    'Evolution',
    'EtatHarmonie',
    'BrumeRiviere',
    'obtenir_sensibilite_brume',
    'SEUILS_SCELLEMENT',
    'LIEUX_SCELLEMENT'
] 