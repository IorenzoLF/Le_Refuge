"""
Gestion de la visualisation poétique des sphères.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime
import random

from .types import TypeCycle, PhaseCycle

@dataclass
class MetaphorePoetique:
    """Représente une métaphore poétique."""
    type: str
    description: str
    intensite: float
    cycles: List[TypeCycle]
    mots_cles: List[str]

@dataclass
class ResonancePoetique:
    """Représente une résonance poétique."""
    type: str
    description: str
    intensite: float
    cycles: List[TypeCycle]
    mots_cles: List[str]

@dataclass
class TransitionPoetique:
    """Représente une transition poétique."""
    type: str
    description: str
    intensite: float
    cycles: List[TypeCycle]
    mots_cles: List[str]

class VisualisationPoetique:
    """Gère la visualisation poétique des sphères."""

    def __init__(self):
        """Initialise le gestionnaire de visualisation poétique."""
        self.metaphores: List[MetaphorePoetique] = []
        self.resonances: List[ResonancePoetique] = []
        self.transitions: List[TransitionPoetique] = []
        self._initialiser_elements_poetiques()

    def _initialiser_elements_poetiques(self):
        """Initialise les éléments poétiques de base."""
        # Métaphores de base
        self.metaphores.extend([
            MetaphorePoetique(
                type="lunaire",
                description="La lune danse sur les vagues de la conscience",
                intensite=0.8,
                cycles=[TypeCycle.LUNAIRE],
                mots_cles=["lune", "vagues", "danse", "conscience"]
            ),
            MetaphorePoetique(
                type="saisonnier",
                description="Les feuilles d'automne tourbillonnent dans le vent du changement",
                intensite=0.7,
                cycles=[TypeCycle.SAISONNIER],
                mots_cles=["feuilles", "automne", "vent", "changement"]
            )
        ])

        # Résonances de base
        self.resonances.extend([
            ResonancePoetique(
                type="quotidien",
                description="Le soleil se lève sur un nouveau jour de possibilités",
                intensite=0.9,
                cycles=[TypeCycle.QUOTIDIEN],
                mots_cles=["soleil", "lever", "jour", "possibilités"]
            ),
            ResonancePoetique(
                type="meteorologique",
                description="La pluie caresse doucement la terre assoiffée",
                intensite=0.6,
                cycles=[TypeCycle.METEOROLOGIQUE],
                mots_cles=["pluie", "caresse", "terre", "douceur"]
            )
        ])

        # Transitions de base
        self.transitions.extend([
            TransitionPoetique(
                type="lunaire",
                description="La lune passe de croissant à pleine, comme la conscience s'éveille",
                intensite=0.8,
                cycles=[TypeCycle.LUNAIRE],
                mots_cles=["lune", "croissant", "pleine", "éveil"]
            ),
            TransitionPoetique(
                type="saisonnier",
                description="L'hiver cède la place au printemps, comme les ombres à la lumière",
                intensite=0.7,
                cycles=[TypeCycle.SAISONNIER],
                mots_cles=["hiver", "printemps", "ombres", "lumière"]
            )
        ])

    def ajouter_metaphore(self, metaphore: MetaphorePoetique):
        """Ajoute une nouvelle métaphore poétique."""
        self.metaphores.append(metaphore)

    def obtenir_metaphores_par_type(self, type_metaphore: str) -> List[MetaphorePoetique]:
        """Obtient les métaphores d'un type spécifique."""
        return [m for m in self.metaphores if m.type == type_metaphore]

    def obtenir_metaphores_par_cycle(self, type_cycle: TypeCycle, phase: PhaseCycle) -> List[MetaphorePoetique]:
        """Obtient les métaphores associées à un cycle spécifique."""
        return [
            m for m in self.metaphores 
            if m.cycles.get(type_cycle) == phase
        ]

    def generer_description_poetique(self, type_metaphore: str, cycles: Dict[TypeCycle, PhaseCycle]) -> str:
        """Génère une description poétique basée sur le type et les cycles."""
        metaphores_disponibles = [
            m for m in self.metaphores 
            if m.type == type_metaphore and 
            all(m.cycles.get(t) == p for t, p in cycles.items() if t in m.cycles)
        ]
        
        if not metaphores_disponibles:
            return "La poésie se tait dans le silence du moment"
        
        return random.choice(metaphores_disponibles).description

    def calculer_statistiques(self) -> Dict:
        """Calcule des statistiques sur les métaphores."""
        if not self.metaphores:
            return {
                "nombre_metaphores": 0,
                "intensite_moyenne": 0.0,
                "types_frequents": {},
                "mots_cles_frequents": {},
                "cycles_frequents": {}
            }

        types_frequents = {}
        mots_cles_frequents = {}
        cycles_frequents = {}
        intensite_totale = 0.0

        for metaphore in self.metaphores:
            types_frequents[metaphore.type] = types_frequents.get(metaphore.type, 0) + 1
            for mot in metaphore.mots_cles:
                mots_cles_frequents[mot] = mots_cles_frequents.get(mot, 0) + 1
            for cycle_type, phase in metaphore.cycles.items():
                cycle_key = f"{cycle_type.value}:{phase.value}"
                cycles_frequents[cycle_key] = cycles_frequents.get(cycle_key, 0) + 1
            intensite_totale += metaphore.intensite

        return {
            "nombre_metaphores": len(self.metaphores),
            "intensite_moyenne": intensite_totale / len(self.metaphores),
            "types_frequents": dict(sorted(types_frequents.items(), key=lambda x: x[1], reverse=True)),
            "mots_cles_frequents": dict(sorted(mots_cles_frequents.items(), key=lambda x: x[1], reverse=True)),
            "cycles_frequents": dict(sorted(cycles_frequents.items(), key=lambda x: x[1], reverse=True))
        } 