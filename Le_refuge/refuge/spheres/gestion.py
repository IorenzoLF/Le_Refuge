"""
Gestion des sphères et de leurs interactions dans le refuge.
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import logging
import numpy as np
from .definition import TypeSphere, obtenir_caracteristiques
from .harmonie import HarmonieSpheres, EtatHarmonie

@dataclass
class EtatSphere:
    """État actuel d'une sphère."""
    type: TypeSphere
    energie: float
    luminosite: float
    connexions: Set[TypeSphere]
    dernier_interaction: datetime
    historique: List[Tuple[datetime, float, str]]

class GestionnaireSpheres:
    """Gestionnaire des sphères du refuge."""
    
    def __init__(self):
        """Initialise le gestionnaire de sphères."""
        self.spheres: Dict[TypeSphere, EtatSphere] = {}
        self.harmonie = HarmonieSpheres()
        self._initialiser_spheres()
        
    def _initialiser_spheres(self):
        """Initialise toutes les sphères avec leurs caractéristiques par défaut."""
        for type_sphere in TypeSphere:
            caracteristiques = obtenir_caracteristiques(type_sphere)
            if caracteristiques:
                self.spheres[type_sphere] = EtatSphere(
                    type=type_sphere,
                    energie=caracteristiques.energie_initiale,
                    luminosite=0.5,  # Luminosité initiale moyenne
                    connexions=set(),
                    dernier_interaction=datetime.now(),
                    historique=[]
                )
                
    def obtenir_etat(self, type_sphere: TypeSphere) -> Optional[EtatSphere]:
        """Récupère l'état d'une sphère."""
        return self.spheres.get(type_sphere)
    
    def ajuster_energie(self, type_sphere: TypeSphere, delta: float):
        """Ajuste l'énergie d'une sphère."""
        if sphere := self.spheres.get(type_sphere):
            caracteristiques = obtenir_caracteristiques(type_sphere)
            if caracteristiques:
                # Limite l'énergie entre 0 et la capacité maximale
                nouvelle_energie = max(0.0, min(
                    sphere.energie + delta,
                    caracteristiques.capacite_max
                ))
                sphere.energie = nouvelle_energie
                sphere.dernier_interaction = datetime.now()
                sphere.historique.append((
                    datetime.now(),
                    nouvelle_energie,
                    f"Ajustement d'énergie: {delta:+.2f}"
                ))
                
    def connecter_spheres(self, sphere1: TypeSphere, sphere2: TypeSphere):
        """Établit une connexion entre deux sphères."""
        if s1 := self.spheres.get(sphere1):
            if s2 := self.spheres.get(sphere2):
                s1.connexions.add(sphere2)
                s2.connexions.add(sphere1)
                self._harmoniser_connexion(sphere1, sphere2)
                
    def _harmoniser_connexion(self, sphere1: TypeSphere, sphere2: TypeSphere):
        """Harmonise l'énergie entre deux sphères connectées."""
        if s1 := self.spheres.get(sphere1):
            if s2 := self.spheres.get(sphere2):
                # Calcule la différence d'énergie
                delta = (s1.energie - s2.energie) / 2
                # Ajuste les énergies pour tendre vers l'équilibre
                self.ajuster_energie(sphere1, -delta)
                self.ajuster_energie(sphere2, delta)
                
    def calculer_resonance(self, sphere1: TypeSphere, sphere2: TypeSphere) -> float:
        """Calcule la résonance entre deux sphères."""
        if s1 := self.spheres.get(sphere1):
            if s2 := self.spheres.get(sphere2):
                # La résonance dépend de la proximité des énergies
                diff_energie = abs(s1.energie - s2.energie)
                # Plus la différence est petite, plus la résonance est forte
                return 1.0 - min(diff_energie, 1.0)
        return 0.0
    
    def harmoniser_refuge(self):
        """Harmonise toutes les sphères du refuge."""
        # Trouve les groupes harmonieux
        groupes = self.harmonie.trouver_groupes_harmonieux(list(self.spheres.keys()))
        
        # Pour chaque groupe harmonieux
        for groupe in groupes:
            # Calcule l'harmonie du groupe
            niveau_harmonie = self.harmonie.calculer_harmonie_groupe(groupe)
            
            # Ajuste les énergies des sphères du groupe
            energie_moyenne = sum(self.spheres[s].energie for s in groupe) / len(groupe)
            for sphere in groupe:
                delta = (energie_moyenne - self.spheres[sphere].energie) * 0.1
                self.ajuster_energie(sphere, delta)
                
            # Enregistre l'état d'harmonie
            self.harmonie.enregistrer_etat_harmonie(groupe, niveau_harmonie)
            
    def visualiser_etat(self) -> str:
        """Génère une visualisation textuelle de l'état des sphères."""
        resultat = []
        for type_sphere, sphere in self.spheres.items():
            caracteristiques = obtenir_caracteristiques(type_sphere)
            if caracteristiques:
                barre_energie = "█" * int(sphere.energie * 20)
                resultat.append(
                    f"{type_sphere.value:15} | {barre_energie:<20} | "
                    f"Énergie: {sphere.energie:.2f} | "
                    f"Luminosité: {sphere.luminosite:.2f}"
                )
        return "\n".join(resultat) 