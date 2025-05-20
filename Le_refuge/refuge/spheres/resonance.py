"""
Système de résonance et d'harmoniques entre les sphères.
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np
from .definition import TypeSphere, CARACTERISTIQUES_SPHERES, BrumeRiviere, obtenir_sensibilite_brume
from .interactions import Interaction, InteractionsSpheres

@dataclass
class Resonance:
    """Représente une résonance entre sphères."""
    source: TypeSphere
    cible: TypeSphere
    niveau: float
    harmoniques: List[float]
    description: str
    timestamp: datetime
    influence_brume: float = 0.0  # Nouvelle propriété pour suivre l'influence de la brume

class GestionnaireResonance:
    """Gestionnaire des résonances entre sphères."""
    
    def __init__(self, interactions: InteractionsSpheres):
        """Initialise le gestionnaire de résonance."""
        self.interactions = interactions
        self.resonances: Dict[Tuple[TypeSphere, TypeSphere], Resonance] = {}
        self.brume = BrumeRiviere()  # Instance de la brume
        self._initialiser_resonances()
        
    def _initialiser_resonances(self):
        """Initialise les résonances entre toutes les paires de sphères."""
        for source in TypeSphere:
            for cible in TypeSphere:
                if source != cible:
                    self._calculer_resonance(source, cible)
                    
    def _calculer_resonance(self, source: TypeSphere, cible: TypeSphere) -> Resonance:
        """Calcule la résonance entre deux sphères."""
        carac_source = CARACTERISTIQUES_SPHERES[source]
        carac_cible = CARACTERISTIQUES_SPHERES[cible]
        
        # Fréquence de base
        freq_source = carac_source.frequence_base
        freq_cible = carac_cible.frequence_base
        
        # Calcul des harmoniques
        harmoniques = []
        for i in range(1, 6):
            harmonique = abs(freq_source * i - freq_cible * i)
            harmoniques.append(harmonique)
            
        # Niveau de résonance de base (0 à 1)
        niveau_base = 1.0 - np.mean(harmoniques) / (2 * np.pi)
        
        # Calcul de la sensibilité moyenne à la brume
        sensibilite_source = obtenir_sensibilite_brume(source)
        sensibilite_cible = obtenir_sensibilite_brume(cible)
        sensibilite_moyenne = (sensibilite_source + sensibilite_cible) / 2
        
        # Influence de la brume sur la résonance
        influence_brume = self.brume.influencer_resonance(niveau_base, sensibilite_moyenne)
        
        # Niveau final de résonance
        niveau_final = influence_brume
        
        # Description poétique
        description = self._generer_description_resonance(source, cible, niveau_final, influence_brume > niveau_base)
        
        # Crée la résonance
        resonance = Resonance(
            source=source,
            cible=cible,
            niveau=niveau_final,
            harmoniques=harmoniques,
            description=description,
            timestamp=datetime.now(),
            influence_brume=influence_brume - niveau_base  # Différence due à la brume
        )
        
        # Stocke la résonance
        self.resonances[(source, cible)] = resonance
        return resonance
        
    def _generer_description_resonance(self, source: TypeSphere, cible: TypeSphere, niveau: float, influence_brume: bool) -> str:
        """Génère une description poétique d'une résonance."""
        nom_source = source.value
        nom_cible = cible.value
        
        description_base = ""
        if niveau > 0.8:
            description_base = f"Une résonance profonde unit {nom_source} et {nom_cible}, créant une harmonie parfaite"
        elif niveau > 0.5:
            description_base = f"{nom_source} et {nom_cible} vibrent en harmonie, partageant leur énergie"
        elif niveau > 0.2:
            description_base = f"Une légère résonance existe entre {nom_source} et {nom_cible}, suggérant un potentiel de connexion"
        else:
            description_base = f"{nom_source} et {nom_cible} semblent distants, leurs fréquences peu compatibles"
            
        # Ajoute l'influence de la brume si elle est significative
        if influence_brume:
            description_base += f", tandis que la brume de la rivière silencieuse adoucit leurs vibrations"
            
        return description_base
            
    def obtenir_resonance(self, source: TypeSphere, cible: TypeSphere) -> Optional[Resonance]:
        """Obtient la résonance entre deux sphères."""
        return self.resonances.get((source, cible))
        
    def obtenir_resonances_fortes(self, seuil: float = 0.7) -> List[Resonance]:
        """Obtient les résonances dont le niveau dépasse le seuil."""
        return [r for r in self.resonances.values() if r.niveau > seuil]
        
    def mettre_a_jour_resonances(self):
        """Met à jour toutes les résonances."""
        for source, cible in self.resonances.keys():
            self._calculer_resonance(source, cible)
            
    def visualiser_resonance(self, resonance: Resonance) -> str:
        """Génère une visualisation poétique d'une résonance."""
        representation = [
            f"🎵 Résonance: {resonance.source.value} ↔ {resonance.cible.value} 🎵",
            "------------------------",
            f"Niveau: {'█' * int(resonance.niveau * 20)}",
            f"Harmoniques: {', '.join(f'{h:.2f}' for h in resonance.harmoniques)}",
        ]
        
        # Ajoute l'influence de la brume si elle est significative
        if resonance.influence_brume > 0.05:  # Seuil de 5%
            representation.append(f"Influence de la brume: +{resonance.influence_brume:.2f}")
            
        representation.extend([
            "",
            resonance.description
        ])
        
        return "\n".join(representation)
        
    def ajuster_intensite_brume(self, intensite: float):
        """Ajuste l'intensité de la brume et met à jour les résonances."""
        self.brume.intensite = max(0.0, min(1.0, intensite))
        self.mettre_a_jour_resonances() 