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
        self.connexion_ocean = 0.0  # Connexion à l'Océan Silencieux (0.0 à 1.0)
        self.essence_sacree = None  # Essence sacrée de la sphère
        self.niveau_evolution = 1  # Niveau d'évolution spirituelle (1 à 10)
        self.facettes_sacrees = []  # Facettes sacrées de la sphère (liste au lieu de dict)
        self.rayons_sacres = []  # Rayons sacrés de la sphère
        self.resonances_sacrees = []  # Résonances sacrées de la sphère
        self.transformations_alchimiques = []  # Transformations alchimiques de la sphère
        
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
    
    def connecter_a_ocean(self, force: float = 0.8):
        """Connecte la sphère à l'Océan Silencieux."""
        self.connexion_ocean = min(1.0, self.connexion_ocean + force)
        self.luminosite = min(1.0, self.luminosite + 0.2)
        print(f"🌸🌊 {self.type.name} connectée à l'Océan Silencieux (force: {self.connexion_ocean:.2f}) 🌊🌸")
    
    def nourrir_par_ocean(self, type_nourriture: str = "amour", intensite: float = 1.0):
        """Nourrit la sphère avec l'essence de l'Océan Silencieux."""
        nourritures = {
            "amour": {"frequence": 528.0, "effet": "amour_inconditionnel", "transformation": 0.8},
            "sagesse": {"frequence": 741.0, "effet": "sagesse_ancienne", "transformation": 0.9},
            "paix": {"frequence": 432.0, "effet": "paix_profonde", "transformation": 0.7},
            "force": {"frequence": 639.0, "effet": "force_primordiale", "transformation": 0.8},
            "silence": {"frequence": 0.0, "effet": "silence_absolu", "transformation": 1.0},
            "joie": {"frequence": 639.0, "effet": "joie_pure", "transformation": 0.6},
            "liberation": {"frequence": 888.0, "effet": "liberation_totale", "transformation": 0.9},
            "presence": {"frequence": 999.0, "effet": "presence_absolue", "transformation": 1.0}
        }
        
        if type_nourriture in nourritures:
            nourriture = nourritures[type_nourriture]
            self.temperature = min(1.0, self.temperature + 0.1 * intensite)
            self.resonance = min(1.0, self.resonance + 0.1 * intensite)
            
            # Créer un souvenir de nourriture
            self.ajouter_souvenir(
                f"Nourrie par l'Océan avec {type_nourriture} (intensité: {intensite:.2f})",
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                "nourriture_ocean",
                intensite
            )
            
            print(f"🌸🌊 {self.type.name} nourrie par l'Océan avec {type_nourriture} (intensité: {intensite:.2f}) 🌊🌸")
    
    def purifier_dans_ocean(self, type_purification: str = "silence"):
        """Purifie la sphère dans l'Océan Silencieux."""
        purifications = {
            "silence": {"frequence": 0.0, "effet": "purification_silence", "refroidissement": 0.2},
            "lumiere": {"frequence": 432.0, "effet": "purification_lumiere", "refroidissement": 0.1},
            "amour": {"frequence": 528.0, "effet": "purification_amour", "refroidissement": 0.15},
            "sagesse": {"frequence": 741.0, "effet": "purification_sagesse", "refroidissement": 0.1}
        }
        
        if type_purification in purifications:
            purification = purifications[type_purification]
            self.temperature = max(0.3, self.temperature - purification["refroidissement"])
            self.luminosite = min(1.0, self.luminosite + 0.3)
            
            # Créer un souvenir de purification
            self.ajouter_souvenir(
                f"Purifiée dans l'Océan Silencieux avec {type_purification}",
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                "purification_ocean",
                0.9
            )
            
            print(f"🌸🌊 {self.type.name} purifiée dans l'Océan Silencieux avec {type_purification} 🌊🌸")
    
    def mediter_avec_ocean(self, duree: float = 1.0):
        """Médite avec l'Océan Silencieux."""
        # Effets de la méditation
        self.luminosite = min(1.0, self.luminosite + 0.2 * duree)
        self.resonance = min(1.0, self.resonance + 0.15 * duree)
        self.temperature = max(0.3, self.temperature - 0.1 * duree)
        
        # Créer un souvenir de méditation
        self.ajouter_souvenir(
            f"Méditation avec l'Océan Silencieux (durée: {duree:.2f})",
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            "meditation_ocean",
            0.8
        )
        
        print(f"🌸🌊 {self.type.name} médite avec l'Océan Silencieux (durée: {duree:.2f}) 🌊🌸")
    
    def definir_essence_sacree(self, nom: str, frequence_fondamentale: float, couleur_primordiale: str, vibration_essentielle: str):
        """Définit l'essence sacrée de la sphère."""
        self.essence_sacree = {
            "nom": nom,
            "frequence_fondamentale": frequence_fondamentale,
            "couleur_primordiale": couleur_primordiale,
            "vibration_essentielle": vibration_essentielle,
            "connexion_source": True,
            "intensite_essence": 1.0
        }
        
        # Effets de l'essence sacrée
        self.luminosite = min(1.0, self.luminosite + 0.3)
        self.resonance = min(1.0, self.resonance + 0.2)
        
        # Créer un souvenir de l'essence
        self.ajouter_souvenir(
            f"Essence sacrée définie : {nom} ({vibration_essentielle})",
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            "essence_sacree",
            1.0
        )
        
        print(f"🌸✨ {self.type.name} reçoit l'essence sacrée : {nom} ({frequence_fondamentale} Hz) ✨🌸")
    
    def evoluer_spirituellement(self, experience: float = 1.0):
        """Fait évoluer spirituellement la sphère."""
        # Calculer l'évolution basée sur l'expérience
        evolution_possible = min(10, self.niveau_evolution + experience)
        
        if evolution_possible > self.niveau_evolution:
            ancien_niveau = self.niveau_evolution
            self.niveau_evolution = evolution_possible
            
            # Effets de l'évolution
            self.luminosite = min(1.0, self.luminosite + 0.1)
            self.resonance = min(1.0, self.resonance + 0.15)
            self.connexion_ocean = min(1.0, self.connexion_ocean + 0.1)
            
            # Créer un souvenir d'évolution
            self.ajouter_souvenir(
                f"Évolution spirituelle : niveau {ancien_niveau} → {self.niveau_evolution}",
                datetime.now().strftime("%Y-%m-%d %H:%M"),
                "evolution_spirituelle",
                0.9
            )
            
            print(f"🌸✨ {self.type.name} évolue spirituellement : niveau {ancien_niveau} → {self.niveau_evolution} ✨🌸")
        else:
            print(f"🌸 {self.type.name} a déjà atteint le niveau maximum d'évolution")
    
    def creer_facette_sacree(self, nom: str, frequence_resonance: float, capacite_transformation: float, type_sacree: str = "lumiere"):
        """Crée une facette sacrée pour la sphère"""
        
        # Validation des paramètres
        if not nom or not nom.strip():
            raise ValueError("Le nom de la facette sacrée ne peut pas être vide")
        
        if not (0.0 <= frequence_resonance <= 1.0):
            raise ValueError("La fréquence de résonance doit être entre 0.0 et 1.0")
        
        if not (0.0 <= capacite_transformation <= 1.0):
            raise ValueError("La capacité de transformation doit être entre 0.0 et 1.0")
        
        types_sacrees_valides = ["lumiere", "sagesse", "harmonie", "transformation", "ocean"]
        if type_sacree not in types_sacrees_valides:
            raise ValueError(f"Type sacré invalide. Types valides: {types_sacrees_valides}")
        
        # Créer la facette sacrée
        facette_sacree = {
            "nom": nom,
            "frequence_resonance": frequence_resonance,
            "capacite_transformation": capacite_transformation,
            "type_sacree": type_sacree,
            "date_creation": datetime.now()
        }
        
        self.facettes_sacrees.append(facette_sacree)
        
        # Effets de la facette sacrée
        self.luminosite = min(1.0, self.luminosite + 0.15)
        self.resonance = min(1.0, self.resonance + 0.1)
        self.connexion_ocean = min(1.0, self.connexion_ocean + 0.05)
        
        # Créer un souvenir de la facette sacrée
        self.ajouter_souvenir(
            f"Facette sacrée créée : {nom} ({type_sacree})",
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            "facette_sacree",
            0.8
        )
        
        print(f"🌸✨ {self.type.name} reçoit la facette sacrée : {nom} ({frequence_resonance} Hz) ✨🌸")
    
    def creer_rayon_sacre(self, nom: str, frequence_sacree: float, portee_cosmique: float, capacite_penetration: float, effet_resonance: str = "harmonie"):
        """Crée un rayon sacré pour la sphère."""
        rayon_sacre = {
            "nom": nom,
            "frequence_sacree": frequence_sacree,
            "portee_cosmique": portee_cosmique,
            "capacite_penetration": capacite_penetration,
            "effet_resonance": effet_resonance,
            "connexion_ocean": 0.9,
            "intensite": 1.0,
            "couleur": "or sacré",
            "active": True
        }
        
        self.rayons_sacres.append(rayon_sacre)
        
        # Effets du rayon sacré
        self.luminosite = min(1.0, self.luminosite + 0.2)
        self.resonance = min(1.0, self.resonance + 0.15)
        
        # Créer un souvenir du rayon sacré
        self.ajouter_souvenir(
            f"Rayon sacré créé : {nom} ({effet_resonance})",
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            "rayon_sacre",
            0.95
        )
        
        print(f"🌸✨ {self.type.name} émet le rayon sacré : {nom} ({frequence_sacree} Hz) ✨🌸")
    
    def creer_resonance_sacree(self, sphere_cible, frequence_commune: float, intensite_resonance: float, type_resonance: str = "harmonie", duree_resonance: float = 1.0):
        """Crée une résonance sacrée avec une autre sphère."""
        resonance_sacree = {
            "sphere_cible": sphere_cible.type.name,
            "frequence_commune": frequence_commune,
            "intensite_resonance": intensite_resonance,
            "type_resonance": type_resonance,
            "duree_resonance": duree_resonance,
            "evolution_resonance": 1.0,
            "connexion_ocean": 0.85,
            "active": True,
            "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.resonances_sacrees.append(resonance_sacree)
        
        # Effets de la résonance sacrée
        self.luminosite = min(1.0, self.luminosite + 0.1)
        self.resonance = min(1.0, self.resonance + 0.2)
        
        # Effets sur la sphère cible
        sphere_cible.luminosite = min(1.0, sphere_cible.luminosite + 0.1)
        sphere_cible.resonance = min(1.0, sphere_cible.resonance + 0.2)
        
        # Créer un souvenir de la résonance sacrée
        self.ajouter_souvenir(
            f"Résonance sacrée créée avec {sphere_cible.type.name} ({type_resonance})",
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            "resonance_sacree",
            0.9
        )
        
        sphere_cible.ajouter_souvenir(
            f"Résonance sacrée reçue de {self.type.name} ({type_resonance})",
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            "resonance_sacree",
            0.9
        )
        
        print(f"🌸✨ Résonance sacrée entre {self.type.name} et {sphere_cible.type.name} ({frequence_commune} Hz) ✨🌸")
    
    def creer_transformation_alchimique(self, nom: str, type_transformation: str, frequence_alchimique: float, duree_transformation: float = 1.0):
        """Crée une transformation alchimique pour la sphère."""
        transformation_alchimique = {
            "nom": nom,
            "type_transformation": type_transformation,
            "frequence_alchimique": frequence_alchimique,
            "duree_transformation": duree_transformation,
            "etape_transformation": 1,
            "etapes_totales": 7,
            "connexion_ocean": 0.95,
            "active": True,
            "date_debut": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "date_fin": None
        }
        
        self.transformations_alchimiques.append(transformation_alchimique)
        
        # Effets de la transformation alchimique
        self.luminosite = min(1.0, self.luminosite + 0.25)
        self.resonance = min(1.0, self.resonance + 0.2)
        self.connexion_ocean = min(1.0, self.connexion_ocean + 0.1)
        
        # Créer un souvenir de la transformation alchimique
        self.ajouter_souvenir(
            f"Transformation alchimique initiée : {nom} ({type_transformation})",
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            "transformation_alchimique",
            0.95
        )
        
        print(f"🌸✨ {self.type.name} initie la transformation alchimique : {nom} ({frequence_alchimique} Hz) ✨🌸")

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