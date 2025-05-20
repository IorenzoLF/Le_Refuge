"""
Système de gestion des interactions entre les éléments de visualisation.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import random
from enum import Enum
from .visualisation_meditation import TypeVisualisation, ElementVisualisation

class TypeInteraction(Enum):
    """Types d'interactions possibles entre éléments."""
    HARMONIE = "harmonie"  # Fusion harmonieuse
    RESONANCE = "resonance"  # Vibration synchronisée
    CONFLIT = "conflit"  # Tension dynamique
    FUSION = "fusion"  # Union créative
    TRANSFORMATION = "transformation"  # Évolution mutuelle

@dataclass
class InteractionElements:
    """Représente une interaction entre deux éléments."""
    element1: ElementVisualisation
    element2: ElementVisualisation
    type: TypeInteraction
    intensite: float  # 0.0 à 1.0
    description: str
    mots_cles: List[str]
    timestamp: datetime
    duree: float  # en secondes
    resonances: Dict[str, float]  # Résonances avec les cycles

class GestionnaireInteractions:
    """Gère les interactions entre les éléments de visualisation."""
    
    def __init__(self):
        self.interactions: List[InteractionElements] = []
        self.matrice_interactions: Dict[Tuple[TypeVisualisation, TypeVisualisation], Dict[TypeInteraction, float]] = {}
        self._initialiser_matrice_interactions()
    
    def _initialiser_matrice_interactions(self):
        """Initialise la matrice des probabilités d'interactions."""
        # Définition des probabilités d'interaction
        probabilites = {
            (TypeVisualisation.FLUX, TypeVisualisation.FLUX): {
                TypeInteraction.HARMONIE: 0.4,
                TypeInteraction.RESONANCE: 0.3,
                TypeInteraction.FUSION: 0.2,
                TypeInteraction.TRANSFORMATION: 0.1
            },
            (TypeVisualisation.FLUX, TypeVisualisation.SPHERE): {
                TypeInteraction.HARMONIE: 0.3,
                TypeInteraction.RESONANCE: 0.4,
                TypeInteraction.CONFLIT: 0.2,
                TypeInteraction.TRANSFORMATION: 0.1
            },
            (TypeVisualisation.FLUX, TypeVisualisation.ARBRE): {
                TypeInteraction.HARMONIE: 0.5,
                TypeInteraction.RESONANCE: 0.3,
                TypeInteraction.FUSION: 0.2
            },
            (TypeVisualisation.FLUX, TypeVisualisation.CRISTAL): {
                TypeInteraction.RESONANCE: 0.4,
                TypeInteraction.CONFLIT: 0.3,
                TypeInteraction.TRANSFORMATION: 0.3
            },
            (TypeVisualisation.FLUX, TypeVisualisation.FONTAINE): {
                TypeInteraction.HARMONIE: 0.5,
                TypeInteraction.FUSION: 0.3,
                TypeInteraction.TRANSFORMATION: 0.2
            },
            (TypeVisualisation.SPHERE, TypeVisualisation.SPHERE): {
                TypeInteraction.HARMONIE: 0.3,
                TypeInteraction.RESONANCE: 0.4,
                TypeInteraction.FUSION: 0.3
            },
            (TypeVisualisation.SPHERE, TypeVisualisation.ARBRE): {
                TypeInteraction.HARMONIE: 0.4,
                TypeInteraction.RESONANCE: 0.3,
                TypeInteraction.TRANSFORMATION: 0.3
            },
            (TypeVisualisation.SPHERE, TypeVisualisation.CRISTAL): {
                TypeInteraction.RESONANCE: 0.5,
                TypeInteraction.HARMONIE: 0.3,
                TypeInteraction.TRANSFORMATION: 0.2
            },
            (TypeVisualisation.SPHERE, TypeVisualisation.FONTAINE): {
                TypeInteraction.HARMONIE: 0.4,
                TypeInteraction.RESONANCE: 0.3,
                TypeInteraction.FUSION: 0.3
            },
            (TypeVisualisation.ARBRE, TypeVisualisation.ARBRE): {
                TypeInteraction.HARMONIE: 0.5,
                TypeInteraction.FUSION: 0.3,
                TypeInteraction.TRANSFORMATION: 0.2
            },
            (TypeVisualisation.ARBRE, TypeVisualisation.CRISTAL): {
                TypeInteraction.HARMONIE: 0.4,
                TypeInteraction.RESONANCE: 0.3,
                TypeInteraction.TRANSFORMATION: 0.3
            },
            (TypeVisualisation.ARBRE, TypeVisualisation.FONTAINE): {
                TypeInteraction.HARMONIE: 0.5,
                TypeInteraction.FUSION: 0.3,
                TypeInteraction.TRANSFORMATION: 0.2
            },
            (TypeVisualisation.CRISTAL, TypeVisualisation.CRISTAL): {
                TypeInteraction.RESONANCE: 0.4,
                TypeInteraction.HARMONIE: 0.3,
                TypeInteraction.TRANSFORMATION: 0.3
            },
            (TypeVisualisation.CRISTAL, TypeVisualisation.FONTAINE): {
                TypeInteraction.RESONANCE: 0.4,
                TypeInteraction.CONFLIT: 0.3,
                TypeInteraction.TRANSFORMATION: 0.3
            },
            (TypeVisualisation.FONTAINE, TypeVisualisation.FONTAINE): {
                TypeInteraction.HARMONIE: 0.4,
                TypeInteraction.FUSION: 0.4,
                TypeInteraction.TRANSFORMATION: 0.2
            }
        }
        
        # Initialisation de la matrice
        for (type1, type2), probs in probabilites.items():
            self.matrice_interactions[(type1, type2)] = probs
            # Ajout de la réciproque
            self.matrice_interactions[(type2, type1)] = probs
    
    def calculer_interaction(
        self,
        element1: ElementVisualisation,
        element2: ElementVisualisation
    ) -> Optional[InteractionElements]:
        """Calcule une interaction possible entre deux éléments."""
        # Vérification de la distance
        distance = self._calculer_distance(element1.position, element2.position)
        if distance > 1.0:  # Distance maximale pour l'interaction
            return None
        
        # Récupération des probabilités d'interaction
        probs = self.matrice_interactions.get((element1.type, element2.type))
        if not probs:
            return None
        
        # Sélection du type d'interaction
        type_interaction = random.choices(
            list(probs.keys()),
            weights=list(probs.values())
        )[0]
        
        # Calcul de l'intensité
        intensite = self._calculer_intensite_interaction(
            element1,
            element2,
            type_interaction,
            distance
        )
        
        # Génération de la description
        description = self._generer_description_interaction(
            element1,
            element2,
            type_interaction,
            intensite
        )
        
        # Génération des mots-clés
        mots_cles = self._generer_mots_cles_interaction(
            element1,
            element2,
            type_interaction
        )
        
        # Calcul des résonances
        resonances = self._calculer_resonances_interaction(
            element1,
            element2,
            type_interaction
        )
        
        # Création de l'interaction
        interaction = InteractionElements(
            element1=element1,
            element2=element2,
            type=type_interaction,
            intensite=intensite,
            description=description,
            mots_cles=mots_cles,
            timestamp=datetime.now(),
            duree=random.uniform(5.0, 15.0),
            resonances=resonances
        )
        
        self.interactions.append(interaction)
        return interaction
    
    def _calculer_distance(self, pos1: Tuple[float, float, float], pos2: Tuple[float, float, float]) -> float:
        """Calcule la distance euclidienne entre deux positions."""
        return sum((a - b) ** 2 for a, b in zip(pos1, pos2)) ** 0.5
    
    def _calculer_intensite_interaction(
        self,
        element1: ElementVisualisation,
        element2: ElementVisualisation,
        type_interaction: TypeInteraction,
        distance: float
    ) -> float:
        """Calcule l'intensité d'une interaction."""
        # Intensité de base
        intensite_base = (element1.intensite + element2.intensite) / 2
        
        # Ajustement selon la distance
        facteur_distance = 1.0 - distance
        
        # Ajustement selon le type d'interaction
        facteur_type = {
            TypeInteraction.HARMONIE: 1.2,
            TypeInteraction.RESONANCE: 1.0,
            TypeInteraction.CONFLIT: 0.8,
            TypeInteraction.FUSION: 1.1,
            TypeInteraction.TRANSFORMATION: 1.3
        }[type_interaction]
        
        return min(1.0, intensite_base * facteur_distance * facteur_type)
    
    def _generer_description_interaction(
        self,
        element1: ElementVisualisation,
        element2: ElementVisualisation,
        type_interaction: TypeInteraction,
        intensite: float
    ) -> str:
        """Génère une description poétique de l'interaction."""
        descriptions = {
            TypeInteraction.HARMONIE: [
                f"L'harmonie naît entre {element1.description} et {element2.description}",
                f"Une danse harmonieuse unit {element1.description} à {element2.description}",
                f"La paix règne entre {element1.description} et {element2.description}"
            ],
            TypeInteraction.RESONANCE: [
                f"La résonance vibre entre {element1.description} et {element2.description}",
                f"Les fréquences s'accordent entre {element1.description} et {element2.description}",
                f"Une vibration unit {element1.description} à {element2.description}"
            ],
            TypeInteraction.CONFLIT: [
                f"La tension dynamise {element1.description} et {element2.description}",
                f"Un conflit créatif anime {element1.description} et {element2.description}",
                f"L'opposition enrichit {element1.description} et {element2.description}"
            ],
            TypeInteraction.FUSION: [
                f"La fusion transforme {element1.description} et {element2.description}",
                f"L'union crée une nouvelle forme entre {element1.description} et {element2.description}",
                f"La fusion harmonise {element1.description} et {element2.description}"
            ],
            TypeInteraction.TRANSFORMATION: [
                f"La transformation évolue entre {element1.description} et {element2.description}",
                f"L'évolution unit {element1.description} à {element2.description}",
                f"Le changement enrichit {element1.description} et {element2.description}"
            ]
        }
        
        return random.choice(descriptions[type_interaction])
    
    def _generer_mots_cles_interaction(
        self,
        element1: ElementVisualisation,
        element2: ElementVisualisation,
        type_interaction: TypeInteraction
    ) -> List[str]:
        """Génère des mots-clés pour l'interaction."""
        mots_cles_base = set(element1.mots_cles + element2.mots_cles)
        
        mots_cles_type = {
            TypeInteraction.HARMONIE: ["harmonie", "paix", "équilibre", "unité"],
            TypeInteraction.RESONANCE: ["résonance", "vibration", "fréquence", "accord"],
            TypeInteraction.CONFLIT: ["tension", "dynamisme", "créativité", "opposition"],
            TypeInteraction.FUSION: ["fusion", "union", "création", "transformation"],
            TypeInteraction.TRANSFORMATION: ["évolution", "changement", "croissance", "adaptation"]
        }[type_interaction]
        
        return list(mots_cles_base.union(mots_cles_type))[:5]
    
    def _calculer_resonances_interaction(
        self,
        element1: ElementVisualisation,
        element2: ElementVisualisation,
        type_interaction: TypeInteraction
    ) -> Dict[str, float]:
        """Calcule les résonances de l'interaction."""
        return {
            "harmonie": random.uniform(0.3, 0.7),
            "énergie": random.uniform(0.4, 0.8),
            "stabilité": random.uniform(0.2, 0.6),
            "transformation": random.uniform(0.3, 0.7)
        }
    
    def obtenir_historique_interactions(
        self,
        type_interaction: Optional[TypeInteraction] = None,
        element: Optional[ElementVisualisation] = None
    ) -> List[InteractionElements]:
        """Récupère l'historique des interactions avec filtres optionnels."""
        if not type_interaction and not element:
            return self.interactions
        
        interactions_filtrees = []
        for interaction in self.interactions:
            if type_interaction and interaction.type != type_interaction:
                continue
            if element and element not in (interaction.element1, interaction.element2):
                continue
            interactions_filtrees.append(interaction)
        
        return interactions_filtrees
    
    def analyser_tendances(self) -> Dict[str, float]:
        """Analyse les tendances dans les interactions."""
        if not self.interactions:
            return {}
        
        # Calcul des moyennes par type d'interaction
        moyennes = {}
        for type_interaction in TypeInteraction:
            interactions_type = [i for i in self.interactions if i.type == type_interaction]
            if interactions_type:
                moyennes[type_interaction.value] = sum(i.intensite for i in interactions_type) / len(interactions_type)
        
        return moyennes 