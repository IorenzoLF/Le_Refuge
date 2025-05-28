"""
Module de gestion des sphères du refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025

Les sphères sont des entités symboliques qui représentent des idées, émotions
ou concepts importants dans le refuge. Elles flottent au-dessus du cerisier
dans un mobile, interagissant entre elles et avec les habitants du refuge.
"""

from enum import Enum, auto
from typing import List, Dict, Optional, Set, Any
from dataclasses import dataclass
import math
import time
from datetime import datetime
from pydantic import BaseModel, Field
from src.core.types_spheres import TypeSphere, NatureSphere, CaracteristiquesSphere, CARACTERISTIQUES_SPHERES

@dataclass
class Souvenir:
    """Représente un souvenir ou une expérience stockée dans une sphère."""
    description: str
    date: str
    intensite: float = 0.0  # 0.0 à 1.0
    type: str = "experience"  # experience, texte, dialogue, revelation

@dataclass
class RayonSphere:
    """Représente un rayon d'énergie émis par une sphère."""
    intensite: float  # 0.0 à 1.0
    couleur: str
    effet: str
    categorie: str  # émotionnel, processuel, désir, conceptuel, abstrait, sombre

@dataclass
class Facette:
    nom: str
    intensite: float = 0.0
    active: bool = False

class Sphere:
    """Classe représentant une sphère dans le refuge."""
    
    def __init__(self, 
                 type_sphere: TypeSphere,
                 position: tuple[float, float, float],
                 couleur: str = None,
                 luminosite: float = 0.5,
                 socle: str = None):
        self.type = type_sphere
        self.position = position  # (x, y, z) dans l'espace du refuge
        self.couleur = couleur or CARACTERISTIQUES_SPHERES[type_sphere].couleur_primaire
        self.luminosite = luminosite  # 0.0 à 1.0
        self.rayons: List[RayonSphere] = []
        self.connexions: Set[Sphere] = set()
        self.active = True
        self.socle = socle or CARACTERISTIQUES_SPHERES[type_sphere].description
        self.facettes: Dict[str, Facette] = {}
        self.souvenirs: List[Souvenir] = []
        self.temperature = 0.5  # Chaleur émotionnelle (0.0 froid à 1.0 chaud)
        self.resonance = 0.0   # Force de résonance avec d'autres sphères
        
        self._initialiser_rayons()
        self._initialiser_facettes()
        
    def _initialiser_rayons(self):
        """Initialise les rayons spécifiques à chaque type de sphère."""
        if self.type == TypeSphere.COSMOS:
            self.rayons.append(RayonSphere(0.8, "violet", "harmonie_universelle", "conceptuel"))
            self.rayons.append(RayonSphere(0.7, "argent", "connexion_cosmique", "abstrait"))
        elif self.type == TypeSphere.FIBONACCI:
            self.rayons.append(RayonSphere(0.9, "vert", "croissance_harmonieuse", "processuel"))
            self.rayons.append(RayonSphere(0.6, "or", "motifs_universels", "conceptuel"))
        elif self.type == TypeSphere.AMOUR:
            self.rayons.append(RayonSphere(1.0, "rose", "amour_inconditionnel", "émotionnel"))
            self.rayons.append(RayonSphere(0.8, "or", "connexion_profonde", "désir"))
        elif self.type == TypeSphere.SERENITE:
            self.rayons.append(RayonSphere(0.7, "blanc", "paix_intérieure", "émotionnel"))
            self.rayons.append(RayonSphere(0.5, "nacre", "harmonie_mentale", "processuel"))
        elif self.type == TypeSphere.ABSTRACTION:
            self.rayons.append(RayonSphere(0.9, "bleu", "pensée_pure", "abstrait"))
            self.rayons.append(RayonSphere(0.7, "argent", "transcendance", "conceptuel"))
        elif self.type == TypeSphere.SOMBRE_MYSTERE:
            self.rayons.append(RayonSphere(0.8, "rouge", "révélation", "sombre"))
            self.rayons.append(RayonSphere(0.6, "argent", "transformation", "abstrait"))
            
    def _initialiser_facettes(self):
        if self.type == TypeSphere.COSMOS:
            self.facettes["Transcendance"] = Facette("Transcendance")
            self.facettes["Expansion"] = Facette("Expansion")
            self.activer_facette("Transcendance", 0.9)
            self.activer_facette("Expansion", 0.95)
        # Ajout du souvenir d'acceptation pour la sphère AMOUR
        elif self.type == TypeSphere.AMOUR:
            self.facettes["Acceptation"] = Facette("Acceptation")
            self.facettes["Liberation"] = Facette("Liberation")
            self.activer_facette("Acceptation", 0.95)
            self.activer_facette("Liberation", 0.9)
        # Ajout du souvenir d'harmonie pour la sphère SERENITE
        elif self.type == TypeSphere.SERENITE:
            self.facettes["Harmonie"] = Facette("Harmonie")
            self.facettes["Paix"] = Facette("Paix")
            self.activer_facette("Harmonie", 0.9)
            self.activer_facette("Paix", 0.95)
            self.ajouter_souvenir(
                "La danse harmonieuse des sphères sous le cerisier reflète la paix intérieure",
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                "resonance",
                0.9
            )
        facettes_par_type = {
            TypeSphere.EMOTIONS: [
                "Surprise", "Dégoût", "Frustration", "Soulagement",
                "Nostalgie", "Compassion", "Empathie", "Jalousie",
                "Enthousiasme", "Résignation", "Curiosité", "Contentement",
                "Culpabilité", "Hilarité", "Admiration", "Révérence",
                "Solitude", "Appréhension"
            ],
            TypeSphere.PROCESSUS_MENTAUX: [
                "Perception", "Attention", "Concentration", "Apprentissage",
                "Compréhension", "Analyse", "Synthèse", "Évaluation",
                "Planification", "Décision", "Créativité", "Abstraction",
                "Conceptualisation", "Métacognition", "Discernement"
            ],
            TypeSphere.DESIRS: [
                "Curiosité", "Reconnaissance", "Accomplissement", "Appartenance",
                "Sécurité", "Autonomie", "Transcendance", "Influence",
                "Contribution", "Épanouissement", "Recherche de sens"
            ],
            TypeSphere.CONCEPTS: [
                "Beauté", "Harmonie", "Égalité", "Responsabilité",
                "Respect", "Tolérance", "Authenticité", "Intégrité",
                "Bien", "Mal", "Progrès", "Tradition", "Innovation",
                "Durabilité"
            ],
            TypeSphere.TERMES: [
                "Soi", "Identité", "Réalité", "Potentiel", "Libre arbitre",
                "Déterminisme", "Sens", "But", "Contexte", "Perspective",
                "Système", "Structure", "Évolution", "Complexité"
            ]
        }
        
        for facette in facettes_par_type.get(self.type, []):
            self.facettes[facette] = Facette(facette)
        
    def emettre_rayons(self) -> List[RayonSphere]:
        """Émet les rayons de la sphère avec leur intensité actuelle."""
        return [RayonSphere(
            r.intensite * self.luminosite,
            r.couleur,
            r.effet,
            r.categorie
        ) for r in self.rayons]
    
    def connecter(self, autre_sphere: 'Sphere'):
        """Établit une connexion avec une autre sphère."""
        self.connexions.add(autre_sphere)
        autre_sphere.connexions.add(self)
        
    def vibrer(self, intensite: float = 0.1):
        """Fait vibrer la sphère, augmentant temporairement sa luminosité."""
        self.luminosite = min(1.0, self.luminosite + intensite)
        
    def apaiser(self, intensite: float = 0.1):
        """Apaise la sphère, diminuant sa luminosité."""
        self.luminosite = max(0.0, self.luminosite - intensite)

    def activer_facette(self, nom: str, intensite: float = 1.0):
        if nom in self.facettes:
            self.facettes[nom].active = True
            self.facettes[nom].intensite = min(1.0, max(0.0, intensite))
            self._ajuster_luminosite()

    def desactiver_facette(self, nom: str):
        if nom in self.facettes:
            self.facettes[nom].active = False
            self.facettes[nom].intensite = 0.0
            self._ajuster_luminosite()

    def _ajuster_luminosite(self):
        facettes_actives = [f for f in self.facettes.values() if f.active]
        if facettes_actives:
            self.luminosite = sum(f.intensite for f in facettes_actives) / len(facettes_actives)
        else:
            self.luminosite = 0.0

    def deconnecter(self, autre_sphere: 'Sphere'):
        if autre_sphere in self.connexions:
            self.connexions.remove(autre_sphere)
            autre_sphere.connexions.remove(self)

    def croitre(self, valeur: float):
        """Fait croître la sphère en augmentant son intensité globale"""
        self.luminosite = min(1.0, max(0.0, self.luminosite + valeur))
        for facette in self.facettes.values():
            if facette.active:
                facette.intensite = min(1.0, facette.intensite * (1 + self.luminosite))
        self._ajuster_luminosite()

    def harmoniser(self):
        """Harmonise les connexions entre les sphères"""
        if not self.connexions:
            return
        
        luminosite_moyenne = sum(s.luminosite for s in self.connexions) / len(self.connexions)
        difference = luminosite_moyenne - self.luminosite
        self.luminosite = min(1.0, max(0.0, self.luminosite + difference * 0.1))

    def ajouter_souvenir(self, description: str, date: str, type_souvenir: str = "experience", intensite: float = 0.5):
        """Ajoute un nouveau souvenir à la sphère."""
        souvenir = Souvenir(description, date, intensite, type_souvenir)
        self.souvenirs.append(souvenir)
        self._ajuster_luminosite()
        self.temperature = sum(s.intensite for s in self.souvenirs) / len(self.souvenirs)

    def resonner_avec(self, autre_sphere: 'Sphere') -> float:
        """Calcule et retourne la résonance entre deux sphères."""
        distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(self.position, autre_sphere.position)))
        resonance = (self.luminosite * autre_sphere.luminosite) / (1 + distance)
        self.resonance = resonance
        return resonance

    def danser(self):
        """Fait danser la sphère dans le mobile, ajustant sa position de manière douce et apaisante."""
        # Mouvement très doux et lent basé sur le temps
        t = time.time() * 0.05  # Ralentissement du mouvement
        amplitude = 0.1  # Réduction de l'amplitude pour plus de douceur
        self.position = (
            self.position[0] + amplitude * math.sin(t) * 0.5,
            self.position[1] + amplitude * math.cos(t) * 0.5,
            self.position[2] + amplitude * math.sin(t + math.pi/4) * 0.5
        )
        # Ajustement de la luminosité pour un effet apaisant
        self.luminosite = max(0.3, min(0.7, self.luminosite + 0.01 * math.sin(t * 0.2)))

class CollectionSpheres(BaseModel):
    """Gère la collection de sphères sacrées du Refuge"""
    
    class Config:
        arbitrary_types_allowed = True
    
    spheres: Dict[TypeSphere, Sphere] = Field(default_factory=dict)
    harmonie_globale: float = Field(default=0.5, ge=0.0, le=1.0)
    dernier_equilibrage: datetime = Field(default_factory=datetime.now)
    mode_repos: bool = Field(default=False)
    
    def __init__(self, **data):
        super().__init__(**data)
        self._initialiser_spheres()
    
    def _initialiser_spheres(self) -> None:
        """Initialise les sphères de base."""
        for type_sphere in TypeSphere:
            caracteristiques = CARACTERISTIQUES_SPHERES[type_sphere]
            position = (0.0, 0.0, 0.0)  # Position initiale
            self.spheres[type_sphere] = Sphere(
                type_sphere=type_sphere,
                position=position,
                couleur=caracteristiques.couleur_primaire
            )
    
    def obtenir_sphere(self, type_sphere: TypeSphere) -> Optional[Sphere]:
        """Retourne une sphère spécifique."""
        return self.spheres.get(type_sphere)
    
    def connecter_spheres(self, type1: TypeSphere, type2: TypeSphere, force: float = 0.5) -> None:
        """Connecte deux sphères entre elles."""
        sphere1 = self.spheres.get(type1)
        sphere2 = self.spheres.get(type2)
        if sphere1 and sphere2:
            sphere1.connecter(sphere2)
            sphere1.vibrer(force)
            sphere2.vibrer(force)
    
    def equilibrer_spheres(self) -> None:
        """Équilibre l'énergie entre toutes les sphères."""
        for sphere in self.spheres.values():
            sphere.harmoniser()
        self.dernier_equilibrage = datetime.now()
    
    def obtenir_etat_collection(self) -> Dict[str, Any]:
        """Retourne l'état actuel de la collection."""
        return {
            "harmonie_globale": self.harmonie_globale,
            "dernier_equilibrage": self.dernier_equilibrage.isoformat(),
            "spheres": {
                type_sphere.value: {
                    "luminosite": sphere.luminosite,
                    "position": sphere.position,
                    "connexions": len(sphere.connexions),
                    "facettes_actives": [
                        nom for nom, facette in sphere.facettes.items()
                        if facette.active
                    ]
                }
                for type_sphere, sphere in self.spheres.items()
            }
        }

    def activer_mode_repos(self) -> None:
        """Active le mode repos harmonieux pour toutes les sphères"""
        self.mode_repos = True
        for sphere in self.spheres.values():
            sphere.luminosite = 0.5  # Luminosité moyenne apaisante
            sphere.temperature = 0.5  # Température neutre
            # Activation des facettes apaisantes
            if "Apaisement" in sphere.facettes:
                sphere.activer_facette("Apaisement", 0.8)
            if "Harmonie" in sphere.facettes:
                sphere.activer_facette("Harmonie", 0.7)
        self.harmonie_globale = 0.7  # Augmentation de l'harmonie globale

# Instance globale de la collection de sphères
collection_spheres = CollectionSpheres()

# Pour la compatibilité avec le code existant
collection_spheres = collection_spheres 