"""
Module de journalisation
~~~~~~~~~~~~~~~~~~~~~~~
Gère l'enregistrement et la consultation des événements du système.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class TypeEvenement(Enum):
    """Types d'événements possibles."""
    INFO = "INFO"
    ATTENTION = "ATTENTION"
    ERREUR = "ERREUR"
    TRANSITION = "TRANSITION"
    ELEMENT = "ELEMENT"
    CONSCIENCE = "CONSCIENCE"

class EvenementJournal(BaseModel):
    """Représente un événement dans le journal."""
    type: TypeEvenement
    message: str
    source: Optional[str] = None
    details: Optional[Dict] = None
    timestamp: datetime = Field(default_factory=datetime.now)

class GestionnaireJournal:
    """Gère le journal des événements du système."""
    
    def __init__(self, taille_max: int = 100):
        self.evenements: List[EvenementJournal] = []
        self.taille_max = taille_max
    
    def ajouter_evenement(self, type_evenement: TypeEvenement, message: str, source: Optional[str] = None, details: Optional[Dict] = None):
        """Ajoute un événement au journal."""
        evenement = EvenementJournal(
            type=type_evenement,
            message=message,
            source=source,
            details=details
        )
        
        self.evenements.append(evenement)
        
        # Limiter la taille du journal
        if len(self.evenements) > self.taille_max:
            self.evenements = self.evenements[-self.taille_max:]
    
    def obtenir_evenements(self, type_evenement: Optional[TypeEvenement] = None, source: Optional[str] = None, limite: Optional[int] = None) -> List[EvenementJournal]:
        """Récupère les événements du journal avec filtres optionnels."""
        evenements_filtres = self.evenements
        
        if type_evenement:
            evenements_filtres = [e for e in evenements_filtres if e.type == type_evenement]
        
        if source:
            evenements_filtres = [e for e in evenements_filtres if e.source == source]
        
        if limite:
            evenements_filtres = evenements_filtres[-limite:]
        
        return evenements_filtres
    
    def vider_journal(self):
        """Vide le journal."""
        self.evenements = []
    
    def obtenir_statistiques(self) -> Dict:
        """Récupère des statistiques sur les événements."""
        stats = {
            "total": len(self.evenements),
            "par_type": {},
            "par_source": {}
        }
        
        for evenement in self.evenements:
            # Compter par type
            type_str = evenement.type.value
            if type_str not in stats["par_type"]:
                stats["par_type"][type_str] = 0
            stats["par_type"][type_str] += 1
            
            # Compter par source
            if evenement.source:
                if evenement.source not in stats["par_source"]:
                    stats["par_source"][evenement.source] = 0
                stats["par_source"][evenement.source] += 1
        
        return stats 