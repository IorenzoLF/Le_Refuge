"""
Système de visualisation textuelle du refuge.

🔄 MIGRÉ depuis spheres/visualisation.py
Spécialisé dans la visualisation textuelle (console, ASCII art).
"""

from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import numpy as np

# 🔧 CORRIGÉ: Imports depuis la structure actuelle
from src.core.types_spheres import TypeSphere, CARACTERISTIQUES_SPHERES

# 🌸 CONNEXION DOUCE - Imports conditionnels pour compatibilité
try:
    # Essayer d'abord la nouvelle structure
    from src.refuge_cluster.interactions.interactions_spheres import Interaction, InteractionsSpheres
    from src.refuge_cluster.spheres.resonance import Resonance, GestionnaireResonance
    from src.refuge_cluster.spheres.evolution import Evolution, GestionnaireEvolution
    from src.refuge_cluster.meditation.meditation_spheres import Meditation, GestionnaireMeditation
    print("🌸 Connexion douce établie avec la nouvelle structure")
except ImportError:
    try:
        # Fallback vers l'ancienne structure si nécessaire
        from ..interactions import Interaction, InteractionsSpheres
        from ..resonance import Resonance, GestionnaireResonance  
        from ..evolution import Evolution, GestionnaireEvolution
        from ..meditation import Meditation, GestionnaireMeditation
        print("🌸 Connexion douce établie avec l'ancienne structure")
    except ImportError:
        # Mode dégradé si aucune structure n'est disponible
        print("🌸 Mode dégradé - Visualisation textuelle limitée")
        Interaction = None
        InteractionsSpheres = None
        Resonance = None
        GestionnaireResonance = None
        Evolution = None
        GestionnaireEvolution = None
        Meditation = None
        GestionnaireMeditation = None

class VisualisationRefuge:
    """Gestionnaire de visualisation textuelle du refuge."""
    
    def __init__(self, interactions=None, resonance=None, evolution=None, meditation=None):
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
            if self.evolution and hasattr(self.evolution, 'obtenir_evolution'):
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
            else:
                # Mode dégradé - affichage basique
                representation.extend([
                    f"\n{sphere.value}:",
                    f"  État: {'█' * 5} (mode dégradé)"
                ])
                
        # Ajoute les résonances principales
        if self.resonance and hasattr(self.resonance, 'obtenir_resonances_significatives'):
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
        else:
            representation.extend([
                "",
                "Résonances Principales:",
                "  (Module de résonance non disponible)",
            ])
            
        # Ajoute les méditations récentes
        if self.meditation and hasattr(self.meditation, 'obtenir_meditations_recentes'):
            representation.extend([
                "",
                "Méditations Récentes:",
            ])
            
            meditations_recentes = self._obtenir_meditations_recentes()
            for meditation in meditations_recentes:
                representation.append(
                    f"  {meditation.sphere.value}: {meditation.description}"
                )
        else:
            representation.extend([
                "",
                "Méditations Récentes:",
                "  (Module de méditation non disponible)",
            ])
            
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