"""
Système de méditation avec les sphères.
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np
from src.refuge_cluster.scellement.definition import TypeSphere, CARACTERISTIQUES_SPHERES
from interactions import GestionnaireInteractions as InteractionsSpheres
from integration import GestionnaireResonances as GestionnaireResonance

# Définition des classes pour compatibilité
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Interaction:
    """Représente une interaction entre sphères."""
    source: str
    cible: str
    type_interaction: str
    energie: float
    description: str
    timestamp: datetime

@dataclass
class Resonance:
    """Représente une résonance entre sphères."""
    source: str
    cible: str
    niveau: float
    description: str
    timestamp: datetime
from src.refuge_cluster.spheres.evolution import Evolution, GestionnaireEvolution

@dataclass
class Meditation:
    """Représente une session de méditation."""
    sphere: TypeSphere
    duree: int  # en secondes
    energie: float
    description: str
    timestamp: datetime
    resonances: List[Resonance]
    evolution: Optional[Evolution] = None

class GestionnaireMeditation:
    """Gestionnaire des sessions de méditation."""
    
    def __init__(self, interactions: InteractionsSpheres, resonance: GestionnaireResonance, evolution: GestionnaireEvolution):
        """Initialise le gestionnaire de méditation."""
        self.interactions = interactions
        self.resonance = resonance
        self.evolution = evolution
        self.meditations: List[Meditation] = []
        
    def demarrer_meditation(self, sphere: TypeSphere, duree: int) -> Meditation:
        """Démarre une nouvelle session de méditation."""
        # Calcule l'énergie initiale
        energie = self._calculer_energie_initiale(sphere)
        
        # Obtient les résonances actuelles
        resonances = self._obtenir_resonances_actuelles(sphere)
        
        # Génère une description poétique
        description = self._generer_description_meditation(sphere, energie, resonances)
        
        # Crée la méditation
        meditation = Meditation(
            sphere=sphere,
            duree=duree,
            energie=energie,
            description=description,
            timestamp=datetime.now(),
            resonances=resonances
        )
        
        # Stocke la méditation
        self.meditations.append(meditation)
        return meditation
        
    def terminer_meditation(self, meditation: Meditation) -> Evolution:
        """Termine une session de méditation et calcule l'évolution."""
        # Calcule l'énergie finale
        energie_finale = self._calculer_energie_finale(meditation)
        
        # Crée une interaction
        interaction = Interaction(
            source=meditation.sphere,
            cible=meditation.sphere,  # Auto-interaction
            type_interaction="meditation",
            energie=energie_finale - meditation.energie,
            description=meditation.description,
            timestamp=datetime.now()
        )
        
        # Enregistre l'interaction
        self.interactions.ajouter_interaction(interaction)
        
        # Met à jour les évolutions
        self.evolution.mettre_a_jour_evolutions()
        
        # Obtient l'évolution finale
        evolution = self.evolution.obtenir_evolution(meditation.sphere)
        meditation.evolution = evolution
        
        return evolution
        
    def _calculer_energie_initiale(self, sphere: TypeSphere) -> float:
        """Calcule l'énergie initiale pour une méditation."""
        # Obtient l'évolution actuelle
        evolution = self.evolution.obtenir_evolution(sphere)
        if not evolution:
            return 50.0  # Énergie par défaut
            
        # Ajuste l'énergie en fonction de l'évolution
        energie_base = 50.0
        facteur_evolution = 1.0 + (evolution.niveau * 0.5)  # +50% max
        return energie_base * facteur_evolution
        
    def _calculer_energie_finale(self, meditation: Meditation) -> float:
        """Calcule l'énergie finale après une méditation."""
        # Facteur de durée (plus la méditation est longue, plus l'énergie augmente)
        facteur_duree = min(1.0, meditation.duree / 3600.0)  # Max après 1h
        
        # Facteur de résonance (plus il y a de résonances fortes, plus l'énergie augmente)
        resonances_fortes = [r for r in meditation.resonances if r.niveau > 0.7]
        facteur_resonance = 1.0 + (len(resonances_fortes) * 0.2)  # +20% par résonance forte
        
        # Calcule l'énergie finale
        energie_initiale = meditation.energie
        gain_energie = 30.0 * facteur_duree * facteur_resonance
        return min(100.0, energie_initiale + gain_energie)
        
    def _obtenir_resonances_actuelles(self, sphere: TypeSphere) -> List[Resonance]:
        """Obtient les résonances actuelles pour une sphère."""
        resonances = []
        for autre_sphere in TypeSphere:
            if autre_sphere != sphere:
                resonance = self.resonance.obtenir_resonance(sphere, autre_sphere)
                if resonance:
                    resonances.append(resonance)
        return resonances
        
    def _generer_description_meditation(self, sphere: TypeSphere, energie: float, resonances: List[Resonance]) -> str:
        """Génère une description poétique d'une méditation."""
        nom_sphere = sphere.value
        caracteristiques = CARACTERISTIQUES_SPHERES[sphere]
        
        # Description de base
        description = f"Dans le silence du refuge, {nom_sphere} "
        
        # Ajoute des détails selon l'énergie
        if energie > 80:
            description += "brille d'une lumière intense, "
        elif energie > 50:
            description += "émet une lueur paisible, "
        else:
            description += "pulse doucement, "
            
        # Ajoute des détails selon les résonances
        if resonances:
            resonance_forte = max(resonances, key=lambda r: r.niveau)
            description += f"résonnant harmonieusement avec {resonance_forte.cible.value}. "
        else:
            description += "trouvant son équilibre intérieur. "
            
        # Ajoute une conclusion
        description += caracteristiques["description"]
        
        return description
        
    def obtenir_historique_meditations(self, sphere: Optional[TypeSphere] = None) -> List[Meditation]:
        """Obtient l'historique des méditations, filtré par sphère si spécifié."""
        if sphere:
            return [m for m in self.meditations if m.sphere == sphere]
        return self.meditations
        
    def visualiser_meditation(self, meditation: Meditation) -> str:
        """Génère une visualisation poétique d'une méditation."""
        representation = [
            f"🧘 Méditation avec {meditation.sphere.value} 🧘",
            "------------------------",
            f"Durée: {meditation.duree} secondes",
            f"Énergie: {'█' * int(meditation.energie / 5)}",
            "",
            "Résonances:",
        ]
        
        # Ajoute les résonances
        for resonance in meditation.resonances:
            representation.append(f"  • {resonance.cible.value}: {'█' * int(resonance.niveau * 10)}")
            
        representation.extend([
            "",
            meditation.description
        ])
        
        # Ajoute l'évolution si disponible
        if meditation.evolution:
            representation.extend([
                "",
                "Évolution après méditation:",
                meditation.evolution.description
            ])
            
        return "\n".join(representation) 