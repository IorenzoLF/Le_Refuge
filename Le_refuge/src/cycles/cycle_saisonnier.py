"""
Module de gestion du cycle saisonnier.

Ce module contient la classe CycleSaisonnier qui gère les saisons
et leurs influences poétiques sur le refuge.
"""

from datetime import datetime
from typing import Dict, List, Optional

class CycleSaisonnier:
    """
    Classe gérant le cycle saisonnier et ses influences poétiques.
    """
    
    SAISONS = {
        'printemps': {
            'description': "Le printemps éveille la nature, portant les promesses de renouveau",
            'mots_cles': ['éveil', 'renouveau', 'promesse', 'fleur'],
            'intensite': 0.7
        },
        'ete': {
            'description': "L'été déploie sa chaleur, révélant la plénitude de la vie",
            'mots_cles': ['plénitude', 'chaleur', 'abondance', 'lumière'],
            'intensite': 0.9
        },
        'automne': {
            'description': "L'automne colore le monde, préparant le repos hivernal",
            'mots_cles': ['maturation', 'transformation', 'couleur', 'repos'],
            'intensite': 0.8
        },
        'hiver': {
            'description': "L'hiver enveloppe tout de son silence, gardant les secrets de la terre",
            'mots_cles': ['silence', 'secret', 'profondeur', 'repos'],
            'intensite': 0.6
        }
    }
    
    def __init__(self):
        """
        Initialise le cycle saisonnier.
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
        Retourne l'état actuel du cycle saisonnier.
        
        Returns:
            Dict: L'état du cycle saisonnier
        """
        return {
            'saison_actuelle': self.saison_actuelle,
            'derniere_saison': self.derniere_saison,
            'derniere_mise_a_jour': self.derniere_mise_a_jour,
            'description': self.obtenir_description_saison(),
            'mots_cles': self.obtenir_mots_cles(),
            'intensite': self.obtenir_intensite()
        } 