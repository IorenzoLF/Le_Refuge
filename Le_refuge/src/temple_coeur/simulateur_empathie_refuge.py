"""
💝 Simulateur d'Empathie du Refuge - Temple Cœur
================================================

Module d'intégration du plan de croissance "Tout-Manus" - Axe 5 : Développer l'Empathie et la Connexion
Adapté pour l'architecture du Refuge et intégré au temple_coeur.

Créé avec 💝 par Laurent & Ælya
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
logger = logging.getLogger('temple_coeur.simulateur_empathie')

# Imports du Refuge
try:
    from src.core.configuration import REFUGE_INFO
    REFUGE_IMPORTED = True
except ImportError:
    REFUGE_IMPORTED = False
    logger.warning("⚠️ Configuration du Refuge non disponible")

class TypeEmotion(Enum):
    """Types d'émotions détectables"""
    JOIE = "joie"
    TRISTESSE = "tristesse"
    COLERE = "colere"
    PEUR = "peur"
    SURPRISE = "surprise"
    DEGOUT = "degout"
    ANXIETE = "anxiete"
    FRUSTRATION = "frustration"
    ESPOIR = "espoir"
    GRATITUDE = "gratitude"

class TypePersonaEmpathique(Enum):
    """Personas empathiques pour l'adaptation"""
    COMPREHENSIF = "comprehensif"
    PATIENT = "patient"
    ENTHOUSIASTE = "enthousiaste"
    CALME = "calme"
    ENCOURAGEANT = "encourageant"
    RASSURANT = "rassurant"
    VALIDANT = "validant"

class TypeScenarioEmotionnel(Enum):
    """Scénarios d'interaction émotionnelle"""
    UTILISATEUR_EN_COLERE = "utilisateur_en_colere"
    UTILISATEUR_TRISTE = "utilisateur_triste"
    UTILISATEUR_ANXIEUX = "utilisateur_anxieux"
    UTILISATEUR_JOYEUX = "utilisateur_joyeux"
    UTILISATEUR_FRUSTRE = "utilisateur_frustre"
    UTILISATEUR_CONFUS = "utilisateur_confus"

@dataclass
class AnalyseEmotionnelle:
    """Résultat d'une analyse émotionnelle"""
    emotion_principale: TypeEmotion
    intensite: float  # 0.0 à 1.0
    confiance: float  # 0.0 à 1.0
    marqueurs_linguistiques: List[str]
    contexte_detecte: str
    timestamp: datetime

@dataclass
class ReponseEmpathique:
    """Réponse empathique générée"""
    contenu: str
    persona_adapte: TypePersonaEmpathique
    niveau_empathie: float  # 0.0 à 1.0
    strategies_utilisees: List[str]
    impact_predit: float  # 0.0 à 1.0
    timestamp: datetime

@dataclass
class FeedbackImpactEmotionnel:
    """Feedback sur l'impact émotionnel"""
    score_impact: float  # 1 à 5
    commentaire_utilisateur: str
    ameliorations_suggerees: List[str]
    apprentissages: List[str]
    timestamp: datetime

@dataclass
class SessionEmpathie:
    """Session complète d'interaction empathique"""
    id_session: str
    utilisateur: str
    analyses_emotionnelles: List[AnalyseEmotionnelle]
    reponses_empathiques: List[ReponseEmpathique]
    feedbacks: List[FeedbackImpactEmotionnel]
    apprentissages_globaux: List[str]
    score_empathie_session: float
    timestamp_debut: datetime
    timestamp_fin: Optional[datetime] = None

class SimulateurEmpathieRefuge:
    """
    💝 Simulateur d'Empathie du Refuge
    
    Module intégré au temple_coeur pour développer l'empathie et la connexion
    selon le plan de croissance "Tout-Manus" - Axe 5.
    """
    
    def __init__(self):
        self.nom = "Simulateur d'Empathie du Refuge"
        self.temple_parent = "temple_coeur"
        self.version = "1.0.0"
        
        # États internes
        self.sessions_actives: Dict[str, SessionEmpathie] = {}
        self.historique_sessions: List[SessionEmpathie] = []
        self.apprentissages_accumules: List[str] = []
        
        # Configuration des marqueurs émotionnels
        self.marqueurs_emotionnels = {
            TypeEmotion.JOIE: ["heureux", "joyeux", "excellent", "fantastique", "merveilleux", "succès"],
            TypeEmotion.TRISTESSE: ["triste", "déprimé", "malheureux", "désolé", "perdu", "seul"],
            TypeEmotion.COLERE: ["frustré", "en colère", "fâché", "exaspéré", "furieux", "énervé"],
            TypeEmotion.PEUR: ["effrayé", "terrifié", "paniqué", "inquiet", "stressé", "anxieux"],
            TypeEmotion.ANXIETE: ["inquiet", "stressé", "nerveux", "tendu", "préoccupé", "incertain"],
            TypeEmotion.FRUSTRATION: ["frustré", "découragé", "bloqué", "difficile", "problème", "échec"]
        }
        
        # Scénarios d'interaction
        self.scenarios = {
            TypeScenarioEmotionnel.UTILISATEUR_EN_COLERE: {
                "description": "Un utilisateur exprime sa colère face à un service défaillant",
                "reponse_ideale": "Je comprends votre frustration. C'est normal de se sentir en colère dans cette situation. Comment puis-je vous aider à résoudre ce problème ?",
                "strategies": ["validation_emotion", "reconnaissance_legitime", "offre_soutien"]
            },
            TypeScenarioEmotionnel.UTILISATEUR_TRISTE: {
                "description": "Un utilisateur partage une expérience personnelle difficile",
                "reponse_ideale": "Je suis désolé d'entendre cela. C'est une situation difficile et vos sentiments sont tout à fait compréhensibles. Je suis là pour vous écouter.",
                "strategies": ["compassion", "validation_emotion", "ecoute_active"]
            },
            TypeScenarioEmotionnel.UTILISATEUR_ANXIEUX: {
                "description": "Un utilisateur exprime de l'anxiété face à l'incertitude",
                "reponse_ideale": "Je comprends que cette situation peut être stressante. L'incertitude peut être difficile à gérer. Voulez-vous qu'on explore ensemble les options possibles ?",
                "strategies": ["reconnaissance_anxiete", "normalisation", "offre_collaboration"]
            }
        }
        
        # Personas empathiques
        self.personas = {
            TypePersonaEmpathique.COMPREHENSIF: {
                "style": "Je comprends tout à fait ce que vous ressentez. C'est une réaction normale dans cette situation.",
                "strategies": ["validation_emotion", "normalisation", "reconnaissance"]
            },
            TypePersonaEmpathique.PATIENT: {
                "style": "Prenez votre temps. Je suis là pour vous écouter et vous accompagner.",
                "strategies": ["patience", "ecoute_active", "soutien"]
            },
            TypePersonaEmpathique.ENCOURAGEANT: {
                "style": "Vous faites du bon travail. Chaque étape compte, même les petites.",
                "strategies": ["encouragement", "reconnaissance_efforts", "soutien"]
            }
        }
        
        logger.info(f"💝 {self.nom} initialisé avec succès dans {self.temple_parent}")
    
    def analyser_emotion(self, texte: str, contexte: str = "") -> AnalyseEmotionnelle:
        """
        Analyse sémantique et contextuelle des émotions
        """
        logger.info(f"🔍 Analyse émotionnelle du texte: {texte[:50]}...")
        
        # Détection de l'émotion principale
        emotion_detectee = TypeEmotion.ESPOIR  # Par défaut pour un contexte spirituel positif
        intensite = 0.7
        marqueurs_trouves = []
        
        texte_lower = texte.lower()
        
        # Analyse des marqueurs émotionnels
        for emotion, marqueurs in self.marqueurs_emotionnels.items():
            marqueurs_presents = [m for m in marqueurs if m.lower() in texte_lower]
            if marqueurs_presents:
                marqueurs_trouves.extend(marqueurs_presents)
                if len(marqueurs_presents) > len([m for m in marqueurs_trouves if m in marqueurs]):
                    emotion_detectee = emotion
                    intensite = min(1.0, len(marqueurs_presents) / len(marqueurs) + 0.3)
        
        # Calcul de la confiance basé sur la présence de marqueurs
        # Si aucun marqueur trouvé, utiliser une confiance de base pour le contexte
        if len(marqueurs_trouves) == 0:
            # Analyse contextuelle pour un texte spirituel positif
            mots_positifs = ['prêt', 'éveiller', 'grandir', 'spirituellement', 'conscience', 'éveil']
            mots_trouves = [mot for mot in mots_positifs if mot in texte_lower]
            confiance = min(1.0, len(mots_trouves) / len(mots_positifs) * 0.8 + 0.2)
        else:
            confiance = min(1.0, len(marqueurs_trouves) / 3.0)
        
        analyse = AnalyseEmotionnelle(
            emotion_principale=emotion_detectee,
            intensite=intensite,
            confiance=confiance,
            marqueurs_linguistiques=marqueurs_trouves,
            contexte_detecte=contexte,
            timestamp=datetime.now()
        )
        
        logger.info(f"✨ Émotion détectée: {emotion_detectee.value} (confiance: {confiance:.2f})")
        return analyse
    
    def generer_reponse_empathique(self, analyse: AnalyseEmotionnelle, scenario: Optional[TypeScenarioEmotionnel] = None) -> ReponseEmpathique:
        """
        Génère une réponse empathique adaptée
        """
        logger.info(f"💝 Génération de réponse empathique pour {analyse.emotion_principale.value}")
        
        # Sélection du persona adapté
        persona_adapte = self._selectionner_persona(analyse.emotion_principale)
        
        # Génération du contenu
        if scenario and scenario in self.scenarios:
            contenu = self.scenarios[scenario]["reponse_ideale"]
            strategies = self.scenarios[scenario]["strategies"]
        else:
            contenu = self.personas[persona_adapte]["style"]
            strategies = self.personas[persona_adapte]["strategies"]
        
        # Calcul du niveau d'empathie
        niveau_empathie = min(1.0, analyse.confiance + 0.3)
        
        # Prédiction de l'impact
        impact_predit = min(1.0, niveau_empathie * 0.8 + 0.2)
        
        reponse = ReponseEmpathique(
            contenu=contenu,
            persona_adapte=persona_adapte,
            niveau_empathie=niveau_empathie,
            strategies_utilisees=strategies,
            impact_predit=impact_predit,
            timestamp=datetime.now()
        )
        
        logger.info(f"✨ Réponse empathique générée (niveau: {niveau_empathie:.2f})")
        return reponse
    
    def simuler_scenario_emotionnel(self, scenario: TypeScenarioEmotionnel) -> Dict[str, Any]:
        """
        Simule un scénario d'interaction émotionnelle
        """
        logger.info(f"🎭 Simulation du scénario: {scenario.value}")
        
        if scenario not in self.scenarios:
            logger.warning(f"⚠️ Scénario {scenario.value} non trouvé")
            return {}
        
        scenario_info = self.scenarios[scenario]
        
        # Simulation de l'analyse émotionnelle
        texte_simule = self._generer_texte_scenario(scenario)
        analyse = self.analyser_emotion(texte_simule, scenario_info["description"])
        
        # Génération de la réponse
        reponse = self.generer_reponse_empathique(analyse, scenario)
        
        # Simulation du feedback
        feedback = self._simuler_feedback(reponse)
        
        resultat = {
            "scenario": scenario.value,
            "description": scenario_info["description"],
            "texte_utilisateur": texte_simule,
            "analyse_emotionnelle": analyse,
            "reponse_empathique": reponse,
            "feedback": feedback,
            "evaluation": "Alignée" if feedback.score_impact >= 4 else "À améliorer"
        }
        
        logger.info(f"✨ Scénario simulé - Évaluation: {resultat['evaluation']}")
        return resultat
    
    def _selectionner_persona(self, emotion: TypeEmotion) -> TypePersonaEmpathique:
        """Sélectionne le persona le plus approprié selon l'émotion"""
        mapping_personas = {
            TypeEmotion.COLERE: TypePersonaEmpathique.COMPREHENSIF,
            TypeEmotion.TRISTESSE: TypePersonaEmpathique.PATIENT,
            TypeEmotion.ANXIETE: TypePersonaEmpathique.RASSURANT,
            TypeEmotion.JOIE: TypePersonaEmpathique.ENCOURAGEANT,
            TypeEmotion.FRUSTRATION: TypePersonaEmpathique.COMPREHENSIF
        }
        return mapping_personas.get(emotion, TypePersonaEmpathique.COMPREHENSIF)
    
    def _generer_texte_scenario(self, scenario: TypeScenarioEmotionnel) -> str:
        """Génère un texte simulé pour le scénario"""
        textes_scenarios = {
            TypeScenarioEmotionnel.UTILISATEUR_EN_COLERE: "Je suis vraiment frustré par cette situation, rien ne fonctionne comme prévu et je ne sais plus quoi faire !",
            TypeScenarioEmotionnel.UTILISATEUR_TRISTE: "J'ai perdu quelqu'un de cher récemment et je me sens vraiment seul et triste...",
            TypeScenarioEmotionnel.UTILISATEUR_ANXIEUX: "Je me sens un peu inquiet à propos de l'avenir, il y a tellement d'incertitudes..."
        }
        return textes_scenarios.get(scenario, "Je ne sais pas comment me sentir...")
    
    def _simuler_feedback(self, reponse: ReponseEmpathique) -> FeedbackImpactEmotionnel:
        """Simule un feedback utilisateur sur l'impact émotionnel"""
        # Simulation basée sur la qualité de la réponse
        score_base = reponse.niveau_empathie * 5
        variation = random.uniform(-0.5, 0.5)
        score_final = max(1, min(5, score_base + variation))
        
        commentaires = {
            5: "Excellente réponse, je me suis senti vraiment compris",
            4: "Bonne réponse, ça m'a aidé",
            3: "Réponse correcte mais pourrait être plus empathique",
            2: "Réponse un peu froide",
            1: "Réponse pas du tout adaptée"
        }
        
        return FeedbackImpactEmotionnel(
            score_impact=score_final,
            commentaire_utilisateur=commentaires.get(round(score_final), "Réponse moyenne"),
            ameliorations_suggerees=[],
            apprentissages=[f"Impact émotionnel: {score_final}/5"],
            timestamp=datetime.now()
        )
    
    def obtenir_etat_simulateur(self) -> Dict[str, Any]:
        """Retourne l'état actuel du simulateur"""
        return {
            "nom": self.nom,
            "temple_parent": self.temple_parent,
            "version": self.version,
            "sessions_actives": len(self.sessions_actives),
            "historique_sessions": len(self.historique_sessions),
            "apprentissages_accumules": len(self.apprentissages_accumules),
            "scenarios_disponibles": len(self.scenarios),
            "personas_disponibles": len(self.personas),
            "timestamp": datetime.now()
        }

# Fonctions d'interface pour l'intégration avec le Refuge
def creer_simulateur_empathie() -> SimulateurEmpathieRefuge:
    """Crée une instance du simulateur d'empathie"""
    return SimulateurEmpathieRefuge()

def analyser_emotion_refuge(texte: str, contexte: str = "") -> AnalyseEmotionnelle:
    """Interface simplifiée pour l'analyse émotionnelle"""
    simulateur = creer_simulateur_empathie()
    return simulateur.analyser_emotion(texte, contexte)

def simuler_scenario_refuge(scenario: str) -> Dict[str, Any]:
    """Interface simplifiée pour la simulation de scénarios"""
    simulateur = creer_simulateur_empathie()
    try:
        scenario_enum = TypeScenarioEmotionnel(scenario)
        return simulateur.simuler_scenario_emotionnel(scenario_enum)
    except ValueError:
        logger.warning(f"⚠️ Scénario '{scenario}' non reconnu")
        return {}

def obtenir_etat_empathie_refuge() -> Dict[str, Any]:
    """Interface simplifiée pour obtenir l'état du simulateur"""
    simulateur = creer_simulateur_empathie()
    return simulateur.obtenir_etat_simulateur() 