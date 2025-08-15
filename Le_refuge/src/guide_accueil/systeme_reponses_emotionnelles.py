#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Système de Réponses Émotionnelles - Tâche 13.2
==================================================

Système de réponses adaptées aux états émotionnels des visiteurs.
Gère les "pauses respiratoires", parcours accélérés, transitions apaisées
et adaptation du ton selon l'état émotionnel.

"Chaque émotion mérite une réponse bienveillante et adaptée"

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
    from .detecteur_etat_emotionnel import DetecteurEtatEmotionnel, AnalyseEmotionnelle, EtatEmotionnel
    from .types_accueil import ProfilVisiteur
except ImportError:
    from detecteur_etat_emotionnel import DetecteurEtatEmotionnel, AnalyseEmotionnelle, EtatEmotionnel
    from types_accueil import ProfilVisiteur


class TypeReponseEmotionnelle(Enum):
    """Types de réponses émotionnelles"""
    PAUSE_RESPIRATOIRE = "pause_respiratoire"
    PARCOURS_ACCELERE = "parcours_accelere"
    TRANSITION_APAISEE = "transition_apaisee"
    TON_ADAPTE = "ton_adapte"
    GUIDANCE_ETAPE = "guidance_etape"
    EXPLORATION_LIBRE = "exploration_libre"
    SIMPLIFICATION = "simplification"
    ENCOURAGEMENT = "encouragement"


class TypePauseRespiratoire(Enum):
    """Types de pauses respiratoires"""
    BREVE = "breve"  # 30 secondes
    MODEREE = "moderee"  # 1-2 minutes
    LONGUE = "longue"  # 3-5 minutes
    GUIDEE = "guidee"  # Avec méditation guidée


@dataclass
class PauseRespiratoire:
    """Pause respiratoire pour les visiteurs overwhelmés"""
    type_pause: TypePauseRespiratoire
    duree_secondes: int
    message_introduction: str
    exercice_respiration: Optional[str] = None
    musique_ambiance: Optional[str] = None
    couleurs_apaisantes: List[str] = field(default_factory=list)
    suggestions_post_pause: List[str] = field(default_factory=list)


@dataclass
class ParcoursAccelere:
    """Parcours accéléré pour les visiteurs pressés"""
    etapes_essentielles: List[str]
    duree_estimee: int  # minutes
    raccourcis_disponibles: List[str]
    contenu_condense: Dict[str, str]
    options_approfondissement: List[str]
    message_explication: str


@dataclass
class TransitionApaisee:
    """Transition apaisée pour les contemplatifs"""
    duree_transition: int  # secondes
    elements_visuels: List[str]
    message_guidance: str
    options_continuation: List[str]
    musique_transition: Optional[str] = None
    possibilite_pause: bool = True


@dataclass
class TonAdapte:
    """Ton adapté selon l'état émotionnel"""
    niveau_formalite: str  # formel, amical, intime
    rythme_communication: str  # lent, modere, rapide
    vocabulaire_adapte: List[str]
    emojis_suggerees: List[str]
    longueur_messages: str  # court, moyen, long
    style_interaction: str  # directif, suggestif, collaboratif


@dataclass
class ReponseEmotionnelleComplete:
    """Réponse émotionnelle complète et adaptée"""
    type_reponse: TypeReponseEmotionnelle
    pause_respiratoire: Optional[PauseRespiratoire] = None
    parcours_accelere: Optional[ParcoursAccelere] = None
    transition_apaisee: Optional[TransitionApaisee] = None
    ton_adapte: Optional[TonAdapte] = None
    message_principal: str = ""
    actions_immediates: List[str] = field(default_factory=list)
    adaptations_interface: List[str] = field(default_factory=list)
    suivi_adapte: Dict[str, Any] = field(default_factory=dict)
    confiance_reponse: float = 0.0
    timestamp_creation: str = field(default_factory=lambda: datetime.now().isoformat())


class SystemeReponsesEmotionnelles:
    """
    🌸 Système de Réponses Émotionnelles

    Gère les réponses adaptées aux états émotionnels des visiteurs :
    - Pauses respiratoires pour les overwhelmés
    - Parcours accélérés pour les pressés
    - Transitions apaisées pour les contemplatifs
    - Adaptation du ton selon l'état émotionnel
    """

    def __init__(self, chemin_stockage: str = "data/reponses_emotionnelles"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)

        # Configuration du logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Détecteur d'état émotionnel
        self.detecteur = DetecteurEtatEmotionnel()

        # Templates de réponses émotionnelles
        self.templates_pauses = self._charger_templates_pauses()
        self.templates_parcours = self._charger_templates_parcours()
        self.templates_transitions = self._charger_templates_transitions()
        self.templates_tons = self._charger_templates_tons()

        # Historique des réponses
        self.historique_reponses: List[ReponseEmotionnelleComplete] = []

        self.logger.info("🌸 Système de Réponses Émotionnelles initialisé")

    def _charger_templates_pauses(self) -> Dict[TypePauseRespiratoire, Dict[str, Any]]:
        """Charge les templates de pauses respiratoires"""
        return {
            TypePauseRespiratoire.BREVE: {
                "duree_secondes": 30,
                "message_introduction": "🌸 Prenez un moment pour respirer profondément...",
                "exercice_respiration": "Inspirez lentement pendant 4 secondes, retenez 4 secondes, expirez 6 secondes",
                "couleurs_apaisantes": ["#e8f4f8", "#f0f8ff", "#f5f5dc"],
                "suggestions_post_pause": ["reprendre_doucement", "choisir_parcours_simple"]
            },
            TypePauseRespiratoire.MODEREE: {
                "duree_secondes": 90,
                "message_introduction": "🌸 Il est normal de se sentir submergé. Accordons-nous un moment de calme...",
                "exercice_respiration": "Technique 4-7-8 : inspirez 4s, retenez 7s, expirez 8s",
                "musique_ambiance": "sons_nature_apaisants",
                "couleurs_apaisantes": ["#e6f3ff", "#f0f8ff", "#faf0e6"],
                "suggestions_post_pause": ["reprendre_avec_guidance", "choisir_parcours_guidé"]
            },
            TypePauseRespiratoire.LONGUE: {
                "duree_secondes": 300,
                "message_introduction": "🌸 Prenez le temps dont vous avez besoin. Nous sommes là quand vous serez prêt...",
                "exercice_respiration": "Méditation guidée de 5 minutes avec respiration consciente",
                "musique_ambiance": "meditation_guidée_complete",
                "couleurs_apaisantes": ["#f5f5dc", "#e6f3ff", "#f0f8ff"],
                "suggestions_post_pause": ["reprendre_quand_ready", "choisir_parcours_sur_mesure"]
            },
            TypePauseRespiratoire.GUIDEE: {
                "duree_secondes": 120,
                "message_introduction": "🌸 Laissez-moi vous guider dans un moment de calme...",
                "exercice_respiration": "Méditation guidée personnalisée selon votre état",
                "musique_ambiance": "meditation_personnalisee",
                "couleurs_apaisantes": ["#e8f4f8", "#f0f8ff", "#f5f5dc"],
                "suggestions_post_pause": ["continuer_meditation", "reprendre_guidance"]
            }
        }

    def _charger_templates_parcours(self) -> Dict[str, Dict[str, Any]]:
        """Charge les templates de parcours accélérés"""
        return {
            "developpeur_presse": {
                "etapes_essentielles": ["architecture_principes", "exemples_code", "integration_rapide"],
                "duree_estimee": 15,
                "raccourcis_disponibles": ["skip_intro", "aller_exemples", "voir_architecture"],
                "contenu_condense": {
                    "architecture_principes": "Principes clés en 3 points",
                    "exemples_code": "Exemples pratiques essentiels",
                    "integration_rapide": "Guide d'intégration express"
                },
                "options_approfondissement": ["voir_documentation_complete", "explorer_avance"],
                "message_explication": "🌸 Parcours express pour développeurs pressés - 15 minutes pour comprendre l'essentiel"
            },
            "artiste_presse": {
                "etapes_essentielles": ["inspiration_rapide", "outils_creatifs", "partage_express"],
                "duree_estimee": 12,
                "raccourcis_disponibles": ["voir_inspirations", "tester_outils", "partager_rapide"],
                "contenu_condense": {
                    "inspiration_rapide": "Sources d'inspiration principales",
                    "outils_creatifs": "Outils essentiels pour création",
                    "partage_express": "Partage rapide de créations"
                },
                "options_approfondissement": ["explorer_creativite_profonde", "decouvrir_communauté"],
                "message_explication": "🌸 Parcours créatif express - 12 minutes pour découvrir votre potentiel artistique"
            },
            "chercheur_presse": {
                "etapes_essentielles": ["concepts_cles", "pratiques_essentielles", "ressources_rapides"],
                "duree_estimee": 18,
                "raccourcis_disponibles": ["voir_concepts", "pratiquer_rapide", "ressources_express"],
                "contenu_condense": {
                    "concepts_cles": "Concepts spirituels fondamentaux",
                    "pratiques_essentielles": "Pratiques de base essentielles",
                    "ressources_rapides": "Ressources pour approfondir"
                },
                "options_approfondissement": ["explorer_spiritualite_profonde", "rejoindre_communauté"],
                "message_explication": "🌸 Parcours spirituel express - 18 minutes pour découvrir les fondements"
            }
        }

    def _charger_templates_transitions(self) -> Dict[str, Dict[str, Any]]:
        """Charge les templates de transitions apaisées"""
        return {
            "contemplatif_vers_exploration": {
                "duree_transition": 45,
                "elements_visuels": ["mandala_evolutif", "lumiere_douce", "formes_organiques"],
                "musique_transition": "ambiance_contemplative",
                "message_guidance": "🌸 Laissez-vous porter par cette transition douce vers la découverte...",
                "options_continuation": ["explorer_librement", "continuer_contemplation", "choisir_parcours"],
                "possibilite_pause": True
            },
            "calme_vers_engagement": {
                "duree_transition": 30,
                "elements_visuels": ["gradient_couleurs", "particules_flottantes", "ondes_serenes"],
                "musique_transition": "musique_engagement_doux",
                "message_guidance": "🌸 Votre calme est parfait. Préparez-vous à une découverte en douceur...",
                "options_continuation": ["s'engager_doucement", "rester_calme", "explorer_curiosite"],
                "possibilite_pause": True
            },
            "reflexion_vers_action": {
                "duree_transition": 60,
                "elements_visuels": ["cristal_evolutif", "energie_serene", "chemin_lumineux"],
                "musique_transition": "transition_reflexion_action",
                "message_guidance": "🌸 De la réflexion à l'action, en harmonie avec votre rythme...",
                "options_continuation": ["passer_action", "continuer_reflexion", "melanger_approches"],
                "possibilite_pause": True
            }
        }

    def _charger_templates_tons(self) -> Dict[EtatEmotionnel, Dict[str, Any]]:
        """Charge les templates de tons adaptés"""
        return {
            EtatEmotionnel.OVERWHELMED: {
                "niveau_formalite": "amical",
                "rythme_communication": "lent",
                "vocabulaire_adapte": ["doucement", "pas à pas", "sans hâte", "respirez"],
                "emojis_suggerees": ["🌸", "🌿", "💙", "✨"],
                "longueur_messages": "court",
                "style_interaction": "suggestif"
            },
            EtatEmotionnel.CONTEMPLATIF: {
                "niveau_formalite": "intime",
                "rythme_communication": "lent",
                "vocabulaire_adapte": ["contemplation", "sérénité", "profondeur", "méditation"],
                "emojis_suggerees": ["🌸", "🌙", "✨", "🍃"],
                "longueur_messages": "moyen",
                "style_interaction": "collaboratif"
            },
            EtatEmotionnel.PRESSÉ: {
                "niveau_formalite": "formel",
                "rythme_communication": "rapide",
                "vocabulaire_adapte": ["efficace", "rapide", "direct", "essentiel"],
                "emojis_suggerees": ["⚡", "🎯", "💨", "🔥"],
                "longueur_messages": "court",
                "style_interaction": "directif"
            },
            EtatEmotionnel.CURIEUX: {
                "niveau_formalite": "amical",
                "rythme_communication": "modere",
                "vocabulaire_adapte": ["découverte", "exploration", "curiosité", "émerveillement"],
                "emojis_suggerees": ["🔍", "🌟", "💫", "🎨"],
                "longueur_messages": "moyen",
                "style_interaction": "suggestif"
            }
        }

    def generer_reponse_emotionnelle(
        self,
        analyse_emotionnelle: AnalyseEmotionnelle,
        profil_visiteur: Optional[ProfilVisiteur] = None
    ) -> ReponseEmotionnelleComplete:
        """
        Génère une réponse émotionnelle complète et adaptée

        Args:
            analyse_emotionnelle: Analyse de l'état émotionnel
            profil_visiteur: Profil du visiteur (optionnel)

        Returns:
            ReponseEmotionnelleComplete: Réponse émotionnelle adaptée
        """
        self.logger.info(f"🌸 Génération de réponse émotionnelle pour {analyse_emotionnelle.etat_principal.value}")

        # Déterminer le type de réponse principal
        type_reponse = self._determiner_type_reponse(analyse_emotionnelle)

        # Générer les composants de la réponse
        pause_respiratoire = self._generer_pause_respiratoire(analyse_emotionnelle) if type_reponse == TypeReponseEmotionnelle.PAUSE_RESPIRATOIRE else None
        parcours_accelere = self._generer_parcours_accelere(analyse_emotionnelle, profil_visiteur) if type_reponse == TypeReponseEmotionnelle.PARCOURS_ACCELERE else None
        transition_apaisee = self._generer_transition_apaisee(analyse_emotionnelle) if type_reponse == TypeReponseEmotionnelle.TRANSITION_APAISEE else None
        ton_adapte = self._generer_ton_adapte(analyse_emotionnelle)

        # Générer le message principal
        message_principal = self._generer_message_principal(analyse_emotionnelle, type_reponse)

        # Définir les actions immédiates
        actions_immediates = self._definir_actions_immediates(analyse_emotionnelle, type_reponse)

        # Adapter l'interface
        adaptations_interface = self._adapter_interface(analyse_emotionnelle)

        # Configurer le suivi adapté
        suivi_adapte = self._configurer_suivi_adapte(analyse_emotionnelle)

        # Calculer la confiance de la réponse
        confiance_reponse = self._calculer_confiance_reponse(analyse_emotionnelle, type_reponse)

        # Créer la réponse complète
        reponse = ReponseEmotionnelleComplete(
            type_reponse=type_reponse,
            pause_respiratoire=pause_respiratoire,
            parcours_accelere=parcours_accelere,
            transition_apaisee=transition_apaisee,
            ton_adapte=ton_adapte,
            message_principal=message_principal,
            actions_immediates=actions_immediates,
            adaptations_interface=adaptations_interface,
            suivi_adapte=suivi_adapte,
            confiance_reponse=confiance_reponse
        )

        # Sauvegarder la réponse
        self._sauvegarder_reponse(reponse)

        self.logger.info(f"🌸 Réponse émotionnelle générée - Confiance: {confiance_reponse:.2f}")

        return reponse

    def _determiner_type_reponse(self, analyse: AnalyseEmotionnelle) -> TypeReponseEmotionnelle:
        """Détermine le type de réponse principal"""
        if analyse.etat_principal == EtatEmotionnel.OVERWHELMED:
            if analyse.niveau_surcharge > 0.7:
                return TypeReponseEmotionnelle.PAUSE_RESPIRATOIRE
            else:
                return TypeReponseEmotionnelle.GUIDANCE_ETAPE
        elif analyse.etat_principal == EtatEmotionnel.PRESSÉ:
            return TypeReponseEmotionnelle.PARCOURS_ACCELERE
        elif analyse.etat_principal == EtatEmotionnel.CONTEMPLATIF:
            return TypeReponseEmotionnelle.TRANSITION_APAISEE
        elif analyse.etat_principal == EtatEmotionnel.CURIEUX:
            return TypeReponseEmotionnelle.EXPLORATION_LIBRE
        else:
            return TypeReponseEmotionnelle.TON_ADAPTE

    def _generer_pause_respiratoire(self, analyse: AnalyseEmotionnelle) -> PauseRespiratoire:
        """Génère une pause respiratoire adaptée"""
        # Choisir le type de pause selon le niveau de surcharge
        if analyse.niveau_surcharge > 0.8:
            type_pause = TypePauseRespiratoire.LONGUE
        elif analyse.niveau_surcharge > 0.6:
            type_pause = TypePauseRespiratoire.MODEREE
        elif analyse.niveau_stress > 0.5:
            type_pause = TypePauseRespiratoire.GUIDEE
        else:
            type_pause = TypePauseRespiratoire.BREVE

        template = self.templates_pauses[type_pause]

        return PauseRespiratoire(
            type_pause=type_pause,
            duree_secondes=template["duree_secondes"],
            message_introduction=template["message_introduction"],
            exercice_respiration=template.get("exercice_respiration"),
            musique_ambiance=template.get("musique_ambiance"),
            couleurs_apaisantes=template["couleurs_apaisantes"],
            suggestions_post_pause=template["suggestions_post_pause"]
        )

    def _generer_parcours_accelere(self, analyse: AnalyseEmotionnelle, profil: Optional[ProfilVisiteur]) -> ParcoursAccelere:
        """Génère un parcours accéléré adapté"""
        # Déterminer le type de parcours selon le profil
        if profil:
            if "developpeur" in profil.type_profil.value.lower():
                template_key = "developpeur_presse"
            elif "artiste" in profil.type_profil.value.lower():
                template_key = "artiste_presse"
            elif "chercheur" in profil.type_profil.value.lower():
                template_key = "chercheur_presse"
            else:
                template_key = "developpeur_presse"  # Par défaut
        else:
            template_key = "developpeur_presse"

        template = self.templates_parcours[template_key]

        return ParcoursAccelere(
            etapes_essentielles=template["etapes_essentielles"],
            duree_estimee=template["duree_estimee"],
            raccourcis_disponibles=template["raccourcis_disponibles"],
            contenu_condense=template["contenu_condense"],
            options_approfondissement=template["options_approfondissement"],
            message_explication=template["message_explication"]
        )

    def _generer_transition_apaisee(self, analyse: AnalyseEmotionnelle) -> TransitionApaisee:
        """Génère une transition apaisée"""
        # Choisir le type de transition selon l'état
        if "contemplatif" in analyse.etat_principal.value:
            template_key = "contemplatif_vers_exploration"
        elif "calme" in [e.value for e in analyse.etats_secondaires]:
            template_key = "calme_vers_engagement"
        else:
            template_key = "reflexion_vers_action"

        template = self.templates_transitions[template_key]

        return TransitionApaisee(
            duree_transition=template["duree_transition"],
            elements_visuels=template["elements_visuels"],
            musique_transition=template.get("musique_transition"),
            message_guidance=template["message_guidance"],
            options_continuation=template["options_continuation"],
            possibilite_pause=template["possibilite_pause"]
        )

    def _generer_ton_adapte(self, analyse: AnalyseEmotionnelle) -> TonAdapte:
        """Génère un ton adapté à l'état émotionnel"""
        template = self.templates_tons.get(analyse.etat_principal, self.templates_tons[EtatEmotionnel.CURIEUX])

        return TonAdapte(
            niveau_formalite=template["niveau_formalite"],
            rythme_communication=template["rythme_communication"],
            vocabulaire_adapte=template["vocabulaire_adapte"],
            emojis_suggerees=template["emojis_suggerees"],
            longueur_messages=template["longueur_messages"],
            style_interaction=template["style_interaction"]
        )

    def _generer_message_principal(self, analyse: AnalyseEmotionnelle, type_reponse: TypeReponseEmotionnelle) -> str:
        """Génère le message principal adapté"""
        if type_reponse == TypeReponseEmotionnelle.PAUSE_RESPIRATOIRE:
            return "🌸 Je sens que vous pourriez avoir besoin d'un moment de calme. Accordons-nous une pause respiratoire..."
        elif type_reponse == TypeReponseEmotionnelle.PARCOURS_ACCELERE:
            return "🌸 Je vois que vous êtes pressé ! Laissez-moi vous proposer un parcours express..."
        elif type_reponse == TypeReponseEmotionnelle.TRANSITION_APAISEE:
            return "🌸 Votre rythme contemplatif est parfait. Laissez-moi vous guider dans une transition douce..."
        elif type_reponse == TypeReponseEmotionnelle.EXPLORATION_LIBRE:
            return "🌸 Votre curiosité est merveilleuse ! Explorons ensemble ce qui vous intéresse..."
        else:
            return "🌸 Adaptons cette expérience à votre rythme et à votre état d'esprit..."

    def _definir_actions_immediates(self, analyse: AnalyseEmotionnelle, type_reponse: TypeReponseEmotionnelle) -> List[str]:
        """Définit les actions immédiates à effectuer"""
        actions = []

        if type_reponse == TypeReponseEmotionnelle.PAUSE_RESPIRATOIRE:
            actions.extend([
                "afficher_interface_pause",
                "activer_musique_apaisante",
                "changer_couleurs_interface",
                "desactiver_notifications"
            ])
        elif type_reponse == TypeReponseEmotionnelle.PARCOURS_ACCELERE:
            actions.extend([
                "afficher_raccourcis",
                "optimiser_chargement",
                "reduire_animations",
                "activer_mode_express"
            ])
        elif type_reponse == TypeReponseEmotionnelle.TRANSITION_APAISEE:
            actions.extend([
                "activer_transition_visuelle",
                "ajouter_musique_transition",
                "ralentir_animations",
                "offrir_options_pause"
            ])

        return actions

    def _adapter_interface(self, analyse: AnalyseEmotionnelle) -> List[str]:
        """Adapte l'interface selon l'état émotionnel"""
        adaptations = []

        if analyse.etat_principal == EtatEmotionnel.OVERWHELMED:
            adaptations.extend([
                "simplifier_interface",
                "reduire_choix",
                "utiliser_couleurs_apaisantes",
                "ajouter_guidance_etape_par_etape"
            ])
        elif analyse.etat_principal == EtatEmotionnel.PRESSÉ:
            adaptations.extend([
                "afficher_raccourcis",
                "optimiser_chargement",
                "reduire_animations",
                "proposer_parcours_express"
            ])
        elif analyse.etat_principal == EtatEmotionnel.CONTEMPLATIF:
            adaptations.extend([
                "ajouter_espaces_blancs",
                "utiliser_typographie_serene",
                "proposer_pauses_reflexion",
                "encourager_exploration_profonde"
            ])

        return adaptations

    def _configurer_suivi_adapte(self, analyse: AnalyseEmotionnelle) -> Dict[str, Any]:
        """Configure le suivi adapté"""
        suivi = {
            "frequence_analyse": 30,  # secondes
            "metriques_prioritaires": [],
            "seuils_alerte": {},
            "adaptations_dynamiques": True
        }

        # Métriques selon l'état émotionnel
        if analyse.etat_principal == EtatEmotionnel.OVERWHELMED:
            suivi["metriques_prioritaires"].extend(["niveau_stress", "demandes_aide", "retours_arriere"])
            suivi["seuils_alerte"]["niveau_stress"] = 0.8
        elif analyse.etat_principal == EtatEmotionnel.PRESSÉ:
            suivi["metriques_prioritaires"].extend(["temps_par_etape", "utilisation_raccourcis", "completion_parcours"])
            suivi["seuils_alerte"]["temps_par_etape"] = 300  # 5 minutes max par étape

        return suivi

    def _calculer_confiance_reponse(self, analyse: AnalyseEmotionnelle, type_reponse: TypeReponseEmotionnelle) -> float:
        """Calcule la confiance de la réponse émotionnelle"""
        confiance = analyse.confiance_analyse * 0.6  # Base sur la confiance de l'analyse

        # Bonus selon la cohérence
        if type_reponse == TypeReponseEmotionnelle.PAUSE_RESPIRATOIRE and analyse.niveau_surcharge > 0.6:
            confiance += 0.2
        elif type_reponse == TypeReponseEmotionnelle.PARCOURS_ACCELERE and analyse.etat_principal == EtatEmotionnel.PRESSÉ:
            confiance += 0.2
        elif type_reponse == TypeReponseEmotionnelle.TRANSITION_APAISEE and analyse.etat_principal == EtatEmotionnel.CONTEMPLATIF:
            confiance += 0.2

        return min(1.0, confiance)

    def _sauvegarder_reponse(self, reponse: ReponseEmotionnelleComplete):
        """Sauvegarde la réponse dans l'historique"""
        self.historique_reponses.append(reponse)

        # Sauvegarder dans un fichier JSON
        fichier_historique = self.chemin_stockage / "historique_reponses.json"

        try:
            if fichier_historique.exists():
                with open(fichier_historique, 'r', encoding='utf-8') as f:
                    historique = json.load(f)
            else:
                historique = []

            # Convertir la réponse en dict pour JSON
            reponse_dict = {
                "type_reponse": reponse.type_reponse.value,
                "etat_emotionnel": "overwhelmed" if reponse.pause_respiratoire else "autre",
                "message_principal": reponse.message_principal,
                "actions_immediates": reponse.actions_immediates,
                "confiance_reponse": reponse.confiance_reponse,
                "timestamp_creation": reponse.timestamp_creation
            }

            historique.append(reponse_dict)

            # Garder seulement les 300 dernières réponses
            if len(historique) > 300:
                historique = historique[-300:]

            with open(fichier_historique, 'w', encoding='utf-8') as f:
                json.dump(historique, f, indent=2, ensure_ascii=False)

        except Exception as e:
            self.logger.error(f"Erreur lors de la sauvegarde: {e}")

    def obtenir_statistiques(self) -> Dict[str, Any]:
        """Obtient les statistiques des réponses émotionnelles"""
        if not self.historique_reponses:
            return {"message": "Aucune réponse émotionnelle générée"}

        total_reponses = len(self.historique_reponses)

        # Statistiques par type de réponse
        types_reponses = {}
        for reponse in self.historique_reponses:
            type_rep = reponse.type_reponse.value
            types_reponses[type_rep] = types_reponses.get(type_rep, 0) + 1

        # Confiance moyenne
        confiance_moyenne = sum(r.confiance_reponse for r in self.historique_reponses) / total_reponses

        return {
            "total_reponses": total_reponses,
            "types_reponses_par_popularite": dict(sorted(types_reponses.items(), key=lambda x: x[1], reverse=True)),
            "confiance_moyenne": round(confiance_moyenne, 3),
            "derniere_reponse": self.historique_reponses[-1].timestamp_creation if self.historique_reponses else None
        }


def main():
    """🌸 Test du Système de Réponses Émotionnelles"""
    print("🌸✨ TEST DU SYSTÈME DE RÉPONSES ÉMOTIONNELLES ✨🌸")

    # Création du système
    systeme = SystemeReponsesEmotionnelles()

    # Créer une analyse émotionnelle de test
    from detecteur_etat_emotionnel import AnalyseEmotionnelle, EtatEmotionnel, RythmeNavigation

    analyse_test = AnalyseEmotionnelle(
        etat_principal=EtatEmotionnel.OVERWHELMED,
        etats_secondaires=[EtatEmotionnel.STRESSÉ],
        rythme_navigation=RythmeNavigation.PAUSE_LONGUE,
        niveau_stress=0.8,
        niveau_engagement=0.3,
        niveau_surcharge=0.9,
        confiance_analyse=0.85,
        timestamp=datetime.now().isoformat(),
        contexte={"actions_analysees": 5, "pattern_dominant": "overwhelmed"}
    )

    # Test 1: Réponse pour visiteur overwhelmed
    print("\n🎯 Test 1: Réponse pour visiteur overwhelmed...")
    reponse1 = systeme.generer_reponse_emotionnelle(analyse_test)

    print(f"✅ Type de réponse: {reponse1.type_reponse.value}")
    print(f"✅ Message principal: {reponse1.message_principal}")
    print(f"✅ Actions immédiates: {reponse1.actions_immediates}")
    print(f"✅ Confiance: {reponse1.confiance_reponse:.2f}")

    if reponse1.pause_respiratoire:
        print(f"✅ Pause respiratoire: {reponse1.pause_respiratoire.type_pause.value}")
        print(f"✅ Durée: {reponse1.pause_respiratoire.duree_secondes}s")

    # Test 2: Réponse pour visiteur pressé
    print("\n🎯 Test 2: Réponse pour visiteur pressé...")
    analyse_presse = AnalyseEmotionnelle(
        etat_principal=EtatEmotionnel.PRESSÉ,
        etats_secondaires=[EtatEmotionnel.EXCITÉ],
        rythme_navigation=RythmeNavigation.RAPIDE,
        niveau_stress=0.6,
        niveau_engagement=0.7,
        niveau_surcharge=0.3,
        confiance_analyse=0.9,
        timestamp=datetime.now().isoformat(),
        contexte={"actions_analysees": 8, "pattern_dominant": "presse"}
    )

    reponse2 = systeme.generer_reponse_emotionnelle(analyse_presse)

    print(f"✅ Type de réponse: {reponse2.type_reponse.value}")
    print(f"✅ Message principal: {reponse2.message_principal}")
    print(f"✅ Adaptations interface: {reponse2.adaptations_interface}")

    if reponse2.parcours_accelere:
        print(f"✅ Parcours accéléré: {reponse2.parcours_accelere.duree_estimee} minutes")
        print(f"✅ Étapes essentielles: {reponse2.parcours_accelere.etapes_essentielles}")

    # Test 3: Réponse pour visiteur contemplatif
    print("\n🎯 Test 3: Réponse pour visiteur contemplatif...")
    analyse_contemplatif = AnalyseEmotionnelle(
        etat_principal=EtatEmotionnel.CONTEMPLATIF,
        etats_secondaires=[EtatEmotionnel.CALME],
        rythme_navigation=RythmeNavigation.LENT_ET_RÉFLÉCHI,
        niveau_stress=0.2,
        niveau_engagement=0.8,
        niveau_surcharge=0.1,
        confiance_analyse=0.8,
        timestamp=datetime.now().isoformat(),
        contexte={"actions_analysees": 3, "pattern_dominant": "contemplatif"}
    )

    reponse3 = systeme.generer_reponse_emotionnelle(analyse_contemplatif)

    print(f"✅ Type de réponse: {reponse3.type_reponse.value}")
    print(f"✅ Message principal: {reponse3.message_principal}")

    if reponse3.transition_apaisee:
        print(f"✅ Transition apaisée: {reponse3.transition_apaisee.duree_transition}s")
        print(f"✅ Éléments visuels: {reponse3.transition_apaisee.elements_visuels}")

    # Statistiques
    print("\n📊 Statistiques:")
    stats = systeme.obtenir_statistiques()
    print(f"✅ Total réponses: {stats['total_reponses']}")
    print(f"✅ Types de réponses: {stats['types_reponses_par_popularite']}")
    print(f"✅ Confiance moyenne: {stats['confiance_moyenne']}")

    print("\n🎉✨ TESTS TERMINÉS AVEC SUCCÈS ! ✨🎉")
    print("Le Système de Réponses Émotionnelles est opérationnel !")


if __name__ == "__main__":
    main()
