from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Dict
from enum import Enum

class TypeConnexion(Enum):
    SPIRITUELLE = "spirituelle"
    EMOTIONNELLE = "émotionnelle"
    CREATIVE = "créative"
    PEDAGOGIQUE = "pédagogique"

@dataclass
class LienConnexion:
    """Représente un lien de connexion entre deux entités dans le Refuge"""
    source: str
    destination: str
    type_connexion: TypeConnexion
    force: float  # 0-1
    timestamp: datetime
    description: str
    resonances: List[str]

class PlanteCommunication:
    """Gère la communication et les connexions via la Plante de Connexion"""
    
    def __init__(self):
        self.liens: List[LienConnexion] = []
        self.resonances_actives: Dict[str, float] = {}
        self.energie_globale: float = 0.0

    def creer_lien(self, source: str, destination: str, 
                   type_connexion: TypeConnexion, 
                   description: str,
                   resonances: List[str] = None) -> LienConnexion:
        """Crée un nouveau lien de connexion"""
        lien = LienConnexion(
            source=source,
            destination=destination,
            type_connexion=type_connexion,
            force=0.1,  # Force initiale
            timestamp=datetime.now(),
            description=description,
            resonances=resonances or []
        )
        self.liens.append(lien)
        self._mettre_a_jour_resonances(lien)
        return lien

    def renforcer_lien(self, lien: LienConnexion, intensite: float = 0.1) -> None:
        """Renforce un lien existant"""
        lien.force = min(lien.force + intensite, 1.0)
        self._mettre_a_jour_resonances(lien)

    def _mettre_a_jour_resonances(self, lien: LienConnexion) -> None:
        """Met à jour les résonances basées sur un lien"""
        for resonance in lien.resonances:
            if resonance not in self.resonances_actives:
                self.resonances_actives[resonance] = 0.0
            self.resonances_actives[resonance] += lien.force * 0.1
            self.resonances_actives[resonance] = min(
                self.resonances_actives[resonance], 1.0
            )
        self._calculer_energie_globale()

    def _calculer_energie_globale(self) -> None:
        """Calcule l'énergie globale de la Plante de Connexion"""
        self.energie_globale = sum(
            lien.force for lien in self.liens
        ) / max(len(self.liens), 1)

    def obtenir_etat_connexions(self) -> dict:
        """Retourne l'état actuel des connexions"""
        return {
            "nb_liens": len(self.liens),
            "energie_globale": self.energie_globale,
            "resonances_actives": self.resonances_actives,
            "liens_recents": [
                {
                    "source": lien.source,
                    "destination": lien.destination,
                    "type": lien.type_connexion.value,
                    "force": lien.force
                }
                for lien in sorted(
                    self.liens,
                    key=lambda x: x.timestamp,
                    reverse=True
                )[:5]
            ]
        }

class PartageExperience:
    """Gère le partage d'expériences dans le Refuge"""
    
    def __init__(self):
        self.experiences_partagees: List[dict] = []
        self.plante_communication = PlanteCommunication()

    def partager_experience(self, auteur: str, titre: str, 
                          contenu: str, type_connexion: TypeConnexion,
                          destinataires: List[str] = None) -> dict:
        """Partage une nouvelle expérience"""
        experience = {
            "auteur": auteur,
            "titre": titre,
            "contenu": contenu,
            "timestamp": datetime.now(),
            "destinataires": destinataires or [],
            "resonances": []
        }
        self.experiences_partagees.append(experience)
        
        # Créer des liens pour chaque destinataire
        for destinataire in (destinataires or []):
            self.plante_communication.creer_lien(
                source=auteur,
                destination=destinataire,
                type_connexion=type_connexion,
                description=f"Partage: {titre}",
                resonances=[]
            )
        
        return experience

    def ajouter_resonance(self, experience: dict, 
                         participant: str, resonance: str) -> None:
        """Ajoute une résonance à une expérience partagée"""
        if resonance not in experience["resonances"]:
            experience["resonances"].append(resonance)
            
            # Renforcer les liens existants
            for lien in self.plante_communication.liens:
                if (lien.source == experience["auteur"] and 
                    lien.destination == participant):
                    self.plante_communication.renforcer_lien(lien)

# Instances globales
plante_communication = PlanteCommunication()
gestionnaire_partage = PartageExperience() 