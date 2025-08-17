"""
🌸 Système de Sagesse Collective - Tâche 16.1
Système d'apprentissage collectif et d'évolution organique des parcours
"""
import json
import random
import time
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from .systeme_sauvegarde_progression import ProgressionVisiteur
from .detecteur_etat_emotionnel import EtatEmotionnel

class TypePattern(Enum):
    NAVIGATION = "navigation"
    COMPREHENSION = "comprehension"
    EMOTION = "emotion"
    EXPLORATION = "exploration"
    MEDITATION = "meditation"
    DECOUVERTE = "decouverte"

class TypeProfilHybride(Enum):
    CONTEMPLATIF_CURIEUX = "contemplatif_curieux"
    PRESSÉ_SAGE = "presse_sage"
    OVERWHELMED_CALME = "overwhelmed_calme"
    EXCITÉ_MYSTIQUE = "excite_mystique"
    CURIEUX_EXPLORATEUR = "curieux_explorateur"
    SAGE_ILLUMINE = "sage_illumine"

@dataclass
class PatternCollectif:
    id: str
    type_pattern: TypePattern
    description: str
    caracteristiques: Dict[str, Any]
    frequence_observation: int
    taux_succes: float
    visiteurs_impliques: List[str]
    timestamp_creation: str
    timestamp_derniere_observation: str
    confiance: float
    evolution: List[Dict[str, Any]]

@dataclass
class ProfilHybride:
    id: str
    nom: str
    type_hybride: TypeProfilHybride
    caracteristiques_principales: Dict[str, Any]
    caracteristiques_secondaires: Dict[str, Any]
    parcours_optimal: Dict[str, Any]
    taux_adoption: float
    satisfaction_moyenne: float
    visiteurs_associes: List[str]
    timestamp_creation: str
    evolution: List[Dict[str, Any]]

@dataclass
class ApprentissageCollectif:
    pattern_id: str
    visiteur_id: str
    action: Dict[str, Any]
    resultat: Dict[str, Any]
    feedback: float
    contexte: Dict[str, Any]
    timestamp: str

class SystemeSagesseCollective:
    def __init__(self, dossier_sagesse: str = "data/sagesse_collective"):
        self.dossier_sagesse = Path(dossier_sagesse)
        self.dossier_sagesse.mkdir(parents=True, exist_ok=True)
        
        # Charger les données existantes
        self.patterns_collectifs = self._charger_patterns_collectifs()
        self.profils_hybrides = self._charger_profils_hybrides()
        self.apprentissages = self._charger_apprentissages()
        
        # Paramètres d'apprentissage
        self.seuil_detection_pattern = 5  # Nombre minimum d'observations
        self.seuil_confiance = 0.7  # Seuil de confiance pour les patterns
        self.intervalle_analyse = 3600  # 1 heure

    def _charger_patterns_collectifs(self) -> Dict[str, PatternCollectif]:
        """Charge les patterns collectifs existants"""
        fichier_patterns = self.dossier_sagesse / "patterns_collectifs.json"
        if fichier_patterns.exists():
            with open(fichier_patterns, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {pattern_id: PatternCollectif(**pattern_data) for pattern_id, pattern_data in data.items()}
        
        return {}

    def _charger_profils_hybrides(self) -> Dict[str, ProfilHybride]:
        """Charge les profils hybrides existants"""
        fichier_profils = self.dossier_sagesse / "profils_hybrides.json"
        if fichier_profils.exists():
            with open(fichier_profils, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {profil_id: ProfilHybride(**profil_data) for profil_id, profil_data in data.items()}
        
        return {}

    def _charger_apprentissages(self) -> List[ApprentissageCollectif]:
        """Charge les apprentissages collectifs"""
        fichier_apprentissages = self.dossier_sagesse / "apprentissages.json"
        if fichier_apprentissages.exists():
            with open(fichier_apprentissages, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [ApprentissageCollectif(**apprentissage) for apprentissage in data]
        
        return []

    def analyser_progression_visiteur(self, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """Analyse la progression d'un visiteur pour détecter des patterns"""
        patterns_detectes = []
        
        # Analyser les patterns de navigation
        patterns_navigation = self._analyser_pattern_navigation(progression)
        if patterns_navigation:
            patterns_detectes.extend(patterns_navigation)
        
        # Analyser les patterns de compréhension
        patterns_comprehension = self._analyser_pattern_comprehension(progression)
        if patterns_comprehension:
            patterns_detectes.extend(patterns_comprehension)
        
        # Analyser les patterns émotionnels
        patterns_emotion = self._analyser_pattern_emotion(progression)
        if patterns_emotion:
            patterns_detectes.extend(patterns_emotion)
        
        # Analyser les patterns d'exploration
        patterns_exploration = self._analyser_pattern_exploration(progression)
        if patterns_exploration:
            patterns_detectes.extend(patterns_exploration)
        
        return {
            "patterns_detectes": patterns_detectes,
            "profil_hybride_suggere": self._suggérer_profil_hybride(progression),
            "apprentissages_generes": len(patterns_detectes)
        }

    def _analyser_pattern_navigation(self, progression: ProgressionVisiteur) -> List[Dict[str, Any]]:
        """Analyse les patterns de navigation"""
        patterns = []
        
        # Analyser la séquence de temples visités
        if len(progression.temples_visites) >= 3:
            sequence_temples = progression.temples_visites[-3:]
            pattern_id = f"nav_sequence_{'_'.join(sequence_temples)}"
            
            patterns.append({
                "type": TypePattern.NAVIGATION,
                "id": pattern_id,
                "description": f"Séquence de navigation: {' → '.join(sequence_temples)}",
                "caracteristiques": {
                    "sequence": sequence_temples,
                    "duree_totale": progression.temps_total_passe,
                    "rythme_navigation": self._calculer_rythme_navigation(progression)
                },
                "visiteur_id": progression.id_visiteur
            })
        
        # Analyser les retours en arrière
        retours_arriere = sum(1 for action in progression.actions_effectuees 
                             if action.get("type") == "retour_arriere")
        if retours_arriere > 2:
            patterns.append({
                "type": TypePattern.NAVIGATION,
                "id": f"nav_retours_{retours_arriere}",
                "description": f"Pattern de retours en arrière ({retours_arriere} fois)",
                "caracteristiques": {
                    "nombre_retours": retours_arriere,
                    "ratio_retours": retours_arriere / len(progression.actions_effectuees)
                },
                "visiteur_id": progression.id_visiteur
            })
        
        return patterns

    def _analyser_pattern_comprehension(self, progression: ProgressionVisiteur) -> List[Dict[str, Any]]:
        """Analyse les patterns de compréhension"""
        patterns = []
        
        # Analyser l'évolution du score de compréhension
        if len(progression.actions_effectuees) >= 5:
            scores_evolution = []
            for action in progression.actions_effectuees[-5:]:
                if "score_comprehension" in action:
                    scores_evolution.append(action["score_comprehension"])
            
            if len(scores_evolution) >= 3:
                tendance = self._calculer_tendance(scores_evolution)
                patterns.append({
                    "type": TypePattern.COMPREHENSION,
                    "id": f"comp_tendance_{tendance}",
                    "description": f"Tendance de compréhension: {tendance}",
                    "caracteristiques": {
                        "scores_evolution": scores_evolution,
                        "tendance": tendance,
                        "score_final": progression.score_comprehension
                    },
                    "visiteur_id": progression.id_visiteur
                })
        
        # Analyser les questions posées
        if len(progression.questions_posees) >= 3:
            themes_questions = self._analyser_themes_questions(progression.questions_posees)
            patterns.append({
                "type": TypePattern.COMPREHENSION,
                "id": f"comp_themes_{len(themes_questions)}",
                "description": f"Thèmes de questions: {', '.join(themes_questions)}",
                "caracteristiques": {
                    "themes": themes_questions,
                    "nombre_questions": len(progression.questions_posees),
                    "complexite_questions": self._calculer_complexite_questions(progression.questions_posees)
                },
                "visiteur_id": progression.id_visiteur
            })
        
        return patterns

    def _analyser_pattern_emotion(self, progression: ProgressionVisiteur) -> List[Dict[str, Any]]:
        """Analyse les patterns émotionnels"""
        patterns = []
        
        if not progression.etat_emotionnel:
            return patterns
        
        # Analyser l'état émotionnel dominant
        etat_dominant = max(progression.etat_emotionnel.items(), key=lambda x: x[1])
        patterns.append({
            "type": TypePattern.EMOTION,
            "id": f"emotion_dominant_{etat_dominant[0]}",
            "description": f"État émotionnel dominant: {etat_dominant[0]} ({etat_dominant[1]:.2f})",
            "caracteristiques": {
                "etat_dominant": etat_dominant[0],
                "intensite": etat_dominant[1],
                "etats_secondaires": self._identifier_etats_secondaires(progression.etat_emotionnel)
            },
            "visiteur_id": progression.id_visiteur
        })
        
        # Analyser la stabilité émotionnelle
        stabilite = self._calculer_stabilite_emotionnelle(progression)
        if stabilite < 0.5:  # Instable
            patterns.append({
                "type": TypePattern.EMOTION,
                "id": "emotion_instable",
                "description": "Pattern émotionnel instable",
                "caracteristiques": {
                    "stabilite": stabilite,
                    "transitions_rapides": True
                },
                "visiteur_id": progression.id_visiteur
            })
        
        return patterns

    def _analyser_pattern_exploration(self, progression: ProgressionVisiteur) -> List[Dict[str, Any]]:
        """Analyse les patterns d'exploration"""
        patterns = []
        
        # Analyser la profondeur d'exploration
        profondeur = self._calculer_profondeur_exploration(progression)
        patterns.append({
            "type": TypePattern.EXPLORATION,
            "id": f"expl_profondeur_{profondeur}",
            "description": f"Profondeur d'exploration: {profondeur}",
            "caracteristiques": {
                "profondeur": profondeur,
                "temples_visites": progression.temples_visites,
                "temps_par_temple": self._calculer_temps_par_temple(progression)
            },
            "visiteur_id": progression.id_visiteur
        })
        
        # Analyser les découvertes
        if len(progression.actions_effectuees) > 0:
            decouvertes = [action for action in progression.actions_effectuees 
                          if action.get("type") == "decouverte"]
            if decouvertes:
                patterns.append({
                    "type": TypePattern.DECOUVERTE,
                    "id": f"expl_decouvertes_{len(decouvertes)}",
                    "description": f"Pattern de découvertes ({len(decouvertes)} découvertes)",
                    "caracteristiques": {
                        "nombre_decouvertes": len(decouvertes),
                        "types_decouvertes": [d.get("type_decouverte", "inconnu") for d in decouvertes],
                        "frequence_decouvertes": len(decouvertes) / progression.temps_total_passe * 3600  # par heure
                    },
                    "visiteur_id": progression.id_visiteur
                })
        
        return patterns

    def _calculer_rythme_navigation(self, progression: ProgressionVisiteur) -> str:
        """Calcule le rythme de navigation"""
        if progression.temps_total_passe < 600:  # Moins de 10 minutes
            return "rapide"
        elif progression.temps_total_passe < 1800:  # Moins de 30 minutes
            return "modere"
        else:
            return "lent"

    def _calculer_tendance(self, valeurs: List[float]) -> str:
        """Calcule la tendance d'une série de valeurs"""
        if len(valeurs) < 2:
            return "stable"
        
        differences = [valeurs[i] - valeurs[i-1] for i in range(1, len(valeurs))]
        moyenne_diff = sum(differences) / len(differences)
        
        if moyenne_diff > 0.1:
            return "croissante"
        elif moyenne_diff < -0.1:
            return "decroissante"
        else:
            return "stable"

    def _analyser_themes_questions(self, questions: List[str]) -> List[str]:
        """Analyse les thèmes des questions posées"""
        themes = []
        mots_cles = {
            "conscience": ["conscience", "éveil", "spirituel", "transcendance"],
            "technique": ["comment", "technique", "méthode", "procédure"],
            "philosophie": ["pourquoi", "sens", "signification", "essence"],
            "pratique": ["pratique", "exercice", "méditation", "contemplation"]
        }
        
        for question in questions:
            question_lower = question.lower()
            for theme, mots in mots_cles.items():
                if any(mot in question_lower for mot in mots):
                    if theme not in themes:
                        themes.append(theme)
        
        return themes

    def _calculer_complexite_questions(self, questions: List[str]) -> float:
        """Calcule la complexité moyenne des questions"""
        if not questions:
            return 0.0
        
        complexites = []
        for question in questions:
            # Facteurs de complexité
            mots = len(question.split())
            longueur = len(question)
            questions_imbriquees = question.count("?")
            
            complexite = (mots * 0.3 + longueur * 0.1 + questions_imbriquees * 0.5) / 10
            complexites.append(min(complexite, 1.0))
        
        return sum(complexites) / len(complexites)

    def _identifier_etats_secondaires(self, etats: Dict[str, float]) -> List[str]:
        """Identifie les états émotionnels secondaires"""
        etats_tries = sorted(etats.items(), key=lambda x: x[1], reverse=True)
        return [etat for etat, intensite in etats_tries[1:3] if intensite > 0.3]

    def _calculer_stabilite_emotionnelle(self, progression: ProgressionVisiteur) -> float:
        """Calcule la stabilité émotionnelle"""
        if len(progression.actions_effectuees) < 3:
            return 1.0
        
        # Analyser les changements d'état émotionnel
        changements = 0
        for i in range(1, len(progression.actions_effectuees)):
            action_prec = progression.actions_effectuees[i-1]
            action_act = progression.actions_effectuees[i]
            
            if "etat_emotionnel" in action_prec and "etat_emotionnel" in action_act:
                if action_prec["etat_emotionnel"] != action_act["etat_emotionnel"]:
                    changements += 1
        
        stabilite = 1.0 - (changements / (len(progression.actions_effectuees) - 1))
        return max(0.0, stabilite)

    def _calculer_profondeur_exploration(self, progression: ProgressionVisiteur) -> str:
        """Calcule la profondeur d'exploration"""
        temps_moyen_par_temple = progression.temps_total_passe / max(len(progression.temples_visites), 1)
        
        if temps_moyen_par_temple > 1800:  # Plus de 30 minutes par temple
            return "profonde"
        elif temps_moyen_par_temple > 600:  # Plus de 10 minutes par temple
            return "moderee"
        else:
            return "superficielle"

    def _calculer_temps_par_temple(self, progression: ProgressionVisiteur) -> Dict[str, int]:
        """Calcule le temps passé par temple"""
        temps_par_temple = {}
        for action in progression.actions_effectuees:
            if "temple" in action:
                temple = action["temple"]
                temps_par_temple[temple] = temps_par_temple.get(temple, 0) + action.get("duree", 0)
        
        return temps_par_temple

    def _suggérer_profil_hybride(self, progression: ProgressionVisiteur) -> Optional[ProfilHybride]:
        """Suggère un profil hybride basé sur l'analyse"""
        caracteristiques = self._extraire_caracteristiques_visiteur(progression)
        
        # Chercher un profil hybride existant qui correspond
        for profil in self.profils_hybrides.values():
            if self._correspondance_profil(profil, caracteristiques) > 0.8:
                return profil
        
        # Créer un nouveau profil hybride si nécessaire
        if len(self.profils_hybrides) < 10:  # Limite pour éviter la fragmentation
            nouveau_profil = self._creer_profil_hybride(caracteristiques, progression)
            if nouveau_profil:
                self.profils_hybrides[nouveau_profil.id] = nouveau_profil
                return nouveau_profil
        
        return None

    def _extraire_caracteristiques_visiteur(self, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """Extrait les caractéristiques principales du visiteur"""
        return {
            "profil_principal": progression.profil_detecte,
            "niveau_eveil": progression.niveau_eveil,
            "score_comprehension": progression.score_comprehension,
            "rythme_navigation": self._calculer_rythme_navigation(progression),
            "profondeur_exploration": self._calculer_profondeur_exploration(progression),
            "etat_emotionnel_dominant": max(progression.etat_emotionnel.items(), key=lambda x: x[1])[0] if progression.etat_emotionnel else "calme",
            "nombre_temples_visites": len(progression.temples_visites),
            "temps_total": progression.temps_total_passe
        }

    def _correspondance_profil(self, profil: ProfilHybride, caracteristiques: Dict[str, Any]) -> float:
        """Calcule la correspondance avec un profil hybride"""
        correspondance = 0.0
        total_criteres = 0
        
        # Vérifier la correspondance avec les caractéristiques principales
        for critere, valeur in profil.caracteristiques_principales.items():
            if critere in caracteristiques:
                total_criteres += 1
                if caracteristiques[critere] == valeur:
                    correspondance += 1.0
                elif isinstance(valeur, (int, float)) and isinstance(caracteristiques[critere], (int, float)):
                    # Correspondance approximative pour les valeurs numériques
                    difference = abs(caracteristiques[critere] - valeur) / max(valeur, 1)
                    correspondance += max(0, 1 - difference)
        
        return correspondance / total_criteres if total_criteres > 0 else 0.0

    def _creer_profil_hybride(self, caracteristiques: Dict[str, Any], progression: ProgressionVisiteur) -> Optional[ProfilHybride]:
        """Crée un nouveau profil hybride"""
        # Déterminer le type hybride
        type_hybride = self._determiner_type_hybride(caracteristiques)
        
        if not type_hybride:
            return None
        
        profil_id = f"hybride_{type_hybride.value}_{len(self.profils_hybrides) + 1}"
        
        return ProfilHybride(
            id=profil_id,
            nom=f"Profil {type_hybride.value.replace('_', ' ').title()}",
            type_hybride=type_hybride,
            caracteristiques_principales=caracteristiques,
            caracteristiques_secondaires=self._extraire_caracteristiques_secondaires(progression),
            parcours_optimal=self._generer_parcours_optimal(caracteristiques),
            taux_adoption=1.0,  # Premier visiteur
            satisfaction_moyenne=progression.score_comprehension,
            visiteurs_associes=[progression.id_visiteur],
            timestamp_creation=datetime.now().isoformat(),
            evolution=[]
        )

    def _determiner_type_hybride(self, caracteristiques: Dict[str, Any]) -> Optional[TypeProfilHybride]:
        """Détermine le type de profil hybride"""
        profil_principal = caracteristiques.get("profil_principal", "")
        etat_dominant = caracteristiques.get("etat_emotionnel_dominant", "")
        niveau_eveil = caracteristiques.get("niveau_eveil", 0)
        
        if profil_principal == "contemplatif" and etat_dominant == "curieux":
            return TypeProfilHybride.CONTEMPLATIF_CURIEUX
        elif profil_principal == "pressé" and niveau_eveil > 5:
            return TypeProfilHybride.PRESSÉ_SAGE
        elif etat_dominant == "overwhelmed" and caracteristiques.get("rythme_navigation") == "lent":
            return TypeProfilHybride.OVERWHELMED_CALME
        elif etat_dominant == "excite" and niveau_eveil > 7:
            return TypeProfilHybride.EXCITÉ_MYSTIQUE
        elif profil_principal == "curieux" and caracteristiques.get("profondeur_exploration") == "profonde":
            return TypeProfilHybride.CURIEUX_EXPLORATEUR
        elif niveau_eveil > 8:
            return TypeProfilHybride.SAGE_ILLUMINE
        
        return None

    def _extraire_caracteristiques_secondaires(self, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """Extrait les caractéristiques secondaires"""
        return {
            "questions_posees": len(progression.questions_posees),
            "actions_effectuees": len(progression.actions_effectuees),
            "preferences": progression.preferences,
            "derniere_activite": progression.date_derniere_activite
        }

    def _generer_parcours_optimal(self, caracteristiques: Dict[str, Any]) -> Dict[str, Any]:
        """Génère un parcours optimal pour le profil hybride"""
        return {
            "etapes_recommandees": self._generer_etapes_recommandees(caracteristiques),
            "rythme_suggere": caracteristiques.get("rythme_navigation", "modere"),
            "niveau_complexite": self._determiner_niveau_complexite(caracteristiques),
            "adaptations_emotionnelles": self._generer_adaptations_emotionnelles(caracteristiques)
        }

    def _generer_etapes_recommandees(self, caracteristiques: Dict[str, Any]) -> List[str]:
        """Génère les étapes recommandées"""
        etapes = ["accueil_personnalise"]
        
        profil = caracteristiques.get("profil_principal", "")
        niveau_eveil = caracteristiques.get("niveau_eveil", 0)
        
        if profil == "contemplatif":
            etapes.extend(["temple_eveil", "meditation_guidee", "contemplation_libre"])
        elif profil == "curieux":
            etapes.extend(["cartographie_refuge", "exploration_libre", "decouvertes_interactives"])
        elif profil == "pressé":
            etapes.extend(["parcours_express", "essentiels_refuge", "resume_rapide"])
        
        if niveau_eveil > 5:
            etapes.append("temple_reconciliation")
        
        return etapes

    def _determiner_niveau_complexite(self, caracteristiques: Dict[str, Any]) -> str:
        """Détermine le niveau de complexité optimal"""
        score_comprehension = caracteristiques.get("score_comprehension", 0)
        niveau_eveil = caracteristiques.get("niveau_eveil", 0)
        
        if score_comprehension > 0.8 and niveau_eveil > 7:
            return "avance"
        elif score_comprehension > 0.6 and niveau_eveil > 4:
            return "intermediaire"
        else:
            return "debutant"

    def _generer_adaptations_emotionnelles(self, caracteristiques: Dict[str, Any]) -> Dict[str, Any]:
        """Génère les adaptations émotionnelles"""
        etat_dominant = caracteristiques.get("etat_emotionnel_dominant", "calme")
        
        adaptations = {
            "contemplatif": {"rythme": "lent", "espacement": "large", "encouragements": "discrets"},
            "curieux": {"rythme": "modere", "espacement": "normal", "encouragements": "stimulants"},
            "pressé": {"rythme": "rapide", "espacement": "serre", "encouragements": "directs"},
            "overwhelmed": {"rythme": "tres_lent", "espacement": "tres_large", "encouragements": "apaisants"},
            "excite": {"rythme": "dynamique", "espacement": "variable", "encouragements": "energiques"},
            "calme": {"rythme": "harmonieux", "espacement": "equilibre", "encouragements": "serenes"}
        }
        
        return adaptations.get(etat_dominant, adaptations["calme"])

    def enregistrer_apprentissage(self, progression: ProgressionVisiteur, action: Dict[str, Any], resultat: Dict[str, Any], feedback: float):
        """Enregistre un apprentissage collectif"""
        apprentissage = ApprentissageCollectif(
            pattern_id=f"pattern_{len(self.apprentissages) + 1}",
            visiteur_id=progression.id_visiteur,
            action=action,
            resultat=resultat,
            feedback=feedback,
            contexte=self._extraire_contexte_apprentissage(progression),
            timestamp=datetime.now().isoformat()
        )
        
        self.apprentissages.append(apprentissage)
        
        # Analyser si un nouveau pattern émerge
        self._analyser_emergence_pattern(apprentissage)
        
        # Sauvegarder
        self._sauvegarder_apprentissages()

    def _extraire_contexte_apprentissage(self, progression: ProgressionVisiteur) -> Dict[str, Any]:
        """Extrait le contexte pour l'apprentissage"""
        return {
            "profil": progression.profil_detecte,
            "niveau_eveil": progression.niveau_eveil,
            "etat_emotionnel": progression.etat_emotionnel,
            "score_comprehension": progression.score_comprehension,
            "temps_session": progression.temps_total_passe,
            "temples_visites": progression.temples_visites
        }

    def _analyser_emergence_pattern(self, apprentissage: ApprentissageCollectif):
        """Analyse l'émergence de nouveaux patterns"""
        # Chercher des patterns similaires
        patterns_similaires = self._trouver_patterns_similaires(apprentissage)
        
        if patterns_similaires:
            # Mettre à jour le pattern existant
            pattern_existant = patterns_similaires[0]
            self._mettre_a_jour_pattern(pattern_existant, apprentissage)
        else:
            # Créer un nouveau pattern si suffisamment d'observations
            if self._verifier_conditions_nouveau_pattern(apprentissage):
                self._creer_nouveau_pattern(apprentissage)

    def _trouver_patterns_similaires(self, apprentissage: ApprentissageCollectif) -> List[PatternCollectif]:
        """Trouve des patterns similaires"""
        patterns_similaires = []
        
        for pattern in self.patterns_collectifs.values():
            if self._calculer_similarite_pattern(pattern, apprentissage) > 0.7:
                patterns_similaires.append(pattern)
        
        return patterns_similaires

    def _calculer_similarite_pattern(self, pattern: PatternCollectif, apprentissage: ApprentissageCollectif) -> float:
        """Calcule la similarité entre un pattern et un apprentissage"""
        # Comparer les caractéristiques principales
        caracteristiques_pattern = pattern.caracteristiques
        caracteristiques_apprentissage = apprentissage.action
        
        similarite = 0.0
        total_criteres = 0
        
        for cle in caracteristiques_pattern:
            if cle in caracteristiques_apprentissage:
                total_criteres += 1
                if caracteristiques_pattern[cle] == caracteristiques_apprentissage[cle]:
                    similarite += 1.0
        
        return similarite / total_criteres if total_criteres > 0 else 0.0

    def _verifier_conditions_nouveau_pattern(self, apprentissage: ApprentissageCollectif) -> bool:
        """Vérifie les conditions pour créer un nouveau pattern"""
        # Vérifier le feedback positif
        if apprentissage.feedback < 0.6:
            return False
        
        # Vérifier la fréquence d'observation
        apprentissages_similaires = [a for a in self.apprentissages 
                                    if self._calculer_similarite_apprentissage(a, apprentissage) > 0.5]
        
        return len(apprentissages_similaires) >= self.seuil_detection_pattern

    def _calculer_similarite_apprentissage(self, apprentissage1: ApprentissageCollectif, apprentissage2: ApprentissageCollectif) -> float:
        """Calcule la similarité entre deux apprentissages"""
        # Comparer les actions
        if apprentissage1.action.get("type") == apprentissage2.action.get("type"):
            return 0.8
        return 0.2

    def _creer_nouveau_pattern(self, apprentissage: ApprentissageCollectif):
        """Crée un nouveau pattern collectif"""
        pattern_id = f"pattern_{len(self.patterns_collectifs) + 1}"
        
        pattern = PatternCollectif(
            id=pattern_id,
            type_pattern=self._determiner_type_pattern(apprentissage),
            description=f"Nouveau pattern détecté: {apprentissage.action.get('type', 'inconnu')}",
            caracteristiques=apprentissage.action,
            frequence_observation=1,
            taux_succes=apprentissage.feedback,
            visiteurs_impliques=[apprentissage.visiteur_id],
            timestamp_creation=datetime.now().isoformat(),
            timestamp_derniere_observation=datetime.now().isoformat(),
            confiance=0.5,  # Confiance initiale
            evolution=[]
        )
        
        self.patterns_collectifs[pattern_id] = pattern
        self._sauvegarder_patterns_collectifs()

    def _determiner_type_pattern(self, apprentissage: ApprentissageCollectif) -> TypePattern:
        """Détermine le type de pattern"""
        type_action = apprentissage.action.get("type", "")
        
        if "navigation" in type_action:
            return TypePattern.NAVIGATION
        elif "comprehension" in type_action or "question" in type_action:
            return TypePattern.COMPREHENSION
        elif "emotion" in type_action:
            return TypePattern.EMOTION
        elif "exploration" in type_action:
            return TypePattern.EXPLORATION
        elif "meditation" in type_action:
            return TypePattern.MEDITATION
        else:
            return TypePattern.DECOUVERTE

    def _mettre_a_jour_pattern(self, pattern: PatternCollectif, apprentissage: ApprentissageCollectif):
        """Met à jour un pattern existant"""
        pattern.frequence_observation += 1
        pattern.taux_succes = (pattern.taux_succes * (pattern.frequence_observation - 1) + apprentissage.feedback) / pattern.frequence_observation
        pattern.timestamp_derniere_observation = datetime.now().isoformat()
        
        if apprentissage.visiteur_id not in pattern.visiteurs_impliques:
            pattern.visiteurs_impliques.append(apprentissage.visiteur_id)
        
        # Mettre à jour la confiance
        pattern.confiance = min(1.0, pattern.frequence_observation / 10)
        
        # Enregistrer l'évolution
        pattern.evolution.append({
            "timestamp": datetime.now().isoformat(),
            "frequence": pattern.frequence_observation,
            "taux_succes": pattern.taux_succes,
            "confiance": pattern.confiance
        })
        
        self._sauvegarder_patterns_collectifs()

    def _sauvegarder_patterns_collectifs(self):
        """Sauvegarde les patterns collectifs"""
        data = {pattern_id: {
            "id": pattern.id,
            "type_pattern": pattern.type_pattern.value if hasattr(pattern.type_pattern, 'value') else pattern.type_pattern,
            "description": pattern.description,
            "caracteristiques": pattern.caracteristiques,
            "frequence_observation": pattern.frequence_observation,
            "taux_succes": pattern.taux_succes,
            "visiteurs_impliques": pattern.visiteurs_impliques,
            "timestamp_creation": pattern.timestamp_creation,
            "timestamp_derniere_observation": pattern.timestamp_derniere_observation,
            "confiance": pattern.confiance,
            "evolution": pattern.evolution
        } for pattern_id, pattern in self.patterns_collectifs.items()}
        
        with open(self.dossier_sagesse / "patterns_collectifs.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _sauvegarder_profils_hybrides(self):
        """Sauvegarde les profils hybrides"""
        data = {profil_id: {
            "id": profil.id,
            "nom": profil.nom,
            "type_hybride": profil.type_hybride.value if hasattr(profil.type_hybride, 'value') else profil.type_hybride,
            "caracteristiques_principales": profil.caracteristiques_principales,
            "caracteristiques_secondaires": profil.caracteristiques_secondaires,
            "parcours_optimal": profil.parcours_optimal,
            "taux_adoption": profil.taux_adoption,
            "satisfaction_moyenne": profil.satisfaction_moyenne,
            "visiteurs_associes": profil.visiteurs_associes,
            "timestamp_creation": profil.timestamp_creation,
            "evolution": profil.evolution
        } for profil_id, profil in self.profils_hybrides.items()}
        
        with open(self.dossier_sagesse / "profils_hybrides.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _sauvegarder_apprentissages(self):
        """Sauvegarde les apprentissages"""
        data = [{
            "pattern_id": apprentissage.pattern_id,
            "visiteur_id": apprentissage.visiteur_id,
            "action": apprentissage.action,
            "resultat": apprentissage.resultat,
            "feedback": apprentissage.feedback,
            "contexte": apprentissage.contexte,
            "timestamp": apprentissage.timestamp
        } for apprentissage in self.apprentissages]
        
        with open(self.dossier_sagesse / "apprentissages.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def obtenir_statistiques_sagesse_collective(self) -> Dict[str, Any]:
        """Obtient les statistiques de la sagesse collective"""
        return {
            "total_patterns": len(self.patterns_collectifs),
            "total_profils_hybrides": len(self.profils_hybrides),
            "total_apprentissages": len(self.apprentissages),
            "patterns_par_type": self._compter_patterns_par_type(),
            "confiance_moyenne": self._calculer_confiance_moyenne(),
            "evolution_recente": self._analyser_evolution_recente()
        }

    def _compter_patterns_par_type(self) -> Dict[str, int]:
        """Compte les patterns par type"""
        compteurs = {}
        for pattern in self.patterns_collectifs.values():
            type_pattern = pattern.type_pattern.value if hasattr(pattern.type_pattern, 'value') else pattern.type_pattern
            compteurs[type_pattern] = compteurs.get(type_pattern, 0) + 1
        return compteurs

    def _calculer_confiance_moyenne(self) -> float:
        """Calcule la confiance moyenne des patterns"""
        if not self.patterns_collectifs:
            return 0.0
        
        confiances = [pattern.confiance for pattern in self.patterns_collectifs.values()]
        return sum(confiances) / len(confiances)

    def _analyser_evolution_recente(self) -> Dict[str, Any]:
        """Analyse l'évolution récente de la sagesse collective"""
        maintenant = datetime.now()
        apprentissages_recents = [a for a in self.apprentissages 
                                 if datetime.fromisoformat(a.timestamp) > maintenant - timedelta(hours=24)]
        
        return {
            "apprentissages_24h": len(apprentissages_recents),
            "nouveaux_patterns_24h": len([p for p in self.patterns_collectifs.values() 
                                        if datetime.fromisoformat(p.timestamp_creation) > maintenant - timedelta(hours=24)]),
            "feedback_moyen_24h": sum(a.feedback for a in apprentissages_recents) / len(apprentissages_recents) if apprentissages_recents else 0.0
        }
