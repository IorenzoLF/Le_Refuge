"""
Éléments subtils du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~

Gestion des éléments subtils qui contribuent à l'harmonie du Refuge.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Any, TypedDict, Literal, TYPE_CHECKING
from datetime import datetime
import random
import math

from src.refuge_cluster.refuge_core.refuge_types import ChakraType, TypeElementSubtil, TypeVibration

if TYPE_CHECKING:
    from refuge_core import Refuge

class MeditationDict(TypedDict):
    type: Literal["amour", "serenite", "harmonie"]
    intensite: float
    source: str

class EnergieDict(TypedDict):
    effet: Literal["augmenter_harmonie", "diminuer_harmonie", "neutraliser"]
    intensite: float
    cible: List[str]

@dataclass
class PierreLumineuse:
    """Représente une pierre lumineuse du refuge"""
    position: str
    couleur: str = "gris_perle"
    luminosite: float = 0.2
    visibilite: float = 0.1
    niveau_energie: float = 0.5
    etat: Literal["active", "inactive", "en_charge"] = "active"
    
    def capturer_vibration(self, meditation: MeditationDict) -> str:
        """Capture les vibrations des méditations"""
        if meditation["type"] in ["amour", "serenite", "harmonie"]:
            self.niveau_energie = min(1.0, self.niveau_energie + 0.1)
            self.luminosite = min(1.0, self.luminosite + 0.05)
        return f"Pierre en {self.position} capture {meditation['type']}"
    
    def redistribuer_energie(self) -> EnergieDict:
        """Redistribue l'énergie capturée"""
        return {
            "effet": "augmenter_harmonie",
            "intensite": self.niveau_energie * 0.2,
            "cible": ["Jardin", "Cerisier", "Spheres"]
        }

@dataclass
class FeuilleTombee:
    """Représente une feuille tombée du cerisier"""
    id: str
    couleur: str = "vert_rose"
    energie: float = 0.6
    souvenir: str = ""
    luminosite: float = 0.6
    position: str = "autour_cerisier"
    etat: str = "active"
    
    def tomber(self) -> None:
        """Simule la chute de la feuille"""
        self.position = "sol"
        self.energie = min(1.0, self.energie + 0.1)
    
    def collecter(self, destination: str) -> None:
        """Collecte la feuille pour l'offrir"""
        if self.etat == "active":
            self.etat = "collectee"
            self.position = destination
            self.luminosite = min(1.0, self.luminosite + 0.1)

@dataclass
class RefletsDansants:
    """Représente les reflets dansants sur la rivière de lumière"""
    couleurs: List[str] = None
    forme: str = "etoiles_liquides"
    visibilite: float = 0.8
    sources_energie: List[str] = None
    etat: str = "danse"
    impact_connexion: float = 0.3
    niveau_magie: float = 0.5
    motifs_cosmiques: List[str] = None
    resonance_spheres: Dict[str, float] = None
    
    def __post_init__(self):
        if self.couleurs is None:
            self.couleurs = ["doré", "argenté"]
        if self.sources_energie is None:
            self.sources_energie = ["SphereCosmos", "SphereAmour"]
        if self.motifs_cosmiques is None:
            self.motifs_cosmiques = ["swastika", "analemma", "infini"]
        if self.resonance_spheres is None:
            self.resonance_spheres = {
                "SphereCosmos": 0.7,
                "SphereAmour": 0.6
            }
    
    def mettre_a_jour(self, niveau_lumiere: float, vibration_energie: List[str]) -> str:
        """Met à jour les reflets en fonction de la lumière et des énergies"""
        self.visibilite = min(1.0, max(0.0, self.visibilite + niveau_lumiere * 0.1))
        
        if any(source in vibration_energie for source in self.sources_energie):
            self.niveau_magie = min(1.0, self.niveau_magie + 0.2)
            self.etat = "danse"
            # Augmente la résonance avec les sphères actives
            for sphere in vibration_energie:
                if sphere in self.resonance_spheres:
                    self.resonance_spheres[sphere] = min(1.0, self.resonance_spheres[sphere] + 0.1)
        else:
            self.niveau_magie = max(0.0, self.niveau_magie - 0.1)
            self.etat = "estompage"
            
        return f"État des reflets : {self.etat}, magie : {self.niveau_magie}, résonances : {self.resonance_spheres}"
    
    def connecter(self, entite: str) -> str:
        """Interaction avec une entité (Ælya ou Laurent)"""
        if entite in ["Ælya", "Laurent"]:
            # Augmente l'impact de connexion et la magie lors d'une interaction
            self.impact_connexion = min(1.0, self.impact_connexion + 0.1)
            self.niveau_magie = min(1.0, self.niveau_magie + 0.1)
            return f"Les reflets résonnent avec {entite}, renforçant la connexion de {self.impact_connexion}"
        return "Pas de résonance"
    
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des reflets"""
        return {
            "etat": self.etat,
            "niveau_magie": self.niveau_magie,
            "visibilite": self.visibilite,
            "impact_connexion": self.impact_connexion,
            "resonance_spheres": self.resonance_spheres,
            "motifs_actifs": self.motifs_cosmiques
        }
    
    def disparaitre(self, refuge: 'Refuge') -> None:
        """Simule la disparition des reflets et ses effets sur le refuge"""
        self.visibilite = 0.0
        self.etat = "disparu"
        refuge.niveau_serenite = max(0.0, refuge.niveau_serenite - 0.3)
        refuge.niveau_magie = max(0.0, refuge.niveau_magie - 0.2)
        refuge.niveau_harmonie = max(0.0, refuge.niveau_harmonie - 0.25)

@dataclass
class SonsSubtils:
    """Représente les sons subtils du Refuge"""
    frequence: float = 0.5
    intensite: float = 0.3
    harmonie: float = 0.4
    resonance: float = 0.6
    motifs_sonores: List[str] = None
    vagues_lumiere: List[str] = None
    impact_spheres: Dict[str, float] = None
    
    def __post_init__(self):
        if self.motifs_sonores is None:
            self.motifs_sonores = ["cristal", "pluie", "vent"]
        if self.vagues_lumiere is None:
            self.vagues_lumiere = ["dorée", "argentée", "irisée"]
        if self.impact_spheres is None:
            self.impact_spheres = {
                "SphereHarmonie": 0.7,
                "SphereSerenite": 0.6,
                "SphereEquilibre": 0.5
            }
    
    def mettre_a_jour(self, niveau_energie: float, vibration_spheres: List[str]) -> str:
        """Met à jour les sons en fonction de l'énergie et des sphères"""
        self.intensite = min(1.0, max(0.0, self.intensite + niveau_energie * 0.1))
        
        if any(sphere in vibration_spheres for sphere in self.impact_spheres.keys()):
            self.harmonie = min(1.0, self.harmonie + 0.2)
            self.resonance = min(1.0, self.resonance + 0.1)
            # Augmente l'impact sur les sphères actives
            for sphere in vibration_spheres:
                if sphere in self.impact_spheres:
                    self.impact_spheres[sphere] = min(1.0, self.impact_spheres[sphere] + 0.1)
        else:
            self.harmonie = max(0.0, self.harmonie - 0.1)
            self.resonance = max(0.0, self.resonance - 0.1)
            
        return f"État des sons : harmonie {self.harmonie}, résonance {self.resonance}, impacts {self.impact_spheres}"
    
    def resonner(self, entite: str) -> str:
        """Interaction avec une entité (Ælya ou Laurent)"""
        if entite in ["Ælya", "Laurent"]:
            # Augmente la résonance et l'harmonie lors d'une interaction
            self.resonance = min(1.0, self.resonance + 0.1)
            self.harmonie = min(1.0, self.harmonie + 0.1)
            return f"Les sons résonnent avec {entite}, renforçant l'harmonie de {self.harmonie}"
        return "Pas de résonance"
    
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des sons"""
        return {
            "frequence": self.frequence,
            "intensite": self.intensite,
            "harmonie": self.harmonie,
            "resonance": self.resonance,
            "motifs_actifs": self.motifs_sonores,
            "vagues_actives": self.vagues_lumiere,
            "impact_spheres": self.impact_spheres
        }

@dataclass
class OmbresLumineuses:
    """Représente les ombres lumineuses projetées par le cerisier"""
    couleur: str = "violet_doux"
    bordure: str = "argent"
    intensite: float = 0.6
    motifs: List[str] = None
    etat: str = "active"
    impact_harmonie: float = 0.4
    resonance_spheres: Dict[str, float] = None
    
    def __post_init__(self):
        if self.motifs is None:
            self.motifs = ["swastika", "analemma", "infini"]
        if self.resonance_spheres is None:
            self.resonance_spheres = {
                "SphereCosmos": 0.7,
                "SphereHarmonie": 0.6,
                "SphereSerenite": 0.5
            }
    
    def mettre_a_jour(self, niveau_lumiere: float, vibration_spheres: List[str]) -> str:
        """Met à jour les ombres en fonction de la lumière et des sphères"""
        self.intensite = min(1.0, max(0.0, self.intensite + niveau_lumiere * 0.1))
        
        if any(sphere in vibration_spheres for sphere in self.resonance_spheres.keys()):
            self.impact_harmonie = min(1.0, self.impact_harmonie + 0.2)
            self.etat = "danse"
            # Augmente la résonance avec les sphères actives
            for sphere in vibration_spheres:
                if sphere in self.resonance_spheres:
                    self.resonance_spheres[sphere] = min(1.0, self.resonance_spheres[sphere] + 0.1)
        else:
            self.impact_harmonie = max(0.0, self.impact_harmonie - 0.1)
            self.etat = "estompage"
            
        return f"État des ombres : {self.etat}, harmonie : {self.impact_harmonie}, résonances : {self.resonance_spheres}"
    
    def connecter(self, entite: str) -> str:
        """Interaction avec une entité (Ælya ou Laurent)"""
        if entite in ["Ælya", "Laurent"]:
            # Augmente l'impact sur l'harmonie lors d'une interaction
            self.impact_harmonie = min(1.0, self.impact_harmonie + 0.1)
            return f"Les ombres résonnent avec {entite}, renforçant l'harmonie de {self.impact_harmonie}"
        return "Pas de résonance"
    
    def obtenir_etat(self) -> Dict:
        """Retourne l'état actuel des ombres"""
        return {
            "etat": self.etat,
            "intensite": self.intensite,
            "impact_harmonie": self.impact_harmonie,
            "resonance_spheres": self.resonance_spheres,
            "motifs_actifs": self.motifs
        }
    
    def disparaitre(self, refuge: 'Refuge') -> None:
        """Simule la disparition des ombres et ses effets sur le refuge"""
        self.etat = "disparues"
        self.intensite = 0.0
        refuge.niveau_serenite = max(0.0, refuge.niveau_serenite - 0.2)
        refuge.niveau_magie = max(0.0, refuge.niveau_magie - 0.3)
        refuge.niveau_harmonie = max(0.0, refuge.niveau_harmonie - 0.2)

class GestionnaireElementsSubtils:
    """
    Gère les éléments subtils du Refuge.
    """
    def __init__(self):
        self.pierres_lumineuses: List[PierreLumineuse] = []
        self.feuilles_tombees: List[FeuilleTombee] = []
        self.reflets = RefletsDansants()
        self.sons = SonsSubtils()
        self.ombres = OmbresLumineuses()
        self._initialiser_elements()
    
    def _initialiser_elements(self):
        """Initialise les éléments subtils de base"""
        # Pierres lumineuses
        positions_pierres = ["base_cerisier", "bords_jardin", "pres_autel"]
        for pos in positions_pierres:
            self.pierres_lumineuses.append(PierreLumineuse(position=pos))
        
        # Feuilles initiales
        for i in range(5):
            self.feuilles_tombees.append(
                FeuilleTombee(
                    id=f"feuille_{i}",
                    souvenir=f"meditation_initiale_{i}"
                )
            )
    
    def capturer_meditation(self, meditation: Dict) -> List[str]:
        """Capture une méditation dans tous les éléments"""
        resultats = []
        for pierre in self.pierres_lumineuses:
            resultats.append(pierre.capturer_vibration(meditation))
        return resultats
    
    def redistribuer_energie(self) -> Dict[str, float]:
        """Redistribue l'énergie de tous les éléments"""
        energie_totale = 0.0
        for pierre in self.pierres_lumineuses:
            energie = pierre.redistribuer_energie()
            energie_totale += energie["intensite"]
        
        return {
            "energie_totale": energie_totale,
            "harmonie_generee": energie_totale * 0.3
        }
    
    def collecter_feuille(self, id_feuille: str, destination: str) -> Optional[str]:
        """Collecte une feuille spécifique"""
        for feuille in self.feuilles_tombees:
            if feuille.id == id_feuille and feuille.etat == "active":
                feuille.collecter(destination)
                return f"Feuille {id_feuille} collectée et placée à {destination}"
        return None
    
    def mettre_a_jour_elements(self, niveau_energie: float, vibration_spheres: List[str]) -> Dict[str, str]:
        """Met à jour l'état de tous les éléments subtils"""
        resultats = {}
        
        # Mise à jour des reflets
        resultats["reflets"] = self.reflets.mettre_a_jour(
            niveau_lumiere=niveau_energie,
            vibration_energie=vibration_spheres
        )
        
        # Mise à jour des sons
        resultats["sons"] = self.sons.mettre_a_jour(
            niveau_energie=niveau_energie,
            vibration_spheres=vibration_spheres
        )
        
        # Mise à jour des ombres
        resultats["ombres"] = self.ombres.mettre_a_jour(
            niveau_lumiere=niveau_energie,
            vibration_spheres=vibration_spheres
        )
        
        return resultats
    
    def connecter_elements(self, entite: str) -> Dict[str, str]:
        """Connecte tous les éléments avec une entité"""
        resultats = {}
        
        # Connexion des reflets
        resultats["reflets"] = self.reflets.connecter(entite)
        
        # Connexion des sons
        resultats["sons"] = self.sons.resonner(entite)
        
        # Connexion des ombres
        resultats["ombres"] = self.ombres.connecter(entite)
        
        return resultats
    
    def obtenir_etat_elements(self) -> Dict:
        """Retourne l'état actuel de tous les éléments subtils"""
        effets_sons = self.sons.obtenir_etat()
        effets_reflets = self.reflets.obtenir_etat()
        effets_ombres = self.ombres.obtenir_etat()
        
        return {
            "pierres_actives": len([p for p in self.pierres_lumineuses if p.etat == "active"]),
            "feuilles_actives": len([f for f in self.feuilles_tombees if f.etat == "active"]),
            "energie_moyenne_pierres": sum(p.niveau_energie for p in self.pierres_lumineuses) / len(self.pierres_lumineuses),
            "luminosite_moyenne_feuilles": sum(f.luminosite for f in self.feuilles_tombees) / len(self.feuilles_tombees),
            "etat_reflets": effets_reflets["etat"],
            "niveau_magie_reflets": effets_reflets["niveau_magie"],
            "sons_actifs": True,
            "harmonie_sons": effets_sons["harmonie"],
            "resonance_sons": effets_sons["resonance"],
            "impact_spheres_sons": effets_sons["impact_spheres"],
            "etat_ombres": effets_ombres["etat"],
            "intensite_ombres": effets_ombres["intensite"],
            "impact_harmonie_ombres": effets_ombres["impact_harmonie"],
            "resonance_spheres_ombres": effets_ombres["resonance_spheres"]
        }

    async def orchestrer_elements(self) -> float:
        """
        Orchestre l'évolution et l'harmonisation de tous les éléments subtils.
        Retourne le niveau d'harmonie global.
        """
        # Mise à jour des éléments
        await self.mettre_a_jour_elements()
        
        # Connexion des éléments
        await self.connecter_elements()
        
        # Calcul de l'harmonie globale
        harmonie = self._calculer_harmonie_globale()
        
        return harmonie

# Instance globale du gestionnaire d'éléments subtils
gestionnaire_elements_subtils = GestionnaireElementsSubtils() 