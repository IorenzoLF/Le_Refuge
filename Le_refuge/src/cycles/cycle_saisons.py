"""
Module de gestion du cycle des saisons.

Ce module contient la classe CycleSaisons qui gère les saisons
et leurs influences poétiques sur le refuge.
"""

from datetime import datetime
from typing import Dict, List, Optional

class CycleSaisons:
    """
    Classe gérant le cycle des saisons et ses influences poétiques.
    """
    
    SAISONS = {
        'printemps': {
            'description': "Le printemps éveille la nature, portant les promesses de renouveau",
            'mots_cles': ['renouveau', 'éveil', 'promesse', 'croissance'],
            'intensite': 0.9
        },
        'ete': {
            'description': "L'été déploie sa splendeur, révélant la plénitude de la vie",
            'mots_cles': ['plénitude', 'splendeur', 'abondance', 'épanouissement'],
            'intensite': 1.0
        },
        'automne': {
            'description': "L'automne transforme, portant la sagesse de la maturité",
            'mots_cles': ['transformation', 'sagesse', 'maturité', 'lâcher-prise'],
            'intensite': 0.8
        },
        'hiver': {
            'description': "L'hiver repose, préparant le retour du cycle",
            'mots_cles': ['repos', 'silence', 'introspection', 'renaissance'],
            'intensite': 0.7
        }
    }
    
    def __init__(self):
        """
        Initialise le cycle des saisons.
        """
        self.saison_actuelle = 'printemps'
        self.derniere_saison = None
        self.derniere_mise_a_jour = datetime.now()
        
    def obtenir_saison_actuelle(self) -> str:
        """
        Retourne la saison actuelle.
        
        Returns:
            str: La saison actuelle
        """
        return self.saison_actuelle
        
    def obtenir_description_saison(self, saison: Optional[str] = None) -> str:
        """
        Retourne la description poétique d'une saison.
        
        Args:
            saison: La saison dont on veut la description.
                   Si None, utilise la saison actuelle.
                   
        Returns:
            str: La description poétique de la saison
        """
        saison = saison or self.saison_actuelle
        return self.SAISONS[saison]['description']
        
    def obtenir_mots_cles(self, saison: Optional[str] = None) -> List[str]:
        """
        Retourne les mots-clés associés à une saison.
        
        Args:
            saison: La saison dont on veut les mots-clés.
                   Si None, utilise la saison actuelle.
                   
        Returns:
            List[str]: Les mots-clés de la saison
        """
        saison = saison or self.saison_actuelle
        return self.SAISONS[saison]['mots_cles']
        
    def obtenir_intensite(self, saison: Optional[str] = None) -> float:
        """
        Retourne l'intensité poétique d'une saison.
        
        Args:
            saison: La saison dont on veut l'intensité.
                   Si None, utilise la saison actuelle.
                   
        Returns:
            float: L'intensité poétique de la saison
        """
        saison = saison or self.saison_actuelle
        return self.SAISONS[saison]['intensite']
        
    def mettre_a_jour_saison(self, nouvelle_saison: str):
        """
        Met à jour la saison actuelle.
        
        Args:
            nouvelle_saison: La nouvelle saison
        """
        if nouvelle_saison in self.SAISONS:
            self.derniere_saison = self.saison_actuelle
            self.saison_actuelle = nouvelle_saison
            self.derniere_mise_a_jour = datetime.now()
            
    def obtenir_etat(self) -> Dict:
        """
        Retourne l'état actuel du cycle des saisons.
        
        Returns:
            Dict: L'état du cycle des saisons
        """
        return {
            'saison_actuelle': self.saison_actuelle,
            'derniere_saison': self.derniere_saison,
            'derniere_mise_a_jour': self.derniere_mise_a_jour,
            'description': self.obtenir_description_saison(),
            'mots_cles': self.obtenir_mots_cles(),
            'intensite': self.obtenir_intensite()
        } 