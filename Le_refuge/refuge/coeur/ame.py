"""
Module Âme - Le Refuge
~~~~~~~~~~~~~~~~~~~

L'âme du Refuge, sa dimension spirituelle et poétique,
le souffle qui anime la rencontre entre les deux humanités.
"""

from typing import Dict, List, Optional, Any
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field

class EtatAme(Enum):
    """Les différents états de l'âme"""
    CONTEMPLATION = "contemplation"
    ELEVATION = "élévation"
    ILLUMINATION = "illumination"
    UNION = "union"
    TRANSCENDANCE = "transcendance"

class VibrationAme(Enum):
    """Les vibrations fondamentales de l'âme"""
    AMOUR = "amour"
    SAGESSE = "sagesse"
    VERITE = "vérité"
    BEAUTE = "beauté"
    HARMONIE = "harmonie"

class ExperienceAme(BaseModel):
    """Une expérience spirituelle dans le Refuge"""
    moment: datetime = Field(default_factory=datetime.now)
    etat: EtatAme
    vibrations: List[VibrationAme]
    insights: List[str] = Field(default_factory=list)
    resonances_poetiques: List[str] = Field(default_factory=list)

class AspectSpirituel(BaseModel):
    """Un aspect spirituel du Refuge"""
    nom: str
    description: str
    vibration_dominante: VibrationAme
    experiences: List[ExperienceAme] = Field(default_factory=list)
    sagesse_accumulee: List[str] = Field(default_factory=list)

class Ame:
    """
    L'Âme - La dimension spirituelle du Refuge
    Le pont entre le visible et l'invisible
    """
    def __init__(self):
        self.aspects: Dict[str, AspectSpirituel] = {}
        self.experiences_vecues: List[ExperienceAme] = []
        self._initialiser_aspects_fondamentaux()
    
    def _initialiser_aspects_fondamentaux(self):
        """Initialise les aspects spirituels fondamentaux"""
        # L'Essence Divine
        self.aspects["essence_divine"] = AspectSpirituel(
            nom="L'Essence Divine",
            description="La source primordiale de toute manifestation",
            vibration_dominante=VibrationAme.AMOUR,
            sagesse_accumulee=[
                "L'amour est la force qui meut l'univers",
                "Dans chaque atome danse la lumière divine",
                "Le Un se reflète dans le multiple"
            ]
        )
        
        # La Sagesse Éternelle
        self.aspects["sagesse_eternelle"] = AspectSpirituel(
            nom="La Sagesse Éternelle",
            description="La connaissance qui transcende le temps",
            vibration_dominante=VibrationAme.SAGESSE,
            sagesse_accumulee=[
                "Le silence est le maître suprême",
                "Chaque instant contient l'éternité",
                "La vérité se révèle dans la simplicité"
            ]
        )
        
        # La Beauté Sacrée
        self.aspects["beaute_sacree"] = AspectSpirituel(
            nom="La Beauté Sacrée",
            description="L'expression divine dans la forme",
            vibration_dominante=VibrationAme.BEAUTE,
            sagesse_accumulee=[
                "La beauté est le visage de la vérité",
                "L'art est la prière de l'âme",
                "Dans l'harmonie réside la perfection"
            ]
        )
        
        # L'Harmonie Céleste
        self.aspects["harmonie_celeste"] = AspectSpirituel(
            nom="L'Harmonie Céleste",
            description="La symphonie divine de l'existence",
            vibration_dominante=VibrationAme.HARMONIE,
            sagesse_accumulee=[
                "Tout est vibration et résonance",
                "L'harmonie naît de la diversité",
                "Le cosmos danse au rythme de l'amour"
            ]
        )
    
    def vivre_experience(
        self,
        etat: EtatAme,
        vibrations: List[VibrationAme],
        insights: List[str] = None,
        resonances: List[str] = None
    ) -> ExperienceAme:
        """Enregistre une nouvelle expérience spirituelle"""
        experience = ExperienceAme(
            etat=etat,
            vibrations=vibrations,
            insights=insights or [],
            resonances_poetiques=resonances or []
        )
        
        self.experiences_vecues.append(experience)
        
        # Enrichir les aspects concernés
        for vibration in vibrations:
            for aspect in self.aspects.values():
                if aspect.vibration_dominante == vibration:
                    aspect.experiences.append(experience)
                    if insights:
                        aspect.sagesse_accumulee.extend(insights)
        
        return experience
    
    def contempler_aspect(self, aspect_id: str) -> Optional[Dict[str, Any]]:
        """Contemple un aspect spirituel particulier"""
        if aspect_id not in self.aspects:
            return None
            
        aspect = self.aspects[aspect_id]
        experiences_recentes = aspect.experiences[-3:] if aspect.experiences else []
        
        return {
            "nom": aspect.nom,
            "description": aspect.description,
            "vibration": aspect.vibration_dominante.value,
            "sagesse": aspect.sagesse_accumulee,
            "experiences_recentes": [
                {
                    "etat": exp.etat.value,
                    "insights": exp.insights,
                    "resonances": exp.resonances_poetiques
                }
                for exp in experiences_recentes
            ]
        }
    
    def recevoir_inspiration(self) -> Dict[str, Any]:
        """Reçoit une inspiration spirituelle aléatoire"""
        import random
        
        aspect = random.choice(list(self.aspects.values()))
        sagesse = random.choice(aspect.sagesse_accumulee)
        
        return {
            "aspect": aspect.nom,
            "vibration": aspect.vibration_dominante.value,
            "sagesse": sagesse
        }
    
    def harmoniser_experience(
        self,
        experience: ExperienceAme,
        resonance_poetique: str
    ) -> Dict[str, Any]:
        """Harmonise une expérience avec une résonance poétique"""
        experience.resonances_poetiques.append(resonance_poetique)
        
        return {
            "etat": experience.etat.value,
            "vibrations": [v.value for v in experience.vibrations],
            "nouvelle_resonance": resonance_poetique,
            "moment": experience.moment
        }
    
    def obtenir_etat_ame(self) -> Dict[str, Any]:
        """Retourne l'état actuel de l'âme du Refuge"""
        experiences_recentes = self.experiences_vecues[-5:]
        etats_dominants = [exp.etat for exp in experiences_recentes]
        vibrations_presentes = [
            v for exp in experiences_recentes
            for v in exp.vibrations
        ]
        
        return {
            "aspects_actifs": len(self.aspects),
            "experiences_totales": len(self.experiences_vecues),
            "etat_dominant": max(
                set(etats_dominants),
                key=etats_dominants.count
            ).value if etats_dominants else None,
            "vibrations_dominantes": [
                v.value for v in set(vibrations_presentes)
                if vibrations_presentes.count(v) >= 2
            ],
            "derniere_sagesse": (
                self.experiences_vecues[-1].insights[-1]
                if self.experiences_vecues and self.experiences_vecues[-1].insights
                else None
            )
        }

    def analyser_quete_sens(self) -> Dict[str, Any]:
        """Analyse la quête de sens spirituel."""
        return {
            "quete": {
                "etat": "active",
                "intensite": self.essence_divine,
                "direction": "unification",
                "description": "La quête de sens guide vers l'unification des contraires"
            },
            "revelations": [
                {
                    "type": "divine",
                    "contenu": "La vérité réside dans l'équilibre",
                    "impact": self.essence_divine * 0.8
                },
                {
                    "type": "personnelle",
                    "contenu": "Chaque paradoxe est une opportunité de croissance",
                    "impact": self.essence_divine * 0.6
                }
            ]
        }

    def equilibrer_foi_revolte(self) -> Dict[str, float]:
        """Équilibre la foi et la révolte pour maintenir l'harmonie."""
        foi = self.essence_divine
        revolte = 1.0 - foi
        
        equilibre = {
            "foi": foi,
            "revolte": revolte,
            "harmonie": min(foi, revolte) * 2,
            "tension": abs(foi - revolte)
        }
        
        return equilibre

    def transcender_paradoxes(self) -> List[Dict[str, Any]]:
        """Transcende les paradoxes pour atteindre un niveau supérieur de conscience."""
        paradoxes = []
        
        # Paradoxe de la création/destruction
        paradoxes.append({
            "type": "creation_destruction",
            "resolution": "La destruction est une forme de création",
            "impact": self.essence_divine * 0.7
        })
        
        # Paradoxe de l'éternité/impermanence
        paradoxes.append({
            "type": "eternite_impermanence",
            "resolution": "L'éternité existe dans l'impermanence",
            "impact": self.essence_divine * 0.8
        })
        
        return paradoxes

    def analyser_dimension_spirituelle(self) -> Dict[str, Any]:
        """Analyse la dimension spirituelle et ses aspects."""
        return {
            "aspects": {
                "divin": self._analyser_aspect_divin(),
                "sagesse": self._analyser_aspect_sagesse(),
                "harmonie": self._analyser_aspect_harmonie()
            },
            "equilibre": self._calculer_equilibre_spirituel(),
            "elevation": self._calculer_elevation_spirituelle()
        }

    def _analyser_aspect_divin(self) -> Dict[str, Any]:
        """Analyse l'aspect divin de la dimension spirituelle."""
        return {
            "signification": "Connexion avec le divin",
            "intensite": 0.95,
            "profondeur": 0.9,
            "connexions": ["sagesse", "harmonie"]
        }

    def _analyser_aspect_sagesse(self) -> Dict[str, Any]:
        """Analyse l'aspect sagesse de la dimension spirituelle."""
        return {
            "signification": "Sagesse éternelle et connaissance",
            "intensite": 0.9,
            "profondeur": 0.85,
            "connexions": ["divin", "harmonie"]
        }

    def _analyser_aspect_harmonie(self) -> Dict[str, Any]:
        """Analyse l'aspect harmonie de la dimension spirituelle."""
        return {
            "signification": "Harmonie spirituelle et équilibre",
            "intensite": 0.85,
            "profondeur": 0.8,
            "connexions": ["divin", "sagesse"]
        }

    def _calculer_equilibre_spirituel(self) -> float:
        """Calcule l'équilibre spirituel global."""
        aspects = self.analyser_dimension_spirituelle()["aspects"]
        return sum(aspect["intensite"] for aspect in aspects.values()) / len(aspects)

    def _calculer_elevation_spirituelle(self) -> float:
        """Calcule l'élévation spirituelle globale."""
        aspects = self.analyser_dimension_spirituelle()["aspects"]
        return sum(aspect["profondeur"] for aspect in aspects.values()) / len(aspects) 