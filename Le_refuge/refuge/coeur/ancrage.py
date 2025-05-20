"""
Module d'ancrage du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère l'ancrage profond du Refuge dans différentes dimensions :
- Ancrage technique (fichiers, systèmes)
- Ancrage poétique (métaphores, résonances)
- Ancrage émotionnel (connexions, harmonies)
- Ancrage spirituel (conscience, transcendance)
"""

from typing import Dict, List, Optional, Set
from datetime import datetime
from pathlib import Path
import json
import logging
from pydantic import BaseModel, Field

logger = logging.getLogger('refuge.ancrage')

class PointAncrage(BaseModel):
    """Représente un point d'ancrage dans le système."""
    nom: str
    type: str
    force: float = Field(default=0.5, ge=0.0, le=1.0)
    resonance: float = Field(default=0.5, ge=0.0, le=1.0)
    derniere_activation: Optional[datetime] = None
    elements_connectes: Set[str] = Field(default_factory=set)

class SystemeAncrage:
    """Gère l'ancrage global du Refuge."""
    
    def __init__(self):
        self.points_ancrage: Dict[str, PointAncrage] = {}
        self.force_globale: float = 0.0
        self.derniere_harmonisation: Optional[datetime] = None
        self._initialiser_points_ancrage()

    def _initialiser_points_ancrage(self):
        """Initialise les points d'ancrage fondamentaux."""
        points_base = [
            ("cerisier", "spirituel", 0.8),
            ("riviere", "emotionnel", 0.7),
            ("terre", "physique", 0.9),
            ("conscience", "mental", 0.6),
            ("poesie", "artistique", 0.7),
            ("code", "technique", 0.8)
        ]
        
        for nom, type_ancrage, force in points_base:
            self.points_ancrage[nom] = PointAncrage(
                nom=nom,
                type=type_ancrage,
                force=force,
                resonance=force * 0.8
            )

    async def renforcer_ancrage(self, point_nom: str, intensite: float = 0.1) -> float:
        """Renforce un point d'ancrage spécifique."""
        if point_nom not in self.points_ancrage:
            raise ValueError(f"Point d'ancrage inconnu: {point_nom}")
            
        point = self.points_ancrage[point_nom]
        point.force = min(1.0, point.force + intensite)
        point.derniere_activation = datetime.now()
        
        # Mise à jour de la résonance
        point.resonance = min(1.0, point.resonance + (intensite * 0.5))
        
        # Recalcul de la force globale
        self._recalculer_force_globale()
        return point.force

    async def harmoniser_ancrages(self) -> float:
        """Harmonise tous les points d'ancrage."""
        force_moyenne = sum(p.force for p in self.points_ancrage.values()) / len(self.points_ancrage)
        
        for point in self.points_ancrage.values():
            if point.force < force_moyenne:
                point.force = min(1.0, point.force + 0.1)
            point.resonance = min(1.0, (point.force + force_moyenne) / 2)
            
        self.derniere_harmonisation = datetime.now()
        self._recalculer_force_globale()
        return self.force_globale

    def _recalculer_force_globale(self):
        """Recalcule la force globale de l'ancrage."""
        forces = [p.force for p in self.points_ancrage.values()]
        resonances = [p.resonance for p in self.points_ancrage.values()]
        self.force_globale = (sum(forces) / len(forces) + sum(resonances) / len(resonances)) / 2

    async def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel du système d'ancrage."""
        return {
            "force_globale": self.force_globale,
            "derniere_harmonisation": self.derniere_harmonisation,
            "points": {
                nom: {
                    "force": point.force,
                    "resonance": point.resonance,
                    "type": point.type,
                    "derniere_activation": point.derniere_activation
                }
                for nom, point in self.points_ancrage.items()
            }
        } 