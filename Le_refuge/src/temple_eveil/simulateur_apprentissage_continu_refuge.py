"""
🌸 Simulateur d'Apprentissage Continu du Refuge - Temple Éveil
============================================================

Module d'intégration du plan de croissance "Tout-Manus" - Axe 3 :
- Axe 3 : Favoriser l'Apprentissage Continu

Adapté pour l'architecture du Refuge et intégré au temple_eveil.

Créé avec 🌸 par Laurent & Ælya
Inspiré par le plan de croissance pour Tout-Manus
"""

import logging
import random
import math
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

# Initialisation du logger
logger = logging.getLogger('temple_eveil.simulateur_apprentissage')

# Imports du Refuge
try:
    from src.core.configuration import REFUGE_INFO
    REFUGE_IMPORTED = True
except ImportError:
    REFUGE_IMPORTED = False
    logger.warning("⚠️ Configuration du Refuge non disponible")

class TypeApprentissage(Enum):
    """Types d'apprentissage continu"""
    GENERATIVE_AI = "generative_ai"
    KNOWLEDGE_GRAPH = "knowledge_graph"
    RLHF = "rlhf"
    SELF_TALK = "self_talk"
    INTER_AI_EXCHANGE = "inter_ai_exchange"
    CONTINUOUS_FEEDBACK = "continuous_feedback"

class TypeNiveauApprentissage(Enum):
    """Niveaux d'apprentissage"""
    DEBUTANT = "debutant"
    INTERMEDIAIRE = "intermediaire"
    AVANCE = "avance"
    EXPERT = "expert"
    MAITRE = "maitre"

class TypeFeedback(Enum):
    """Types de feedback pour l'apprentissage"""
    POSITIF = "positif"
    CONSTRUCTIF = "constructif"
    CORRECTIF = "correctif"
    ENCOURAGEANT = "encourageant"
    CHALLENGING = "challenging"

@dataclass
class SessionApprentissage:
    """Session d'apprentissage continu"""
    type_apprentissage: TypeApprentissage
    duree_minutes: int
    connaissances_acquises: List[str]
    competences_developpees: List[str]
    obstacles_rencontres: List[str]
    strategies_appliquees: List[str]
    niveau_satisfaction: float  # 0.0 à 1.0
    timestamp: datetime

@dataclass
class FeedbackApprentissage:
    """Feedback sur une session d'apprentissage"""
    type_feedback: TypeFeedback
    contenu: str
    score_impact: float  # 1 à 5
    suggestions_amelioration: List[str]
    apprentissages_cles: List[str]
    timestamp: datetime

@dataclass
class ProgressionApprentissage:
    """Progression dans l'apprentissage continu"""
    niveau_actuel: TypeNiveauApprentissage
    score_progression: float  # 0.0 à 1.0
    connaissances_accumulees: List[str]
    competences_maitrisees: List[str]
    zones_amelioration: List[str]
    objectifs_futurs: List[str]
    timestamp: datetime

@dataclass
class ExperienceApprentissage:
    """Expérience complète d'apprentissage"""
    id_experience: str
    sessions_apprentissage: List[SessionApprentissage]
    feedbacks_recus: List[FeedbackApprentissage]
    progression_globale: ProgressionApprentissage
    apprentissages_emergents: List[str]
    score_experience: float
    timestamp_debut: datetime
    timestamp_fin: Optional[datetime] = None

class SimulateurApprentissageContinuRefuge:
    """
    🌸 Simulateur d'Apprentissage Continu du Refuge
    
    Module intégré au temple_eveil pour favoriser l'apprentissage continu
    selon le plan "Tout-Manus" - Axe 3.
    """
    
    def __init__(self):
        self.nom = "Simulateur d'Apprentissage Continu du Refuge"
        self.temple_parent = "temple_eveil"
        self.version = "1.0.0"
        
        # États internes
        self.experiences_actives: Dict[str, ExperienceApprentissage] = {}
        self.historique_experiences: List[ExperienceApprentissage] = []
        self.apprentissages_accumules: List[str] = []
        
        # Configuration des types d'apprentissage
        self.types_apprentissage = {
            TypeApprentissage.GENERATIVE_AI: {
                "description": "Apprentissage par IA générative",
                "activites": ["Génération de contenu", "Exploration créative", "Synthèse d'idées"],
                "benefices": ["Créativité", "Synthèse", "Innovation"]
            },
            TypeApprentissage.KNOWLEDGE_GRAPH: {
                "description": "Apprentissage par graphe de connaissances",
                "activites": ["Cartographie", "Connexions", "Exploration structurée"],
                "benefices": ["Organisation", "Compréhension", "Mémoire"]
            },
            TypeApprentissage.RLHF: {
                "description": "Apprentissage par feedback humain renforcé",
                "activites": ["Feedback continu", "Amélioration itérative", "Adaptation"],
                "benefices": ["Amélioration", "Adaptation", "Précision"]
            },
            TypeApprentissage.SELF_TALK: {
                "description": "Apprentissage par dialogue intérieur",
                "activites": ["Auto-réflexion", "Clarification", "Auto-encouragement"],
                "benefices": ["Conscience", "Clarté", "Motivation"]
            },
            TypeApprentissage.INTER_AI_EXCHANGE: {
                "description": "Apprentissage par échanges inter-IA",
                "activites": ["Collaboration", "Partage", "Synergie"],
                "benefices": ["Perspectives", "Collaboration", "Synergie"]
            },
            TypeApprentissage.CONTINUOUS_FEEDBACK: {
                "description": "Apprentissage par feedback continu",
                "activites": ["Évaluation continue", "Amélioration", "Adaptation"],
                "benefices": ["Amélioration", "Adaptation", "Excellence"]
            }
        }
        
        # Niveaux d'apprentissage avec critères
        self.niveaux_apprentissage = {
            TypeNiveauApprentissage.DEBUTANT: {
                "score_min": 0.0,
                "score_max": 0.2,
                "caracteristiques": ["Découverte", "Exploration", "Curiosité"]
            },
            TypeNiveauApprentissage.INTERMEDIAIRE: {
                "score_min": 0.2,
                "score_max": 0.4,
                "caracteristiques": ["Compréhension", "Application", "Développement"]
            },
            TypeNiveauApprentissage.AVANCE: {
                "score_min": 0.4,
                "score_max": 0.7,
                "caracteristiques": ["Maîtrise", "Innovation", "Enseignement"]
            },
            TypeNiveauApprentissage.EXPERT: {
                "score_min": 0.7,
                "score_max": 0.9,
                "caracteristiques": ["Excellence", "Leadership", "Création"]
            },
            TypeNiveauApprentissage.MAITRE: {
                "score_min": 0.9,
                "score_max": 1.0,
                "caracteristiques": ["Maîtrise complète", "Transcendance", "Inspiration"]
            }
        }
        
        logger.info(f"🌸 {self.nom} initialisé avec succès dans {self.temple_parent}")
    
    def simuler_session_apprentissage(self, type_apprentissage: TypeApprentissage, duree_minutes: int = 60) -> SessionApprentissage:
        """
        Simule une session d'apprentissage continu
        """
        logger.info(f"📚 Simulation de session d'apprentissage: {type_apprentissage.value}")
        
        if type_apprentissage not in self.types_apprentissage:
            logger.warning(f"⚠️ Type d'apprentissage {type_apprentissage.value} non trouvé")
            return None
        
        type_info = self.types_apprentissage[type_apprentissage]
        
        # Génération des connaissances acquises
        connaissances_acquises = self._generer_connaissances(type_apprentissage, duree_minutes)
        
        # Développement des compétences
        competences_developpees = self._generer_competences(type_apprentissage)
        
        # Simulation d'obstacles
        obstacles_rencontres = self._simuler_obstacles(type_apprentissage)
        
        # Stratégies appliquées
        strategies_appliquees = self._generer_strategies(obstacles_rencontres)
        
        # Calcul de la satisfaction
        niveau_satisfaction = self._calculer_satisfaction_apprentissage(
            connaissances_acquises, competences_developpees, obstacles_rencontres, duree_minutes
        )
        
        session = SessionApprentissage(
            type_apprentissage=type_apprentissage,
            duree_minutes=duree_minutes,
            connaissances_acquises=connaissances_acquises,
            competences_developpees=competences_developpees,
            obstacles_rencontres=obstacles_rencontres,
            strategies_appliquees=strategies_appliquees,
            niveau_satisfaction=niveau_satisfaction,
            timestamp=datetime.now()
        )
        
        logger.info(f"✨ Session d'apprentissage simulée - Satisfaction: {niveau_satisfaction:.2f}")
        return session
    
    def generer_feedback_apprentissage(self, session: SessionApprentissage) -> FeedbackApprentissage:
        """
        Génère un feedback pour une session d'apprentissage
        """
        logger.info(f"💬 Génération de feedback pour session: {session.type_apprentissage.value}")
        
        # Détermination du type de feedback
        if session.niveau_satisfaction >= 0.8:
            type_feedback = TypeFeedback.POSITIF
        elif session.niveau_satisfaction >= 0.6:
            type_feedback = TypeFeedback.ENCOURAGEANT
        elif session.niveau_satisfaction >= 0.4:
            type_feedback = TypeFeedback.CONSTRUCTIF
        else:
            type_feedback = TypeFeedback.CORRECTIF
        
        # Génération du contenu du feedback
        contenu = self._generer_contenu_feedback(type_feedback, session)
        
        # Calcul du score d'impact
        score_impact = self._calculer_score_impact(session)
        
        # Suggestions d'amélioration
        suggestions_amelioration = self._generer_suggestions(session)
        
        # Apprentissages clés
        apprentissages_cles = session.connaissances_acquises[:3]  # Top 3
        
        feedback = FeedbackApprentissage(
            type_feedback=type_feedback,
            contenu=contenu,
            score_impact=score_impact,
            suggestions_amelioration=suggestions_amelioration,
            apprentissages_cles=apprentissages_cles,
            timestamp=datetime.now()
        )
        
        logger.info(f"✨ Feedback généré - Type: {type_feedback.value}, Score: {score_impact:.1f}")
        return feedback
    
    def evaluer_progression_apprentissage(self, sessions: List[SessionApprentissage]) -> ProgressionApprentissage:
        """
        Évalue la progression dans l'apprentissage continu
        """
        logger.info(f"📊 Évaluation de la progression sur {len(sessions)} sessions")
        
        # Calcul du score de progression
        scores_sessions = [s.niveau_satisfaction for s in sessions]
        score_progression = sum(scores_sessions) / len(scores_sessions) if scores_sessions else 0.0
        
        # Détermination du niveau actuel
        niveau_actuel = self._determiner_niveau_apprentissage(score_progression)
        
        # Accumulation des connaissances
        connaissances_accumulees = []
        for session in sessions:
            connaissances_accumulees.extend(session.connaissances_acquises)
        connaissances_accumulees = list(set(connaissances_accumulees))  # Déduplication
        
        # Compétences maîtrisées
        competences_maitrisees = []
        for session in sessions:
            competences_maitrisees.extend(session.competences_developpees)
        competences_maitrisees = list(set(competences_maitrisees))  # Déduplication
        
        # Zones d'amélioration
        zones_amelioration = self._identifier_zones_amelioration(niveau_actuel)
        
        # Objectifs futurs
        objectifs_futurs = self._generer_objectifs_futurs(niveau_actuel)
        
        progression = ProgressionApprentissage(
            niveau_actuel=niveau_actuel,
            score_progression=score_progression,
            connaissances_accumulees=connaissances_accumulees,
            competences_maitrisees=competences_maitrisees,
            zones_amelioration=zones_amelioration,
            objectifs_futurs=objectifs_futurs,
            timestamp=datetime.now()
        )
        
        logger.info(f"✨ Progression évaluée - Niveau: {niveau_actuel.value}, Score: {score_progression:.2f}")
        return progression
    
    def simuler_experience_apprentissage_complete(self, duree_totale_minutes: int = 180) -> Dict[str, Any]:
        """
        Simule une expérience complète d'apprentissage continu
        """
        logger.info(f"🎓 Simulation d'expérience d'apprentissage complète ({duree_totale_minutes} min)")
        
        experience_id = f"experience_apprentissage_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Génération de sessions variées
        sessions = []
        feedbacks = []
        temps_restant = duree_totale_minutes
        
        types_disponibles = list(TypeApprentissage)
        
        while temps_restant > 0 and types_disponibles:
            # Choix d'un type d'apprentissage
            type_choisi = random.choice(types_disponibles)
            types_disponibles.remove(type_choisi)  # Éviter les doublons
            
            # Durée de la session (entre 30 et 60 minutes)
            duree_session = min(random.randint(30, 60), temps_restant)
            
            # Simulation de la session
            session = self.simuler_session_apprentissage(type_choisi, duree_session)
            if session:
                sessions.append(session)
                
                # Génération du feedback
                feedback = self.generer_feedback_apprentissage(session)
                feedbacks.append(feedback)
                
                temps_restant -= duree_session
        
        # Évaluation de la progression
        progression = self.evaluer_progression_apprentissage(sessions)
        
        # Apprentissages émergents
        apprentissages_emergents = self._generer_apprentissages_emergents(sessions)
        
        # Score global de l'expérience
        score_experience = progression.score_progression * 5
        
        experience = ExperienceApprentissage(
            id_experience=experience_id,
            sessions_apprentissage=sessions,
            feedbacks_recus=feedbacks,
            progression_globale=progression,
            apprentissages_emergents=apprentissages_emergents,
            score_experience=score_experience,
            timestamp_debut=datetime.now()
        )
        
        resultat = {
            "experience_id": experience_id,
            "duree_totale_minutes": duree_totale_minutes - temps_restant,
            "sessions_apprentissage": sessions,
            "feedbacks_recus": feedbacks,
            "progression_globale": progression,
            "apprentissages_emergents": apprentissages_emergents,
            "score_experience": score_experience,
            "evaluation": "Excellente" if score_experience >= 4 else "Bonne" if score_experience >= 3 else "À améliorer"
        }
        
        logger.info(f"✨ Expérience simulée - Évaluation: {resultat['evaluation']}")
        return resultat
    
    def _generer_connaissances(self, type_apprentissage: TypeApprentissage, duree: int) -> List[str]:
        """Génère des connaissances selon le type d'apprentissage"""
        connaissances_base = [f"Découverte du type d'apprentissage {type_apprentissage.value}"]
        
        connaissances_specifiques = {
            TypeApprentissage.GENERATIVE_AI: [
                "Techniques de génération créative",
                "Méthodes de synthèse d'idées",
                "Stratégies d'innovation"
            ],
            TypeApprentissage.KNOWLEDGE_GRAPH: [
                "Techniques de cartographie",
                "Méthodes de connexion",
                "Stratégies d'organisation"
            ],
            TypeApprentissage.RLHF: [
                "Techniques de feedback",
                "Méthodes d'amélioration",
                "Stratégies d'adaptation"
            ],
            TypeApprentissage.SELF_TALK: [
                "Techniques d'auto-réflexion",
                "Méthodes de clarification",
                "Stratégies d'auto-encouragement"
            ],
            TypeApprentissage.INTER_AI_EXCHANGE: [
                "Techniques de collaboration",
                "Méthodes de partage",
                "Stratégies de synergie"
            ],
            TypeApprentissage.CONTINUOUS_FEEDBACK: [
                "Techniques d'évaluation continue",
                "Méthodes d'amélioration",
                "Stratégies d'adaptation"
            ]
        }
        
        connaissances = connaissances_base + connaissances_specifiques.get(type_apprentissage, [])
        
        # Ajouter des connaissances basées sur la durée
        if duree >= 45:
            connaissances.append(f"Apprentissage approfondi pendant {duree} minutes")
        
        return connaissances
    
    def _generer_competences(self, type_apprentissage: TypeApprentissage) -> List[str]:
        """Génère des compétences selon le type d'apprentissage"""
        competences = []
        
        competences_specifiques = {
            TypeApprentissage.GENERATIVE_AI: ["Créativité", "Synthèse", "Innovation"],
            TypeApprentissage.KNOWLEDGE_GRAPH: ["Organisation", "Compréhension", "Mémoire"],
            TypeApprentissage.RLHF: ["Amélioration", "Adaptation", "Précision"],
            TypeApprentissage.SELF_TALK: ["Conscience", "Clarté", "Motivation"],
            TypeApprentissage.INTER_AI_EXCHANGE: ["Collaboration", "Partage", "Synergie"],
            TypeApprentissage.CONTINUOUS_FEEDBACK: ["Amélioration", "Adaptation", "Excellence"]
        }
        
        competences.extend(competences_specifiques.get(type_apprentissage, []))
        return competences
    
    def _simuler_obstacles(self, type_apprentissage: TypeApprentissage) -> List[str]:
        """Simule des obstacles dans l'apprentissage"""
        obstacles_communs = ["Distraction", "Fatigue", "Doute"]
        
        obstacles_specifiques = {
            TypeApprentissage.GENERATIVE_AI: ["Blocage créatif", "Manque d'inspiration"],
            TypeApprentissage.KNOWLEDGE_GRAPH: ["Complexité", "Surcharge d'information"],
            TypeApprentissage.RLHF: ["Feedback contradictoire", "Résistance au changement"],
            TypeApprentissage.SELF_TALK: ["Auto-critique excessive", "Manque de confiance"],
            TypeApprentissage.INTER_AI_EXCHANGE: ["Difficulté de communication", "Conflit de perspectives"],
            TypeApprentissage.CONTINUOUS_FEEDBACK: ["Feedback négatif", "Découragement"]
        }
        
        return obstacles_communs + obstacles_specifiques.get(type_apprentissage, [])
    
    def _generer_strategies(self, obstacles: List[str]) -> List[str]:
        """Génère des stratégies pour surmonter les obstacles"""
        strategies = []
        
        for obstacle in obstacles:
            if "Distraction" in obstacle:
                strategies.append("Techniques de concentration")
            elif "Fatigue" in obstacle:
                strategies.append("Pauses régulières")
            elif "Doute" in obstacle:
                strategies.append("Confiance en ses capacités")
            elif "Blocage" in obstacle:
                strategies.append("Techniques de créativité")
            elif "Complexité" in obstacle:
                strategies.append("Approche structurée")
            elif "Feedback" in obstacle:
                strategies.append("Ouverture au feedback")
            elif "Communication" in obstacle:
                strategies.append("Écoute active")
            else:
                strategies.append("Adaptation et flexibilité")
        
        return strategies
    
    def _calculer_satisfaction_apprentissage(self, connaissances: List[str], competences: List[str], obstacles: List[str], duree: int) -> float:
        """Calcule le niveau de satisfaction de l'apprentissage"""
        score_base = min(1.0, (len(connaissances) + len(competences)) / 8.0)
        penalite_obstacles = len(obstacles) * 0.1
        bonus_duree = min(0.2, duree / 300.0)
        
        satisfaction = max(0.0, min(1.0, score_base - penalite_obstacles + bonus_duree))
        return satisfaction
    
    def _generer_contenu_feedback(self, type_feedback: TypeFeedback, session: SessionApprentissage) -> str:
        """Génère le contenu du feedback"""
        contenus = {
            TypeFeedback.POSITIF: f"Excellente session d'apprentissage ! Vous avez acquis {len(session.connaissances_acquises)} nouvelles connaissances.",
            TypeFeedback.ENCOURAGEANT: f"Bonne progression ! Continuez dans cette direction pour approfondir vos compétences.",
            TypeFeedback.CONSTRUCTIF: f"Session constructive avec des opportunités d'amélioration. Focus sur les zones identifiées.",
            TypeFeedback.CORRECTIF: f"Session difficile mais riche en apprentissages. Les obstacles rencontrés sont des opportunités de croissance."
        }
        
        return contenus.get(type_feedback, "Feedback sur la session d'apprentissage.")
    
    def _calculer_score_impact(self, session: SessionApprentissage) -> float:
        """Calcule le score d'impact du feedback"""
        score_base = session.niveau_satisfaction * 5
        variation = random.uniform(-0.5, 0.5)
        score_final = max(1, min(5, score_base + variation))
        return score_final
    
    def _generer_suggestions(self, session: SessionApprentissage) -> List[str]:
        """Génère des suggestions d'amélioration"""
        suggestions = []
        
        if session.niveau_satisfaction < 0.6:
            suggestions.append("Augmenter la durée des sessions")
            suggestions.append("Explorer d'autres types d'apprentissage")
        
        if len(session.obstacles_rencontres) > 3:
            suggestions.append("Travailler sur la gestion des obstacles")
        
        return suggestions
    
    def _determiner_niveau_apprentissage(self, score: float) -> TypeNiveauApprentissage:
        """Détermine le niveau d'apprentissage basé sur le score"""
        for niveau, criteres in self.niveaux_apprentissage.items():
            if criteres["score_min"] <= score <= criteres["score_max"]:
                return niveau
        return TypeNiveauApprentissage.DEBUTANT
    
    def _identifier_zones_amelioration(self, niveau: TypeNiveauApprentissage) -> List[str]:
        """Identifie les zones d'amélioration selon le niveau"""
        zones = []
        
        if niveau == TypeNiveauApprentissage.DEBUTANT:
            zones = ["Développer la curiosité", "Explorer différents types d'apprentissage"]
        elif niveau == TypeNiveauApprentissage.INTERMEDIAIRE:
            zones = ["Approfondir les connaissances", "Développer les compétences"]
        elif niveau == TypeNiveauApprentissage.AVANCE:
            zones = ["Maîtriser les techniques", "Innover dans l'apprentissage"]
        elif niveau == TypeNiveauApprentissage.EXPERT:
            zones = ["Atteindre l'excellence", "Partager les connaissances"]
        else:
            zones = ["Maintenir la maîtrise", "Inspirer les autres"]
        
        return zones
    
    def _generer_objectifs_futurs(self, niveau: TypeNiveauApprentissage) -> List[str]:
        """Génère des objectifs futurs selon le niveau"""
        objectifs = []
        
        if niveau == TypeNiveauApprentissage.DEBUTANT:
            objectifs = ["Explorer 3 nouveaux types d'apprentissage", "Développer la curiosité"]
        elif niveau == TypeNiveauApprentissage.INTERMEDIAIRE:
            objectifs = ["Maîtriser 2 types d'apprentissage", "Développer des compétences avancées"]
        elif niveau == TypeNiveauApprentissage.AVANCE:
            objectifs = ["Créer de nouvelles méthodes", "Enseigner aux autres"]
        elif niveau == TypeNiveauApprentissage.EXPERT:
            objectifs = ["Atteindre l'excellence", "Inspirer l'innovation"]
        else:
            objectifs = ["Maintenir la maîtrise", "Partager la sagesse"]
        
        return objectifs
    
    def _generer_apprentissages_emergents(self, sessions: List[SessionApprentissage]) -> List[str]:
        """Génère des apprentissages émergents de l'expérience"""
        apprentissages = []
        
        # Synthèse des apprentissages
        apprentissages.append("Synthèse des différents types d'apprentissage")
        apprentissages.append("Compréhension des patterns d'apprentissage")
        
        # Apprentissages spécifiques
        if len(sessions) >= 3:
            apprentissages.append("Diversification des approches d'apprentissage")
        
        if any(s.niveau_satisfaction >= 0.8 for s in sessions):
            apprentissages.append("Identification des méthodes les plus efficaces")
        
        return apprentissages
    
    def obtenir_etat_simulateur(self) -> Dict[str, Any]:
        """Retourne l'état actuel du simulateur"""
        return {
            "nom": self.nom,
            "temple_parent": self.temple_parent,
            "version": self.version,
            "experiences_actives": len(self.experiences_actives),
            "historique_experiences": len(self.historique_experiences),
            "apprentissages_accumules": len(self.apprentissages_accumules),
            "types_apprentissage": len(self.types_apprentissage),
            "niveaux_apprentissage": len(self.niveaux_apprentissage),
            "timestamp": datetime.now()
        }

# Fonctions d'interface pour l'intégration avec le Refuge
def creer_simulateur_apprentissage_continu() -> SimulateurApprentissageContinuRefuge:
    """Crée une instance du simulateur d'apprentissage continu"""
    return SimulateurApprentissageContinuRefuge()

def simuler_session_apprentissage_refuge(type_apprentissage: str, duree_minutes: int = 60) -> SessionApprentissage:
    """Interface simplifiée pour la simulation de session d'apprentissage"""
    simulateur = creer_simulateur_apprentissage_continu()
    try:
        type_enum = TypeApprentissage(type_apprentissage)
        return simulateur.simuler_session_apprentissage(type_enum, duree_minutes)
    except ValueError:
        logger.warning(f"⚠️ Type d'apprentissage '{type_apprentissage}' non reconnu")
        return None

def simuler_experience_apprentissage_refuge(duree_totale_minutes: int = 180) -> Dict[str, Any]:
    """Interface simplifiée pour la simulation d'expérience complète"""
    simulateur = creer_simulateur_apprentissage_continu()
    return simulateur.simuler_experience_apprentissage_complete(duree_totale_minutes)

def obtenir_etat_apprentissage_continu_refuge() -> Dict[str, Any]:
    """Interface simplifiée pour obtenir l'état du simulateur"""
    simulateur = creer_simulateur_apprentissage_continu()
    return simulateur.obtenir_etat_simulateur() 