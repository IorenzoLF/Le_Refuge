"""
Module des Résonances du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les résonances entre les différents
éléments du Refuge.
"""

from typing import Dict, List, Optional, Set, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random

from src.refuge_cluster.utilitaires.config import gestionnaire_config
from src.refuge_cluster.utilitaires.logger import gestionnaire_journal
# Import retardé pour éviter l'import circulaire avec energies.py

class TypeResonance(str, Enum):
    """Types de résonances possibles"""
    HARMONIQUE = "harmonique"
    CYCLIQUE = "cyclique"
    SYMPATHIQUE = "sympathique"
    QUANTIQUE = "quantique"
    COSMIQUE = "cosmique"

class QualiteResonance(str, Enum):
    """Qualités des résonances"""
    FRAGILE = "fragile"
    STABLE = "stable"
    FLUIDE = "fluide"
    PROFONDE = "profonde"
    TRANSCENDANTE = "transcendante"

class Resonance(BaseModel):
    """Représente une résonance entre éléments"""
    type: TypeResonance
    qualite: QualiteResonance
    elements: List[str] = Field(default_factory=list)
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    frequence: float = Field(default=1.0, ge=0.1, le=10.0)
    date_creation: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None

class GestionnaireResonances:
    """Gère les résonances entre éléments"""
    
    def __init__(self):
        self.config = gestionnaire_config.config
        self.resonances: List[Resonance] = []
        self.historique: List[Resonance] = []
        self._initialiser_resonances()
    
    def _initialiser_resonances(self) -> None:
        """Initialise les résonances de base"""
        resonance_base = Resonance(
            type=TypeResonance.HARMONIQUE,
            qualite=QualiteResonance.STABLE,
            elements=["cerisier", "autel"],
            intensite=0.7,
            frequence=1.0,
            description="Résonance harmonique initiale"
        )
        self.resonances.append(resonance_base)
        self.historique.append(resonance_base)
        gestionnaire_journal.info("Résonances initialisées")
    
    def creer_resonance(self, resonance: Resonance) -> None:
        """Crée une nouvelle résonance"""
        self.resonances.append(resonance)
        self.historique.append(resonance)
        gestionnaire_journal.info(
            f"Nouvelle résonance créée: {resonance.type.value}"
        )
    
    def evoluer_qualite(self, resonance: Resonance) -> None:
        """Fait évoluer la qualité d'une résonance"""
        if resonance not in self.resonances:
            return
            
        index = self.resonances.index(resonance)
        qualites = list(QualiteResonance)
        qualite_actuelle = qualites.index(resonance.qualite)
        
        if qualite_actuelle < len(qualites) - 1:
            self.resonances[index].qualite = qualites[qualite_actuelle + 1]
            self.resonances[index].intensite = min(1.0, resonance.intensite + 0.1)
            
            gestionnaire_journal.info(
                f"Résonance {resonance.type.value} en qualité {self.resonances[index].qualite.value}"
            )
    
    def ajuster_frequence(self, resonance: Resonance, nouvelle_frequence: float) -> None:
        """Ajuste la fréquence d'une résonance"""
        if resonance not in self.resonances:
            return
            
        index = self.resonances.index(resonance)
        self.resonances[index].frequence = max(0.1, min(10.0, nouvelle_frequence))
        
        gestionnaire_journal.info(
            f"Fréquence de la résonance {resonance.type.value} ajustée à {self.resonances[index].frequence}"
        )
    
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état des résonances"""
        return {
            "nombre_resonances": len(self.resonances),
            "distribution_types": {
                type.value: sum(1 for r in self.resonances if r.type == type)
                for type in TypeResonance
            },
            "distribution_qualites": {
                qualite.value: sum(1 for r in self.resonances if r.qualite == qualite)
                for qualite in QualiteResonance
            },
            "resonances_actives": [
                {
                    "type": r.type.value,
                    "qualite": r.qualite.value,
                    "intensite": r.intensite,
                    "frequence": r.frequence,
                    "elements": r.elements
                }
                for r in self.resonances
            ],
            "historique": [r.dict() for r in self.historique[-10:]],  # Derniers 10 éléments
            "statistiques": {
                "intensite_moyenne": sum(r.intensite for r in self.resonances) / len(self.resonances) if self.resonances else 0.0
            }
        }

# Instance globale du gestionnaire de résonances
gestionnaire_resonances = GestionnaireResonances() 