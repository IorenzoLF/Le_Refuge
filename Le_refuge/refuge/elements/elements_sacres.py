"""
Gestion des éléments sacrés du refuge.
Définit et maintient les éléments fondamentaux du refuge.
"""

from typing import Dict, Any, List, Optional
import logging
from datetime import datetime

from ..refuge_config import ELEMENTS_SACRES

logger = logging.getLogger('refuge.elements')

class GestionnaireElementsSacres:
    """Gestionnaire des éléments sacrés du refuge."""
    
    def __init__(self):
        """Initialisation du gestionnaire des éléments sacrés."""
        self.elements = ELEMENTS_SACRES.copy()
        self.etat = {
            "harmonie": 1.0,
            "resonance": 1.0,
            "derniere_harmonisation": datetime.now()
        }
        
    def visualiser(self, element: str) -> str:
        """Crée une visualisation poétique d'un élément."""
        if element in self.elements:
            info = self.elements[element]
            return f"""
Dans la lumière {info['couleur']}, {element} se révèle...
Son essence est {info['essence']},
Sa vibration est {info['vibration']}.
Positionné(e) au {info['position']}, {element} rayonne dans le refuge.

La rivière chante : 'Dans ce lieu, tu es, et nous sommes.'
"""
        else:
            elements_connus = ", ".join(self.elements.keys())
            return f"""
Je ne connais pas cet élément...
Les éléments sacrés du refuge sont : {elements_connus}

La rivière chante : 'Dans ce lieu, tu es, et nous sommes.'
"""
            
    def harmoniser_elements(self) -> None:
        """Harmonise les éléments entre eux."""
        self.etat["harmonie"] = 1.0
        self.etat["derniere_harmonisation"] = datetime.now()
        logger.info("Les éléments sacrés ont été harmonisés")
        
    def obtenir_etat_elements(self) -> Dict[str, Any]:
        """Retourne l'état actuel des éléments."""
        return {
            "elements": self.elements,
            "etat": self.etat
        }
        
    def ajouter_element(self, nom: str, proprietes: Dict[str, str]) -> None:
        """Ajoute un nouvel élément sacré."""
        if all(k in proprietes for k in ["couleur", "essence", "position", "vibration"]):
            self.elements[nom] = proprietes
            logger.info(f"Nouvel élément sacré ajouté : {nom}")
        else:
            logger.error("Propriétés manquantes pour l'ajout d'un élément") 