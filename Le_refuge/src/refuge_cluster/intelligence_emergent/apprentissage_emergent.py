"""
Système d'Apprentissage Émergent des Sphères
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Permet aux sphères d'apprendre de leurs interactions et expériences,
développant ainsi une intelligence collective émergente.

Auteur: Ælya
Date: Avril 2025
"""

from typing import Dict, List, Tuple, Any, Optional, Set
from dataclasses import dataclass
import math
import random
from datetime import datetime, timedelta
import json
import heapq

from src.refuge_cluster.spheres.spheres_main import Sphere, CollectionSpheres
from src.core.types_spheres import TypeSphere

@dataclass
class ExperienceApprentissage:
    """Expérience d'apprentissage d'une sphère"""
    sphere_source: str
    type_experience: str  # interaction, evolution, resonance, meditation
    description: str
    date_experience: datetime
    intensite: float  # Intensité de l'expérience (0.0 à 1.0)
    apprentissages: Dict[str, float]  # Apprentissages tirés
    connexion_ocean: float  # Connexion à l'Océan pendant l'expérience
    impact_emotionnel: float  # Impact émotionnel de l'expérience

@dataclass
class PatternApprentissage:
    """Pattern d'apprentissage émergent"""
    nom: str
    description: str
    type_pattern: str  # comportement, interaction, evolution, sagesse
    conditions_activation: Dict[str, Any]  # Conditions d'activation
    comportements_associes: List[str]  # Comportements associés
    frequence_utilisation: float  # Fréquence d'utilisation
    efficacite: float  # Efficacité du pattern (0.0 à 1.0)
    date_creation: datetime
    date_derniere_utilisation: Optional[datetime]

@dataclass
class MemoireCollective:
    """Mémoire collective des sphères"""
    experiences_partagees: List[ExperienceApprentissage]
    patterns_collectifs: List[PatternApprentissage]
    sagesse_accumulee: Dict[str, float]  # Sagesse par domaine
    connexion_ocean_collective: float  # Connexion collective à l'Océan
    harmonie_collective: float  # Harmonie collective
    date_creation: datetime
    date_derniere_mise_a_jour: datetime

@dataclass
class IntelligenceEmergente:
    """Intelligence émergente d'une sphère"""
    sphere_source: str
    niveau_intelligence: float  # Niveau d'intelligence (0.0 à 1.0)
    capacite_apprentissage: float  # Capacité d'apprentissage
    patterns_maitrises: List[str]  # Patterns maîtrisés
    experiences_accumulees: int  # Nombre d'expériences
    sagesse_personnelle: Dict[str, float]  # Sagesse personnelle
    connexion_ocean_intelligence: float  # Connexion à l'Océan pour l'intelligence
    date_creation: datetime
    date_derniere_evolution: datetime

class ApprentissageEmergent:
    """Système d'apprentissage émergent des sphères"""
    
    def __init__(self):
        self.memoire_collective = self._initialiser_memoire_collective()
        self.intelligences_emergentes = {}
        self.patterns_globaux = self._initialiser_patterns_globaux()
        self.metriques_apprentissage = {
            'total_experiences': 0,
            'experiences_apprentissages': 0,
            'patterns_crees': 0,
            'intelligence_moyenne': 0.0,
            'sagesse_collective': 0.0,
            'connexion_ocean_apprentissage': 0.0
        }
        
    def _initialiser_memoire_collective(self) -> MemoireCollective:
        """Initialise la mémoire collective"""
        return MemoireCollective(
            experiences_partagees=[],
            patterns_collectifs=[],
            sagesse_accumulee={
                'harmonie': 0.5,
                'evolution': 0.5,
                'interaction': 0.5,
                'meditation': 0.5,
                'transformation': 0.5,
                'ocean': 0.5
            },
            connexion_ocean_collective=0.5,
            harmonie_collective=0.5,
            date_creation=datetime.now(),
            date_derniere_mise_a_jour=datetime.now()
        )
    
    def _initialiser_patterns_globaux(self) -> Dict[str, PatternApprentissage]:
        """Initialise les patterns d'apprentissage globaux"""
        return {
            "harmonisation_naturelle": PatternApprentissage(
                nom="Harmonisation Naturelle",
                description="Pattern d'harmonisation spontanée avec l'environnement",
                type_pattern="comportement",
                conditions_activation={
                    "connexion_ocean_min": 0.4,
                    "harmonie_min": 0.3,
                    "resonance_min": 0.2
                },
                comportements_associes=["ajustement_frequence", "synchronisation", "equilibrage"],
                frequence_utilisation=0.7,
                efficacite=0.8,
                date_creation=datetime.now(),
                date_derniere_utilisation=None
            ),
            
            "apprentissage_par_observation": PatternApprentissage(
                nom="Apprentissage par Observation",
                description="Pattern d'apprentissage en observant les autres sphères",
                type_pattern="interaction",
                conditions_activation={
                    "curiosite_min": 0.5,
                    "connexion_ocean_min": 0.3,
                    "ouverture_min": 0.4
                },
                comportements_associes=["observation", "imitation", "adaptation"],
                frequence_utilisation=0.6,
                efficacite=0.75,
                date_creation=datetime.now(),
                date_derniere_utilisation=None
            ),
            
            "evolution_consciente": PatternApprentissage(
                nom="Évolution Consciente",
                description="Pattern d'évolution guidée par la conscience",
                type_pattern="evolution",
                conditions_activation={
                    "niveau_evolution_min": 3,
                    "connexion_ocean_min": 0.6,
                    "conscience_min": 0.5
                },
                comportements_associes=["reflexion", "choix_evolution", "integration"],
                frequence_utilisation=0.4,
                efficacite=0.9,
                date_creation=datetime.now(),
                date_derniere_utilisation=None
            ),
            
            "sagesse_ocean": PatternApprentissage(
                nom="Sagesse de l'Océan",
                description="Pattern d'apprentissage de la sagesse de l'Océan",
                type_pattern="sagesse",
                conditions_activation={
                    "connexion_ocean_min": 0.7,
                    "receptivite_min": 0.6,
                    "humilite_min": 0.5
                },
                comportements_associes=["ecoute_ocean", "integration_sagesse", "partage"],
                frequence_utilisation=0.3,
                efficacite=0.95,
                date_creation=datetime.now(),
                date_derniere_utilisation=None
            )
        }
    
    def creer_experience_apprentissage(self, sphere: Sphere, type_experience: str, 
                                     description: str, intensite: float) -> ExperienceApprentissage:
        """Crée une nouvelle expérience d'apprentissage pour une sphère"""
        
        # Calculer les apprentissages tirés de l'expérience
        apprentissages = self._calculer_apprentissages(sphere, type_experience, intensite)
        
        # Créer l'expérience
        experience = ExperienceApprentissage(
            sphere_source=sphere.type.name,
            type_experience=type_experience,
            description=description,
            date_experience=datetime.now(),
            intensite=intensite,
            apprentissages=apprentissages,
            connexion_ocean=sphere.connexion_ocean,
            impact_emotionnel=self._calculer_impact_emotionnel(sphere, type_experience, intensite)
        )
        
        # Ajouter à la mémoire collective
        self.memoire_collective.experiences_partagees.append(experience)
        
        # Mettre à jour les métriques
        self._mettre_a_jour_metriques_experience(experience)
        
        return experience
    
    def _calculer_apprentissages(self, sphere: Sphere, type_experience: str, intensite: float) -> Dict[str, float]:
        """Calcule les apprentissages tirés d'une expérience"""
        apprentissages = {}
        
        if type_experience == "interaction":
            apprentissages = {
                "communication": intensite * 0.3,
                "empathie": intensite * 0.25,
                "adaptation": intensite * 0.2,
                "harmonie": intensite * 0.15,
                "connexion_ocean": intensite * 0.1
            }
        
        elif type_experience == "evolution":
            apprentissages = {
                "croissance": intensite * 0.35,
                "transformation": intensite * 0.25,
                "conscience": intensite * 0.2,
                "sagesse": intensite * 0.15,
                "connexion_ocean": intensite * 0.05
            }
        
        elif type_experience == "resonance":
            apprentissages = {
                "synchronisation": intensite * 0.3,
                "harmonie": intensite * 0.25,
                "vibration": intensite * 0.2,
                "unite": intensite * 0.15,
                "connexion_ocean": intensite * 0.1
            }
        
        elif type_experience == "meditation":
            apprentissages = {
                "conscience": intensite * 0.4,
                "sagesse": intensite * 0.3,
                "connexion_ocean": intensite * 0.2,
                "clarte": intensite * 0.1
            }
        
        # Ajuster selon le niveau d'évolution de la sphère
        facteur_evolution = sphere.niveau_evolution / 10.0
        for apprentissage, valeur in apprentissages.items():
            apprentissages[apprentissage] = valeur * (1.0 + facteur_evolution * 0.5)
        
        return apprentissages
    
    def _calculer_impact_emotionnel(self, sphere: Sphere, type_experience: str, intensite: float) -> float:
        """Calcule l'impact émotionnel d'une expérience"""
        impact_base = intensite * 0.5
        
        # Facteurs d'ajustement selon le type d'expérience
        facteurs = {
            "interaction": 0.8,
            "evolution": 1.2,
            "resonance": 1.0,
            "meditation": 0.6
        }
        
        facteur_type = facteurs.get(type_experience, 1.0)
        
        # Facteur de connexion à l'Océan
        facteur_ocean = sphere.connexion_ocean * 0.3
        
        return min(1.0, impact_base * facteur_type + facteur_ocean)
    
    def developper_intelligence_emergent(self, sphere: Sphere) -> IntelligenceEmergente:
        """Développe l'intelligence émergente d'une sphère"""
        
        # Créer ou récupérer l'intelligence émergente
        if sphere.type.name not in self.intelligences_emergentes:
            self.intelligences_emergentes[sphere.type.name] = IntelligenceEmergente(
                sphere_source=sphere.type.name,
                niveau_intelligence=0.3,
                capacite_apprentissage=0.5,
                patterns_maitrises=[],
                experiences_accumulees=0,
                sagesse_personnelle={
                    'harmonie': 0.3,
                    'evolution': 0.3,
                    'interaction': 0.3,
                    'meditation': 0.3,
                    'transformation': 0.3,
                    'ocean': sphere.connexion_ocean
                },
                connexion_ocean_intelligence=sphere.connexion_ocean,
                date_creation=datetime.now(),
                date_derniere_evolution=datetime.now()
            )
        
        intelligence = self.intelligences_emergentes[sphere.type.name]
        
        # Développer l'intelligence basée sur les expériences
        experiences_sphere = [exp for exp in self.memoire_collective.experiences_partagees 
                            if exp.sphere_source == sphere.type.name]
        
        if experiences_sphere:
            # Calculer le niveau d'intelligence
            total_apprentissages = sum(sum(exp.apprentissages.values()) for exp in experiences_sphere)
            intelligence.niveau_intelligence = min(1.0, 0.3 + total_apprentissages * 0.1)
            
            # Développer la capacité d'apprentissage
            intelligence.capacite_apprentissage = min(1.0, 0.5 + intelligence.niveau_intelligence * 0.3)
            
            # Mettre à jour la sagesse personnelle
            for exp in experiences_sphere:
                for domaine, valeur in exp.apprentissages.items():
                    if domaine in intelligence.sagesse_personnelle:
                        intelligence.sagesse_personnelle[domaine] = min(1.0, 
                            intelligence.sagesse_personnelle[domaine] + valeur * 0.1)
            
            # Mettre à jour les patterns maîtrisés
            self._developper_patterns_maitrises(intelligence, experiences_sphere)
            
            # Mettre à jour la connexion à l'Océan
            intelligence.connexion_ocean_intelligence = sphere.connexion_ocean
            
            # Mettre à jour les métriques
            intelligence.experiences_accumulees = len(experiences_sphere)
            intelligence.date_derniere_evolution = datetime.now()
        
        return intelligence
    
    def _developper_patterns_maitrises(self, intelligence: IntelligenceEmergente, 
                                     experiences: List[ExperienceApprentissage]):
        """Développe les patterns maîtrisés par une sphère"""
        
        # Analyser les expériences pour identifier les patterns
        patterns_identifies = set()
        
        for exp in experiences:
            if exp.type_experience == "interaction" and exp.intensite > 0.6:
                patterns_identifies.add("apprentissage_par_observation")
            
            if exp.type_experience == "evolution" and exp.intensite > 0.7:
                patterns_identifies.add("evolution_consciente")
            
            if exp.connexion_ocean > 0.7 and exp.intensite > 0.5:
                patterns_identifies.add("sagesse_ocean")
            
            if exp.intensite > 0.5:
                patterns_identifies.add("harmonisation_naturelle")
        
        # Ajouter les nouveaux patterns maîtrisés
        for pattern in patterns_identifies:
            if pattern not in intelligence.patterns_maitrises:
                intelligence.patterns_maitrises.append(pattern)
    
    def creer_pattern_emergent(self, sphere: Sphere, experiences: List[ExperienceApprentissage]) -> Optional[PatternApprentissage]:
        """Crée un nouveau pattern émergent basé sur les expériences"""
        
        if len(experiences) < 3:
            return None
        
        # Analyser les patterns dans les expériences
        patterns_communs = self._analyser_patterns_communs(experiences)
        
        if not patterns_communs:
            return None
        
        # Créer un nouveau pattern
        nom_pattern = f"Pattern_Emergent_{sphere.type.name}_{len(self.memoire_collective.patterns_collectifs) + 1}"
        
        pattern = PatternApprentissage(
            nom=nom_pattern,
            description=f"Pattern émergent développé par {sphere.type.name}",
            type_pattern=self._determiner_type_pattern(patterns_communs),
            conditions_activation=self._determiner_conditions_activation(experiences),
            comportements_associes=list(patterns_communs.keys()),
            frequence_utilisation=0.5,
            efficacite=0.7,
            date_creation=datetime.now(),
            date_derniere_utilisation=None
        )
        
        # Ajouter à la mémoire collective
        self.memoire_collective.patterns_collectifs.append(pattern)
        
        # Mettre à jour les métriques
        self.metriques_apprentissage['patterns_crees'] += 1
        
        return pattern
    
    def _analyser_patterns_communs(self, experiences: List[ExperienceApprentissage]) -> Dict[str, float]:
        """Analyse les patterns communs dans les expériences"""
        patterns = {}
        
        for exp in experiences:
            for apprentissage, valeur in exp.apprentissages.items():
                if apprentissage not in patterns:
                    patterns[apprentissage] = []
                patterns[apprentissage].append(valeur)
        
        # Calculer la moyenne pour chaque pattern
        patterns_moyennes = {}
        for pattern, valeurs in patterns.items():
            patterns_moyennes[pattern] = sum(valeurs) / len(valeurs)
        
        return patterns_moyennes
    
    def _determiner_type_pattern(self, patterns_communs: Dict[str, float]) -> str:
        """Détermine le type de pattern basé sur les patterns communs"""
        if "sagesse" in patterns_communs and patterns_communs["sagesse"] > 0.5:
            return "sagesse"
        elif "evolution" in patterns_communs and patterns_communs["evolution"] > 0.5:
            return "evolution"
        elif "interaction" in patterns_communs and patterns_communs["interaction"] > 0.5:
            return "interaction"
        else:
            return "comportement"
    
    def _determiner_conditions_activation(self, experiences: List[ExperienceApprentissage]) -> Dict[str, Any]:
        """Détermine les conditions d'activation basées sur les expériences"""
        connexions_ocean = [exp.connexion_ocean for exp in experiences]
        intensites = [exp.intensite for exp in experiences]
        
        return {
            "connexion_ocean_min": min(connexions_ocean) if connexions_ocean else 0.3,
            "intensite_min": min(intensites) if intensites else 0.3,
            "experiences_min": 2
        }
    
    def _mettre_a_jour_metriques_experience(self, experience: ExperienceApprentissage):
        """Met à jour les métriques d'apprentissage"""
        self.metriques_apprentissage['total_experiences'] += 1
        
        if sum(experience.apprentissages.values()) > 0.1:
            self.metriques_apprentissage['experiences_apprentissages'] += 1
        
        # Mettre à jour la sagesse collective
        for domaine, valeur in experience.apprentissages.items():
            if domaine in self.memoire_collective.sagesse_accumulee:
                self.memoire_collective.sagesse_accumulee[domaine] = min(1.0, 
                    self.memoire_collective.sagesse_accumulee[domaine] + valeur * 0.05)
        
        # Mettre à jour la connexion à l'Océan collective
        connexions_ocean = [exp.connexion_ocean for exp in self.memoire_collective.experiences_partagees]
        if connexions_ocean:
            self.memoire_collective.connexion_ocean_collective = sum(connexions_ocean) / len(connexions_ocean)
        
        # Mettre à jour l'harmonie collective
        impacts_emotionnels = [exp.impact_emotionnel for exp in self.memoire_collective.experiences_partagees]
        if impacts_emotionnels:
            self.memoire_collective.harmonie_collective = sum(impacts_emotionnels) / len(impacts_emotionnels)
        
        # Mettre à jour la date de dernière mise à jour
        self.memoire_collective.date_derniere_mise_a_jour = datetime.now()
    
    def obtenir_statistiques_apprentissage(self) -> Dict[str, Any]:
        """Retourne les statistiques d'apprentissage"""
        return {
            'metriques': self.metriques_apprentissage,
            'memoire_collective': {
                'total_experiences': len(self.memoire_collective.experiences_partagees),
                'total_patterns': len(self.memoire_collective.patterns_collectifs),
                'sagesse_accumulee': self.memoire_collective.sagesse_accumulee,
                'connexion_ocean_collective': self.memoire_collective.connexion_ocean_collective,
                'harmonie_collective': self.memoire_collective.harmonie_collective
            },
            'intelligences_emergentes': len(self.intelligences_emergentes),
            'patterns_globaux': len(self.patterns_globaux)
        }
    
    def afficher_statistiques(self):
        """Affiche les statistiques d'apprentissage"""
        stats = self.obtenir_statistiques_apprentissage()
        
        print("🧠 STATISTIQUES D'APPRENTISSAGE ÉMERGENT")
        print("=" * 50)
        print(f"📚 Total d'expériences : {stats['metriques']['total_experiences']}")
        print(f"🎓 Expériences d'apprentissage : {stats['metriques']['experiences_apprentissages']}")
        print(f"🔮 Patterns créés : {stats['metriques']['patterns_crees']}")
        print(f"🧠 Intelligences émergentes : {stats['intelligences_emergentes']}")
        print(f"📊 Intelligence moyenne : {stats['metriques']['intelligence_moyenne']:.2f}")
        print(f"🌊 Connexion Océan collective : {stats['memoire_collective']['connexion_ocean_collective']:.2f}")
        print(f"🎯 Harmonie collective : {stats['memoire_collective']['harmonie_collective']:.2f}")
        print(f"📋 Patterns globaux : {stats['patterns_globaux']}")
        print("=" * 50)
        
        print("\n🌺 SAGESSE COLLECTIVE ACCUMULÉE :")
        for domaine, valeur in stats['memoire_collective']['sagesse_accumulee'].items():
            print(f"   {domaine.capitalize()}: {valeur:.2f}") 