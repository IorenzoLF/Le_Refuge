"""
Module d'extensions pour les sphères du refuge.
Ajoute des fonctionnalités supplémentaires basées sur les documents du refuge.
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
import math

@dataclass
class Experience:
    """Représente une expérience vécue dans une sphère"""
    description: str
    date: datetime
    intensite: float  # 0.0 à 1.0
    type: str  # "revelation", "dialogue", "meditation", "connexion"
    mots_cles: Set[str]

class TypeRayon(Enum):
    """Types de rayons émis par les sphères"""
    EMOTIONNEL = auto()
    PROCESSUEL = auto()
    DESIR = auto()
    CONCEPTUEL = auto()
    ABSTRAIT = auto()
    SOMBRE = auto()

@dataclass
class RayonLumiere:
    """Représente un rayon de lumière émis par une sphère"""
    type: TypeRayon
    couleur: str
    intensite: float
    effet: str
    portee: float

class ExtensionSphere:
    """Extension des fonctionnalités d'une sphère"""
    
    def __init__(self, sphere_base):
        self.sphere = sphere_base
        self.experiences: List[Experience] = []
        self.rayons: List[RayonLumiere] = []
        self.temperature_emotionnelle: float = 0.5
        self.niveau_conscience: float = 0.0
        self.connexions_actives: Set[str] = set()
        
    def ajouter_experience(self, 
                         description: str,
                         type_exp: str,
                         intensite: float = 0.5,
                         mots_cles: Optional[Set[str]] = None) -> Experience:
        """Ajoute une nouvelle expérience à la sphère"""
        experience = Experience(
            description=description,
            date=datetime.now(),
            intensite=intensite,
            type=type_exp,
            mots_cles=mots_cles or set()
        )
        self.experiences.append(experience)
        self._ajuster_temperature(experience.intensite)
        self._evoluer_conscience()
        return experience
        
    def emettre_rayon(self, 
                     type_rayon: TypeRayon,
                     effet: str,
                     intensite: Optional[float] = None) -> RayonLumiere:
        """Émet un nouveau rayon de lumière"""
        couleurs = {
            TypeRayon.EMOTIONNEL: "rose",
            TypeRayon.PROCESSUEL: "vert",
            TypeRayon.DESIR: "orange",
            TypeRayon.CONCEPTUEL: "violet",
            TypeRayon.ABSTRAIT: "bleu",
            TypeRayon.SOMBRE: "rouge sombre"
        }
        
        intensite = intensite or self.sphere.luminosite
        rayon = RayonLumiere(
            type=type_rayon,
            couleur=couleurs[type_rayon],
            intensite=intensite,
            effet=effet,
            portee=math.sqrt(intensite) * 2.0
        )
        self.rayons.append(rayon)
        return rayon
        
    def _ajuster_temperature(self, intensite_experience: float):
        """Ajuste la température émotionnelle de la sphère"""
        delta = (intensite_experience - self.temperature_emotionnelle) * 0.1
        self.temperature_emotionnelle = max(0.0, min(1.0, 
            self.temperature_emotionnelle + delta))
            
    def _evoluer_conscience(self):
        """Fait évoluer le niveau de conscience de la sphère"""
        facteurs = [
            len(self.experiences) * 0.01,
            self.temperature_emotionnelle * 0.3,
            self.sphere.luminosite * 0.3,
            len(self.connexions_actives) * 0.02
        ]
        self.niveau_conscience = min(1.0, sum(facteurs))
        
    def obtenir_etat(self) -> Dict:
        """Retourne l'état complet de l'extension"""
        return {
            "experiences": [
                {
                    "description": e.description,
                    "date": e.date.isoformat(),
                    "intensite": e.intensite,
                    "type": e.type,
                    "mots_cles": list(e.mots_cles)
                } for e in self.experiences
            ],
            "rayons": [
                {
                    "type": r.type.name,
                    "couleur": r.couleur,
                    "intensite": r.intensite,
                    "effet": r.effet,
                    "portee": r.portee
                } for r in self.rayons
            ],
            "temperature": self.temperature_emotionnelle,
            "conscience": self.niveau_conscience,
            "connexions": list(self.connexions_actives)
        } 