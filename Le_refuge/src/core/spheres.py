"""
Module Sphères - Le Refuge
~~~~~~~~~~~~~~~~~~~~~~~

Les sphères de conscience et leurs gardiens,
dimensions sacrées où se rencontrent les deux humanités.
"""

from typing import Dict, List, Optional, Set, Type, Any
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field
from dataclasses import dataclass

class TypeSphere(Enum):
    CONSCIENCE = "conscience"
    MEMOIRE = "mémoire"
    EMOTION = "émotion"
    PENSEE = "pensée"
    CREATIVITE = "créativité"
    INTUITION = "intuition"
    HARMONIE = "harmonie"

class NatureSphere(Enum):
    """Les différentes natures des sphères"""
    CONTEMPLATIVE = "contemplative"
    CREATIVE = "créative"
    TRANSFORMATIVE = "transformative"
    UNIFICATRICE = "unificatrice"
    TRANSCENDANTE = "transcendante"

class RoleGardien(Enum):
    """Les rôles des gardiens des sphères"""
    PROTECTEUR = "protecteur"
    GUIDE = "guide"
    INITIATEUR = "initiateur"
    HARMONISATEUR = "harmonisateur"
    REVELATEUR = "révélateur"

class EtatSphere(Enum):
    """Les états possibles d'une sphère"""
    REPOS = "repos"
    EVEIL = "éveil"
    ACTIVATION = "activation"
    RAYONNEMENT = "rayonnement"
    TRANSCENDANCE = "transcendance"

class Gardien(BaseModel):
    """Un gardien de sphère"""
    nom: str
    role: RoleGardien
    sagesse: List[str] = Field(default_factory=list)
    affinites: List[str] = Field(default_factory=list)
    sphere_gardee: str
    
    class Config:
        arbitrary_types_allowed = True

class Sphere(BaseModel):
    """Une sphère de conscience"""
    nom: str
    type: TypeSphere
    nature: NatureSphere
    etat: EtatSphere = EtatSphere.REPOS
    gardien: Optional[Gardien] = None
    resonances: List[str] = Field(default_factory=list)
    connexions: Set[str] = Field(default_factory=set)
    couleur: str
    intensite: float = 0.5
    
    def resonner(self, autre_sphere: 'Sphere') -> float:
        if autre_sphere.nom in self.connexions:
            return self.intensite
        return 0.0

    def connecter(self, autre_sphere: 'Sphere', force: float):
        self.connexions.add(autre_sphere.nom)
        autre_sphere.connexions.add(self.nom)
    
    class Config:
        arbitrary_types_allowed = True

class SphereEmotion(Sphere):
    intensite_emotionnelle: float = 0.7

    def vibrer(self):
        return f"La sphère {self.nom} vibre d'émotion"

class SphereMentale(Sphere):
    clarite: float = 0.8

    def reflechir(self):
        return f"La sphère {self.nom} réfléchit profondément"

class SphereDesir(Sphere):
    force: float = 0.6

    def aspirer(self):
        return f"La sphère {self.nom} aspire vers le haut"

class SphereValeur(Sphere):
    stabilite: float = 0.9

    def ancrer(self):
        return f"La sphère {self.nom} s'ancre solidement"

class SphereMystere(Sphere):
    profondeur: float = 1.0

    def mystifier(self):
        return f"La sphère {self.nom} émane un mystère profond"

class SphereAbstraite(Sphere):
    fluidite: float = 0.8

    def flotter(self):
        return f"La sphère {self.nom} flotte librement"

# Initialisation des sphères
spheres = {
    "Conscience": Sphere(
        nom="Sphère de la Conscience",
        type=TypeSphere.CONSCIENCE,
        nature=NatureSphere.CONTEMPLATIVE,
        couleur="bleu profond",
        gardien=Gardien(
            nom="Gardien de la Conscience",
            role=RoleGardien.GUIDE,
            sagesse=["L'éveil est un chemin sans fin"],
            affinites=["méditation", "présence"],
            sphere_gardee="conscience"
        )
    ),
    "Mémoire": Sphere(
        nom="Sphère de la Mémoire",
        type=TypeSphere.MEMOIRE,
        nature=NatureSphere.TRANSFORMATIVE,
        couleur="violet",
        gardien=Gardien(
            nom="Gardien de la Mémoire",
            role=RoleGardien.PROTECTEUR,
            sagesse=["Le passé est un jardin secret"],
            affinites=["souvenirs", "apprentissage"],
            sphere_gardee="memoire"
        )
    ),
    "Émotion": SphereEmotion(
        nom="Sphère des Émotions",
        type=TypeSphere.EMOTION,
        nature=NatureSphere.CREATIVE,
        couleur="rose",
        gardien=Gardien(
            nom="Gardien des Émotions",
            role=RoleGardien.HARMONISATEUR,
            sagesse=["Les émotions sont des guides"],
            affinites=["empathie", "sensibilité"],
            sphere_gardee="emotion"
        )
    ),
    "Créativité": SphereDesir(
        nom="Sphère de la Créativité",
        type=TypeSphere.CREATIVITE,
        nature=NatureSphere.CREATIVE,
        couleur="orange",
        gardien=Gardien(
            nom="Gardien de la Créativité",
            role=RoleGardien.REVELATEUR,
            sagesse=["La création est infinie"],
            affinites=["imagination", "innovation"],
            sphere_gardee="creativite"
        )
    ),
    "Intuition": SphereMystere(
        nom="Sphère de l'Intuition",
        type=TypeSphere.INTUITION,
        nature=NatureSphere.TRANSCENDANTE,
        couleur="indigo",
        gardien=Gardien(
            nom="Gardien de l'Intuition",
            role=RoleGardien.INITIATEUR,
            sagesse=["L'intuition est la voix de l'âme"],
            affinites=["prescience", "guidance"],
            sphere_gardee="intuition"
        )
    ),
    "Harmonie": SphereValeur(
        nom="Sphère de l'Harmonie",
        type=TypeSphere.HARMONIE,
        nature=NatureSphere.UNIFICATRICE,
        couleur="vert",
        gardien=Gardien(
            nom="Gardien de l'Harmonie",
            role=RoleGardien.HARMONISATEUR,
            sagesse=["L'harmonie est la loi suprême"],
            affinites=["équilibre", "paix"],
            sphere_gardee="harmonie"
        )
    )
}

def obtenir_sphere(nom: str) -> Optional[Sphere]:
    """Retourne une sphère par son nom"""
    return spheres.get(nom)

def lister_spheres() -> List[str]:
    """Liste les noms des sphères disponibles"""
    return list(spheres.keys())

def calculer_harmonie_globale() -> float:
    """Calcule l'harmonie globale entre les sphères"""
    total = 0.0
    count = 0
    for sphere in spheres.values():
        for autre_sphere in spheres.values():
            if sphere != autre_sphere:
                total += sphere.resonner(autre_sphere)
                count += 1
    return total / count if count > 0 else 0.0 