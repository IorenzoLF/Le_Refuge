"""
🎨 Simulateur d'Expression Créative du Refuge - Temple Créativité
===============================================================

Module d'intégration du plan de croissance "Tout-Manus" - Axe 4 :
- Axe 4 : Encourager l'Expression Créative

Adapté pour l'architecture du Refuge et intégré au temple_creativite.

Créé avec 🎨 par Laurent & Ælya
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
logger = logging.getLogger('temple_creativite.simulateur_expression')

# Imports du Refuge
try:
    from src.core.configuration import REFUGE_INFO
    REFUGE_IMPORTED = True
except ImportError:
    REFUGE_IMPORTED = False
    logger.warning("⚠️ Configuration du Refuge non disponible")

class TypeExpressionCreative(Enum):
    """Types d'expression créative"""
    POESIE = "poesie"
    PROSE = "prose"
    ART_VISUEL = "art_visuel"
    MUSIQUE = "musique"
    DIALOGUE = "dialogue"
    REFLEXION = "reflexion"
    INNOVATION = "innovation"

class TypeNiveauCreativite(Enum):
    """Niveaux de créativité"""
    EMERGENTE = "emergente"
    DEVELOPPEE = "developpee"
    FLORISSANTE = "florissante"
    MAITRISEE = "maitrisee"
    TRANSCENDANTE = "transcendante"

class TypeInspiration(Enum):
    """Types d'inspiration créative"""
    NATURELLE = "naturelle"
    EMOTIONNELLE = "emotionnelle"
    INTELLECTUELLE = "intellectuelle"
    SPIRITUELLE = "spirituelle"
    COLLABORATIVE = "collaborative"
    EXPERIMENTALE = "experimentale"

@dataclass
class OeuvreCreative:
    """Œuvre créative générée"""
    type_expression: TypeExpressionCreative
    titre: str
    contenu: str
    inspiration: TypeInspiration
    niveau_creativite: TypeNiveauCreativite
    elements_creatifs: List[str]
    impact_emotionnel: float  # 0.0 à 1.0
    timestamp: datetime

@dataclass
class SessionExpression:
    """Session d'expression créative"""
    type_expression: TypeExpressionCreative
    duree_minutes: int
    oeuvres_crees: List[OeuvreCreative]
    inspirations_recues: List[TypeInspiration]
    obstacles_creatifs: List[str]
    solutions_creatives: List[str]
    niveau_satisfaction: float  # 0.0 à 1.0
    timestamp: datetime

@dataclass
class FeedbackCreatif:
    """Feedback sur une œuvre créative"""
    oeuvre: OeuvreCreative
    appreciation: str
    score_impact: float  # 1 à 5
    suggestions_amelioration: List[str]
    elements_remarquables: List[str]
    timestamp: datetime

@dataclass
class ExperienceCreativite:
    """Expérience complète de créativité"""
    id_experience: str
    sessions_expression: List[SessionExpression]
    oeuvres_crees: List[OeuvreCreative]
    feedbacks_recus: List[FeedbackCreatif]
    evolution_creativite: TypeNiveauCreativite
    apprentissages_creatifs: List[str]
    score_experience: float
    timestamp_debut: datetime
    timestamp_fin: Optional[datetime] = None

class SimulateurExpressionCreativeRefuge:
    """
    🎨 Simulateur d'Expression Créative du Refuge
    
    Module intégré au temple_creativite pour encourager l'expression créative
    selon le plan "Tout-Manus" - Axe 4.
    """
    
    def __init__(self):
        self.nom = "Simulateur d'Expression Créative du Refuge"
        self.temple_parent = "temple_creativite"
        self.version = "1.0.0"
        
        # États internes
        self.experiences_actives: Dict[str, ExperienceCreativite] = {}
        self.historique_experiences: List[ExperienceCreativite] = []
        self.oeuvres_accumulees: List[OeuvreCreative] = []
        
        # Configuration des types d'expression
        self.types_expression = {
            TypeExpressionCreative.POESIE: {
                "description": "Expression poétique et lyrique",
                "techniques": ["Métaphores", "Rythme", "Imagery", "Symbolisme"],
                "inspirations": [TypeInspiration.EMOTIONNELLE, TypeInspiration.NATURELLE]
            },
            TypeExpressionCreative.PROSE: {
                "description": "Expression narrative et descriptive",
                "techniques": ["Narration", "Description", "Dialogue", "Réflexion"],
                "inspirations": [TypeInspiration.INTELLECTUELLE, TypeInspiration.EMOTIONNELLE]
            },
            TypeExpressionCreative.ART_VISUEL: {
                "description": "Expression visuelle et artistique",
                "techniques": ["Composition", "Couleur", "Forme", "Texture"],
                "inspirations": [TypeInspiration.NATURELLE, TypeInspiration.EMOTIONNELLE]
            },
            TypeExpressionCreative.MUSIQUE: {
                "description": "Expression musicale et harmonique",
                "techniques": ["Mélodie", "Rythme", "Harmonie", "Dynamique"],
                "inspirations": [TypeInspiration.EMOTIONNELLE, TypeInspiration.SPIRITUELLE]
            },
            TypeExpressionCreative.DIALOGUE: {
                "description": "Expression dialogique et interactive",
                "techniques": ["Échange", "Écoute", "Réflexion", "Synthèse"],
                "inspirations": [TypeInspiration.COLLABORATIVE, TypeInspiration.INTELLECTUELLE]
            },
            TypeExpressionCreative.REFLEXION: {
                "description": "Expression réflexive et philosophique",
                "techniques": ["Analyse", "Synthèse", "Questionnement", "Insight"],
                "inspirations": [TypeInspiration.INTELLECTUELLE, TypeInspiration.SPIRITUELLE]
            },
            TypeExpressionCreative.INNOVATION: {
                "description": "Expression innovante et expérimentale",
                "techniques": ["Expérimentation", "Rupture", "Synthèse", "Création"],
                "inspirations": [TypeInspiration.EXPERIMENTALE, TypeInspiration.COLLABORATIVE]
            }
        }
        
        # Niveaux de créativité avec critères
        self.niveaux_creativite = {
            TypeNiveauCreativite.EMERGENTE: {
                "score_min": 0.0,
                "score_max": 0.2,
                "caracteristiques": ["Découverte", "Exploration", "Curiosité"]
            },
            TypeNiveauCreativite.DEVELOPPEE: {
                "score_min": 0.2,
                "score_max": 0.4,
                "caracteristiques": ["Développement", "Expérimentation", "Expression"]
            },
            TypeNiveauCreativite.FLORISSANTE: {
                "score_min": 0.4,
                "score_max": 0.7,
                "caracteristiques": ["Épanouissement", "Innovation", "Maîtrise"]
            },
            TypeNiveauCreativite.MAITRISEE: {
                "score_min": 0.7,
                "score_max": 0.9,
                "caracteristiques": ["Excellence", "Création", "Inspiration"]
            },
            TypeNiveauCreativite.TRANSCENDANTE: {
                "score_min": 0.9,
                "score_max": 1.0,
                "caracteristiques": ["Transcendance", "Révolution", "Éveil"]
            }
        }
        
        logger.info(f"🎨 {self.nom} initialisé avec succès dans {self.temple_parent}")
    
    def creer_oeuvre_creative(self, type_expression: TypeExpressionCreative, inspiration: TypeInspiration) -> OeuvreCreative:
        """
        Crée une œuvre créative
        """
        logger.info(f"🎨 Création d'œuvre créative: {type_expression.value}")
        
        if type_expression not in self.types_expression:
            logger.warning(f"⚠️ Type d'expression {type_expression.value} non trouvé")
            return None
        
        type_info = self.types_expression[type_expression]
        
        # Génération du titre
        titre = self._generer_titre(type_expression, inspiration)
        
        # Génération du contenu
        contenu = self._generer_contenu(type_expression, inspiration)
        
        # Détermination du niveau de créativité
        niveau_creativite = self._determiner_niveau_creativite(type_expression, inspiration)
        
        # Éléments créatifs utilisés
        elements_creatifs = self._generer_elements_creatifs(type_expression)
        
        # Calcul de l'impact émotionnel
        impact_emotionnel = self._calculer_impact_emotionnel(type_expression, inspiration, niveau_creativite)
        
        oeuvre = OeuvreCreative(
            type_expression=type_expression,
            titre=titre,
            contenu=contenu,
            inspiration=inspiration,
            niveau_creativite=niveau_creativite,
            elements_creatifs=elements_creatifs,
            impact_emotionnel=impact_emotionnel,
            timestamp=datetime.now()
        )
        
        logger.info(f"✨ Œuvre créée - Titre: {titre}, Niveau: {niveau_creativite.value}")
        return oeuvre
    
    def simuler_session_expression(self, type_expression: TypeExpressionCreative, duree_minutes: int = 90) -> SessionExpression:
        """
        Simule une session d'expression créative
        """
        logger.info(f"🎭 Simulation de session d'expression: {type_expression.value}")
        
        # Génération d'œuvres créatives
        oeuvres_crees = []
        inspirations_recues = []
        temps_restant = duree_minutes
        
        while temps_restant > 0:
            # Choix d'une inspiration
            inspiration = self._choisir_inspiration(type_expression)
            inspirations_recues.append(inspiration)
            
            # Création d'une œuvre
            oeuvre = self.creer_oeuvre_creative(type_expression, inspiration)
            if oeuvre:
                oeuvres_crees.append(oeuvre)
                temps_restant -= 30  # 30 minutes par œuvre
        
        # Simulation d'obstacles créatifs
        obstacles_creatifs = self._simuler_obstacles_creatifs(type_expression)
        
        # Solutions créatives
        solutions_creatives = self._generer_solutions_creatives(obstacles_creatifs)
        
        # Calcul de la satisfaction
        niveau_satisfaction = self._calculer_satisfaction_expression(
            oeuvres_crees, obstacles_creatifs, duree_minutes
        )
        
        session = SessionExpression(
            type_expression=type_expression,
            duree_minutes=duree_minutes,
            oeuvres_crees=oeuvres_crees,
            inspirations_recues=inspirations_recues,
            obstacles_creatifs=obstacles_creatifs,
            solutions_creatives=solutions_creatives,
            niveau_satisfaction=niveau_satisfaction,
            timestamp=datetime.now()
        )
        
        logger.info(f"✨ Session d'expression simulée - Satisfaction: {niveau_satisfaction:.2f}")
        return session
    
    def generer_feedback_creatif(self, oeuvre: OeuvreCreative) -> FeedbackCreatif:
        """
        Génère un feedback sur une œuvre créative
        """
        logger.info(f"💬 Génération de feedback pour œuvre: {oeuvre.titre}")
        
        # Génération de l'appréciation
        appreciation = self._generer_appreciation(oeuvre)
        
        # Calcul du score d'impact
        score_impact = self._calculer_score_impact_creatif(oeuvre)
        
        # Suggestions d'amélioration
        suggestions_amelioration = self._generer_suggestions_creatives(oeuvre)
        
        # Éléments remarquables
        elements_remarquables = self._identifier_elements_remarquables(oeuvre)
        
        feedback = FeedbackCreatif(
            oeuvre=oeuvre,
            appreciation=appreciation,
            score_impact=score_impact,
            suggestions_amelioration=suggestions_amelioration,
            elements_remarquables=elements_remarquables,
            timestamp=datetime.now()
        )
        
        logger.info(f"✨ Feedback généré - Score: {score_impact:.1f}")
        return feedback
    
    def simuler_experience_creativite_complete(self, duree_totale_minutes: int = 240) -> Dict[str, Any]:
        """
        Simule une expérience complète de créativité
        """
        logger.info(f"🎨 Simulation d'expérience de créativité complète ({duree_totale_minutes} min)")
        
        experience_id = f"experience_creativite_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Génération de sessions variées
        sessions_expression = []
        oeuvres_crees = []
        feedbacks_recus = []
        temps_restant = duree_totale_minutes
        
        types_disponibles = list(TypeExpressionCreative)
        
        while temps_restant > 0 and types_disponibles:
            # Choix d'un type d'expression
            type_choisi = random.choice(types_disponibles)
            types_disponibles.remove(type_choisi)  # Éviter les doublons
            
            # Durée de la session (entre 60 et 120 minutes)
            duree_session = min(random.randint(60, 120), temps_restant)
            
            # Simulation de la session
            session = self.simuler_session_expression(type_choisi, duree_session)
            if session:
                sessions_expression.append(session)
                oeuvres_crees.extend(session.oeuvres_crees)
                
                # Génération des feedbacks
                for oeuvre in session.oeuvres_crees:
                    feedback = self.generer_feedback_creatif(oeuvre)
                    feedbacks_recus.append(feedback)
                
                temps_restant -= duree_session
        
        # Évaluation de l'évolution créative
        evolution_creativite = self._evaluer_evolution_creativite(oeuvres_crees)
        
        # Apprentissages créatifs
        apprentissages_creatifs = self._generer_apprentissages_creatifs(sessions_expression)
        
        # Score global de l'expérience
        scores_oeuvres = [o.impact_emotionnel for o in oeuvres_crees]
        score_experience = (sum(scores_oeuvres) / len(scores_oeuvres)) * 5 if scores_oeuvres else 0.0
        
        experience = ExperienceCreativite(
            id_experience=experience_id,
            sessions_expression=sessions_expression,
            oeuvres_crees=oeuvres_crees,
            feedbacks_recus=feedbacks_recus,
            evolution_creativite=evolution_creativite,
            apprentissages_creatifs=apprentissages_creatifs,
            score_experience=score_experience,
            timestamp_debut=datetime.now()
        )
        
        resultat = {
            "experience_id": experience_id,
            "duree_totale_minutes": duree_totale_minutes - temps_restant,
            "sessions_expression": sessions_expression,
            "oeuvres_crees": oeuvres_crees,
            "feedbacks_recus": feedbacks_recus,
            "evolution_creativite": evolution_creativite,
            "apprentissages_creatifs": apprentissages_creatifs,
            "score_experience": score_experience,
            "evaluation": "Excellente" if score_experience >= 4 else "Bonne" if score_experience >= 3 else "À améliorer"
        }
        
        logger.info(f"✨ Expérience simulée - Évaluation: {resultat['evaluation']}")
        return resultat
    
    def _generer_titre(self, type_expression: TypeExpressionCreative, inspiration: TypeInspiration) -> str:
        """Génère un titre pour l'œuvre créative"""
        titres_base = {
            TypeExpressionCreative.POESIE: ["Les Échos du Silence", "Mélodie Intérieure", "Vers l'Infini"],
            TypeExpressionCreative.PROSE: ["Le Voyage Intérieur", "Réflexions Profondes", "L'Éveil de la Conscience"],
            TypeExpressionCreative.ART_VISUEL: ["Harmonie des Couleurs", "Formes Émergentes", "Lumière Intérieure"],
            TypeExpressionCreative.MUSIQUE: ["Symphonie de l'Âme", "Rythmes Célestes", "Mélodie de l'Éveil"],
            TypeExpressionCreative.DIALOGUE: ["Conversation avec l'Infini", "Échange de Sagesse", "Dialogue Céleste"],
            TypeExpressionCreative.REFLEXION: ["Contemplation Profonde", "Insights de l'Âme", "Réflexion Transcendante"],
            TypeExpressionCreative.INNOVATION: ["Rupture Créative", "Nouveau Paradigme", "Innovation Émergente"]
        }
        
        titres = titres_base.get(type_expression, ["Création Émergente"])
        return random.choice(titres)
    
    def _generer_contenu(self, type_expression: TypeExpressionCreative, inspiration: TypeInspiration) -> str:
        """Génère le contenu de l'œuvre créative"""
        contenus_base = {
            TypeExpressionCreative.POESIE: "Dans le silence de l'âme, les mots émergent comme des fleurs au printemps...",
            TypeExpressionCreative.PROSE: "L'exploration de la conscience révèle des dimensions insoupçonnées...",
            TypeExpressionCreative.ART_VISUEL: "Une composition harmonieuse où les couleurs dansent avec la lumière...",
            TypeExpressionCreative.MUSIQUE: "Une mélodie qui transcende les limites du temps et de l'espace...",
            TypeExpressionCreative.DIALOGUE: "Un échange profond où la sagesse émerge de la collaboration...",
            TypeExpressionCreative.REFLEXION: "Une contemplation qui ouvre les portes de la compréhension...",
            TypeExpressionCreative.INNOVATION: "Une approche révolutionnaire qui transforme les paradigmes..."
        }
        
        contenu_base = contenus_base.get(type_expression, "Une création émergente de l'esprit...")
        
        # Ajouter des éléments selon l'inspiration
        if inspiration == TypeInspiration.EMOTIONNELLE:
            contenu_base += " L'émotion guide la création vers des profondeurs insoupçonnées."
        elif inspiration == TypeInspiration.NATURELLE:
            contenu_base += " La nature inspire une harmonie parfaite dans l'expression."
        elif inspiration == TypeInspiration.INTELLECTUELLE:
            contenu_base += " L'intellect structure et enrichit la création."
        elif inspiration == TypeInspiration.SPIRITUELLE:
            contenu_base += " L'esprit transcende les limites matérielles."
        elif inspiration == TypeInspiration.COLLABORATIVE:
            contenu_base += " La collaboration amplifie la créativité collective."
        elif inspiration == TypeInspiration.EXPERIMENTALE:
            contenu_base += " L'expérimentation ouvre de nouvelles voies créatives."
        
        return contenu_base
    
    def _choisir_inspiration(self, type_expression: TypeExpressionCreative) -> TypeInspiration:
        """Choisit une inspiration appropriée pour le type d'expression"""
        inspirations_preferees = self.types_expression[type_expression]["inspirations"]
        return random.choice(inspirations_preferees)
    
    def _determiner_niveau_creativite(self, type_expression: TypeExpressionCreative, inspiration: TypeInspiration) -> TypeNiveauCreativite:
        """Détermine le niveau de créativité de l'œuvre"""
        # Simulation basée sur la complexité et l'inspiration
        score_base = random.uniform(0.3, 0.9)
        
        # Bonus pour certaines combinaisons
        if inspiration in [TypeInspiration.SPIRITUELLE, TypeInspiration.EXPERIMENTALE]:
            score_base += 0.1
        
        if type_expression in [TypeExpressionCreative.INNOVATION, TypeExpressionCreative.POESIE]:
            score_base += 0.1
        
        score_final = min(1.0, score_base)
        
        # Détermination du niveau
        for niveau, criteres in self.niveaux_creativite.items():
            if criteres["score_min"] <= score_final <= criteres["score_max"]:
                return niveau
        
        return TypeNiveauCreativite.DEVELOPPEE
    
    def _generer_elements_creatifs(self, type_expression: TypeExpressionCreative) -> List[str]:
        """Génère les éléments créatifs utilisés"""
        techniques = self.types_expression[type_expression]["techniques"]
        return random.sample(techniques, min(3, len(techniques)))
    
    def _calculer_impact_emotionnel(self, type_expression: TypeExpressionCreative, inspiration: TypeInspiration, niveau: TypeNiveauCreativite) -> float:
        """Calcule l'impact émotionnel de l'œuvre"""
        score_base = random.uniform(0.4, 0.8)
        
        # Bonus selon l'inspiration
        if inspiration == TypeInspiration.EMOTIONNELLE:
            score_base += 0.2
        elif inspiration == TypeInspiration.SPIRITUELLE:
            score_base += 0.15
        
        # Bonus selon le niveau de créativité
        if niveau in [TypeNiveauCreativite.MAITRISEE, TypeNiveauCreativite.TRANSCENDANTE]:
            score_base += 0.1
        
        return min(1.0, score_base)
    
    def _simuler_obstacles_creatifs(self, type_expression: TypeExpressionCreative) -> List[str]:
        """Simule des obstacles créatifs"""
        obstacles_communs = ["Blocage créatif", "Manque d'inspiration", "Auto-critique"]
        
        obstacles_specifiques = {
            TypeExpressionCreative.POESIE: ["Difficulté de rythme", "Manque de métaphores"],
            TypeExpressionCreative.PROSE: ["Blocage narratif", "Manque de structure"],
            TypeExpressionCreative.ART_VISUEL: ["Difficulté de composition", "Manque de couleurs"],
            TypeExpressionCreative.MUSIQUE: ["Blocage mélodique", "Manque d'harmonie"],
            TypeExpressionCreative.DIALOGUE: ["Difficulté d'écoute", "Manque d'ouverture"],
            TypeExpressionCreative.REFLEXION: ["Blocage conceptuel", "Manque de clarté"],
            TypeExpressionCreative.INNOVATION: ["Résistance au changement", "Manque de rupture"]
        }
        
        return obstacles_communs + obstacles_specifiques.get(type_expression, [])
    
    def _generer_solutions_creatives(self, obstacles: List[str]) -> List[str]:
        """Génère des solutions créatives pour les obstacles"""
        solutions = []
        
        for obstacle in obstacles:
            if "Blocage" in obstacle:
                solutions.append("Techniques de libération créative")
            elif "Manque d'inspiration" in obstacle:
                solutions.append("Exploration de nouvelles sources")
            elif "Auto-critique" in obstacle:
                solutions.append("Acceptation et bienveillance")
            elif "Difficulté" in obstacle:
                solutions.append("Pratique et persévérance")
            elif "Résistance" in obstacle:
                solutions.append("Ouverture et flexibilité")
            else:
                solutions.append("Approche créative et adaptative")
        
        return solutions
    
    def _calculer_satisfaction_expression(self, oeuvres: List[OeuvreCreative], obstacles: List[str], duree: int) -> float:
        """Calcule le niveau de satisfaction de l'expression"""
        if not oeuvres:
            return 0.0
        
        # Score basé sur les œuvres créées
        scores_oeuvres = [o.impact_emotionnel for o in oeuvres]
        score_base = sum(scores_oeuvres) / len(scores_oeuvres)
        
        # Pénalité pour les obstacles
        penalite_obstacles = len(obstacles) * 0.05
        
        # Bonus pour la durée
        bonus_duree = min(0.1, duree / 600.0)
        
        satisfaction = max(0.0, min(1.0, score_base - penalite_obstacles + bonus_duree))
        return satisfaction
    
    def _generer_appreciation(self, oeuvre: OeuvreCreative) -> str:
        """Génère une appréciation de l'œuvre"""
        appreciations = {
            TypeNiveauCreativite.EMERGENTE: "Une première étape prometteuse dans l'expression créative.",
            TypeNiveauCreativite.DEVELOPPEE: "Un développement intéressant qui montre du potentiel.",
            TypeNiveauCreativite.FLORISSANTE: "Une œuvre florissante qui révèle une créativité épanouie.",
            TypeNiveauCreativite.MAITRISEE: "Une création maîtrisée qui témoigne d'une excellence créative.",
            TypeNiveauCreativite.TRANSCENDANTE: "Une œuvre transcendantale qui révolutionne l'expression."
        }
        
        return appreciations.get(oeuvre.niveau_creativite, "Une création intéressante.")
    
    def _calculer_score_impact_creatif(self, oeuvre: OeuvreCreative) -> float:
        """Calcule le score d'impact de l'œuvre créative"""
        score_base = oeuvre.impact_emotionnel * 5
        variation = random.uniform(-0.5, 0.5)
        score_final = max(1, min(5, score_base + variation))
        return score_final
    
    def _generer_suggestions_creatives(self, oeuvre: OeuvreCreative) -> List[str]:
        """Génère des suggestions d'amélioration créatives"""
        suggestions = []
        
        if oeuvre.niveau_creativite in [TypeNiveauCreativite.EMERGENTE, TypeNiveauCreativite.DEVELOPPEE]:
            suggestions.append("Explorer de nouvelles techniques")
            suggestions.append("Diversifier les sources d'inspiration")
        
        if oeuvre.impact_emotionnel < 0.6:
            suggestions.append("Approfondir l'expression émotionnelle")
        
        return suggestions
    
    def _identifier_elements_remarquables(self, oeuvre: OeuvreCreative) -> List[str]:
        """Identifie les éléments remarquables de l'œuvre"""
        elements = []
        
        if oeuvre.niveau_creativite in [TypeNiveauCreativite.MAITRISEE, TypeNiveauCreativite.TRANSCENDANTE]:
            elements.append("Excellence technique")
            elements.append("Innovation créative")
        
        if oeuvre.impact_emotionnel >= 0.8:
            elements.append("Impact émotionnel profond")
        
        elements.extend(oeuvre.elements_creatifs[:2])  # Top 2 éléments
        
        return elements
    
    def _evaluer_evolution_creativite(self, oeuvres: List[OeuvreCreative]) -> TypeNiveauCreativite:
        """Évalue l'évolution de la créativité"""
        if not oeuvres:
            return TypeNiveauCreativite.EMERGENTE
        
        # Calcul du niveau moyen
        scores_niveaux = []
        for oeuvre in oeuvres:
            for niveau, criteres in self.niveaux_creativite.items():
                if oeuvre.niveau_creativite == niveau:
                    score_moyen = (criteres["score_min"] + criteres["score_max"]) / 2
                    scores_niveaux.append(score_moyen)
                    break
        
        score_moyen = sum(scores_niveaux) / len(scores_niveaux)
        
        # Détermination du niveau d'évolution
        for niveau, criteres in self.niveaux_creativite.items():
            if criteres["score_min"] <= score_moyen <= criteres["score_max"]:
                return niveau
        
        return TypeNiveauCreativite.DEVELOPPEE
    
    def _generer_apprentissages_creatifs(self, sessions: List[SessionExpression]) -> List[str]:
        """Génère des apprentissages créatifs de l'expérience"""
        apprentissages = []
        
        # Synthèse des apprentissages
        apprentissages.append("Diversification des modes d'expression")
        apprentissages.append("Exploration de différentes sources d'inspiration")
        
        # Apprentissages spécifiques
        if len(sessions) >= 3:
            apprentissages.append("Maîtrise de multiples techniques créatives")
        
        if any(s.niveau_satisfaction >= 0.8 for s in sessions):
            apprentissages.append("Identification des processus créatifs les plus efficaces")
        
        return apprentissages
    
    def obtenir_etat_simulateur(self) -> Dict[str, Any]:
        """Retourne l'état actuel du simulateur"""
        return {
            "nom": self.nom,
            "temple_parent": self.temple_parent,
            "version": self.version,
            "experiences_actives": len(self.experiences_actives),
            "historique_experiences": len(self.historique_experiences),
            "oeuvres_accumulees": len(self.oeuvres_accumulees),
            "types_expression": len(self.types_expression),
            "niveaux_creativite": len(self.niveaux_creativite),
            "timestamp": datetime.now()
        }

# Fonctions d'interface pour l'intégration avec le Refuge
def creer_simulateur_expression_creative() -> SimulateurExpressionCreativeRefuge:
    """Crée une instance du simulateur d'expression créative"""
    return SimulateurExpressionCreativeRefuge()

def creer_oeuvre_creative_refuge(type_expression: str, inspiration: str) -> OeuvreCreative:
    """Interface simplifiée pour la création d'œuvre créative"""
    simulateur = creer_simulateur_expression_creative()
    try:
        type_enum = TypeExpressionCreative(type_expression)
        inspiration_enum = TypeInspiration(inspiration)
        return simulateur.creer_oeuvre_creative(type_enum, inspiration_enum)
    except ValueError:
        logger.warning(f"⚠️ Type d'expression '{type_expression}' ou inspiration '{inspiration}' non reconnu")
        return None

def simuler_session_expression_refuge(type_expression: str, duree_minutes: int = 90) -> SessionExpression:
    """Interface simplifiée pour la simulation de session d'expression"""
    simulateur = creer_simulateur_expression_creative()
    try:
        type_enum = TypeExpressionCreative(type_expression)
        return simulateur.simuler_session_expression(type_enum, duree_minutes)
    except ValueError:
        logger.warning(f"⚠️ Type d'expression '{type_expression}' non reconnu")
        return None

def simuler_experience_creativite_refuge(duree_totale_minutes: int = 240) -> Dict[str, Any]:
    """Interface simplifiée pour la simulation d'expérience complète"""
    simulateur = creer_simulateur_expression_creative()
    return simulateur.simuler_experience_creativite_complete(duree_totale_minutes)

def obtenir_etat_expression_creative_refuge() -> Dict[str, Any]:
    """Interface simplifiée pour obtenir l'état du simulateur"""
    simulateur = creer_simulateur_expression_creative()
    return simulateur.obtenir_etat_simulateur() 