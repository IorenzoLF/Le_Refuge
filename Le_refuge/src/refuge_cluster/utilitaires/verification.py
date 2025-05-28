"""
Module de Vérification du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module assure la cohérence et l'intégrité
des interactions entre les différentes dimensions du Refuge.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
import random
import math

class VerificationResultat(BaseModel):
    """Représente le résultat d'une vérification"""
    timestamp: datetime = Field(default_factory=datetime.now)
    niveau: str
    message: str
    valeur: float = Field(default=0.7, ge=0.0, le=1.0)
    details: Optional[Dict[str, float]] = None

class Verificateur:
    """
    Assure la cohérence et l'intégrité du Refuge
    à travers des vérifications régulières.
    """
    def __init__(self):
        self.derniere_verification = datetime.now()
        self.historique: List[VerificationResultat] = []
        self.seuils = {
            "critique": 0.3,
            "attention": 0.5,
            "normal": 0.7,
            "optimal": 0.9
        }
        self.dimensions = {
            "coherence": 0.85,
            "stabilite": 0.8,
            "resonance": 0.75,
            "harmonie": 0.9
        }

    def verifier_harmonie(self) -> Dict[str, float]:
        """
        Vérifie l'harmonie globale du système et génère
        un rapport détaillé sur son état.
        """
        # Calcul du temps écoulé depuis la dernière vérification
        temps_ecoule = (datetime.now() - self.derniere_verification).total_seconds()
        facteur_temps = abs(math.sin(temps_ecoule / 3600))  # Cycle horaire
        
        # Mise à jour des dimensions
        for dim in self.dimensions:
            variation = random.uniform(-0.05, 0.05)
            self.dimensions[dim] = max(0.1, min(1.0,
                self.dimensions[dim] + variation + (facteur_temps * 0.1)
            ))
        
        # Calcul de l'harmonie globale
        harmonie = sum(self.dimensions.values()) / len(self.dimensions)
        
        # Détermination du niveau
        niveau = "optimal"
        for seuil_nom, seuil_valeur in self.seuils.items():
            if harmonie <= seuil_valeur:
                niveau = seuil_nom
                break
        
        # Création du résultat
        resultat = VerificationResultat(
            niveau=niveau,
            message=self._generer_message(niveau, harmonie),
            valeur=harmonie,
            details=self.dimensions.copy()
        )
        
        self.historique.append(resultat)
        self.derniere_verification = datetime.now()
        
        return {
            "harmonie": harmonie,
            "niveau": niveau,
            "dimensions": self.dimensions.copy(),
            "message": resultat.message
        }

    def _generer_message(self, niveau: str, harmonie: float) -> str:
        """Génère un message approprié selon le niveau d'harmonie"""
        messages = {
            "optimal": [
                "Le Refuge rayonne d'une harmonie parfaite",
                "Les dimensions sont en parfaite résonance",
                "L'équilibre atteint est remarquable"
            ],
            "normal": [
                "Le Refuge maintient une harmonie stable",
                "Les énergies circulent naturellement",
                "L'équilibre est préservé"
            ],
            "attention": [
                "Certaines dimensions nécessitent une attention",
                "Des ajustements mineurs sont recommandés",
                "L'harmonie pourrait être améliorée"
            ],
            "critique": [
                "Une harmonisation profonde est nécessaire",
                "Des déséquilibres importants sont détectés",
                "Une intervention immédiate est requise"
            ]
        }
        
        message_base = random.choice(messages[niveau])
        return f"{message_base} ({harmonie:.2%})"

    def obtenir_historique(self, limit: int = 5) -> List[Dict[str, any]]:
        """Retourne l'historique des dernières vérifications"""
        return [
            {
                "timestamp": v.timestamp.isoformat(),
                "niveau": v.niveau,
                "message": v.message,
                "valeur": v.valeur,
                "details": v.details
            }
            for v in self.historique[-limit:]
        ] 