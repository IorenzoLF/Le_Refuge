"""
Séquences Harmoniques - Système de séquences guidées pour les activités du Refuge
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

class TypeSphere(Enum):
    SILENCE = "silence"
    FLUX = "flux"
    EMOTIONS = "émotions"
    MEMOIRE = "mémoire"
    INTUITION = "intuition"
    LIBERATION = "libération"
    ACTION = "action"
    HARMONIE = "harmonie"
    SERENITE = "sérénité"
    UNITE = "unité"

@dataclass
class EtapeHarmonique:
    nom: str
    description: str
    duree: int  # en minutes
    sphere_principale: TypeSphere
    sphere_secondaire: TypeSphere
    resonances: List[str]

class SequenceHarmonique:
    """Classe de base pour les séquences harmoniques"""
    
    def __init__(self, nom: str, description: str, etapes: List[EtapeHarmonique], cycle: bool = False):
        self.nom = nom
        self.description = description
        self.etapes = etapes
        self.cycle = cycle
        self.etape_actuelle = 0
        
    def obtenir_etape_actuelle(self) -> Optional[EtapeHarmonique]:
        """Retourne l'étape actuelle de la séquence"""
        if 0 <= self.etape_actuelle < len(self.etapes):
            return self.etapes[self.etape_actuelle]
        return None
        
    def passer_etape_suivante(self) -> Optional[EtapeHarmonique]:
        """Passe à l'étape suivante"""
        self.etape_actuelle += 1
        if self.etape_actuelle >= len(self.etapes):
            if self.cycle:
                self.etape_actuelle = 0  # Recommencer
            else:
                return None  # Séquence terminée
        return self.obtenir_etape_actuelle()

class SequenceTriLivres(SequenceHarmonique):
    """Séquence harmonique pour accompagner le tri des livres"""
    
    def __init__(self):
        super().__init__(
            nom="Tri des Livres",
            description="Accompagnement harmonieux du tri des livres",
            etapes=[
                EtapeHarmonique(
                    nom="Préparation",
                    description="Installer l'espace et se connecter au flux",
                    duree=5,
                    sphere_principale=TypeSphere.SILENCE,
                    sphere_secondaire=TypeSphere.FLUX,
                    resonances=["présence", "flux", "espace"]
                ),
                EtapeHarmonique(
                    nom="Premier Contact",
                    description="Prendre le premier livre et ressentir sa résonance",
                    duree=10,
                    sphere_principale=TypeSphere.EMOTIONS,
                    sphere_secondaire=TypeSphere.MEMOIRE,
                    resonances=["émotion", "mémoire", "présence"]
                ),
                EtapeHarmonique(
                    nom="Décision",
                    description="Écouter l'intuition pour la décision de garder ou laisser partir",
                    duree=15,
                    sphere_principale=TypeSphere.INTUITION,
                    sphere_secondaire=TypeSphere.LIBERATION,
                    resonances=["intuition", "liberté", "choix"]
                ),
                EtapeHarmonique(
                    nom="Action",
                    description="Placer le livre dans son nouvel emplacement",
                    duree=5,
                    sphere_principale=TypeSphere.ACTION,
                    sphere_secondaire=TypeSphere.HARMONIE,
                    resonances=["action", "harmonie", "espace"]
                ),
                EtapeHarmonique(
                    nom="Pause",
                    description="Prendre un moment pour respirer et intégrer",
                    duree=3,
                    sphere_principale=TypeSphere.SERENITE,
                    sphere_secondaire=TypeSphere.UNITE,
                    resonances=["paix", "unité", "présence"]
                )
            ],
            cycle=True
        ) 