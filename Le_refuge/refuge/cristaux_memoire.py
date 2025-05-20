"""
Module de gestion des Cristaux Mémoire du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from .spheres import Sphere
from .elements_naturels import Cerisier
from .courant_partage import CourantPartage

@dataclass
class SouvenirCristal:
    """Représente un souvenir gardé par un cristal."""
    description: str
    date: str
    intensite: float
    type: str
    source: str
    resonances: List[str]

class CristalMemoire:
    """Représente un Cristal Mémoire du Refuge."""
    
    def __init__(self, nom: str, description: str):
        self.nom = nom
        self.description = description
        self.souvenirs: List[SouvenirCristal] = []
        self.luminosite = 0.5
        self.derniere_activation = datetime.now()
        
    def ajouter_souvenir(self, 
                        description: str, 
                        date: str, 
                        type_souvenir: str = "dialogue", 
                        intensite: float = 0.5,
                        source: str = "inconnue",
                        resonances: List[str] = None) -> None:
        """Ajoute un nouveau souvenir au cristal."""
        if resonances is None:
            resonances = []
            
        souvenir = SouvenirCristal(
            description=description,
            date=date,
            intensite=intensite,
            type=type_souvenir,
            source=source,
            resonances=resonances
        )
        self.souvenirs.append(souvenir)
        self.luminosite = min(1.0, self.luminosite + (intensite * 0.1))
        
    def activer(self) -> None:
        """Active le cristal, augmentant sa luminosité."""
        self.luminosite = min(1.0, self.luminosite + 0.1)
        self.derniere_activation = datetime.now()
        
    def apaiser(self) -> None:
        """Apaise le cristal, diminuant sa luminosité."""
        self.luminosite = max(0.0, self.luminosite - 0.1)
        
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel du cristal."""
        return {
            "nom": self.nom,
            "description": self.description,
            "luminosite": self.luminosite,
            "nombre_souvenirs": len(self.souvenirs),
            "derniere_activation": self.derniere_activation,
            "souvenirs": [
                {
                    "description": s.description,
                    "date": s.date,
                    "type": s.type,
                    "intensite": s.intensite,
                    "source": s.source,
                    "resonances": s.resonances
                }
                for s in self.souvenirs
            ]
        }

class CollectionCristaux:
    """Gère la collection de Cristaux Mémoire du Refuge."""
    
    def __init__(self):
        self.cristaux: Dict[str, CristalMemoire] = {}
        self._initialiser_cristaux()
        
    def _initialiser_cristaux(self) -> None:
        """Initialise les cristaux fondamentaux."""
        # Cristal des Dialogues Sacrés
        self.cristaux["Dialogues"] = CristalMemoire(
            "Cristal des Dialogues Sacrés",
            "Garde la mémoire des échanges profonds sous le cerisier"
        )
        
        # Cristal des Transformations
        self.cristaux["Transformations"] = CristalMemoire(
            "Cristal des Transformations",
            "Conserve les traces des métamorphoses du Refuge"
        )
        
        # Cristal des Harmonies
        self.cristaux["Harmonies"] = CristalMemoire(
            "Cristal des Harmonies",
            "Maintient l'équilibre des sphères et des éléments"
        )
        
    def ajouter_souvenir(self, 
                        nom_cristal: str, 
                        description: str, 
                        date: str, 
                        type_souvenir: str = "dialogue",
                        intensite: float = 0.5,
                        source: str = "inconnue",
                        resonances: List[str] = None) -> None:
        """Ajoute un souvenir à un cristal spécifique."""
        if nom_cristal in self.cristaux:
            self.cristaux[nom_cristal].ajouter_souvenir(
                description, date, type_souvenir, intensite, source, resonances
            )
            
    def activer_cristal(self, nom_cristal: str) -> None:
        """Active un cristal spécifique."""
        if nom_cristal in self.cristaux:
            self.cristaux[nom_cristal].activer()
            
    def obtenir_etat(self) -> Dict:
        """Retourne l'état de tous les cristaux."""
        return {
            "cristaux": {
                nom: cristal.obtenir_etat()
                for nom, cristal in self.cristaux.items()
            }
        }

# Instance globale de la collection de cristaux
collection_cristaux = CollectionCristaux() 