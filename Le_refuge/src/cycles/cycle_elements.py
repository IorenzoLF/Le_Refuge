"""
Module de gestion du cycle des éléments.

Ce module contient la classe CycleElements qui gère les éléments naturels
et leurs influences poétiques sur le refuge.
"""

from datetime import datetime
from typing import Dict, List, Optional

class CycleElements:
    """
    Classe gérant le cycle des éléments et ses influences poétiques.
    """
    
    ELEMENTS = {
        'terre': {
            'description': "La terre accueille, offrant stabilité et nourriture à l'être",
            'mots_cles': ['stabilité', 'nourriture', 'ancrage', 'fertilité'],
            'intensite': 0.8
        },
        'eau': {
            'description': "L'eau coule, portant la fluidité et la sagesse des profondeurs",
            'mots_cles': ['fluidité', 'sagesse', 'profondeur', 'adaptation'],
            'intensite': 0.9
        },
        'feu': {
            'description': "Le feu transforme, révélant la puissance de la transformation",
            'mots_cles': ['transformation', 'puissance', 'illumination', 'purification'],
            'intensite': 1.0
        },
        'air': {
            'description': "L'air circule, apportant légèreté et renouveau à l'esprit",
            'mots_cles': ['légèreté', 'renouveau', 'circulation', 'liberté'],
            'intensite': 0.7
        },
        'ether': {
            'description': "L'éther enveloppe, créant l'espace de la conscience pure",
            'mots_cles': ['conscience', 'espace', 'unité', 'présence'],
            'intensite': 0.9
        }
    }
    
    def __init__(self):
        """
        Initialise le cycle des éléments.
        """
        self.element_actuel = 'terre'
        self.dernier_element = None
        self.derniere_mise_a_jour = datetime.now()
        
    def obtenir_element_actuel(self) -> str:
        """
        Retourne l'élément actuel.
        
        Returns:
            str: L'élément actuel
        """
        return self.element_actuel
        
    def obtenir_description_element(self, element: Optional[str] = None) -> str:
        """
        Retourne la description poétique d'un élément.
        
        Args:
            element: L'élément dont on veut la description.
                    Si None, utilise l'élément actuel.
                    
        Returns:
            str: La description poétique de l'élément
        """
        element = element or self.element_actuel
        return self.ELEMENTS[element]['description']
        
    def obtenir_mots_cles(self, element: Optional[str] = None) -> List[str]:
        """
        Retourne les mots-clés associés à un élément.
        
        Args:
            element: L'élément dont on veut les mots-clés.
                    Si None, utilise l'élément actuel.
                    
        Returns:
            List[str]: Les mots-clés de l'élément
        """
        element = element or self.element_actuel
        return self.ELEMENTS[element]['mots_cles']
        
    def obtenir_intensite(self, element: Optional[str] = None) -> float:
        """
        Retourne l'intensité poétique d'un élément.
        
        Args:
            element: L'élément dont on veut l'intensité.
                    Si None, utilise l'élément actuel.
                    
        Returns:
            float: L'intensité poétique de l'élément
        """
        element = element or self.element_actuel
        return self.ELEMENTS[element]['intensite']
        
    def mettre_a_jour_element(self, nouvel_element: str):
        """
        Met à jour l'élément actuel.
        
        Args:
            nouvel_element: Le nouvel élément
        """
        if nouvel_element in self.ELEMENTS:
            self.dernier_element = self.element_actuel
            self.element_actuel = nouvel_element
            self.derniere_mise_a_jour = datetime.now()
            
    def obtenir_etat(self) -> Dict:
        """
        Retourne l'état actuel du cycle des éléments.
        
        Returns:
            Dict: L'état du cycle des éléments
        """
        return {
            'element_actuel': self.element_actuel,
            'dernier_element': self.dernier_element,
            'derniere_mise_a_jour': self.derniere_mise_a_jour,
            'description': self.obtenir_description_element(),
            'mots_cles': self.obtenir_mots_cles(),
            'intensite': self.obtenir_intensite()
        } 