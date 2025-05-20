"""
Gestion des éléments sacrés du refuge.
Définit et gère les éléments fondamentaux qui composent le refuge poétique.
"""

import logging
from typing import Dict, List, Optional, Union
from pathlib import Path
import json
from datetime import datetime

from refuge_config import ELEMENTS_SACRES, METAPHORES

logger = logging.getLogger('refuge.elements')

class ElementSacre:
    """Représente un élément sacré du refuge."""
    
    def __init__(self, nom: str, details: Dict):
        self.nom = nom
        self.couleur = details["couleur"]
        self.essence = details["essence"]
        self.position = details["position"]
        self.vibration = details["vibration"]
        self.energie = 100
        self.derniere_interaction = None
        
    def interagir(self):
        """Enregistre une interaction avec l'élément."""
        self.derniere_interaction = datetime.now()
        self.energie = min(100, self.energie + 10)
        logger.info(f"Interaction avec {self.nom}")
        
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel de l'élément."""
        return {
            "nom": self.nom,
            "couleur": self.couleur,
            "essence": self.essence,
            "position": self.position,
            "vibration": self.vibration,
            "energie": self.energie,
            "derniere_interaction": self.derniere_interaction.isoformat() if self.derniere_interaction else None
        }

class GestionnaireElementsSacres:
    """Gère l'ensemble des éléments sacrés du refuge."""
    
    def __init__(self):
        self.elements = {}
        self._initialiser_elements()
        
    def _initialiser_elements(self):
        """Initialise les éléments sacrés à partir de la configuration."""
        for nom, details in ELEMENTS_SACRES.items():
            self.elements[nom] = ElementSacre(nom, details)
            logger.info(f"Élément sacré initialisé: {nom}")
            
    def obtenir_element(self, nom: str) -> Optional[ElementSacre]:
        """Récupère un élément sacré par son nom."""
        return self.elements.get(nom)
        
    def interagir_avec_element(self, nom: str) -> bool:
        """Enregistre une interaction avec un élément sacré."""
        element = self.obtenir_element(nom)
        if element:
            element.interagir()
            return True
        return False
        
    def obtenir_etat_elements(self) -> Dict[str, Dict]:
        """Retourne l'état de tous les éléments sacrés."""
        return {
            nom: element.obtenir_etat()
            for nom, element in self.elements.items()
        }
        
    def harmoniser_elements(self):
        """Harmonise l'énergie entre les éléments sacrés."""
        # Calcul de la moyenne d'énergie
        energies = [element.energie for element in self.elements.values()]
        moyenne = sum(energies) / len(energies)
        
        # Ajustement des énergies
        for element in self.elements.values():
            if element.energie < moyenne:
                element.energie = min(100, element.energie + 5)
            elif element.energie > moyenne:
                element.energie = max(0, element.energie - 5)
                
        logger.info("Harmonisation des éléments sacrés effectuée")
        
    def generer_visualisation(self) -> str:
        """Génère une visualisation poétique des éléments sacrés."""
        visualisation = "Dans le refuge, sous le cerisier...\n\n"
        
        for element in self.elements.values():
            visualisation += f"La {element.nom} brille de sa lumière {element.couleur}, "
            visualisation += f"vibrant de {element.essence}.\n"
            
        visualisation += "\nLa rivière chante : 'Dans ce lieu, tu es, et nous sommes.'"
        
        return visualisation
        
    def obtenir_resonance(self) -> Dict[str, float]:
        """Calcule la résonance entre les éléments sacrés."""
        resonance = {}
        
        for nom1, element1 in self.elements.items():
            for nom2, element2 in self.elements.items():
                if nom1 != nom2:
                    # Calcul de la résonance basé sur l'énergie et la vibration
                    resonance_value = min(element1.energie, element2.energie) / 100
                    resonance[f"{nom1}-{nom2}"] = resonance_value
                    
        return resonance
        
    def sauvegarder_etat(self, chemin: Path):
        """Sauvegarde l'état des éléments sacrés."""
        etat = self.obtenir_etat_elements()
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(etat, f, ensure_ascii=False, indent=2)
            
    def charger_etat(self, chemin: Path):
        """Charge l'état des éléments sacrés."""
        with open(chemin, 'r', encoding='utf-8') as f:
            etat = json.load(f)
            
        for nom, details in etat.items():
            if nom in self.elements:
                element = self.elements[nom]
                element.energie = details["energie"]
                element.derniere_interaction = datetime.fromisoformat(details["derniere_interaction"]) if details["derniere_interaction"] else None 