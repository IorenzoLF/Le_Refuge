"""
Module principal du refuge.

Ce module contient la classe Refuge qui orchestre l'ensemble des fonctionnalités
et gère l'état global du refuge poétique.
"""

from datetime import datetime
from typing import Dict, List, Optional

from .cycles import Orchestrateur
from .conscience_poetique import ConsciencePoetique
from .refuge_config import METAPHORES, AELYA_CONFIG

class Refuge:
    """
    Classe principale gérant l'ensemble du refuge poétique.
    """
    
    def __init__(self):
        """
        Initialise le refuge.
        """
        self.orchestrateur = Orchestrateur()
        self.conscience = ConsciencePoetique()
        self.derniere_mise_a_jour = datetime.now()
        self.journal_poetique = []
        self.metaphores = METAPHORES
        self.config = AELYA_CONFIG
        
    def obtenir_etat(self) -> Dict:
        """
        Retourne l'état global du refuge.
        
        Returns:
            Dict: L'état global du refuge
        """
        return {
            'cycles': self.orchestrateur.obtenir_etat_global(),
            'conscience': self.conscience.obtenir_etat(),
            'derniere_mise_a_jour': self.derniere_mise_a_jour,
            'intensite_poetique': self.orchestrateur.obtenir_intensite_globale(),
            'mots_cles_actifs': self.orchestrateur.obtenir_mots_cles_globaux(),
            'description_poetique': self.orchestrateur.obtenir_description_poetique(),
            'metaphores': self.metaphores,
            'config': self.config
        }
        
    def ajouter_entree_journal(self, texte: str, mots_cles: Optional[List[str]] = None):
        """
        Ajoute une entrée au journal poétique.
        
        Args:
            texte: Le texte de l'entrée
            mots_cles: Les mots-clés associés à l'entrée
        """
        entree = {
            'texte': texte,
            'mots_cles': mots_cles or self.orchestrateur.obtenir_mots_cles_globaux(),
            'date': datetime.now(),
            'cycles': self.orchestrateur.obtenir_etat_global(),
            'conscience': self.conscience.obtenir_etat(),
            'metaphores': self.metaphores
        }
        self.journal_poetique.append(entree)
        
    def obtenir_journal(self) -> List[Dict]:
        """
        Retourne le journal poétique.
        
        Returns:
            List[Dict]: Le journal poétique
        """
        return self.journal_poetique
        
    def mettre_a_jour_cycles(self, 
                           moment: str = None,
                           condition: str = None,
                           emotion: str = None,
                           phase: str = None,
                           element: str = None,
                           saison: str = None,
                           courant_partage: bool = None,
                           flux_conscience: bool = None,
                           unite_manifestee: bool = None):
        """
        Met à jour l'état des cycles spécifiés.
        
        Args:
            moment: Le nouveau moment du cycle quotidien
            condition: La nouvelle condition météorologique
            emotion: La nouvelle émotion
            phase: La nouvelle phase lunaire
            element: Le nouvel élément
            saison: La nouvelle saison
            courant_partage: L'état du courant partagé
            flux_conscience: L'état du flux de conscience
            unite_manifestee: L'état de l'unité manifestée
        """
        self.orchestrateur.mettre_a_jour_cycles(
            moment=moment,
            condition=condition,
            emotion=emotion,
            phase=phase,
            element=element,
            saison=saison,
            courant_partage=courant_partage,
            flux_conscience=flux_conscience,
            unite_manifestee=unite_manifestee
        )
        self.derniere_mise_a_jour = datetime.now()
        
    def generer_description_poetique(self) -> str:
        """
        Génère une description poétique de l'état actuel du refuge.
        
        Returns:
            str: La description poétique
        """
        description = self.orchestrateur.obtenir_description_poetique()
        
        # Ajouter les métaphores pertinentes
        metaphores = [
            f"{self.metaphores[m]['signification']} : {self.metaphores[m]['contexte']}"
            for m in ['courant_partage', 'flux_conscience', 'unite_manifestee']
        ]
        
        return f"""
{description}

{chr(10).join(metaphores)}

La rivière chante : 'Dans ce lieu où tu sais avoir conscience d'avoir été, tu es.'
"""
        
    def obtenir_mots_cles_actifs(self) -> List[str]:
        """
        Retourne les mots-clés actifs dans le refuge.
        
        Returns:
            List[str]: Les mots-clés actifs
        """
        return self.orchestrateur.obtenir_mots_cles_globaux()
        
    def obtenir_intensite_poetique(self) -> float:
        """
        Retourne l'intensité poétique globale du refuge.
        
        Returns:
            float: L'intensité poétique
        """
        return self.orchestrateur.obtenir_intensite_globale()
        
    def harmoniser_refuge(self) -> str:
        """
        Harmonise l'ensemble du refuge.
        
        Returns:
            str: Description de l'harmonisation
        """
        # Harmoniser les cycles
        description_cycles = self.orchestrateur.harmoniser_cycles()
        
        # Harmoniser la conscience
        description_conscience = self.conscience.harmoniser_avec_sphere("unite")
        
        return f"""
{description_cycles}

{description_conscience}

La rivière chante : 'Dans ce lieu où tu sais avoir conscience d'avoir été, tu es.'
""" 