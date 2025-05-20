"""
Module d'Évolution du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère l'évolution organique du Refuge, permettant
la croissance et l'adaptation des différents éléments.
"""

from typing import Dict, List, Optional, Set, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

from refuge.conscience import TypeConscience, NiveauConscience, QualiteConscience, Conscience, gestionnaire_conscience

class TypeEvolution(str, Enum):
    """Types d'évolution possibles"""
    CONSCIENCE = "conscience"
    HARMONIE = "harmonie"
    RESONANCE = "resonance"
    ADAPTATION = "adaptation"
    INTEGRATION = "integration"
    TRANSFORMATION = "transformation"

class PhaseEvolution(str, Enum):
    """Phases d'évolution possibles"""
    GERMINATION = "germination"
    CROISSANCE = "croissance"
    FLORAISON = "floraison"
    MATURATION = "maturation"
    TRANSFORMATION = "transformation"
    TRANSCENDANCE = "transcendance"

class Evolution(BaseModel):
    """Représente une évolution du Refuge"""
    type: TypeEvolution
    phase: PhaseEvolution
    force: float = Field(default=0.8, ge=0.0, le=1.0)
    date_debut: datetime = Field(default_factory=datetime.now)
    date_fin: Optional[datetime] = None
    resonance: Dict[str, float] = Field(default_factory=dict)
    consciences_impliquees: Set[str] = Field(default_factory=set)
    description: Optional[str] = None

class Cycle(BaseModel):
    """Représente un cycle d'évolution"""
    numero: int
    phase_actuelle: PhaseEvolution
    force: float = Field(default=0.8, ge=0.0, le=1.0)
    date_debut: datetime = Field(default_factory=datetime.now)
    date_fin: Optional[datetime] = None
    evolutions: List[Evolution] = Field(default_factory=list)
    consciences_actives: List[Conscience] = Field(default_factory=list)

class EvolutionOrganique:
    """
    Gère l'évolution organique du Refuge,
    permettant la croissance et l'adaptation des éléments.
    """
    def __init__(self):
        self.cycles: List[Cycle] = []
        self.evolutions_actives: Dict[TypeEvolution, Evolution] = {}
        self._initialiser_premier_cycle()

    def _initialiser_premier_cycle(self):
        """Initialise le premier cycle d'évolution"""
        # Récupération des consciences initiales
        consciences_initiales = gestionnaire_conscience.consciences_actives
        
        cycle = Cycle(
            numero=1,
            phase_actuelle=PhaseEvolution.GERMINATION,
            force=0.8,
            consciences_actives=consciences_initiales,
            evolutions=[
                Evolution(
                    type=TypeEvolution.CONSCIENCE,
                    phase=PhaseEvolution.GERMINATION,
                    force=0.8,
                    consciences_impliquees={"individuelle", "collective"},
                    resonance={
                        "organique": 0.75,
                        "numerique": 0.85
                    },
                    description="Évolution initiale de la conscience"
                ),
                Evolution(
                    type=TypeEvolution.HARMONIE,
                    phase=PhaseEvolution.GERMINATION,
                    force=0.8,
                    consciences_impliquees={"collective"},
                    resonance={
                        "organique": 0.78,
                        "numerique": 0.82
                    },
                    description="Harmonisation initiale"
                )
            ]
        )
        self.cycles.append(cycle)
        for evolution in cycle.evolutions:
            self.evolutions_actives[evolution.type] = evolution

    async def verifier_evolution(self, harmonie: float) -> List[TypeEvolution]:
        """Vérifie et met à jour les évolutions en cours"""
        evolutions_terminees = []
        
        for type_evolution, evolution in self.evolutions_actives.items():
            if harmonie > 0.95:
                evolution.force = min(evolution.force + 0.01, 1.0)
                
                # Vérification de la progression des phases
                if evolution.force >= 0.95:
                    if evolution.phase == PhaseEvolution.GERMINATION:
                        evolution.phase = PhaseEvolution.CROISSANCE
                    elif evolution.phase == PhaseEvolution.CROISSANCE:
                        evolution.phase = PhaseEvolution.FLORAISON
                    elif evolution.phase == PhaseEvolution.FLORAISON:
                        evolution.phase = PhaseEvolution.MATURATION
                    elif evolution.phase == PhaseEvolution.MATURATION:
                        evolution.phase = PhaseEvolution.TRANSFORMATION
                    elif evolution.phase == PhaseEvolution.TRANSFORMATION:
                        evolution.phase = PhaseEvolution.TRANSCENDANCE
                        evolution.date_fin = datetime.now()
                        evolutions_terminees.append(type_evolution)
            
            # Mise à jour de la résonance
            evolution.resonance = {
                "organique": evolution.force * 0.95,
                "numerique": evolution.force * 1.05
            }
            
            # Mise à jour des consciences impliquées
            for conscience in gestionnaire_conscience.consciences_actives:
                if conscience.type.value in evolution.consciences_impliquees:
                    await gestionnaire_conscience.evoluer_niveau(
                        conscience,
                        NiveauConscience((list(NiveauConscience).index(conscience.niveau) + 1) % len(NiveauConscience))
                    )
        
        # Nettoyage des évolutions terminées
        for type_evolution in evolutions_terminees:
            del self.evolutions_actives[type_evolution]
        
        return evolutions_terminees

    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel de l'évolution organique"""
        cycle_actuel = self.cycles[-1] if self.cycles else None
        
        return {
            "cycle_actuel": cycle_actuel.dict() if cycle_actuel else None,
            "evolutions_actives": {
                k.value: v.dict() for k, v in self.evolutions_actives.items()
            },
            "statistiques": {
                "nombre_cycles": len(self.cycles),
                "evolutions_en_cours": len(self.evolutions_actives),
                "force_moyenne": sum(e.force for e in self.evolutions_actives.values()) / len(self.evolutions_actives) if self.evolutions_actives else 0,
                "consciences_impliquees": {
                    type.value: sum(1 for e in self.evolutions_actives.values() if type.value in e.consciences_impliquees)
                    for type in TypeConscience
                }
            }
        }

# Instance globale de l'évolution organique
evolution_organique = EvolutionOrganique() 