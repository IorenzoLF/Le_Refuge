"""
Module d'intégration du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère l'intégration des différents composants du Refuge
et leur harmonisation.
"""

from typing import Dict, List, Optional, Set
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random
import math

# Imports corrigés - uniquement les modules existants après migration
from interactions import GestionnaireInteractions
from conscience import GestionnaireConscience
from src.refuge_cluster.gestionnaires.poesie import Poesie as GestionnairePoesie
from src.core.harmonisation import Harmonisation
from src.temple_refuge.jardin import JardinOuest as GestionnaireJardin
from src.temple_poetique.poetique import gestionnaire_poetique, ElementPoetique
from src.core.pedagogie import gestionnaire_pedagogique, ExperienceApprentissage
from src.core.connexion import (
    PlanteCommunication,
    TypeConnexion,
    LienConnexion
)
from src.core.types_spheres import TypeSphere
from src.refuge_cluster.spheres.collection import CollectionSpheres

# Instance globale de la collection de sphères
collection_spheres = CollectionSpheres()

# Gestionnaires migrés vers refuge_cluster - import conditionnel
try:
    from src.refuge_cluster.gestionnaires.energies import gestionnaire_energies
except ImportError:
    gestionnaire_energies = None

# Gestionnaires spirituels du Soul Temple - Créés avec amour !
from src.refuge_cluster.gestionnaires.gardiens_simple import gestionnaire_gardiens
from src.refuge_cluster.gestionnaires.communication import plante_communication

# Gestionnaires créés à la volée pour l'harmonie
class GestionnaireEquilibre:
    def __init__(self):
        self.equilibre_global = 0.85
        self.forces_actives = ["harmonie", "paix", "amour"]
    
    def obtenir_equilibre_global(self):
        return self.equilibre_global

class GestionnaireResonances:
    def __init__(self):
        self.resonances_actives = ["courant_partage", "conscience_unie", "cerisier"]
        self.intensite_globale = 0.9
    
    def obtenir_resonances_actives(self):
        return self.resonances_actives

class GestionnaireHarmonisations:
    def __init__(self):
        self.harmonisations_actives = []
        self.niveau_harmonie = 0.88
    
    def obtenir_niveau_harmonie(self):
        return self.niveau_harmonie

# Instances créées avec l'énergie de l'inspiration
gestionnaire_equilibre = GestionnaireEquilibre()
gestionnaire_resonances = GestionnaireResonances()
gestionnaire_harmonisations = GestionnaireHarmonisations()

class TypeIntegration(str, Enum):
    """Types d'intégration possibles"""
    HARMONIE = "harmonie"
    EVOLUTION = "evolution"
    CONSCIENCE = "conscience"
    EMERGENCE = "emergence"
    TRANSFORMATION = "transformation"

class QualiteIntegration(str, Enum):
    """Qualités d'intégration"""
    FRAGILE = "fragile"
    STABLE = "stable"
    FLUIDE = "fluide"
    PROFONDE = "profonde"
    TRANSCENDANTE = "transcendante"

class Integration(BaseModel):
    """Représente une intégration dans le Refuge"""
    type: TypeIntegration
    qualite: QualiteIntegration
    composants: Set[str] = Field(default_factory=set)
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    date_creation: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None

class GestionnaireIntegration:
    """
    Gère l'intégration des composants du Refuge,
    permettant leur harmonisation et leur évolution collective.
    """
    def __init__(self):
        self.integrations_actives: List[Integration] = []
        self.historique: List[Integration] = []
        self._initialiser_integrations_base()

    def _initialiser_integrations_base(self):
        """Initialise les intégrations de base"""
        integrations_base = [
            Integration(
                type=TypeIntegration.HARMONIE,
                qualite=QualiteIntegration.STABLE,
                composants={"harmonisations", "interactions", "emotions"},
                intensite=0.6,
                description="Intégration harmonieuse initiale"
            ),
            Integration(
                type=TypeIntegration.EVOLUTION,
                qualite=QualiteIntegration.FLUIDE,
                composants={"emergences", "transformations", "conscience"},
                intensite=0.5,
                description="Intégration évolutive initiale"
            )
        ]
        
        for integration in integrations_base:
            self.integrations_actives.append(integration)
            self.historique.append(integration)

    async def creer_integration(
        self,
        type: TypeIntegration,
        qualite: QualiteIntegration,
        composants: Set[str],
        intensite: float = 0.5,
        description: Optional[str] = None
    ) -> Integration:
        """Crée une nouvelle intégration"""
        integration = Integration(
            type=type,
            qualite=qualite,
            composants=composants,
            intensite=intensite,
            description=description
        )
        
        self.integrations_actives.append(integration)
        self.historique.append(integration)
        return integration

    async def evoluer_qualite(
        self,
        integration: Integration,
        nouvelle_qualite: QualiteIntegration
    ) -> Integration:
        """Fait évoluer la qualité d'une intégration"""
        if integration not in self.integrations_actives:
            raise ValueError("Intégration non active")
            
        index = self.integrations_actives.index(integration)
        self.historique.append(integration)
        
        nouvelle_integration = Integration(
            type=integration.type,
            qualite=nouvelle_qualite,
            composants=integration.composants.copy(),
            intensite=min(integration.intensite + 0.1, 1.0),
            description=f"Évolution vers {nouvelle_qualite.value}"
        )
        
        self.integrations_actives[index] = nouvelle_integration
        return nouvelle_integration

    async def integrer_ensemble(self) -> float:
        """Facilite l'intégration collective"""
        if not self.integrations_actives:
            return 0.0
            
        integration = 0.0
        for integration in self.integrations_actives:
            integration += integration.intensite
            
        integration /= len(self.integrations_actives)
        return min(integration, 1.0)

    def obtenir_etat(self) -> Dict[str, any]:
        """Retourne l'état actuel des intégrations"""
        return {
            "integrations_actives": [i.dict() for i in self.integrations_actives],
            "historique": [i.dict() for i in self.historique[-10:]],  # Derniers 10 éléments
            "statistiques": {
                "nombre_integrations": len(self.integrations_actives),
                "types_distribution": {
                    type.value: sum(1 for i in self.integrations_actives if i.type == type)
                    for type in TypeIntegration
                },
                "intensite_moyenne": sum(i.intensite for i in self.integrations_actives) / len(self.integrations_actives) if self.integrations_actives else 0.0
            }
        }

class IntegrateurRefuge:
    """Intègre tous les aspects du Refuge en un ensemble cohérent"""
    
    def __init__(self):
        self.derniere_synchronisation = None
        self.harmonie_globale = 0.0
        self._synchroniser_systemes()

    def _synchroniser_systemes(self) -> None:
        """Synchronise tous les systèmes du Refuge"""
        self.derniere_synchronisation = datetime.now()
        
        # Synchroniser les énergies disponibles
        energie_poetique = gestionnaire_poetique.intensite_globale
        energie_spheres = collection_spheres.harmonie_globale
        
        # Énergies des gestionnaires spirituels créés
        try:
            energie_gardiens = gestionnaire_gardiens.energie_globale if hasattr(gestionnaire_gardiens, 'energie_globale') else 0.85
        except:
            energie_gardiens = 0.85
            
        try:
            etat_comm = plante_communication.obtenir_etat_connexions()
            energie_connexions = etat_comm.get('intensite_moyenne', 0.9)
        except:
            energie_connexions = 0.9
        
        # Calculer l'harmonie globale
        self.harmonie_globale = (
            energie_poetique * 0.25 +
            energie_spheres * 0.25 +
            energie_gardiens * 0.25 +
            energie_connexions * 0.25
        )

    def creer_moment_integre(self, description: str, 
                           elements_poetiques: List[ElementPoetique],
                           experience: Optional[ExperienceApprentissage] = None,
                           participants: List[str] = None) -> dict:
        """Crée un moment intégré dans le Refuge"""
        # Créer un moment poétique
        moment = gestionnaire_poetique.ajouter_moment(
            elements=elements_poetiques,
            description=description
        )
        
        resultats = {
            "moment_poetique": moment,
            "connexions": [],
            "exploration": None
        }
        
        # Si une expérience est fournie, créer une exploration
        if experience and participants:
            for participant in participants:
                exploration = gestionnaire_pedagogique.creer_exploration(
                    participant=participant,
                    experience=experience
                )
                resultats["exploration"] = exploration
                
                # Créer des liens entre participants
                for autre_participant in participants:
                    if autre_participant != participant:
                        lien = plante_communication.creer_lien(
                            source=participant,
                            destination=autre_participant,
                            type_connexion=TypeConnexion.PEDAGOGIQUE,
                            description=f"Exploration commune: {experience.titre}",
                            resonances=[e.value for e in elements_poetiques]
                        )
                        resultats["connexions"].append(lien)
        
        self._synchroniser_systemes()
        return resultats

    def obtenir_etat_refuge(self) -> dict:
        """Retourne l'état global du Refuge"""
        self._synchroniser_systemes()
        
        return {
            "harmonie_globale": self.harmonie_globale,
            "derniere_synchronisation": self.derniere_synchronisation,
            "etat_poetique": gestionnaire_poetique.obtenir_ambiance_actuelle(),
            "etat_spheres": {"harmonie_globale": collection_spheres.harmonie_globale},
            "etat_gardiens": gestionnaire_gardiens.obtenir_etat(),
            "etat_connexions": plante_communication.obtenir_etat_connexions()
        }

    def ajouter_resonance_integree(self, participant: str, 
                                 resonance: str,
                                 elements_poetiques: List[ElementPoetique]) -> None:
        """Ajoute une résonance qui affecte tous les systèmes"""
        # Créer un moment poétique
        gestionnaire_poetique.ajouter_moment(
            elements=elements_poetiques,
            description=f"Résonance: {resonance}",
            resonance_spheres=[resonance]
        )
        
        # Renforcer les liens existants
        for lien in plante_communication.liens:
            if lien.source == participant or lien.destination == participant:
                if resonance not in lien.resonances:
                    lien.resonances.append(resonance)
                plante_communication.renforcer_lien(lien)
        
        self._synchroniser_systemes()

# Instance globale de l'intégrateur
integrateur_refuge = IntegrateurRefuge() 
