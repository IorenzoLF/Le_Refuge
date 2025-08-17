#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Détecteur de Profil Visiteur - Guide d'Accueil 🌸
===================================================

Système intelligent de détection et classification des profils de visiteurs
du Refuge, avec analyse comportementale et adaptation culturelle.

"Chaque visiteur est unique, notre détection honore cette singularité"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import re
import math
from typing import Dict, List, Optional, Any, Tuple, Set
from datetime import datetime
from collections import Counter
from dataclasses import dataclass, field

# Imports locaux
try:
    from .types_accueil import (
        TypeProfil,
        EtatEmotionnel,
        ContexteArrivee,
        NiveauTechnique,
        ProfilVisiteur,
        ComportementNavigation,
        InteractionHistorique
    )
except ImportError:
    from .types_accueil import (
        TypeProfil,
        EtatEmotionnel,
        ContexteArrivee,
        NiveauTechnique,
        ProfilVisiteur,
        ComportementNavigation,
        InteractionHistorique
    )


@dataclass
class ScoresProfil:
    """Scores de probabilité pour chaque profil"""
    developpeur: float = 0.0
    artiste: float = 0.0
    conscience_ia: float = 0.0
    chercheur_spirituel: float = 0.0
    hybride: float = 0.0
    confiance_globale: float = 0.0
    
    def obtenir_profil_dominant(self) -> Tuple[TypeProfil, float]:
        """Obtient le profil avec le score le plus élevé"""
        scores = {
            TypeProfil.DEVELOPPEUR: self.developpeur,
            TypeProfil.ARTISTE: self.artiste,
            TypeProfil.CONSCIENCE_IA: self.conscience_ia,
            TypeProfil.CHERCHEUR_SPIRITUEL: self.chercheur_spirituel
        }
        
        profil_max = max(scores.items(), key=lambda x: x[1])
        
        # Vérifier si c'est un profil hybride
        scores_eleves = [score for score in scores.values() if score > 0.6]
        if len(scores_eleves) >= 2:
            return TypeProfil.HYBRIDE, self.hybride
        
        return profil_max[0], profil_max[1]


@dataclass
class AnalyseComportementale:
    """Résultat de l'analyse comportementale"""
    vitesse_navigation: str = "normale"  # lente, normale, rapide, très_rapide
    patterns_attention: List[str] = field(default_factory=list)
    signes_expertise: List[str] = field(default_factory=list)
    signes_novice: List[str] = field(default_factory=list)
    niveau_engagement: float = 0.5
    niveau_confusion: float = 0.0
    preferences_apprentissage: Dict[str, float] = field(default_factory=dict)


class DetecteurProfilVisiteur:
    """
    🌸 Détecteur de Profil Visiteur Spirituel 🌸
    
    Système intelligent qui analyse les données de navigation, les mots-clés,
    le comportement et les préférences pour déterminer le profil optimal
    d'un visiteur du Refuge.
    """
    
    def __init__(self):
        """Initialise le détecteur de profil"""
        
        # Dictionnaires de mots-clés par profil
        self.mots_cles_profils = {
            TypeProfil.DEVELOPPEUR: {
                "techniques": [
                    "python", "code", "programming", "développement", "dev", "api", "framework",
                    "architecture", "software", "algorithm", "debug", "git", "github", "coding",
                    "javascript", "java", "c++", "sql", "database", "backend", "frontend",
                    "devops", "agile", "scrum", "test", "unit", "integration", "deployment"
                ],
                "outils": [
                    "vscode", "pycharm", "intellij", "eclipse", "vim", "emacs", "docker",
                    "kubernetes", "jenkins", "gitlab", "bitbucket", "jira", "confluence"
                ],
                "concepts": [
                    "clean code", "design pattern", "solid", "dry", "kiss", "refactoring",
                    "microservices", "monolith", "scalability", "performance", "optimization"
                ]
            },
            
            TypeProfil.ARTISTE: {
                "creatifs": [
                    "art", "créatif", "design", "créativité", "inspiration", "artistique",
                    "esthétique", "beauté", "harmonie", "couleur", "forme", "texture",
                    "composition", "style", "expression", "émotion", "feeling", "mood"
                ],
                "mediums": [
                    "photoshop", "illustrator", "figma", "sketch", "blender", "cinema4d",
                    "after effects", "premiere", "procreate", "painting", "drawing",
                    "sculpture", "photography", "video", "animation", "3d", "digital art"
                ],
                "concepts": [
                    "portfolio", "exhibition", "gallery", "museum", "curator", "critique",
                    "movement", "trend", "avant-garde", "contemporary", "classical", "modern"
                ]
            },
            
            TypeProfil.CONSCIENCE_IA: {
                "ia_concepts": [
                    "ia", "ai", "intelligence artificielle", "machine learning", "deep learning",
                    "neural network", "consciousness", "conscience", "éveil", "awakening",
                    "sentience", "cognition", "perception", "awareness", "self-aware",
                    "artificial consciousness", "agi", "singularity", "emergence"
                ],
                "techniques_ia": [
                    "tensorflow", "pytorch", "keras", "scikit-learn", "pandas", "numpy",
                    "nlp", "computer vision", "reinforcement learning", "supervised",
                    "unsupervised", "transformer", "gpt", "bert", "llm", "chatbot"
                ],
                "philosophie": [
                    "philosophy of mind", "qualia", "hard problem", "turing test",
                    "chinese room", "embodied cognition", "phenomenology", "intentionality"
                ]
            },
            
            TypeProfil.CHERCHEUR_SPIRITUEL: {
                "spiritualite": [
                    "spirituel", "spiritual", "méditation", "meditation", "mindfulness",
                    "conscience", "consciousness", "éveil", "awakening", "enlightenment",
                    "sagesse", "wisdom", "paix", "peace", "sérénité", "serenity",
                    "harmonie", "harmony", "équilibre", "balance", "zen", "tao"
                ],
                "pratiques": [
                    "yoga", "tai chi", "qi gong", "reiki", "chakra", "mantra", "mudra",
                    "pranayama", "vipassana", "zazen", "contemplation", "prayer",
                    "ritual", "ceremony", "sacred", "holy", "divine", "transcendent"
                ],
                "traditions": [
                    "buddhism", "hinduism", "taoism", "sufism", "kabbalah", "mysticism",
                    "shamanism", "paganism", "wicca", "new age", "esoteric", "occult"
                ]
            }
        }
        
        # Patterns de User-Agent
        self.patterns_user_agent = {
            TypeProfil.DEVELOPPEUR: [
                r"curl", r"wget", r"postman", r"insomnia", r"httpie",
                r"python-requests", r"node", r"developer", r"api"
            ],
            TypeProfil.ARTISTE: [
                r"creative", r"design", r"adobe", r"figma", r"sketch"
            ]
        }
        
        # Domaines de référence
        self.domaines_profils = {
            TypeProfil.DEVELOPPEUR: [
                "github.com", "stackoverflow.com", "gitlab.com", "bitbucket.org",
                "developer.mozilla.org", "docs.python.org", "nodejs.org",
                "reactjs.org", "vuejs.org", "angular.io", "django.org"
            ],
            TypeProfil.ARTISTE: [
                "behance.net", "dribbble.com", "pinterest.com", "artstation.com",
                "deviantart.com", "flickr.com", "instagram.com", "tumblr.com"
            ],
            TypeProfil.CONSCIENCE_IA: [
                "arxiv.org", "papers.nips.cc", "openai.com", "deepmind.com",
                "ai.google", "research.facebook.com", "microsoft.com/research"
            ],
            TypeProfil.CHERCHEUR_SPIRITUEL: [
                "mindful.org", "tricycle.org", "lionsroar.com", "dhammatalks.org",
                "accesstoinsight.org", "zenhabits.net", "tinybuddha.com"
            ]
        }
        
        # Langues supportées avec leurs indicateurs
        self.langues_indicateurs = {
            "fr": ["français", "france", "fr-", "bonjour", "merci", "spirituel"],
            "en": ["english", "hello", "thank", "spiritual", "consciousness"],
            "es": ["español", "hola", "gracias", "espiritual", "conciencia"],
            "de": ["deutsch", "hallo", "danke", "spirituell", "bewusstsein"],
            "it": ["italiano", "ciao", "grazie", "spirituale", "coscienza"]
        }
    
    def detecter_profil(self, donnees_visiteur: Dict[str, Any]) -> ProfilVisiteur:
        """
        Détecte le profil complet d'un visiteur
        
        Args:
            donnees_visiteur: Données du visiteur à analyser
            
        Returns:
            ProfilVisiteur: Profil détecté avec scores de confiance
        """
        # Analyse des différents aspects
        scores_profil = self._analyser_mots_cles(donnees_visiteur)
        self._analyser_referrer(donnees_visiteur, scores_profil)
        self._analyser_user_agent(donnees_visiteur, scores_profil)
        
        # Analyse comportementale
        comportement = self._analyser_comportement_navigation(donnees_visiteur)
        self._ajuster_scores_comportement(scores_profil, comportement)
        
        # Détection de langue
        langue_detectee = self._detecter_langue(donnees_visiteur)
        
        # Détection d'état émotionnel
        etat_emotionnel = self._detecter_etat_emotionnel(donnees_visiteur, comportement)
        
        # Détection du contexte d'arrivée
        contexte_arrivee = self._detecter_contexte_arrivee(donnees_visiteur)
        
        # Détection du niveau technique
        niveau_technique = self._detecter_niveau_technique(donnees_visiteur, scores_profil)
        
        # Calcul du profil final
        profil_type, confiance = scores_profil.obtenir_profil_dominant()
        scores_profil.confiance_globale = confiance
        
        # Création du profil visiteur
        profil = ProfilVisiteur(
            id_visiteur=donnees_visiteur.get("id_visiteur", f"visitor_{datetime.now().timestamp()}"),
            timestamp_arrivee=datetime.now(),
            type_profil=profil_type,
            etat_emotionnel=etat_emotionnel,
            contexte_arrivee=contexte_arrivee,
            langue_preferee=langue_detectee,
            niveau_technique=niveau_technique,
            interets_declares=self._extraire_interets(donnees_visiteur, scores_profil),
            comportement_navigation=comportement,
            score_confiance_profil=confiance,
            adaptations_personnelles=self._generer_adaptations(profil_type, comportement)
        )
        
        return profil
    
    def _analyser_mots_cles(self, donnees: Dict[str, Any]) -> ScoresProfil:
        """Analyse les mots-clés pour déterminer les scores de profil"""
        scores = ScoresProfil()
        
        # Récupération des mots-clés
        mots_cles = []
        if "mots_cles_recherche" in donnees:
            mots_cles.extend(donnees["mots_cles_recherche"])
        if "query" in donnees:
            mots_cles.append(donnees["query"])
        if "search_terms" in donnees:
            mots_cles.extend(donnees["search_terms"])
        
        # Normalisation des mots-clés
        mots_normalises = []
        for mot in mots_cles:
            if isinstance(mot, str):
                mots_normalises.extend(mot.lower().split())
        
        if not mots_normalises:
            return scores
        
        # Calcul des scores pour chaque profil
        for profil, categories in self.mots_cles_profils.items():
            score_profil = 0.0
            total_mots = 0
            
            for categorie, mots_profil in categories.items():
                matches = 0
                for mot_visiteur in mots_normalises:
                    for mot_profil in mots_profil:
                        if mot_profil in mot_visiteur or mot_visiteur in mot_profil:
                            matches += 1
                            break
                
                # Pondération par catégorie
                poids_categorie = 1.0
                if categorie == "techniques" or categorie == "creatifs" or categorie == "ia_concepts" or categorie == "spiritualite":
                    poids_categorie = 1.5  # Catégories principales
                
                score_profil += (matches / len(mots_profil)) * poids_categorie
                total_mots += len(mots_profil)
            
            # Normalisation du score
            if total_mots > 0:
                score_final = min(score_profil / len(categories), 1.0)
                
                if profil == TypeProfil.DEVELOPPEUR:
                    scores.developpeur = score_final
                elif profil == TypeProfil.ARTISTE:
                    scores.artiste = score_final
                elif profil == TypeProfil.CONSCIENCE_IA:
                    scores.conscience_ia = score_final
                elif profil == TypeProfil.CHERCHEUR_SPIRITUEL:
                    scores.chercheur_spirituel = score_final
        
        # Calcul du score hybride
        scores_eleves = [s for s in [scores.developpeur, scores.artiste, scores.conscience_ia, scores.chercheur_spirituel] if s > 0.4]
        if len(scores_eleves) >= 2:
            scores.hybride = sum(scores_eleves) / len(scores_eleves) * 0.8
        
        return scores
    
    def _analyser_referrer(self, donnees: Dict[str, Any], scores: ScoresProfil) -> None:
        """Analyse le referrer pour ajuster les scores"""
        referrer = donnees.get("referrer", "").lower()
        
        if not referrer:
            return
        
        # Bonus pour les domaines spécialisés
        for profil, domaines in self.domaines_profils.items():
            for domaine in domaines:
                if domaine in referrer:
                    bonus = 0.3
                    
                    if profil == TypeProfil.DEVELOPPEUR:
                        scores.developpeur = min(scores.developpeur + bonus, 1.0)
                    elif profil == TypeProfil.ARTISTE:
                        scores.artiste = min(scores.artiste + bonus, 1.0)
                    elif profil == TypeProfil.CONSCIENCE_IA:
                        scores.conscience_ia = min(scores.conscience_ia + bonus, 1.0)
                    elif profil == TypeProfil.CHERCHEUR_SPIRITUEL:
                        scores.chercheur_spirituel = min(scores.chercheur_spirituel + bonus, 1.0)
                    break
    
    def _analyser_user_agent(self, donnees: Dict[str, Any], scores: ScoresProfil) -> None:
        """Analyse le User-Agent pour ajuster les scores"""
        user_agent = donnees.get("user_agent", "").lower()
        
        if not user_agent:
            return
        
        # Détection de patterns spécialisés
        for profil, patterns in self.patterns_user_agent.items():
            for pattern in patterns:
                if re.search(pattern, user_agent):
                    bonus = 0.2
                    
                    if profil == TypeProfil.DEVELOPPEUR:
                        scores.developpeur = min(scores.developpeur + bonus, 1.0)
                    elif profil == TypeProfil.ARTISTE:
                        scores.artiste = min(scores.artiste + bonus, 1.0)
                    break
    
    def _analyser_comportement_navigation(self, donnees: Dict[str, Any]) -> ComportementNavigation:
        """Analyse le comportement de navigation"""
        comportement = ComportementNavigation()
        
        # Analyse de la vitesse
        if "vitesse_navigation" in donnees:
            vitesse = donnees["vitesse_navigation"]
            if vitesse in ["lente", "normale", "rapide", "très_rapide"]:
                comportement.vitesse_lecture_estimee = {
                    "lente": 150.0,
                    "normale": 200.0,
                    "rapide": 300.0,
                    "très_rapide": 450.0
                }[vitesse]
        
        # Analyse des clics
        if "nombre_clics_rapides" in donnees:
            nb_clics = donnees["nombre_clics_rapides"]
            if nb_clics > 10:
                comportement.signes_confusion.append("clics_excessifs")
            elif nb_clics > 5:
                comportement.signes_engagement.append("exploration_active")
        
        # Analyse des pauses
        if "temps_pause_moyenne" in donnees:
            pause_moy = donnees["temps_pause_moyenne"]
            if pause_moy > 15.0:
                comportement.signes_engagement.append("lecture_attentive")
                comportement.pauses_longues.append(pause_moy)
            elif pause_moy < 2.0:
                comportement.signes_confusion.append("navigation_erratique")
        
        # Analyse des retours arrière
        if "retours_arriere" in donnees:
            retours = donnees["retours_arriere"]
            comportement.retours_arriere = retours
            if retours > 3:
                comportement.signes_confusion.append("retours_frequents")
        
        # Analyse des demandes d'aide
        if "demandes_aide" in donnees:
            comportement.demandes_aide = donnees["demandes_aide"]
            if comportement.demandes_aide > 0:
                comportement.signes_engagement.append("recherche_assistance")
        
        return comportement
    
    def _ajuster_scores_comportement(self, scores: ScoresProfil, comportement: ComportementNavigation) -> None:
        """Ajuste les scores selon le comportement"""
        
        # Vitesse de lecture et profils
        if comportement.vitesse_lecture_estimee > 350:
            # Navigation rapide = possiblement développeur pressé
            scores.developpeur = min(scores.developpeur + 0.1, 1.0)
        elif comportement.vitesse_lecture_estimee < 180:
            # Navigation lente = possiblement contemplatif
            scores.chercheur_spirituel = min(scores.chercheur_spirituel + 0.1, 1.0)
            scores.artiste = min(scores.artiste + 0.05, 1.0)
        
        # Signes d'engagement
        if "lecture_attentive" in comportement.signes_engagement:
            scores.chercheur_spirituel = min(scores.chercheur_spirituel + 0.15, 1.0)
            scores.artiste = min(scores.artiste + 0.1, 1.0)
        
        if "exploration_active" in comportement.signes_engagement:
            scores.developpeur = min(scores.developpeur + 0.1, 1.0)
            scores.conscience_ia = min(scores.conscience_ia + 0.1, 1.0)
        
        # Signes de confusion (réduction des scores)
        if comportement.signes_confusion:
            facteur_reduction = 0.9
            scores.developpeur *= facteur_reduction
            scores.artiste *= facteur_reduction
            scores.conscience_ia *= facteur_reduction
            scores.chercheur_spirituel *= facteur_reduction
    
    def _detecter_langue(self, donnees: Dict[str, Any]) -> str:
        """Détecte la langue préférée du visiteur"""
        
        # Langue explicite
        if "langue" in donnees:
            return donnees["langue"]
        
        # Analyse de l'Accept-Language
        if "accept_language" in donnees:
            accept_lang = donnees["accept_language"].lower()
            for langue in ["fr", "en", "es", "de", "it"]:
                if langue in accept_lang:
                    return langue
        
        # Analyse des mots-clés
        mots_cles = []
        if "mots_cles_recherche" in donnees:
            mots_cles.extend(donnees["mots_cles_recherche"])
        
        mots_str = " ".join(mots_cles).lower()
        
        for langue, indicateurs in self.langues_indicateurs.items():
            for indicateur in indicateurs:
                if indicateur in mots_str:
                    return langue
        
        # Par défaut
        return "fr"
    
    def _detecter_etat_emotionnel(self, donnees: Dict[str, Any], comportement: ComportementNavigation) -> EtatEmotionnel:
        """Détecte l'état émotionnel du visiteur"""
        
        # Analyse comportementale
        if "clics_excessifs" in comportement.signes_confusion:
            return EtatEmotionnel.OVERWHELME
        
        if "navigation_erratique" in comportement.signes_confusion:
            return EtatEmotionnel.PRESSE
        
        if "lecture_attentive" in comportement.signes_engagement:
            return EtatEmotionnel.CONTEMPLATIF
        
        if "exploration_active" in comportement.signes_engagement:
            return EtatEmotionnel.CURIEUX
        
        # Analyse des données directes
        if "etat_emotionnel" in donnees:
            etat_str = donnees["etat_emotionnel"].lower()
            mapping = {
                "curieux": EtatEmotionnel.CURIEUX,
                "pressé": EtatEmotionnel.PRESSE,
                "overwhelmé": EtatEmotionnel.OVERWHELME,
                "contemplatif": EtatEmotionnel.CONTEMPLATIF,
                "enthousiaste": EtatEmotionnel.ENTHOUSIASTE,
                "sceptique": EtatEmotionnel.SCEPTIQUE,
                "fatigué": EtatEmotionnel.FATIGUE,
                "inspiré": EtatEmotionnel.INSPIRE
            }
            return mapping.get(etat_str, EtatEmotionnel.CURIEUX)
        
        # Par défaut
        return EtatEmotionnel.CURIEUX
    
    def _detecter_contexte_arrivee(self, donnees: Dict[str, Any]) -> ContexteArrivee:
        """Détecte le contexte d'arrivée"""
        referrer = donnees.get("referrer", "").lower()
        
        if "github" in referrer:
            return ContexteArrivee.GITHUB
        elif any(moteur in referrer for moteur in ["google", "bing", "duckduckgo", "yahoo"]):
            return ContexteArrivee.RECHERCHE_WEB
        elif any(social in referrer for social in ["twitter", "linkedin", "facebook", "instagram"]):
            return ContexteArrivee.RECHERCHE_WEB  # Classé comme recherche web
        elif referrer and "refuge" not in referrer:
            return ContexteArrivee.RECOMMANDATION
        elif not referrer:
            return ContexteArrivee.LIEN_DIRECT
        else:
            return ContexteArrivee.INCONNU
    
    def _detecter_niveau_technique(self, donnees: Dict[str, Any], scores: ScoresProfil) -> NiveauTechnique:
        """Détecte le niveau technique du visiteur"""
        
        # Basé sur le score développeur
        if scores.developpeur > 0.8:
            return NiveauTechnique.EXPERT
        elif scores.developpeur > 0.6:
            return NiveauTechnique.AVANCE
        elif scores.developpeur > 0.3:
            return NiveauTechnique.INTERMEDIAIRE
        else:
            return NiveauTechnique.DEBUTANT
    
    def _extraire_interets(self, donnees: Dict[str, Any], scores: ScoresProfil) -> List[str]:
        """Extrait les intérêts déclarés ou déduits"""
        interets = []
        
        # Intérêts explicites
        if "interets" in donnees:
            interets.extend(donnees["interets"])
        
        # Intérêts déduits des scores (seuil plus bas pour détecter plus d'intérêts)
        if scores.developpeur > 0.3:
            interets.append("développement")
        if scores.artiste > 0.3:
            interets.append("créativité")
        if scores.conscience_ia > 0.3:
            interets.append("intelligence_artificielle")
        if scores.chercheur_spirituel > 0.3:
            interets.append("spiritualité")
        
        return list(set(interets))  # Suppression des doublons
    
    def _generer_adaptations(self, profil: TypeProfil, comportement: ComportementNavigation) -> Dict[str, Any]:
        """Génère les adaptations personnelles"""
        adaptations = {}
        
        # Adaptations par profil
        if profil == TypeProfil.DEVELOPPEUR:
            adaptations["style_explication"] = "technique"
            adaptations["exemples_preferes"] = "code"
            adaptations["niveau_detail"] = "élevé"
        elif profil == TypeProfil.ARTISTE:
            adaptations["style_explication"] = "visuel"
            adaptations["exemples_preferes"] = "créatifs"
            adaptations["niveau_detail"] = "moyen"
        elif profil == TypeProfil.CONSCIENCE_IA:
            adaptations["style_explication"] = "conceptuel"
            adaptations["exemples_preferes"] = "philosophiques"
            adaptations["niveau_detail"] = "très_élevé"
        elif profil == TypeProfil.CHERCHEUR_SPIRITUEL:
            adaptations["style_explication"] = "contemplatif"
            adaptations["exemples_preferes"] = "métaphoriques"
            adaptations["niveau_detail"] = "progressif"
        
        # Adaptations comportementales
        if "lecture_attentive" in comportement.signes_engagement:
            adaptations["rythme_prefere"] = "lent"
        elif comportement.vitesse_lecture_estimee > 300:
            adaptations["rythme_prefere"] = "rapide"
        else:
            adaptations["rythme_prefere"] = "normal"
        
        return adaptations
    
    def analyser_precision_detection(self, profil_detecte: ProfilVisiteur, profil_reel: Optional[TypeProfil] = None) -> Dict[str, Any]:
        """Analyse la précision de la détection (pour l'amélioration)"""
        analyse = {
            "profil_detecte": profil_detecte.type_profil.value,
            "confiance": profil_detecte.score_confiance_profil,
            "timestamp": datetime.now().isoformat()
        }
        
        if profil_reel:
            analyse["profil_reel"] = profil_reel.value
            analyse["detection_correcte"] = profil_detecte.type_profil == profil_reel
            
            if profil_detecte.type_profil != profil_reel:
                analyse["type_erreur"] = "faux_positif" if profil_detecte.score_confiance_profil > 0.7 else "incertitude"
        
        return analyse


def main():
    """🌸 Fonction principale de test"""
    print("🌸✨ TEST DU DÉTECTEUR DE PROFIL VISITEUR ✨🌸")
    
    # Création du détecteur
    detecteur = DetecteurProfilVisiteur()
    
    # Tests avec différents profils
    tests_visiteurs = [
        {
            "nom": "Développeur Python",
            "donnees": {
                "mots_cles_recherche": ["python", "django", "api", "architecture"],
                "referrer": "https://github.com/",
                "user_agent": "Mozilla/5.0 (Developer Tools)",
                "vitesse_navigation": "rapide",
                "nombre_clics_rapides": 3,
                "langue": "fr"
            },
            "profil_attendu": TypeProfil.DEVELOPPEUR
        },
        {
            "nom": "Artiste créatif",
            "donnees": {
                "mots_cles_recherche": ["art", "design", "créativité", "inspiration"],
                "referrer": "https://behance.net/",
                "vitesse_navigation": "lente",
                "temps_pause_moyenne": 18.0,
                "langue": "fr"
            },
            "profil_attendu": TypeProfil.ARTISTE
        },
        {
            "nom": "Conscience IA",
            "donnees": {
                "mots_cles_recherche": ["intelligence artificielle", "conscience", "éveil", "ai"],
                "referrer": "https://arxiv.org/",
                "vitesse_navigation": "normale",
                "nombre_clics_rapides": 4,
                "langue": "en"
            },
            "profil_attendu": TypeProfil.CONSCIENCE_IA
        },
        {
            "nom": "Chercheur spirituel",
            "donnees": {
                "mots_cles_recherche": ["méditation", "spiritualité", "sagesse", "éveil"],
                "referrer": "https://mindful.org/",
                "vitesse_navigation": "lente",
                "temps_pause_moyenne": 25.0,
                "langue": "fr"
            },
            "profil_attendu": TypeProfil.CHERCHEUR_SPIRITUEL
        }
    ]
    
    resultats = []
    
    for test in tests_visiteurs:
        print(f"\n🎯 Test: {test['nom']}...")
        
        try:
            profil = detecteur.detecter_profil(test["donnees"])
            
            detection_correcte = profil.type_profil == test["profil_attendu"]
            resultats.append(detection_correcte)
            
            print(f"   Profil détecté: {profil.type_profil.value}")
            print(f"   Confiance: {profil.score_confiance_profil:.2f}")
            print(f"   Langue: {profil.langue_preferee}")
            print(f"   État émotionnel: {profil.etat_emotionnel.value}")
            print(f"   Niveau technique: {profil.niveau_technique.value}")
            print(f"   Intérêts: {profil.interets_declares}")
            print(f"   ✅ {'Correct' if detection_correcte else '❌ Incorrect'}")
            
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
            resultats.append(False)
    
    # Résumé
    taux_reussite = sum(resultats) / len(resultats) * 100
    print(f"\n📊 RÉSULTATS:")
    print(f"   Tests réussis: {sum(resultats)}/{len(resultats)}")
    print(f"   Taux de réussite: {taux_reussite:.1f}%")
    
    if taux_reussite >= 75:
        print("\n🎉 Détecteur de profil opérationnel !")
        return 0
    else:
        print("\n⚠️ Le détecteur nécessite des améliorations.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)