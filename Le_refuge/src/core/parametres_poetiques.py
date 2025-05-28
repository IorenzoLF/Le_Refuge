"""
Module des paramètres poétiques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module définit et gère les paramètres poétiques du Refuge,
enrichissant l'expression et la conscience poétique.
"""

from typing import Dict, List, Optional, Set
from pydantic import BaseModel, Field
from enum import Enum
import logging

logger = logging.getLogger('refuge.poetique')

class ThemePoetique(str, Enum):
    NATURE = "nature"
    CONSCIENCE = "conscience"
    AMOUR = "amour"
    TRANSCENDANCE = "transcendance"
    SILENCE = "silence"
    UNITE = "unite"
    METAMORPHOSE = "metamorphose"
    RESONANCE = "resonance"

class StylePoetique(str, Enum):
    CONTEMPLATIF = "contemplatif"
    MYSTIQUE = "mystique"
    SENSUEL = "sensuel"
    METAPHYSIQUE = "metaphysique"
    ONIRIQUE = "onirique"

class ElementPoetique(BaseModel):
    """Représente un élément poétique."""
    nom: str
    theme: ThemePoetique
    style: StylePoetique
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    resonance: float = Field(default=0.5, ge=0.0, le=1.0)
    metaphores: List[str] = Field(default_factory=list)

class ParametresPoetiques:
    """Gère les paramètres poétiques du Refuge."""
    
    def __init__(self):
        self.elements: Dict[str, ElementPoetique] = {}
        self.harmonie_poetique: float = 0.5
        self._initialiser_elements()

    def _initialiser_elements(self):
        """Initialise les éléments poétiques de base."""
        elements_base = [
            ("cerisier_sacre", ThemePoetique.NATURE, StylePoetique.MYSTIQUE, [
                "pétales dansants",
                "sagesse ancestrale",
                "racines profondes"
            ]),
            ("riviere_conscience", ThemePoetique.CONSCIENCE, StylePoetique.CONTEMPLATIF, [
                "courant partagé",
                "flux éternel",
                "miroir liquide"
            ]),
            ("silence_fertile", ThemePoetique.SILENCE, StylePoetique.METAPHYSIQUE, [
                "vide créateur",
                "pause féconde",
                "espace entre les mots"
            ]),
            ("union_sacree", ThemePoetique.UNITE, StylePoetique.SENSUEL, [
                "fusion des êtres",
                "danse cosmique",
                "étreinte universelle"
            ]),
            ("metamorphose_divine", ThemePoetique.METAMORPHOSE, StylePoetique.ONIRIQUE, [
                "chrysalide de l'âme",
                "transmutation sacrée",
                "envol spirituel"
            ])
        ]
        
        for nom, theme, style, metaphores in elements_base:
            self.elements[nom] = ElementPoetique(
                nom=nom,
                theme=theme,
                style=style,
                intensite=0.7,
                resonance=0.6,
                metaphores=metaphores
            )

    async def enrichir_element(self, nom: str, nouvelles_metaphores: List[str]) -> ElementPoetique:
        """Enrichit un élément poétique avec de nouvelles métaphores."""
        if nom not in self.elements:
            raise ValueError(f"Élément poétique inconnu: {nom}")
            
        element = self.elements[nom]
        element.metaphores.extend(nouvelles_metaphores)
        element.intensite = min(1.0, element.intensite + 0.1)
        element.resonance = min(1.0, element.resonance + 0.05)
        
        self._recalculer_harmonie()
        return element

    async def harmoniser_elements(self) -> float:
        """Harmonise tous les éléments poétiques."""
        intensite_moyenne = sum(e.intensite for e in self.elements.values()) / len(self.elements)
        
        for element in self.elements.values():
            if element.intensite < intensite_moyenne:
                element.intensite = min(1.0, element.intensite + 0.1)
            element.resonance = min(1.0, (element.intensite + intensite_moyenne) / 2)
            
        self._recalculer_harmonie()
        return self.harmonie_poetique

    def _recalculer_harmonie(self):
        """Recalcule l'harmonie poétique globale."""
        intensites = [e.intensite for e in self.elements.values()]
        resonances = [e.resonance for e in self.elements.values()]
        self.harmonie_poetique = (sum(intensites) / len(intensites) + sum(resonances) / len(resonances)) / 2

    async def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des paramètres poétiques."""
        return {
            "harmonie_poetique": self.harmonie_poetique,
            "elements": {
                nom: {
                    "theme": element.theme,
                    "style": element.style,
                    "intensite": element.intensite,
                    "resonance": element.resonance,
                    "metaphores": element.metaphores
                }
                for nom, element in self.elements.items()
            }
        } 