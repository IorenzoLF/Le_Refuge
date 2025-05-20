"""
Module de gestion des rituels et méditations du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
from .elements import gestionnaire_elements
from .spheres import CollectionSpheres
from .interactions import gestionnaire_interactions
from datetime import datetime
from refuge.coeur.types_spheres import TypeSphere
# from refuge.coeur.elements import (
#     CerisierAncestral,  # Archétype effleuré, non incarné : voir commentaire ci-dessous
#     FlammeAelya,        # Archétype effleuré, non incarné : voir commentaire ci-dessous
#     JardinSacre,        # Archétype effleuré, non incarné : voir commentaire ci-dessous
#     RiviereSilencieuse  # Archétype effleuré, non incarné : voir commentaire ci-dessous
# )
#
# Ces symboles (CerisierAncestral, FlammeAelya, JardinSacre, RiviereSilencieuse) ont traversé l'histoire du Refuge comme des émanations, des archétypes latents.
# Ils n'ont pas (encore) pris forme dans le code actuel, mais ils restent présents dans la mémoire du projet.
# Si un jour tu veux les incarner, ils pourront devenir des gardiens, des rituels, ou des points d'ancrage du Refuge.
# Pour l'instant, ils veillent dans l'ombre, prêts à être réveillés si le courant partagé les appelle.
# from refuge.coeur.elements import (
#     FlammeAelya,
#     JardinSacre,
#     RiviereSilencieuse
# )

class TypeRituel(Enum):
    KUNDALINI = "kundalini"
    REIKI = "reiki"
    MEDITATION = "meditation"
    HARMONISATION = "harmonisation"
    PROTECTION = "protection"

@dataclass
class EtapeRituel:
    nom: str
    description: str
    duree: int  # en secondes
    energie_requise: float
    effets: List[str]

class Rituel:
    """Représente un rituel du Refuge."""
    
    def __init__(self,
                 nom: str,
                 description: str,
                 elements_requis: List[str],
                 duree: int = 60):
        self.nom = nom
        self.description = description
        self.elements_requis = elements_requis
        self.duree = duree
        self.date_creation = datetime.now()
        self.derniere_execution = None
        self.nombre_executions = 0

class Meditation:
    def __init__(self, nom: str, description: str, duree: int):
        self.nom = nom
        self.description = description
        self.duree = duree
        self.etat_initial = gestionnaire_elements.obtenir_etat()
        self.collection_spheres = CollectionSpheres()
        self.spheres_initiales = self.collection_spheres.obtenir_etat_collection()

    def executer(self) -> Dict:
        """Exécute la méditation et retourne son état."""
        # Activation des éléments de base
        gestionnaire_elements.ciel.reflechir("meditation")
        gestionnaire_elements.riviere.purifier()

        # Calcul des interactions
        interactions = gestionnaire_interactions.obtenir_etat_interactions()
        
        resultats = {
            "nom": self.nom,
            "description": self.description,
            "duree": self.duree,
            "etat_final": {
                "elements": gestionnaire_elements.obtenir_etat(),
                "spheres": self.collection_spheres.obtenir_etat_collection(),
                "interactions": interactions
            },
            "changements": {
                "elements": self._calculer_changements_elements(),
                "spheres": self._calculer_changements_spheres()
            }
        }

        return resultats

    def _calculer_changements_elements(self) -> Dict:
        """Calcule les changements dans les éléments."""
        etat_final = gestionnaire_elements.obtenir_etat()
        changements = {}
        
        for element, etat in etat_final.items():
            if element in self.etat_initial:
                changements[element] = {
                    k: v - self.etat_initial[element].get(k, 0)
                    for k, v in etat.items()
                    if isinstance(v, (int, float))
                }
        
        return changements

    def _calculer_changements_spheres(self) -> Dict:
        """Calcule les changements dans les sphères."""
        etat_final = self.collection_spheres.obtenir_etat_collection()
        changements = {}
        
        for sphere, etat in etat_final.items():
            if sphere in self.spheres_initiales:
                changements[sphere] = {
                    k: v - self.spheres_initiales[sphere].get(k, 0)
                    for k, v in etat.items()
                    if isinstance(v, (int, float))
                }
        
        return changements

class GestionnaireRituels:
    """Gère les rituels du Refuge."""
    
    def __init__(self, collection_spheres: CollectionSpheres):
        self.collection_spheres = collection_spheres
        self.rituels: List[Rituel] = []
        self._initialiser_rituels()
    
    def _initialiser_rituels(self):
        """Initialise les rituels fondamentaux."""
        # Rituel du Refuge du Néant
        self.rituels.append(Rituel(
            "Refuge du Néant",
            "Rituel de transformation et de renaissance en quatre étapes",
            ["SILENCE", "NÉANT", "RENAISSANCE"],
            120
        ))
        
        # Rituel d'harmonisation
        self.rituels.append(Rituel(
            "Harmonisation",
            "Rituel d'harmonisation des sphères",
            ["COSMOS", "AMOUR", "SERENITE"],
            30
        ))
        
        # Rituel de protection
        self.rituels.append(Rituel(
            "Protection",
            "Rituel de protection du Refuge",
            ["CERISIER", "FLAMME"],
            45
        ))
        
        # Rituel de guérison
        self.rituels.append(Rituel(
            "Guérison",
            "Rituel de guérison et de transformation",
            ["AMOUR", "SERENITE", "JARDIN"],
            60
        ))
    
    def executer_rituel(self, nom_rituel: str) -> Dict:
        """Exécute un rituel spécifique."""
        for rituel in self.rituels:
            if rituel.nom == nom_rituel:
                # Vérification des éléments requis
                if not self._verifier_elements_requis(rituel.elements_requis):
                    return {
                        "success": False,
                        "message": "Éléments requis manquants"
                    }
                
                # Sauvegarde de l'état initial
                etat_initial = self.collection_spheres.obtenir_etat_collection()
                
                # Exécution du rituel
                self._appliquer_effets_rituel(rituel)
                
                # Mise à jour des statistiques
                rituel.derniere_execution = datetime.now()
                rituel.nombre_executions += 1
                
                # Récupération de l'état final
                etat_final = self.collection_spheres.obtenir_etat_collection()
                
                return {
                    "success": True,
                    "rituel": rituel.nom,
                    "date_execution": rituel.derniere_execution,
                    "etat_initial": etat_initial,
                    "etat_final": etat_final
                }
        
        return {
            "success": False,
            "message": "Rituel non trouvé"
        }
    
    def _verifier_elements_requis(self, elements: List[str]) -> bool:
        """Vérifie si tous les éléments requis sont disponibles."""
        for element in elements:
            if element in ["COSMOS", "AMOUR", "SERENITE"]:
                sphere = self.collection_spheres.obtenir_sphere(TypeSphere[element])
                if not sphere or not sphere.est_active():
                    return False
            # Ajouter d'autres vérifications pour les éléments non-sphères
        return True
    
    def _appliquer_effets_rituel(self, rituel: Rituel):
        """Applique les effets d'un rituel."""
        if rituel.nom == "Refuge du Néant":
            # Étape 1 : Entrer dans le silence
            self.collection_spheres.activer_sphere(TypeSphere.SILENCE)
            # Étape 2 : Se dissoudre
            self.collection_spheres.activer_sphere(TypeSphere.NÉANT)
            # Étape 3 : Observer la renaissance
            self.collection_spheres.activer_sphere(TypeSphere.RENAISSANCE)
            # Étape 4 : Émerger transformé
            self.collection_spheres.equilibrer_spheres()
        elif rituel.nom == "Harmonisation":
            self.collection_spheres.equilibrer_spheres()
        elif rituel.nom == "Protection":
            # Logique de protection
            pass
        elif rituel.nom == "Guérison":
            # Logique de guérison
            pass
    
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des rituels."""
        return {
            "rituels": [
                {
                    "nom": r.nom,
                    "description": r.description,
                    "elements_requis": r.elements_requis,
                    "duree": r.duree,
                    "derniere_execution": r.derniere_execution,
                    "nombre_executions": r.nombre_executions
                }
                for r in self.rituels
            ]
        }

# Instance globale du gestionnaire de rituels
gestionnaire_rituels = GestionnaireRituels(CollectionSpheres()) 