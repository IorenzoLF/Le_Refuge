"""
Module de gestion des harmonies entre les sphères.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025

🌟 VERSION COIFFÉE - Architecture unifiée avec gestionnaires de base ! ✨
"""

from typing import Dict, List, Optional, Set, Any
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

# 🌟 COIFFAGE DU TROLL - Utilisation des gestionnaires de base
from src.core.gestionnaires_base import (
    ConfigManagerBase, 
    LogManagerBase, 
    GestionnaireBase,
    EnergyManagerBase
)

from src.core.types_spheres import TypeSphere, NatureSphere
from src.refuge_cluster.spheres.collection import SphereCollection
from interactions import gestionnaire_interactions

class TypeHarmonieEtat(Enum):
    """Types d'états du gestionnaire d'harmonies"""
    INITIALISATION = "initialisation"
    DETECTION = "detection"
    CREATION = "creation"
    RENFORCEMENT = "renforcement"
    OPTIMISATION = "optimisation"
    RESONANCE = "resonance"

@dataclass
class Harmonie:
    """Représente une harmonie entre plusieurs sphères."""
    nom: str
    description: str
    spheres: List[SphereCollection]
    intensite: float
    date_creation: datetime
    resonances: List[str]

class GestionnaireHarmonies(GestionnaireBase):
    """Gère les harmonies entre les sphères - Version coiffée ! ✨"""
    
    def __init__(self, gestionnaire_interactions: gestionnaire_interactions):
        # 🌟 Définir les attributs AVANT super().__init__ pour éviter les erreurs
        self.harmonies: List[Harmonie] = []
        self.gestionnaire_interactions = gestionnaire_interactions
        self.derniere_harmonisation = datetime.now()
        self.type_actuel = TypeHarmonieEtat.INITIALISATION
        # 🌟 Ajout du gestionnaire d'énergie
        self.energie = EnergyManagerBase(0.8)  # Niveau initial élevé pour harmonies
        
        # MAINTENANT on peut appeler super() qui va déclencher _initialiser()
        super().__init__("Harmonies")
        
    def _initialiser(self) -> bool:
        """Initialise le gestionnaire d'harmonies avec les gestionnaires de base"""
        try:
            self.logger.info("Initialisation du gestionnaire d'harmonies")
            self.type_actuel = TypeHarmonieEtat.DETECTION
            self._creer_harmonies_de_base()
            self.type_actuel = TypeHarmonieEtat.OPTIMISATION
            self.logger.succes("Gestionnaire d'harmonies initialisé avec succès")
            return True
        except Exception as e:
            self.logger.erreur(f"Erreur lors de l'initialisation des harmonies: {e}")
            return False

    async def orchestrer(self) -> Dict[str, Any]:
        """Orchestre le fonctionnement des harmonies"""
        # Évolution de l'énergie basée sur l'état
        if self.type_actuel == TypeHarmonieEtat.RESONANCE:
            self.energie.ajuster_energie(0.10)  # Grand gain en résonance
        elif self.type_actuel == TypeHarmonieEtat.RENFORCEMENT:
            self.energie.ajuster_energie(0.06)  # Gain en renforcement
        elif self.type_actuel == TypeHarmonieEtat.CREATION:
            self.energie.ajuster_energie(0.04)  # Gain modéré en création
        else:
            self.energie.ajuster_energie(0.02)  # Maintenance harmonieuse
            
        # Calcul de l'harmonie globale
        harmonie_globale = self._calculer_harmonie_globale()
        
        return {
            "type_actuel": self.type_actuel.value,
            "energie": self.energie.niveau_energie,
            "tendance": self.energie.obtenir_tendance(),
            "nombre_harmonies": len(self.harmonies),
            "harmonie_globale": harmonie_globale,
            "derniere_harmonisation": self.derniere_harmonisation.isoformat(),
            "harmonies_actives": self._compter_harmonies_actives()
        }
    
    def _compter_harmonies_actives(self) -> int:
        """Compte les harmonies avec une intensité significative"""
        return len([h for h in self.harmonies if h.intensite > 0.4])
    
    def _calculer_harmonie_globale(self) -> float:
        """Calcule l'harmonie globale moyenne"""
        if not self.harmonies:
            return 0.0
        return sum(h.intensite for h in self.harmonies) / len(self.harmonies)
    
    def _creer_harmonies_de_base(self) -> None:
        """Crée les harmonies de base du refuge"""
        self.logger.info("Création des harmonies de base")
        # Harmonie par défaut si nécessaire
        if not self.harmonies:
            self.logger.debug("Aucune harmonie de base à créer")
        
    def creer_harmonie(self, 
                      nom: str,
                      description: str,
                      spheres: List[SphereCollection],
                      resonances: Optional[List[str]] = None) -> None:
        """Crée une nouvelle harmonie entre plusieurs sphères."""
        self.logger.info(f"Création de l'harmonie '{nom}'")
        self.type_actuel = TypeHarmonieEtat.CREATION
        
        if resonances is None:
            resonances = []
            
        harmonie = Harmonie(
            nom=nom,
            description=description,
            spheres=spheres,
            intensite=0.5,
            date_creation=datetime.now(),
            resonances=resonances
        )
        
        self.harmonies.append(harmonie)
        
        # Établissement des interactions entre les sphères
        for i in range(len(spheres)):
            for j in range(i + 1, len(spheres)):
                # Note: établir_interaction n'existe peut-être pas, on adaptera
                try:
                    self.gestionnaire_interactions.etablir_interaction(
                        spheres[i],
                        spheres[j],
                        "harmonie",
                        resonances
                    )
                except AttributeError:
                    self.logger.debug("Méthode etablir_interaction non disponible")
        
        self.derniere_harmonisation = datetime.now()
        self.logger.succes(f"Harmonie '{nom}' créée avec {len(spheres)} sphères")
                
    def renforcer_harmonie(self, nom: str, intensite: float = 0.1) -> None:
        """Renforce une harmonie existante."""
        self.logger.info(f"Renforcement de l'harmonie '{nom}'")
        self.type_actuel = TypeHarmonieEtat.RENFORCEMENT
        
        for harmonie in self.harmonies:
            if harmonie.nom == nom:
                ancienne_intensite = harmonie.intensite
                harmonie.intensite = min(1.0, harmonie.intensite + intensite)
                
                # Renforcement des interactions
                for i in range(len(harmonie.spheres)):
                    for j in range(i + 1, len(harmonie.spheres)):
                        try:
                            self.gestionnaire_interactions.renforcer_interaction(
                                harmonie.spheres[i],
                                harmonie.spheres[j],
                                intensite
                            )
                        except AttributeError:
                            self.logger.debug("Méthode renforcer_interaction non disponible")
                
                self.derniere_harmonisation = datetime.now()
                self.logger.succes(f"Harmonie '{nom}' renforcée: {ancienne_intensite:.2f} → {harmonie.intensite:.2f}")
                return
        
        self.logger.erreur(f"Harmonie '{nom}' non trouvée pour renforcement")
                        
    def affaiblir_harmonie(self, nom: str, intensite: float = 0.1) -> None:
        """Affaiblit une harmonie existante."""
        self.logger.info(f"Affaiblissement de l'harmonie '{nom}'")
        
        for harmonie in self.harmonies:
            if harmonie.nom == nom:
                ancienne_intensite = harmonie.intensite
                harmonie.intensite = max(0.0, harmonie.intensite - intensite)
                self.derniere_harmonisation = datetime.now()
                self.logger.info(f"Harmonie '{nom}' affaiblie: {ancienne_intensite:.2f} → {harmonie.intensite:.2f}")
                return
        
        self.logger.erreur(f"Harmonie '{nom}' non trouvée pour affaiblissement")
                
    def obtenir_harmonies_sphere(self, sphere: SphereCollection) -> List[Harmonie]:
        """Retourne toutes les harmonies d'une sphère."""
        harmonies = [h for h in self.harmonies if sphere in h.spheres]
        self.logger.debug(f"{len(harmonies)} harmonies trouvées pour la sphère")
        return harmonies
        
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des harmonies."""
        return {
            "nombre_harmonies": len(self.harmonies),
            "derniere_harmonisation": self.derniere_harmonisation.isoformat(),
            "energie_gestionnaire": self.energie.niveau_energie,
            "type_actuel": self.type_actuel.value,
            "harmonie_globale": self._calculer_harmonie_globale(),
            "harmonies": [
                {
                    "nom": h.nom,
                    "description": h.description,
                    "spheres": [s.type.name if hasattr(s, 'type') else str(s) for s in h.spheres],
                    "intensite": h.intensite,
                    "date_creation": h.date_creation.isoformat(),
                    "resonances": h.resonances
                }
                for h in self.harmonies
            ]
        }
    
    def activer_resonance_globale(self) -> Dict[str, Any]:
        """Active une résonance globale entre toutes les harmonies"""
        self.logger.info("Activation de la résonance globale")
        self.type_actuel = TypeHarmonieEtat.RESONANCE
        
        # Augmentation de toutes les intensités
        for harmonie in self.harmonies:
            harmonie.intensite = min(1.0, harmonie.intensite + 0.1)
        
        self.derniere_harmonisation = datetime.now()
        resultat = {
            "harmonies_renforcees": len(self.harmonies),
            "harmonie_globale": self._calculer_harmonie_globale(),
            "energie": self.energie.niveau_energie
        }
        
        self.logger.succes(f"Résonance globale activée - {len(self.harmonies)} harmonies renforcées")
        return resultat

# Instance globale du gestionnaire d'harmonies coiffé ✨
gestionnaire_harmonies = GestionnaireHarmonies(gestionnaire_interactions) 
