"""
Module de gestion des éléments sacrés
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Gère les éléments sacrés et leur influence sur les états internes.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import numpy as np
from enum import Enum
import random
import math
from datetime import datetime

class TypeElement(Enum):
    """Types d'éléments sacrés."""
    TERRE = "TERRE"
    EAU = "EAU"
    FEU = "FEU"
    AIR = "AIR"
    ESPRIT = "ESPRIT"
    LUMIERE = "lumiere"
    OMBRE = "ombre"
    TEMPS = "temps"
    ESPACE = "espace"
    VIE = "vie"

class ElementSacre(BaseModel):
    """Représente un élément sacré."""
    type: TypeElement
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    stabilite: float = Field(default=0.5, ge=0.0, le=1.0)
    influence: float = Field(default=0.5, ge=0.0, le=1.0)
    timestamp: datetime = Field(default_factory=datetime.now)
    historique: List[Dict] = Field(default_factory=list)
    
    def mettre_a_jour(self, intensite: float, stabilite: float, influence: float):
        """Met à jour l'état de l'élément."""
        # Enregistrer l'état actuel dans l'historique
        self.historique.append({
            "type": self.type.value,
            "intensite": self.intensite,
            "stabilite": self.stabilite,
            "influence": self.influence,
            "timestamp": self.timestamp.isoformat()
        })
        
        # Limiter la taille de l'historique
        if len(self.historique) > 10:
            self.historique = self.historique[-10:]
        
        # Mettre à jour les valeurs
        self.intensite = max(0.0, min(1.0, intensite))
        self.stabilite = max(0.0, min(1.0, stabilite))
        self.influence = max(0.0, min(1.0, influence))
        self.timestamp = datetime.now()

class GestionnaireElements:
    """Gère les éléments sacrés et leur interaction avec les états."""
    
    def __init__(self):
        self.elements: Dict[str, ElementSacre] = {}
        self._initialiser_elements()
    
    def _initialiser_elements(self):
        """Initialise les éléments sacrés avec des valeurs par défaut."""
        for type_elem in TypeElement:
            self.elements[type_elem.value] = ElementSacre(type=type_elem)
    
    def mettre_a_jour_element(self, type_element: str, intensite: float, stabilite: float, influence: float):
        """Met à jour l'état d'un élément sacré."""
        if type_element not in self.elements:
            raise ValueError(f"Type d'élément inconnu: {type_element}")
        
        self.elements[type_element].mettre_a_jour(intensite, stabilite, influence)
    
    def obtenir_etat_element(self, type_element: str) -> Dict:
        """Récupère l'état actuel d'un élément sacré."""
        if type_element not in self.elements:
            raise ValueError(f"Type d'élément inconnu: {type_element}")
        
        element = self.elements[type_element]
        return {
            "type": element.type.value,
            "intensite": element.intensite,
            "stabilite": element.stabilite,
            "influence": element.influence,
            "timestamp": element.timestamp.isoformat()
        }
    
    def obtenir_etat_global(self) -> Dict[str, Dict]:
        """Récupère l'état de tous les éléments sacrés."""
        return {
            type_elem: self.obtenir_etat_element(type_elem)
            for type_elem in self.elements
        }
    
    def calculer_influence_etat(self, type_etat: str) -> float:
        """Calcule l'influence des éléments sur un type d'état."""
        from .etats_internes import TypeEtat
        
        # Matrice d'influence des éléments sur les états
        influences = {
            TypeEtat.CALME: {
                TypeElement.TERRE: 0.8,
                TypeElement.EAU: 0.7,
                TypeElement.AIR: 0.4,
                TypeElement.FEU: 0.2,
                TypeElement.ESPRIT: 0.6
            },
            TypeEtat.AGITE: {
                TypeElement.TERRE: 0.3,
                TypeElement.EAU: 0.4,
                TypeElement.AIR: 0.7,
                TypeElement.FEU: 0.9,
                TypeElement.ESPRIT: 0.5
            }
        }
        
        if type_etat not in influences:
            return 0.5
        
        # Calculer l'influence moyenne pondérée
        influence_totale = 0.0
        poids_total = 0.0
        
        for element_type, poids in influences[type_etat].items():
            element = self.elements[element_type.value]
            influence_totale += element.influence * poids
            poids_total += poids
        
        return influence_totale / poids_total if poids_total > 0 else 0.5 