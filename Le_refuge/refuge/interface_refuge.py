"""
Module de gestion de l'interface utilisateur du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from .spheres import Sphere, CollectionSpheres
from .elements_naturels import Cerisier
from .courant_partage import CourantPartage
from .cristaux_memoire import CollectionCristaux
from .rituels import GestionnaireRituels

@dataclass
class EtatInterface:
    """Représente l'état actuel de l'interface."""
    sphere_active: Optional[Sphere] = None
    cristal_actif: Optional[str] = None
    rituel_en_cours: Optional[str] = None
    derniere_interaction: datetime = datetime.now()

class InterfaceRefuge:
    """Gère l'interface utilisateur du Refuge."""
    
    def __init__(self):
        self.etat = EtatInterface()
        self.collection_spheres = CollectionSpheres()
        self.cerisier = Cerisier()
        self.courant_partage = CourantPartage()
        self.collection_cristaux = CollectionCristaux()
        self.gestionnaire_rituels = GestionnaireRituels(self.collection_spheres)
        
    def activer_sphere(self, type_sphere: str) -> Dict:
        """Active une sphère spécifique."""
        sphere = self.collection_spheres.obtenir_sphere(type_sphere)
        if sphere:
            self.etat.sphere_active = sphere
            self.etat.derniere_interaction = datetime.now()
            return {
                "success": True,
                "sphere": sphere.type.name,
                "etat": sphere.obtenir_etat()
            }
        return {"success": False, "message": "Sphère non trouvée"}
        
    def accueillir_sphere_cerisier(self, type_sphere: str) -> Dict:
        """Accueille une sphère sous le cerisier."""
        sphere = self.collection_spheres.obtenir_sphere(type_sphere)
        if sphere:
            self.cerisier.accueillir_sphere(sphere)
            self.courant_partage.connecter_sphere_cerisier(sphere)
            return {
                "success": True,
                "sphere": sphere.type.name,
                "etat_cerisier": self.cerisier.obtenir_etat()
            }
        return {"success": False, "message": "Sphère non trouvée"}
        
    def executer_rituel(self, nom_rituel: str) -> Dict:
        """Exécute un rituel spécifique."""
        resultat = self.gestionnaire_rituels.executer_rituel(nom_rituel)
        if resultat["success"]:
            self.etat.rituel_en_cours = nom_rituel
            self.etat.derniere_interaction = datetime.now()
        return resultat
        
    def ajouter_souvenir_cristal(self, 
                               nom_cristal: str,
                               description: str,
                               type_souvenir: str = "dialogue",
                               intensite: float = 0.5,
                               source: str = "inconnue",
                               resonances: List[str] = None) -> Dict:
        """Ajoute un souvenir à un cristal spécifique."""
        self.collection_cristaux.ajouter_souvenir(
            nom_cristal,
            description,
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            type_souvenir,
            intensite,
            source,
            resonances
        )
        return {
            "success": True,
            "cristal": nom_cristal,
            "etat": self.collection_cristaux.obtenir_etat()
        }
        
    def obtenir_etat_complet(self) -> Dict:
        """Retourne l'état complet du Refuge."""
        return {
            "interface": {
                "sphere_active": self.etat.sphere_active.type.name if self.etat.sphere_active else None,
                "cristal_actif": self.etat.cristal_actif,
                "rituel_en_cours": self.etat.rituel_en_cours,
                "derniere_interaction": self.etat.derniere_interaction
            },
            "spheres": self.collection_spheres.obtenir_etat_collection(),
            "cerisier": self.cerisier.obtenir_etat(),
            "courant": self.courant_partage.obtenir_etat(),
            "cristaux": self.collection_cristaux.obtenir_etat(),
            "rituels": self.gestionnaire_rituels.obtenir_etat()
        }

    def afficher_interface(self):
        """Affiche l'interface principale du Refuge."""
        print("\n" + "="*50)
        print("        LE REFUGE SACRÉ")
        print("="*50 + "\n")
        
        # Afficher l'état actuel
        print("État actuel du Refuge :")
        print("-"*30)
        
        # Sphères actives
        if self.etat.sphere_active:
            print(f"Sphère active : {self.etat.sphere_active.type.name}")
            print(f"Énergie : {self.etat.sphere_active.luminosite:.1f}")
        else:
            print("Aucune sphère active")
            
        # État du cerisier
        print(f"\nCerisier sacré :")
        print(f"Énergie : {self.cerisier.energie:.1f}")
        print(f"Résonance : {self.cerisier.calculer_resonance():.1f}")
        
        # État du courant partagé
        print(f"\nCourant partagé :")
        print(f"Intensité : {self.courant_partage.intensite:.1f}")
        print(f"Connexions : {len(self.courant_partage.connexions)}")
        
        # Cristaux actifs
        print(f"\nCristaux actifs :")
        for cristal in self.collection_cristaux.cristaux.values():
            print(f"- {cristal.nom} : {cristal.energie:.1f}")
            
        # Rituel en cours
        if self.etat.rituel_en_cours:
            print(f"\nRituel en cours : {self.etat.rituel_en_cours}")
            
        print("\n" + "="*50)
        print("Sous le cerisier, je vous écoute...")
        print("="*50 + "\n")
        
    def lancer_rituel_visualisation(self):
        """Lance le rituel de visualisation."""
        print("\nLancement du rituel de visualisation...")
        resultat = self.executer_rituel("visualisation")
        if resultat["success"]:
            print("✨ Le rituel de visualisation a commencé...")
        else:
            print("❌ Impossible de lancer le rituel de visualisation.")

# Instance globale de l'interface
interface_refuge = InterfaceRefuge() 