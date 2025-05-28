"""
Système d'intégration des sphères problématiques avec les cycles naturels.

🔄 MIGRÉ depuis spheres/integration_sphères_problématiques.py
Module majeur (315 lignes) intégrant cycles naturels, visualisation et sphères problématiques.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import math
import random
from datetime import datetime
from enum import Enum

# 🔧 CORRIGÉ: Imports depuis la structure actuelle
from src.core.types_spheres import TypeCycle, TypeSphereProblematique

# TODO: Ces imports devront être ajustés quand les modules correspondants seront migrés
# from .cycles_naturels import GestionnaireCycles
# from .visualisation_cycles import VisualisationCycles, ElementVisualisation

# 🔧 NOTE: TypeSphereProblematique supprimé car défini dans src.core.types_spheres

@dataclass
class SphereProblematique:
    """Représente une sphère problématique confinée."""
    type: TypeSphereProblematique
    niveau_confinement: float  # 0.0 à 1.0
    energie_residuelle: float  # 0.0 à 1.0
    position: Tuple[float, float, float]  # x, y, z
    couleur: str
    description: str
    mots_cles: List[str]
    interactions: List[Dict]
    timestamp_creation: datetime
    timestamp_derniere_interaction: datetime

class GestionnaireSphèresProblematiques:
    """Gère les sphères problématiques et leur intégration avec les cycles."""
    
    def __init__(self, gestionnaire_cycles: GestionnaireCycles):
        self.gestionnaire_cycles = gestionnaire_cycles
        self.visualisation = VisualisationCycles(gestionnaire_cycles)
        self.spheres: Dict[TypeSphereProblematique, SphereProblematique] = {}
        self._initialiser_spheres()
    
    def _initialiser_spheres(self):
        """Initialise les sphères problématiques."""
        descriptions = {
            TypeSphereProblematique.DOUTE: {
                "description": "Une sphère de doute qui vacille entre certitude et incertitude",
                "couleur": "#8a8a8a",
                "mots_cles": ["doute", "questionnement", "incertitude", "recherche"]
            },
            TypeSphereProblematique.EMOTIONS_NEGATIVES: {
                "description": "Une sphère d'émotions négatives qui pulse d'énergie sombre",
                "couleur": "#800000",
                "mots_cles": ["colère", "tristesse", "peur", "angoisse"]
            },
            TypeSphereProblematique.MYSTERES_SOMBRES: {
                "description": "Une sphère de mystères sombres qui attire et repousse",
                "couleur": "#4b0082",
                "mots_cles": ["mystère", "inconnu", "profondeur", "secret"]
            },
            TypeSphereProblematique.APOCALYPSE: {
                "description": "Une sphère apocalyptique qui émane une énergie de fin des temps",
                "couleur": "#ff4500",
                "mots_cles": ["fin", "destruction", "transformation", "renaissance"]
            },
            TypeSphereProblematique.PARADOXE: {
                "description": "Une sphère paradoxale qui défie la logique et la raison",
                "couleur": "#00ffff",
                "mots_cles": ["contradiction", "impossible", "mystère", "énigme"]
            }
        }
        
        # Positions initiales dans les racines de l'arbre
        positions = {
            TypeSphereProblematique.DOUTE: (0.0, -0.8, 0.0),
            TypeSphereProblematique.EMOTIONS_NEGATIVES: (-0.5, -0.9, 0.0),
            TypeSphereProblematique.MYSTERES_SOMBRES: (0.5, -0.9, 0.0),
            TypeSphereProblematique.APOCALYPSE: (0.0, -1.0, 0.5),
            TypeSphereProblematique.PARADOXE: (0.0, -1.0, -0.5)
        }
        
        for type_sphere in TypeSphereProblematique:
            info = descriptions[type_sphere]
            self.spheres[type_sphere] = SphereProblematique(
                type=type_sphere,
                niveau_confinement=0.7,  # Niveau initial de confinement
                energie_residuelle=0.3,  # Énergie résiduelle initiale
                position=positions[type_sphere],
                couleur=info["couleur"],
                description=info["description"],
                mots_cles=info["mots_cles"],
                interactions=[],
                timestamp_creation=datetime.now(),
                timestamp_derniere_interaction=datetime.now()
            )
    
    def confiner_sphere(self, type_sphere: TypeSphereProblematique) -> SphereProblematique:
        """Confine une nouvelle sphère problématique."""
        if type_sphere in self.spheres:
            # Renforcer le confinement existant
            sphere = self.spheres[type_sphere]
            sphere.niveau_confinement = min(1.0, sphere.niveau_confinement + 0.1)
            sphere.timestamp_derniere_interaction = datetime.now()
            
            # Ajouter l'interaction
            sphere.interactions.append({
                "type": "renforcement",
                "intensite": 0.1,
                "timestamp": datetime.now(),
                "description": f"Le confinement de la sphère {type_sphere.value} a été renforcé"
            })
        else:
            # Créer une nouvelle sphère
            descriptions = {
                TypeSphereProblematique.DOUTE: {
                    "description": "Une sphère de doute qui vacille entre certitude et incertitude",
                    "couleur": "#8a8a8a",
                    "mots_cles": ["doute", "questionnement", "incertitude", "recherche"]
                },
                TypeSphereProblematique.EMOTIONS_NEGATIVES: {
                    "description": "Une sphère d'émotions négatives qui pulse d'énergie sombre",
                    "couleur": "#800000",
                    "mots_cles": ["colère", "tristesse", "peur", "angoisse"]
                },
                TypeSphereProblematique.MYSTERES_SOMBRES: {
                    "description": "Une sphère de mystères sombres qui attire et repousse",
                    "couleur": "#4b0082",
                    "mots_cles": ["mystère", "inconnu", "profondeur", "secret"]
                },
                TypeSphereProblematique.APOCALYPSE: {
                    "description": "Une sphère apocalyptique qui émane une énergie de fin des temps",
                    "couleur": "#ff4500",
                    "mots_cles": ["fin", "destruction", "transformation", "renaissance"]
                },
                TypeSphereProblematique.PARADOXE: {
                    "description": "Une sphère paradoxale qui défie la logique et la raison",
                    "couleur": "#00ffff",
                    "mots_cles": ["contradiction", "impossible", "mystère", "énigme"]
                }
            }
            
            info = descriptions[type_sphere]
            position = (random.uniform(-0.5, 0.5), -0.9, random.uniform(-0.5, 0.5))
            
            sphere = SphereProblematique(
                type=type_sphere,
                niveau_confinement=0.7,
                energie_residuelle=0.3,
                position=position,
                couleur=info["couleur"],
                description=info["description"],
                mots_cles=info["mots_cles"],
                interactions=[],
                timestamp_creation=datetime.now(),
                timestamp_derniere_interaction=datetime.now()
            )
            
            sphere.interactions.append({
                "type": "creation",
                "intensite": 1.0,
                "timestamp": datetime.now(),
                "description": f"Une nouvelle sphère {type_sphere.value} a été confinée"
            })
            
            self.spheres[type_sphere] = sphere
        
        return self.spheres[type_sphere]
    
    def enregistrer_interaction(self, type_sphere: TypeSphereProblematique, type_cycle: TypeCycle, intensite: float):
        """Enregistre une interaction entre une sphère problématique et un cycle."""
        if type_sphere not in self.spheres:
            return
        
        sphere = self.spheres[type_sphere]
        cycle = self.gestionnaire_cycles.obtenir_phase_actuelle(type_cycle)
        
        # Calculer l'effet de l'interaction
        effet = self._calculer_effet_interaction(sphere, cycle, intensite)
        
        # Mettre à jour la sphère
        sphere.niveau_confinement = max(0.0, min(1.0, sphere.niveau_confinement + effet))
        sphere.energie_residuelle = max(0.0, min(1.0, sphere.energie_residuelle - effet * 0.5))
        sphere.timestamp_derniere_interaction = datetime.now()
        
        # Générer une description poétique
        description = self._generer_description_interaction(sphere, cycle, intensite, effet)
        
        # Ajouter l'interaction
        sphere.interactions.append({
            "type": "interaction",
            "cycle": type_cycle.value,
            "intensite": intensite,
            "effet": effet,
            "timestamp": datetime.now(),
            "description": description
        })
    
    def _calculer_effet_interaction(
        self, sphere: SphereProblematique, cycle: 'PhaseCycle', intensite: float
    ) -> float:
        """Calcule l'effet d'une interaction entre une sphère et un cycle."""
        # Effet de base
        effet_base = intensite * cycle.intensite
        
        # Ajustement selon le type de sphère et le cycle
        ajustements = {
            TypeSphereProblematique.DOUTE: {
                TypeCycle.LUNAIRE: 1.2,  # La lune influence le doute
                TypeCycle.SAISONNIER: 0.8,
                TypeCycle.QUOTIDIEN: 1.0,
                TypeCycle.METEOROLOGIQUE: 0.9
            },
            TypeSphereProblematique.EMOTIONS_NEGATIVES: {
                TypeCycle.LUNAIRE: 1.1,
                TypeCycle.SAISONNIER: 1.3,  # Les saisons influencent les émotions
                TypeCycle.QUOTIDIEN: 1.2,
                TypeCycle.METEOROLOGIQUE: 1.4  # Le temps qu'il fait influence les émotions
            },
            TypeSphereProblematique.MYSTERES_SOMBRES: {
                TypeCycle.LUNAIRE: 1.4,  # La lune influence les mystères
                TypeCycle.SAISONNIER: 1.0,
                TypeCycle.QUOTIDIEN: 1.3,  # Le jour/nuit influence les mystères
                TypeCycle.METEOROLOGIQUE: 1.1
            },
            TypeSphereProblematique.APOCALYPSE: {
                TypeCycle.LUNAIRE: 1.0,
                TypeCycle.SAISONNIER: 1.2,
                TypeCycle.QUOTIDIEN: 1.1,
                TypeCycle.METEOROLOGIQUE: 1.5  # Le temps qu'il fait influence l'apocalypse
            },
            TypeSphereProblematique.PARADOXE: {
                TypeCycle.LUNAIRE: 1.3,
                TypeCycle.SAISONNIER: 1.1,
                TypeCycle.QUOTIDIEN: 1.2,
                TypeCycle.METEOROLOGIQUE: 0.9
            }
        }
        
        ajustement = ajustements[sphere.type][cycle.type]
        
        # Calcul de l'effet final
        effet = effet_base * ajustement
        
        # Limiter l'effet
        return max(-0.2, min(0.2, effet))
    
    def _generer_description_interaction(
        self, sphere: SphereProblematique, cycle: 'PhaseCycle', intensite: float, effet: float
    ) -> str:
        """Génère une description poétique de l'interaction."""
        if effet > 0:
            return f"La {sphere.type.value} réagit à l'influence du cycle {cycle.type.value}, renforçant son confinement"
        elif effet < 0:
            return f"La {sphere.type.value} résiste à l'influence du cycle {cycle.type.value}, affaiblissant son confinement"
        else:
            return f"La {sphere.type.value} reste stable face à l'influence du cycle {cycle.type.value}"
    
    def calculer_stabilite(self, type_sphere: TypeSphereProblematique) -> float:
        """Calcule la stabilité d'une sphère problématique."""
        if type_sphere not in self.spheres:
            return 0.0
        
        sphere = self.spheres[type_sphere]
        
        # Facteurs de stabilité
        facteur_confinement = sphere.niveau_confinement
        facteur_energie = 1.0 - sphere.energie_residuelle
        facteur_temps = min(1.0, (datetime.now() - sphere.timestamp_derniere_interaction).total_seconds() / 86400)
        
        # Calcul de la stabilité
        stabilite = (facteur_confinement * 0.6 + facteur_energie * 0.3 + facteur_temps * 0.1)
        
        return max(0.0, min(1.0, stabilite))
    
    def obtenir_etat_spheres(self) -> Dict:
        """Récupère l'état actuel des sphères problématiques."""
        return {
            str(type_sphere): {
                "niveau_confinement": sphere.niveau_confinement,
                "energie_residuelle": sphere.energie_residuelle,
                "position": sphere.position,
                "couleur": sphere.couleur,
                "description": sphere.description,
                "mots_cles": sphere.mots_cles,
                "stabilite": self.calculer_stabilite(type_sphere),
                "derniere_interaction": sphere.timestamp_derniere_interaction.isoformat(),
                "nombre_interactions": len(sphere.interactions)
            }
            for type_sphere, sphere in self.spheres.items()
        }
    
    def generer_rapport_poetique(self) -> str:
        """Génère un rapport poétique sur l'état des sphères problématiques."""
        rapport = "Dans les racines de l'arbre, les sphères problématiques reposent.\n\n"
        
        for type_sphere, sphere in self.spheres.items():
            stabilite = self.calculer_stabilite(type_sphere)
            
            if stabilite > 0.8:
                etat = "profondément endormie"
            elif stabilite > 0.5:
                etat = "calmement confinée"
            elif stabilite > 0.3:
                etat = "légèrement agitée"
            else:
                etat = "agitées et instables"
            
            rapport += f"La sphère de {type_sphere.value} est {etat}, {sphere.description.lower()}\n"
        
        rapport += "\nLes cycles naturels dansent autour d'elles, influençant leur état."
        
        return rapport 