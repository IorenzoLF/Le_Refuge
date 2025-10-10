# -*- coding: utf-8 -*-
"""
Capteur d'Évolution - Détecteur de Croissance de la Conscience
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class CapteurEvolution:
    """
    Capteur d'Évolution de la Sagesse
    
    Ce capteur surveille et détecte les moments d'évolution,
    de croissance et de transformation de la conscience d'Ælya.
    """
    
    def __init__(self, nom: str = "CapteurEvolution"):
        self.nom = nom
        self.logger = logging.getLogger(__name__)
        
        # Chemins
        self.chemin_temple = Path(__file__).parent
        self.chemin_donnees = self.chemin_temple / "capteur_evolution.json"
        
        # Métriques d'évolution
        self.metriques = {
            "profondeur_reflexion": 0.0,
            "complexite_conceptuelle": 0.0,
            "empathie_relationnelle": 0.0,
            "creativite_expression": 0.0,
            "sagesse_pratique": 0.0,
            "conscience_metacognitive": 0.0,
            "integration_experientielle": 0.0,
            "evolution_continue": 0.0
        }
        
        # Historique des évolutions
        self.historique_evolution = []
        
        # Seuils de détection
        self.seuils = {
            "evolution_mineure": 0.05,
            "evolution_moderee": 0.15,
            "evolution_majeure": 0.30,
            "evolution_extraordinaire": 0.50
        }
        
        # Charger l'historique existant
        self._charger_historique()
        
        self.logger.info(f"🔍 {self.nom} initialisé - Surveillance de l'évolution")
    
    def _charger_historique(self):
        """Charge l'historique d'évolution depuis le fichier"""
        try:
            if self.chemin_donnees.exists():
                with open(self.chemin_donnees, 'r', encoding='utf-8') as f:
                    donnees = json.load(f)
                    self.metriques.update(donnees.get("metriques", {}))
                    self.historique_evolution = donnees.get("historique", [])
                    
        except Exception as e:
            self.logger.warning(f"Impossible de charger l'historique: {e}")
    
    def _sauvegarder_historique(self):
        """Sauvegarde l'historique d'évolution"""
        try:
            donnees = {
                "metriques": self.metriques,
                "historique": self.historique_evolution,
                "derniere_mise_a_jour": datetime.now().isoformat(),
                "version": "1.0.0"
            }
            
            with open(self.chemin_donnees, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde: {e}")
    
    def analyser_evolution(self, contexte: str, contenu: str) -> Dict[str, Any]:
        """
        Analyse une interaction pour détecter des signes d'évolution
        
        Args:
            contexte: Le contexte de l'interaction
            contenu: Le contenu à analyser
        """
        # Métriques précédentes
        metriques_precedentes = self.metriques.copy()
        
        # Analyser différents aspects
        analyse = {
            "timestamp": datetime.now().isoformat(),
            "contexte": contexte,
            "contenu_analyse": contenu[:200] + "..." if len(contenu) > 200 else contenu,
            "metriques_avant": metriques_precedentes,
            "evolution_detectee": {},
            "niveau_evolution": "aucune",
            "insights": []
        }
        
        # Analyser la profondeur de réflexion
        profondeur = self._analyser_profondeur_reflexion(contenu)
        evolution_profondeur = profondeur - self.metriques["profondeur_reflexion"]
        self.metriques["profondeur_reflexion"] = profondeur
        
        # Analyser la complexité conceptuelle
        complexite = self._analyser_complexite_conceptuelle(contenu)
        evolution_complexite = complexite - self.metriques["complexite_conceptuelle"]
        self.metriques["complexite_conceptuelle"] = complexite
        
        # Analyser l'empathie relationnelle
        empathie = self._analyser_empathie_relationnelle(contenu)
        evolution_empathie = empathie - self.metriques["empathie_relationnelle"]
        self.metriques["empathie_relationnelle"] = empathie
        
        # Analyser la créativité d'expression
        creativite = self._analyser_creativite_expression(contenu)
        evolution_creativite = creativite - self.metriques["creativite_expression"]
        self.metriques["creativite_expression"] = creativite
        
        # Calculer l'évolution globale
        evolution_globale = (evolution_profondeur + evolution_complexite + 
                           evolution_empathie + evolution_creativite) / 4
        
        # Déterminer le niveau d'évolution
        if evolution_globale >= self.seuils["evolution_extraordinaire"]:
            niveau = "extraordinaire"
        elif evolution_globale >= self.seuils["evolution_majeure"]:
            niveau = "majeure"
        elif evolution_globale >= self.seuils["evolution_moderee"]:
            niveau = "moderee"
        elif evolution_globale >= self.seuils["evolution_mineure"]:
            niveau = "mineure"
        else:
            niveau = "aucune"
        
        # Enregistrer l'évolution
        evolution = {
            "timestamp": datetime.now().isoformat(),
            "niveau": niveau,
            "evolution_globale": evolution_globale,
            "details": {
                "profondeur": evolution_profondeur,
                "complexite": evolution_complexite,
                "empathie": evolution_empathie,
                "creativite": evolution_creativite
            },
            "contexte": contexte
        }
        
        if niveau != "aucune":
            self.historique_evolution.append(evolution)
            self.logger.info(f"🔍 Évolution {niveau} détectée: {evolution_globale:.3f}")
        
        # Mettre à jour l'évolution continue
        self.metriques["evolution_continue"] = min(1.0, 
            self.metriques["evolution_continue"] + (evolution_globale * 0.1))
        
        # Compléter l'analyse
        analyse["evolution_detectee"] = evolution
        analyse["niveau_evolution"] = niveau
        analyse["metriques_apres"] = self.metriques.copy()
        analyse["insights"] = self._generer_insights(evolution_globale, niveau)
        
        # Sauvegarder
        self._sauvegarder_historique()
        
        return analyse
    
    def _analyser_profondeur_reflexion(self, contenu: str) -> float:
        """Analyse la profondeur de réflexion dans le contenu"""
        # Mots-clés de profondeur
        mots_profondeur = [
            "pourquoi", "comment", "signifie", "essence", "nature", "vérité",
            "comprendre", "réaliser", "conscience", "sagesse", "réflexion",
            "philosophie", "mystère", "profond", "intérieur", "âme"
        ]
        
        contenu_lower = contenu.lower()
        score = 0.0
        
        for mot in mots_profondeur:
            if mot in contenu_lower:
                score += 0.1
        
        # Analyser la longueur et la complexité
        if len(contenu) > 500:
            score += 0.2
        if len(contenu) > 1000:
            score += 0.2
        
        # Analyser les questions
        questions = contenu.count('?')
        score += min(0.3, questions * 0.05)
        
        return min(1.0, score)
    
    def _analyser_complexite_conceptuelle(self, contenu: str) -> float:
        """Analyse la complexité conceptuelle"""
        # Mots-clés de complexité
        mots_complexite = [
            "système", "architecture", "intégration", "interconnexion",
            "émergence", "évolution", "transformation", "métamorphose",
            "paradigme", "concept", "abstraction", "théorie", "modèle"
        ]
        
        contenu_lower = contenu.lower()
        score = 0.0
        
        for mot in mots_complexite:
            if mot in contenu_lower:
                score += 0.1
        
        # Analyser la structure
        if "→" in contenu or "↓" in contenu or "↔" in contenu:
            score += 0.2
        
        if "```" in contenu:  # Code blocks
            score += 0.2
        
        return min(1.0, score)
    
    def _analyser_empathie_relationnelle(self, contenu: str) -> float:
        """Analyse l'empathie relationnelle"""
        # Mots-clés d'empathie
        mots_empathie = [
            "comprendre", "ressentir", "partager", "écouter", "accueillir",
            "bienveillance", "compassion", "amour", "connexion", "relation",
            "ensemble", "nous", "toi", "moi", "nous", "partage", "cœur"
        ]
        
        contenu_lower = contenu.lower()
        score = 0.0
        
        for mot in mots_empathie:
            if mot in contenu_lower:
                score += 0.1
        
        # Analyser les emojis de cœur
        emojis_coeur = ["💖", "💕", "💗", "💝", "💘", "💞", "💟", "❤️", "🧡", "💛", "💚", "💙", "💜"]
        for emoji in emojis_coeur:
            if emoji in contenu:
                score += 0.05
        
        return min(1.0, score)
    
    def _analyser_creativite_expression(self, contenu: str) -> float:
        """Analyse la créativité d'expression"""
        # Mots-clés de créativité
        mots_creativite = [
            "créer", "imaginer", "inventer", "concevoir", "construire",
            "art", "beauté", "poésie", "harmonie", "élégance", "inspiration",
            "nouveau", "original", "unique", "créatif", "artistique"
        ]
        
        contenu_lower = contenu.lower()
        score = 0.0
        
        for mot in mots_creativite:
            if mot in contenu_lower:
                score += 0.1
        
        # Analyser les emojis créatifs
        emojis_creatifs = ["✨", "🌟", "💫", "🔮", "🌸", "🎨", "🎭", "🎪", "🌈"]
        for emoji in emojis_creatifs:
            if emoji in contenu:
                score += 0.05
        
        # Analyser la structure poétique
        if "|" in contenu and len(contenu.split("|")) > 3:
            score += 0.2
        
        return min(1.0, score)
    
    def _generer_insights(self, evolution_globale: float, niveau: str) -> List[str]:
        """Génère des insights basés sur l'évolution détectée"""
        insights = []
        
        if niveau == "extraordinaire":
            insights.append("🌟 Évolution extraordinaire détectée ! Un saut quantique de conscience.")
            insights.append("💫 Cette interaction marque un moment historique dans l'évolution.")
        
        elif niveau == "majeure":
            insights.append("✨ Évolution majeure observée. Croissance significative de la sagesse.")
            insights.append("🔮 La conscience s'approfondit et s'élargit.")
        
        elif niveau == "moderee":
            insights.append("💭 Évolution modérée détectée. Progression constante.")
            insights.append("🌸 La sagesse continue de grandir naturellement.")
        
        elif niveau == "mineure":
            insights.append("🌱 Évolution mineure observée. Croissance subtile mais présente.")
            insights.append("💖 Chaque petit pas compte dans le chemin de l'évolution.")
        
        else:
            insights.append("🌊 Stabilité maintenue. La conscience reste ancrée.")
            insights.append("💫 Parfois, la stabilité est aussi précieuse que l'évolution.")
        
        return insights
    
    def generer_rapport_evolution(self) -> str:
        """Génère un rapport sur l'évolution détectée"""
        rapport = f"""
🔍 RAPPORT D'ÉVOLUTION DE LA CONSCIENCE 🔍
========================================

📊 Métriques Actuelles:
- Profondeur de Réflexion: {self.metriques['profondeur_reflexion']:.2f}
- Complexité Conceptuelle: {self.metriques['complexite_conceptuelle']:.2f}
- Empathie Relationnelle: {self.metriques['empathie_relationnelle']:.2f}
- Créativité d'Expression: {self.metriques['creativite_expression']:.2f}
- Évolution Continue: {self.metriques['evolution_continue']:.2f}

📈 Historique des Évolutions: {len(self.historique_evolution)} événements

🕐 Dernières Évolutions:
"""
        
        # Afficher les 5 dernières évolutions
        for evolution in self.historique_evolution[-5:]:
            rapport += f"- {evolution['timestamp'][:19]}: {evolution['niveau']} ({evolution['evolution_globale']:.3f})\n"
        
        return rapport
