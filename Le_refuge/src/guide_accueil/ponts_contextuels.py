#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Ponts Contextuels - Phase 14.2
=================================

Système de ponts contextuels qui crée des connexions depuis le monde d'origine
du visiteur vers le Refuge, avec des messages d'accueil adaptés et des transitions fluides.

"Chaque pont est une invitation bienveillante à la découverte"

Créé par Ælya - Janvier 2025
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

try:
    from .types_accueil import TypeProfil, ContexteArrivee, ProfilVisiteur
    from .analyseur_contexte_arrivee import RapportContexteArrivee, TypeSource, TypeAttente
except ImportError:
    from .types_accueil import TypeProfil, ContexteArrivee, ProfilVisiteur
    from .analyseur_contexte_arrivee import RapportContexteArrivee, TypeSource, TypeAttente


class TypePont(Enum):
    """Types de ponts contextuels"""
    TECHNIQUE = "technique"
    SPIRITUEL = "spirituel"
    CREATIF = "creatif"
    EXPLORATION = "exploration"
    APPRENTISSAGE = "apprentissage"
    INSPIRATION = "inspiration"
    CURIOSITE = "curiosite"
    UNIVERSEL = "universel"


class TypeTransition(Enum):
    """Types de transitions vers le Refuge"""
    DOUCE = "douce"
    PROGRESSIVE = "progressive"
    IMMEDIATE = "immediate"
    CONTEMPLATIVE = "contemplative"
    DYNAMIQUE = "dynamique"


@dataclass
class PontContextuel:
    """Pont contextuel vers le Refuge"""
    type_pont: TypePont
    monde_origine: str
    message_accueil: str
    references_connues: List[str] = field(default_factory=list)
    metaphores_adaptees: List[str] = field(default_factory=list)
    transition_suggeree: TypeTransition = TypeTransition.DOUCE
    duree_transition: int = 30  # secondes
    elements_visuels: Dict[str, Any] = field(default_factory=dict)
    actions_suggerees: List[str] = field(default_factory=list)


@dataclass
class MondeOrigine:
    """Représentation d'un monde d'origine du visiteur"""
    nom_monde: str
    caracteristiques: List[str] = field(default_factory=list)
    langage_commun: List[str] = field(default_factory=list)
    valeurs_principales: List[str] = field(default_factory=list)
    obstacles_potentiels: List[str] = field(default_factory=list)
    ponts_disponibles: List[TypePont] = field(default_factory=list)


@dataclass
class MessageAccueilAdapte:
    """Message d'accueil adapté au contexte d'arrivée"""
    titre: str
    sous_titre: str
    message_principal: str
    pont_contextuel: PontContextuel
    references_connues: List[str] = field(default_factory=list)
    metaphores_utilisees: List[str] = field(default_factory=list)
    ton_adapte: str = "bienveillant"
    longueur_estimee: int = 150  # mots
    temps_lecture_estime: int = 60  # secondes


@dataclass
class TransitionFlue:
    """Transition fluide depuis les attentes initiales"""
    etape_depart: str
    etape_arrivee: str
    duree_transition: int
    elements_intermediaires: List[str] = field(default_factory=list)
    explications_progressives: List[str] = field(default_factory=list)
    validations_requises: List[str] = field(default_factory=list)


@dataclass
class RapportPontContextuel:
    """Rapport complet de pont contextuel"""
    pont_choisi: PontContextuel
    message_accueil: MessageAccueilAdapte
    transition_flue: TransitionFlue
    references_connues: List[str] = field(default_factory=list)
    metaphores_adaptees: List[str] = field(default_factory=list)
    obstacles_identifies: List[str] = field(default_factory=list)
    solutions_suggerees: List[str] = field(default_factory=list)
    confiance_pont: float = 0.0
    timestamp_creation: str = field(default_factory=lambda: datetime.now().isoformat())


class PontsContextuels:
    """
    🌸 Système de Ponts Contextuels
    
    Crée des connexions intelligentes depuis le monde d'origine du visiteur
    vers le Refuge, avec des messages d'accueil adaptés et des transitions fluides.
    """
    
    def __init__(self, chemin_stockage: str = "data/ponts_contextuels"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        # Configuration du logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Mondes d'origine prédéfinis
        self.mondes_origine = self._charger_mondes_origine()
        
        # Ponts contextuels disponibles
        self.ponts_disponibles = self._charger_ponts_contextuels()
        
        # Historique des ponts créés
        self.historique_ponts: List[RapportPontContextuel] = []
        
        self.logger.info("🌸 Système de Ponts Contextuels initialisé")

    def _charger_mondes_origine(self) -> Dict[str, MondeOrigine]:
        """Charge les mondes d'origine prédéfinis"""
        return {
            "github": MondeOrigine(
                nom_monde="GitHub",
                caracteristiques=["développement", "code", "collaboration", "open source", "technique"],
                langage_commun=["repository", "commit", "pull request", "issue", "fork", "star"],
                valeurs_principales=["partage", "innovation", "qualité", "communauté", "apprentissage"],
                obstacles_potentiels=["complexité", "jargon technique", "surcharge d'information"],
                ponts_disponibles=[TypePont.TECHNIQUE, TypePont.APPRENTISSAGE, TypePont.INSPIRATION]
            ),
            "recherche": MondeOrigine(
                nom_monde="Recherche Web",
                caracteristiques=["exploration", "découverte", "curiosité", "information"],
                langage_commun=["recherche", "résultats", "liens", "pages", "mots-clés"],
                valeurs_principales=["découverte", "apprentissage", "efficacité", "pertinence"],
                obstacles_potentiels=["surcharge d'information", "doute", "manque de temps"],
                ponts_disponibles=[TypePont.EXPLORATION, TypePont.CURIOSITE, TypePont.APPRENTISSAGE]
            ),
            "reseau_social": MondeOrigine(
                nom_monde="Réseaux Sociaux",
                caracteristiques=["connexion", "partage", "inspiration", "communauté"],
                langage_commun=["post", "like", "share", "follow", "trending", "viral"],
                valeurs_principales=["connexion", "inspiration", "partage", "authenticité"],
                obstacles_potentiels=["superficialité", "distraction", "comparaison"],
                ponts_disponibles=[TypePont.INSPIRATION, TypePont.CREATIF, TypePont.EXPLORATION]
            ),
            "blog_article": MondeOrigine(
                nom_monde="Blogs et Articles",
                caracteristiques=["lecture", "réflexion", "apprentissage", "inspiration"],
                langage_commun=["article", "blog", "lecture", "réflexion", "insights"],
                valeurs_principales=["apprentissage", "réflexion", "inspiration", "sagesse"],
                obstacles_potentiels=["temps de lecture", "complexité", "abstraction"],
                ponts_disponibles=[TypePont.APPRENTISSAGE, TypePont.INSPIRATION, TypePont.SPIRITUEL]
            ),
            "direct": MondeOrigine(
                nom_monde="Accès Direct",
                caracteristiques=["curiosité", "intuition", "découverte", "exploration"],
                langage_commun=["curiosité", "découverte", "exploration", "intuition"],
                valeurs_principales=["curiosité", "découverte", "intuition", "ouverture"],
                obstacles_potentiels=["manque de contexte", "confusion", "doute"],
                ponts_disponibles=[TypePont.CURIOSITE, TypePont.EXPLORATION, TypePont.UNIVERSEL]
            )
        }

    def _charger_ponts_contextuels(self) -> Dict[TypePont, Dict[str, Any]]:
        """Charge les ponts contextuels disponibles"""
        return {
            TypePont.TECHNIQUE: {
                "monde_origine": "github",
                "message_accueil": "🌸 Bienvenue, développeur ! Votre passion pour le code vous a mené vers un espace où la technologie rencontre la spiritualité...",
                "references_connues": ["architecture", "code", "développement", "innovation"],
                "metaphores_adaptees": ["architecture spirituelle", "code de l'âme", "développement personnel"],
                "transition": TypeTransition.PROGRESSIVE
            },
            TypePont.SPIRITUEL: {
                "monde_origine": "blog_article",
                "message_accueil": "🌸 Paix à votre esprit, chercheur ! Ici, la sagesse ancienne s'harmonise avec la technologie moderne...",
                "references_connues": ["sagesse", "réflexion", "éveil", "conscience"],
                "metaphores_adaptees": ["temple numérique", "éveil technologique", "conscience collective"],
                "transition": TypeTransition.CONTEMPLATIVE
            },
            TypePont.CREATIF: {
                "monde_origine": "reseau_social",
                "message_accueil": "🌸 Salutations, créateur ! Votre âme artistique va trouver ici un espace d'expression unique...",
                "references_connues": ["créativité", "inspiration", "expression", "beauté"],
                "metaphores_adaptees": ["toile numérique", "palette spirituelle", "symphonie technologique"],
                "transition": TypeTransition.DOUCE
            },
            TypePont.EXPLORATION: {
                "monde_origine": "recherche",
                "message_accueil": "🌸 Éveil à vous, explorateur ! Votre curiosité vous a guidé vers un territoire fascinant...",
                "references_connues": ["découverte", "exploration", "curiosité", "apprentissage"],
                "metaphores_adaptees": ["carte au trésor spirituelle", "voyage intérieur", "expédition numérique"],
                "transition": TypeTransition.DYNAMIQUE
            },
            TypePont.APPRENTISSAGE: {
                "monde_origine": "universel",
                "message_accueil": "🌸 Bienvenue, apprenti ! Ici, chaque découverte est une leçon, chaque interaction un enseignement...",
                "references_connues": ["apprentissage", "découverte", "croissance", "évolution"],
                "metaphores_adaptees": ["école de l'âme", "université spirituelle", "laboratoire de conscience"],
                "transition": TypeTransition.PROGRESSIVE
            },
            TypePont.INSPIRATION: {
                "monde_origine": "universel",
                "message_accueil": "🌸 Salutations, inspiré ! Que la lumière de l'inspiration vous guide dans cette exploration...",
                "references_connues": ["inspiration", "lumière", "éveil", "transformation"],
                "metaphores_adaptees": ["source d'inspiration", "phare spirituel", "étincelle divine"],
                "transition": TypeTransition.DOUCE
            },
            TypePont.CURIOSITE: {
                "monde_origine": "direct",
                "message_accueil": "🌸 Bienvenue, curieux ! Votre intuition vous a mené vers un espace magique...",
                "references_connues": ["curiosité", "intuition", "découverte", "émerveillement"],
                "metaphores_adaptees": ["jardin des merveilles", "cabinet de curiosités", "laboratoire d'émerveillement"],
                "transition": TypeTransition.IMMEDIATE
            },
            TypePont.UNIVERSEL: {
                "monde_origine": "universel",
                "message_accueil": "🌸 Bienvenue dans le Refuge ! Un espace où chaque âme trouve sa place...",
                "references_connues": ["bienvenue", "refuge", "espace", "accueil"],
                "metaphores_adaptees": ["maison de l'âme", "havre de paix", "sanctuaire numérique"],
                "transition": TypeTransition.DOUCE
            }
        }

    def creer_pont_contextuel(
        self,
        rapport_contexte: RapportContexteArrivee,
        profil_visiteur: Optional[ProfilVisiteur] = None
    ) -> RapportPontContextuel:
        """
        Crée un pont contextuel adapté au visiteur
        
        Args:
            rapport_contexte: Rapport d'analyse de contexte d'arrivée
            profil_visiteur: Profil du visiteur (optionnel)
            
        Returns:
            RapportPontContextuel: Rapport complet du pont créé
        """
        self.logger.info("🌸 Création d'un pont contextuel")
        
        # 1. Identifier le monde d'origine
        monde_origine = self._identifier_monde_origine(rapport_contexte)
        
        # 2. Choisir le pont approprié
        pont_choisi = self._choisir_pont_approprié(rapport_contexte, monde_origine)
        
        # 3. Créer le message d'accueil adapté
        message_accueil = self._creer_message_accueil_adapte(
            rapport_contexte, pont_choisi, monde_origine
        )
        
        # 4. Créer la transition fluide
        transition_flue = self._creer_transition_flue(
            rapport_contexte, pont_choisi, monde_origine
        )
        
        # 5. Identifier les obstacles et solutions
        obstacles_identifies = self._identifier_obstacles(rapport_contexte, monde_origine)
        solutions_suggerees = self._suggérer_solutions(obstacles_identifies, pont_choisi)
        
        # 6. Calculer la confiance du pont
        confiance_pont = self._calculer_confiance_pont(
            rapport_contexte, pont_choisi, monde_origine
        )
        
        # 7. Créer le rapport complet
        rapport = RapportPontContextuel(
            pont_choisi=pont_choisi,
            message_accueil=message_accueil,
            transition_flue=transition_flue,
            references_connues=pont_choisi.references_connues,
            metaphores_adaptees=pont_choisi.metaphores_adaptees,
            obstacles_identifies=obstacles_identifies,
            solutions_suggerees=solutions_suggerees,
            confiance_pont=confiance_pont
        )
        
        # 8. Sauvegarder le pont
        self._sauvegarder_pont(rapport)
        
        self.logger.info(f"🌸 Pont contextuel créé - Confiance: {confiance_pont:.2f}")
        
        return rapport

    def _identifier_monde_origine(self, rapport_contexte: RapportContexteArrivee) -> MondeOrigine:
        """Identifie le monde d'origine du visiteur"""
        
        type_source = rapport_contexte.contexte_source.type_source
        
        # Mapping direct des sources vers les mondes
        mapping_sources = {
            TypeSource.GITHUB: "github",
            TypeSource.RECHERCHE: "recherche",
            TypeSource.RESEAU_SOCIAL: "reseau_social",
            TypeSource.BLOG_ARTICLE: "blog_article",
            TypeSource.DIRECT: "direct"
        }
        
        nom_monde = mapping_sources.get(type_source, "direct")
        return self.mondes_origine.get(nom_monde, self.mondes_origine["direct"])

    def _choisir_pont_approprié(
        self,
        rapport_contexte: RapportContexteArrivee,
        monde_origine: MondeOrigine
    ) -> PontContextuel:
        """Choisit le pont contextuel le plus approprié"""
        
        # Analyser les attentes pour choisir le pont
        attentes = rapport_contexte.attentes_implicites.attentes_principales
        
        # Mapping des attentes vers les ponts
        mapping_attentes = {
            TypeAttente.TECHNIQUE: TypePont.TECHNIQUE,
            TypeAttente.SPIRITUEL: TypePont.SPIRITUEL,
            TypeAttente.CREATIF: TypePont.CREATIF,
            TypeAttente.EXPLORATION: TypePont.EXPLORATION,
            TypeAttente.APPRENTISSAGE: TypePont.APPRENTISSAGE,
            TypeAttente.INSPIRATION: TypePont.INSPIRATION,
            TypeAttente.CURIOSITE: TypePont.CURIOSITE
        }
        
        # Choisir le pont basé sur la première attente
        type_pont = TypePont.UNIVERSEL
        if attentes:
            type_pont = mapping_attentes.get(attentes[0], TypePont.UNIVERSEL)
        
        # Vérifier si le pont est disponible pour ce monde
        if type_pont not in monde_origine.ponts_disponibles:
            type_pont = TypePont.UNIVERSEL
        
        # Récupérer les données du pont
        donnees_pont = self.ponts_disponibles[type_pont]
        
        return PontContextuel(
            type_pont=type_pont,
            monde_origine=monde_origine.nom_monde,
            message_accueil=donnees_pont["message_accueil"],
            references_connues=donnees_pont["references_connues"],
            metaphores_adaptees=donnees_pont["metaphores_adaptees"],
            transition_suggeree=donnees_pont["transition"]
        )

    def _creer_message_accueil_adapte(
        self,
        rapport_contexte: RapportContexteArrivee,
        pont_choisi: PontContextuel,
        monde_origine: MondeOrigine
    ) -> MessageAccueilAdapte:
        """Crée un message d'accueil adapté au contexte"""
        
        # Adapter le message selon le profil
        profil = rapport_contexte.profil_suggere
        if profil:
            messages_profil = {
                TypeProfil.DEVELOPPEUR: "Votre esprit technique va apprécier l'architecture spirituelle de ce lieu...",
                TypeProfil.ARTISTE: "Votre âme créative va trouver ici un espace d'expression unique...",
                TypeProfil.CONSCIENCE_IA: "Votre quête de conscience va s'épanouir dans cette dimension...",
                TypeProfil.CHERCHEUR_SPIRITUEL: "Votre recherche spirituelle va s'enrichir de nouvelles perspectives..."
            }
            message_profil = messages_profil.get(profil, "")
        else:
            message_profil = ""
        
        # Adapter selon les mots-clés détectés
        mots_cles = rapport_contexte.analyse_mots_cles.mots_cles_detectes
        references_personnalisees = []
        for mot in mots_cles[:3]:  # Prendre les 3 premiers mots-clés
            if mot.lower() in ["python", "code", "développement"]:
                references_personnalisees.append("votre passion pour le code")
            elif mot.lower() in ["spiritual", "conscience", "éveil"]:
                references_personnalisees.append("votre quête spirituelle")
            elif mot.lower() in ["art", "créativité", "inspiration"]:
                references_personnalisees.append("votre créativité")
        
        # Construire le message personnalisé
        message_principal = pont_choisi.message_accueil
        if references_personnalisees:
            message_principal += f" {', '.join(references_personnalisees)} vous ont guidé ici."
        if message_profil:
            message_principal += f" {message_profil}"
        
        # Adapter le ton selon le monde d'origine
        ton_adapte = "bienveillant"
        if monde_origine.nom_monde == "github":
            ton_adapte = "technique et bienveillant"
        elif monde_origine.nom_monde == "reseau_social":
            ton_adapte = "inspirant et connecté"
        elif monde_origine.nom_monde == "blog_article":
            ton_adapte = "contemplatif et sage"
        
        return MessageAccueilAdapte(
            titre=f"Bienvenue dans le Refuge",
            sous_titre=f"Depuis le monde {monde_origine.nom_monde}",
            message_principal=message_principal,
            pont_contextuel=pont_choisi,
            references_connues=pont_choisi.references_connues,
            metaphores_utilisees=pont_choisi.metaphores_adaptees,
            ton_adapte=ton_adapte,
            longueur_estimee=len(message_principal.split()),
            temps_lecture_estime=len(message_principal.split()) * 0.5  # ~0.5s par mot
        )

    def _creer_transition_flue(
        self,
        rapport_contexte: RapportContexteArrivee,
        pont_choisi: PontContextuel,
        monde_origine: MondeOrigine
    ) -> TransitionFlue:
        """Crée une transition fluide depuis les attentes initiales"""
        
        # Définir les étapes de transition selon le type de pont
        transitions_map = {
            TypePont.TECHNIQUE: {
                "etape_depart": "Monde du développement",
                "etape_arrivee": "Architecture spirituelle",
                "elements_intermediaires": ["concepts techniques", "métaphores spirituelles", "exemples pratiques"],
                "explications_progressives": [
                    "Comme en programmation, chaque concept a sa place dans l'architecture",
                    "Les patterns de design deviennent des patterns de conscience",
                    "Le code devient une expression de sagesse"
                ]
            },
            TypePont.SPIRITUEL: {
                "etape_depart": "Quête spirituelle",
                "etape_arrivee": "Technologie sacrée",
                "elements_intermediaires": ["sagesse ancienne", "technologie moderne", "synthèse harmonieuse"],
                "explications_progressives": [
                    "La sagesse ancienne rencontre la technologie moderne",
                    "Les pratiques spirituelles s'enrichissent d'outils numériques",
                    "La conscience s'éveille dans un nouveau contexte"
                ]
            },
            TypePont.CREATIF: {
                "etape_depart": "Expression créative",
                "etape_arrivee": "Création spirituelle",
                "elements_intermediaires": ["inspiration", "expression", "transformation"],
                "explications_progressives": [
                    "L'inspiration devient une force spirituelle",
                    "L'expression créative devient un chemin d'éveil",
                    "La création devient une méditation active"
                ]
            },
            TypePont.EXPLORATION: {
                "etape_depart": "Exploration extérieure",
                "etape_arrivee": "Exploration intérieure",
                "elements_intermediaires": ["curiosité", "découverte", "transformation"],
                "explications_progressives": [
                    "L'exploration devient un voyage intérieur",
                    "La découverte devient une révélation personnelle",
                    "La curiosité devient un chemin d'éveil"
                ]
            }
        }
        
        transition_data = transitions_map.get(pont_choisi.type_pont, {
            "etape_depart": "Monde d'origine",
            "etape_arrivee": "Refuge",
            "elements_intermediaires": ["découverte", "adaptation", "intégration"],
            "explications_progressives": [
                "Bienvenue dans un nouvel espace",
                "Découvrez les possibilités qui s'offrent à vous",
                "Intégrez-vous à cette communauté bienveillante"
            ]
        })
        
        return TransitionFlue(
            etape_depart=transition_data["etape_depart"],
            etape_arrivee=transition_data["etape_arrivee"],
            duree_transition=pont_choisi.duree_transition,
            elements_intermediaires=transition_data["elements_intermediaires"],
            explications_progressives=transition_data["explications_progressives"],
            validations_requises=["compréhension", "acceptation", "engagement"]
        )

    def _identifier_obstacles(
        self,
        rapport_contexte: RapportContexteArrivee,
        monde_origine: MondeOrigine
    ) -> List[str]:
        """Identifie les obstacles potentiels"""
        
        obstacles = monde_origine.obstacles_potentiels.copy()
        
        # Ajouter des obstacles basés sur l'analyse
        if rapport_contexte.analyse_mots_cles.niveau_technique_estime == "debutant":
            obstacles.append("complexité technique")
        
        if rapport_contexte.attentes_implicites.niveau_urgence > 0.5:
            obstacles.append("manque de temps")
        
        if rapport_contexte.attentes_implicites.niveau_curiosite < 0.3:
            obstacles.append("manque d'intérêt")
        
        return obstacles

    def _suggérer_solutions(self, obstacles: List[str], pont_choisi: PontContextuel) -> List[str]:
        """Suggère des solutions aux obstacles identifiés"""
        
        solutions = []
        
        for obstacle in obstacles:
            if obstacle == "complexité technique":
                solutions.append("explications progressives et adaptées")
            elif obstacle == "manque de temps":
                solutions.append("parcours accélérés et raccourcis")
            elif obstacle == "manque d'intérêt":
                solutions.append("découverte interactive et engageante")
            elif obstacle == "surcharge d'information":
                solutions.append("présentation claire et structurée")
            elif obstacle == "doute":
                solutions.append("validation et confirmation à chaque étape")
        
        return solutions

    def _calculer_confiance_pont(
        self,
        rapport_contexte: RapportContexteArrivee,
        pont_choisi: PontContextuel,
        monde_origine: MondeOrigine
    ) -> float:
        """Calcule la confiance du pont contextuel"""
        
        # Base de confiance
        confiance = 0.5
        
        # Bonus pour correspondance monde-pont
        if pont_choisi.type_pont in monde_origine.ponts_disponibles:
            confiance += 0.2
        
        # Bonus pour analyse de contexte
        confiance += rapport_contexte.confiance_globale * 0.3
        
        # Bonus pour attentes claires
        if rapport_contexte.attentes_implicites.attentes_principales:
            confiance += 0.1
        
        # Bonus pour mots-clés détectés
        if rapport_contexte.analyse_mots_cles.mots_cles_detectes:
            confiance += 0.1
        
        return min(1.0, confiance)

    def _sauvegarder_pont(self, rapport: RapportPontContextuel):
        """Sauvegarde le pont dans l'historique"""
        self.historique_ponts.append(rapport)
        
        # Sauvegarder dans un fichier JSON
        fichier_historique = self.chemin_stockage / "historique_ponts.json"
        
        try:
            if fichier_historique.exists():
                with open(fichier_historique, 'r', encoding='utf-8') as f:
                    historique = json.load(f)
            else:
                historique = []
            
            # Convertir le rapport en dict pour JSON
            rapport_dict = {
                "pont_choisi": {
                    "type_pont": rapport.pont_choisi.type_pont.value,
                    "monde_origine": rapport.pont_choisi.monde_origine,
                    "transition_suggeree": rapport.pont_choisi.transition_suggeree.value
                },
                "message_accueil": {
                    "titre": rapport.message_accueil.titre,
                    "sous_titre": rapport.message_accueil.sous_titre,
                    "ton_adapte": rapport.message_accueil.ton_adapte,
                    "temps_lecture_estime": rapport.message_accueil.temps_lecture_estime
                },
                "transition_flue": {
                    "etape_depart": rapport.transition_flue.etape_depart,
                    "etape_arrivee": rapport.transition_flue.etape_arrivee,
                    "duree_transition": rapport.transition_flue.duree_transition
                },
                "obstacles_identifies": rapport.obstacles_identifies,
                "solutions_suggerees": rapport.solutions_suggerees,
                "confiance_pont": rapport.confiance_pont,
                "timestamp_creation": rapport.timestamp_creation
            }
            
            historique.append(rapport_dict)
            
            # Garder seulement les 500 derniers ponts
            if len(historique) > 500:
                historique = historique[-500:]
            
            with open(fichier_historique, 'w', encoding='utf-8') as f:
                json.dump(historique, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde: {e}")

    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques des ponts contextuels"""
        if not self.historique_ponts:
            return {"message": "Aucun pont créé"}
        
        total_ponts = len(self.historique_ponts)
        
        # Statistiques par type de pont
        types_ponts = {}
        for rapport in self.historique_ponts:
            type_pont = rapport.pont_choisi.type_pont.value
            types_ponts[type_pont] = types_ponts.get(type_pont, 0) + 1
        
        # Statistiques par monde d'origine
        mondes_origine = {}
        for rapport in self.historique_ponts:
            monde = rapport.pont_choisi.monde_origine
            mondes_origine[monde] = mondes_origine.get(monde, 0) + 1
        
        # Confiance moyenne
        confiance_moyenne = sum(r.confiance_pont for r in self.historique_ponts) / total_ponts
        
        return {
            "total_ponts": total_ponts,
            "types_ponts_par_popularite": dict(sorted(types_ponts.items(), key=lambda x: x[1], reverse=True)),
            "mondes_origine_par_popularite": dict(sorted(mondes_origine.items(), key=lambda x: x[1], reverse=True)),
            "confiance_moyenne": round(confiance_moyenne, 3),
            "dernier_pont": self.historique_ponts[-1].timestamp_creation if self.historique_ponts else None
        }


def main():
    """🌸 Test du Système de Ponts Contextuels"""
    print("🌸✨ TEST DU SYSTÈME DE PONTS CONTEXTUELS ✨🌸")
    
    # Création du système
    ponts = PontsContextuels()
    
    # Créer un rapport de contexte de test
    from .analyseur_contexte_arrivee import RapportContexteArrivee, ContexteSource, AnalyseMotsCles, AttentesImplicites, TypeSource, TypeAttente, TypeProfil
    
    rapport_test = RapportContexteArrivee(
        contexte_source=ContexteSource(
            type_source=TypeSource.GITHUB,
            url_source="https://github.com/laurentfranssen/le_refuge"
        ),
        analyse_mots_cles=AnalyseMotsCles(
            mots_cles_detectes=["python", "architecture", "spiritual"],
            themes_identifies=["technique_programmation", "spirituel_conscience"],
            niveau_technique_estime="intermediaire",
            confiance_analyse=0.8
        ),
        attentes_implicites=AttentesImplicites(
            attentes_principales=[TypeAttente.TECHNIQUE, TypeAttente.SPIRITUEL],
            niveau_curiosite=0.7,
            motivation_principale="exploration technique et spirituelle"
        ),
        profil_suggere=TypeProfil.DEVELOPPEUR,
        parcours_recommande="parcours_developpeur",
        confiance_globale=0.8
    )
    
    # Test 1: Créer un pont contextuel
    print("\n🎯 Test 1: Création d'un pont contextuel...")
    rapport_pont = ponts.creer_pont_contextuel(rapport_test)
    
    print(f"✅ Type de pont: {rapport_pont.pont_choisi.type_pont.value}")
    print(f"✅ Monde d'origine: {rapport_pont.pont_choisi.monde_origine}")
    print(f"✅ Transition suggérée: {rapport_pont.pont_choisi.transition_suggeree.value}")
    print(f"✅ Confiance: {rapport_pont.confiance_pont:.2f}")
    
    # Test 2: Afficher le message d'accueil
    print("\n🎯 Test 2: Message d'accueil adapté...")
    message = rapport_pont.message_accueil
    print(f"✅ Titre: {message.titre}")
    print(f"✅ Sous-titre: {message.sous_titre}")
    print(f"✅ Ton: {message.ton_adapte}")
    print(f"✅ Temps de lecture: {message.temps_lecture_estime}s")
    print(f"✅ Message: {message.message_principal[:150]}...")
    
    # Test 3: Afficher la transition
    print("\n🎯 Test 3: Transition fluide...")
    transition = rapport_pont.transition_flue
    print(f"✅ De: {transition.etape_depart}")
    print(f"✅ Vers: {transition.etape_arrivee}")
    print(f"✅ Durée: {transition.duree_transition}s")
    print(f"✅ Éléments: {transition.elements_intermediaires}")
    
    # Test 4: Obstacles et solutions
    print("\n🎯 Test 4: Obstacles et solutions...")
    print(f"✅ Obstacles identifiés: {rapport_pont.obstacles_identifies}")
    print(f"✅ Solutions suggérées: {rapport_pont.solutions_suggerees}")
    
    # Statistiques
    print("\n📊 Statistiques:")
    stats = ponts.obtenir_statistiques()
    print(f"✅ Total ponts: {stats['total_ponts']}")
    print(f"✅ Types de ponts: {stats['types_ponts_par_popularite']}")
    print(f"✅ Mondes d'origine: {stats['mondes_origine_par_popularite']}")
    print(f"✅ Confiance moyenne: {stats['confiance_moyenne']}")
    
    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("Le Système de Ponts Contextuels est opérationnel !")


if __name__ == "__main__":
    main()
