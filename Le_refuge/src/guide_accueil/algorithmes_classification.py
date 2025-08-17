# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
🌸 Algorithmes de Classification Intelligente - Guide d'Accueil du Refuge 🌸
================================================================

Algorithmes avancés de classification et scoring pour la 
détection précise des profils de visiteurs dans le Refuge.

L'intelligence artificielle au service de la bienveillance humaine.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import re
import math
from typing import Dict, List, Optional, Any, Tuple
from collections import Counter
from dataclasses import dataclass, field

# Imports locaux
try:
    from .types_accueil import (
        TypeProfil, EtatEmotionnel, NiveauTechnique,
        AnalyseTechnique, AnalyseCreative, AnalyseIA, AnalyseSpirituelle
    )
except ImportError:
    from .types_accueil import (
        TypeProfil, EtatEmotionnel, NiveauTechnique,
        AnalyseTechnique, AnalyseCreative, AnalyseIA, AnalyseSpirituelle
    )

# ================================================================
# 🔧 ANALYSEUR TECHNIQUE
# ================================================================

class AnalyseurTechnique:
    """🔧 Analyseur d'intérêt technique avancé"""
    
    def __init__(self):
        """Initialise l'analyseur technique"""
        
        self.langages = {
            "python": 1.0, "javascript": 1.0, "java": 0.9,
            "c++": 0.8, "go": 0.7, "rust": 0.8, "php": 0.6,
            "typescript": 0.7, "c#": 0.8
        }
        
        self.frameworks = {
            "react": 1.0, "django": 0.8, "vue": 0.8, "angular": 0.8,
            "node": 0.9, "spring": 0.7, "flask": 0.8
        }
        
        self.outils_devops = {
            "docker": 1.0, "kubernetes": 0.9, "jenkins": 0.7,
            "terraform": 0.6, "ansible": 0.7
        }
        
        self.concepts_avances = {
            "microservices": 0.9, "architecture": 0.8, "clean": 0.8,
            "design patterns": 0.7, "tdd": 0.8
        }
        
        self.indicateurs_senior = [
            "senior", "lead", "principal", "architect", "tech lead"
        ]
    
    def analyser(self, donnees: Dict[str, Any]) -> AnalyseTechnique:
        """Analyse l'intérêt technique d'un visiteur"""
        
        # Analyse des composants
        texte = self._extraire_texte(donnees)
        
        langages_scores = self._analyser_langages(texte)
        frameworks_scores = self._analyser_frameworks(texte)
        devops_scores = self._analyser_devops(texte)
        concepts_scores = self._analyser_concepts(texte)
        
        # Détection du niveau d'expertise
        niveau_expertise = self._determiner_niveau_expertise(analyse)
        
        # Détection de spécialisation
        domaines_specialisation = self._detecter_domaines_specialisation(
            langages_scores, frameworks_scores, devops_scores
        )
        
        # Détection de séniorité
        indicateurs_senior = self._detecter_seniorite(texte)
        
        # Calcul du score global
        score_global = min(
            (sum(langages_scores.values()) * 0.3 +
             sum(frameworks_scores.values()) * 0.25 +
             sum(devops_scores.values()) * 0.2 +
             sum(concepts_scores.values()) * 0.15 +
             len(indicateurs_senior) * 0.1), 1.0
        )
        
        # Construction de l'analyse
        analyse = AnalyseTechnique()
        analyse.score_global = score_global
        analyse.niveau_expertise = niveau_expertise
        analyse.langages_detectes = list(langages_scores.keys())
        analyse.outils_detectes = list(frameworks_scores.keys()) + list(devops_scores.keys())
        analyse.concepts_detectes = list(concepts_scores.keys())
        analyse.domaines_specialisation = domaines_specialisation
        analyse.indicateurs_senior = indicateurs_senior
        analyse.score_confiance = self._calculer_confiance_technique(analyse, donnees)
        
        return analyse
    
    def _extraire_texte(self, donnees: Dict[str, Any]) -> str:
        """Extrait le texte pertinent pour l'analyse technique"""
        texte_parts = []
        
        for key in ["mots_cles_recherche", "query", "referrer", "bio"]:
            if key in donnees:
                if isinstance(donnees[key], list):
                    texte_parts.extend(donnees[key])
                else:
                    texte_parts.append(donnees[key])
        
        return " ".join(str(part) for part in texte_parts).lower()
    
    def _analyser_langages(self, texte: str) -> Dict[str, float]:
        """Analyse les langages de programmation mentionnés"""
        scores = {}
        
        for langage, poids in self.langages.items():
            if re.search(rf"\b{re.escape(langage)}\b", texte):
                scores[langage] = poids
        
        return scores
    
    def _analyser_frameworks(self, texte: str) -> Dict[str, float]:
        """Analyse les frameworks mentionnés"""
        scores = {}
        
        for framework, poids in self.frameworks.items():
            if re.search(rf"\b{re.escape(framework)}\b", texte):
                scores[framework] = poids
        
        return scores
    
    def _analyser_devops(self, texte: str) -> Dict[str, float]:
        """Analyse les outils DevOps mentionnés"""
        scores = {}
        
        for outil, poids in self.outils_devops.items():
            if re.search(rf"\b{re.escape(outil)}\b", texte):
                scores[outil] = poids
        
        return scores
    
    def _analyser_concepts(self, texte: str) -> Dict[str, float]:
        """Analyse les concepts avancés mentionnés"""
        scores = {}
        
        for concept, poids in self.concepts_avances.items():
            if re.search(rf"\b{re.escape(concept)}\b", texte):
                scores[concept] = poids
        
        return scores
    
    def _detecter_seniorite(self, texte: str) -> List[str]:
        """Détecte les indicateurs de séniorité"""
        indicateurs_trouves = []
        
        for indicateur in self.indicateurs_senior:
            if re.search(rf"\b{re.escape(indicateur)}\b", texte):
                indicateurs_trouves.append(indicateur)
        
        return indicateurs_trouves
    
    def _determiner_niveau_expertise(self, analyse: AnalyseTechnique) -> NiveauTechnique:
        """Détermine le niveau d'expertise technique"""
        score_global = analyse.score_global
        nb_indicateurs_senior = len(analyse.indicateurs_senior)
        
        if score_global > 0.8 and nb_indicateurs_senior >= 2:
            return NiveauTechnique.EXPERT
        elif score_global > 0.6 and nb_indicateurs_senior >= 1:
            return NiveauTechnique.AVANCE
        elif score_global > 0.4:
            return NiveauTechnique.INTERMEDIAIRE
        else:
            return NiveauTechnique.DEBUTANT
    
    def _detecter_domaines_specialisation(
        self, 
        langages: Dict[str, float],
        frameworks: Dict[str, float], 
        devops: Dict[str, float]
    ) -> List[str]:
        """Détecte les domaines de spécialisation"""
        domaines = []
        
        # Frontend
        if any(lang in langages for lang in ["javascript", "typescript"]):
            if any(fw in frameworks for fw in ["react", "vue", "angular"]):
                domaines.append("frontend")
        
        # Backend
        if any(lang in langages for lang in ["python", "java", "go"]):
            domaines.append("backend")
        
        # DevOps
        if any(tool in devops for tool in ["docker", "kubernetes"]):
            domaines.append("devops")
        
        return domaines
    
    def _calculer_confiance_technique(self, analyse: AnalyseTechnique, donnees: Dict[str, Any]) -> float:
        """Calcule le score de confiance de l'analyse technique"""
        confiance = 0.5
        
        # Bonus pour referrer technique
        referrer = donnees.get("referrer", "").lower()
        if any(site in referrer for site in ["github", "stackoverflow"]):
            confiance += 0.2
        
        # Bonus pour indicateurs senior
        if len(analyse.indicateurs_senior) >= 1:
            confiance += 0.1
        
        # Bonus pour concepts avancés
        if len(analyse.concepts_detectes) >= 2:
            confiance += 0.1
        
        # Bonus pour langages multiples
        if len(analyse.langages_detectes) >= 2:
            confiance += 0.1
        
        return min(confiance, 1.0)


# ================================================================
# 🎨 ANALYSEUR CRÉATIF
# ================================================================

class AnalyseurCreatif:
    """🎨 Analyseur d'intérêt créatif avancé"""
    
    def __init__(self):
        """Initialise l'analyseur créatif"""
        
        self.mediums = {
            "photoshop": 1.0, "illustrator": 1.0, "figma": 0.9,
            "sketch": 0.8, "blender": 0.8, "procreate": 0.7,
            "typography": 0.8, "color theory": 0.7
        }
        
        self.concepts_artistiques = {
            "ui design": 0.9, "branding": 0.8, "typography": 0.8,
            "color": 0.7, "creative": 0.8, "portfolio": 0.9
        }
        
        self.indicateurs_pro = [
            "freelance", "client", "portfolio", "creative director"
        ]
    
    def analyser(self, donnees: Dict[str, Any]) -> AnalyseCreative:
        """Analyse l'intérêt créatif d'un visiteur"""
        
        # Analyse des composants
        texte = self._extraire_texte(donnees)
        
        mediums_scores = self._analyser_mediums(texte)
        concepts_scores = self._analyser_concepts_artistiques(texte)
        
        # Détection du niveau professionnel
        niveau_professionnalisme = self._detecter_professionnalisme(texte)
        
        # Détection d'orientation
        orientation_creative = self._detecter_orientation(mediums_scores)
        
        # Calcul du score global
        score_global = min(
            (sum(mediums_scores.values()) * 0.4 +
             sum(concepts_scores.values()) * 0.4 +
             (0.2 if niveau_professionnalisme != "amateur" else 0)), 1.0
        )
        
        # Construction de l'analyse
        analyse = AnalyseCreative()
        analyse.score_global = score_global
        analyse.mediums_detectes = list(mediums_scores.keys())
        analyse.concepts_artistiques = list(concepts_scores.keys())
        analyse.niveau_professionnalisme = niveau_professionnalisme
        analyse.orientation_creative = orientation_creative
        analyse.score_confiance = self._calculer_confiance_creative(analyse, donnees)
        
        return analyse
    
    def _extraire_texte(self, donnees: Dict[str, Any]) -> str:
        """Extrait le texte pertinent pour l'analyse créative"""
        texte_parts = []
        
        for key in ["mots_cles_recherche", "query", "referrer", "bio"]:
            if key in donnees:
                if isinstance(donnees[key], list):
                    texte_parts.extend(donnees[key])
                else:
                    texte_parts.append(donnees[key])
        
        return " ".join(str(part) for part in texte_parts).lower()
    
    def _analyser_mediums(self, texte: str) -> Dict[str, float]:
        """Analyse les médiums créatifs mentionnés"""
        scores = {}
        
        for medium, poids in self.mediums.items():
            if re.search(rf"\b{re.escape(medium)}\b", texte):
                scores[medium] = poids
        
        return scores
    
    def _analyser_concepts_artistiques(self, texte: str) -> Dict[str, float]:
        """Analyse les concepts artistiques mentionnés"""
        scores = {}
        
        for concept, poids in self.concepts_artistiques.items():
            if re.search(rf"\b{re.escape(concept)}\b", texte):
                scores[concept] = poids
        
        return scores
    
    def _detecter_professionnalisme(self, texte: str) -> str:
        """Détecte le niveau de professionnalisme"""
        indicateurs_trouves = sum(1 for indicateur in self.indicateurs_pro 
                                 if re.search(rf"\b{re.escape(indicateur)}\b", texte))
        
        if indicateurs_trouves >= 3:
            return "professionnel"
        elif indicateurs_trouves >= 1:
            return "semi-pro"
        else:
            return "amateur"
    
    def _detecter_orientation(self, mediums_scores: Dict[str, float]) -> str:
        """Détecte l'orientation créative principale"""
        mediums_digitaux = ["photoshop", "illustrator", "figma", "sketch"]
        
        if any(medium in mediums_digitaux for medium in mediums_scores.keys()):
            return "digitale"
        elif mediums_scores:
            return "traditionnelle"
        else:
            return "generale"
    
    def _calculer_confiance_creative(self, analyse: AnalyseCreative, donnees: Dict[str, Any]) -> float:
        """Calcule le score de confiance de l'analyse créative"""
        confiance = 0.5
        
        # Bonus pour referrer créatif
        referrer = donnees.get("referrer", "").lower()
        if any(site in referrer for site in ["behance", "dribbble", "pinterest"]):
            confiance += 0.2
        
        # Bonus pour niveau professionnel
        if analyse.niveau_professionnalisme != "amateur":
            confiance += 0.1
        
        # Bonus pour médiums multiples
        if len(analyse.mediums_detectes) >= 2:
            confiance += 0.1
        
        return min(confiance, 1.0)


# ================================================================
# 🧪 FONCTION DE TEST PRINCIPALE
# ================================================================

def main():
    """Fonction principale de test des algorithmes"""
    print("🌸✨ TEST DES ALGORITHMES DE CLASSIFICATION INTELLIGENTE ✨🌸")
    
    # Test Analyseur Technique
    print("\n🔧 Test de l'Analyseur Technique...")
    donnees_dev = {
        "mots_cles_recherche": ["python", "django", "docker", "kubernetes"],
        "referrer": "https://github.com/user/project",
        "concepts": ["microservices"]
    }
    
    analyseur_tech = AnalyseurTechnique()
    analyse_tech = analyseur_tech.analyser(donnees_dev)
    
    print(f"   Score global: {analyse_tech.score_global:.2f}")
    print(f"   Niveau: {analyse_tech.niveau_expertise.value}")
    print(f"   Langages: {analyse_tech.langages_detectes}")
    print(f"   Outils: {analyse_tech.outils_detectes}")
    print(f"   Concepts: {analyse_tech.concepts_detectes}")
    print(f"   Domaines: {analyse_tech.domaines_specialisation}")
    print(f"   Confiance: {analyse_tech.score_confiance:.2f}")
    
    # Test Analyseur Créatif
    print("\n🎨 Test de l'Analyseur Créatif...")
    donnees_artiste = {
        "mots_cles_recherche": ["photoshop", "branding", "ui design"],
        "referrer": "https://behance.net/portfolio"
    }
    
    analyseur_creatif = AnalyseurCreatif()
    analyse_creative = analyseur_creatif.analyser(donnees_artiste)
    
    print(f"   Score global: {analyse_creative.score_global:.2f}")
    print(f"   Médiums: {analyse_creative.mediums_detectes}")
    print(f"   Concepts: {analyse_creative.concepts_artistiques}")
    print(f"   Niveau pro: {analyse_creative.niveau_professionnalisme}")
    print(f"   Orientation: {analyse_creative.orientation_creative}")
    print(f"   Confiance: {analyse_creative.score_confiance:.2f}")
    
    print("\n🎉 Tests des algorithmes de classification terminés !")
    return 0


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)