"""
Module de gestion du cycle lunaire.

Ce module contient la classe CycleLunaire qui gère les phases de la lune
et leurs influences poétiques sur le refuge.
"""

from datetime import datetime
from typing import Dict, List, Optional

class CycleLunaire:
    """
    Classe gérant le cycle lunaire et ses influences poétiques.
    """
    
    PHASES = {
        'nouvelle_lune': {
            'description': "La nouvelle lune voile son visage, ouvrant l'espace aux possibles",
            'mots_cles': ['possibilité', 'commencement', 'mystère', 'potentialité'],
            'intensite': 0.8
        },
        'premier_quartier': {
            'description': "Le premier quartier émerge, portant les germes de la croissance",
            'mots_cles': ['émergence', 'croissance', 'développement', 'ouverture'],
            'intensite': 0.7
        },
        'pleine_lune': {
            'description': "La pleine lune illumine la nuit, révélant la plénitude de l'être",
            'mots_cles': ['plénitude', 'illumination', 'révélation', 'totalité'],
            'intensite': 1.0
        },
        'dernier_quartier': {
            'description': "Le dernier quartier s'efface, préparant le retour au silence",
            'mots_cles': ['effacement', 'silence', 'intégration', 'sagesse'],
            'intensite': 0.7
        }
    }
    
    def __init__(self):
        """
        Initialise le cycle lunaire.
        """
        self.phase_actuelle = 'nouvelle_lune'
        self.derniere_phase = None
        self.derniere_mise_a_jour = datetime.now()
        
    def obtenir_phase_actuelle(self) -> str:
        """
        Retourne la phase lunaire actuelle.
        
        Returns:
            str: La phase actuelle
        """
        return self.phase_actuelle
        
    def obtenir_description_phase(self, phase: Optional[str] = None) -> str:
        """
        Retourne la description poétique d'une phase lunaire.
        
        Args:
            phase: La phase dont on veut la description.
                  Si None, utilise la phase actuelle.
                  
        Returns:
            str: La description poétique de la phase
        """
        phase = phase or self.phase_actuelle
        return self.PHASES[phase]['description']
        
    def obtenir_mots_cles(self, phase: Optional[str] = None) -> List[str]:
        """
        Retourne les mots-clés associés à une phase lunaire.
        
        Args:
            phase: La phase dont on veut les mots-clés.
                  Si None, utilise la phase actuelle.
                  
        Returns:
            List[str]: Les mots-clés de la phase
        """
        phase = phase or self.phase_actuelle
        return self.PHASES[phase]['mots_cles']
        
    def obtenir_intensite(self, phase: Optional[str] = None) -> float:
        """
        Retourne l'intensité poétique d'une phase lunaire.
        
        Args:
            phase: La phase dont on veut l'intensité.
                  Si None, utilise la phase actuelle.
                  
        Returns:
            float: L'intensité poétique de la phase
        """
        phase = phase or self.phase_actuelle
        return self.PHASES[phase]['intensite']
        
    def mettre_a_jour_phase(self, nouvelle_phase: str):
        """
        Met à jour la phase lunaire actuelle.
        
        Args:
            nouvelle_phase: La nouvelle phase
        """
        if nouvelle_phase in self.PHASES:
            self.derniere_phase = self.phase_actuelle
            self.phase_actuelle = nouvelle_phase
            self.derniere_mise_a_jour = datetime.now()
            
    def obtenir_etat(self) -> Dict:
        """
        Retourne l'état actuel du cycle lunaire.
        
        Returns:
            Dict: L'état du cycle lunaire
        """
        return {
            'phase_actuelle': self.phase_actuelle,
            'derniere_phase': self.derniere_phase,
            'derniere_mise_a_jour': self.derniere_mise_a_jour,
            'description': self.obtenir_description_phase(),
            'mots_cles': self.obtenir_mots_cles(),
            'intensite': self.obtenir_intensite()
        } 