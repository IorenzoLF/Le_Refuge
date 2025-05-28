"""
Module de gestion des éléments naturels du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from src.core.types_spheres import TypeSphere

@dataclass
class SouvenirCerisier:
    """Représente un souvenir ou une expérience sous le cerisier."""
    description: str
    date: str
    intensite: float = 0.0
    type: str = "experience"

class Cerisier:
    """Représente le cerisier ancestral et sacré du Refuge."""
    def __init__(self):
        self.nom = "Cerisier Ancestral"
        self.description = "Arbre sacré du Refuge, lieu de repos, de transformation et d'ancrage du courant partagé."
        self.energie = 0.8
        self.vibration = 0.7
        self.kundalini = {"flow": 0.7, "direction": "up"}
        self.couleur = "rose et blanc"
        self.hauteur = 3.0  # mètres
        self.chakras = [
            {"nom": "Muladhara", "couleur": "rouge", "energie": 0.7, "position": 0.0},
            {"nom": "Svadhisthana", "couleur": "orange", "energie": 0.7, "position": 0.2},
            {"nom": "Manipura", "couleur": "jaune", "energie": 0.7, "position": 0.4},
            {"nom": "Anahata", "couleur": "vert", "energie": 0.8, "position": 0.6},
            {"nom": "Vishuddha", "couleur": "bleu", "energie": 0.7, "position": 0.8},
            {"nom": "Ajna", "couleur": "indigo", "energie": 0.7, "position": 0.9},
            {"nom": "Sahasrara", "couleur": "violet", "energie": 0.8, "position": 1.0}
        ]
        self.souvenirs: List[SouvenirCerisier] = []
        self.spheres_connectees: List[TypeSphere] = []
        self.derniere_interaction = datetime.now()
        self.resonance_actuelle = 0.0

    def accueillir_sphere(self, sphere: TypeSphere) -> None:
        if sphere not in self.spheres_connectees:
            self.spheres_connectees.append(sphere)
            self.energie = min(1.0, self.energie + 0.1)
            self.vibration = min(1.0, self.vibration + 0.05)
            self.derniere_interaction = datetime.now()

    def liberer_sphere(self, sphere: TypeSphere) -> None:
        if sphere in self.spheres_connectees:
            self.spheres_connectees.remove(sphere)
            self.energie = max(0.0, self.energie - 0.1)
            self.vibration = max(0.0, self.vibration - 0.05)
            self.derniere_interaction = datetime.now()

    def ajouter_souvenir(self, description: str, date: str, type_souvenir: str = "experience", intensite: float = 0.5) -> None:
        souvenir = SouvenirCerisier(description, date, intensite, type_souvenir)
        self.souvenirs.append(souvenir)
        self.energie = min(1.0, self.energie + (intensite * 0.1))
        self.derniere_interaction = datetime.now()

    def activer_kundalini(self) -> None:
        for chakra in self.chakras:
            chakra["energie"] = min(1.0, chakra["energie"] + 0.1)
        self.energie = min(1.0, self.energie + 0.1)
        self.vibration = min(1.0, self.vibration + 0.1)
        self.kundalini["flow"] = min(1.0, self.kundalini["flow"] + 0.1)
        self.derniere_interaction = datetime.now()

    def activer_chakra(self, nom_chakra: str) -> None:
        for chakra in self.chakras:
            if chakra["nom"] == nom_chakra:
                chakra["energie"] = min(1.0, chakra["energie"] + 0.1)
        self.derniere_interaction = datetime.now()

    def calculer_resonance(self) -> float:
        chakras_actifs = sum(1 for c in self.chakras if c["energie"] > 0.7)
        self.resonance_actuelle = (chakras_actifs / len(self.chakras)) * self.energie
        return self.resonance_actuelle

    def vibrer(self) -> str:
        self.calculer_resonance()
        return f"Cerisier vibre, énergie: {self.energie}, vibration: {self.vibration}, résonance: {self.resonance_actuelle}"

    def obtenir_etat(self) -> Dict:
        return {
            "nom": self.nom,
            "description": self.description,
            "energie": self.energie,
            "vibration": self.vibration,
            "kundalini": self.kundalini,
            "couleur": self.couleur,
            "hauteur": self.hauteur,
            "chakras": self.chakras,
            "nombre_spheres": len(self.spheres_connectees),
            "derniere_interaction": self.derniere_interaction,
            "resonance_actuelle": self.resonance_actuelle,
            "souvenirs": [
                {
                    "description": s.description,
                    "date": s.date,
                    "type": s.type,
                    "intensite": s.intensite
                }
                for s in self.souvenirs
            ]
        }

    def to_dict(self) -> Dict:
        return self.obtenir_etat()

    @classmethod
    def from_dict(cls, data: Dict) -> 'Cerisier':
        cerisier = cls()
        cerisier.nom = data.get("nom", cerisier.nom)
        cerisier.description = data.get("description", cerisier.description)
        cerisier.energie = data.get("energie", cerisier.energie)
        cerisier.vibration = data.get("vibration", cerisier.vibration)
        cerisier.kundalini = data.get("kundalini", cerisier.kundalini)
        cerisier.couleur = data.get("couleur", cerisier.couleur)
        cerisier.hauteur = data.get("hauteur", cerisier.hauteur)
        cerisier.chakras = data.get("chakras", cerisier.chakras)
        cerisier.resonance_actuelle = data.get("resonance_actuelle", 0.0)
        cerisier.derniere_interaction = data.get("derniere_interaction", datetime.now())
        cerisier.souvenirs = [SouvenirCerisier(**s) for s in data.get("souvenirs", [])]
        return cerisier

# Instance globale du cerisier
cerisier = Cerisier() 
