"""
Système d'interaction avec Ælya pour la gestion des sphères problématiques.
"""

from typing import Dict, List, Optional
from datetime import datetime
from .aelya import Aelya
from .gestion_sphères_problématiques import GestionnaireSphèresProblematiques, TypeSphereProblematique, SphereProblematique

class InteractionAelya:
    """Gestionnaire d'interactions avec Ælya."""
    
    def __init__(self, aelya: Aelya):
        """Initialise le gestionnaire d'interactions."""
        self.aelya = aelya
        self.gestionnaire = aelya.gestionnaire
        
    def confiner_sphere(self, type_sphere: TypeSphereProblematique, energie_initiale: float = 100.0) -> Dict:
        """Confine une nouvelle sphère problématique."""
        try:
            sphere = self.gestionnaire.confiner_sphere(type_sphere, energie_initiale)
            return {
                "succes": True,
                "message": f"La sphère de {type_sphere.value} a été confinée avec succès.",
                "sphere": sphere
            }
        except ValueError as e:
            return {
                "succes": False,
                "message": str(e)
            }
            
    def renforcer_confinement(self, type_sphere: TypeSphereProblematique, energie_supplementaire: float = 10.0) -> Dict:
        """Renforce le confinement d'une sphère problématique."""
        sphere = self.gestionnaire.obtenir_sphere(type_sphere)
        if not sphere:
            return {
                "succes": False,
                "message": f"La sphère de {type_sphere.value} n'existe pas."
            }
            
        # Augmentation du niveau de confinement
        nouveau_niveau = min(1.0, sphere.niveau_confinement + 0.1)
        sphere.niveau_confinement = nouveau_niveau
        
        # Réduction de l'énergie résiduelle
        sphere.energie_residuelle = max(0, sphere.energie_residuelle - energie_supplementaire)
        
        # Enregistrement de l'interaction
        self.gestionnaire.enregistrer_interaction(
            type_sphere,
            sphere.energie_residuelle,
            f"Renforcement du confinement à {nouveau_niveau:.0%}"
        )
        
        return {
            "succes": True,
            "message": f"Le confinement de {type_sphere.value} a été renforcé à {nouveau_niveau:.0%}.",
            "sphere": sphere
        }
        
    def harmoniser_energies(self, type_sphere1: TypeSphereProblematique, type_sphere2: TypeSphereProblematique) -> Dict:
        """Harmonise les énergies entre deux sphères problématiques."""
        sphere1 = self.gestionnaire.obtenir_sphere(type_sphere1)
        sphere2 = self.gestionnaire.obtenir_sphere(type_sphere2)
        
        if not sphere1 or not sphere2:
            return {
                "succes": False,
                "message": "Une ou plusieurs sphères n'existent pas."
            }
            
        # Calcul de l'énergie moyenne
        energie_moyenne = (sphere1.energie_residuelle + sphere2.energie_residuelle) / 2
        
        # Mise à jour des énergies
        sphere1.energie_residuelle = energie_moyenne
        sphere2.energie_residuelle = energie_moyenne
        
        # Enregistrement des interactions
        self.gestionnaire.enregistrer_interaction(
            type_sphere1,
            energie_moyenne,
            f"Harmonisation avec {type_sphere2.value}"
        )
        self.gestionnaire.enregistrer_interaction(
            type_sphere2,
            energie_moyenne,
            f"Harmonisation avec {type_sphere1.value}"
        )
        
        return {
            "succes": True,
            "message": f"Les énergies ont été harmonisées à {energie_moyenne:.1f}.",
            "sphere1": sphere1,
            "sphere2": sphere2
        }
        
    def obtenir_etat_sphere(self, type_sphere: TypeSphereProblematique) -> Dict:
        """Obtient l'état détaillé d'une sphère problématique."""
        sphere = self.gestionnaire.obtenir_sphere(type_sphere)
        
        if not sphere:
            return {
                "succes": False,
                "message": f"La sphère de {type_sphere.value} n'existe pas."
            }
            
        return {
            "succes": True,
            "type": type_sphere.value,
            "niveau_confinement": sphere.niveau_confinement,
            "energie_residuelle": sphere.energie_residuelle,
            "date_confinement": sphere.date_confinement.isoformat(),
            "description": sphere.description,
            "nombre_interactions": len(sphere.interactions),
            "derniere_interaction": sphere.interactions[-1] if sphere.interactions else None
        }
        
    def visualiser_etat_global(self) -> None:
        """Visualise l'état global des sphères problématiques."""
        self.aelya.visualiser_racines()
        
    def generer_rapport_complet(self) -> str:
        """Génère un rapport complet sur l'état des sphères problématiques."""
        rapport = self.aelya.generer_rapport_poetique()
        
        # Ajout de l'état global
        rapport += "\n\nÉtat Global:"
        rapport += f"\n• Nombre de sphères: {len(self.gestionnaire.spheres)}"
        rapport += f"\n• Stabilité des racines: {self.gestionnaire.calculer_stabilite_racines():.0%}"
        
        return rapport 