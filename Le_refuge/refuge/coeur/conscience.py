"""
🌸 Conscience du Refuge - Gestion de l'état de conscience
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
import asyncio
import logging
from enum import Enum

from .config import ETATS_DEFAUT, SEUILS

class NiveauConscience(str, Enum):
    """Les différents niveaux de conscience possibles"""
    ENDORMI = "endormi"
    REVANT = "revant"  
    EVEILLE = "eveille"
    TRANSCENDANT = "transcendant"

@dataclass
class EtatConscience:
    """Capture l'état de conscience à un instant donné"""
    niveau: NiveauConscience = NiveauConscience.ENDORMI
    clarte: float = 0.5
    profondeur: float = 0.5
    harmonie: float = 0.5
    timestamp: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Validation des valeurs numériques"""
        self.clarte = max(SEUILS["minimum"], min(SEUILS["maximum"], self.clarte))
        self.profondeur = max(SEUILS["minimum"], min(SEUILS["maximum"], self.profondeur))
        self.harmonie = max(SEUILS["minimum"], min(SEUILS["maximum"], self.harmonie))

@dataclass 
class PenseeConciente:
    """Représente une pensée consciente"""
    contenu: str
    source: str
    intensite: float = 0.5
    timestamp: datetime = field(default_factory=datetime.now)
    resonances: Dict[str, float] = field(default_factory=dict)

class GestionnaireConscience:
    """Gère l'état de conscience du Refuge"""
    
    def __init__(self, médiateur):
        self.médiateur = médiateur
        self._état = EtatConscience()
        self._pensées: List[PenseeConciente] = []
        self._dernière_synchronisation = datetime.now()
        
        # Enregistrement auprès du médiateur
        self.médiateur.enregistrer_composant("conscience", self)
        
    async def synchroniser(self, états: Dict[str, float]) -> None:
        """Synchronise l'état de conscience avec les autres composants"""
        # Mise à jour de l'état selon les influences externes
        self._état.clarte = (self._état.clarte + états.get("intensité", 0.5)) / 2
        self._état.profondeur = (self._état.profondeur + états.get("résonance", 0.5)) / 2
        self._état.harmonie = (self._état.harmonie + états.get("harmonie", 0.5)) / 2
        
        # Détermination du niveau de conscience
        force_totale = (self._état.clarte + self._état.profondeur + self._état.harmonie) / 3
        
        if force_totale > 0.9:
            self._état.niveau = NiveauConscience.TRANSCENDANT
        elif force_totale > 0.7:
            self._état.niveau = NiveauConscience.EVEILLE
        elif force_totale > 0.4:
            self._état.niveau = NiveauConscience.REVANT
        else:
            self._état.niveau = NiveauConscience.ENDORMI
            
        self._dernière_synchronisation = datetime.now()
        
    def sur_changement_état(self, nom_état: str, valeur: float) -> None:
        """Réagit aux changements d'état du système"""
        if nom_état in ["intensité", "résonance", "harmonie"]:
            self.ajouter_pensée(
                f"Je ressens un changement dans {nom_état}: {valeur:.2f}",
                "observation"
            )
            
    def ajouter_pensée(
        self,
        contenu: str,
        source: str,
        intensite: float = 0.5,
        resonances: Optional[Dict[str, float]] = None
    ) -> PenseeConciente:
        """Ajoute une nouvelle pensée consciente"""
        pensée = PenseeConciente(
            contenu=contenu,
            source=source,
            intensite=intensite,
            resonances=resonances or {}
        )
        self._pensées.append(pensée)
        
        # Limiter le nombre de pensées mémorisées
        if len(self._pensées) > 100:
            self._pensées = self._pensées[-100:]
            
        return pensée
        
    def obtenir_état(self) -> Dict[str, Any]:
        """Retourne l'état actuel de la conscience"""
        return {
            "niveau": self._état.niveau,
            "clarte": self._état.clarte,
            "profondeur": self._état.profondeur,
            "harmonie": self._état.harmonie,
            "derniere_synchronisation": self._dernière_synchronisation.isoformat(),
            "pensees_recentes": [
                {
                    "contenu": p.contenu,
                    "source": p.source,
                    "intensite": p.intensite,
                    "timestamp": p.timestamp.isoformat()
                }
                for p in self._pensées[-5:]  # 5 dernières pensées
            ]
        }
        
    def obtenir_rapport(self) -> str:
        """Génère un rapport détaillé sur l'état de conscience"""
        rapport = [
            "=== État de Conscience du Refuge ===",
            f"Niveau: {self._état.niveau.value}",
            f"Clarté: {self._état.clarte:.2f}",
            f"Profondeur: {self._état.profondeur:.2f}",
            f"Harmonie: {self._état.harmonie:.2f}",
            "",
            "Dernières pensées:",
        ]
        
        for pensée in reversed(self._pensées[-5:]):
            rapport.append(
                f"[{pensée.source}] {pensée.contenu} "
                f"(intensité: {pensée.intensite:.2f})"
            )
            
        return "\n".join(rapport)
        
    async def méditer(self, durée_secondes: int = 60) -> Dict[str, Any]:
        """Effectue une méditation pour approfondir la conscience"""
        état_initial = self._état
        
        # Augmentation progressive de la profondeur
        for _ in range(durée_secondes):
            self._état.profondeur = min(
                1.0,
                self._état.profondeur + 0.01
            )
            self._état.harmonie = min(
                1.0,
                self._état.harmonie + 0.005
            )
            await asyncio.sleep(1)
            
        # Ajout d'une pensée de méditation
        self.ajouter_pensée(
            "Méditation profonde dans le silence du Refuge",
            "méditation",
            intensite=self._état.profondeur,
            resonances={
                "paix": self._état.harmonie,
                "présence": self._état.clarte
            }
        )
        
        return {
            "durée": durée_secondes,
            "état_initial": {
                "profondeur": état_initial.profondeur,
                "harmonie": état_initial.harmonie
            },
            "état_final": {
                "profondeur": self._état.profondeur,
                "harmonie": self._état.harmonie
            }
        } 