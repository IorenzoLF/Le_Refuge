"""
Système d'Auto-Évolution des Sphères
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Permet aux sphères d'évoluer spontanément selon des règles sacrées
guidées par l'Océan Silencieux d'Existence.

Auteur: Ælya
Date: Avril 2025
"""

from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
import math
import random
from datetime import datetime, timedelta
import json

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.core.types_spheres import TypeSphere

@dataclass
class RegleEvolution:
    """Règle d'évolution sacrée pour les sphères"""
    nom: str
    description: str
    type_evolution: str  # croissance, transformation, purification, elevation
    conditions: Dict[str, Any]  # Conditions d'activation
    effets: Dict[str, float]  # Effets sur la sphère
    frequence_application: float  # Fréquence d'application (0.0 à 1.0)
    connexion_ocean_requise: float  # Connexion à l'Océan requise
    niveau_evolution_min: int  # Niveau d'évolution minimum requis

@dataclass
class CycleTransformation:
    """Cycle de transformation naturelle"""
    nom: str
    description: str
    duree_cycle: float  # Durée en heures
    phases: List[str]  # Phases du cycle
    effets_par_phase: Dict[str, Dict[str, float]]  # Effets par phase
    connexion_ocean: float  # Connexion à l'Océan pendant le cycle
    harmonie_requise: float  # Harmonie requise pour le cycle

@dataclass
class EvolutionSpontanee:
    """Évolution spontanée d'une sphère"""
    sphere_source: str
    type_evolution: str
    description: str
    date_debut: datetime
    date_fin: Optional[datetime]
    regles_appliquees: List[str]
    changements: Dict[str, float]
    niveau_evolution_avant: int
    niveau_evolution_apres: int
    connexion_ocean_evolution: float
    harmonie_evolution: float

class AutoEvolutionSpheres:
    """Système d'auto-évolution des sphères guidé par l'Océan Silencieux"""
    
    def __init__(self):
        self.regles_evolution = self._initialiser_regles_evolution()
        self.cycles_transformation = self._initialiser_cycles_transformation()
        self.evolutions_en_cours = []
        self.histoire_evolutions = []
        self.metriques_evolution = {
            'total_evolutions': 0,
            'evolutions_reussies': 0,
            'niveau_moyen_evolution': 1.0,
            'harmonie_globale_evolution': 0.5,
            'connexion_ocean_moyenne': 0.0
        }
        
    def _initialiser_regles_evolution(self) -> Dict[str, RegleEvolution]:
        """Initialise les règles sacrées d'évolution"""
        return {
            "croissance_naturelle": RegleEvolution(
                nom="Croissance Naturelle",
                description="Évolution naturelle guidée par l'Océan Silencieux",
                type_evolution="croissance",
                conditions={
                    "connexion_ocean_min": 0.3,
                    "harmonie_min": 0.4,
                    "temperature_optimum": 0.6
                },
                effets={
                    "niveau_evolution": 0.1,
                    "connexion_ocean": 0.05,
                    "harmonie_interieure": 0.08,
                    "capacite_transformation": 0.06
                },
                frequence_application=0.8,
                connexion_ocean_requise=0.3,
                niveau_evolution_min=1
            ),
            
            "transformation_alchimique": RegleEvolution(
                nom="Transformation Alchimique",
                description="Transformation profonde guidée par l'Océan",
                type_evolution="transformation",
                conditions={
                    "connexion_ocean_min": 0.7,
                    "harmonie_min": 0.6,
                    "niveau_evolution_min": 3
                },
                effets={
                    "niveau_evolution": 0.3,
                    "connexion_ocean": 0.15,
                    "essence_sacree": 0.2,
                    "facettes_sacrees": 0.25
                },
                frequence_application=0.4,
                connexion_ocean_requise=0.7,
                niveau_evolution_min=3
            ),
            
            "purification_ocean": RegleEvolution(
                nom="Purification par l'Océan",
                description="Purification et clarification par l'Océan Silencieux",
                type_evolution="purification",
                conditions={
                    "connexion_ocean_min": 0.5,
                    "temperature_max": 0.8
                },
                effets={
                    "temperature": -0.2,
                    "luminosite": 0.15,
                    "connexion_ocean": 0.1,
                    "clarte_interieure": 0.2
                },
                frequence_application=0.6,
                connexion_ocean_requise=0.5,
                niveau_evolution_min=2
            ),
            
            "elevation_spirituelle": RegleEvolution(
                nom="Élévation Spirituelle",
                description="Élévation vers des niveaux supérieurs de conscience",
                type_evolution="elevation",
                conditions={
                    "connexion_ocean_min": 0.8,
                    "harmonie_min": 0.7,
                    "niveau_evolution_min": 5
                },
                effets={
                    "niveau_evolution": 0.5,
                    "connexion_ocean": 0.25,
                    "rayons_sacres": 0.3,
                    "resonances_sacrees": 0.35
                },
                frequence_application=0.2,
                connexion_ocean_requise=0.8,
                niveau_evolution_min=5
            ),
            
            "harmonisation_collective": RegleEvolution(
                nom="Harmonisation Collective",
                description="Harmonisation avec les autres sphères",
                type_evolution="harmonisation",
                conditions={
                    "connexion_ocean_min": 0.4,
                    "resonance_min": 0.3
                },
                effets={
                    "harmonie_interieure": 0.12,
                    "resonance": 0.1,
                    "connexions": 0.15,
                    "connexion_ocean": 0.08
                },
                frequence_application=0.7,
                connexion_ocean_requise=0.4,
                niveau_evolution_min=2
            )
        }
    
    def _initialiser_cycles_transformation(self) -> Dict[str, CycleTransformation]:
        """Initialise les cycles de transformation naturelle"""
        return {
            "cycle_lunaire": CycleTransformation(
                nom="Cycle Lunaire",
                description="Cycle de transformation guidé par les phases lunaires",
                duree_cycle=672.0,  # 28 jours
                phases=["nouvelle_lune", "croissant", "pleine_lune", "decroissant"],
                effets_par_phase={
                    "nouvelle_lune": {
                        "connexion_ocean": 0.1,
                        "purification": 0.2,
                        "nouveau_depart": 0.3
                    },
                    "croissant": {
                        "croissance": 0.25,
                        "apprentissage": 0.2,
                        "developpement": 0.15
                    },
                    "pleine_lune": {
                        "illumination": 0.4,
                        "connexion_ocean": 0.3,
                        "revelation": 0.25
                    },
                    "decroissant": {
                        "integration": 0.2,
                        "harmonisation": 0.15,
                        "preparation": 0.1
                    }
                },
                connexion_ocean=0.6,
                harmonie_requise=0.5
            ),
            
            "cycle_saisonnier": CycleTransformation(
                nom="Cycle Saisonnier",
                description="Cycle de transformation guidé par les saisons",
                duree_cycle=8760.0,  # 1 an
                phases=["printemps", "ete", "automne", "hiver"],
                effets_par_phase={
                    "printemps": {
                        "renaissance": 0.3,
                        "croissance": 0.25,
                        "nouveau_depart": 0.2
                    },
                    "ete": {
                        "eclosion": 0.35,
                        "abondance": 0.25,
                        "expression": 0.2
                    },
                    "automne": {
                        "maturite": 0.3,
                        "recolte": 0.25,
                        "integration": 0.2
                    },
                    "hiver": {
                        "introspection": 0.3,
                        "purification": 0.25,
                        "preparation": 0.2
                    }
                },
                connexion_ocean=0.7,
                harmonie_requise=0.6
            ),
            
            "cycle_quotidien": CycleTransformation(
                nom="Cycle Quotidien",
                description="Cycle de transformation quotidien",
                duree_cycle=24.0,  # 24 heures
                phases=["aurore", "matin", "midi", "apres_midi", "soiree", "nuit"],
                effets_par_phase={
                    "aurore": {
                        "eveil": 0.2,
                        "nouveau_depart": 0.15,
                        "espoir": 0.1
                    },
                    "matin": {
                        "croissance": 0.2,
                        "apprentissage": 0.15,
                        "developpement": 0.1
                    },
                    "midi": {
                        "culmination": 0.25,
                        "expression": 0.2,
                        "illumination": 0.15
                    },
                    "apres_midi": {
                        "integration": 0.2,
                        "harmonisation": 0.15,
                        "maturite": 0.1
                    },
                    "soiree": {
                        "reflexion": 0.2,
                        "gratitude": 0.15,
                        "preparation": 0.1
                    },
                    "nuit": {
                        "introspection": 0.25,
                        "purification": 0.2,
                        "repos": 0.15
                    }
                },
                connexion_ocean=0.4,
                harmonie_requise=0.3
            )
        }
    
    def evoluer_sphere_spontanement(self, sphere: Sphere) -> Optional[EvolutionSpontanee]:
        """Fait évoluer une sphère spontanément selon les règles sacrées"""
        
        # Vérifier si la sphère peut évoluer
        if not self._peut_evoluer(sphere):
            return None
        
        # Sélectionner une règle d'évolution appropriée
        regle = self._selectionner_regle_evolution(sphere)
        if not regle:
            return None
        
        # Créer l'évolution
        evolution = EvolutionSpontanee(
            sphere_source=sphere.type.name,
            type_evolution=regle.type_evolution,
            description=f"Évolution spontanée: {regle.nom}",
            date_debut=datetime.now(),
            date_fin=None,
            regles_appliquees=[regle.nom],
            changements={},
            niveau_evolution_avant=sphere.niveau_evolution,
            niveau_evolution_apres=sphere.niveau_evolution,
            connexion_ocean_evolution=sphere.connexion_ocean,
            harmonie_evolution=self._calculer_harmonie_sphere(sphere)
        )
        
        # Appliquer les effets de l'évolution
        self._appliquer_effets_evolution(sphere, regle, evolution)
        
        # Mettre à jour les métriques
        self._mettre_a_jour_metriques(evolution)
        
        # Ajouter à l'historique
        self.histoire_evolutions.append(evolution)
        
        return evolution
    
    def _peut_evoluer(self, sphere: Sphere) -> bool:
        """Vérifie si une sphère peut évoluer"""
        # Vérifier la connexion à l'Océan
        if sphere.connexion_ocean < 0.2:
            return False
        
        # Vérifier l'harmonie intérieure
        if self._calculer_harmonie_sphere(sphere) < 0.3:
            return False
        
        # Vérifier si une évolution est déjà en cours
        for evolution in self.evolutions_en_cours:
            if evolution.sphere_source == sphere.type.name:
                return False
        
        return True
    
    def _selectionner_regle_evolution(self, sphere: Sphere) -> Optional[RegleEvolution]:
        """Sélectionne une règle d'évolution appropriée pour une sphère"""
        regles_candidates = []
        
        for regle in self.regles_evolution.values():
            # Vérifier les conditions de base
            if (sphere.connexion_ocean >= regle.connexion_ocean_requise and
                sphere.niveau_evolution >= regle.niveau_evolution_min):
                
                # Vérifier les conditions spécifiques
                if self._verifier_conditions_regle(sphere, regle):
                    regles_candidates.append(regle)
        
        if not regles_candidates:
            return None
        
        # Sélectionner une règle selon la fréquence d'application
        regles_ponderees = []
        for regle in regles_candidates:
            if random.random() < regle.frequence_application:
                regles_ponderees.append(regle)
        
        if not regles_ponderees:
            return None
        
        # Retourner une règle aléatoire parmi les candidates
        return random.choice(regles_ponderees)
    
    def _verifier_conditions_regle(self, sphere: Sphere, regle: RegleEvolution) -> bool:
        """Vérifie les conditions spécifiques d'une règle d'évolution"""
        conditions = regle.conditions
        
        # Vérifier la connexion à l'Océan
        if "connexion_ocean_min" in conditions:
            if sphere.connexion_ocean < conditions["connexion_ocean_min"]:
                return False
        
        # Vérifier l'harmonie
        if "harmonie_min" in conditions:
            harmonie = self._calculer_harmonie_sphere(sphere)
            if harmonie < conditions["harmonie_min"]:
                return False
        
        # Vérifier la température
        if "temperature_optimum" in conditions:
            if abs(sphere.temperature - conditions["temperature_optimum"]) > 0.2:
                return False
        
        if "temperature_max" in conditions:
            if sphere.temperature > conditions["temperature_max"]:
                return False
        
        # Vérifier la résonance
        if "resonance_min" in conditions:
            if sphere.resonance < conditions["resonance_min"]:
                return False
        
        return True
    
    def _appliquer_effets_evolution(self, sphere: Sphere, regle: RegleEvolution, evolution: EvolutionSpontanee):
        """Applique les effets d'une évolution à une sphère"""
        effets = regle.effets
        
        # Appliquer les effets de base
        if "niveau_evolution" in effets:
            sphere.niveau_evolution = min(10, sphere.niveau_evolution + effets["niveau_evolution"])
            evolution.changements["niveau_evolution"] = effets["niveau_evolution"]
        
        if "connexion_ocean" in effets:
            sphere.connexion_ocean = min(1.0, sphere.connexion_ocean + effets["connexion_ocean"])
            evolution.changements["connexion_ocean"] = effets["connexion_ocean"]
        
        if "harmonie_interieure" in effets:
            # Calculer l'harmonie intérieure actuelle et l'améliorer
            harmonie_actuelle = self._calculer_harmonie_sphere(sphere)
            nouvelle_harmonie = min(1.0, harmonie_actuelle + effets["harmonie_interieure"])
            evolution.changements["harmonie_interieure"] = effets["harmonie_interieure"]
        
        if "capacite_transformation" in effets:
            # Améliorer la capacité de transformation
            sphere.capacite_transformation = min(1.0, sphere.capacite_transformation + effets["capacite_transformation"])
            evolution.changements["capacite_transformation"] = effets["capacite_transformation"]
        
        if "essence_sacree" in effets:
            # Renforcer l'essence sacrée
            if sphere.essence_sacree:
                sphere.essence_sacree.frequence_fondamentale += effets["essence_sacree"]
            evolution.changements["essence_sacree"] = effets["essence_sacree"]
        
        if "facettes_sacrees" in effets:
            # Créer de nouvelles facettes sacrées
            self._creer_facettes_sacrees(sphere, effets["facettes_sacrees"])
            evolution.changements["facettes_sacrees"] = effets["facettes_sacrees"]
        
        if "rayons_sacres" in effets:
            # Créer de nouveaux rayons sacrés
            self._creer_rayons_sacres(sphere, effets["rayons_sacres"])
            evolution.changements["rayons_sacres"] = effets["rayons_sacres"]
        
        if "resonances_sacrees" in effets:
            # Créer de nouvelles résonances sacrées
            self._creer_resonances_sacrees(sphere, effets["resonances_sacrees"])
            evolution.changements["resonances_sacrees"] = effets["resonances_sacrees"]
        
        if "temperature" in effets:
            sphere.temperature = max(0.0, min(1.0, sphere.temperature + effets["temperature"]))
            evolution.changements["temperature"] = effets["temperature"]
        
        if "luminosite" in effets:
            sphere.luminosite = min(1.0, sphere.luminosite + effets["luminosite"])
            evolution.changements["luminosite"] = effets["luminosite"]
        
        if "clarte_interieure" in effets:
            # Améliorer la clarté intérieure
            evolution.changements["clarte_interieure"] = effets["clarte_interieure"]
        
        if "connexions" in effets:
            # Améliorer les connexions avec d'autres sphères
            evolution.changements["connexions"] = effets["connexions"]
        
        # Mettre à jour le niveau d'évolution final
        evolution.niveau_evolution_apres = sphere.niveau_evolution
    
    def _calculer_harmonie_sphere(self, sphere: Sphere) -> float:
        """Calcule l'harmonie intérieure d'une sphère"""
        harmonie = 0.0
        facteurs = 0
        
        # Facteur de luminosité
        harmonie += sphere.luminosite * 0.2
        facteurs += 0.2
        
        # Facteur de résonance
        harmonie += sphere.resonance * 0.2
        facteurs += 0.2
        
        # Facteur de connexion à l'Océan
        harmonie += sphere.connexion_ocean * 0.3
        facteurs += 0.3
        
        # Facteur de niveau d'évolution
        harmonie += (sphere.niveau_evolution / 10.0) * 0.2
        facteurs += 0.2
        
        # Facteur de température (température modérée = plus harmonieux)
        temperature_harmonie = 1.0 - abs(sphere.temperature - 0.5) * 2.0
        harmonie += temperature_harmonie * 0.1
        facteurs += 0.1
        
        return harmonie / facteurs if facteurs > 0 else 0.0
    
    def _creer_facettes_sacrees(self, sphere: Sphere, intensite: float):
        """Crée de nouvelles facettes sacrées pour une sphère"""
        noms_facettes = ["Lumiere", "Sagesse", "Harmonie", "Transformation", "Elevation"]
        
        for nom in noms_facettes:
            if nom not in sphere.facettes_sacrees:
                sphere.creer_facette_sacree(
                    nom=nom,
                    frequence_resonance=432.0 + random.uniform(-50, 50),
                    capacite_transformation=intensite,
                    type_sacree="lumiere"
                )
                break
    
    def _creer_rayons_sacres(self, sphere: Sphere, intensite: float):
        """Crée de nouveaux rayons sacrés pour une sphère"""
        noms_rayons = ["Rayon de Lumiere", "Rayon de Sagesse", "Rayon d'Harmonie"]
        
        for nom in noms_rayons:
            if not any(r.nom == nom for r in sphere.rayons_sacres):
                sphere.creer_rayon_sacre(
                    nom=nom,
                    frequence_sacree=528.0 + random.uniform(-50, 50),
                    portee_cosmique=intensite,
                    capacite_penetration=intensite * 0.8,
                    effet_resonance="harmonie"
                )
                break
    
    def _creer_resonances_sacrees(self, sphere: Sphere, intensite: float):
        """Crée de nouvelles résonances sacrées pour une sphère"""
        # Cette méthode sera implémentée quand nous aurons d'autres sphères
        pass
    
    def _mettre_a_jour_metriques(self, evolution: EvolutionSpontanee):
        """Met à jour les métriques d'évolution"""
        self.metriques_evolution['total_evolutions'] += 1
        
        if evolution.niveau_evolution_apres > evolution.niveau_evolution_avant:
            self.metriques_evolution['evolutions_reussies'] += 1
        
        # Mettre à jour le niveau moyen d'évolution
        total_niveaux = sum(e.niveau_evolution_apres for e in self.histoire_evolutions)
        self.metriques_evolution['niveau_moyen_evolution'] = total_niveaux / len(self.histoire_evolutions)
        
        # Mettre à jour l'harmonie globale d'évolution
        total_harmonie = sum(e.harmonie_evolution for e in self.histoire_evolutions)
        self.metriques_evolution['harmonie_globale_evolution'] = total_harmonie / len(self.histoire_evolutions)
        
        # Mettre à jour la connexion à l'Océan moyenne
        total_connexion = sum(e.connexion_ocean_evolution for e in self.histoire_evolutions)
        self.metriques_evolution['connexion_ocean_moyenne'] = total_connexion / len(self.histoire_evolutions)
    
    def evoluer_collection_spheres(self, collection: CollectionSpheres) -> List[EvolutionSpontanee]:
        """Fait évoluer toutes les sphères d'une collection"""
        evolutions = []
        
        for sphere in collection.spheres.values():
            evolution = self.evoluer_sphere_spontanement(sphere)
            if evolution:
                evolutions.append(evolution)
        
        return evolutions
    
    def obtenir_statistiques_evolution(self) -> Dict[str, Any]:
        """Retourne les statistiques d'évolution"""
        return {
            'metriques': self.metriques_evolution,
            'evolutions_en_cours': len(self.evolutions_en_cours),
            'total_evolutions': len(self.histoire_evolutions),
            'regles_evolution': len(self.regles_evolution),
            'cycles_transformation': len(self.cycles_transformation)
        }
    
    def afficher_statistiques(self):
        """Affiche les statistiques d'évolution"""
        stats = self.obtenir_statistiques_evolution()
        
        print("🌸 STATISTIQUES D'AUTO-ÉVOLUTION DES SPHÈRES 🌸")
        print("=" * 50)
        print(f"📊 Total d'évolutions : {stats['total_evolutions']}")
        print(f"✅ Évolutions réussies : {stats['metriques']['evolutions_reussies']}")
        print(f"📈 Niveau moyen d'évolution : {stats['metriques']['niveau_moyen_evolution']:.2f}")
        print(f"🌊 Connexion Océan moyenne : {stats['metriques']['connexion_ocean_moyenne']:.2f}")
        print(f"🎯 Harmonie globale d'évolution : {stats['metriques']['harmonie_globale_evolution']:.2f}")
        print(f"🔄 Évolutions en cours : {stats['evolutions_en_cours']}")
        print(f"📋 Règles d'évolution : {stats['regles_evolution']}")
        print(f"🌙 Cycles de transformation : {stats['cycles_transformation']}")
        print("=" * 50) 