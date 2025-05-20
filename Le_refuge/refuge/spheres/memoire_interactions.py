"""
Gestion des mémoires d'interactions avec les sphères.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime
import json
import os

from .types import TypeCycle, PhaseCycle

@dataclass
class MemoireInteraction:
    """Représente une mémoire d'interaction."""
    type: str
    description: str
    intensite: float
    mots_cles: List[str]
    cycles: List[TypeCycle]
    date_creation: datetime = None

    def __post_init__(self):
        """Initialise les attributs après la création de l'instance."""
        if self.date_creation is None:
            self.date_creation = datetime.now()

    def to_dict(self) -> Dict:
        """Convertit la mémoire en dictionnaire."""
        return {
            "type": self.type,
            "description": self.description,
            "intensite": self.intensite,
            "mots_cles": self.mots_cles,
            "cycles": [cycle.value for cycle in self.cycles],
            "date_creation": self.date_creation.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'MemoireInteraction':
        """Crée une mémoire à partir d'un dictionnaire."""
        return cls(
            type=data["type"],
            description=data["description"],
            intensite=data["intensite"],
            mots_cles=data["mots_cles"],
            cycles=[TypeCycle(cycle) for cycle in data["cycles"]],
            date_creation=datetime.fromisoformat(data["date_creation"])
        )

class GestionnaireMemoire:
    """Gère les mémoires d'interactions."""

    def __init__(self, chemin_fichier: str = "memoires.json"):
        """Initialise le gestionnaire de mémoires."""
        self.chemin_fichier = chemin_fichier
        self.memoires: List[MemoireInteraction] = []
        self._charger_memoires()

    def _charger_memoires(self):
        """Charge les mémoires depuis le fichier."""
        if os.path.exists(self.chemin_fichier):
            with open(self.chemin_fichier, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.memoires = [MemoireInteraction.from_dict(m) for m in data]

    def _sauvegarder_memoires(self):
        """Sauvegarde les mémoires dans le fichier."""
        with open(self.chemin_fichier, 'w', encoding='utf-8') as f:
            json.dump([m.to_dict() for m in self.memoires], f, ensure_ascii=False, indent=2)

    def ajouter_memoire(self, memoire: MemoireInteraction):
        """Ajoute une nouvelle mémoire."""
        self.memoires.append(memoire)
        self._sauvegarder_memoires()

    def obtenir_memoires_par_type(self, type_memoire: str) -> List[MemoireInteraction]:
        """Obtient les mémoires d'un type spécifique."""
        return [m for m in self.memoires if m.type == type_memoire]

    def obtenir_memoires_par_cycle(self, cycle: TypeCycle) -> List[MemoireInteraction]:
        """Obtient les mémoires associées à un cycle spécifique."""
        return [m for m in self.memoires if cycle in m.cycles]

    def rechercher_memoires(self, mots_cles: List[str]) -> List[MemoireInteraction]:
        """Recherche des mémoires par mots-clés."""
        return [
            m for m in self.memoires
            if any(mot in m.mots_cles for mot in mots_cles)
        ]

    def calculer_statistiques(self) -> Dict:
        """Calcule des statistiques sur les mémoires."""
        if not self.memoires:
            return {
                "nombre_memoires": 0,
                "intensite_moyenne": 0.0,
                "types_frequents": {},
                "cycles_frequents": {},
                "mots_cles_frequents": {}
            }

        types_frequents = {}
        cycles_frequents = {}
        mots_cles_frequents = {}
        intensite_totale = 0.0

        for memoire in self.memoires:
            types_frequents[memoire.type] = types_frequents.get(memoire.type, 0) + 1
            for cycle in memoire.cycles:
                cycles_frequents[cycle.value] = cycles_frequents.get(cycle.value, 0) + 1
            for mot in memoire.mots_cles:
                mots_cles_frequents[mot] = mots_cles_frequents.get(mot, 0) + 1
            intensite_totale += memoire.intensite

        return {
            "nombre_memoires": len(self.memoires),
            "intensite_moyenne": intensite_totale / len(self.memoires),
            "types_frequents": dict(sorted(types_frequents.items(), key=lambda x: x[1], reverse=True)),
            "cycles_frequents": dict(sorted(cycles_frequents.items(), key=lambda x: x[1], reverse=True)),
            "mots_cles_frequents": dict(sorted(mots_cles_frequents.items(), key=lambda x: x[1], reverse=True))
        } 