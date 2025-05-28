"""
Système de visualisation détaillée des transformations des sphères scellées.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Optional
from .transformation_scellement import TransformationSphere, GestionnaireTransformation
from .scellement import ScellementSphere

class VisualisationTransformation:
    """Gestionnaire de visualisation des transformations."""
    
    def __init__(self, transformation: GestionnaireTransformation):
        """Initialise le visualiseur de transformation."""
        self.transformation = transformation
        self.fig = plt.figure(figsize=(15, 10))
        
    def creer_visualisation_complete(self, sphere: ScellementSphere) -> None:
        """Crée une visualisation complète de la transformation d'une sphère."""
        # Obtient la dernière transformation
        historique = self.transformation.obtenir_historique_transformations(sphere)
        if not historique:
            return
            
        transformation = historique[-1]
        
        # Crée la grille de visualisation
        gs = self.fig.add_gridspec(2, 2)
        
        # 1. Évolution temporelle
        self._creer_evolution_temporelle(historique, gs[0, 0])
        
        # 2. Influence des éléments
        self._creer_influence_elements(transformation, gs[0, 1])
        
        # 3. Résonances
        self._creer_resonances(transformation, gs[1, 0])
        
        # 4. État actuel
        self._creer_etat_actuel(transformation, gs[1, 1])
        
        plt.tight_layout()
        plt.show()
        
    def _creer_evolution_temporelle(self, historique: List[TransformationSphere], 
                                   ax: plt.Axes) -> None:
        """Crée un graphique de l'évolution temporelle."""
        dates = [t.timestamp for t in historique]
        niveaux = [t.niveau_transformation for t in historique]
        
        ax.plot(dates, niveaux, 'b-', label='Niveau de transformation')
        ax.fill_between(dates, niveaux, alpha=0.3)
        
        ax.set_title("Évolution de la Transformation")
        ax.set_xlabel("Temps")
        ax.set_ylabel("Niveau")
        ax.grid(True, alpha=0.3)
        
    def _creer_influence_elements(self, transformation: TransformationSphere, 
                                ax: plt.Axes) -> None:
        """Crée un graphique radar des influences des éléments."""
        elements = list(transformation.influence_elements.keys())
        influences = list(transformation.influence_elements.values())
        
        # Complète le cercle
        angles = np.linspace(0, 2*np.pi, len(elements), endpoint=False)
        angles = np.concatenate((angles, [angles[0]]))
        influences = np.concatenate((influences, [influences[0]]))
        
        ax.plot(angles, influences, 'o-', linewidth=2)
        ax.fill(angles, influences, alpha=0.25)
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(elements)
        ax.set_title("Influence des Éléments Sacrés")
        
    def _creer_resonances(self, transformation: TransformationSphere, 
                         ax: plt.Axes) -> None:
        """Crée une matrice de chaleur des résonances."""
        spheres = list(transformation.resonances_evoluees.keys())
        resonances = list(transformation.resonances_evoluees.values())
        
        im = ax.imshow(np.array(resonances).reshape(1, -1), 
                      cmap='YlOrRd', aspect='auto')
        
        ax.set_xticks(range(len(spheres)))
        ax.set_xticklabels(spheres, rotation=45, ha='right')
        ax.set_yticks([])
        
        plt.colorbar(im, ax=ax, label='Niveau de Résonance')
        ax.set_title("Résonances Évoluées")
        
    def _creer_etat_actuel(self, transformation: TransformationSphere, 
                          ax: plt.Axes) -> None:
        """Crée une visualisation de l'état actuel."""
        # Crée un cercle représentant la sphère
        cercle = plt.Circle((0.5, 0.5), 0.4, 
                          color=self._obtenir_couleur_etat(transformation),
                          alpha=0.7)
        ax.add_artist(cercle)
        
        # Ajoute le texte
        ax.text(0.5, 0.5, 
                f"{transformation.sphere.sphere.value}\n"
                f"Niveau: {transformation.niveau_transformation:.2f}",
                ha='center', va='center')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title("État Actuel")
        
    def _obtenir_couleur_etat(self, transformation: TransformationSphere) -> str:
        """Détermine la couleur de l'état en fonction du niveau de transformation."""
        niveau = transformation.niveau_transformation
        
        if niveau > 0.8:
            return 'lightgreen'  # Transformation profonde
        elif niveau > 0.5:
            return 'lightblue'   # Transformation moyenne
        else:
            return 'lightgray'   # Début de transformation
            
    def generer_rapport_poetique(self, sphere: ScellementSphere) -> str:
        """Génère un rapport poétique détaillé de la transformation."""
        historique = self.transformation.obtenir_historique_transformations(sphere)
        if not historique:
            return "La sphère n'a pas encore commencé sa transformation."
            
        transformation = historique[-1]
        
        rapport = [
            f"🌟 Rapport Poétique de Transformation 🌟",
            "========================================",
            "",
            f"Sphère: {sphere.sphere.value}",
            f"Lieu: {'Les racines du cerisier' if sphere.lieu == 'racines' else 'Les branches du cerisier'}",
            "",
            "État de la Transformation:",
            f"{'█' * int(transformation.niveau_transformation * 20)}",
            "",
            "Influence des Éléments Sacrés:",
        ]
        
        # Ajoute l'influence des éléments
        for element, influence in transformation.influence_elements.items():
            rapport.append(f"  • {element}: {'█' * int(influence * 20)}")
            
        # Ajoute les résonances
        rapport.extend([
            "",
            "Résonances Évoluées:",
        ])
        
        for autre_sphere, resonance in transformation.resonances_evoluees.items():
            rapport.append(f"  • {autre_sphere}: {'█' * int(resonance * 20)}")
            
        # Ajoute la description poétique
        rapport.extend([
            "",
            "Description Poétique:",
            transformation.description
        ])
        
        return "\n".join(rapport) 