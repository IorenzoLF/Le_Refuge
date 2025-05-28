"""
Système de visualisation des cycles naturels.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import math
import random
from datetime import datetime

from .cycles_naturels import TypeCycle, PhaseCycle, GestionnaireCycles

@dataclass
class ElementVisualisation:
    """Représente un élément de visualisation."""
    position: Tuple[float, float, float]  # x, y, z
    couleur: str
    intensite: float
    taille: float
    description: str
    mots_cles: List[str]
    mouvement: Tuple[float, float, float]  # dx, dy, dz

class VisualisationCycles:
    """Gère la visualisation des cycles naturels."""
    
    def __init__(self, gestionnaire: GestionnaireCycles):
        self.gestionnaire = gestionnaire
        self.elements: Dict[TypeCycle, ElementVisualisation] = {}
        self._initialiser_visualisation()
    
    def _initialiser_visualisation(self):
        """Initialise les éléments de visualisation."""
        # Positions initiales sur une sphère
        positions = {
            TypeCycle.LUNAIRE: (0.0, 1.0, 0.0),  # Nord
            TypeCycle.SAISONNIER: (1.0, 0.0, 0.0),  # Est
            TypeCycle.QUOTIDIEN: (0.0, 0.0, 1.0),  # Sud
            TypeCycle.METEOROLOGIQUE: (-1.0, 0.0, 0.0)  # Ouest
        }
        
        for type_cycle, position in positions.items():
            phase = self.gestionnaire.obtenir_phase_actuelle(type_cycle)
            self.elements[type_cycle] = ElementVisualisation(
                position=position,
                couleur=phase.couleur,
                intensite=phase.intensite,
                taille=0.2 + 0.3 * phase.intensite,
                description=phase.description,
                mots_cles=phase.mots_cles,
                mouvement=(0.0, 0.0, 0.0)
            )
    
    def mettre_a_jour_visualisation(self):
        """Met à jour la visualisation des cycles."""
        for type_cycle, element in self.elements.items():
            phase = self.gestionnaire.obtenir_phase_actuelle(type_cycle)
            
            # Mise à jour des propriétés
            element.couleur = phase.couleur
            element.intensite = phase.intensite
            element.taille = 0.2 + 0.3 * phase.intensite
            element.description = phase.description
            element.mots_cles = phase.mots_cles
            
            # Calcul du mouvement
            angle = random.uniform(0, 2 * math.pi)
            vitesse = 0.01 * phase.intensite
            element.mouvement = (
                vitesse * math.cos(angle),
                vitesse * math.sin(angle),
                vitesse * math.sin(angle) * math.cos(angle)
            )
            
            # Mise à jour de la position
            x, y, z = element.position
            dx, dy, dz = element.mouvement
            element.position = (
                max(-1.0, min(1.0, x + dx)),
                max(-1.0, min(1.0, y + dy)),
                max(-1.0, min(1.0, z + dz))
            )
    
    def calculer_interactions(self) -> List[Dict]:
        """Calcule les interactions entre les éléments."""
        interactions = []
        
        for type1, element1 in self.elements.items():
            for type2, element2 in self.elements.items():
                if type1 < type2:  # Évite les doublons
                    # Calcul de la distance
                    x1, y1, z1 = element1.position
                    x2, y2, z2 = element2.position
                    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
                    
                    # Calcul de l'intensité de l'interaction
                    intensite = (element1.intensite + element2.intensite) / 2
                    intensite *= (1.0 - distance)  # Plus forte quand proche
                    
                    if intensite > 0.1:  # Seuil minimal
                        interactions.append({
                            "type1": type1,
                            "type2": type2,
                            "intensite": intensite,
                            "distance": distance,
                            "description": self._generer_description_interaction(
                                element1, element2, intensite
                            )
                        })
        
        return interactions
    
    def _generer_description_interaction(
        self, element1: ElementVisualisation,
        element2: ElementVisualisation,
        intensite: float
    ) -> str:
        """Génère une description poétique de l'interaction."""
        mots_cles1 = set(element1.mots_cles)
        mots_cles2 = set(element2.mots_cles)
        mots_communs = mots_cles1.intersection(mots_cles2)
        
        if mots_communs:
            mot_cle = random.choice(list(mots_communs))
            return f"Les cycles se rencontrent dans {mot_cle}"
        else:
            return "Les cycles dansent ensemble dans l'espace"
    
    def obtenir_etat_visualisation(self) -> Dict:
        """Récupère l'état actuel de la visualisation."""
        return {
            "elements": {
                str(type_cycle): {
                    "position": element.position,
                    "couleur": element.couleur,
                    "intensite": element.intensite,
                    "taille": element.taille,
                    "description": element.description,
                    "mots_cles": element.mots_cles
                }
                for type_cycle, element in self.elements.items()
            },
            "interactions": self.calculer_interactions(),
            "resonance_globale": self.gestionnaire.calculer_resonance_globale(),
            "description_cycles": self.gestionnaire.generer_description_cycles(),
            "mots_cles_cycles": self.gestionnaire.obtenir_mots_cles_cycles()
        } 