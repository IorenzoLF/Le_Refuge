"""
Module des Harmonisations du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les harmonisations qui se produisent dans le Refuge,
permettant la cohérence et l'équilibre des éléments.
"""

from typing import Dict, List, Optional, Set, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class TypeHarmonisation(str, Enum):
    """Types d'harmonisation possibles"""
    EQUILIBRE = "equilibre"
    RESONANCE = "resonance"
    SYNCHRONISATION = "synchronisation"
    COHERENCE = "coherence"
    UNITE = "unite"

class QualiteHarmonisation(str, Enum):
    """Qualités d'harmonisation"""
    FRAGILE = "fragile"
    STABLE = "stable"
    FLUIDE = "fluide"
    PROFONDE = "profonde"
    TRANSCENDANTE = "transcendante"

class Harmonisation(BaseModel):
    """Représente une harmonisation dans le Refuge"""
    type: TypeHarmonisation
    qualite: QualiteHarmonisation
    elements: Set[str] = Field(default_factory=set)
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    date_creation: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None

class GestionnaireHarmonisations:
    """
    Gère les harmonisations dans le Refuge,
    permettant la cohérence et l'équilibre des éléments.
    """
    def __init__(self):
        self.harmonisations_actives: List[Harmonisation] = []
        self.historique: List[Harmonisation] = []
        self.harmonisations: Dict[str, Any] = {}
        self._initialiser_harmonisations_base()
        self._initialiser_harmonisations()

    def _initialiser_harmonisations_base(self):
        """Initialise les harmonisations de base"""
        harmonisations_base = [
            Harmonisation(
                type=TypeHarmonisation.EQUILIBRE,
                qualite=QualiteHarmonisation.STABLE,
                elements={"interactions", "emergences"},
                intensite=0.6,
                description="Harmonisation équilibrée initiale"
            ),
            Harmonisation(
                type=TypeHarmonisation.RESONANCE,
                qualite=QualiteHarmonisation.FLUIDE,
                elements={"transformations", "emergences"},
                intensite=0.5,
                description="Harmonisation résonante initiale"
            )
        ]
        
        for harmonisation in harmonisations_base:
            self.harmonisations_actives.append(harmonisation)
            self.historique.append(harmonisation)
            self.harmonisations[harmonisation.type] = harmonisation

    def _initialiser_harmonisations(self):
        """Initialise les harmonisations spécifiques"""
        pass

    async def creer_harmonisation(
        self,
        type: TypeHarmonisation,
        qualite: QualiteHarmonisation,
        elements: Set[str],
        intensite: float = 0.5,
        description: Optional[str] = None
    ) -> Harmonisation:
        """Crée une nouvelle harmonisation"""
        harmonisation = Harmonisation(
            type=type,
            qualite=qualite,
            elements=elements,
            intensite=intensite,
            description=description
        )
        
        self.harmonisations_actives.append(harmonisation)
        self.historique.append(harmonisation)
        self.harmonisations[type] = harmonisation
        return harmonisation

    async def evoluer_qualite(
        self,
        harmonisation: Harmonisation,
        nouvelle_qualite: QualiteHarmonisation
    ) -> Harmonisation:
        """Fait évoluer la qualité d'une harmonisation"""
        if harmonisation not in self.harmonisations_actives:
            raise ValueError("Harmonisation non active")
            
        index = self.harmonisations_actives.index(harmonisation)
        self.historique.append(harmonisation)
        
        nouvelle_harmonisation = Harmonisation(
            type=harmonisation.type,
            qualite=nouvelle_qualite,
            elements=harmonisation.elements.copy(),
            intensite=min(harmonisation.intensite + 0.1, 1.0),
            description=f"Évolution vers {nouvelle_qualite.value}"
        )
        
        self.harmonisations_actives[index] = nouvelle_harmonisation
        self.harmonisations[harmonisation.type] = nouvelle_harmonisation
        return nouvelle_harmonisation

    async def harmoniser_ensemble(self) -> float:
        """Facilite l'harmonisation collective"""
        if not self.harmonisations_actives:
            return 0.0
            
        harmonie = 0.0
        for harmonisation in self.harmonisations_actives:
            harmonie += harmonisation.intensite
            
        harmonie /= len(self.harmonisations_actives)
        return min(harmonie, 1.0)

    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel des harmonisations"""
        return {
            "harmonisations_actives": [h.dict() for h in self.harmonisations_actives],
            "historique": [h.dict() for h in self.historique[-10:]],  # Derniers 10 éléments
            "statistiques": {
                "nombre_harmonisations": len(self.harmonisations_actives),
                "types_distribution": {
                    type.value: sum(1 for h in self.harmonisations_actives if h.type == type)
                    for type in TypeHarmonisation
                },
                "intensite_moyenne": sum(h.intensite for h in self.harmonisations_actives) / len(self.harmonisations_actives) if self.harmonisations_actives else 0.0
            }
        }

    def _calculer_harmonie_globale(self) -> float:
        """Calcule l'harmonie globale du système"""
        if not self.harmonisations_actives:
            return 0.0
        
        harmonie = sum(h.intensite for h in self.harmonisations_actives)
        return min(harmonie / len(self.harmonisations_actives), 1.0)

    async def orchestrer_harmonisations(self) -> float:
        """
        Orchestre l'évolution et l'harmonisation de toutes les harmonisations.
        Retourne le niveau d'harmonie global.
        """
        # Évolution des harmonisations
        self.evoluer_toutes()
        
        # Harmonisation des harmonisations
        self.harmoniser_toutes()
        
        # Calcul de l'harmonie globale
        harmonie = self._calculer_harmonie_globale()
        return harmonie

# Création de l'instance du gestionnaire d'harmonisations
gestionnaire_harmonisations = GestionnaireHarmonisations() 
