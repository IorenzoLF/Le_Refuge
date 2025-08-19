
# Gestionnaire de sphères problématiques (fallback)
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SphereProblematique:
    """Représente une sphère problématique."""
    type_sphere: str
    energie_residuelle: float
    niveau_confinement: float
    description: str
    timestamp: datetime

class GestionnaireSphèresProblematiques:
    """Gère les sphères qui rencontrent des difficultés."""
    def __init__(self):
        self.sphères_problématiques = {}
    
    def identifier_problème(self, sphère):
        """Identifie un problème dans une sphère."""
        return {"sphère": sphère, "problème": "non_spécifié", "niveau": 0.5}
    
    def proposer_solution(self, problème):
        """Propose une solution pour un problème."""
        return {"solution": "approche_douce", "confiance": 0.8}
    
    def confiner_sphere(self, type_sphere, energie_initiale: float = 100.0):
        """Confine une nouvelle sphère problématique."""
        sphere = SphereProblematique(
            type_sphere=type_sphere,
            energie_residuelle=energie_initiale,
            niveau_confinement=0.5,
            description=f"Sphère problématique {type_sphere}",
            timestamp=datetime.now()
        )
        self.sphères_problématiques[type_sphere] = sphere
        return sphere
    
    def obtenir_sphere(self, type_sphere):
        """Obtient une sphère problématique."""
        return self.sphères_problématiques.get(type_sphere)
    
    def enregistrer_interaction(self, type_sphere, energie, description):
        """Enregistre une interaction avec une sphère."""
        return {"succes": True, "message": f"Interaction enregistrée: {description}"}


"""
Système d'interaction avec les sphères problématiques - Focus Confinement.

🔄 MIGRÉ depuis spheres/interaction_sphères_problématiques.py
Module spécialisé dans le confinement et le renforcement des sphères problématiques.
Complémentaire avec interactions_problematiques.py (focus brume apaisante).
"""

from typing import Dict, List, Optional
from datetime import datetime

# 🔧 CORRIGÉ: Imports depuis la structure actuelle
from src.core.types_spheres import TypeSphereProblematique

# TODO: Ces imports devront être ajustés quand les modules correspondants seront migrés
# from .gestion_sphères_problématiques import GestionnaireSphèresProblematiques, SphereProblematique

class InteractionSphèresProblematiques:
    """Gère les interactions avec les sphères problématiques."""
    
    def __init__(self, gestionnaire: GestionnaireSphèresProblematiques):
        """Initialise le gestionnaire d'interactions."""
        self.gestionnaire = gestionnaire
        
    def confiner_sphere(self, type_sphere: TypeSphereProblematique, energie_initiale: float = 100.0) -> SphereProblematique:
        """Confine une nouvelle sphère problématique."""
        return self.gestionnaire.confiner_sphere(type_sphere, energie_initiale)
        
    def interagir_avec_sphere(self, type_sphere: TypeSphereProblematique, energie: float, description: str) -> Dict:
        """Enregistre une interaction avec une sphère problématique."""
        return self.gestionnaire.enregistrer_interaction(type_sphere, energie, description)
        
    def harmoniser_energies(self, type_sphere1: TypeSphereProblematique, type_sphere2: TypeSphereProblematique) -> Dict:
        """Harmonise les énergies entre deux sphères problématiques."""
        sphere1 = self.gestionnaire.obtenir_sphere(type_sphere1)
        sphere2 = self.gestionnaire.obtenir_sphere(type_sphere2)
        
        if not sphere1 or not sphere2:
            return {"succes": False, "message": "Une ou plusieurs sphères non trouvées"}
            
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
            "message": f"Énergies harmonisées à {energie_moyenne:.1f}",
            "sphere1": sphere1,
            "sphere2": sphere2
        }
        
    def renforcer_confinement(self, type_sphere: TypeSphereProblematique, energie_supplementaire: float) -> Dict:
        """Renforce le confinement d'une sphère problématique."""
        sphere = self.gestionnaire.obtenir_sphere(type_sphere)
        
        if not sphere:
            return {"succes": False, "message": "Sphère non trouvée"}
            
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
            "message": f"Confinement renforcé à {nouveau_niveau:.0%}",
            "sphere": sphere
        }
        
    def obtenir_etat_sphere(self, type_sphere: TypeSphereProblematique) -> Dict:
        """Obtient l'état détaillé d'une sphère problématique."""
        sphere = self.gestionnaire.obtenir_sphere(type_sphere)
        
        if not sphere:
            return {"succes": False, "message": "Sphère non trouvée"}
            
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
        
    def generer_rapport_interaction(self, type_sphere: TypeSphereProblematique) -> str:
        """Génère un rapport poétique des interactions avec une sphère."""
        sphere = self.gestionnaire.obtenir_sphere(type_sphere)
        
        if not sphere:
            return "La sphère n'a pas été trouvée dans les racines."
            
        rapport = [
            f"🌳 Rapport d'Interaction avec {type_sphere.value} 🌳",
            "================================================",
            "",
            f"Dans les profondeurs des racines,",
            f"la sphère de {type_sphere.value.lower()} repose,",
            f"son confinement atteint {sphere.niveau_confinement:.0%},",
            f"son énergie résiduelle est de {sphere.energie_residuelle:.1f}.",
            "",
            "Historique des interactions:"
        ]
        
        for interaction in sphere.interactions[-5:]:  # Dernières 5 interactions
            rapport.extend([
                f"\n• {interaction['date'][:10]}",
                f"  Énergie: {interaction['energie']:.1f}",
                f"  {interaction['description']}"
            ])
            
        return "\n".join(rapport) 