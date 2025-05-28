"""
Module d'intégration des sphères avec les autres composants du refuge.

Ce module gère les interactions entre les sphères et les autres éléments du refuge,
comme le cerisier, la rivière de lumière, et les gardiens.
"""

from typing import Dict, List, Optional, Any, Set
import logging
import json
from datetime import datetime
from dataclasses import dataclass, field

from src.core.types_spheres import TypeSphere
from src.refuge_cluster.spheres.collection import CollectionSpheres
from gardiens import gestionnaire_gardiens
from energies import gestionnaire_energies
from equilibre import gestionnaire_equilibre
from resonance import gestionnaire_resonances
from harmonisations import gestionnaire_harmonisations

class IntegrateurSpheres:
    """Intègre les sphères avec les autres composants du refuge"""
    
    def __init__(self):
        self.collection_spheres = CollectionSpheres()
        self.gardiens = gestionnaire_gardiens
        self.energies = gestionnaire_energies
        self.equilibre = gestionnaire_equilibre
        self.resonances = gestionnaire_resonances
        self.harmonisations = gestionnaire_harmonisations
        self.derniere_integration = None
        self.niveau_harmonie = 0.0
        
    def synchroniser_tout(self) -> Dict[str, float]:
        """Synchronise tous les composants du refuge avec les sphères"""
        # Synchronise les sphères avec les chakras
        self.collection_spheres.synchroniser_spheres_chakras()
        
        # Synchronise avec les gardiens
        self._synchroniser_gardiens()
        
        # Synchronise avec les énergies
        self._synchroniser_energies()
        
        # Synchronise avec l'équilibre
        self._synchroniser_equilibre()
        
        # Synchronise avec les résonances
        self._synchroniser_resonances()
        
        # Synchronise avec les harmonisations
        self._synchroniser_harmonisations()
        
        return self.obtenir_harmonies()
        
    def _synchroniser_gardiens(self) -> None:
        """Synchronise les sphères avec les gardiens"""
        # Les gardiens résonnent avec certaines sphères
        resonances = {
            "CERF": TypeSphere.EMOTIONS,
            "LOUP_NOIR": TypeSphere.SOMBRES_MYSTERES,
            "AIGLE": TypeSphere.ABSTRACTIONS,
            "SERPENT": TypeSphere.PROCESSUS
        }
        
        for gardien_type, sphere_type in resonances.items():
            if sphere := self.collection_spheres.obtenir_sphere(sphere_type):
                self.gardiens.ajuster_force_gardien(gardien_type, sphere.energie)
                
    def _synchroniser_energies(self) -> None:
        """Synchronise les sphères avec les flux d'énergie"""
        # Chaque type de sphère influence certains types d'énergie
        for sphere_type in TypeSphere:
            if sphere := self.collection_spheres.obtenir_sphere(sphere_type):
                self.energies.ajuster_flux(str(sphere_type), sphere.energie)
                
    def _synchroniser_equilibre(self) -> None:
        """Synchronise les sphères avec l'équilibre global"""
        harmonie_spheres = self.collection_spheres.calculer_harmonie_globale()
        self.equilibre.ajuster_force_equilibre(harmonie_spheres)
        
    def _synchroniser_resonances(self) -> None:
        """Synchronise les sphères avec les résonances"""
        # Les sphères principales créent des résonances spécifiques
        resonances_principales = [
            TypeSphere.AMOUR,
            TypeSphere.SERENITE,
            TypeSphere.FIBONACCI,
            TypeSphere.COSMOS
        ]
        
        for type_sphere in resonances_principales:
            if sphere := self.collection_spheres.obtenir_sphere(type_sphere):
                self.resonances.creer_resonance(str(type_sphere), sphere.energie)
                
    def _synchroniser_harmonisations(self) -> None:
        """Synchronise les sphères avec les harmonisations"""
        # L'harmonisation globale dépend de l'état des sphères
        harmonie = self.collection_spheres.calculer_harmonie_globale()
        self.harmonisations.ajuster_niveau_harmonie(harmonie)
        
    def activer_protection_complete(self) -> Tuple[bool, str]:
        """Active la protection complète du refuge"""
        # Active la Sphère Metatron
        succes_metatron, _ = self.collection_spheres.activer_metatron()
        
        # Renforce les gardiens
        self.gardiens.eveiller_gardiens()
        
        # Amplifie les énergies protectrices
        self.energies.amplifier_protection()
        
        # Stabilise l'équilibre
        self.equilibre.stabiliser()
        
        return succes_metatron, "Protection complète activée"
        
    def maintenir_autonomie(self) -> Tuple[bool, str]:
        """Maintient l'autonomie du refuge"""
        # Active la Sphère d'Autonomie
        succes_autonomie, _ = self.collection_spheres.activer_autonomie()
        
        if succes_autonomie:
            # Ajuste les résonances pour maintenir la connexion
            self.resonances.maintenir_connexion()
            
            # Stabilise les harmonisations
            self.harmonisations.stabiliser_niveau()
            
            # Maintient l'équilibre énergétique
            self.equilibre.maintenir_equilibre()
            
        return succes_autonomie, "Autonomie maintenue"
        
    def obtenir_harmonies(self) -> Dict[str, float]:
        """Retourne les niveaux d'harmonie de tous les composants"""
        return {
            "spheres": self.collection_spheres.calculer_harmonie_globale(),
            "chakras": self.collection_spheres.calculer_harmonie_chakras(),
            "gardiens": self.gardiens.calculer_harmonie(),
            "energies": self.energies.calculer_harmonie(),
            "equilibre": self.equilibre.obtenir_force(),
            "resonances": self.resonances.calculer_harmonie(),
            "harmonisations": self.harmonisations.obtenir_niveau()
        }
        
    def obtenir_etat_complet(self) -> Dict:
        """Retourne l'état complet du refuge intégré"""
        return {
            "spheres": self.collection_spheres.obtenir_etat_complet(),
            "gardiens": self.gardiens.obtenir_etat(),
            "energies": self.energies.obtenir_etat(),
            "equilibre": self.equilibre.obtenir_etat(),
            "resonances": self.resonances.obtenir_etat(),
            "harmonisations": self.harmonisations.obtenir_etat(),
            "harmonies": self.obtenir_harmonies()
        }

    def integrer_spheres(self) -> Dict:
        """Intègre et harmonise les sphères."""
        # Sauvegarde de l'état initial
        etat_initial = self.collection_spheres.obtenir_etat_collection()
        
        # Équilibrage des sphères
        self.collection_spheres.equilibrer_spheres()
        
        # Calcul du niveau d'harmonie
        self.niveau_harmonie = self._calculer_harmonie()
        
        # Mise à jour de la date d'intégration
        self.derniere_integration = datetime.now()
        
        # Récupération de l'état final
        etat_final = self.collection_spheres.obtenir_etat_collection()
        
        return {
            "success": True,
            "date_integration": self.derniere_integration,
            "niveau_harmonie": self.niveau_harmonie,
            "etat_initial": etat_initial,
            "etat_final": etat_final
        }
    
    def _calculer_harmonie(self) -> float:
        """Calcule le niveau d'harmonie entre les sphères."""
        # Récupération de l'état des sphères
        etat = self.collection_spheres.obtenir_etat_collection()
        
        # Calcul de la moyenne des énergies
        energies = [sphere["energie"] for sphere in etat["spheres"].values()]
        moyenne_energie = sum(energies) / len(energies)
        
        # Calcul de la variance des énergies
        variance = sum((e - moyenne_energie) ** 2 for e in energies) / len(energies)
        
        # Plus la variance est faible, plus l'harmonie est élevée
        harmonie = 1.0 / (1.0 + variance)
        
        return harmonie
    
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel de l'intégration."""
        return {
            "derniere_integration": self.derniere_integration,
            "niveau_harmonie": self.niveau_harmonie,
            "spheres": self.collection_spheres.obtenir_etat_collection()
        }

# Instance globale de l'intégrateur
integrateur_spheres = IntegrateurSpheres() 
