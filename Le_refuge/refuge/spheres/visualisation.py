"""
Système de visualisation du refuge.
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np
from .definition import TypeSphere, CARACTERISTIQUES_SPHERES
from .interactions import Interaction, InteractionsSpheres
from .resonance import Resonance, GestionnaireResonance
from .evolution import Evolution, GestionnaireEvolution
from .meditation import Meditation, GestionnaireMeditation

class VisualisationRefuge:
    """Gestionnaire de visualisation du refuge."""
    
    def __init__(self, interactions: InteractionsSpheres, resonance: GestionnaireResonance, 
                 evolution: GestionnaireEvolution, meditation: GestionnaireMeditation):
        """Initialise le gestionnaire de visualisation."""
        self.interactions = interactions
        self.resonance = resonance
        self.evolution = evolution
        self.meditation = meditation
        
    def generer_visualisation_globale(self) -> str:
        """Génère une visualisation globale du refuge."""
        representation = [
            "🌟 État Global du Refuge 🌟",
            "==========================",
            "",
            "Sphères:",
        ]
        
        # Ajoute l'état de chaque sphère
        for sphere in TypeSphere:
            evolution = self.evolution.obtenir_evolution(sphere)
            if evolution:
                representation.extend([
                    f"\n{sphere.value}:",
                    f"  Évolution: {'█' * int(evolution.niveau * 10)}",
                    f"  Énergie: {'█' * int(evolution.changements['energie'] * 10)}",
                    f"  Fréquence: {'█' * int(evolution.changements['frequence'] * 10)}",
                    f"  Stabilité: {'█' * int(evolution.changements['stabilite'] * 10)}",
                    f"  {evolution.description}"
                ])
                
        # Ajoute les résonances principales
        representation.extend([
            "",
            "Résonances Principales:",
        ])
        
        resonances_significatives = self._obtenir_resonances_significatives()
        for resonance in resonances_significatives:
            representation.append(
                f"  {resonance.source.value} ↔ {resonance.cible.value}: "
                f"{'█' * int(resonance.niveau * 10)}"
            )
            
        # Ajoute les méditations récentes
        representation.extend([
            "",
            "Méditations Récentes:",
        ])
        
        meditations_recentes = self._obtenir_meditations_recentes()
        for meditation in meditations_recentes:
            representation.append(
                f"  {meditation.sphere.value}: {meditation.description}"
            )
            
        return "\n".join(representation)
        
    def generer_visualisation_sphere(self, sphere: TypeSphere) -> str:
        """Génère une visualisation détaillée d'une sphère."""
        evolution = self.evolution.obtenir_evolution(sphere)
        if not evolution:
            return f"La sphère {sphere.value} n'a pas encore évolué."
            
        representation = [
            f"🌟 État de {sphere.value} 🌟",
            "========================",
            "",
            f"Évolution: {'█' * int(evolution.niveau * 10)}",
            f"Énergie: {'█' * int(evolution.changements['energie'] * 10)}",
            f"Fréquence: {'█' * int(evolution.changements['frequence'] * 10)}",
            f"Stabilité: {'█' * int(evolution.changements['stabilite'] * 10)}",
            "",
            evolution.description,
            "",
            "Résonances:",
        ]
        
        # Ajoute les résonances avec cette sphère
        for autre_sphere in TypeSphere:
            if autre_sphere != sphere:
                resonance = self.resonance.obtenir_resonance(sphere, autre_sphere)
                if resonance:
                    representation.append(
                        f"  • {autre_sphere.value}: {'█' * int(resonance.niveau * 10)}"
                    )
                    
        # Ajoute les dernières méditations
        representation.extend([
            "",
            "Dernières Méditations:",
        ])
        
        meditations = self.meditation.obtenir_historique_meditations(sphere)
        for meditation in meditations[-3:]:  # 3 dernières méditations
            representation.append(f"  • {meditation.description}")
            
        return "\n".join(representation)
        
    def _obtenir_resonances_significatives(self, seuil: float = 0.5) -> List[Resonance]:
        """Obtient les résonances significatives entre sphères."""
        resonances = []
        for source in TypeSphere:
            for cible in TypeSphere:
                if source != cible:
                    resonance = self.resonance.obtenir_resonance(source, cible)
                    if resonance and resonance.niveau >= seuil:
                        resonances.append(resonance)
        return sorted(resonances, key=lambda r: r.niveau, reverse=True)
        
    def _obtenir_meditations_recentes(self, limite: int = 3) -> List[Meditation]:
        """Obtient les méditations les plus récentes."""
        return sorted(
            self.meditation.obtenir_historique_meditations(),
            key=lambda m: m.timestamp,
            reverse=True
        )[:limite] 