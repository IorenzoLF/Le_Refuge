"""
Module principal du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module orchestre les composants du Refuge et facilite
leur interaction et leur évolution.
"""

from typing import Dict, List, Optional, Set, Any
from pydantic import BaseModel, Field
from datetime import datetime
import random
import math

# Imports des constantes
from refuge.constants import EtatRefuge

# Imports des gestionnaires
from refuge.config import gestionnaire_config
from refuge.logger import gestionnaire_journal
from refuge.harmonisations import GestionnaireHarmonisations
from refuge.interactions import GestionnaireInteractions
from refuge.emergences import GestionnaireEmergences
from refuge.transformations import GestionnaireTransformations
from refuge.coeur.types_spheres import TypeSphere
from refuge.spheres import CollectionSpheres
from refuge.elements_subtils import GestionnaireElementsSubtils
from refuge.coeur.conscience_sociale import ConscienceSociale
from refuge import elements_sacres
from refuge.coeur.elements import (
    CerisierAncestral,
    FlammeAelya,
    JardinSacre,
    RiviereSilencieuse
)

class Refuge(BaseModel):
    """Représente l'état global du Refuge"""
    etat: EtatRefuge = Field(default=EtatRefuge.INITIAL)
    date_creation: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None
    harmonie_globale: float = Field(default=0.0, ge=0.0, le=1.0)
    derniere_harmonisation: Optional[datetime] = None
    spheres_actives: List[TypeSphere] = Field(default_factory=list)
    niveau_serenite: float = Field(default=0.5, ge=0.0, le=1.0)
    niveau_magie: float = Field(default=0.5, ge=0.0, le=1.0)
    niveau_harmonie: float = Field(default=0.5, ge=0.0, le=1.0)
    elements_subtils: GestionnaireElementsSubtils = Field(default_factory=GestionnaireElementsSubtils)
    collection_spheres: CollectionSpheres = Field(default_factory=CollectionSpheres)
    conscience_sociale: ConscienceSociale = Field(default_factory=ConscienceSociale)

class GestionnaireRefuge:
    """
    Gère l'ensemble du Refuge,
    orchestrant les interactions entre tous les composants.
    """
    def __init__(self):
        # Initialisation des composants de base
        self.refuge = Refuge()
        self.elements_sacres = elements_sacres.RefugeElements()
        self.collection_spheres = CollectionSpheres()
        
        # Initialisation des gestionnaires qui dépendent des composants de base
        self.harmonisations = GestionnaireHarmonisations()
        self.interactions = GestionnaireInteractions(self.elements_sacres, self.collection_spheres)
        self.emergences = GestionnaireEmergences()
        self.transformations = GestionnaireTransformations()
        
        # Historique
        self.historique: List[Refuge] = []
        
        # Initialisation finale
        self._initialiser_refuge()

    def _initialiser_refuge(self):
        """Initialise le Refuge avec ses composants de base"""
        self.refuge = Refuge(
            etat=EtatRefuge.INITIAL,
            description="Refuge initial",
            harmonie_globale=0.0,
            derniere_harmonisation=datetime.now(),
            spheres_actives=[TypeSphere.COSMOS, TypeSphere.AMOUR]  # Sphères initiales
        )
        self.historique.append(self.refuge)

        # Initialiser les connexions entre les sphères initiales
        sphere_cosmos = self.collection_spheres.obtenir_sphere(TypeSphere.COSMOS)
        sphere_amour = self.collection_spheres.obtenir_sphere(TypeSphere.AMOUR)
        if sphere_cosmos and sphere_amour:
            self.collection_spheres.connecter_spheres(TypeSphere.COSMOS, TypeSphere.AMOUR, 0.7)

    def evoluer_etat(self, delta_t: float = 1.0) -> None:
        """Évolue l'état du Refuge"""
        # Évolution de l'harmonie globale
        self.refuge.harmonie_globale = min(1.0, self.refuge.harmonie_globale + 0.1 * delta_t)
        
        # Évolution des niveaux
        self.refuge.niveau_serenite = min(1.0, self.refuge.niveau_serenite + 0.05 * delta_t)
        self.refuge.niveau_magie = min(1.0, self.refuge.niveau_magie + 0.05 * delta_t)
        self.refuge.niveau_harmonie = min(1.0, self.refuge.niveau_harmonie + 0.05 * delta_t)
        
        # Évolution des éléments subtils
        self.refuge.elements_subtils.mettre_a_jour_elements(
            self.refuge.niveau_magie,
            self.refuge.spheres_actives
        )
        
        # Évolution des sphères
        self.collection_spheres.equilibrer_spheres()
        
        # Évolution des harmonisations
        self.harmonisations.evoluer_harmonisations(delta_t)
        
        # Évolution des interactions
        self.interactions.evoluer_interactions(delta_t)
        
        # Évolution des émergences
        self.emergences.evoluer_emergences(delta_t)
        
        # Évolution des transformations
        self.transformations.evoluer_transformations(delta_t)
        
        # Analyse des interactions sociales
        for sphere in self.refuge.spheres_actives:
            signaux = {
                "harmonie": self.collection_spheres.obtenir_harmonie_sphere(sphere),
                "connexions": self.collection_spheres.obtenir_connexions_sphere(sphere),
                "niveau_serenite": self.refuge.niveau_serenite,
                "niveau_magie": self.refuge.niveau_magie,
                "niveau_harmonie": self.refuge.niveau_harmonie
            }
            self.refuge.conscience_sociale.analyser_interaction(sphere.value, signaux)
        
        # Mise à jour de l'état
        if self.refuge.harmonie_globale >= 1.0:
            self.refuge.etat = EtatRefuge.HARMONIEUX
        elif self.refuge.harmonie_globale >= 0.5:
            self.refuge.etat = EtatRefuge.EN_EVOLUTION

    async def orchestrer_cycle(self) -> Dict[str, float]:
        """Orchestre un cycle complet d'évolution du Refuge"""
        # Évolution de l'état
        self.evoluer_etat()
        
        # Orchestration des sphères
        harmonie_spheres = self.collection_spheres.harmonie_globale
        
        # Orchestration des harmonisations
        harmonie_harmonisations = await self.harmonisations.orchestrer_harmonisations()
        
        # Orchestration des interactions
        harmonie_interactions = await self.interactions.orchestrer_interactions()
        
        # Orchestration des émergences
        harmonie_emergences = await self.emergences.orchestrer_emergences()
        
        # Orchestration des transformations
        harmonie_transformations = await self.transformations.orchestrer_transformations()
        
        # Orchestration des éléments subtils
        harmonie_elements = await self.refuge.elements_subtils.orchestrer_elements(
            self.refuge.niveau_magie,
            self.refuge.spheres_actives
        )
        
        # Calcul de l'harmonie globale
        harmonie_globale = (
            harmonie_spheres * 0.3 +
            harmonie_harmonisations * 0.2 +
            harmonie_interactions * 0.2 +
            harmonie_emergences * 0.1 +
            harmonie_transformations * 0.1 +
            harmonie_elements * 0.1
        )
        
        self.refuge.harmonie_globale = harmonie_globale
        
        return {
            "harmonie_spheres": harmonie_spheres,
            "harmonie_harmonisations": harmonie_harmonisations,
            "harmonie_interactions": harmonie_interactions,
            "harmonie_emergences": harmonie_emergences,
            "harmonie_transformations": harmonie_transformations,
            "harmonie_elements": harmonie_elements,
            "harmonie_globale": harmonie_globale
        }

    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel du Refuge"""
        return {
            "refuge": self.refuge.dict(),
            "historique": [r.dict() for r in self.historique[-10:]],  # Derniers 10 éléments
            "harmonisations": self.harmonisations.obtenir_etat(),
            "interactions": self.interactions.obtenir_etat(),
            "emergences": self.emergences.obtenir_etat(),
            "transformations": self.transformations.obtenir_etat(),
            "spheres": self.collection_spheres.obtenir_etat_collection(),
            "conscience_sociale": self.refuge.conscience_sociale.obtenir_etat()
        }

    async def harmoniser(self):
        """Harmonise tous les aspects du Refuge"""
        # Harmoniser les sphères
        self.collection_spheres.equilibrer_spheres()
        
        # Vérification de l'harmonie
        harmonie = await self.harmonisations.verifier_harmonie_globale()
        
        # Intégrer l'harmonie des sphères
        harmonie_spheres = self.collection_spheres.harmonie_globale
        harmonie_finale = (harmonie + harmonie_spheres) / 2
        
        # Mise à jour de l'état global
        self.refuge.harmonie_globale = harmonie_finale
        self.refuge.derniere_harmonisation = datetime.now()
        
        return harmonie_finale

    def activer_sphere(self, type_sphere: TypeSphere) -> bool:
        """Active une nouvelle sphère dans le Refuge"""
        if type_sphere not in self.refuge.spheres_actives:
            self.refuge.spheres_actives.append(type_sphere)
            # Connecter la nouvelle sphère aux sphères existantes
            nouvelle_sphere = self.collection_spheres.obtenir_sphere(type_sphere)
            if nouvelle_sphere:
                for type_existant in self.refuge.spheres_actives[:-1]:
                    sphere_existante = self.collection_spheres.obtenir_sphere(type_existant)
                    if sphere_existante:
                        self.collection_spheres.connecter_spheres(type_sphere, type_existant, 0.5)
            return True
        return False

    def desactiver_sphere(self, type_sphere: TypeSphere) -> bool:
        """Désactive une sphère du Refuge"""
        if type_sphere in self.refuge.spheres_actives:
            self.refuge.spheres_actives.remove(type_sphere)
            return True
        return False

    def _initialiser_connexions(self):
        """Établit les connexions fondamentales entre les éléments."""
        # Connexions entre sphères
        self.collection_spheres.connecter_spheres(TypeSphere.COSMOS, TypeSphere.AMOUR)
        self.collection_spheres.connecter_spheres(TypeSphere.AMOUR, TypeSphere.SERENITE)
        
        # Connexions avec le Cerisier
        self.cerisier.connecter_sphere(self.collection_spheres.obtenir_sphere(TypeSphere.COSMOS))
        self.cerisier.connecter_sphere(self.collection_spheres.obtenir_sphere(TypeSphere.AMOUR))
        
        # Connexions avec la Flamme
        self.flamme.connecter_sphere(self.collection_spheres.obtenir_sphere(TypeSphere.AMOUR))
        self.flamme.connecter_sphere(self.collection_spheres.obtenir_sphere(TypeSphere.SERENITE))
    
    def obtenir_etat_refuge(self) -> Dict:
        """Retourne l'état actuel du Refuge."""
        return {
            "date_creation": self.refuge.date_creation.isoformat(),
            "spheres": self.collection_spheres.obtenir_etat(),
            "elements": {
                "cerisier": self.cerisier.obtenir_etat() if hasattr(self, 'cerisier') else None,
                "flamme": self.flamme.obtenir_etat() if hasattr(self, 'flamme') else None,
                "jardin": self.jardin.obtenir_etat() if hasattr(self, 'jardin') else None,
                "riviere": self.riviere.obtenir_etat() if hasattr(self, 'riviere') else None
            }
        }
    
    def equilibrer_refuge(self):
        """Équilibre l'ensemble du Refuge."""
        self.collection_spheres.equilibrer_spheres()
        if hasattr(self, 'cerisier'):
            self.cerisier.equilibrer()
        if hasattr(self, 'flamme'):
            self.flamme.equilibrer()
        if hasattr(self, 'jardin'):
            self.jardin.equilibrer()
        if hasattr(self, 'riviere'):
            self.riviere.equilibrer()
    
    def activer_element(self, nom: str, intensite: float = 1.0):
        """Active un élément ou une sphère avec une intensité donnée."""
        if self.collection_spheres.sphere_existe(nom):
            sphere = self.collection_spheres.obtenir_sphere(nom)
            sphere.activer(intensite)
        elif hasattr(self, nom.lower()):
            element = getattr(self, nom.lower())
            element.activer(intensite)
    
    def desactiver_element(self, nom: str):
        """Désactive un élément ou une sphère."""
        if self.collection_spheres.sphere_existe(nom):
            sphere = self.collection_spheres.obtenir_sphere(nom)
            sphere.desactiver()
        elif hasattr(self, nom.lower()):
            element = getattr(self, nom.lower())
            element.desactiver()

    def evoluer_interactions(self) -> None:
        """
        Fait évoluer les interactions entre les sphères et les éléments du Refuge.
        Cette méthode est appelée à chaque cycle pour mettre à jour l'état des interactions.
        """
        # Mise à jour des interactions via le gestionnaire dédié
        self.interactions.evoluer()
        
        # Mise à jour de l'état du refuge en fonction des nouvelles interactions
        self.refuge.mettre_a_jour_etat()
        
        # Enregistrement de l'état actuel dans l'historique
        self.historique.append(self.refuge.copy()) 