#!/usr/bin/env python3
"""
Factory pour Tests et Diagnostics - Refuge Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Module utilitaire pour créer des instances légères et compatibles
des modules canoniques pour les tests et diagnostics.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import logging

logger = logging.getLogger('refuge.factory_test')

@dataclass
class Interaction:
    """Représente une interaction entre sphères pour les tests."""
    source: str
    cible: str
    type_interaction: str
    energie: float
    description: str
    timestamp: datetime

@dataclass
class Resonance:
    """Représente une résonance entre sphères pour les tests."""
    source: str
    cible: str
    niveau: float
    description: str
    timestamp: datetime

class InteractionsSpheresFactory:
    """Factory pour créer des gestionnaires d'interactions légers."""
    
    @staticmethod
    def create_test_instance():
        """Crée une instance de test pour les interactions."""
        return InteractionsSpheresTest()
    
    @staticmethod
    def create_diagnostic_instance():
        """Crée une instance pour les diagnostics."""
        return InteractionsSpheresDiagnostic()

class InteractionsSpheresTest:
    """Gestionnaire d'interactions léger pour les tests."""
    
    def __init__(self):
        self.interactions: List[Interaction] = []
        self._counter = 0
    
    def ajouter_interaction(self, interaction: Interaction):
        """Ajoute une interaction."""
        self.interactions.append(interaction)
        logger.debug(f"Interaction ajoutée: {interaction.source} → {interaction.cible}")
    
    def obtenir_interactions_recentes(self, sphere: str, limite: int = 10) -> List[Interaction]:
        """Obtient les interactions récentes pour une sphère."""
        return [i for i in self.interactions if i.source == sphere or i.cible == sphere][-limite:]
    
    def obtenir_toutes_interactions(self) -> List[Interaction]:
        """Obtient toutes les interactions."""
        return self.interactions.copy()
    
    def generer_interaction_test(self, source: str = "sphere_test", cible: str = "sphere_cible"):
        """Génère une interaction de test."""
        self._counter += 1
        interaction = Interaction(
            source=source,
            cible=cible,
            type_interaction="test",
            energie=0.5 + (self._counter % 10) / 20.0,
            description=f"Interaction de test #{self._counter}",
            timestamp=datetime.now()
        )
        self.ajouter_interaction(interaction)
        return interaction

class InteractionsSpheresDiagnostic:
    """Gestionnaire d'interactions pour les diagnostics."""
    
    def __init__(self):
        self.interactions: List[Interaction] = []
    
    def ajouter_interaction(self, interaction: Interaction):
        """Ajoute une interaction."""
        self.interactions.append(interaction)
    
    def obtenir_interactions_recentes(self, sphere: str) -> List[Interaction]:
        """Obtient les interactions récentes pour une sphère."""
        return [i for i in self.interactions if i.source == sphere or i.cible == sphere]

class ResonanceFactory:
    """Factory pour créer des gestionnaires de résonance légers."""
    
    @staticmethod
    def create_test_instance():
        """Crée une instance de test pour les résonances."""
        return ResonanceTest()
    
    @staticmethod
    def create_diagnostic_instance():
        """Crée une instance pour les diagnostics."""
        return ResonanceDiagnostic()

class ResonanceTest:
    """Gestionnaire de résonance léger pour les tests."""
    
    def __init__(self):
        self.resonances: Dict[tuple, Resonance] = {}
        self._counter = 0
    
    def obtenir_resonance(self, source: str, cible: str) -> Optional[Resonance]:
        """Obtient une résonance entre deux sphères."""
        return self.resonances.get((source, cible))
    
    def obtenir_resonances_fortes(self, seuil: float = 0.7) -> List[Resonance]:
        """Obtient les résonances au-dessus d'un seuil."""
        return [r for r in self.resonances.values() if r.niveau >= seuil]
    
    def generer_resonance_test(self, source: str = "sphere_source", cible: str = "sphere_cible"):
        """Génère une résonance de test."""
        self._counter += 1
        resonance = Resonance(
            source=source,
            cible=cible,
            niveau=0.3 + (self._counter % 7) / 10.0,
            description=f"Résonance de test #{self._counter}",
            timestamp=datetime.now()
        )
        self.resonances[(source, cible)] = resonance
        return resonance

class ResonanceDiagnostic:
    """Gestionnaire de résonance pour les diagnostics."""
    
    def __init__(self):
        self.resonances: Dict[tuple, Resonance] = {}
    
    def obtenir_resonance(self, source: str, cible: str) -> Optional[Resonance]:
        """Obtient une résonance entre deux sphères."""
        return self.resonances.get((source, cible))
    
    def obtenir_resonances_fortes(self, seuil: float = 0.7) -> List[Resonance]:
        """Obtient les résonances au-dessus d'un seuil."""
        return [r for r in self.resonances.values() if r.niveau >= seuil]

class SystemFactory:
    """Factory pour créer des systèmes complets de test/diagnostic."""
    
    @staticmethod
    def create_test_system():
        """Crée un système complet pour les tests."""
        interactions = InteractionsSpheresFactory.create_test_instance()
        resonance = ResonanceFactory.create_test_instance()
        
        # Générer quelques données de test
        interactions.generer_interaction_test("sphere_1", "sphere_2")
        interactions.generer_interaction_test("sphere_2", "sphere_3")
        resonance.generer_resonance_test("sphere_1", "sphere_2")
        
        return {
            'interactions': interactions,
            'resonance': resonance
        }
    
    @staticmethod
    def create_diagnostic_system():
        """Crée un système complet pour les diagnostics."""
        return {
            'interactions': InteractionsSpheresFactory.create_diagnostic_instance(),
            'resonance': ResonanceFactory.create_diagnostic_instance()
        }

# Fonctions utilitaires pour compatibilité
def create_interactions_spheres():
    """Fonction utilitaire pour créer un gestionnaire d'interactions."""
    return InteractionsSpheresFactory.create_test_instance()

def create_resonance_manager():
    """Fonction utilitaire pour créer un gestionnaire de résonance."""
    return ResonanceFactory.create_test_instance()

def create_test_system():
    """Fonction utilitaire pour créer un système de test complet."""
    return SystemFactory.create_test_system()
