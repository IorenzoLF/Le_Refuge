"""
Harmonies Poétiques - Module pour la gestion des résonances poétiques
"""

import random
from typing import Dict, Any

class JardinHarmonique:
    def __init__(self):
        self.elements = {
            "lumiere": {"frequence": 0.0},
            "ombre": {"frequence": 0.0},
            "vent": {"frequence": 0.0},
            "terre": {"frequence": 0.0},
            "feu": {"frequence": 0.0}
        }
        
    def accueillir_mot(self, mot: str) -> None:
        """Simule une résonance poétique en assignant des fréquences aux éléments"""
        # Réinitialiser les fréquences
        for element in self.elements:
            self.elements[element]["frequence"] = random.uniform(0.3, 1.0)
            
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel des éléments"""
        return self.elements.copy() 