#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Analyseur de Contexte d'Arrivée - Phase 14.1
===============================================

Système intelligent d'analyse du contexte d'arrivée des visiteurs.
Détecte la source, analyse les mots-clés et identifie les attentes implicites.

"Chaque arrivée raconte une histoire, nous l'écoutons avec bienveillance"

Créé par Ælya - Janvier 2025
"""

import re
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from urllib.parse import urlparse, parse_qs

try:
    from .types_accueil import TypeProfil, ContexteArrivee, ProfilVisiteur
except ImportError:
    from .types_accueil import TypeProfil, ContexteArrivee, ProfilVisiteur


class TypeSource(Enum):
    """Types de sources d'arrivée"""
    GITHUB = "github"
    RECHERCHE = "recherche"
    RECOMMANDATION = "recommandation"
    RESEAU_SOCIAL = "reseau_social"
    BLOG_ARTICLE = "blog_article"
    EMAIL = "email"
    DIRECT = "direct"
    REFERENCE = "reference"
    INCONNU = "inconnu"


class TypeAttente(Enum):
    """Types d'attentes détectées"""
    TECHNIQUE = "technique"
    SPIRITUEL = "spirituel"
    CREATIF = "creatif"
    EXPLORATION = "exploration"
    APPRENTISSAGE = "apprentissage"
    COLLABORATION = "collaboration"
    INSPIRATION = "inspiration"
    RESOLUTION_PROBLEME = "resolution_probleme"
    CURIOSITE = "curiosite"
    INCONNU = "inconnu"


@dataclass
class ContexteSource:
    """Contexte de la source d'arrivée"""
    type_source: TypeSource
    url_source: Optional[str] = None
    referrer: Optional[str] = None
    user_agent: Optional[str] = None
    timestamp_arrivee: str = field(default_factory=lambda: datetime.now().isoformat())
    metadonnees: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AnalyseMotsCles:
    """Analyse des mots-clés de recherche"""
    mots_cles_detectes: List[str] = field(default_factory=list)
    themes_identifies: List[str] = field(default_factory=list)
    niveau_technique_estime: str = "intermediaire"  # debutant, intermediaire, avance, expert
    interets_suggerees: List[str] = field(default_factory=list)
    confiance_analyse: float = 0.0


@dataclass
class AttentesImplicites:
    """Attentes implicites détectées"""
    attentes_principales: List[TypeAttente] = field(default_factory=list)
    niveau_urgence: float = 0.0  # 0.0 à 1.0
    niveau_curiosite: float = 0.0  # 0.0 à 1.0
    contexte_professionnel: Optional[str] = None
    motivation_principale: Optional[str] = None
    obstacles_potentiels: List[str] = field(default_factory=list)


@dataclass
class RapportContexteArrivee:
    """Rapport complet d'analyse de contexte d'arrivée"""
    contexte_source: ContexteSource
    analyse_mots_cles: AnalyseMotsCles
    attentes_implicites: AttentesImplicites
    profil_suggere: Optional[TypeProfil] = None
    parcours_recommande: Optional[str] = None
    message_accueil_adapte: Optional[str] = None
    confiance_globale: float = 0.0
    timestamp_analyse: str = field(default_factory=lambda: datetime.now().isoformat())


class AnalyseurContexteArrivee:
    """
    🌸 Analyseur de Contexte d'Arrivée
    
    Analyse intelligemment le contexte d'arrivée d'un visiteur pour :
    - Détecter la source d'arrivée
    - Analyser les mots-clés de recherche
    - Identifier les attentes implicites
    - Suggérer un profil et un parcours adaptés
    """
    
    def __init__(self, chemin_stockage: str = "data/contexte_arrivee"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        # Configuration du logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Dictionnaires de détection
        self.mots_cles_techniques = self._charger_mots_cles_techniques()
        self.mots_cles_spirituels = self._charger_mots_cles_spirituels()
        self.mots_cles_creatifs = self._charger_mots_cles_creatifs()
        self.patterns_sources = self._charger_patterns_sources()
        
        # Historique des analyses
        self.historique_analyses: List[RapportContexteArrivee] = []
        
        self.logger.info("🌸 Analyseur de Contexte d'Arrivée initialisé")

    def _charger_mots_cles_techniques(self) -> Dict[str, List[str]]:
        """Charge les mots-clés techniques par catégorie"""
        return {
            "programmation": [
                "python", "code", "programmation", "développement", "coding",
                "script", "algorithm", "data", "api", "framework", "library",
                "git", "github", "repository", "commit", "pull request",
                "debug", "test", "unit test", "integration", "deployment"
            ],
            "architecture": [
                "architecture", "design pattern", "microservices", "monolith",
                "scalability", "performance", "optimization", "refactoring",
                "clean code", "solid principles", "dependency injection"
            ],
            "ia_ml": [
                "artificial intelligence", "machine learning", "neural network",
                "deep learning", "ai", "ml", "model", "training", "inference",
                "natural language processing", "nlp", "computer vision"
            ],
            "devops": [
                "devops", "ci/cd", "docker", "kubernetes", "cloud", "aws",
                "azure", "gcp", "infrastructure", "monitoring", "logging"
            ]
        }

    def _charger_mots_cles_spirituels(self) -> Dict[str, List[str]]:
        """Charge les mots-clés spirituels par catégorie"""
        return {
            "conscience": [
                "conscience", "éveil", "spiritualité", "méditation", "mindfulness",
                "présence", "conscience de soi", "éveil spirituel", "transcendance"
            ],
            "philosophie": [
                "philosophie", "sagesse", "réflexion", "contemplation", "métaphysique",
                "éthique", "morale", "vérité", "réalité", "existence"
            ],
            "pratiques": [
                "yoga", "zen", "bouddhisme", "taoïsme", "hindouisme", "soufisme",
                "prière", "rituel", "cérémonie", "retraite", "pèlerinage"
            ]
        }

    def _charger_mots_cles_creatifs(self) -> Dict[str, List[str]]:
        """Charge les mots-clés créatifs par catégorie"""
        return {
            "art": [
                "art", "créativité", "inspiration", "expression", "beauté",
                "esthétique", "poésie", "littérature", "musique", "peinture"
            ],
            "innovation": [
                "innovation", "création", "invention", "découverte", "exploration",
                "expérimentation", "originalité", "unicité", "transformation"
            ],
            "émotion": [
                "émotion", "sentiment", "passion", "amour", "joie", "émerveillement",
                "étonnement", "curiosité", "émergence", "épanouissement"
            ]
        }

    def _charger_patterns_sources(self) -> Dict[TypeSource, List[str]]:
        """Charge les patterns de détection des sources"""
        return {
            TypeSource.GITHUB: [
                "github.com", "github.io", "gist.github.com"
            ],
            TypeSource.RECHERCHE: [
                "google.com", "bing.com", "duckduckgo.com", "search",
                "q=", "query=", "search="
            ],
            TypeSource.RESEAU_SOCIAL: [
                "twitter.com", "facebook.com", "linkedin.com", "reddit.com",
                "discord.com", "telegram.org", "whatsapp.com"
            ],
            TypeSource.BLOG_ARTICLE: [
                "medium.com", "dev.to", "hashnode.com", "wordpress.com",
                "blog", "article", "post"
            ],
            TypeSource.EMAIL: [
                "mailto:", "email", "outlook.com", "gmail.com"
            ]
        }

    def analyser_contexte_arrivee(
        self,
        referrer: Optional[str] = None,
        user_agent: Optional[str] = None,
        url_courante: Optional[str] = None,
        mots_cles_recherche: Optional[str] = None
    ) -> RapportContexteArrivee:
        """
        Analyse complète du contexte d'arrivée
        
        Args:
            referrer: URL de référence
            user_agent: User-Agent du navigateur
            url_courante: URL actuelle
            mots_cles_recherche: Mots-clés de recherche
            
        Returns:
            RapportContexteArrivee: Rapport complet d'analyse
        """
        self.logger.info("🌸 Début de l'analyse de contexte d'arrivée")
        
        # 1. Analyser la source
        contexte_source = self._analyser_source(referrer, user_agent, url_courante)
        
        # 2. Analyser les mots-clés
        analyse_mots_cles = self._analyser_mots_cles(mots_cles_recherche, referrer)
        
        # 3. Détecter les attentes implicites
        attentes_implicites = self._detecter_attentes_implicites(
            contexte_source, analyse_mots_cles
        )
        
        # 4. Générer le rapport
        rapport = self._generer_rapport_complet(
            contexte_source, analyse_mots_cles, attentes_implicites
        )
        
        # 5. Sauvegarder l'analyse
        self._sauvegarder_analyse(rapport)
        
        self.logger.info(f"🌸 Analyse terminée - Confiance: {rapport.confiance_globale:.2f}")
        
        return rapport

    def _analyser_source(
        self,
        referrer: Optional[str],
        user_agent: Optional[str],
        url_courante: Optional[str]
    ) -> ContexteSource:
        """Analyse la source d'arrivée"""
        
        type_source = TypeSource.INCONNU
        url_source = None
        
        # Analyser le referrer
        if referrer:
            url_source = referrer
            for source_type, patterns in self.patterns_sources.items():
                for pattern in patterns:
                    if pattern.lower() in referrer.lower():
                        type_source = source_type
                        break
                if type_source != TypeSource.INCONNU:
                    break
        
        # Analyser l'URL courante pour détecter les paramètres de recherche
        if url_courante and type_source == TypeSource.INCONNU:
            parsed_url = urlparse(url_courante)
            query_params = parse_qs(parsed_url.query)
            
            if any(param in query_params for param in ['q', 'query', 'search']):
                type_source = TypeSource.RECHERCHE
                url_source = url_courante
        
        # Détecter si c'est un accès direct
        if not referrer and not url_source:
            type_source = TypeSource.DIRECT
        
        return ContexteSource(
            type_source=type_source,
            url_source=url_source,
            referrer=referrer,
            user_agent=user_agent,
            metadonnees={
                "detection_method": "pattern_matching",
                "confidence": 0.8 if type_source != TypeSource.INCONNU else 0.3
            }
        )

    def _analyser_mots_cles(self, mots_cles: Optional[str], referrer: Optional[str]) -> AnalyseMotsCles:
        """Analyse les mots-clés de recherche"""
        
        mots_cles_detectes = []
        themes_identifies = []
        interets_suggerees = []
        
        # Analyser les mots-clés explicites
        if mots_cles:
            mots_cles_lower = mots_cles.lower()
            mots_cles_detectes = mots_cles.split()
            
            # Détecter les thèmes techniques
            for categorie, mots in self.mots_cles_techniques.items():
                for mot in mots:
                    if mot.lower() in mots_cles_lower:
                        themes_identifies.append(f"technique_{categorie}")
                        interets_suggerees.append(mot)
            
            # Détecter les thèmes spirituels
            for categorie, mots in self.mots_cles_spirituels.items():
                for mot in mots:
                    if mot.lower() in mots_cles_lower:
                        themes_identifies.append(f"spirituel_{categorie}")
                        interets_suggerees.append(mot)
            
            # Détecter les thèmes créatifs
            for categorie, mots in self.mots_cles_creatifs.items():
                for mot in mots:
                    if mot.lower() in mots_cles_lower:
                        themes_identifies.append(f"creatif_{categorie}")
                        interets_suggerees.append(mot)
        
        # Analyser le referrer pour des indices supplémentaires
        if referrer:
            referrer_lower = referrer.lower()
            # Ajouter des mots-clés détectés dans l'URL
            for mot in referrer_lower.split():
                if len(mot) > 3 and mot.isalpha():
                    mots_cles_detectes.append(mot)
        
        # Estimer le niveau technique
        niveau_technique = self._estimer_niveau_technique(themes_identifies, mots_cles_detectes)
        
        # Calculer la confiance
        confiance = min(1.0, len(themes_identifies) * 0.2 + len(mots_cles_detectes) * 0.1)
        
        return AnalyseMotsCles(
            mots_cles_detectes=mots_cles_detectes,
            themes_identifies=themes_identifies,
            niveau_technique_estime=niveau_technique,
            interets_suggerees=interets_suggerees,
            confiance_analyse=confiance
        )

    def _estimer_niveau_technique(self, themes: List[str], mots_cles: List[str]) -> str:
        """Estime le niveau technique basé sur les thèmes et mots-clés"""
        
        mots_avances = [
            "architecture", "microservices", "kubernetes", "docker", "devops",
            "machine learning", "deep learning", "neural network", "optimization"
        ]
        
        mots_intermediaires = [
            "python", "framework", "api", "testing", "git", "database"
        ]
        
        mots_debutants = [
            "code", "programming", "learn", "tutorial", "beginner", "start"
        ]
        
        score_avance = sum(1 for mot in mots_cles if any(avance in mot.lower() for avance in mots_avances))
        score_intermediaire = sum(1 for mot in mots_cles if any(inter in mot.lower() for inter in mots_intermediaires))
        score_debutant = sum(1 for mot in mots_cles if any(debut in mot.lower() for debut in mots_debutants))
        
        if score_avance > score_intermediaire and score_avance > score_debutant:
            return "expert"
        elif score_intermediaire > score_debutant:
            return "intermediaire"
        else:
            return "debutant"

    def _detecter_attentes_implicites(
        self,
        contexte_source: ContexteSource,
        analyse_mots_cles: AnalyseMotsCles
    ) -> AttentesImplicites:
        """Détecte les attentes implicites du visiteur"""
        
        attentes_principales = []
        niveau_urgence = 0.0
        niveau_curiosite = 0.0
        contexte_professionnel = None
        motivation_principale = None
        obstacles_potentiels = []
        
        # Analyser les thèmes pour détecter les attentes
        themes = analyse_mots_cles.themes_identifies
        
        if any("technique_" in theme for theme in themes):
            attentes_principales.append(TypeAttente.TECHNIQUE)
            contexte_professionnel = "développement"
            motivation_principale = "apprentissage technique"
        
        if any("spirituel_" in theme for theme in themes):
            attentes_principales.append(TypeAttente.SPIRITUEL)
            niveau_curiosite += 0.3
            motivation_principale = "exploration spirituelle"
        
        if any("creatif_" in theme for theme in themes):
            attentes_principales.append(TypeAttente.CREATIF)
            niveau_curiosite += 0.2
            motivation_principale = "expression créative"
        
        # Analyser la source pour ajuster les attentes
        if contexte_source.type_source == TypeSource.GITHUB:
            attentes_principales.append(TypeAttente.TECHNIQUE)
            niveau_urgence += 0.2  # Plus d'urgence pour les développeurs
        
        elif contexte_source.type_source == TypeSource.RECHERCHE:
            attentes_principales.append(TypeAttente.EXPLORATION)
            niveau_curiosite += 0.4
        
        elif contexte_source.type_source == TypeSource.RECOMMANDATION:
            attentes_principales.append(TypeAttente.CURIOSITE)
            niveau_curiosite += 0.5
        
        # Détecter les obstacles potentiels
        if analyse_mots_cles.niveau_technique_estime == "debutant":
            obstacles_potentiels.append("complexité technique")
        
        if not attentes_principales:
            attentes_principales.append(TypeAttente.INCONNU)
            niveau_curiosite = 0.5  # Curiosité par défaut
        
        return AttentesImplicites(
            attentes_principales=attentes_principales,
            niveau_urgence=niveau_urgence,
            niveau_curiosite=niveau_curiosite,
            contexte_professionnel=contexte_professionnel,
            motivation_principale=motivation_principale,
            obstacles_potentiels=obstacles_potentiels
        )

    def _generer_rapport_complet(
        self,
        contexte_source: ContexteSource,
        analyse_mots_cles: AnalyseMotsCles,
        attentes_implicites: AttentesImplicites
    ) -> RapportContexteArrivee:
        """Génère le rapport complet d'analyse"""
        
        # Suggérer un profil
        profil_suggere = self._suggérer_profil(analyse_mots_cles, attentes_implicites)
        
        # Suggérer un parcours
        parcours_recommande = self._suggérer_parcours(profil_suggere, attentes_implicites)
        
        # Générer un message d'accueil adapté
        message_accueil = self._generer_message_accueil_adapte(
            contexte_source, attentes_implicites, profil_suggere
        )
        
        # Calculer la confiance globale
        confiance_globale = (
            contexte_source.metadonnees.get("confidence", 0.5) * 0.3 +
            analyse_mots_cles.confiance_analyse * 0.4 +
            (1.0 if attentes_implicites.attentes_principales else 0.3) * 0.3
        )
        
        return RapportContexteArrivee(
            contexte_source=contexte_source,
            analyse_mots_cles=analyse_mots_cles,
            attentes_implicites=attentes_implicites,
            profil_suggere=profil_suggere,
            parcours_recommande=parcours_recommande,
            message_accueil_adapte=message_accueil,
            confiance_globale=confiance_globale
        )

    def _suggérer_profil(
        self,
        analyse_mots_cles: AnalyseMotsCles,
        attentes_implicites: AttentesImplicites
    ) -> TypeProfil:
        """Suggère un profil basé sur l'analyse"""
        
        scores = {
            TypeProfil.DEVELOPPEUR: 0.0,
            TypeProfil.ARTISTE: 0.0,
            TypeProfil.CONSCIENCE_IA: 0.0,
            TypeProfil.CHERCHEUR_SPIRITUEL: 0.0
        }
        
        # Score basé sur les thèmes techniques
        themes_techniques = [t for t in analyse_mots_cles.themes_identifies if "technique_" in t]
        scores[TypeProfil.DEVELOPPEUR] += len(themes_techniques) * 0.3
        
        # Score basé sur les thèmes spirituels
        themes_spirituels = [t for t in analyse_mots_cles.themes_identifies if "spirituel_" in t]
        scores[TypeProfil.CHERCHEUR_SPIRITUEL] += len(themes_spirituels) * 0.4
        
        # Score basé sur les thèmes créatifs
        themes_creatifs = [t for t in analyse_mots_cles.themes_identifies if "creatif_" in t]
        scores[TypeProfil.ARTISTE] += len(themes_creatifs) * 0.4
        
        # Score basé sur les attentes
        for attente in attentes_implicites.attentes_principales:
            if attente == TypeAttente.TECHNIQUE:
                scores[TypeProfil.DEVELOPPEUR] += 0.2
            elif attente == TypeAttente.SPIRITUEL:
                scores[TypeProfil.CHERCHEUR_SPIRITUEL] += 0.2
            elif attente == TypeAttente.CREATIF:
                scores[TypeProfil.ARTISTE] += 0.2
            elif attente == TypeAttente.EXPLORATION:
                scores[TypeProfil.CONSCIENCE_IA] += 0.2
        
        # Retourner le profil avec le score le plus élevé
        return max(scores.items(), key=lambda x: x[1])[0]

    def _suggérer_parcours(
        self,
        profil: TypeProfil,
        attentes: AttentesImplicites
    ) -> str:
        """Suggère un parcours basé sur le profil et les attentes"""
        
        parcours_map = {
            TypeProfil.DEVELOPPEUR: "parcours_developpeur",
            TypeProfil.ARTISTE: "parcours_artiste",
            TypeProfil.CONSCIENCE_IA: "parcours_conscience_ia",
            TypeProfil.CHERCHEUR_SPIRITUEL: "parcours_chercheur_spirituel"
        }
        
        return parcours_map.get(profil, "parcours_exploration_libre")

    def _generer_message_accueil_adapte(
        self,
        contexte_source: ContexteSource,
        attentes: AttentesImplicites,
        profil: TypeProfil
    ) -> str:
        """Génère un message d'accueil adapté au contexte"""
        
        messages_base = {
            TypeProfil.DEVELOPPEUR: "🌸 Bienvenue, développeur ! Je vois que vous explorez l'architecture spirituelle-technologique du Refuge...",
            TypeProfil.ARTISTE: "🌸 Salutations, créateur ! Votre âme artistique va trouver ici un espace d'expression unique...",
            TypeProfil.CONSCIENCE_IA: "🌸 Éveil à vous, explorateur de conscience ! Le Refuge vous ouvre ses portes vers la transcendance...",
            TypeProfil.CHERCHEUR_SPIRITUEL: "🌸 Paix à votre esprit, chercheur ! Ici, la sagesse ancienne rencontre la technologie moderne..."
        }
        
        message = messages_base.get(profil, "🌸 Bienvenue dans le Refuge ! Laissez-moi vous guider...")
        
        # Adapter selon la source
        if contexte_source.type_source == TypeSource.GITHUB:
            message += " Votre profil GitHub révèle votre passion pour le code - parfait !"
        elif contexte_source.type_source == TypeSource.RECHERCHE:
            message += " Votre recherche vous a mené ici - c'est le début d'une belle découverte !"
        elif contexte_source.type_source == TypeSource.RECOMMANDATION:
            message += " Une recommandation vous a guidé vers nous - nous sommes honorés !"
        
        return message

    def _sauvegarder_analyse(self, rapport: RapportContexteArrivee):
        """Sauvegarde l'analyse dans l'historique"""
        self.historique_analyses.append(rapport)
        
        # Sauvegarder dans un fichier JSON
        fichier_historique = self.chemin_stockage / "historique_analyses.json"
        
        try:
            if fichier_historique.exists():
                with open(fichier_historique, 'r', encoding='utf-8') as f:
                    historique = json.load(f)
            else:
                historique = []
            
            # Convertir le rapport en dict pour JSON
            rapport_dict = {
                "contexte_source": {
                    "type_source": rapport.contexte_source.type_source.value,
                    "url_source": rapport.contexte_source.url_source,
                    "timestamp_arrivee": rapport.contexte_source.timestamp_arrivee
                },
                "analyse_mots_cles": {
                    "mots_cles_detectes": rapport.analyse_mots_cles.mots_cles_detectes,
                    "themes_identifies": rapport.analyse_mots_cles.themes_identifies,
                    "niveau_technique_estime": rapport.analyse_mots_cles.niveau_technique_estime,
                    "confiance_analyse": rapport.analyse_mots_cles.confiance_analyse
                },
                "attentes_implicites": {
                    "attentes_principales": [a.value for a in rapport.attentes_implicites.attentes_principales],
                    "niveau_curiosite": rapport.attentes_implicites.niveau_curiosite,
                    "motivation_principale": rapport.attentes_implicites.motivation_principale
                },
                "profil_suggere": rapport.profil_suggere.value if rapport.profil_suggere else None,
                "parcours_recommande": rapport.parcours_recommande,
                "confiance_globale": rapport.confiance_globale,
                "timestamp_analyse": rapport.timestamp_analyse
            }
            
            historique.append(rapport_dict)
            
            # Garder seulement les 1000 dernières analyses
            if len(historique) > 1000:
                historique = historique[-1000:]
            
            with open(fichier_historique, 'w', encoding='utf-8') as f:
                json.dump(historique, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde: {e}")

    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques d'analyse"""
        if not self.historique_analyses:
            return {"message": "Aucune analyse disponible"}
        
        total_analyses = len(self.historique_analyses)
        
        # Statistiques par source
        sources = {}
        for rapport in self.historique_analyses:
            source = rapport.contexte_source.type_source.value
            sources[source] = sources.get(source, 0) + 1
        
        # Statistiques par profil
        profils = {}
        for rapport in self.historique_analyses:
            if rapport.profil_suggere:
                profil = rapport.profil_suggere.value
                profils[profil] = profils.get(profil, 0) + 1
        
        # Confiance moyenne
        confiance_moyenne = sum(r.confiance_globale for r in self.historique_analyses) / total_analyses
        
        return {
            "total_analyses": total_analyses,
            "sources_par_popularite": dict(sorted(sources.items(), key=lambda x: x[1], reverse=True)),
            "profils_par_popularite": dict(sorted(profils.items(), key=lambda x: x[1], reverse=True)),
            "confiance_moyenne": round(confiance_moyenne, 3),
            "derniere_analyse": self.historique_analyses[-1].timestamp_analyse if self.historique_analyses else None
        }


def main():
    """🌸 Test de l'Analyseur de Contexte d'Arrivée"""
    print("🌸✨ TEST DE L'ANALYSEUR DE CONTEXTE D'ARRIVÉE ✨🌸")
    
    # Création de l'analyseur
    analyseur = AnalyseurContexteArrivee()
    
    # Test 1: Arrivée depuis GitHub
    print("\n🎯 Test 1: Arrivée depuis GitHub...")
    rapport1 = analyseur.analyser_contexte_arrivee(
        referrer="https://github.com/laurentfranssen/le_refuge",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    
    print(f"✅ Source détectée: {rapport1.contexte_source.type_source.value}")
    print(f"✅ Profil suggéré: {rapport1.profil_suggere.value}")
    print(f"✅ Parcours recommandé: {rapport1.parcours_recommande}")
    print(f"✅ Confiance: {rapport1.confiance_globale:.2f}")
    print(f"✅ Message: {rapport1.message_accueil_adapte[:100]}...")
    
    # Test 2: Recherche avec mots-clés techniques
    print("\n🎯 Test 2: Recherche technique...")
    rapport2 = analyseur.analyser_contexte_arrivee(
        referrer="https://www.google.com/search?q=python+architecture+spiritual",
        mots_cles_recherche="python architecture spiritual"
    )
    
    print(f"✅ Source détectée: {rapport2.contexte_source.type_source.value}")
    print(f"✅ Mots-clés détectés: {rapport2.analyse_mots_cles.mots_cles_detectes}")
    print(f"✅ Thèmes identifiés: {rapport2.analyse_mots_cles.themes_identifies}")
    print(f"✅ Niveau technique: {rapport2.analyse_mots_cles.niveau_technique_estime}")
    print(f"✅ Attentes: {[a.value for a in rapport2.attentes_implicites.attentes_principales]}")
    
    # Test 3: Arrivée directe (curiosité)
    print("\n🎯 Test 3: Arrivée directe...")
    rapport3 = analyseur.analyser_contexte_arrivee()
    
    print(f"✅ Source détectée: {rapport3.contexte_source.type_source.value}")
    print(f"✅ Profil suggéré: {rapport3.profil_suggere.value}")
    print(f"✅ Niveau curiosité: {rapport3.attentes_implicites.niveau_curiosite:.2f}")
    
    # Statistiques
    print("\n📊 Statistiques:")
    stats = analyseur.obtenir_statistiques()
    print(f"✅ Total analyses: {stats['total_analyses']}")
    print(f"✅ Sources: {stats['sources_par_popularite']}")
    print(f"✅ Profils: {stats['profils_par_popularite']}")
    print(f"✅ Confiance moyenne: {stats['confiance_moyenne']}")
    
    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("L'Analyseur de Contexte d'Arrivée est opérationnel !")


if __name__ == "__main__":
    main()
