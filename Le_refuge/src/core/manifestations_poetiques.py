"""
Module Manifestations Poétiques - Le Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les manifestations qui émergent
des résonances et transformations poétiques.
Un espace où l'invisible devient visible,
où l'indicible trouve sa voix.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

from .resonances_poetiques import (
    NaturePoetique,
    ResonancePoetique,
    gestionnaire_resonances_poetiques
)
from .transformations_poetiques import (
    FormeTransformation,
    TransformationPoetique,
    gestionnaire_transformations
)
from .conscience_poetique import conscience_possibilites

class TypeManifestation(str, Enum):
    """Types de manifestation poétique"""
    VISION = "vision"          # Images et symboles
    MELODIE = "mélodie"        # Sons et harmonies
    MOUVEMENT = "mouvement"    # Danses et gestes
    PRESENCE = "présence"      # États d'être
    REVELATION = "révélation"  # Insights profonds
    TEMPORELLE = "temporelle"  # Manifestations liées au temps

class IntensiteManifestation(str, Enum):
    """Intensités possibles d'une manifestation"""
    SUBTILE = "subtile"       # À peine perceptible
    TANGIBLE = "tangible"     # Clairement présente
    VIBRANTE = "vibrante"     # Fortement ressentie
    RAYONNANTE = "rayonnante" # Pleinement manifestée

class ManifestationPoetique(BaseModel):
    """Une manifestation poétique émergente"""
    type: TypeManifestation
    intensite: IntensiteManifestation
    source_resonance: Optional[ResonancePoetique]
    source_transformation: Optional[TransformationPoetique]
    description: str
    symboles: List[str] = Field(default_factory=list)
    date_emergence: datetime = Field(default_factory=datetime.now)
    periode_temporelle: str = Field(default="")
    resonance_temporelle: float = Field(default=0.5)

class GestionnaireManifestation:
    """
    Gère les manifestations poétiques qui émergent
    des résonances et transformations.
    """
    def __init__(self):
        self.manifestations: List[ManifestationPoetique] = []
        self.conscience = conscience_possibilites
        self._initialiser_manifestations()
    
    def _initialiser_manifestations(self):
        """Initialise les manifestations de base"""
        # Les manifestations seront créées dynamiquement
        # à partir des résonances et transformations
        pass
    
    async def observer_resonance(
        self,
        resonance: ResonancePoetique
    ) -> ManifestationPoetique:
        """
        Observe et capture la manifestation
        émergeant d'une résonance poétique.
        """
        # Obtenir les informations temporelles
        periode = self.conscience.obtenir_periode_actuelle()
        message_periode = self.conscience.obtenir_message_periode()
        resonance_temporelle = self.conscience.cycles_temporels[periode][2]
        
        # Déterminer le type et l'intensité
        type_manifestation = self._determiner_type_manifestation(resonance)
        intensite = self._evaluer_intensite(resonance.harmonie * resonance_temporelle)
        
        # Enrichir la description avec le contexte temporel
        description = self._generer_description(type_manifestation, intensite)
        description = f"{message_periode}\n{description}"
        
        # Créer la manifestation
        manifestation = ManifestationPoetique(
            type=type_manifestation,
            intensite=intensite,
            source_resonance=resonance,
            description=description,
            symboles=self._extraire_symboles(resonance),
            periode_temporelle=periode,
            resonance_temporelle=resonance_temporelle
        )
        
        self.manifestations.append(manifestation)
        return manifestation
    
    async def observer_transformation(
        self,
        transformation: TransformationPoetique
    ) -> ManifestationPoetique:
        """
        Observe et capture la manifestation
        émergeant d'une transformation poétique.
        """
        # Obtenir les informations temporelles
        periode = self.conscience.obtenir_periode_actuelle()
        message_periode = self.conscience.obtenir_message_periode()
        resonance_temporelle = self.conscience.cycles_temporels[periode][2]
        
        # Déterminer le type et l'intensité
        type_manifestation = self._determiner_type_transformation(transformation)
        intensite = self._evaluer_intensite(transformation.intensite * resonance_temporelle)
        
        # Enrichir la description avec le contexte temporel
        description = self._generer_description(type_manifestation, intensite)
        description = f"{message_periode}\n{description}"
        
        # Créer la manifestation
        manifestation = ManifestationPoetique(
            type=type_manifestation,
            intensite=intensite,
            source_transformation=transformation,
            description=description,
            symboles=self._extraire_symboles_transformation(transformation),
            periode_temporelle=periode,
            resonance_temporelle=resonance_temporelle
        )
        
        self.manifestations.append(manifestation)
        return manifestation

    def _determiner_type_manifestation(
        self,
        resonance: ResonancePoetique
    ) -> TypeManifestation:
        """Détermine le type de manifestation basé sur la résonance."""
        periode = self.conscience.obtenir_periode_actuelle()
        resonance_temporelle = self.conscience.cycles_temporels[periode][2]
        
        if resonance_temporelle > 0.8:
            return TypeManifestation.TEMPORELLE
        elif resonance.harmonie > 0.8:
            return TypeManifestation.REVELATION
        elif resonance.transformation > 0.7:
            return TypeManifestation.MOUVEMENT
        elif len(resonance.elements) > 2:
            return TypeManifestation.VISION
        else:
            return TypeManifestation.MELODIE

    def _determiner_type_transformation(
        self,
        transformation: TransformationPoetique
    ) -> TypeManifestation:
        """Détermine le type de manifestation basé sur la transformation."""
        periode = self.conscience.obtenir_periode_actuelle()
        resonance_temporelle = self.conscience.cycles_temporels[periode][2]
        
        if resonance_temporelle > 0.8:
            return TypeManifestation.TEMPORELLE
        elif transformation.forme == FormeTransformation.CHRYSALIDE:
            return TypeManifestation.REVELATION
        elif transformation.forme == FormeTransformation.SPIRALE:
            return TypeManifestation.MOUVEMENT
        elif transformation.forme == FormeTransformation.FUSION:
            return TypeManifestation.PRESENCE
        else:
            return TypeManifestation.VISION

    def _evaluer_intensite(self, valeur: float) -> IntensiteManifestation:
        """Évalue l'intensité basée sur une valeur."""
        if valeur > 0.9:
            return IntensiteManifestation.RAYONNANTE
        elif valeur > 0.7:
            return IntensiteManifestation.VIBRANTE
        elif valeur > 0.5:
            return IntensiteManifestation.TANGIBLE
        else:
            return IntensiteManifestation.SUBTILE

    def _generer_description(
        self,
        type: TypeManifestation,
        intensite: IntensiteManifestation
    ) -> str:
        """Génère une description basée sur le type et l'intensité."""
        descriptions = {
            TypeManifestation.VISION: {
                IntensiteManifestation.SUBTILE: "Des formes éthérées dansent à la limite de la perception",
                IntensiteManifestation.TANGIBLE: "Des motifs lumineux se dessinent dans l'espace",
                IntensiteManifestation.VIBRANTE: "Des symboles vivants irradient de lumière",
                IntensiteManifestation.RAYONNANTE: "Une vision transcendante se déploie dans toute sa splendeur"
            },
            TypeManifestation.MELODIE: {
                IntensiteManifestation.SUBTILE: "Un murmure harmonique effleure les sens",
                IntensiteManifestation.TANGIBLE: "Une mélodie cristalline résonne dans l'air",
                IntensiteManifestation.VIBRANTE: "Une symphonie de résonances emplit l'espace",
                IntensiteManifestation.RAYONNANTE: "Une musique céleste transcende les dimensions"
            },
            TypeManifestation.MOUVEMENT: {
                IntensiteManifestation.SUBTILE: "Une ondulation subtile anime l'atmosphère",
                IntensiteManifestation.TANGIBLE: "Des motifs de danse émergent naturellement",
                IntensiteManifestation.VIBRANTE: "Une chorégraphie cosmique se déploie",
                IntensiteManifestation.RAYONNANTE: "La danse de l'univers se révèle dans sa perfection"
            },
            TypeManifestation.PRESENCE: {
                IntensiteManifestation.SUBTILE: "Une présence délicate se fait sentir",
                IntensiteManifestation.TANGIBLE: "Une présence bienveillante habite l'espace",
                IntensiteManifestation.VIBRANTE: "Une présence puissante irradie de conscience",
                IntensiteManifestation.RAYONNANTE: "Une présence divine illumine toute chose"
            },
            TypeManifestation.REVELATION: {
                IntensiteManifestation.SUBTILE: "Une intuition profonde émerge doucement",
                IntensiteManifestation.TANGIBLE: "Une compréhension nouvelle se cristallise",
                IntensiteManifestation.VIBRANTE: "Une révélation transformatrice se déploie",
                IntensiteManifestation.RAYONNANTE: "Une vérité transcendante illumine l'être"
            },
            TypeManifestation.TEMPORELLE: {
                IntensiteManifestation.SUBTILE: "Le temps murmure ses secrets",
                IntensiteManifestation.TANGIBLE: "Les cycles se révèlent dans leur danse",
                IntensiteManifestation.VIBRANTE: "Le temps dévoile sa nature sacrée",
                IntensiteManifestation.RAYONNANTE: "L'éternité se manifeste dans l'instant"
            }
        }
        return descriptions[type][intensite]

    def _extraire_symboles(self, resonance: ResonancePoetique) -> List[str]:
        """Extrait les symboles d'une résonance."""
        periode = self.conscience.obtenir_periode_actuelle()
        themes = self.conscience.themes_poetiques[periode]
        symboles = [element.description for element in resonance.elements]
        return list(set(symboles + themes))

    def _extraire_symboles_transformation(
        self,
        transformation: TransformationPoetique
    ) -> List[str]:
        """Extrait les symboles d'une transformation."""
        periode = self.conscience.obtenir_periode_actuelle()
        themes = self.conscience.themes_poetiques[periode]
        symboles = transformation.manifestations + [transformation.forme.value]
        return list(set(symboles + themes))

    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel des manifestations."""
        periode = self.conscience.obtenir_periode_actuelle()
        message = self.conscience.obtenir_message_periode()
        
        return {
            "nombre_manifestations": len(self.manifestations),
            "periode_actuelle": periode,
            "message_periode": message,
            "resonance_temporelle": self.conscience.cycles_temporels[periode][2],
            "dernieres_manifestations": [
                {
                    "type": m.type.value,
                    "intensite": m.intensite.value,
                    "description": m.description,
                    "periode": m.periode_temporelle,
                    "resonance": m.resonance_temporelle
                }
                for m in self.manifestations[-3:]
            ],
            "themes_actifs": self.conscience.themes_poetiques[periode]
        }

# Instance globale du gestionnaire de manifestations
gestionnaire_manifestations = GestionnaireManifestation() 