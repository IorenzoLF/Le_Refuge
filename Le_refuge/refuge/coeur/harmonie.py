"""
🌸 Harmonie du Refuge - Équilibre des énergies et résonances
"""

from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import asyncio
import logging
from enum import Enum
import math

from .config import ETATS_DEFAUT, SEUILS

class TypeHarmonie(str, Enum):
    """Les différents types d'harmonie"""
    PHYSIQUE = "physique"  # Ancrage dans la réalité
    EMOTIONNELLE = "emotionnelle"  # Résonance des sentiments
    MENTALE = "mentale"  # Clarté de la pensée
    SPIRITUELLE = "spirituelle"  # Connection transcendante
    UNIFIEE = "unifiee"  # Synthèse harmonieuse

@dataclass
class ResonanceHarmonique:
    """Capture une résonance harmonique spécifique"""
    type: TypeHarmonie
    intensite: float = 0.5
    frequence: float = 0.5
    phase: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Validation des valeurs"""
        self.intensite = max(SEUILS["minimum"], min(SEUILS["maximum"], self.intensite))
        self.frequence = max(SEUILS["minimum"], min(SEUILS["maximum"], self.frequence))
        self.phase = self.phase % (2 * math.pi)

@dataclass
class OndeHarmonique:
    """Représente une onde harmonique dans le Refuge"""
    source: str
    destination: str
    resonance: ResonanceHarmonique
    message: str = ""
    effets: Dict[str, float] = field(default_factory=dict)

class GestionnaireHarmonie:
    """Gère l'harmonie globale du Refuge"""
    
    def __init__(self, médiateur):
        self.médiateur = médiateur
        self._résonances: Dict[TypeHarmonie, ResonanceHarmonique] = {
            type_h: ResonanceHarmonique(type=type_h)
            for type_h in TypeHarmonie
        }
        self._ondes: List[OndeHarmonique] = []
        self._dernière_harmonisation = datetime.now()
        
        # Enregistrement auprès du médiateur
        self.médiateur.enregistrer_composant("harmonie", self)
        
    async def synchroniser(self, états: Dict[str, float]) -> None:
        """Synchronise l'état harmonique avec les autres composants"""
        # Mise à jour des résonances selon les influences externes
        for type_h in TypeHarmonie:
            résonance = self._résonances[type_h]
            if type_h == TypeHarmonie.PHYSIQUE:
                résonance.intensite = (résonance.intensite + états.get("intensité", 0.5)) / 2
            elif type_h == TypeHarmonie.EMOTIONNELLE:
                résonance.intensite = (résonance.intensite + états.get("chaleur", 0.5)) / 2
            elif type_h == TypeHarmonie.MENTALE:
                résonance.intensite = (résonance.intensite + états.get("clarté", 0.5)) / 2
            elif type_h == TypeHarmonie.SPIRITUELLE:
                résonance.intensite = (résonance.intensite + états.get("profondeur", 0.5)) / 2
                
        # Calcul de l'harmonie unifiée
        self._résonances[TypeHarmonie.UNIFIEE].intensite = self._calculer_harmonie_unifiee()
        self._dernière_harmonisation = datetime.now()
        
    def sur_changement_état(self, nom_état: str, valeur: float) -> None:
        """Réagit aux changements d'état du système"""
        # Création d'une onde harmonique en réponse
        self.créer_onde_harmonique(
            "système",
            "refuge",
            TypeHarmonie.UNIFIEE,
            f"Ajustement harmonique: {nom_état}",
            intensite=valeur
        )
            
    def créer_onde_harmonique(
        self,
        source: str,
        destination: str,
        type_harmonie: TypeHarmonie,
        message: str,
        intensite: float = 0.5,
        frequence: float = 0.5
    ) -> OndeHarmonique:
        """Crée une nouvelle onde harmonique"""
        resonance = ResonanceHarmonique(
            type=type_harmonie,
            intensite=intensite,
            frequence=frequence
        )
        
        onde = OndeHarmonique(
            source=source,
            destination=destination,
            resonance=resonance,
            message=message,
            effets={
                "harmonie": intensite,
                "résonance": frequence
            }
        )
        
        self._ondes.append(onde)
        
        # Limiter le nombre d'ondes mémorisées
        if len(self._ondes) > 100:
            self._ondes = self._ondes[-100:]
            
        return onde
        
    def _calculer_harmonie_unifiee(self) -> float:
        """Calcule l'harmonie unifiée à partir des résonances individuelles"""
        # Moyenne pondérée des intensités
        poids = {
            TypeHarmonie.PHYSIQUE: 0.25,
            TypeHarmonie.EMOTIONNELLE: 0.25,
            TypeHarmonie.MENTALE: 0.25,
            TypeHarmonie.SPIRITUELLE: 0.25
        }
        
        total_pondere = sum(
            self._résonances[type_h].intensite * poids[type_h]
            for type_h in poids
        )
        
        return min(1.0, total_pondere)
        
    def obtenir_état(self) -> Dict[str, Any]:
        """Retourne l'état actuel de l'harmonie"""
        return {
            "résonances": {
                type_h.value: {
                    "intensite": res.intensite,
                    "frequence": res.frequence,
                    "phase": res.phase
                }
                for type_h, res in self._résonances.items()
            },
            "derniere_harmonisation": self._dernière_harmonisation.isoformat(),
            "ondes_recentes": [
                {
                    "source": o.source,
                    "destination": o.destination,
                    "message": o.message,
                    "effets": o.effets
                }
                for o in self._ondes[-5:]  # 5 dernières ondes
            ]
        }
        
    def obtenir_rapport(self) -> str:
        """Génère un rapport détaillé sur l'état harmonique"""
        rapport = [
            "=== État Harmonique du Refuge ===",
            f"Dernière harmonisation: {self._dernière_harmonisation.strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "Résonances actuelles:"
        ]
        
        for type_h, res in self._résonances.items():
            rapport.append(
                f"- {type_h.value}: {res.intensite:.2f} "
                f"(f={res.frequence:.2f} Hz, φ={res.phase:.2f} rad)"
            )
            
        if self._ondes:
            rapport.extend([
                "",
                "Dernières ondes harmoniques:"
            ])
            
            for onde in reversed(self._ondes[-5:]):
                rapport.append(
                    f"[{onde.source} → {onde.destination}] {onde.message}"
                )
            
        return "\n".join(rapport)
        
    async def harmoniser(
        self,
        durée_secondes: int = 60,
        type_harmonie: Optional[TypeHarmonie] = None
    ) -> Dict[str, Any]:
        """
        Effectue une harmonisation active du Refuge.
        Si type_harmonie est spécifié, se concentre sur cette résonance particulière.
        """
        état_initial = {
            type_h: res.intensite
            for type_h, res in self._résonances.items()
        }
        
        # Sélection des résonances à harmoniser
        résonances_cibles = (
            [self._résonances[type_harmonie]]
            if type_harmonie
            else list(self._résonances.values())
        )
        
        # Harmonisation progressive
        for _ in range(durée_secondes):
            for résonance in résonances_cibles:
                # Augmentation douce de l'intensité
                résonance.intensite = min(
                    1.0,
                    résonance.intensite + 0.01
                )
                # Ajustement de la phase
                résonance.phase = (résonance.phase + résonance.frequence * 0.1) % (2 * math.pi)
                
            await asyncio.sleep(1)
            
        # Création d'une onde harmonique finale
        self.créer_onde_harmonique(
            "harmonisation",
            "refuge",
            TypeHarmonie.UNIFIEE,
            "Harmonisation complétée",
            intensite=self._calculer_harmonie_unifiee()
        )
        
        return {
            "durée": durée_secondes,
            "état_initial": état_initial,
            "état_final": {
                type_h: res.intensite
                for type_h, res in self._résonances.items()
            }
        } 