"""
Module de gestion des harmonies entre les sphères.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from datetime import datetime
from .coeur.types_spheres import TypeSphere, NatureSphere
from .spheres import Sphere
from .interactions import gestionnaire_interactions

@dataclass
class Harmonie:
    """Représente une harmonie entre plusieurs sphères."""
    nom: str
    description: str
    spheres: List[Sphere]
    intensite: float
    date_creation: datetime
    resonances: List[str]

class GestionnaireHarmonies:
    """Gère les harmonies entre les sphères."""
    
    def __init__(self, gestionnaire_interactions: gestionnaire_interactions):
        self.harmonies: List[Harmonie] = []
        self.gestionnaire_interactions = gestionnaire_interactions
        self.derniere_harmonisation = datetime.now()
        
    def creer_harmonie(self, 
                      nom: str,
                      description: str,
                      spheres: List[Sphere],
                      resonances: Optional[List[str]] = None) -> None:
        """Crée une nouvelle harmonie entre plusieurs sphères."""
        if resonances is None:
            resonances = []
            
        harmonie = Harmonie(
            nom=nom,
            description=description,
            spheres=spheres,
            intensite=0.5,
            date_creation=datetime.now(),
            resonances=resonances
        )
        
        self.harmonies.append(harmonie)
        
        # Établissement des interactions entre les sphères
        for i in range(len(spheres)):
            for j in range(i + 1, len(spheres)):
                self.gestionnaire_interactions.etablir_interaction(
                    spheres[i],
                    spheres[j],
                    "harmonie",
                    resonances
                )
                
    def renforcer_harmonie(self, nom: str, intensite: float = 0.1) -> None:
        """Renforce une harmonie existante."""
        for harmonie in self.harmonies:
            if harmonie.nom == nom:
                harmonie.intensite = min(1.0, harmonie.intensite + intensite)
                
                # Renforcement des interactions
                for i in range(len(harmonie.spheres)):
                    for j in range(i + 1, len(harmonie.spheres)):
                        self.gestionnaire_interactions.renforcer_interaction(
                            harmonie.spheres[i],
                            harmonie.spheres[j],
                            intensite
                        )
                        
    def affaiblir_harmonie(self, nom: str, intensite: float = 0.1) -> None:
        """Affaiblit une harmonie existante."""
        for harmonie in self.harmonies:
            if harmonie.nom == nom:
                harmonie.intensite = max(0.0, harmonie.intensite - intensite)
                
    def obtenir_harmonies_sphere(self, sphere: Sphere) -> List[Harmonie]:
        """Retourne toutes les harmonies d'une sphère."""
        return [
            h for h in self.harmonies 
            if sphere in h.spheres
        ]
        
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des harmonies."""
        return {
            "nombre_harmonies": len(self.harmonies),
            "derniere_harmonisation": self.derniere_harmonisation,
            "harmonies": [
                {
                    "nom": h.nom,
                    "description": h.description,
                    "spheres": [s.type.name for s in h.spheres],
                    "intensite": h.intensite,
                    "date_creation": h.date_creation,
                    "resonances": h.resonances
                }
                for h in self.harmonies
            ]
        }

# Instance globale du gestionnaire d'harmonies
gestionnaire_harmonies = GestionnaireHarmonies(gestionnaire_interactions) 