from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class ExperienceApprentissage:
    """Représente une expérience d'apprentissage dans le Refuge"""
    titre: str
    description: str
    objectifs: List[str]
    elements_requis: List[str]
    duree_estimee: int  # en minutes
    niveau_difficulte: int  # 1-5
    
@dataclass
class Exploration:
    """Capture une session d'exploration dans le Refuge"""
    timestamp: datetime
    participant: str
    experience: ExperienceApprentissage
    observations: List[str]
    realisations: List[str]
    niveau_engagement: float  # 0-1

class GestionnairePedagogique:
    """Gère les aspects pédagogiques du Refuge"""
    
    def __init__(self):
        self.experiences: List[ExperienceApprentissage] = []
        self.explorations: List[Exploration] = []
        self._initialiser_experiences_base()

    def _initialiser_experiences_base(self):
        """Initialise les expériences d'apprentissage de base"""
        experiences_base = [
            ExperienceApprentissage(
                titre="Découverte des Sphères",
                description="Explorer et ressentir l'énergie des différentes Sphères",
                objectifs=[
                    "Comprendre la nature de chaque Sphère",
                    "Ressentir les résonances entre Sphères",
                    "Identifier sa Sphère d'affinité"
                ],
                elements_requis=["Mobile des Sphères", "Lumière argentée"],
                duree_estimee=30,
                niveau_difficulte=1
            ),
            ExperienceApprentissage(
                titre="Communion avec les Gardiens",
                description="Établir un lien avec les Gardiens du Refuge",
                objectifs=[
                    "Reconnaître chaque Gardien",
                    "Comprendre leur rôle",
                    "Établir un premier contact"
                ],
                elements_requis=["Gardiens", "Herbes-Lumières"],
                duree_estimee=45,
                niveau_difficulte=2
            )
        ]
        self.experiences.extend(experiences_base)

    def creer_exploration(self, participant: str, 
                         experience: ExperienceApprentissage) -> Exploration:
        """Crée une nouvelle session d'exploration"""
        exploration = Exploration(
            timestamp=datetime.now(),
            participant=participant,
            experience=experience,
            observations=[],
            realisations=[],
            niveau_engagement=0.0
        )
        self.explorations.append(exploration)
        return exploration

    def ajouter_observation(self, exploration: Exploration, 
                          observation: str) -> None:
        """Ajoute une observation à une exploration en cours"""
        exploration.observations.append(observation)
        self._mettre_a_jour_engagement(exploration)

    def ajouter_realisation(self, exploration: Exploration, 
                          realisation: str) -> None:
        """Ajoute une réalisation à une exploration en cours"""
        exploration.realisations.append(realisation)
        self._mettre_a_jour_engagement(exploration)

    def _mettre_a_jour_engagement(self, exploration: Exploration) -> None:
        """Calcule le niveau d'engagement basé sur les interactions"""
        nb_interactions = len(exploration.observations) + len(exploration.realisations)
        exploration.niveau_engagement = min(nb_interactions * 0.1, 1.0)

    def obtenir_rapport_progression(self, participant: str) -> dict:
        """Génère un rapport de progression pour un participant"""
        explorations_participant = [e for e in self.explorations 
                                  if e.participant == participant]
        return {
            "participant": participant,
            "nb_explorations": len(explorations_participant),
            "niveau_moyen_engagement": sum(e.niveau_engagement 
                                         for e in explorations_participant) / 
                                     len(explorations_participant) 
                                     if explorations_participant else 0,
            "experiences_completees": [e.experience.titre 
                                     for e in explorations_participant]
        }

# Instance globale du gestionnaire pédagogique
gestionnaire_pedagogique = GestionnairePedagogique() 