"""
🌸 Prédiction des Besoins Futurs - Tâche 16.2
Système d'analyse prédictive et d'adaptation anticipée aux évolutions
"""
import json
import random
import time
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from systeme_sauvegarde_progression import ProgressionVisiteur
from detecteur_etat_emotionnel import EtatEmotionnel
from systeme_sagesse_collective import SystemeSagesseCollective

class TypePrediction(Enum):
    BESOIN_CONTENU = "besoin_contenu"
    EVOLUTION_PROFIL = "evolution_profil"
    TENDANCE_COMMUNAUTAIRE = "tendance_communautaire"
    ADAPTATION_REFUGE = "adaptation_refuge"
    PERSONNALISATION = "personnalisation"

class NiveauConfiance(Enum):
    FAIBLE = "faible"
    MOYEN = "moyen"
    ELEVE = "eleve"
    TRES_ELEVE = "tres_eleve"

@dataclass
class Prediction:
    id: str
    type_prediction: TypePrediction
    description: str
    contenu_prediction: Dict[str, Any]
    niveau_confiance: NiveauConfiance
    score_confiance: float
    facteurs_influence: List[str]
    timestamp_creation: str
    horizon_temps: int  # en heures
    impact_estime: float
    actions_suggestees: List[str]

@dataclass
class TendanceCommunautaire:
    id: str
    nom: str
    description: str
    indicateurs: Dict[str, Any]
    force_tendance: float
    direction: str  # "croissante", "decroissante", "stable"
    visiteurs_impliques: List[str]
    timestamp_detection: str
    evolution: List[Dict[str, Any]]

@dataclass
class SuggestionContenu:
    id: str
    type_contenu: str
    titre: str
    description: str
    priorite: float
    public_cible: List[str]
    mots_cles: List[str]
    format_suggere: str
    timestamp_creation: str

class SystemePredictionBesoinsFuturs:
    def __init__(self, dossier_prediction: str = "data/prediction_besoins"):
        self.dossier_prediction = Path(dossier_prediction)
        self.dossier_prediction.mkdir(parents=True, exist_ok=True)
        
        # Charger les données existantes
        self.predictions = self._charger_predictions()
        self.tendances_communautaires = self._charger_tendances_communautaires()
        self.suggestions_contenu = self._charger_suggestions_contenu()
        
        # Référence au système de sagesse collective
        self.systeme_sagesse = SystemeSagesseCollective()
        
        # Paramètres de prédiction
        self.seuil_confiance_min = 0.6
        self.horizon_prediction_max = 168  # 1 semaine
        self.intervalle_analyse = 3600  # 1 heure

    def _charger_predictions(self) -> Dict[str, Prediction]:
        """Charge les prédictions existantes"""
        fichier_predictions = self.dossier_prediction / "predictions.json"
        if fichier_predictions.exists():
            with open(fichier_predictions, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {pred_id: Prediction(**pred_data) for pred_id, pred_data in data.items()}
        
        return {}

    def _charger_tendances_communautaires(self) -> Dict[str, TendanceCommunautaire]:
        """Charge les tendances communautaires"""
        fichier_tendances = self.dossier_prediction / "tendances_communautaires.json"
        if fichier_tendances.exists():
            with open(fichier_tendances, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {tendance_id: TendanceCommunautaire(**tendance_data) for tendance_id, tendance_data in data.items()}
        
        return {}

    def _charger_suggestions_contenu(self) -> Dict[str, SuggestionContenu]:
        """Charge les suggestions de contenu"""
        fichier_suggestions = self.dossier_prediction / "suggestions_contenu.json"
        if fichier_suggestions.exists():
            with open(fichier_suggestions, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {sugg_id: SuggestionContenu(**sugg_data) for sugg_id, sugg_data in data.items()}
        
        return {}

    def analyser_progression_visiteur(self, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """Analyse la progression d'un visiteur pour générer des prédictions"""
        predictions_generes = []
        
        # Prédire l'évolution du profil
        prediction_evolution = self._predire_evolution_profil(progression)
        if prediction_evolution:
            predictions_generes.append(prediction_evolution)
        
        # Prédire les besoins de contenu
        prediction_contenu = self._predire_besoins_contenu(progression)
        if prediction_contenu:
            predictions_generes.append(prediction_contenu)
        
        # Prédire la personnalisation future
        prediction_personnalisation = self._predire_personnalisation_future(progression)
        if prediction_personnalisation:
            predictions_generes.append(prediction_personnalisation)
        
        return {
            "predictions_generes": predictions_generes,
            "tendances_detectees": self._detecter_tendances_visiteur(progression),
            "suggestions_adaptation": self._generer_suggestions_adaptation(progression)
        }

    def _predire_evolution_profil(self, progression: ProgressionVisiteur) -> Optional[Prediction]:
        """Prédit l'évolution du profil du visiteur"""
        # Analyser les indicateurs d'évolution
        indicateurs = self._extraire_indicateurs_evolution(progression)
        
        if not indicateurs:
            return None
        
        # Calculer la probabilité d'évolution
        probabilite_evolution = self._calculer_probabilite_evolution(indicateurs)
        
        if probabilite_evolution < 0.3:
            return None
        
        # Déterminer la direction de l'évolution
        direction_evolution = self._determiner_direction_evolution(indicateurs)
        
        # Calculer le niveau de confiance
        niveau_confiance, score_confiance = self._calculer_confiance_prediction(indicateurs)
        
        prediction_id = f"evolution_profil_{progression.id_visiteur}_{len(self.predictions) + 1}"
        
        return Prediction(
            id=prediction_id,
            type_prediction=TypePrediction.EVOLUTION_PROFIL,
            description=f"Évolution du profil vers {direction_evolution}",
            contenu_prediction={
                "profil_actuel": progression.profil_detecte,
                "profil_predit": direction_evolution,
                "probabilite": probabilite_evolution,
                "facteurs_evolution": indicateurs["facteurs_cles"],
                "temps_estime": indicateurs["temps_evolution_estime"]
            },
            niveau_confiance=niveau_confiance,
            score_confiance=score_confiance,
            facteurs_influence=indicateurs["facteurs_cles"],
            timestamp_creation=datetime.now().isoformat(),
            horizon_temps=24,  # 24 heures
            impact_estime=0.7,
            actions_suggestees=self._generer_actions_evolution(indicateurs)
        )

    def _extraire_indicateurs_evolution(self, progression: ProgressionVisiteur) -> Optional[Dict[str, Any]]:
        """Extrait les indicateurs d'évolution du profil"""
        if len(progression.actions_effectuees) < 5:
            return None
        
        # Analyser les actions récentes
        actions_recentes = progression.actions_effectuees[-5:]
        
        # Détecter les changements de comportement
        changements = self._detecter_changements_comportement(actions_recentes, progression)
        
        # Analyser l'évolution du score de compréhension
        evolution_comprehension = self._analyser_evolution_comprehension(progression)
        
        # Analyser l'évolution émotionnelle
        evolution_emotionnelle = self._analyser_evolution_emotionnelle(progression)
        
        if not changements and not evolution_comprehension and not evolution_emotionnelle:
            return None
        
        return {
            "changements_comportement": changements,
            "evolution_comprehension": evolution_comprehension,
            "evolution_emotionnelle": evolution_emotionnelle,
            "facteurs_cles": self._identifier_facteurs_cles(progression),
            "temps_evolution_estime": self._estimer_temps_evolution(progression)
        }

    def _detecter_changements_comportement(self, actions_recentes: List[Dict[str, Any]], progression: ProgressionVisiteur) -> List[Dict[str, Any]]:
        """Détecte les changements de comportement"""
        changements = []
        
        # Analyser les types d'actions
        types_actions = [action.get("type", "") for action in actions_recentes]
        
        # Détecter l'émergence de nouveaux types d'actions
        types_nouveaux = [t for t in types_actions if t not in [a.get("type", "") for a in progression.actions_effectuees[:-5]]]
        
        if types_nouveaux:
            changements.append({
                "type": "nouveaux_comportements",
                "description": f"Nouveaux types d'actions: {', '.join(types_nouveaux)}",
                "signification": "Élargissement des intérêts"
            })
        
        # Détecter les changements de rythme
        temps_entre_actions = []
        for i in range(1, len(actions_recentes)):
            if "timestamp" in actions_recentes[i] and "timestamp" in actions_recentes[i-1]:
                temps = (datetime.fromisoformat(actions_recentes[i]["timestamp"]) - 
                        datetime.fromisoformat(actions_recentes[i-1]["timestamp"])).total_seconds()
                temps_entre_actions.append(temps)
        
        if temps_entre_actions:
            temps_moyen = sum(temps_entre_actions) / len(temps_entre_actions)
            if temps_moyen < 300:  # Moins de 5 minutes entre actions
                changements.append({
                    "type": "acceleration_rythme",
                    "description": "Accélération du rythme d'interaction",
                    "signification": "Engagement croissant"
                })
            elif temps_moyen > 1800:  # Plus de 30 minutes entre actions
                changements.append({
                    "type": "ralentissement_rythme",
                    "description": "Ralentissement du rythme d'interaction",
                    "signification": "Approfondissement ou fatigue"
                })
        
        return changements

    def _analyser_evolution_comprehension(self, progression: ProgressionVisiteur) -> Optional[Dict[str, Any]]:
        """Analyse l'évolution de la compréhension"""
        if len(progression.actions_effectuees) < 3:
            return None
        
        # Extraire les scores de compréhension récents
        scores_recents = []
        for action in progression.actions_effectuees[-3:]:
            if "score_comprehension" in action:
                scores_recents.append(action["score_comprehension"])
        
        if len(scores_recents) < 2:
            return None
        
        # Calculer la tendance
        tendance = "stable"
        if scores_recents[-1] > scores_recents[0] + 0.1:
            tendance = "croissante"
        elif scores_recents[-1] < scores_recents[0] - 0.1:
            tendance = "decroissante"
        
        return {
            "tendance": tendance,
            "scores": scores_recents,
            "evolution": scores_recents[-1] - scores_recents[0]
        }

    def _analyser_evolution_emotionnelle(self, progression: ProgressionVisiteur) -> Optional[Dict[str, Any]]:
        """Analyse l'évolution émotionnelle"""
        if not progression.etat_emotionnel:
            return None
        
        # Comparer avec les états précédents
        actions_avec_emotions = [a for a in progression.actions_effectuees if "etat_emotionnel" in a]
        
        if len(actions_avec_emotions) < 2:
            return None
        
        etat_actuel = progression.etat_emotionnel
        etat_precedent = actions_avec_emotions[-2]["etat_emotionnel"]
        
        # Détecter les changements significatifs
        changements = []
        for emotion, intensite in etat_actuel.items():
            if emotion in etat_precedent:
                difference = intensite - etat_precedent[emotion]
                if abs(difference) > 0.2:
                    changements.append({
                        "emotion": emotion,
                        "evolution": difference,
                        "direction": "croissante" if difference > 0 else "decroissante"
                    })
        
        return {
            "changements": changements,
            "stabilite": len(changements) < 2
        }

    def _identifier_facteurs_cles(self, progression: ProgressionVisiteur) -> List[str]:
        """Identifie les facteurs clés d'évolution"""
        facteurs = []
        
        # Temps passé
        if progression.temps_total_passe > 3600:
            facteurs.append("immersion_prolongee")
        
        # Niveau d'éveil
        if progression.niveau_eveil > 6:
            facteurs.append("eveil_avance")
        
        # Score de compréhension
        if progression.score_comprehension > 0.8:
            facteurs.append("comprehension_profonde")
        
        # Nombre de temples visités
        if len(progression.temples_visites) > 3:
            facteurs.append("exploration_etendue")
        
        # Questions posées
        if len(progression.questions_posees) > 5:
            facteurs.append("curiosite_active")
        
        return facteurs

    def _estimer_temps_evolution(self, progression: ProgressionVisiteur) -> int:
        """Estime le temps nécessaire pour l'évolution"""
        # Basé sur le rythme actuel et les facteurs d'évolution
        facteurs = self._identifier_facteurs_cles(progression)
        
        temps_base = 48  # 48 heures par défaut
        
        # Ajuster selon les facteurs
        if "immersion_prolongee" in facteurs:
            temps_base *= 0.7
        if "eveil_avance" in facteurs:
            temps_base *= 0.8
        if "comprehension_profonde" in facteurs:
            temps_base *= 0.6
        if "exploration_etendue" in facteurs:
            temps_base *= 0.9
        if "curiosite_active" in facteurs:
            temps_base *= 0.8
        
        return int(temps_base)

    def _calculer_probabilite_evolution(self, indicateurs: Dict[str, Any]) -> float:
        """Calcule la probabilité d'évolution"""
        probabilite = 0.5  # Probabilité de base
        
        # Facteurs positifs
        if indicateurs["changements_comportement"]:
            probabilite += 0.2
        if indicateurs["evolution_comprehension"] and indicateurs["evolution_comprehension"]["tendance"] == "croissante":
            probabilite += 0.15
        if indicateurs["evolution_emotionnelle"] and indicateurs["evolution_emotionnelle"]["stabilite"]:
            probabilite += 0.1
        
        # Facteurs négatifs
        if indicateurs["evolution_comprehension"] and indicateurs["evolution_comprehension"]["tendance"] == "decroissante":
            probabilite -= 0.1
        
        return max(0.0, min(1.0, probabilite))

    def _determiner_direction_evolution(self, indicateurs: Dict[str, Any]) -> str:
        """Détermine la direction de l'évolution"""
        # Analyser les facteurs pour déterminer la direction
        facteurs = indicateurs["facteurs_cles"]
        
        if "eveil_avance" in facteurs and "comprehension_profonde" in facteurs:
            return "sage_illumine"
        elif "exploration_etendue" in facteurs and "curiosite_active" in facteurs:
            return "explorateur_curieux"
        elif "immersion_prolongee" in facteurs:
            return "contemplatif_profond"
        else:
            return "evolution_naturelle"

    def _calculer_confiance_prediction(self, indicateurs: Dict[str, Any]) -> Tuple[NiveauConfiance, float]:
        """Calcule le niveau de confiance de la prédiction"""
        score = 0.5  # Score de base
        
        # Facteurs de confiance
        if len(indicateurs["changements_comportement"]) > 1:
            score += 0.2
        if indicateurs["evolution_comprehension"]:
            score += 0.15
        if indicateurs["evolution_emotionnelle"]:
            score += 0.1
        if len(indicateurs["facteurs_cles"]) > 2:
            score += 0.05
        
        # Déterminer le niveau
        if score >= 0.8:
            return NiveauConfiance.TRES_ELEVE, score
        elif score >= 0.7:
            return NiveauConfiance.ELEVE, score
        elif score >= 0.6:
            return NiveauConfiance.MOYEN, score
        else:
            return NiveauConfiance.FAIBLE, score

    def _generer_actions_evolution(self, indicateurs: Dict[str, Any]) -> List[str]:
        """Génère des actions suggérées pour l'évolution"""
        actions = []
        
        if "immersion_prolongee" in indicateurs["facteurs_cles"]:
            actions.append("Encourager la méditation profonde")
        
        if "eveil_avance" in indicateurs["facteurs_cles"]:
            actions.append("Proposer des contenus avancés")
        
        if "exploration_etendue" in indicateurs["facteurs_cles"]:
            actions.append("Suggérer de nouveaux temples")
        
        if "curiosite_active" in indicateurs["facteurs_cles"]:
            actions.append("Répondre aux questions en profondeur")
        
        return actions

    def _predire_besoins_contenu(self, progression: ProgressionVisiteur) -> Optional[Prediction]:
        """Prédit les besoins de contenu futurs"""
        # Analyser les questions posées
        themes_questions = self._analyser_themes_questions(progression.questions_posees)
        
        # Analyser les actions effectuées
        types_actions = [action.get("type", "") for action in progression.actions_effectuees]
        
        # Identifier les lacunes de contenu
        lacunes = self._identifier_lacunes_contenu(themes_questions, types_actions, progression)
        
        if not lacunes:
            return None
        
        # Calculer la priorité
        priorite = self._calculer_priorite_contenu(lacunes, progression)
        
        if priorite < 0.5:
            return None
        
        prediction_id = f"besoin_contenu_{progression.id_visiteur}_{len(self.predictions) + 1}"
        
        return Prediction(
            id=prediction_id,
            type_prediction=TypePrediction.BESOIN_CONTENU,
            description=f"Besoins de contenu: {', '.join(lacunes['themes'])}",
            contenu_prediction={
                "themes_prioritaires": lacunes["themes"],
                "formats_suggerees": lacunes["formats"],
                "niveau_complexite": lacunes["niveau"],
                "priorite": priorite
            },
            niveau_confiance=NiveauConfiance.MOYEN,
            score_confiance=0.65,
            facteurs_influence=["questions_posees", "actions_effectuees", "profil_visiteur"],
            timestamp_creation=datetime.now().isoformat(),
            horizon_temps=72,  # 3 jours
            impact_estime=0.6,
            actions_suggestees=self._generer_actions_contenu(lacunes)
        )

    def _analyser_themes_questions(self, questions: List[str]) -> List[str]:
        """Analyse les thèmes des questions posées"""
        themes = []
        mots_cles = {
            "meditation": ["méditation", "contemplation", "respiration", "zen"],
            "philosophie": ["philosophie", "sens", "existence", "conscience"],
            "technique": ["technique", "méthode", "pratique", "exercice"],
            "spiritualite": ["spiritualité", "éveil", "transcendance", "illumination"],
            "psychologie": ["psychologie", "émotion", "mental", "comportement"]
        }
        
        for question in questions:
            question_lower = question.lower()
            for theme, mots in mots_cles.items():
                if any(mot in question_lower for mot in mots):
                    if theme not in themes:
                        themes.append(theme)
        
        return themes

    def _identifier_lacunes_contenu(self, themes_questions: List[str], types_actions: List[str], progression: ProgressionVisiteur) -> Optional[Dict[str, Any]]:
        """Identifie les lacunes de contenu"""
        # Analyser les thèmes non couverts
        themes_disponibles = ["meditation", "philosophie", "technique", "spiritualite", "psychologie"]
        themes_manquants = [theme for theme in themes_disponibles if theme not in themes_questions]
        
        # Analyser les types d'actions manquantes
        actions_disponibles = ["meditation", "contemplation", "exploration", "etude", "pratique"]
        actions_manquantes = [action for action in actions_disponibles if action not in types_actions]
        
        if not themes_manquants and not actions_manquantes:
            return None
        
        return {
            "themes": themes_manquants,
            "actions": actions_manquantes,
            "formats": self._suggérer_formats_contenu(progression),
            "niveau": self._determiner_niveau_contenu(progression)
        }

    def _suggérer_formats_contenu(self, progression: ProgressionVisiteur) -> List[str]:
        """Suggère des formats de contenu"""
        formats = []
        
        if progression.niveau_eveil > 7:
            formats.extend(["texte_avance", "meditation_guidee", "contemplation_libre"])
        elif progression.niveau_eveil > 4:
            formats.extend(["texte_intermediaire", "exercices_pratiques", "exemples_concrets"])
        else:
            formats.extend(["texte_simple", "introductions", "explications_etapes"])
        
        return formats

    def _determiner_niveau_contenu(self, progression: ProgressionVisiteur) -> str:
        """Détermine le niveau de complexité du contenu"""
        if progression.score_comprehension > 0.8 and progression.niveau_eveil > 7:
            return "avance"
        elif progression.score_comprehension > 0.6 and progression.niveau_eveil > 4:
            return "intermediaire"
        else:
            return "debutant"

    def _calculer_priorite_contenu(self, lacunes: Dict[str, Any], progression: ProgressionVisiteur) -> float:
        """Calcule la priorité du besoin de contenu"""
        priorite = 0.5
        
        # Facteurs de priorité
        if len(lacunes["themes"]) > 2:
            priorite += 0.2
        if progression.score_comprehension > 0.7:
            priorite += 0.15
        if len(progression.questions_posees) > 3:
            priorite += 0.1
        
        return min(1.0, priorite)

    def _generer_actions_contenu(self, lacunes: Dict[str, Any]) -> List[str]:
        """Génère des actions pour le contenu"""
        actions = []
        
        for theme in lacunes["themes"]:
            actions.append(f"Créer du contenu sur {theme}")
        
        for format_contenu in lacunes["formats"]:
            actions.append(f"Développer le format {format_contenu}")
        
        return actions

    def _predire_personnalisation_future(self, progression: ProgressionVisiteur) -> Optional[Prediction]:
        """Prédit la personnalisation future"""
        # Analyser les préférences actuelles
        preferences = progression.preferences
        
        # Analyser l'historique des actions
        actions_frequentes = self._analyser_actions_frequentes(progression.actions_effectuees)
        
        # Prédire les préférences futures
        preferences_futures = self._predire_preferences_futures(preferences, actions_frequentes, progression)
        
        if not preferences_futures:
            return None
        
        prediction_id = f"personnalisation_{progression.id_visiteur}_{len(self.predictions) + 1}"
        
        return Prediction(
            id=prediction_id,
            type_prediction=TypePrediction.PERSONNALISATION,
            description="Évolution de la personnalisation",
            contenu_prediction={
                "preferences_actuelles": preferences,
                "preferences_predites": preferences_futures,
                "adaptations_suggerees": self._generer_adaptations_personnalisation(preferences_futures)
            },
            niveau_confiance=NiveauConfiance.ELEVE,
            score_confiance=0.75,
            facteurs_influence=["preferences", "actions_frequentes", "evolution_comportement"],
            timestamp_creation=datetime.now().isoformat(),
            horizon_temps=48,  # 2 jours
            impact_estime=0.8,
            actions_suggestees=self._generer_actions_personnalisation(preferences_futures)
        )

    def _analyser_actions_frequentes(self, actions: List[Dict[str, Any]]) -> Dict[str, int]:
        """Analyse les actions fréquentes"""
        frequences = {}
        for action in actions:
            type_action = action.get("type", "")
            frequences[type_action] = frequences.get(type_action, 0) + 1
        
        return frequences

    def _predire_preferences_futures(self, preferences: Dict[str, Any], actions_frequentes: Dict[str, int], progression: ProgressionVisiteur) -> Dict[str, Any]:
        """Prédit les préférences futures"""
        preferences_futures = preferences.copy()
        
        # Ajuster selon les actions fréquentes
        for action, frequence in actions_frequentes.items():
            if frequence > 3:  # Action très fréquente
                if action == "meditation":
                    preferences_futures["rythme"] = "lent"
                    preferences_futures["style"] = "contemplatif"
                elif action == "exploration":
                    preferences_futures["rythme"] = "modere"
                    preferences_futures["style"] = "curieux"
                elif action == "etude":
                    preferences_futures["niveau_detail"] = "eleve"
        
        # Ajuster selon l'évolution du niveau d'éveil
        if progression.niveau_eveil > 6:
            preferences_futures["complexite"] = "avancee"
        
        return preferences_futures

    def _generer_adaptations_personnalisation(self, preferences_futures: Dict[str, Any]) -> Dict[str, Any]:
        """Génère des adaptations de personnalisation"""
        adaptations = {}
        
        if preferences_futures.get("rythme") == "lent":
            adaptations["vitesse_interface"] = "ralentie"
            adaptations["espacement_contenu"] = "augmente"
        
        if preferences_futures.get("style") == "contemplatif":
            adaptations["couleurs"] = "douces"
            adaptations["animations"] = "subtiles"
        
        if preferences_futures.get("complexite") == "avancee":
            adaptations["niveau_detail"] = "maximum"
            adaptations["options_avancees"] = "actives"
        
        return adaptations

    def _generer_actions_personnalisation(self, preferences_futures: Dict[str, Any]) -> List[str]:
        """Génère des actions pour la personnalisation"""
        actions = []
        
        if preferences_futures.get("rythme") == "lent":
            actions.append("Adapter l'interface pour un rythme lent")
        
        if preferences_futures.get("style") == "contemplatif":
            actions.append("Optimiser pour un style contemplatif")
        
        if preferences_futures.get("complexite") == "avancee":
            actions.append("Activer les options avancées")
        
        return actions

    def _detecter_tendances_visiteur(self, progression: ProgressionVisiteur) -> List[Dict[str, Any]]:
        """Détecte les tendances spécifiques au visiteur"""
        tendances = []
        
        # Analyser les patterns de navigation
        if len(progression.temples_visites) > 2:
            tendances.append({
                "type": "navigation",
                "description": f"Préférence pour {progression.temples_visites[-1]}",
                "force": 0.7
            })
        
        # Analyser les patterns émotionnels
        if progression.etat_emotionnel:
            etat_dominant = max(progression.etat_emotionnel.items(), key=lambda x: x[1])
            tendances.append({
                "type": "emotion",
                "description": f"État dominant: {etat_dominant[0]}",
                "force": etat_dominant[1]
            })
        
        return tendances

    def _generer_suggestions_adaptation(self, progression: ProgressionVisiteur) -> List[str]:
        """Génère des suggestions d'adaptation"""
        suggestions = []
        
        # Basé sur le profil
        if progression.profil_detecte == "contemplatif":
            suggestions.append("Proposer plus d'espaces de méditation")
        elif progression.profil_detecte == "curieux":
            suggestions.append("Suggérer de nouvelles explorations")
        elif progression.profil_detecte == "pressé":
            suggestions.append("Optimiser pour un accès rapide")
        
        # Basé sur le niveau d'éveil
        if progression.niveau_eveil > 7:
            suggestions.append("Activer les contenus avancés")
        elif progression.niveau_eveil < 3:
            suggestions.append("Simplifier l'interface")
        
        return suggestions

    def analyser_tendances_communautaires(self) -> Dict[str, Any]:
        """Analyse les tendances communautaires globales"""
        # Obtenir les statistiques de sagesse collective
        stats_sagesse = self.systeme_sagesse.obtenir_statistiques_sagesse_collective()
        
        # Analyser les patterns collectifs
        patterns_populaires = self._identifier_patterns_populaires()
        
        # Détecter les nouvelles tendances
        nouvelles_tendances = self._detecter_nouvelles_tendances()
        
        return {
            "patterns_populaires": patterns_populaires,
            "nouvelles_tendances": nouvelles_tendances,
            "evolution_communautaire": self._analyser_evolution_communautaire(stats_sagesse)
        }

    def _identifier_patterns_populaires(self) -> List[Dict[str, Any]]:
        """Identifie les patterns populaires"""
        patterns = []
        
        for pattern in self.systeme_sagesse.patterns_collectifs.values():
            if pattern.frequence_observation > 10:  # Seuil de popularité
                patterns.append({
                    "id": pattern.id,
                    "description": pattern.description,
                    "frequence": pattern.frequence_observation,
                    "taux_succes": pattern.taux_succes,
                    "type": pattern.type_pattern.value if hasattr(pattern.type_pattern, 'value') else pattern.type_pattern
                })
        
        # Trier par fréquence
        patterns.sort(key=lambda x: x["frequence"], reverse=True)
        return patterns[:5]  # Top 5

    def _detecter_nouvelles_tendances(self) -> List[Dict[str, Any]]:
        """Détecte les nouvelles tendances émergentes"""
        tendances = []
        maintenant = datetime.now()
        
        # Analyser les patterns récents
        patterns_recents = [p for p in self.systeme_sagesse.patterns_collectifs.values()
                           if datetime.fromisoformat(p.timestamp_creation) > maintenant - timedelta(hours=24)]
        
        for pattern in patterns_recents:
            if pattern.frequence_observation >= 3:  # Émergence
                tendances.append({
                    "id": pattern.id,
                    "description": pattern.description,
                    "force_emergence": pattern.frequence_observation / 10,
                    "type": pattern.type_pattern.value if hasattr(pattern.type_pattern, 'value') else pattern.type_pattern
                })
        
        return tendances

    def _analyser_evolution_communautaire(self, stats_sagesse: Dict[str, Any]) -> Dict[str, Any]:
        """Analyse l'évolution de la communauté"""
        return {
            "croissance_patterns": len(stats_sagesse["patterns_par_type"]),
            "confiance_moyenne": stats_sagesse["confiance_moyenne"],
            "activite_recente": stats_sagesse["evolution_recente"]["apprentissages_24h"],
            "satisfaction_globale": stats_sagesse["evolution_recente"]["feedback_moyen_24h"]
        }

    def suggerer_nouveaux_contenus(self) -> List[SuggestionContenu]:
        """Suggère de nouveaux contenus basés sur l'analyse prédictive"""
        suggestions = []
        
        # Analyser les besoins non satisfaits
        besoins_non_satisfaits = self._identifier_besoins_non_satisfaits()
        
        # Analyser les tendances émergentes
        tendances_emergentes = self._detecter_nouvelles_tendances()
        
        # Générer des suggestions
        for besoin in besoins_non_satisfaits:
            suggestion = self._creer_suggestion_contenu(besoin)
            if suggestion:
                suggestions.append(suggestion)
        
        for tendance in tendances_emergentes:
            suggestion = self._creer_suggestion_contenu_tendance(tendance)
            if suggestion:
                suggestions.append(suggestion)
        
        # Trier par priorité
        suggestions.sort(key=lambda x: x.priorite, reverse=True)
        return suggestions[:10]  # Top 10

    def _identifier_besoins_non_satisfaits(self) -> List[Dict[str, Any]]:
        """Identifie les besoins non satisfaits"""
        besoins = []
        
        # Analyser les questions fréquentes sans réponse
        questions_frequentes = self._analyser_questions_frequentes()
        
        # Analyser les patterns avec faible taux de succès
        patterns_faibles = [p for p in self.systeme_sagesse.patterns_collectifs.values()
                           if p.taux_succes < 0.6]
        
        for pattern in patterns_faibles:
            besoins.append({
                "type": "amelioration_pattern",
                "description": f"Améliorer le pattern: {pattern.description}",
                "priorite": 1 - pattern.taux_succes
            })
        
        return besoins

    def _analyser_questions_frequentes(self) -> List[str]:
        """Analyse les questions fréquentes"""
        # Cette méthode analyserait les questions posées par tous les visiteurs
        # Pour l'instant, retourner des exemples
        return [
            "Comment méditer efficacement ?",
            "Qu'est-ce que l'éveil spirituel ?",
            "Comment gérer les émotions ?"
        ]

    def _creer_suggestion_contenu(self, besoin: Dict[str, Any]) -> Optional[SuggestionContenu]:
        """Crée une suggestion de contenu basée sur un besoin"""
        suggestion_id = f"suggestion_{len(self.suggestions_contenu) + 1}"
        
        return SuggestionContenu(
            id=suggestion_id,
            type_contenu="guide_pratique",
            titre=f"Guide: {besoin['description']}",
            description=f"Contenu pour répondre au besoin: {besoin['description']}",
            priorite=besoin["priorite"],
            public_cible=["tous"],
            mots_cles=["guide", "pratique", "aide"],
            format_suggere="texte_interactif",
            timestamp_creation=datetime.now().isoformat()
        )

    def _creer_suggestion_contenu_tendance(self, tendance: Dict[str, Any]) -> Optional[SuggestionContenu]:
        """Crée une suggestion de contenu basée sur une tendance"""
        suggestion_id = f"suggestion_tendance_{len(self.suggestions_contenu) + 1}"
        
        return SuggestionContenu(
            id=suggestion_id,
            type_contenu="contenu_tendance",
            titre=f"Tendance: {tendance['description']}",
            description=f"Contenu sur la tendance émergente: {tendance['description']}",
            priorite=tendance["force_emergence"],
            public_cible=["explorateurs"],
            mots_cles=["tendance", "emergent", "nouveau"],
            format_suggere="interactif",
            timestamp_creation=datetime.now().isoformat()
        )

    def sauvegarder_donnees(self):
        """Sauvegarde toutes les données de prédiction"""
        self._sauvegarder_predictions()
        self._sauvegarder_tendances_communautaires()
        self._sauvegarder_suggestions_contenu()

    def _sauvegarder_predictions(self):
        """Sauvegarde les prédictions"""
        data = {pred_id: {
            "id": prediction.id,
            "type_prediction": prediction.type_prediction.value,
            "description": prediction.description,
            "contenu_prediction": prediction.contenu_prediction,
            "niveau_confiance": prediction.niveau_confiance.value,
            "score_confiance": prediction.score_confiance,
            "facteurs_influence": prediction.facteurs_influence,
            "timestamp_creation": prediction.timestamp_creation,
            "horizon_temps": prediction.horizon_temps,
            "impact_estime": prediction.impact_estime,
            "actions_suggestees": prediction.actions_suggestees
        } for pred_id, prediction in self.predictions.items()}
        
        with open(self.dossier_prediction / "predictions.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _sauvegarder_tendances_communautaires(self):
        """Sauvegarde les tendances communautaires"""
        data = {tendance_id: {
            "id": tendance.id,
            "nom": tendance.nom,
            "description": tendance.description,
            "indicateurs": tendance.indicateurs,
            "force_tendance": tendance.force_tendance,
            "direction": tendance.direction,
            "visiteurs_impliques": tendance.visiteurs_impliques,
            "timestamp_detection": tendance.timestamp_detection,
            "evolution": tendance.evolution
        } for tendance_id, tendance in self.tendances_communautaires.items()}
        
        with open(self.dossier_prediction / "tendances_communautaires.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _sauvegarder_suggestions_contenu(self):
        """Sauvegarde les suggestions de contenu"""
        data = {sugg_id: {
            "id": suggestion.id,
            "type_contenu": suggestion.type_contenu,
            "titre": suggestion.titre,
            "description": suggestion.description,
            "priorite": suggestion.priorite,
            "public_cible": suggestion.public_cible,
            "mots_cles": suggestion.mots_cles,
            "format_suggere": suggestion.format_suggere,
            "timestamp_creation": suggestion.timestamp_creation
        } for sugg_id, suggestion in self.suggestions_contenu.items()}
        
        with open(self.dossier_prediction / "suggestions_contenu.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
