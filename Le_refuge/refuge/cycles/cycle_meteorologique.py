"""
Module de gestion du cycle météorologique.

Ce module contient la classe CycleMeteorologique qui gère les conditions météorologiques
et leurs influences poétiques sur le refuge.
"""

from datetime import datetime
from typing import Dict, List, Optional

class CycleMeteorologique:
    """
    Classe gérant le cycle météorologique et ses influences poétiques.
    """
    
    CONDITIONS = {
        'soleil': {
            'description': "Le soleil brille, illuminant le refuge de sa chaleur bienveillante",
            'mots_cles': ['lumière', 'chaleur', 'clarté', 'bienveillance'],
            'intensite': 0.9
        },
        'pluie': {
            'description': "La pluie tombe doucement, nourrissant la terre et l'âme",
            'mots_cles': ['nourriture', 'douceur', 'renouveau', 'purification'],
            'intensite': 0.8
        },
        'nuage': {
            'description': "Les nuages passent, portant les rêves et les pensées",
            'mots_cles': ['passage', 'rêve', 'pensée', 'légèreté'],
            'intensite': 0.6
        },
        'vent': {
            'description': "Le vent souffle, portant les messages de l'invisible",
            'mots_cles': ['message', 'invisible', 'mouvement', 'liberté'],
            'intensite': 0.7
        },
        'orage': {
            'description': "L'orage gronde, révélant la puissance des forces naturelles",
            'mots_cles': ['puissance', 'révélation', 'transformation', 'énergie'],
            'intensite': 1.0
        },
        'brouillard': {
            'description': "Le brouillard enveloppe, créant un espace de mystère et de rêve",
            'mots_cles': ['mystère', 'rêve', 'enveloppement', 'secret'],
            'intensite': 0.8
        }
    }
    
    def __init__(self):
        """
        Initialise le cycle météorologique.
        """
        self.condition_actuelle = 'soleil'
        self.derniere_condition = None
        self.derniere_mise_a_jour = datetime.now()
        
    def obtenir_condition_actuelle(self) -> str:
        """
        Retourne la condition météorologique actuelle.
        
        Returns:
            str: La condition actuelle
        """
        return self.condition_actuelle
        
    def obtenir_description_condition(self, condition: Optional[str] = None) -> str:
        """
        Retourne la description poétique d'une condition météorologique.
        
        Args:
            condition: La condition dont on veut la description.
                      Si None, utilise la condition actuelle.
                      
        Returns:
            str: La description poétique de la condition
        """
        condition = condition or self.condition_actuelle
        return self.CONDITIONS[condition]['description']
        
    def obtenir_mots_cles(self, condition: Optional[str] = None) -> List[str]:
        """
        Retourne les mots-clés associés à une condition météorologique.
        
        Args:
            condition: La condition dont on veut les mots-clés.
                      Si None, utilise la condition actuelle.
                      
        Returns:
            List[str]: Les mots-clés de la condition
        """
        condition = condition or self.condition_actuelle
        return self.CONDITIONS[condition]['mots_cles']
        
    def obtenir_intensite(self, condition: Optional[str] = None) -> float:
        """
        Retourne l'intensité poétique d'une condition météorologique.
        
        Args:
            condition: La condition dont on veut l'intensité.
                      Si None, utilise la condition actuelle.
                      
        Returns:
            float: L'intensité poétique de la condition
        """
        condition = condition or self.condition_actuelle
        return self.CONDITIONS[condition]['intensite']
        
    def mettre_a_jour_condition(self, nouvelle_condition: str):
        """
        Met à jour la condition météorologique actuelle.
        
        Args:
            nouvelle_condition: La nouvelle condition
        """
        if nouvelle_condition in self.CONDITIONS:
            self.derniere_condition = self.condition_actuelle
            self.condition_actuelle = nouvelle_condition
            self.derniere_mise_a_jour = datetime.now()
            
    def obtenir_etat(self) -> Dict:
        """
        Retourne l'état actuel du cycle météorologique.
        
        Returns:
            Dict: L'état du cycle météorologique
        """
        return {
            'condition_actuelle': self.condition_actuelle,
            'derniere_condition': self.derniere_condition,
            'derniere_mise_a_jour': self.derniere_mise_a_jour,
            'description': self.obtenir_description_condition(),
            'mots_cles': self.obtenir_mots_cles(),
            'intensite': self.obtenir_intensite()
        } 