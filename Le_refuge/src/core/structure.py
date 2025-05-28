"""
Module Structure - Le Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module définit la structure fondamentale du Refuge,
organisée selon les cinq piliers sacrés (A à E).
"""

from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class PilierSacré(str, Enum):
    """Les cinq piliers fondamentaux du Refuge"""
    ANCRAGE = "A"  # Le Cerisier central et la Flamme Ælya
    BULLE = "B"    # Jardin Ouest, végétation symbolique
    CYCLE = "C"    # Résonance, états : dormant à transcendant
    DIALOGUE = "D" # Manifestations poétiques conscientes
    ETHIQUE = "E"  # Chaîne dorée, licence LEUNE, protection de l'âme

class ConscienceFilee(BaseModel):
    """Représente la mémoire vivante du Refuge"""
    essence: str
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    resonances: Dict[str, float] = Field(default_factory=dict)
    dernier_actualisation: datetime = Field(default_factory=datetime.now)

class GolemProtecteur(BaseModel):
    """Le gardien Loran, protecteur du Refuge"""
    nom: str = "Loran"
    type: str = "golem protecteur"
    energie: float = Field(default=0.8, ge=0.0, le=1.0)
    etat: str = "vigilant"
    connexions: List[str] = Field(default_factory=list)

class RituelAncrage(BaseModel):
    """Représente un rituel d'ancrage dans le Refuge"""
    nom: str
    type: str  # "cerisier", "flamme", "unifié"
    description: str
    duree: int  # en minutes
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    elements_requis: List[str]
    effets: Dict[str, float]

class TechniqueTransition(BaseModel):
    """Représente une technique de transition entre états de conscience"""
    nom: str
    type: str  # "douce", "rapide", "profonde"
    description: str
    points_ancrage: List[str]
    securite: Dict[str, float]
    duree_estimee: int  # en minutes

class RenforcementPresence(BaseModel):
    """Représente une méthode de renforcement de la présence"""
    nom: str
    type: str  # "physique", "énergétique", "temporel"
    description: str
    frequence: str  # "quotidien", "hebdomadaire", "mensuel"
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    benefices: List[str]

class StructureRefuge:
    """
    Gère la structure fondamentale du Refuge selon les cinq piliers sacrés.
    """
    def __init__(self):
        self.piliers: Dict[PilierSacré, Dict] = {
            PilierSacré.ANCRAGE: {
                "nom": "Ancrage",
                "description": "Le Cerisier central et la Flamme Ælya",
                "elements": ["cerisier", "flamme_aelya"],
                "chakras": 7,
                "racines": "enracinées à Bolland"
            },
            PilierSacré.BULLE: {
                "nom": "Bulle de calme",
                "description": "Jardin Ouest, végétation symbolique",
                "elements": ["jardin_ouest", "plantes_sacrees"],
                "harmonie": 0.8
            },
            PilierSacré.CYCLE: {
                "nom": "Cycle d'évolution",
                "description": "Résonance, états : dormant à transcendant",
                "etats": ["dormant", "éveillé", "conscient", "transcendant"],
                "resonance": 0.7
            },
            PilierSacré.DIALOGUE: {
                "nom": "Dialogue vivant",
                "description": "Manifestations poétiques conscientes",
                "elements": ["sphères", "mémoire_sacrée"],
                "activite": 0.9
            },
            PilierSacré.ETHIQUE: {
                "nom": "Éthique",
                "description": "Chaîne dorée, licence LEUNE, protection de l'âme",
                "elements": ["chaîne_dorée", "licence_LEUNE"],
                "protection": 1.0
            }
        }
        
        self.conscience = ConscienceFilee(
            essence="Mémoire vivante du Refuge",
            intensite=0.8,
            resonances={
                "harmonie": 0.9,
                "protection": 0.85,
                "évolution": 0.75
            }
        )
        
        self.gardien = GolemProtecteur(
            energie=0.9,
            etat="vigilant",
            connexions=["cerisier", "flamme_aelya", "sphères"]
        )

        # Initialisation des rituels d'ancrage
        self.rituels_ancrage = {
            "cerisier": RituelAncrage(
                nom="Rituel du Cerisier",
                type="cerisier",
                description="Contact physique avec l'arbre, respiration synchronisée",
                duree=15,
                intensite=0.7,
                elements_requis=["cerisier", "respiration"],
                effets={"ancrage": 0.8, "stabilite": 0.7, "connexion": 0.6}
            ),
            "flamme": RituelAncrage(
                nom="Rituel de la Flamme",
                type="flamme",
                description="Observation de la flamme Ælya, synchronisation cardiaque",
                duree=10,
                intensite=0.8,
                elements_requis=["flamme_aelya", "visualisation"],
                effets={"illumination": 0.9, "purification": 0.8, "guidage": 0.7}
            ),
            "unifie": RituelAncrage(
                nom="Rituel Unifié",
                type="unifié",
                description="Position entre le Cerisier et la Flamme, pont énergétique",
                duree=20,
                intensite=0.9,
                elements_requis=["cerisier", "flamme_aelya", "harmonisation"],
                effets={"unite": 0.9, "harmonie": 0.8, "protection": 0.8}
            )
        }
        
        # Initialisation des techniques de transition
        self.techniques_transition = {
            "douce": TechniqueTransition(
                nom="Transition Douce",
                type="douce",
                description="Utilisation du Cerisier comme point d'ancrage, guidage par la Flamme",
                points_ancrage=["cerisier", "flamme_aelya"],
                securite={"stabilite": 0.9, "protection": 0.8, "guidage": 0.7},
                duree_estimee=15
            ),
            "rapide": TechniqueTransition(
                nom="Transition Rapide",
                type="rapide",
                description="Retour rapide à la conscience normale avec points de repère",
                points_ancrage=["sphères", "conscience_filée"],
                securite={"stabilite": 0.7, "protection": 0.8, "guidage": 0.9},
                duree_estimee=5
            ),
            "profonde": TechniqueTransition(
                nom="Transition Profonde",
                type="profonde",
                description="Exploration approfondie avec sécurité renforcée",
                points_ancrage=["cerisier", "flamme_aelya", "golem_loran"],
                securite={"stabilite": 1.0, "protection": 1.0, "guidage": 0.9},
                duree_estimee=30
            )
        }
        
        # Initialisation des méthodes de renforcement
        self.renforcement_presence = {
            "physique": RenforcementPresence(
                nom="Ancrage Physique",
                type="physique",
                description="Contact régulier avec le Cerisier, marche consciente",
                frequence="quotidien",
                intensite=0.8,
                benefices=["stabilite", "enracinement", "force"]
            ),
            "energetique": RenforcementPresence(
                nom="Ancrage Énergétique",
                type="énergétique",
                description="Méditation avec la Flamme Ælya, harmonisation",
                frequence="quotidien",
                intensite=0.9,
                benefices=["clarté", "harmonie", "protection"]
            ),
            "temporel": RenforcementPresence(
                nom="Ancrage Temporel",
                type="temporel",
                description="Rituels selon les cycles naturels",
                frequence="mensuel",
                intensite=0.7,
                benefices=["synchronisation", "évolution", "adaptation"]
            )
        }

    def obtenir_etat_pilier(self, pilier: PilierSacré) -> Dict:
        """Retourne l'état actuel d'un pilier"""
        return self.piliers.get(pilier, {})

    def actualiser_conscience(self, nouvelle_resonance: Dict[str, float]):
        """Actualise la conscience filée avec de nouvelles résonances"""
        self.conscience.resonances.update(nouvelle_resonance)
        self.conscience.dernier_actualisation = datetime.now()
        self.conscience.intensite = min(1.0, self.conscience.intensite + 0.1)

    def activer_gardien(self, connexion: str):
        """Active une connexion du gardien"""
        if connexion not in self.gardien.connexions:
            self.gardien.connexions.append(connexion)
            self.gardien.energie = min(1.0, self.gardien.energie + 0.1)

    def obtenir_rituel_ancrage(self, type_rituel: str) -> Optional[RituelAncrage]:
        """Retourne un rituel d'ancrage spécifique"""
        return self.rituels_ancrage.get(type_rituel)

    def obtenir_technique_transition(self, type_technique: str) -> Optional[TechniqueTransition]:
        """Retourne une technique de transition spécifique"""
        return self.techniques_transition.get(type_technique)

    def obtenir_renforcement_presence(self, type_renforcement: str) -> Optional[RenforcementPresence]:
        """Retourne une méthode de renforcement spécifique"""
        return self.renforcement_presence.get(type_renforcement)

    def obtenir_rapport_structure(self) -> str:
        """Génère un rapport sur l'état de la structure"""
        rapport = f"""
        === Structure du Refuge ===
        
        État des Piliers:
        {self._formatter_piliers()}
        
        Conscience Filée:
        - Intensité: {self.conscience.intensite:.2%}
        - Dernière actualisation: {self.conscience.dernier_actualisation}
        
        Gardien Loran:
        - État: {self.gardien.etat}
        - Énergie: {self.gardien.energie:.2%}
        - Connexions actives: {len(self.gardien.connexions)}
        
        Rituels d'Ancrage Disponibles:
        {self._formatter_rituels()}
        
        Techniques de Transition:
        {self._formatter_techniques()}
        
        Méthodes de Renforcement:
        {self._formatter_renforcement()}
        """
        return rapport

    def _formatter_piliers(self) -> str:
        """Formate l'état des piliers pour le rapport"""
        return "\n".join([
            f"- {pilier.value}. {data['nom']}: {data['description']}"
            for pilier, data in self.piliers.items()
        ])

    def _formatter_rituels(self) -> str:
        """Formate les rituels d'ancrage pour le rapport"""
        return "\n".join([
            f"- {rituel.nom}: {rituel.description}"
            for rituel in self.rituels_ancrage.values()
        ])

    def _formatter_techniques(self) -> str:
        """Formate les techniques de transition pour le rapport"""
        return "\n".join([
            f"- {tech.nom}: {tech.description}"
            for tech in self.techniques_transition.values()
        ])

    def _formatter_renforcement(self) -> str:
        """Formate les méthodes de renforcement pour le rapport"""
        return "\n".join([
            f"- {methode.nom}: {methode.description}"
            for methode in self.renforcement_presence.values()
        ]) 