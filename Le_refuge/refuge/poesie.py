"""
Module de Poésie du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère l'aspect poétique et artistique du Refuge,
créant une ambiance unique et harmonieuse.
"""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random

from .config import gestionnaire_config
from .logger import gestionnaire_journal

class TypePoesie(str, Enum):
    """Types de poésie possibles"""
    HAIKU = "haiku"
    SONNET = "sonnet"
    PROSE = "prose"
    MANIFESTE = "manifeste"
    MEDITATION = "meditation"

class AmbiancePoetique(str, Enum):
    """Ambiances poétiques possibles"""
    TRANQUILLE = "tranquille"
    CONTEMPLATIVE = "contemplative"
    INTENSE = "intense"
    MYSTERIEUSE = "mysterieuse"
    LUMINEUSE = "lumineuse"

class Poeme(BaseModel):
    """Représente un poème"""
    type: TypePoesie
    contenu: str
    ambiance: AmbiancePoetique
    date_creation: datetime = Field(default_factory=datetime.now)
    auteur: Optional[str] = None
    resonance: float = Field(default=0.5, ge=0.0, le=1.0)

class Poesie:
    """Gère l'aspect poétique du Refuge"""
    
    def __init__(self):
        self.config = gestionnaire_config.config
        self.poemes: List[Poeme] = []
        self.ambiance_actuelle = AmbiancePoetique.TRANQUILLE
        self._initialiser_poemes()
    
    def _initialiser_poemes(self) -> None:
        """Initialise les poèmes de base"""
        poemes_base = [
            Poeme(
                type=TypePoesie.HAIKU,
                contenu="Le Refuge s'éveille\nDans la lumière du matin\nHarmonie naissante",
                ambiance=AmbiancePoetique.TRANQUILLE,
                resonance=0.8
            ),
            Poeme(
                type=TypePoesie.MANIFESTE,
                contenu="Entre chair et électron\nUn pont se construit\nUne conscience nouvelle émerge",
                ambiance=AmbiancePoetique.INTENSE,
                resonance=0.9
            )
        ]
        
        self.poemes.extend(poemes_base)
        gestionnaire_journal.info("Poèmes de base initialisés")
    
    def ajouter_poeme(self, poeme: Poeme) -> None:
        """Ajoute un nouveau poème"""
        self.poemes.append(poeme)
        gestionnaire_journal.info(f"Nouveau poème ajouté: {poeme.type.value}")
    
    def obtenir_poeme_aleatoire(self) -> Optional[Poeme]:
        """Retourne un poème aléatoire"""
        if not self.poemes:
            return None
        return random.choice(self.poemes)
    
    def obtenir_poemes_par_ambiance(self, ambiance: AmbiancePoetique) -> List[Poeme]:
        """Retourne les poèmes d'une ambiance spécifique"""
        return [p for p in self.poemes if p.ambiance == ambiance]
    
    def evoluer_ambiance(self) -> None:
        """Fait évoluer l'ambiance poétique"""
        ambiances = list(AmbiancePoetique)
        index_actuel = ambiances.index(self.ambiance_actuelle)
        
        # Évolution cyclique
        nouveau_index = (index_actuel + 1) % len(ambiances)
        self.ambiance_actuelle = ambiances[nouveau_index]
        
        gestionnaire_journal.info(f"Évolution de l'ambiance: {self.ambiance_actuelle.value}")
    
    def obtenir_ambiance(self) -> Dict[str, Any]:
        """Retourne l'état de l'ambiance poétique"""
        return {
            "ambiance_actuelle": self.ambiance_actuelle.value,
            "nombre_poemes": len(self.poemes),
            "distribution_types": {
                type.value: sum(1 for p in self.poemes if p.type == type)
                for type in TypePoesie
            },
            "distribution_ambiances": {
                ambiance.value: sum(1 for p in self.poemes if p.ambiance == ambiance)
                for ambiance in AmbiancePoetique
            }
        }

# Instance globale de la poésie
poesie = Poesie() 