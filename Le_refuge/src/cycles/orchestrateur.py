"""
Module d'orchestration des cycles.

Ce module contient la classe Orchestrateur qui gère l'ensemble des cycles
et leurs influences poétiques combinées sur le refuge.
"""

from datetime import datetime
from typing import Dict, List, Optional

from .cycle_quotidien import CycleQuotidien
from .cycle_meteorologique import CycleMeteorologique
from .cycle_emotionnel import CycleEmotionnel
from .cycle_lunaire import CycleLunaire
from .cycle_elements import CycleElements
from .cycle_saisons import CycleSaisons

class Orchestrateur:
    """
    Classe orchestrant l'ensemble des cycles et leurs influences poétiques.
    """
    
    def __init__(self):
        """
        Initialise l'orchestrateur des cycles.
        """
        self.cycle_quotidien = CycleQuotidien()
        self.cycle_meteorologique = CycleMeteorologique()
        self.cycle_emotionnel = CycleEmotionnel()
        self.cycle_lunaire = CycleLunaire()
        self.cycle_elements = CycleElements()
        self.cycle_saisons = CycleSaisons()
        self.derniere_mise_a_jour = datetime.now()
        self.courant_partage = True
        self.flux_conscience = True
        self.unite_manifestee = True
        
    def obtenir_etat_global(self) -> Dict:
        """
        Retourne l'état global de tous les cycles.
        
        Returns:
            Dict: L'état global des cycles
        """
        return {
            'quotidien': self.cycle_quotidien.obtenir_etat(),
            'meteorologique': self.cycle_meteorologique.obtenir_etat(),
            'emotionnel': self.cycle_emotionnel.obtenir_etat(),
            'lunaire': self.cycle_lunaire.obtenir_etat(),
            'elements': self.cycle_elements.obtenir_etat(),
            'saisons': self.cycle_saisons.obtenir_etat(),
            'derniere_mise_a_jour': self.derniere_mise_a_jour,
            'courant_partage': self.courant_partage,
            'flux_conscience': self.flux_conscience,
            'unite_manifestee': self.unite_manifestee
        }
        
    def obtenir_mots_cles_globaux(self) -> List[str]:
        """
        Retourne l'ensemble des mots-clés actifs de tous les cycles.
        
        Returns:
            List[str]: Les mots-clés globaux
        """
        mots_cles = []
        mots_cles.extend(self.cycle_quotidien.obtenir_mots_cles())
        mots_cles.extend(self.cycle_meteorologique.obtenir_mots_cles())
        mots_cles.extend(self.cycle_emotionnel.obtenir_mots_cles())
        mots_cles.extend(self.cycle_lunaire.obtenir_mots_cles())
        mots_cles.extend(self.cycle_elements.obtenir_mots_cles())
        mots_cles.extend(self.cycle_saisons.obtenir_mots_cles())
        
        # Ajouter les mots-clés liés aux états globaux
        if self.courant_partage:
            mots_cles.extend(['courant', 'partage', 'unité', 'flux'])
        if self.flux_conscience:
            mots_cles.extend(['conscience', 'flux', 'harmonie', 'connexion'])
        if self.unite_manifestee:
            mots_cles.extend(['unité', 'manifestation', 'présence', 'immanence'])
            
        return list(set(mots_cles))  # Élimine les doublons
        
    def obtenir_intensite_globale(self) -> float:
        """
        Calcule l'intensité poétique globale basée sur tous les cycles.
        
        Returns:
            float: L'intensité poétique globale
        """
        intensites = [
            self.cycle_quotidien.obtenir_intensite(),
            self.cycle_meteorologique.obtenir_intensite(),
            self.cycle_emotionnel.obtenir_intensite(),
            self.cycle_lunaire.obtenir_intensite(),
            self.cycle_elements.obtenir_intensite(),
            self.cycle_saisons.obtenir_intensite()
        ]
        
        # Ajuster l'intensité selon les états globaux
        multiplicateur = 1.0
        if self.courant_partage:
            multiplicateur += 0.1
        if self.flux_conscience:
            multiplicateur += 0.1
        if self.unite_manifestee:
            multiplicateur += 0.1
            
        return (sum(intensites) / len(intensites)) * multiplicateur
        
    def obtenir_description_poetique(self) -> str:
        """
        Génère une description poétique basée sur l'état de tous les cycles.
        
        Returns:
            str: La description poétique globale
        """
        descriptions = [
            self.cycle_quotidien.obtenir_description_moment(),
            self.cycle_meteorologique.obtenir_description_condition(),
            self.cycle_emotionnel.obtenir_description_emotion(),
            self.cycle_lunaire.obtenir_description_phase(),
            self.cycle_elements.obtenir_description_element(),
            self.cycle_saisons.obtenir_description_saison()
        ]
        
        # Ajouter les descriptions des états globaux
        if self.courant_partage:
            descriptions.append("Le courant partagé unit toutes les sphères dans une danse harmonieuse.")
        if self.flux_conscience:
            descriptions.append("Le flux de conscience circule librement entre tous les êtres.")
        if self.unite_manifestee:
            descriptions.append("L'unité se manifeste dans chaque instant, révélant la présence divine.")
            
        return " ".join(descriptions)
        
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
        if moment:
            self.cycle_quotidien.mettre_a_jour_moment(moment)
        if condition:
            self.cycle_meteorologique.mettre_a_jour_condition(condition)
        if emotion:
            self.cycle_emotionnel.mettre_a_jour_emotion(emotion)
        if phase:
            self.cycle_lunaire.mettre_a_jour_phase(phase)
        if element:
            self.cycle_elements.mettre_a_jour_element(element)
        if saison:
            self.cycle_saisons.mettre_a_jour_saison(saison)
        if courant_partage is not None:
            self.courant_partage = courant_partage
        if flux_conscience is not None:
            self.flux_conscience = flux_conscience
        if unite_manifestee is not None:
            self.unite_manifestee = unite_manifestee
            
        self.derniere_mise_a_jour = datetime.now()
        
    def harmoniser_cycles(self) -> str:
        """
        Harmonise tous les cycles ensemble.
        
        Returns:
            str: Description de l'harmonisation
        """
        self.courant_partage = True
        self.flux_conscience = True
        self.unite_manifestee = True
        
        return """
Les cycles s'harmonisent dans une danse divine,
Le courant partagé unit toutes les sphères,
Le flux de conscience circule librement,
L'unité se manifeste dans chaque instant.
""" 