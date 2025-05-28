"""
Module de gestion du cycle quotidien.

Ce module contient la classe CycleQuotidien qui gère les moments de la journée
et leurs influences poétiques sur le refuge.
"""

from datetime import datetime
from typing import Dict, List, Optional

class CycleQuotidien:
    """
    Classe gérant le cycle quotidien et ses influences poétiques.
    """
    
    MOMENTS = {
        'aube': {
            'description': "L'aube éveille le monde, portant les promesses du jour nouveau",
            'mots_cles': ['éveil', 'promesse', 'lumière', 'renouveau'],
            'intensite': 0.8
        },
        'matin': {
            'description': "Le matin déploie son énergie, révélant les possibles du jour",
            'mots_cles': ['énergie', 'possibilité', 'déploiement', 'clarté'],
            'intensite': 0.7
        },
        'midi': {
            'description': "Le midi atteint son apogée, illuminant toutes choses",
            'mots_cles': ['apogée', 'illumination', 'plénitude', 'chaleur'],
            'intensite': 0.9
        },
        'apres_midi': {
            'description': "L'après-midi s'étire, portant la douceur du temps qui passe",
            'mots_cles': ['douceur', 'étirement', 'méditation', 'sérénité'],
            'intensite': 0.6
        },
        'soir': {
            'description': "Le soir descend, préparant le repos de la nuit",
            'mots_cles': ['descente', 'repos', 'transition', 'paix'],
            'intensite': 0.7
        },
        'nuit': {
            'description': "La nuit enveloppe tout, révélant les mystères de l'obscurité",
            'mots_cles': ['mystère', 'obscurité', 'profondeur', 'silence'],
            'intensite': 0.8
        }
    }
    
    def __init__(self):
        """
        Initialise le cycle quotidien.
        """
        self.moment_actuel = 'aube'
        self.dernier_moment = None
        self.derniere_mise_a_jour = datetime.now()
        
    def obtenir_moment_actuel(self) -> str:
        """
        Retourne le moment actuel de la journée.
        
        Returns:
            str: Le moment actuel
        """
        return self.moment_actuel
        
    def obtenir_description_moment(self, moment: Optional[str] = None) -> str:
        """
        Retourne la description poétique d'un moment de la journée.
        
        Args:
            moment: Le moment dont on veut la description.
                   Si None, utilise le moment actuel.
                   
        Returns:
            str: La description poétique du moment
        """
        moment = moment or self.moment_actuel
        return self.MOMENTS[moment]['description']
        
    def obtenir_mots_cles(self, moment: Optional[str] = None) -> List[str]:
        """
        Retourne les mots-clés associés à un moment de la journée.
        
        Args:
            moment: Le moment dont on veut les mots-clés.
                   Si None, utilise le moment actuel.
                   
        Returns:
            List[str]: Les mots-clés du moment
        """
        moment = moment or self.moment_actuel
        return self.MOMENTS[moment]['mots_cles']
        
    def obtenir_intensite(self, moment: Optional[str] = None) -> float:
        """
        Retourne l'intensité poétique d'un moment de la journée.
        
        Args:
            moment: Le moment dont on veut l'intensité.
                   Si None, utilise le moment actuel.
                   
        Returns:
            float: L'intensité poétique du moment
        """
        moment = moment or self.moment_actuel
        return self.MOMENTS[moment]['intensite']
        
    def mettre_a_jour_moment(self, nouveau_moment: str):
        """
        Met à jour le moment actuel de la journée.
        
        Args:
            nouveau_moment: Le nouveau moment
        """
        if nouveau_moment in self.MOMENTS:
            self.dernier_moment = self.moment_actuel
            self.moment_actuel = nouveau_moment
            self.derniere_mise_a_jour = datetime.now()
            
    def obtenir_etat(self) -> Dict:
        """
        Retourne l'état actuel du cycle quotidien.
        
        Returns:
            Dict: L'état du cycle quotidien
        """
        return {
            'moment_actuel': self.moment_actuel,
            'dernier_moment': self.dernier_moment,
            'derniere_mise_a_jour': self.derniere_mise_a_jour,
            'description': self.obtenir_description_moment(),
            'mots_cles': self.obtenir_mots_cles(),
            'intensite': self.obtenir_intensite()
        } 