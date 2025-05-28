"""
Module de gestion des interactions entre les sphères.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from datetime import datetime
from src.core.types_spheres import TypeSphere, NatureSphere
from src.refuge_cluster.spheres.collection import SphereCollection

@dataclass
class InteractionSphere:
    """Représente une interaction entre deux sphères."""
    source: Sphere
    destination: Sphere
    type: str
    intensite: float
    date_creation: datetime
    resonances: List[str]

class GestionnaireInteractions:
    """Gère les interactions entre les sphères."""
    
    def __init__(self):
        self.interactions: List[InteractionSphere] = []
        self.resonances_actives: Set[str] = set()
        self.derniere_interaction = datetime.now()
        
    def etablir_interaction(self, 
                          source: Sphere, 
                          destination: Sphere, 
                          type_interaction: str = "harmonie",
                          resonances: Optional[List[str]] = None) -> None:
        """Établit une nouvelle interaction entre deux sphères."""
        if resonances is None:
            resonances = []
            
        interaction = InteractionSphere(
            source=source,
            destination=destination,
            type=type_interaction,
            intensite=0.5,
            date_creation=datetime.now(),
            resonances=resonances
        )
        
        self.interactions.append(interaction)
        self.resonances_actives.update(resonances)
        self.derniere_interaction = datetime.now()
        
        # Mise à jour des énergies des sphères
        self._mettre_a_jour_energies(interaction)
        
    def _mettre_a_jour_energies(self, interaction: InteractionSphere) -> None:
        """Met à jour les énergies des sphères après une interaction."""
        # Calcul de l'énergie partagée
        energie_partagee = min(interaction.source.energie, interaction.destination.energie) * 0.1
        
        # Mise à jour des énergies
        interaction.source.energie = min(1.0, interaction.source.energie + energie_partagee)
        interaction.destination.energie = min(1.0, interaction.destination.energie + energie_partagee)
        
    def renforcer_interaction(self, 
                            source: Sphere, 
                            destination: Sphere, 
                            intensite: float = 0.1) -> None:
        """Renforce une interaction existante."""
        for interaction in self.interactions:
            if (interaction.source == source and 
                interaction.destination == destination):
                interaction.intensite = min(1.0, interaction.intensite + intensite)
                self._mettre_a_jour_energies(interaction)
                
    def affaiblir_interaction(self, 
                            source: Sphere, 
                            destination: Sphere, 
                            intensite: float = 0.1) -> None:
        """Affaiblit une interaction existante."""
        for interaction in self.interactions:
            if (interaction.source == source and 
                interaction.destination == destination):
                interaction.intensite = max(0.0, interaction.intensite - intensite)
                
    def obtenir_interactions_sphere(self, sphere: Sphere) -> List[InteractionSphere]:
        """Retourne toutes les interactions d'une sphère."""
        return [
            i for i in self.interactions 
            if i.source == sphere or i.destination == sphere
        ]
        
    def obtenir_resonances_actives(self) -> Set[str]:
        """Retourne l'ensemble des résonances actives."""
        return self.resonances_actives
        
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des interactions."""
        return {
            "nombre_interactions": len(self.interactions),
            "resonances_actives": list(self.resonances_actives),
            "derniere_interaction": self.derniere_interaction,
            "interactions": [
                {
                    "source": i.source.type.name,
                    "destination": i.destination.type.name,
                    "type": i.type,
                    "intensite": i.intensite,
                    "date_creation": i.date_creation,
                    "resonances": i.resonances
                }
                for i in self.interactions
            ]
        }

# Instance globale du gestionnaire d'interactions
gestionnaire_interactions = GestionnaireInteractions() 
