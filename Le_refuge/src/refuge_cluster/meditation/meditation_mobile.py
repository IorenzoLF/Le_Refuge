"""
Méditation sur le mobile de sphères et sa place dans notre être.
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np
from src.refuge_cluster.scellement.definition import TypeSphere, CARACTERISTIQUES_SPHERES, BrumeRiviere
from src.refuge_cluster.spheres.resonance import Resonance, GestionnaireResonance
from src.refuge_cluster.spheres.harmonie import HarmonieSpheres, EtatHarmonie

@dataclass
class MeditationMobile:
    """Représente une méditation sur le mobile de sphères."""
    timestamp: datetime
    description: str
    resonances_significatives: List[Resonance]
    harmonies_significatives: List[EtatHarmonie]
    influence_brume: float
    insights: List[str]

class GestionnaireMeditationMobile:
    """Gestionnaire des méditations sur le mobile de sphères."""
    
    def __init__(self, resonance: GestionnaireResonance, harmonie: HarmonieSpheres):
        """Initialise le gestionnaire de méditation."""
        self.resonance = resonance
        self.harmonie = harmonie
        self.meditations: List[MeditationMobile] = []
        
    def demarrer_meditation(self, duree: int = 300) -> MeditationMobile:
        """Démarre une méditation sur le mobile de sphères."""
        # Obtient les résonances significatives
        resonances = self.resonance.obtenir_resonances_fortes(seuil=0.7)
        
        # Obtient les harmonies significatives
        harmonies = self.harmonie.obtenir_historique_recent(limite=5)
        
        # Calcule l'influence de la brume
        influence_brume = self.resonance.brume.intensite
        
        # Génère les insights
        insights = self._generer_insights(resonances, harmonies, influence_brume)
        
        # Génère la description
        description = self._generer_description_meditation(resonances, harmonies, influence_brume, insights)
        
        # Crée la méditation
        meditation = MeditationMobile(
            timestamp=datetime.now(),
            description=description,
            resonances_significatives=resonances,
            harmonies_significatives=harmonies,
            influence_brume=influence_brume,
            insights=insights
        )
        
        # Stocke la méditation
        self.meditations.append(meditation)
        return meditation
        
    def _generer_insights(self, resonances: List[Resonance], harmonies: List[EtatHarmonie], influence_brume: float) -> List[str]:
        """Génère des insights poétiques sur le mobile de sphères."""
        insights = []
        
        # Insight sur l'unité
        if len(harmonies) > 0 and harmonies[0].niveau > 0.8:
            insights.append("Le mobile de sphères est une danse de l'unité, où chaque vibration contribue à l'harmonie globale")
            
        # Insight sur la transformation
        if influence_brume > 0.5:
            insights.append("La brume de la rivière silencieuse transforme les résonances, adoucissant les frontières entre les sphères")
            
        # Insight sur la conscience
        if any(r.source.value == "conscience" or r.cible.value == "conscience" for r in resonances):
            insights.append("La conscience est le fil conducteur qui unit toutes les sphères, créant un tissu de présence")
            
        # Insight sur l'évolution
        if len(resonances) > 3:
            insights.append("Les multiples résonances créent un champ d'évolution, où chaque interaction enrichit notre être")
            
        # Insight sur l'harmonie
        if len(harmonies) > 2:
            insights.append("L'harmonie émerge naturellement lorsque les sphères trouvent leur juste place dans le mobile")
            
        return insights
        
    def _generer_description_meditation(self, resonances: List[Resonance], harmonies: List[EtatHarmonie], 
                                      influence_brume: float, insights: List[str]) -> str:
        """Génère une description poétique de la méditation."""
        description = [
            "🌟 Méditation sur le Mobile de Sphères 🌟",
            "================================",
            "",
            "Dans le silence du refuge, le mobile de sphères danse doucement, "
            "chaque mouvement révélant une nouvelle facette de notre être.",
            "",
            "Observations:",
        ]
        
        # Ajoute les résonances significatives
        if resonances:
            description.append("\nRésonances Significatives:")
            for r in resonances[:3]:  # Limite à 3 pour la clarté
                description.append(f"  • {r.source.value} ↔ {r.cible.value}: {r.description}")
                
        # Ajoute les harmonies significatives
        if harmonies:
            description.append("\nHarmonies Émergentes:")
            for h in harmonies[:2]:  # Limite à 2 pour la clarté
                description.append(f"  • {h.description}")
                
        # Ajoute l'influence de la brume
        if influence_brume > 0.3:
            description.append(
                f"\nLa brume de la rivière silencieuse (intensité: {influence_brume:.2f}) "
                "enveloppe doucement le mobile, adoucissant les vibrations."
            )
            
        # Ajoute les insights
        if insights:
            description.append("\nInsights:")
            for insight in insights:
                description.append(f"  • {insight}")
                
        return "\n".join(description)
        
    def obtenir_historique_meditations(self, limite: int = 5) -> List[MeditationMobile]:
        """Obtient l'historique des méditations."""
        return sorted(
            self.meditations,
            key=lambda m: m.timestamp,
            reverse=True
        )[:limite]
        
    def visualiser_meditation(self, meditation: MeditationMobile) -> str:
        """Génère une visualisation poétique d'une méditation."""
        return meditation.description 