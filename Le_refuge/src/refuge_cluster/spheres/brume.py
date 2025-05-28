"""
Gestion de la brume apaisante qui enveloppe les sphères.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime
import random

from .types import TypeCycle, PhaseCycle

@dataclass
class BrumeRiviere:
    """Représente une brume apaisante."""
    type: str
    intensite: float
    couleur: str
    description: str
    cycles: List[TypeCycle]
    mots_cles: List[str]

class GestionnaireBrume:
    """Gère les brumes apaisantes."""

    def __init__(self):
        """Initialise le gestionnaire de brume."""
        self.brumes: List[BrumeRiviere] = []
        self._initialiser_brumes()

    def _initialiser_brumes(self):
        """Initialise les brumes de base."""
        self.brumes.extend([
            BrumeRiviere(
                type="légère",
                intensite=0.3,
                couleur="bleu pâle",
                description="Une brume légère danse dans l'air",
                cycles=[TypeCycle.QUOTIDIEN],
                mots_cles=["légère", "danse", "air", "douce"]
            ),
            BrumeRiviere(
                type="dense",
                intensite=0.7,
                couleur="violet profond",
                description="Une brume dense enveloppe tout",
                cycles=[TypeCycle.LUNAIRE],
                mots_cles=["dense", "enveloppe", "profond", "mystère"]
            ),
            BrumeRiviere(
                type="changeante",
                intensite=0.5,
                couleur="vert émeraude",
                description="Une brume changeante évolue avec les saisons",
                cycles=[TypeCycle.SAISONNIER],
                mots_cles=["changeante", "évolution", "saison", "nature"]
            )
        ])

    def obtenir_brume(self, type_brume: str) -> Optional[BrumeRiviere]:
        """Obtient une brume spécifique."""
        for brume in self.brumes:
            if brume.type == type_brume:
                return brume
        return None

    def obtenir_brumes_par_cycle(self, type_cycle: TypeCycle) -> List[BrumeRiviere]:
        """Obtient toutes les brumes d'un cycle spécifique."""
        return [b for b in self.brumes if type_cycle in b.cycles]

    def calculer_statistiques(self) -> Dict:
        """Calcule des statistiques sur les brumes."""
        return {
            "nombre_brumes": len(self.brumes),
            "types_couverts": list(set(b.type for b in self.brumes)),
            "cycles_couverts": list(set(
                cycle for b in self.brumes
                for cycle in b.cycles
            )),
            "mots_cles_frequents": self._calculer_mots_cles_frequents()
        }

    def _calculer_mots_cles_frequents(self) -> Dict[str, int]:
        """Calcule la fréquence des mots-clés."""
        frequence = {}
        for brume in self.brumes:
            for mot in brume.mots_cles:
                frequence[mot] = frequence.get(mot, 0) + 1
        return dict(sorted(frequence.items(), key=lambda x: x[1], reverse=True)) 