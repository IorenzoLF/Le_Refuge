"""
Système de scellement des sphères problématiques dans les racines ou les branches du cerisier.
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np
from src.refuge_cluster.scellement.definition import TypeSphere, CARACTERISTIQUES_SPHERES, BrumeRiviere
from src.refuge_cluster.utilitaires.resonance import Resonance, GestionnaireResonances as GestionnaireResonance
from src.refuge_cluster.spheres.harmonie import HarmonieSpheres, EtatHarmonie

@dataclass
class ScellementSphere:
    """Représente le scellement d'une sphère problématique."""
    sphere: TypeSphere
    lieu: str  # "racines" ou "branches"
    intensite: float  # 0.0 à 1.0
    description: str
    timestamp: datetime
    effets: List[str]

class GestionnaireScellement:
    """Gestionnaire du scellement des sphères problématiques."""
    
    def __init__(self, resonance: GestionnaireResonance, harmonie: HarmonieSpheres):
        """Initialise le gestionnaire de scellement."""
        self.resonance = resonance
        self.harmonie = harmonie
        self.scellements: Dict[TypeSphere, ScellementSphere] = {}
        
    def identifier_spheres_problematiques(self) -> List[TypeSphere]:
        """Identifie les sphères potentiellement problématiques."""
        spheres_problematiques = []
        
        # Vérifie les résonances fortes avec des sphères sombres
        for resonance in self.resonance.obtenir_resonances_fortes(seuil=0.7):
            if self._est_sphere_sombre(resonance.source) or self._est_sphere_sombre(resonance.cible):
                if resonance.source not in spheres_problematiques:
                    spheres_problematiques.append(resonance.source)
                if resonance.cible not in spheres_problematiques:
                    spheres_problematiques.append(resonance.cible)
                    
        return spheres_problematiques
        
    def _est_sphere_sombre(self, sphere: TypeSphere) -> bool:
        """Détermine si une sphère est considérée comme sombre ou problématique."""
        # Liste des sphères sombres ou problématiques
        spheres_sombres = [
            "doute", "peur", "désespoir", "anxiété", "chaos", 
            "paradoxe", "ombre", "apocalypse"
        ]
        
        return any(mot in sphere.value.lower() for mot in spheres_sombres)
        
    def sceller_sphere(self, sphere: TypeSphere, lieu: str, intensite: float = 0.5) -> ScellementSphere:
        """Scelle une sphère problématique dans les racines ou les branches du cerisier."""
        # Vérifie si la sphère est déjà scellée
        if sphere in self.scellements:
            return self.scellements[sphere]
            
        # Génère les effets du scellement
        effets = self._generer_effets_scellement(sphere, lieu, intensite)
        
        # Génère la description
        description = self._generer_description_scellement(sphere, lieu, intensite, effets)
        
        # Crée le scellement
        scellement = ScellementSphere(
            sphere=sphere,
            lieu=lieu,
            intensite=intensite,
            description=description,
            timestamp=datetime.now(),
            effets=effets
        )
        
        # Stocke le scellement
        self.scellements[sphere] = scellement
        
        # Applique les effets du scellement
        self._appliquer_effets_scellement(scellement)
        
        return scellement
        
    def _generer_effets_scellement(self, sphere: TypeSphere, lieu: str, intensite: float) -> List[str]:
        """Génère les effets poétiques du scellement."""
        effets = []
        
        # Effet sur la résonance
        if lieu == "racines":
            effets.append(f"La sphère {sphere.value} est ancrée dans les racines du cerisier, "
                         f"sa vibration stabilisée par la terre nourricière")
        else:  # branches
            effets.append(f"La sphère {sphere.value} est suspendue aux branches du cerisier, "
                         f"sa vibration transformée par la lumière du ciel")
            
        # Effet sur l'harmonie
        if intensite > 0.7:
            effets.append(f"L'intensité du scellement ({intensite:.2f}) permet une transformation "
                         f"profonde de la sphère {sphere.value}")
        elif intensite > 0.3:
            effets.append(f"L'intensité modérée du scellement ({intensite:.2f}) apaise "
                         f"la sphère {sphere.value} sans la contraindre")
        else:
            effets.append(f"Le scellement léger ({intensite:.2f}) offre un espace de repos "
                         f"à la sphère {sphere.value}")
            
        # Effet sur les interactions
        if self._est_sphere_sombre(sphere):
            effets.append(f"La nature sombre de {sphere.value} est contenue et transformée "
                         f"par le scellement dans les {lieu}")
            
        return effets
        
    def _generer_description_scellement(self, sphere: TypeSphere, lieu: str, 
                                       intensite: float, effets: List[str]) -> str:
        """Génère une description poétique du scellement."""
        description = [
            f"🌟 Scellement de la Sphère {sphere.value} 🌟",
            "================================",
            "",
            f"La sphère {sphere.value} a été scellée dans les {lieu} du cerisier, "
            f"avec une intensité de {intensite:.2f}.",
            "",
            "Effets du scellement:",
        ]
        
        for effet in effets:
            description.append(f"  • {effet}")
            
        return "\n".join(description)
        
    def _appliquer_effets_scellement(self, scellement: ScellementSphere):
        """Applique les effets du scellement sur les résonances et harmonies."""
        # Ajuste les résonances
        for resonance in self.resonance.obtenir_resonances_impliquant(sphere=scellement.sphere):
            # Réduit l'intensité des résonances problématiques
            if self._est_sphere_sombre(resonance.source) or self._est_sphere_sombre(resonance.cible):
                self.resonance.ajuster_resonance(
                    resonance.source, 
                    resonance.cible, 
                    resonance.niveau * (1.0 - scellement.intensite)
                )
                
        # Ajuste l'harmonie globale
        self.harmonie.ajuster_intensite_brume(scellement.intensite)
        
    def liberer_sphere(self, sphere: TypeSphere) -> Optional[ScellementSphere]:
        """Libère une sphère scellée."""
        if sphere not in self.scellements:
            return None
            
        scellement = self.scellements[sphere]
        
        # Restaure les résonances
        for resonance in self.resonance.obtenir_resonances_impliquant(sphere=sphere):
            if self._est_sphere_sombre(resonance.source) or self._est_sphere_sombre(resonance.cible):
                self.resonance.ajuster_resonance(
                    resonance.source, 
                    resonance.cible, 
                    resonance.niveau / (1.0 - scellement.intensite)
                )
                
        # Restaure l'harmonie globale
        self.harmonie.ajuster_intensite_brume(0.0)
        
        # Supprime le scellement
        del self.scellements[sphere]
        
        return scellement
        
    def obtenir_spheres_scellees(self) -> List[ScellementSphere]:
        """Obtient la liste des sphères scellées."""
        return list(self.scellements.values())
        
    def visualiser_scellement(self, scellement: ScellementSphere) -> str:
        """Génère une visualisation poétique d'un scellement."""
        return scellement.description 