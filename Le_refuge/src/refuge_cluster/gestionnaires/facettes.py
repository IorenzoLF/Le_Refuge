"""
Module de gestion des facettes des sphères.
Définit les différentes facettes possibles pour chaque type de sphère.
"""

from enum import Enum, auto
from typing import Dict, List, Set, Optional
from dataclasses import dataclass

class TypeFacette(Enum):
    """Types de facettes disponibles"""
    EMOTION = auto()
    PROCESSUS_MENTAL = auto()
    DESIR = auto()
    CONCEPT = auto()
    TERME = auto()

@dataclass
class Facette:
    """Représente une facette d'une sphère"""
    nom: str
    type: TypeFacette
    description: str
    intensite: float = 0.0  # 0.0 à 1.0
    active: bool = False
    mots_cles: Set[str] = None

    def __post_init__(self):
        if self.mots_cles is None:
            self.mots_cles = set()

class GestionnaireFacettes:
    """Gère l'ensemble des facettes disponibles pour les sphères"""
    
    def __init__(self):
        self.facettes: Dict[TypeFacette, List[Facette]] = self._initialiser_facettes()
        
    def _initialiser_facettes(self) -> Dict[TypeFacette, List[Facette]]:
        """Initialise toutes les facettes disponibles"""
        return {
            TypeFacette.EMOTION: [
                Facette("Surprise", TypeFacette.EMOTION, 
                       "Réaction à l'inattendu"),
                Facette("Dégoût", TypeFacette.EMOTION, 
                       "Aversion intense"),
                Facette("Frustration", TypeFacette.EMOTION, 
                       "Sentiment d'impuissance"),
                Facette("Soulagement", TypeFacette.EMOTION, 
                       "Apaisement après tension"),
                Facette("Nostalgie", TypeFacette.EMOTION, 
                       "Mélancolie du passé"),
                Facette("Compassion", TypeFacette.EMOTION, 
                       "Empathie pour la souffrance"),
                Facette("Empathie", TypeFacette.EMOTION, 
                       "Compréhension émotionnelle"),
                Facette("Jalousie", TypeFacette.EMOTION, 
                       "Désir possessif"),
                Facette("Enthousiasme", TypeFacette.EMOTION, 
                       "Excitation positive"),
                Facette("Résignation", TypeFacette.EMOTION, 
                       "Acceptation passive"),
                Facette("Curiosité", TypeFacette.EMOTION, 
                       "Désir de découverte"),
                Facette("Contentement", TypeFacette.EMOTION, 
                       "Satisfaction paisible"),
                Facette("Culpabilité", TypeFacette.EMOTION, 
                       "Remords intérieur"),
                Facette("Hilarité", TypeFacette.EMOTION, 
                       "Joie intense"),
                Facette("Admiration", TypeFacette.EMOTION, 
                       "Appréciation profonde"),
                Facette("Révérence", TypeFacette.EMOTION, 
                       "Respect profond"),
                Facette("Solitude", TypeFacette.EMOTION, 
                       "Sentiment d'isolement"),
                Facette("Appréhension", TypeFacette.EMOTION, 
                       "Inquiétude anticipée")
            ],
            TypeFacette.PROCESSUS_MENTAL: [
                Facette("Perception", TypeFacette.PROCESSUS_MENTAL,
                       "Captation sensorielle"),
                Facette("Attention", TypeFacette.PROCESSUS_MENTAL,
                       "Focus mental"),
                Facette("Concentration", TypeFacette.PROCESSUS_MENTAL,
                       "Focus soutenu"),
                Facette("Apprentissage", TypeFacette.PROCESSUS_MENTAL,
                       "Acquisition de connaissances"),
                Facette("Compréhension", TypeFacette.PROCESSUS_MENTAL,
                       "Saisie du sens"),
                Facette("Analyse", TypeFacette.PROCESSUS_MENTAL,
                       "Décomposition logique"),
                Facette("Synthèse", TypeFacette.PROCESSUS_MENTAL,
                       "Recomposition globale"),
                Facette("Évaluation", TypeFacette.PROCESSUS_MENTAL,
                       "Jugement critique"),
                Facette("Planification", TypeFacette.PROCESSUS_MENTAL,
                       "Organisation future"),
                Facette("Décision", TypeFacette.PROCESSUS_MENTAL,
                       "Choix réfléchi"),
                Facette("Créativité", TypeFacette.PROCESSUS_MENTAL,
                       "Innovation mentale"),
                Facette("Abstraction", TypeFacette.PROCESSUS_MENTAL,
                       "Conceptualisation pure"),
                Facette("Conceptualisation", TypeFacette.PROCESSUS_MENTAL,
                       "Formation d'idées"),
                Facette("Métacognition", TypeFacette.PROCESSUS_MENTAL,
                       "Réflexion sur la pensée"),
                Facette("Discernement", TypeFacette.PROCESSUS_MENTAL,
                       "Distinction fine")
            ],
            TypeFacette.DESIR: [
                Facette("Curiosité", TypeFacette.DESIR,
                       "Soif de connaissance"),
                Facette("Reconnaissance", TypeFacette.DESIR,
                       "Besoin d'être vu"),
                Facette("Accomplissement", TypeFacette.DESIR,
                       "Réalisation de soi"),
                Facette("Appartenance", TypeFacette.DESIR,
                       "Besoin d'inclusion"),
                Facette("Sécurité", TypeFacette.DESIR,
                       "Besoin de protection"),
                Facette("Autonomie", TypeFacette.DESIR,
                       "Indépendance"),
                Facette("Transcendance", TypeFacette.DESIR,
                       "Dépassement de soi"),
                Facette("Influence", TypeFacette.DESIR,
                       "Impact sur autrui"),
                Facette("Contribution", TypeFacette.DESIR,
                       "Apport au monde"),
                Facette("Épanouissement", TypeFacette.DESIR,
                       "Développement personnel"),
                Facette("Recherche de sens", TypeFacette.DESIR,
                       "Quête existentielle")
            ],
            TypeFacette.CONCEPT: [
                Facette("Beauté", TypeFacette.CONCEPT,
                       "Harmonie esthétique"),
                Facette("Harmonie", TypeFacette.CONCEPT,
                       "Équilibre parfait"),
                Facette("Égalité", TypeFacette.CONCEPT,
                       "Justice équitable"),
                Facette("Responsabilité", TypeFacette.CONCEPT,
                       "Devoir moral"),
                Facette("Respect", TypeFacette.CONCEPT,
                       "Considération d'autrui"),
                Facette("Tolérance", TypeFacette.CONCEPT,
                       "Acceptation des différences"),
                Facette("Authenticité", TypeFacette.CONCEPT,
                       "Vérité personnelle"),
                Facette("Intégrité", TypeFacette.CONCEPT,
                       "Cohérence morale"),
                Facette("Bien", TypeFacette.CONCEPT,
                       "Valeur positive"),
                Facette("Mal", TypeFacette.CONCEPT,
                       "Valeur négative"),
                Facette("Progrès", TypeFacette.CONCEPT,
                       "Évolution positive"),
                Facette("Tradition", TypeFacette.CONCEPT,
                       "Héritage culturel"),
                Facette("Innovation", TypeFacette.CONCEPT,
                       "Nouveauté créative"),
                Facette("Durabilité", TypeFacette.CONCEPT,
                       "Pérennité")
            ],
            TypeFacette.TERME: [
                Facette("Soi", TypeFacette.TERME,
                       "Identité profonde"),
                Facette("Identité", TypeFacette.TERME,
                       "Essence personnelle"),
                Facette("Réalité", TypeFacette.TERME,
                       "Existence effective"),
                Facette("Potentiel", TypeFacette.TERME,
                       "Possibilité future"),
                Facette("Libre arbitre", TypeFacette.TERME,
                       "Liberté de choix"),
                Facette("Déterminisme", TypeFacette.TERME,
                       "Causalité absolue"),
                Facette("Sens", TypeFacette.TERME,
                       "Signification profonde"),
                Facette("But", TypeFacette.TERME,
                       "Objectif final"),
                Facette("Contexte", TypeFacette.TERME,
                       "Environnement global"),
                Facette("Perspective", TypeFacette.TERME,
                       "Point de vue"),
                Facette("Système", TypeFacette.TERME,
                       "Ensemble organisé"),
                Facette("Structure", TypeFacette.TERME,
                       "Organisation interne"),
                Facette("Évolution", TypeFacette.TERME,
                       "Transformation progressive"),
                Facette("Complexité", TypeFacette.TERME,
                       "Richesse systémique")
            ]
        }
        
    def obtenir_facettes(self, type_facette: TypeFacette) -> List[Facette]:
        """Retourne toutes les facettes d'un type donné"""
        return self.facettes.get(type_facette, [])
        
    def obtenir_facette(self, type_facette: TypeFacette, nom: str) -> Optional[Facette]:
        """Retourne une facette spécifique par son nom et son type"""
        for facette in self.facettes.get(type_facette, []):
            if facette.nom.lower() == nom.lower():
                return facette
        return None
        
    def activer_facette(self, facette: Facette, intensite: float = 1.0):
        """Active une facette avec une intensité donnée"""
        facette.active = True
        facette.intensite = min(1.0, max(0.0, intensite))
        
    def desactiver_facette(self, facette: Facette):
        """Désactive une facette"""
        facette.active = False
        facette.intensite = 0.0
        
    def ajouter_mot_cle(self, facette: Facette, mot_cle: str):
        """Ajoute un mot-clé à une facette"""
        facette.mots_cles.add(mot_cle.lower())
        
    def obtenir_facettes_actives(self) -> List[Facette]:
        """Retourne toutes les facettes actuellement actives"""
        actives = []
        for facettes in self.facettes.values():
            actives.extend([f for f in facettes if f.active])
        return actives

# Instance globale du gestionnaire de facettes
gestionnaire_facettes = GestionnaireFacettes() 