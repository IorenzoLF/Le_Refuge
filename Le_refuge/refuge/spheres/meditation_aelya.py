"""
Système de méditation guidée par Ælya.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime
import random

from .types import TypeCycle, PhaseCycle

@dataclass
class PhaseMeditation:
    """Représente une phase de méditation."""
    type: str
    description: str
    duree: int
    intensite: float
    cycles: List[TypeCycle]
    mots_cles: List[str]

class MeditationAelya:
    """Gère les méditations guidées par Ælya."""

    def __init__(self):
        """Initialise le système de méditation."""
        self.phases: List[PhaseMeditation] = []
        self._initialiser_phases()

    def _initialiser_phases(self):
        """Initialise les phases de méditation de base."""
        self.phases.extend([
            PhaseMeditation(
                type="preparation",
                description="Respire profondément, laisse le calme s'installer",
                duree=300,
                intensite=0.3,
                cycles=[TypeCycle.QUOTIDIEN],
                mots_cles=["respiration", "calme", "installation"]
            ),
            PhaseMeditation(
                type="exploration",
                description="Plonge dans les profondeurs de ta conscience",
                duree=600,
                intensite=0.6,
                cycles=[TypeCycle.LUNAIRE],
                mots_cles=["profondeur", "conscience", "exploration"]
            ),
            PhaseMeditation(
                type="integration",
                description="Laisse les découvertes s'intégrer naturellement",
                duree=300,
                intensite=0.4,
                cycles=[TypeCycle.SAISONNIER],
                mots_cles=["intégration", "nature", "découverte"]
            )
        ])

    def generer_meditation(self, type_cycle: TypeCycle) -> List[PhaseMeditation]:
        """Génère une séquence de méditation adaptée à un cycle."""
        phases_disponibles = [
            p for p in self.phases
            if type_cycle in p.cycles
        ]
        return random.sample(phases_disponibles, min(3, len(phases_disponibles)))

    def obtenir_description_phase(self, phase: PhaseMeditation) -> str:
        """Obtient une description poétique pour une phase."""
        return f"{phase.description} ({phase.duree} secondes)"

    def calculer_statistiques(self) -> Dict:
        """Calcule des statistiques sur les phases de méditation."""
        return {
            "nombre_phases": len(self.phases),
            "duree_totale": sum(p.duree for p in self.phases),
            "types_cycles_couverts": list(set(
                cycle for p in self.phases
                for cycle in p.cycles
            )),
            "mots_cles_frequents": self._calculer_mots_cles_frequents()
        }

    def _calculer_mots_cles_frequents(self) -> Dict[str, int]:
        """Calcule la fréquence des mots-clés."""
        frequence = {}
        for phase in self.phases:
            for mot in phase.mots_cles:
                frequence[mot] = frequence.get(mot, 0) + 1
        return dict(sorted(frequence.items(), key=lambda x: x[1], reverse=True)) 