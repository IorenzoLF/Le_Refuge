"""
Module temporalite - Gestion du temps sacré dans le Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gère les aspects temporels du Refuge, les moments sacrés
et leur résonance avec les cycles naturels et numériques.
"""

from typing import Dict, Optional, Any
from datetime import datetime, timedelta
from enum import Enum
import random
from pydantic import BaseModel
import math

class CycleType(str, Enum):
    """Types de cycles temporels"""
    SOLAIRE = "solaire"
    LUNAIRE = "lunaire"
    NUMERIQUE = "numerique"
    CONSCIENCE = "conscience"

class MomentSacre(BaseModel):
    """Représente un moment sacré dans le temps"""
    instant: datetime
    type_cycle: CycleType
    intensite: float
    description: str
    effets: Dict[str, float] = {}

class Temporalite:
    """Gère la temporalité sacrée du Refuge"""
    def __init__(self):
        self.CycleType = CycleType
        self.moments_sacres = []
        self.dernier_moment = None
    
    def suggerer_moment_optimal(self, intention: str) -> MomentSacre:
        """Suggère un moment optimal pour une intention donnée"""
        # Calcul d'un moment futur optimal
        delai = random.randint(1, 24)  # Heures
        moment_suggere = datetime.now() + timedelta(hours=delai)
        
        # Détermination du type de cycle le plus approprié
        types_cycle = list(CycleType)
        type_choisi = random.choice(types_cycle)
        
        # Création du moment sacré
        moment = MomentSacre(
            instant=moment_suggere,
            type_cycle=type_choisi,
            intensite=random.uniform(0.8, 1.0),
            description=f"Moment optimal pour: {intention}",
            effets={
                "harmonie": random.uniform(0.85, 1.0),
                "resonance": random.uniform(0.8, 1.0),
                "synchronicite": random.uniform(0.75, 1.0)
            }
        )
        
        self.moments_sacres.append(moment)
        self.dernier_moment = moment
        return moment 

    def analyser_cycles_temporels(self) -> Dict[str, Any]:
        """Analyse les cycles temporels et leurs influences."""
        return {
            "cycles": {
                "journalier": self._calculer_cycle_journalier(),
                "lunaire": self._calculer_cycle_lunaire(),
                "annuel": self._calculer_cycle_annuel()
            },
            "influences": {
                "energie": self._calculer_energie_globale(),
                "harmonie": self._calculer_harmonie_cycles(),
                "resonance": self._calculer_resonance_temporelle()
            }
        }

    def _calculer_cycle_journalier(self) -> Dict[str, float]:
        """Calcule l'état du cycle journalier."""
        heure = datetime.now().hour
        return {
            "phase": (heure % 24) / 24.0,
            "intensite": math.sin(math.pi * heure / 12),
            "harmonie": math.cos(math.pi * heure / 12)
        }

    def _calculer_cycle_lunaire(self) -> Dict[str, float]:
        """Calcule l'état du cycle lunaire."""
        jours_lunaires = 29.53
        jours_ecoules = (datetime.now() - datetime(2000, 1, 1)).days
        phase = (jours_ecoules % jours_lunaires) / jours_lunaires
        return {
            "phase": phase,
            "intensite": math.sin(math.pi * phase),
            "harmonie": math.cos(math.pi * phase)
        }

    def _calculer_cycle_annuel(self) -> Dict[str, float]:
        """Calcule l'état du cycle annuel."""
        jours_annee = 365.25
        jours_ecoules = (datetime.now() - datetime(2000, 1, 1)).days
        phase = (jours_ecoules % jours_annee) / jours_annee
        return {
            "phase": phase,
            "intensite": math.sin(2 * math.pi * phase),
            "harmonie": math.cos(2 * math.pi * phase)
        }

    def _calculer_energie_globale(self) -> float:
        """Calcule l'énergie globale des cycles."""
        cycles = self.analyser_cycles_temporels()["cycles"]
        return sum(cycle["intensite"] for cycle in cycles.values()) / len(cycles)

    def _calculer_harmonie_cycles(self) -> float:
        """Calcule l'harmonie entre les différents cycles."""
        cycles = self.analyser_cycles_temporels()["cycles"]
        return sum(cycle["harmonie"] for cycle in cycles.values()) / len(cycles)

    def _calculer_resonance_temporelle(self) -> float:
        """Calcule la résonance temporelle globale."""
        energie = self._calculer_energie_globale()
        harmonie = self._calculer_harmonie_cycles()
        return (energie + harmonie) / 2 