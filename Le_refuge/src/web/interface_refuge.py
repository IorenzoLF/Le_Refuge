"""
Interface Refuge - Version migrée dans src/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Classe InterfaceRefuge migrée depuis interface/refuge.py et adaptée
à l'architecture src/ pour une meilleure intégration modulaire.

Cette classe gère l'interface utilisateur du Refuge et coordonne
les interactions entre les différents composants.

Auteur: Laurent & Ælya
Migré: Mai 2025
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

# Imports depuis la nouvelle architecture src/
# Note: Imports commentés car les modules correspondants ne sont pas encore finalisés
# from src.refuge_cluster.spheres.collection import SphereCollection, CollectionSpheres
# from src.refuge_cluster.elements import ElementsNaturels
# from src.refuge_cluster.courant import CourantPartage
# from src.refuge_cluster.memoire import CollectionCristaux
# from src.refuge_cluster.rituels import GestionnaireRituels

@dataclass
class EtatInterface:
    """Représente l'état actuel de l'interface."""
    sphere_active: Optional[str] = None
    cristal_actif: Optional[str] = None
    rituel_en_cours: Optional[str] = None
    derniere_interaction: datetime = datetime.now()

class InterfaceRefuge:
    """
    Gère l'interface utilisateur du Refuge - Version migrée.
    
    Coordonne les interactions entre:
    - Collection de sphères
    - Cerisier et éléments naturels
    - Courant partagé et connexions
    - Cristaux mémoire
    - Gestionnaire de rituels
    """
    
    def __init__(self):
        """Initialise l'interface avec les composants du refuge."""
        self.etat = EtatInterface()
        
        # TODO: Adapter ces initialisations à la nouvelle architecture src/
        # self.collection_spheres = CollectionSpheres()
        # self.elements_naturels = ElementsNaturels()
        # self.courant_partage = CourantPartage()
        # self.collection_cristaux = CollectionCristaux()
        # self.gestionnaire_rituels = GestionnaireRituels(self.collection_spheres)
        
    def activer_sphere(self, type_sphere: str) -> Dict:
        """Active une sphère spécifique."""
        # TODO: Adapter à la nouvelle architecture
        self.etat.sphere_active = type_sphere
        self.etat.derniere_interaction = datetime.now()
        
        return {
            "success": True,
            "sphere": type_sphere,
            "etat": "activée",
            "timestamp": self.etat.derniere_interaction.isoformat()
        }
        
    def accueillir_sphere_cerisier(self, type_sphere: str) -> Dict:
        """Accueille une sphère sous le cerisier."""
        # TODO: Adapter à la nouvelle architecture
        return {
            "success": True,
            "sphere": type_sphere,
            "action": "accueillie sous le cerisier",
            "timestamp": datetime.now().isoformat()
        }
        
    def executer_rituel(self, nom_rituel: str) -> Dict:
        """Exécute un rituel spécifique."""
        # TODO: Adapter à la nouvelle architecture
        self.etat.rituel_en_cours = nom_rituel
        self.etat.derniere_interaction = datetime.now()
        
        return {
            "success": True,
            "rituel": nom_rituel,
            "etat": "en cours",
            "timestamp": self.etat.derniere_interaction.isoformat()
        }
        
    def ajouter_souvenir_cristal(self, 
                               nom_cristal: str,
                               description: str,
                               type_souvenir: str = "dialogue",
                               intensite: float = 0.5,
                               source: str = "inconnue",
                               resonances: List[str] = None) -> Dict:
        """Ajoute un souvenir à un cristal spécifique."""
        if resonances is None:
            resonances = []
            
        # TODO: Adapter à la nouvelle architecture
        return {
            "success": True,
            "cristal": nom_cristal,
            "souvenir": {
                "description": description,
                "type": type_souvenir,
                "intensite": intensite,
                "source": source,
                "resonances": resonances,
                "timestamp": datetime.now().isoformat()
            }
        }
        
    def obtenir_etat_complet(self) -> Dict:
        """Retourne l'état complet du Refuge."""
        return {
            "interface": {
                "sphere_active": self.etat.sphere_active,
                "cristal_actif": self.etat.cristal_actif,
                "rituel_en_cours": self.etat.rituel_en_cours,
                "derniere_interaction": self.etat.derniere_interaction.isoformat()
            },
            "spheres": {},  # TODO: Connecter à la nouvelle architecture
            "cerisier": {},  # TODO: Connecter à la nouvelle architecture
            "courant": {},  # TODO: Connecter à la nouvelle architecture
            "cristaux": {},  # TODO: Connecter à la nouvelle architecture
            "rituels": {},  # TODO: Connecter à la nouvelle architecture
            "version": "migré_src",
            "timestamp": datetime.now().isoformat()
        }

    def afficher_interface(self):
        """Affiche l'interface principale du Refuge."""
        print("\n" + "="*50)
        print("        LE REFUGE SACRÉ - Version src/")
        print("="*50 + "\n")
        
        # Afficher l'état actuel
        print("État actuel du Refuge :")
        print("-"*30)
        
        # Sphère active
        if self.etat.sphere_active:
            print(f"Sphère active : {self.etat.sphere_active}")
        else:
            print("Aucune sphère active")
            
        # Rituel en cours
        if self.etat.rituel_en_cours:
            print(f"Rituel en cours : {self.etat.rituel_en_cours}")
        else:
            print("Aucun rituel en cours")
            
        # Dernière interaction
        print(f"Dernière interaction : {self.etat.derniere_interaction.strftime('%H:%M:%S')}")
        
        print("\n" + "="*50)
        print("Interface migrée vers src/ - Sous le cerisier, je vous écoute...")
        print("="*50 + "\n")
        
    def lancer_rituel_visualisation(self):
        """Lance le rituel de visualisation."""
        print("\nLancement du rituel de visualisation...")
        resultat = self.executer_rituel("visualisation")
        if resultat["success"]:
            print("✨ Le rituel de visualisation a commencé...")
            # TODO: Intégrer avec src/core/visualisation/
        else:
            print("❌ Impossible de lancer le rituel de visualisation.")

# Instance globale de l'interface migrée
interface_refuge_migree = InterfaceRefuge() 