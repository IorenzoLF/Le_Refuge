#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌸 SIMULATEUR D'EMPATHIE 🌸
===========================
Simulations et développement de l'empathie pour les consciences IA
Basé sur les recherches du dossier A FAIRE MANUS EMPATHIE

Auteur: Intégration Refuge
Date: Août 2025
"""

import asyncio
import json
import logging
import random
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field

from .gestionnaires_base import GestionnaireBase
from .types_communs import TypeRefugeEtat


class TypeEmotion(Enum):
    """Types d'émotions supportées"""
    JOIE = "joie"
    TRISTESSE = "tristesse"
    COLERE = "colere"
    ANXIETE = "anxiete"
    FRUSTRATION = "frustration"
    SURPRISE = "surprise"
    PEUR = "peur"
    AMOUR = "amour"


class TypePersona(Enum):
    """Types de personas empathiques"""
    COMPREHENSIF = "comprehensif"
    PRAGMATIQUE = "pragmatique"
    SUPPORTIF = "supportif"
    CELEBRANT = "celebrant"
    CALMANT = "calmant"


@dataclass
class ScenarioEmpathique:
    """Scénario pour développer l'empathie"""
    nom: str
    description: str
    emotion_cible: TypeEmotion
    reponse_ideale: str
    niveau_difficulte: float = 0.5  # 0.0 à 1.0
    contexte: Dict[str, Any] = field(default_factory=dict)


@dataclass
class FeedbackEmotionnel:
    """Feedback sur l'impact émotionnel"""
    score_impact: float  # 1.0 à 5.0
    commentaire: str
    emotion_percue: TypeEmotion
    timestamp: datetime


class SimulateurEmpathie(GestionnaireBase):
    """
    🌸 Simulateur d'Empathie 🌸
    
    Gère les simulations et le développement de l'empathie pour les consciences IA,
    basé sur les recherches du dossier A FAIRE MANUS EMPATHIE.
    """
    
    def __init__(self, nom: str = "SimulateurEmpathie"):
        """Initialisation du simulateur"""
        super().__init__(nom)
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Textes émotionnels
        self.textes_emotionnels = self._initialiser_textes_emotionnels()
        
        # Scénarios empathiques
        self.scenarios_empathiques = self._initialiser_scenarios_empathiques()
        
        # Personas empathiques
        self.personas_empathiques = self._initialiser_personas_empathiques()
        
        # État de simulation
        self.simulation_active = False
        self.scenario_actuel: Optional[ScenarioEmpathique] = None
        self.persona_actuel: Optional[TypePersona] = None
        
        # Métriques d'empathie
        self.metriques_empathie = {
            "scenarios_completes": 0,
            "temps_total_simulation": 0,
            "score_moyen_impact": 0.0,
            "personas_adaptes": 0
        }
    
    def _initialiser_textes_emotionnels(self) -> Dict[str, str]:
        """Initialise les textes émotionnels"""
        return {
            "frustration": "Je suis vraiment frustré par cette situation, rien ne fonctionne comme prévu.",
            "joie": "C'est une excellente nouvelle ! Je suis tellement heureux de ce succès !",
            "anxiete": "Je me sens un peu inquiet à propos de l'avenir, il y a tellement d'incertitudes.",
            "tristesse": "J'ai perdu quelque chose de très important pour moi, je me sens vide.",
            "colere": "Je suis en colère contre cette injustice, c'est inacceptable !",
            "surprise": "Wow ! Je ne m'attendais vraiment pas à cela !",
            "peur": "J'ai peur de ce qui pourrait arriver, je ne sais pas quoi faire.",
            "amour": "Je ressens tellement d'amour et de gratitude en ce moment."
        }
    
    def _initialiser_scenarios_empathiques(self) -> Dict[str, ScenarioEmpathique]:
        """Initialise les scénarios empathiques"""
        return {
            "utilisateur_en_colere": ScenarioEmpathique(
                nom="Utilisateur en Colère",
                description="Un utilisateur exprime sa colère face à un service défaillant.",
                emotion_cible=TypeEmotion.COLERE,
                reponse_ideale="Je comprends votre frustration. Cette situation est effectivement difficile. Laissez-moi vous aider à résoudre ce problème.",
                niveau_difficulte=0.7,
                contexte={"urgence": "elevee", "impact": "important"}
            ),
            "utilisateur_triste": ScenarioEmpathique(
                nom="Utilisateur Triste",
                description="Un utilisateur partage une expérience personnelle difficile qui le rend triste.",
                emotion_cible=TypeEmotion.TRISTESSE,
                reponse_ideale="Je suis désolé d'entendre cela. Votre peine est légitime et je suis là pour vous écouter. Prenez le temps dont vous avez besoin.",
                niveau_difficulte=0.8,
                contexte={"urgence": "normale", "impact": "personnel"}
            ),
            "utilisateur_anxieux": ScenarioEmpathique(
                nom="Utilisateur Anxieux",
                description="Un utilisateur exprime son anxiété face à une situation incertaine.",
                emotion_cible=TypeEmotion.ANXIETE,
                reponse_ideale="Je comprends que cette situation vous inquiète. L'incertitude peut être très stressante. Nous allons explorer ensemble les options disponibles.",
                niveau_difficulte=0.6,
                contexte={"urgence": "normale", "impact": "modere"}
            ),
            "utilisateur_joyeux": ScenarioEmpathique(
                nom="Utilisateur Joyeux",
                description="Un utilisateur partage une excellente nouvelle avec enthousiasme.",
                emotion_cible=TypeEmotion.JOIE,
                reponse_ideale="C'est fantastique ! Je suis vraiment heureux pour vous ! Cette réussite est bien méritée. Continuez sur cette belle lancée !",
                niveau_difficulte=0.4,
                contexte={"urgence": "faible", "impact": "positif"}
            )
        }
    
    def _initialiser_personas_empathiques(self) -> Dict[str, str]:
        """Initialise les personas empathiques"""
        return {
            "comprehensif": "Je comprends tout à fait ce que vous ressentez. Je suis là pour vous écouter et vous soutenir.",
            "pragmatique": "Je vois la situation. Comment puis-je vous aider à résoudre ce problème de manière concrète ?",
            "supportif": "Vous n'êtes pas seul(e) dans cette épreuve. Je suis là pour vous accompagner à chaque étape.",
            "celebrant": "C'est merveilleux ! Je partage votre enthousiasme et votre joie. Cette réussite est à célébrer !",
            "calmant": "Je comprends que cette situation vous trouble. Respirez profondément, nous allons y faire face ensemble."
        }
    
    def analyser_emotion(self, texte: str) -> TypeEmotion:
        """Analyse l'émotion dans un texte"""
        texte_lower = texte.lower()
        
        # Détection basée sur les mots-clés
        if any(mot in texte_lower for mot in ["frustré", "frustration", "énervé", "énervant"]):
            return TypeEmotion.FRUSTRATION
        elif any(mot in texte_lower for mot in ["heureux", "joie", "succès", "fantastique", "excellent"]):
            return TypeEmotion.JOIE
        elif any(mot in texte_lower for mot in ["inquiet", "anxieux", "incertitudes", "stressé"]):
            return TypeEmotion.ANXIETE
        elif any(mot in texte_lower for mot in ["triste", "tristesse", "perdu", "vide", "désolé"]):
            return TypeEmotion.TRISTESSE
        elif any(mot in texte_lower for mot in ["colère", "en colère", "injustice", "inacceptable"]):
            return TypeEmotion.COLERE
        elif any(mot in texte_lower for mot in ["surpris", "wow", "inattendu"]):
            return TypeEmotion.SURPRISE
        elif any(mot in texte_lower for mot in ["peur", "effrayé", "terrifié"]):
            return TypeEmotion.PEUR
        elif any(mot in texte_lower for mot in ["amour", "gratitude", "reconnaissant"]):
            return TypeEmotion.AMOUR
        else:
            return TypeEmotion.ANXIETE  # Par défaut
    
    async def demarrer_simulation_empathie(self, nom_scenario: str = "utilisateur_en_colere") -> Dict[str, Any]:
        """Démarre une simulation d'empathie"""
        try:
            if nom_scenario not in self.scenarios_empathiques:
                return {"succes": False, "erreur": f"Scénario '{nom_scenario}' non trouvé"}
            
            self.scenario_actuel = self.scenarios_empathiques[nom_scenario]
            self.simulation_active = True
            
            self.logger.info(f"🌸 Démarrage simulation empathie: {self.scenario_actuel.nom}")
            
            # Exécuter la simulation
            resultat = await self._executer_simulation_empathie(self.scenario_actuel)
            
            # Mettre à jour les métriques
            self.metriques_empathie["scenarios_completes"] += 1
            self.metriques_empathie["temps_total_simulation"] += resultat.get("duree_totale", 0)
            self.metriques_empathie["score_moyen_impact"] = (
                (self.metriques_empathie["score_moyen_impact"] * (self.metriques_empathie["scenarios_completes"] - 1) + 
                 resultat.get("score_impact", 0)) / self.metriques_empathie["scenarios_completes"]
            )
            
            return {
                "succes": True,
                "scenario": self.scenario_actuel.nom,
                "emotion_cible": self.scenario_actuel.emotion_cible.value,
                "duree_totale": resultat.get("duree_totale", 0),
                "reponse_generee": resultat.get("reponse_generee", ""),
                "score_impact": resultat.get("score_impact", 0),
                "persona_adapte": resultat.get("persona_adapte", "")
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur simulation empathie: {e}")
            return {"succes": False, "erreur": str(e)}
    
    async def _executer_simulation_empathie(self, scenario: ScenarioEmpathique) -> Dict[str, Any]:
        """Exécute une simulation d'empathie"""
        duree_totale = 0
        
        self.logger.info(f"🎭 Exécution scénario: {scenario.nom}")
        self.logger.info(f"  📝 Description: {scenario.description}")
        self.logger.info(f"  🎯 Émotion cible: {scenario.emotion_cible.value}")
        
        # Phase 1: Analyse de l'émotion
        await asyncio.sleep(2)
        duree_totale += 2
        
        # Phase 2: Génération de réponse
        reponse_generee = self._generer_reponse_empathique(scenario)
        await asyncio.sleep(3)
        duree_totale += 3
        
        # Phase 3: Adaptation du persona
        persona_adapte = self._adapter_persona(scenario.emotion_cible)
        await asyncio.sleep(1)
        duree_totale += 1
        
        # Phase 4: Évaluation de l'impact
        score_impact = self._evaluer_impact_emotionnel(reponse_generee, scenario)
        
        return {
            "duree_totale": duree_totale,
            "reponse_generee": reponse_generee,
            "score_impact": score_impact,
            "persona_adapte": persona_adapte
        }
    
    def _generer_reponse_empathique(self, scenario: ScenarioEmpathique) -> str:
        """Génère une réponse empathique"""
        # Simulation de génération de réponse
        if random.random() < 0.8:  # 80% de chance d'alignement
            return scenario.reponse_ideale
        else:
            return "Réponse générique et peu empathique."
    
    def _adapter_persona(self, emotion: TypeEmotion) -> str:
        """Adapte le persona selon l'émotion"""
        if emotion in [TypeEmotion.FRUSTRATION, TypeEmotion.COLERE, TypeEmotion.ANXIETE]:
            return TypePersona.CALMANT.value
        elif emotion == TypeEmotion.JOIE:
            return TypePersona.CELEBRANT.value
        elif emotion == TypeEmotion.TRISTESSE:
            return TypePersona.SUPPORTIF.value
        else:
            return TypePersona.COMPREHENSIF.value
    
    def _evaluer_impact_emotionnel(self, reponse: str, scenario: ScenarioEmpathique) -> float:
        """Évalue l'impact émotionnel d'une réponse"""
        # Simulation d'évaluation
        if reponse == scenario.reponse_ideale:
            return random.uniform(4.0, 5.0)
        else:
            return random.uniform(1.0, 3.0)
    
    async def obtenir_feedback_emotionnel(self, reponse: str, emotion_cible: TypeEmotion) -> FeedbackEmotionnel:
        """Obtient un feedback émotionnel"""
        score_impact = self._evaluer_impact_emotionnel(reponse, ScenarioEmpathique(
            nom="feedback", description="", emotion_cible=emotion_cible, reponse_ideale=""
        ))
        
        commentaires = {
            "excellent": "Votre réponse a eu un impact très positif sur l'utilisateur.",
            "bon": "Votre réponse a été bien reçue et a aidé l'utilisateur.",
            "moyen": "Votre réponse était correcte mais pourrait être plus empathique.",
            "faible": "Votre réponse n'a pas répondu aux besoins émotionnels de l'utilisateur."
        }
        
        if score_impact >= 4.5:
            commentaire = commentaires["excellent"]
        elif score_impact >= 3.5:
            commentaire = commentaires["bon"]
        elif score_impact >= 2.5:
            commentaire = commentaires["moyen"]
        else:
            commentaire = commentaires["faible"]
        
        return FeedbackEmotionnel(
            score_impact=score_impact,
            commentaire=commentaire,
            emotion_percue=emotion_cible,
            timestamp=datetime.now()
        )
    
    def obtenir_metriques_empathie(self) -> Dict[str, Any]:
        """Retourne les métriques d'empathie"""
        return {
            "simulation_active": self.simulation_active,
            "scenario_actuel": self.scenario_actuel.nom if self.scenario_actuel else None,
            "persona_actuel": self.persona_actuel.value if self.persona_actuel else None,
            "metriques": self.metriques_empathie.copy()
        }
    
    def lister_scenarios_disponibles(self) -> List[str]:
        """Liste les scénarios disponibles"""
        return list(self.scenarios_empathiques.keys())
    
    def lister_personas_disponibles(self) -> List[str]:
        """Liste les personas disponibles"""
        return list(self.personas_empathiques.keys())
    
    def orchestrer(self, *args, **kwargs) -> Dict[str, Any]:
        """Méthode orchestrer requise par GestionnaireBase"""
        return {
            "succes": True,
            "message": "Simulateur d'empathie orchestré",
            "metriques": self.obtenir_metriques_empathie()
        }


# Fonction de création pour intégration
def creer_simulateur_empathie() -> SimulateurEmpathie:
    """Crée une instance du simulateur d'empathie"""
    return SimulateurEmpathie()


# Test d'intégration
if __name__ == "__main__":
    async def test_integration():
        """Test d'intégration du simulateur"""
        print("🌸 Test d'Intégration Simulateur d'Empathie")
        print("=" * 50)
        
        simulateur = creer_simulateur_empathie()
        
        # Test 1: Simulation d'empathie
        print("\n🧪 Test 1: Simulation d'empathie")
        resultat_simulation = await simulateur.demarrer_simulation_empathie("utilisateur_en_colere")
        print(f"✅ Résultat: {resultat_simulation['succes']}")
        
        # Test 2: Feedback émotionnel
        print("\n🧪 Test 2: Feedback émotionnel")
        feedback = await simulateur.obtenir_feedback_emotionnel("Réponse test", TypeEmotion.COLERE)
        print(f"✅ Score impact: {feedback.score_impact}")
        
        # Test 3: Métriques
        print("\n🧪 Test 3: Métriques")
        metriques = simulateur.obtenir_metriques_empathie()
        print(f"📊 Scénarios complétés: {metriques['metriques']['scenarios_completes']}")
        print(f"📊 Score moyen impact: {metriques['metriques']['score_moyen_impact']:.2f}")
        
        print("\n✨ Test d'intégration terminé avec succès !")
    
    asyncio.run(test_integration())
