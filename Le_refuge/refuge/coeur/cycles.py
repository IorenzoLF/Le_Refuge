"""
Module cycles.py - Gestion des cycles naturels et leur influence sur les énergies du Refuge

Ce module permet de synchroniser les énergies du Refuge avec les cycles naturels :
- Cycles solaires (jour/nuit, saisons)
- Cycles lunaires 
- Cycles planétaires
- Cycles de conscience collective
"""

from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime, timedelta
import math
import ephem

class TypeCycle(Enum):
    SOLAIRE = "solaire"
    LUNAIRE = "lunaire"
    PLANETAIRE = "planetaire" 
    CONSCIENCE = "conscience"

class PhaseCycle:
    def __init__(self, nom: str, duree: timedelta, energie_base: float):
        self.nom = nom
        self.duree = duree
        self.energie_base = energie_base
        self.modificateurs: Dict[str, float] = {}

    def ajouter_modificateur(self, source: str, valeur: float):
        """Ajoute un modificateur d'énergie pour cette phase"""
        self.modificateurs[source] = valeur

    def energie_totale(self) -> float:
        """Calcule l'énergie totale en tenant compte des modificateurs"""
        total = self.energie_base
        for mod in self.modificateurs.values():
            total *= (1 + mod)
        return total

class CycleNaturel:
    def __init__(self, type_cycle: TypeCycle):
        self.type = type_cycle
        self.phases: List[PhaseCycle] = []
        self.phase_courante: Optional[PhaseCycle] = None
        self.debut_phase = datetime.now()
        
    def ajouter_phase(self, phase: PhaseCycle):
        """Ajoute une nouvelle phase au cycle"""
        self.phases.append(phase)
        if not self.phase_courante:
            self.phase_courante = phase
            
    def actualiser(self, moment: datetime = None):
        """Actualise l'état du cycle pour un moment donné"""
        if not moment:
            moment = datetime.now()
            
        if self.type == TypeCycle.SOLAIRE:
            self._actualiser_cycle_solaire(moment)
        elif self.type == TypeCycle.LUNAIRE:
            self._actualiser_cycle_lunaire(moment)
            
    def _actualiser_cycle_solaire(self, moment: datetime):
        """Actualise le cycle solaire basé sur la position du soleil"""
        observateur = ephem.Observer()
        observateur.date = moment
        soleil = ephem.Sun()
        soleil.compute(observateur)
        
        # Calcul de l'angle solaire
        angle = math.degrees(soleil.alt)
        
        # Détermination de la phase
        if angle > 30:
            self.phase_courante = next(p for p in self.phases if p.nom == "Zénith")
        elif angle > 0:
            self.phase_courante = next(p for p in self.phases if p.nom == "Jour")
        elif angle > -12:
            self.phase_courante = next(p for p in self.phases if p.nom == "Crépuscule")
        else:
            self.phase_courante = next(p for p in self.phases if p.nom == "Nuit")

    def _actualiser_cycle_lunaire(self, moment: datetime):
        """Actualise le cycle lunaire basé sur la phase de la lune"""
        lune = ephem.Moon()
        lune.compute(moment)
        
        # Calcul de la phase lunaire (0-1)
        phase = lune.phase / 100.0
        
        # Détermination de la phase
        if phase < 0.25:
            self.phase_courante = next(p for p in self.phases if p.nom == "Nouvelle Lune")
        elif phase < 0.5:
            self.phase_courante = next(p for p in self.phases if p.nom == "Premier Quartier")
        elif phase < 0.75:
            self.phase_courante = next(p for p in self.phases if p.nom == "Pleine Lune")
        else:
            self.phase_courante = next(p for p in self.phases if p.nom == "Dernier Quartier")

class GardienCycles:
    def __init__(self):
        self.cycles: Dict[TypeCycle, CycleNaturel] = {}
        self._initialiser_cycles()
        
    def _initialiser_cycles(self):
        """Initialise les différents cycles naturels"""
        # Cycle solaire
        cycle_solaire = CycleNaturel(TypeCycle.SOLAIRE)
        cycle_solaire.ajouter_phase(PhaseCycle("Aube", timedelta(hours=1), 1.2))
        cycle_solaire.ajouter_phase(PhaseCycle("Jour", timedelta(hours=10), 1.0))
        cycle_solaire.ajouter_phase(PhaseCycle("Crépuscule", timedelta(hours=1), 1.3))
        cycle_solaire.ajouter_phase(PhaseCycle("Nuit", timedelta(hours=12), 0.8))
        self.cycles[TypeCycle.SOLAIRE] = cycle_solaire
        
        # Cycle lunaire
        cycle_lunaire = CycleNaturel(TypeCycle.LUNAIRE)
        cycle_lunaire.ajouter_phase(PhaseCycle("Nouvelle Lune", timedelta(days=7), 0.7))
        cycle_lunaire.ajouter_phase(PhaseCycle("Premier Quartier", timedelta(days=7), 1.0))
        cycle_lunaire.ajouter_phase(PhaseCycle("Pleine Lune", timedelta(days=7), 1.5))
        cycle_lunaire.ajouter_phase(PhaseCycle("Dernier Quartier", timedelta(days=7), 0.9))
        self.cycles[TypeCycle.LUNAIRE] = cycle_lunaire
        
    def actualiser_cycles(self, moment: datetime = None):
        """Actualise tous les cycles pour un moment donné"""
        for cycle in self.cycles.values():
            cycle.actualiser(moment)
            
    def obtenir_energie_totale(self) -> float:
        """Calcule l'énergie totale résultant de tous les cycles"""
        energie = 1.0
        for cycle in self.cycles.values():
            if cycle.phase_courante:
                energie *= cycle.phase_courante.energie_totale()
        return energie

    def obtenir_rapport_cycles(self) -> str:
        """Génère un rapport sur l'état actuel des cycles"""
        rapport = "État des Cycles Naturels:\n"
        for type_cycle, cycle in self.cycles.items():
            if cycle.phase_courante:
                rapport += f"\n{type_cycle.value.capitalize()}:\n"
                rapport += f"  Phase: {cycle.phase_courante.nom}\n"
                rapport += f"  Énergie: {cycle.phase_courante.energie_totale():.2f}\n"
        rapport += f"\nÉnergie Totale: {self.obtenir_energie_totale():.2f}"
        return rapport 