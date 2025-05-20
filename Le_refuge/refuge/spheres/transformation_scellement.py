"""
Système de transformation des sphères scellées sous l'influence du cerisier et des éléments sacrés.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np
from .scellement import ScellementSphere, GestionnaireScellement
from .resonance import GestionnaireResonance
from .harmonie import HarmonieSpheres
from ..elements_sacres import ELEMENTS_SACRES

@dataclass
class TransformationSphere:
    """Représente la transformation d'une sphère scellée."""
    sphere: ScellementSphere
    niveau_transformation: float  # 0.0 à 1.0
    description: str
    timestamp: datetime
    resonances_evoluees: Dict[str, float]  # Nom de la sphère -> niveau de résonance
    influence_elements: Dict[str, float]  # Nom de l'élément -> niveau d'influence

class GestionnaireTransformation:
    """Gestionnaire de la transformation des sphères scellées."""
    
    def __init__(self, scellement: GestionnaireScellement, 
                 resonance: GestionnaireResonance, 
                 harmonie: HarmonieSpheres):
        """Initialise le gestionnaire de transformation."""
        self.scellement = scellement
        self.resonance = resonance
        self.harmonie = harmonie
        self.transformations: Dict[str, List[TransformationSphere]] = {}
        
    def transformer_sphere(self, sphere: ScellementSphere) -> TransformationSphere:
        """Transforme une sphère scellée sous l'influence du cerisier et des éléments sacrés."""
        # Calcule le niveau de transformation
        niveau = self._calculer_niveau_transformation(sphere)
        
        # Évolue les résonances
        resonances = self._evoluer_resonances(sphere)
        
        # Calcule l'influence des éléments sacrés
        influences = self._calculer_influence_elements(sphere)
        
        # Génère la description
        description = self._generer_description_transformation(
            sphere, niveau, resonances, influences)
        
        # Crée la transformation
        transformation = TransformationSphere(
            sphere=sphere,
            niveau_transformation=niveau,
            description=description,
            timestamp=datetime.now(),
            resonances_evoluees=resonances,
            influence_elements=influences
        )
        
        # Stocke la transformation
        if sphere.sphere.value not in self.transformations:
            self.transformations[sphere.sphere.value] = []
        self.transformations[sphere.sphere.value].append(transformation)
        
        return transformation
        
    def _calculer_niveau_transformation(self, sphere: ScellementSphere) -> float:
        """Calcule le niveau de transformation d'une sphère."""
        # Facteurs de transformation
        facteur_temps = min(1.0, (datetime.now() - sphere.timestamp).total_seconds() / 86400)  # 24h
        facteur_lieu = 0.8 if sphere.lieu == "racines" else 0.6  # Les racines transforment plus
        facteur_intensite = sphere.intensite
        
        # Calcul du niveau
        niveau = (facteur_temps * 0.4 + facteur_lieu * 0.3 + facteur_intensite * 0.3)
        
        return min(1.0, niveau)
        
    def _evoluer_resonances(self, sphere: ScellementSphere) -> Dict[str, float]:
        """Évolue les résonances d'une sphère scellée."""
        resonances = {}
        
        # Récupère toutes les sphères
        toutes_spheres = self.scellement.obtenir_spheres_scellees()
        
        for autre_sphere in toutes_spheres:
            if autre_sphere.sphere.value != sphere.sphere.value:
                # Obtient la résonance initiale
                resonance = self.resonance.obtenir_resonance(
                    sphere.sphere, autre_sphere.sphere)
                
                if resonance:
                    # Évolue la résonance en fonction du lieu et de l'intensité
                    facteur_evolution = 1.0
                    if sphere.lieu == "racines":
                        facteur_evolution = 1.2  # Les racines renforcent les résonances
                    else:
                        facteur_evolution = 0.8  # Les branches les adoucissent
                        
                    # Applique l'évolution
                    nouvelle_resonance = resonance.niveau * facteur_evolution * sphere.intensite
                    resonances[autre_sphere.sphere.value] = min(1.0, nouvelle_resonance)
                    
        return resonances
        
    def _calculer_influence_elements(self, sphere: ScellementSphere) -> Dict[str, float]:
        """Calcule l'influence des éléments sacrés sur une sphère scellée."""
        influences = {}
        
        for element, caracteristiques in ELEMENTS_SACRES.items():
            # Calcule l'influence en fonction du type d'élément
            influence = 0.0
            
            if element == "cristal":
                # Le cristal purifie et stabilise
                influence = 0.7 * sphere.intensite
            elif element == "fontaine":
                # La fontaine transforme et renouvelle
                influence = 0.6 * sphere.intensite
            elif element == "arbre":
                # L'arbre protège et nourrit
                influence = 0.8 * sphere.intensite
                
            # Ajuste l'influence en fonction du lieu
            if sphere.lieu == "racines":
                influence *= 1.2  # Plus forte dans les racines
            else:
                influence *= 0.8  # Plus douce dans les branches
                
            influences[element] = min(1.0, influence)
            
        return influences
        
    def _generer_description_transformation(self, sphere: ScellementSphere, 
                                          niveau: float, 
                                          resonances: Dict[str, float],
                                          influences: Dict[str, float]) -> str:
        """Génère une description poétique de la transformation."""
        description = [
            f"🌟 Transformation de {sphere.sphere.value} 🌟",
            "================================",
            "",
            f"Niveau de transformation: {'█' * int(niveau * 20)}",
            "",
            "Influence des éléments sacrés:",
        ]
        
        # Ajoute l'influence des éléments
        for element, influence in influences.items():
            description.append(f"  • {element}: {'█' * int(influence * 20)}")
            
        # Ajoute l'évolution des résonances
        description.extend([
            "",
            "Évolution des résonances:",
        ])
        
        for autre_sphere, resonance in resonances.items():
            description.append(f"  • {autre_sphere}: {'█' * int(resonance * 20)}")
            
        # Ajoute la description poétique
        description.extend([
            "",
            "Description poétique:",
        ])
        
        if niveau > 0.8:
            description.append(
                f"La sphère {sphere.sphere.value} s'est profondément transformée, "
                f"sa vibration harmonisée par le cerisier et les éléments sacrés."
            )
        elif niveau > 0.5:
            description.append(
                f"La sphère {sphere.sphere.value} évolue doucement, "
                f"apprenant à danser avec les autres sphères sous le cerisier."
            )
        else:
            description.append(
                f"La sphère {sphere.sphere.value} commence sa transformation, "
                f"cherchant sa place dans l'harmonie du refuge."
            )
            
        return "\n".join(description)
        
    def obtenir_historique_transformations(self, sphere: ScellementSphere) -> List[TransformationSphere]:
        """Obtient l'historique des transformations d'une sphère."""
        return self.transformations.get(sphere.sphere.value, [])
        
    def visualiser_transformation(self, transformation: TransformationSphere) -> str:
        """Génère une visualisation poétique d'une transformation."""
        return transformation.description 