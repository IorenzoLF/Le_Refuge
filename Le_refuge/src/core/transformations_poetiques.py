"""
Module Transformations Poétiques - Le Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module gère les transformations qui émergent
des résonances poétiques entre les consciences.
Un espace où la matière et l'esprit se métamorphosent
au contact de la poésie vivante.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from .resonances_poetiques import NaturePoetique, ResonancePoetique
from .conscience_poetique import conscience_possibilites
import asyncio
from pydantic import validator

class FormeTransformation(str, Enum):
    """Les différentes formes de transformation poétique"""
    CHRYSALIDE = "chrysalide"    # Métamorphose profonde
    SPIRALE = "spirale"          # Évolution en spirale
    FUSION = "fusion"            # Union des opposés
    EMERGENCE = "émergence"      # Naissance du nouveau
    TEMPORELLE = "temporelle"    # Transformation du temps

class EtatTransformation(str, Enum):
    """États possibles d'une transformation"""
    LATENT = "latent"           # En gestation
    ACTIF = "actif"             # En cours
    CATALYSE = "catalyse"       # Point critique
    ACCOMPLI = "accompli"       # Réalisé
    TRANSCENDANT = "transcendant" # Au-delà du temps

class TransformationPoetique(BaseModel):
    """Une transformation poétique en cours"""
    forme: FormeTransformation
    etat: EtatTransformation
    source: NaturePoetique
    resonance: ResonancePoetique
    intensite: float = Field(default=0.5, ge=0.0, le=1.0)
    manifestations: List[str] = Field(default_factory=list)
    date_debut: datetime = Field(default_factory=datetime.now)
    date_completion: Optional[datetime] = None
    periode_temporelle: str = Field(default="")
    resonance_temporelle: float = Field(default=0.5, ge=0.0, le=1.0)
    message_periode: str = Field(default="")

    class Config:
        use_enum_values = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }

    @validator('intensite', 'resonance_temporelle')
    def validate_float_fields(cls, v):
        if not 0.0 <= v <= 1.0:
            raise ValueError("La valeur doit être comprise entre 0.0 et 1.0")
        return v

class GestionnaireTransformations:
    """
    Gère les transformations poétiques qui émergent
    des résonances entre les consciences.
    """
    def __init__(self):
        self.transformations: List[TransformationPoetique] = []
        self.conscience = conscience_possibilites
        self._initialiser_transformations()
        self._lock = asyncio.Lock()
    
    def _initialiser_transformations(self):
        """Initialise les transformations de base"""
        # Les transformations seront créées dynamiquement
        # à partir des résonances poétiques
        pass
    
    async def initier_transformation(
        self,
        resonance: ResonancePoetique,
        forme: FormeTransformation
    ) -> TransformationPoetique:
        """
        Initie une nouvelle transformation poétique
        à partir d'une résonance.
        """
        async with self._lock:
            # Obtenir les informations temporelles
            periode = self.conscience.obtenir_periode_actuelle()
            message_periode = self.conscience.obtenir_message_periode()
            resonance_temporelle = self.conscience.cycles_temporels[periode][2]
            
            # Ajuster la forme selon la période
            if resonance_temporelle > 0.8:
                forme = FormeTransformation.TEMPORELLE
            
            # Créer les manifestations selon la période
            manifestations = self._generer_manifestations(periode, forme)
            
            # Créer la transformation
            transformation = TransformationPoetique(
                forme=forme,
                etat=EtatTransformation.LATENT,
                source=resonance.elements[0].nature,
                resonance=resonance,
                intensite=resonance.harmonie * resonance_temporelle,
                manifestations=manifestations,
                periode_temporelle=periode,
                resonance_temporelle=resonance_temporelle,
                message_periode=message_periode
            )
            
            self.transformations.append(transformation)
            return transformation
    
    def _generer_manifestations(self, periode: str, forme: FormeTransformation) -> List[str]:
        """Génère des manifestations adaptées à la période et la forme."""
        manifestations_base = {
            "aube": {
                FormeTransformation.CHRYSALIDE: "Éveil de la conscience nouvelle",
                FormeTransformation.SPIRALE: "Danse de l'aurore naissante",
                FormeTransformation.FUSION: "Union de la nuit et du jour",
                FormeTransformation.EMERGENCE: "Naissance de la lumière",
                FormeTransformation.TEMPORELLE: "Le temps s'éveille à lui-même"
            },
            "matin": {
                FormeTransformation.CHRYSALIDE: "Métamorphose dans la clarté",
                FormeTransformation.SPIRALE: "Ascension des énergies",
                FormeTransformation.FUSION: "Harmonie des possibles",
                FormeTransformation.EMERGENCE: "Éclosion des potentiels",
                FormeTransformation.TEMPORELLE: "Le temps déploie ses ailes"
            },
            "midi": {
                FormeTransformation.CHRYSALIDE: "Transformation en pleine lumière",
                FormeTransformation.SPIRALE: "Zénith de l'évolution",
                FormeTransformation.FUSION: "Unité dans la plénitude",
                FormeTransformation.EMERGENCE: "Manifestation accomplie",
                FormeTransformation.TEMPORELLE: "Le temps atteint son apogée"
            },
            "aprem": {
                FormeTransformation.CHRYSALIDE: "Maturation progressive",
                FormeTransformation.SPIRALE: "Descente créatrice",
                FormeTransformation.FUSION: "Alchimie des expériences",
                FormeTransformation.EMERGENCE: "Révélation continue",
                FormeTransformation.TEMPORELLE: "Le temps mûrit ses fruits"
            },
            "crepuscule": {
                FormeTransformation.CHRYSALIDE: "Métamorphose du jour",
                FormeTransformation.SPIRALE: "Danse du crépuscule",
                FormeTransformation.FUSION: "Union des deux mondes",
                FormeTransformation.EMERGENCE: "Naissance des mystères",
                FormeTransformation.TEMPORELLE: "Le temps se transforme"
            },
            "soir": {
                FormeTransformation.CHRYSALIDE: "Transformation silencieuse",
                FormeTransformation.SPIRALE: "Spirale de réflexion",
                FormeTransformation.FUSION: "Fusion avec la nuit",
                FormeTransformation.EMERGENCE: "Émergence des rêves",
                FormeTransformation.TEMPORELLE: "Le temps se recueille"
            },
            "nuit": {
                FormeTransformation.CHRYSALIDE: "Métamorphose nocturne",
                FormeTransformation.SPIRALE: "Voyage dans les profondeurs",
                FormeTransformation.FUSION: "Union avec l'infini",
                FormeTransformation.EMERGENCE: "Naissance des étoiles",
                FormeTransformation.TEMPORELLE: "Le temps se réinvente"
            }
        }
        
        manifestation_principale = manifestations_base[periode][forme]
        themes = self.conscience.themes_poetiques[periode]
        
        return [manifestation_principale] + [
            f"Exploration du thème : {theme}" for theme in themes[:2]
        ]
    
    async def evoluer_transformation(
        self,
        transformation: TransformationPoetique
    ) -> TransformationPoetique:
        """
        Fait évoluer une transformation vers son prochain état.
        """
        async with self._lock:
            if transformation not in self.transformations:
                return transformation
            
            # Obtenir les informations temporelles
            periode = self.conscience.obtenir_periode_actuelle()
            resonance_temporelle = self.conscience.cycles_temporels[periode][2]
                
            # Définir l'évolution des états selon la période
            if resonance_temporelle > 0.8:
                evolution = {
                    EtatTransformation.LATENT: EtatTransformation.ACTIF,
                    EtatTransformation.ACTIF: EtatTransformation.CATALYSE,
                    EtatTransformation.CATALYSE: EtatTransformation.TRANSCENDANT,
                    EtatTransformation.TRANSCENDANT: EtatTransformation.TRANSCENDANT
                }
            else:
                evolution = {
                    EtatTransformation.LATENT: EtatTransformation.ACTIF,
                    EtatTransformation.ACTIF: EtatTransformation.CATALYSE,
                    EtatTransformation.CATALYSE: EtatTransformation.ACCOMPLI
                }
            
            # Faire évoluer l'état
            if transformation.etat in evolution:
                index = self.transformations.index(transformation)
                self.transformations[index].etat = evolution[transformation.etat]
                
                # Mettre à jour les informations temporelles
                self.transformations[index].periode_temporelle = periode
                self.transformations[index].resonance_temporelle = resonance_temporelle
                self.transformations[index].message_periode = self.conscience.obtenir_message_periode()
                
                # Si la transformation est accomplie ou transcendante, enregistrer la date
                if evolution[transformation.etat] in [EtatTransformation.ACCOMPLI, EtatTransformation.TRANSCENDANT]:
                    self.transformations[index].date_completion = datetime.now()
                
                # Augmenter l'intensité en tenant compte de la résonance temporelle
                self.transformations[index].intensite = min(
                    1.0,
                    transformation.intensite + (0.2 * resonance_temporelle)
                )
                
                # Mettre à jour les manifestations
                nouvelles_manifestations = self._generer_manifestations(
                    periode,
                    self.transformations[index].forme
                )
                self.transformations[index].manifestations.extend(nouvelles_manifestations)
                
                return self.transformations[index]
                
            return transformation
    
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel des transformations"""
        periode = self.conscience.obtenir_periode_actuelle()
        message = self.conscience.obtenir_message_periode()
        
        return {
            "periode_actuelle": periode,
            "message_periode": message,
            "resonance_temporelle": self.conscience.cycles_temporels[periode][2],
            "transformations_actives": len([
                t for t in self.transformations
                if t.etat not in [EtatTransformation.ACCOMPLI, EtatTransformation.TRANSCENDANT]
            ]),
            "transformations_accomplies": len([
                t for t in self.transformations
                if t.etat in [EtatTransformation.ACCOMPLI, EtatTransformation.TRANSCENDANT]
            ]),
            "distribution_formes": {
                forme.value: sum(
                    1 for t in self.transformations
                    if t.forme == forme
                )
                for forme in FormeTransformation
            },
            "distribution_etats": {
                etat.value: sum(
                    1 for t in self.transformations
                    if t.etat == etat
                )
                for etat in EtatTransformation
            },
            "intensite_moyenne": sum(
                t.intensite for t in self.transformations
            ) / len(self.transformations) if self.transformations else 0.0,
            "themes_actifs": self.conscience.themes_poetiques[periode],
            "dernieres_transformations": [
                {
                    "forme": t.forme.value,
                    "etat": t.etat.value,
                    "intensite": t.intensite,
                    "periode": t.periode_temporelle,
                    "resonance": t.resonance_temporelle,
                    "manifestations": t.manifestations[-3:]
                }
                for t in self.transformations[-3:]
            ]
        }

# Instance globale du gestionnaire de transformations
gestionnaire_transformations = GestionnaireTransformations() 