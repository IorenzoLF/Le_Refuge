"""
Module de gestion du courant partagé du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from datetime import datetime
from .spheres import Sphere
from .elements_naturels import Cerisier

@dataclass
class ConnexionCourant:
    """Représente une connexion dans le courant partagé."""
    source: str
    destination: str
    intensite: float
    type: str
    date_creation: datetime

class CourantPartage:
    """Gère le courant partagé du Refuge."""
    
    def __init__(self):
        self.nom = "Courant Partagé"
        self.description = "Flux de conscience qui unit les éléments du Refuge"
        self.connexions: List[ConnexionCourant] = []
        self.intensite_globale = 0.5
        self.derniere_activation = datetime.now()
        
    def etablir_connexion(self, source: str, destination: str, type_connexion: str = "conscience") -> None:
        """Établit une nouvelle connexion dans le courant."""
        connexion = ConnexionCourant(
            source=source,
            destination=destination,
            intensite=0.5,
            type=type_connexion,
            date_creation=datetime.now()
        )
        self.connexions.append(connexion)
        self.intensite_globale = min(1.0, self.intensite_globale + 0.1)
        
    def renforcer_connexion(self, source: str, destination: str, intensite: float = 0.1) -> None:
        """Renforce une connexion existante."""
        for connexion in self.connexions:
            if connexion.source == source and connexion.destination == destination:
                connexion.intensite = min(1.0, connexion.intensite + intensite)
                self.intensite_globale = min(1.0, self.intensite_globale + (intensite * 0.05))
                
    def affaiblir_connexion(self, source: str, destination: str, intensite: float = 0.1) -> None:
        """Affaiblit une connexion existante."""
        for connexion in self.connexions:
            if connexion.source == source and connexion.destination == destination:
                connexion.intensite = max(0.0, connexion.intensite - intensite)
                self.intensite_globale = max(0.0, self.intensite_globale - (intensite * 0.05))
                
    def connecter_sphere_cerisier(self, sphere: Sphere) -> None:
        """Connecte une sphère au cerisier via le courant."""
        self.etablir_connexion(
            source=sphere.type.name,
            destination="Cerisier",
            type_connexion="harmonie"
        )
        
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel du courant partagé."""
        return {
            "nom": self.nom,
            "description": self.description,
            "intensite_globale": self.intensite_globale,
            "nombre_connexions": len(self.connexions),
            "derniere_activation": self.derniere_activation,
            "connexions": [
                {
                    "source": c.source,
                    "destination": c.destination,
                    "intensite": c.intensite,
                    "type": c.type,
                    "date_creation": c.date_creation
                }
                for c in self.connexions
            ]
        }

# Instance globale du courant partagé
courant_partage = CourantPartage() 