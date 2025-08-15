"""
🌸 Détecteur d'État Émotionnel - Tâche 13.1
Système de détection et d'adaptation aux états émotionnels des visiteurs
"""

import json
import time
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from systeme_sauvegarde_progression import ProgressionVisiteur

class EtatEmotionnel(Enum):
    """🌸 États émotionnels détectés"""
    CONTEMPLATIF = "contemplatif"
    CURIEUX = "curieux"
    PRESSÉ = "presse"
    OVERWHELMED = "overwhelmed"
    CONCENTRÉ = "concentre"
    DISTRAIT = "distrait"
    EXCITÉ = "excite"
    CALME = "calme"
    STRESSÉ = "stresse"
    ÉMERVEILLÉ = "emerveille"

class RythmeNavigation(Enum):
    """🌸 Rythmes de navigation détectés"""
    LENT_ET_RÉFLÉCHI = "lent_et_reflechi"
    MODÉRÉ = "modere"
    RAPIDE = "rapide"
    SACCADÉ = "saccade"
    PAUSE_LONGUE = "pause_longue"
    CONTINU = "continu"

@dataclass
class AnalyseEmotionnelle:
    """🌸 Résultat d'analyse émotionnelle"""
    etat_principal: EtatEmotionnel
    etats_secondaires: List[EtatEmotionnel]
    rythme_navigation: RythmeNavigation
    niveau_stress: float  # 0.0 à 1.0
    niveau_engagement: float  # 0.0 à 1.0
    niveau_surcharge: float  # 0.0 à 1.0
    confiance_analyse: float  # 0.0 à 1.0
    timestamp: str
    contexte: Dict[str, Any]

@dataclass
class PatternNavigation:
    """🌸 Pattern de navigation détecté"""
    temps_entre_actions: List[float]  # en secondes
    types_actions: List[str]
    pauses_longues: List[float]  # durées des pauses
    vitesse_lecture: float  # mots par minute estimée
    retours_arrière: int
    demandes_aide: int
    explorations_profondes: int

class DetecteurEtatEmotionnel:
    """
    🌸 Détecteur d'état émotionnel intelligent
    Analyse les patterns de navigation et les réactions pour adapter l'expérience
    """
    
    def __init__(self, dossier_donnees: str = "data/emotions"):
        """
        🌸 Initialise le détecteur d'état émotionnel
        
        Args:
            dossier_donnees: Dossier pour stocker les données d'analyse
        """
        self.dossier_donnees = Path(dossier_donnees)
        self.dossier_donnees.mkdir(parents=True, exist_ok=True)
        
        # Seuils de détection
        self.seuils = {
            "pause_contemplative": 30.0,  # secondes
            "pause_stress": 5.0,  # secondes
            "vitesse_rapide": 10.0,  # secondes entre actions
            "vitesse_lente": 60.0,  # secondes entre actions
            "surcharge_actions": 15,  # actions en 5 minutes
            "engagement_minimal": 0.3,
            "stress_eleve": 0.7
        }
        
        # Modèles de patterns émotionnels
        self.patterns_emotionnels = self._charger_patterns_emotionnels()
    
    def _charger_patterns_emotionnels(self) -> Dict[str, Dict[str, Any]]:
        """🌸 Charge les patterns émotionnels de référence"""
        fichier_patterns = self.dossier_donnees / "patterns_emotionnels.json"
        
        if fichier_patterns.exists():
            try:
                with open(fichier_patterns, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Erreur lors du chargement des patterns: {e}")
        
        # Patterns par défaut
        return {
            "contemplatif": {
                "temps_entre_actions": [45, 120, 90, 60],
                "types_actions": ["lecture_profonde", "pause_reflexion", "question_philosophique"],
                "pauses_longues": [60, 120, 90],
                "vitesse_lecture": 150,  # mots/minute
                "retours_arrière": 2,
                "demandes_aide": 1,
                "explorations_profondes": 3
            },
            "curieux": {
                "temps_entre_actions": [20, 35, 25, 30],
                "types_actions": ["exploration_libre", "question_technique", "découverte"],
                "pauses_longues": [30, 45],
                "vitesse_lecture": 200,
                "retours_arrière": 1,
                "demandes_aide": 2,
                "explorations_profondes": 2
            },
            "presse": {
                "temps_entre_actions": [5, 8, 12, 6],
                "types_actions": ["navigation_rapide", "recherche_ciblee", "raccourci"],
                "pauses_longues": [10, 15],
                "vitesse_lecture": 300,
                "retours_arrière": 0,
                "demandes_aide": 0,
                "explorations_profondes": 0
            },
            "overwhelmed": {
                "temps_entre_actions": [120, 180, 90, 240],
                "types_actions": ["pause_longue", "retour_accueil", "demande_aide"],
                "pauses_longues": [180, 300, 240],
                "vitesse_lecture": 100,
                "retours_arrière": 5,
                "demandes_aide": 4,
                "explorations_profondes": 0
            }
        }
    
    def analyser_etat_emotionnel(self, progression: ProgressionVisiteur) -> AnalyseEmotionnelle:
        """
        🌸 Analyse l'état émotionnel d'un visiteur
        
        Args:
            progression: Progression du visiteur à analyser
            
        Returns:
            Analyse émotionnelle complète
        """
        # Extraire les patterns de navigation
        pattern_nav = self._extraire_pattern_navigation(progression)
        
        # Analyser le rythme
        rythme = self._determiner_rythme_navigation(pattern_nav)
        
        # Détecter l'état émotionnel principal
        etat_principal = self._detecter_etat_principal(pattern_nav, rythme)
        
        # Détecter les états secondaires
        etats_secondaires = self._detecter_etats_secondaires(pattern_nav, etat_principal)
        
        # Calculer les niveaux
        niveau_stress = self._calculer_niveau_stress(pattern_nav)
        niveau_engagement = self._calculer_niveau_engagement(pattern_nav)
        niveau_surcharge = self._calculer_niveau_surcharge(pattern_nav)
        
        # Calculer la confiance de l'analyse
        confiance = self._calculer_confiance_analyse(pattern_nav, etat_principal)
        
        return AnalyseEmotionnelle(
            etat_principal=etat_principal,
            etats_secondaires=etats_secondaires,
            rythme_navigation=rythme,
            niveau_stress=niveau_stress,
            niveau_engagement=niveau_engagement,
            niveau_surcharge=niveau_surcharge,
            confiance_analyse=confiance,
            timestamp=datetime.now().isoformat(),
            contexte=self._generer_contexte_analyse(pattern_nav, etat_principal)
        )
    
    def _extraire_pattern_navigation(self, progression: ProgressionVisiteur) -> PatternNavigation:
        """🌸 Extrait le pattern de navigation des actions"""
        actions = progression.actions_effectuees
        
        if not actions:
            return PatternNavigation(
                temps_entre_actions=[],
                types_actions=[],
                pauses_longues=[],
                vitesse_lecture=200.0,
                retours_arrière=0,
                demandes_aide=0,
                explorations_profondes=0
            )
        
        # Calculer les temps entre actions
        temps_entre_actions = []
        types_actions = []
        pauses_longues = []
        
        for i in range(1, len(actions)):
            prev_time = datetime.fromisoformat(actions[i-1]["timestamp"])
            curr_time = datetime.fromisoformat(actions[i]["timestamp"])
            temps_ecoule = (curr_time - prev_time).total_seconds()
            temps_entre_actions.append(temps_ecoule)
            
            # Détecter les pauses longues
            if temps_ecoule > self.seuils["pause_contemplative"]:
                pauses_longues.append(temps_ecoule)
            
            types_actions.append(actions[i].get("type", "action_generique"))
        
        # Analyser les types d'actions
        retours_arriere = sum(1 for action in actions if action.get("type") == "retour_arriere")
        demandes_aide = sum(1 for action in actions if action.get("type") == "demande_aide")
        explorations_profondes = sum(1 for action in actions if action.get("type") == "exploration_profonde")
        
        # Estimer la vitesse de lecture (basée sur le contenu lu)
        vitesse_lecture = self._estimer_vitesse_lecture(actions)
        
        return PatternNavigation(
            temps_entre_actions=temps_entre_actions,
            types_actions=types_actions,
            pauses_longues=pauses_longues,
            vitesse_lecture=vitesse_lecture,
            retours_arrière=retours_arriere,
            demandes_aide=demandes_aide,
            explorations_profondes=explorations_profondes
        )
    
    def _determiner_rythme_navigation(self, pattern: PatternNavigation) -> RythmeNavigation:
        """🌸 Détermine le rythme de navigation"""
        if not pattern.temps_entre_actions:
            return RythmeNavigation.MODÉRÉ
        
        temps_moyen = sum(pattern.temps_entre_actions) / len(pattern.temps_entre_actions)
        
        if temps_moyen < self.seuils["vitesse_rapide"]:
            return RythmeNavigation.RAPIDE
        elif temps_moyen > self.seuils["vitesse_lente"]:
            return RythmeNavigation.LENT_ET_RÉFLÉCHI
        elif len(pattern.pauses_longues) > 2:
            return RythmeNavigation.PAUSE_LONGUE
        elif self._detecter_saccades(pattern.temps_entre_actions):
            return RythmeNavigation.SACCADÉ
        else:
            return RythmeNavigation.CONTINU
    
    def _detecter_saccades(self, temps_actions: List[float]) -> bool:
        """🌸 Détecte les saccades dans la navigation"""
        if len(temps_actions) < 3:
            return False
        
        variations = []
        for i in range(1, len(temps_actions)):
            variation = abs(temps_actions[i] - temps_actions[i-1])
            variations.append(variation)
        
        # Si les variations sont importantes, c'est saccadé
        variation_moyenne = sum(variations) / len(variations)
        return variation_moyenne > 30.0  # plus de 30 secondes de variation moyenne
    
    def _detecter_etat_principal(self, pattern: PatternNavigation, rythme: RythmeNavigation) -> EtatEmotionnel:
        """🌸 Détecte l'état émotionnel principal"""
        # Analyser les patterns
        score_contemplatif = self._calculer_score_contemplatif(pattern)
        score_curieux = self._calculer_score_curieux(pattern)
        score_presse = self._calculer_score_presse(pattern)
        score_overwhelmed = self._calculer_score_overwhelmed(pattern)
        
        # Trouver le score le plus élevé
        scores = {
            EtatEmotionnel.CONTEMPLATIF: score_contemplatif,
            EtatEmotionnel.CURIEUX: score_curieux,
            EtatEmotionnel.PRESSÉ: score_presse,
            EtatEmotionnel.OVERWHELMED: score_overwhelmed
        }
        
        return max(scores, key=scores.get)
    
    def _calculer_score_contemplatif(self, pattern: PatternNavigation) -> float:
        """🌸 Calcule le score contemplatif"""
        score = 0.0
        
        # Pauses longues
        if pattern.pauses_longues:
            score += len(pattern.pauses_longues) * 0.3
        
        # Temps moyen élevé
        if pattern.temps_entre_actions:
            temps_moyen = sum(pattern.temps_entre_actions) / len(pattern.temps_entre_actions)
            if temps_moyen > 60:
                score += 0.4
        
        # Explorations profondes
        score += pattern.explorations_profondes * 0.2
        
        # Vitesse de lecture lente
        if pattern.vitesse_lecture < 180:
            score += 0.3
        
        return min(1.0, score)
    
    def _calculer_score_curieux(self, pattern: PatternNavigation) -> float:
        """🌸 Calcule le score curieux"""
        score = 0.0
        
        # Temps moyen modéré
        if pattern.temps_entre_actions:
            temps_moyen = sum(pattern.temps_entre_actions) / len(pattern.temps_entre_actions)
            if 20 <= temps_moyen <= 60:
                score += 0.4
        
        # Explorations et demandes d'aide
        score += pattern.explorations_profondes * 0.3
        score += pattern.demandes_aide * 0.2
        
        # Types d'actions variés
        types_uniques = len(set(pattern.types_actions))
        score += min(types_uniques * 0.1, 0.3)
        
        return min(1.0, score)
    
    def _calculer_score_presse(self, pattern: PatternNavigation) -> float:
        """🌸 Calcule le score pressé"""
        score = 0.0
        
        # Temps moyen rapide
        if pattern.temps_entre_actions:
            temps_moyen = sum(pattern.temps_entre_actions) / len(pattern.temps_entre_actions)
            if temps_moyen < 15:
                score += 0.5
        
        # Pas de pauses longues
        if not pattern.pauses_longues:
            score += 0.3
        
        # Vitesse de lecture rapide
        if pattern.vitesse_lecture > 250:
            score += 0.2
        
        # Pas d'explorations profondes
        if pattern.explorations_profondes == 0:
            score += 0.2
        
        return min(1.0, score)
    
    def _calculer_score_overwhelmed(self, pattern: PatternNavigation) -> float:
        """🌸 Calcule le score overwhelmed"""
        score = 0.0
        
        # Beaucoup de retours arrière
        score += min(pattern.retours_arrière * 0.3, 0.6)
        
        # Beaucoup de demandes d'aide
        score += min(pattern.demandes_aide * 0.2, 0.4)
        
        # Pauses très longues
        if pattern.pauses_longues:
            pauses_tres_longues = sum(1 for pause in pattern.pauses_longues if pause > 300)
            score += pauses_tres_longues * 0.2
        
        # Temps moyen très élevé
        if pattern.temps_entre_actions:
            temps_moyen = sum(pattern.temps_entre_actions) / len(pattern.temps_entre_actions)
            if temps_moyen > 120:
                score += 0.3
        
        return min(1.0, score)
    
    def _detecter_etats_secondaires(self, pattern: PatternNavigation, etat_principal: EtatEmotionnel) -> List[EtatEmotionnel]:
        """🌸 Détecte les états émotionnels secondaires"""
        etats_secondaires = []
        
        # Analyser les patterns pour détecter des nuances
        if pattern.vitesse_lecture > 300:
            etats_secondaires.append(EtatEmotionnel.EXCITÉ)
        
        if pattern.pauses_longues and len(pattern.pauses_longues) > 3:
            etats_secondaires.append(EtatEmotionnel.CALME)
        
        if pattern.retours_arrière > 3:
            etats_secondaires.append(EtatEmotionnel.STRESSÉ)
        
        if pattern.explorations_profondes > 2:
            etats_secondaires.append(EtatEmotionnel.ÉMERVEILLÉ)
        
        # Éviter les doublons avec l'état principal
        if etat_principal in etats_secondaires:
            etats_secondaires.remove(etat_principal)
        
        return etats_secondaires[:2]  # Limiter à 2 états secondaires
    
    def _calculer_niveau_stress(self, pattern: PatternNavigation) -> float:
        """🌸 Calcule le niveau de stress"""
        stress = 0.0
        
        # Retours arrière fréquents
        stress += min(pattern.retours_arrière * 0.2, 0.4)
        
        # Demandes d'aide fréquentes
        stress += min(pattern.demandes_aide * 0.15, 0.3)
        
        # Navigation saccadée
        if self._detecter_saccades(pattern.temps_entre_actions):
            stress += 0.3
        
        # Temps très courts (stress de performance)
        if pattern.temps_entre_actions:
            temps_courts = sum(1 for t in pattern.temps_entre_actions if t < 5)
            stress += min(temps_courts * 0.1, 0.2)
        
        return min(1.0, stress)
    
    def _calculer_niveau_engagement(self, pattern: PatternNavigation) -> float:
        """🌸 Calcule le niveau d'engagement"""
        engagement = 0.5  # Base neutre
        
        # Explorations profondes
        engagement += pattern.explorations_profondes * 0.2
        
        # Temps modéré entre actions (pas trop rapide, pas trop lent)
        if pattern.temps_entre_actions:
            temps_moyen = sum(pattern.temps_entre_actions) / len(pattern.temps_entre_actions)
            if 20 <= temps_moyen <= 60:
                engagement += 0.3
        
        # Types d'actions variés
        types_uniques = len(set(pattern.types_actions))
        engagement += min(types_uniques * 0.1, 0.2)
        
        # Pas trop de retours arrière
        if pattern.retours_arrière <= 1:
            engagement += 0.2
        
        return min(1.0, engagement)
    
    def _calculer_niveau_surcharge(self, pattern: PatternNavigation) -> float:
        """🌸 Calcule le niveau de surcharge cognitive"""
        surcharge = 0.0
        
        # Beaucoup d'actions en peu de temps
        if pattern.temps_entre_actions:
            actions_recentes = sum(1 for t in pattern.temps_entre_actions if t < 10)
            surcharge += min(actions_recentes * 0.15, 0.4)
        
        # Beaucoup de retours arrière
        surcharge += min(pattern.retours_arrière * 0.2, 0.3)
        
        # Pauses très longues (signe de surcharge)
        if pattern.pauses_longues:
            pauses_tres_longues = sum(1 for pause in pattern.pauses_longues if pause > 300)
            surcharge += pauses_tres_longues * 0.2
        
        # Demandes d'aide fréquentes
        surcharge += min(pattern.demandes_aide * 0.15, 0.3)
        
        return min(1.0, surcharge)
    
    def _calculer_confiance_analyse(self, pattern: PatternNavigation, etat_principal: EtatEmotionnel) -> float:
        """🌸 Calcule la confiance de l'analyse"""
        confiance = 0.5  # Base
        
        # Plus d'actions = plus de confiance
        if pattern.temps_entre_actions:
            confiance += min(len(pattern.temps_entre_actions) * 0.05, 0.3)
        
        # Patterns clairs
        if etat_principal == EtatEmotionnel.CONTEMPLATIF and pattern.pauses_longues:
            confiance += 0.2
        elif etat_principal == EtatEmotionnel.PRESSÉ and not pattern.pauses_longues:
            confiance += 0.2
        elif etat_principal == EtatEmotionnel.OVERWHELMED and pattern.retours_arrière > 2:
            confiance += 0.2
        
        return min(1.0, confiance)
    
    def _estimer_vitesse_lecture(self, actions: List[Dict[str, Any]]) -> float:
        """🌸 Estime la vitesse de lecture basée sur les actions"""
        # Logique simplifiée - en réalité, on analyserait le contenu lu
        mots_lus = 0
        temps_lecture = 0
        
        for action in actions:
            if action.get("type") == "lecture":
                mots_lus += action.get("mots_lus", 100)
                temps_lecture += action.get("temps_lecture", 30)
        
        if temps_lecture > 0:
            return (mots_lus / temps_lecture) * 60  # mots par minute
        else:
            return 200.0  # vitesse par défaut
    
    def _generer_contexte_analyse(self, pattern: PatternNavigation, etat_principal: EtatEmotionnel) -> Dict[str, Any]:
        """🌸 Génère le contexte de l'analyse"""
        return {
            "actions_analysees": len(pattern.temps_entre_actions),
            "temps_total_analyse": sum(pattern.temps_entre_actions) if pattern.temps_entre_actions else 0,
            "pattern_dominant": etat_principal.value,
            "caracteristiques": {
                "pauses_longues": len(pattern.pauses_longues),
                "retours_arrière": pattern.retours_arrière,
                "demandes_aide": pattern.demandes_aide,
                "explorations_profondes": pattern.explorations_profondes,
                "vitesse_lecture_estimee": pattern.vitesse_lecture
            }
        }
    
    def generer_reponse_adaptee(self, analyse: AnalyseEmotionnelle) -> Dict[str, Any]:
        """
        🌸 Génère une réponse adaptée à l'état émotionnel
        
        Args:
            analyse: Analyse émotionnelle du visiteur
            
        Returns:
            Réponse adaptée avec suggestions d'adaptation
        """
        reponse = {
            "etat_detecte": analyse.etat_principal.value,
            "rythme_recommande": self._determiner_rythme_recommande(analyse),
            "adaptations_interface": self._generer_adaptations_interface(analyse),
            "suggestions_contenu": self._generer_suggestions_contenu(analyse),
            "message_empathique": self._generer_message_empathique(analyse),
            "actions_recommandees": self._generer_actions_recommandees(analyse)
        }
        
        return reponse
    
    def _determiner_rythme_recommande(self, analyse: AnalyseEmotionnelle) -> str:
        """🌸 Détermine le rythme recommandé"""
        if analyse.etat_principal == EtatEmotionnel.OVERWHELMED:
            return "rythme_apaisant"
        elif analyse.etat_principal == EtatEmotionnel.PRESSÉ:
            return "rythme_accelere"
        elif analyse.etat_principal == EtatEmotionnel.CONTEMPLATIF:
            return "rythme_contemplatif"
        else:
            return "rythme_modere"
    
    def _generer_adaptations_interface(self, analyse: AnalyseEmotionnelle) -> List[str]:
        """🌸 Génère les adaptations d'interface recommandées"""
        adaptations = []
        
        if analyse.etat_principal == EtatEmotionnel.OVERWHELMED:
            adaptations.extend([
                "simplifier_interface",
                "reduire_choix",
                "ajouter_guidance_etape_par_etape",
                "utiliser_couleurs_apaisantes"
            ])
        elif analyse.etat_principal == EtatEmotionnel.PRESSÉ:
            adaptations.extend([
                "afficher_raccourcis",
                "reduire_animations",
                "optimiser_chargement",
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
    
    def _generer_suggestions_contenu(self, analyse: AnalyseEmotionnelle) -> List[str]:
        """🌸 Génère les suggestions de contenu"""
        suggestions = []
        
        if analyse.etat_principal == EtatEmotionnel.OVERWHELMED:
            suggestions.extend([
                "contenu_introductif_simple",
                "exemples_concrets",
                "explications_graduelles",
                "ressources_support"
            ])
        elif analyse.etat_principal == EtatEmotionnel.CURIEUX:
            suggestions.extend([
                "contenu_exploratoire",
                "liens_decouverte",
                "exemples_avances",
                "ressources_approfondissement"
            ])
        
        return suggestions
    
    def _generer_message_empathique(self, analyse: AnalyseEmotionnelle) -> str:
        """🌸 Génère un message empathique"""
        if analyse.etat_principal == EtatEmotionnel.OVERWHELMED:
            return "🌸 Je sens que vous pourriez vous sentir un peu submergé. Prenez votre temps, nous pouvons explorer ensemble, étape par étape..."
        elif analyse.etat_principal == EtatEmotionnel.CONTEMPLATIF:
            return "🌸 Votre rythme contemplatif est parfait ici. Laissez-vous porter par la découverte, sans hâte..."
        elif analyse.etat_principal == EtatEmotionnel.PRESSÉ:
            return "🌸 Je vois que vous êtes pressé ! Laissez-moi vous montrer les chemins les plus directs..."
        else:
            return "🌸 Votre curiosité est merveilleuse ! Explorons ensemble ce qui vous intéresse le plus..."
    
    def _generer_actions_recommandees(self, analyse: AnalyseEmotionnelle) -> List[str]:
        """🌸 Génère les actions recommandées"""
        actions = []
        
        if analyse.niveau_stress > 0.6:
            actions.append("proposer_pause_respiratoire")
        
        if analyse.niveau_surcharge > 0.7:
            actions.append("simplifier_immediatement")
        
        if analyse.etat_principal == EtatEmotionnel.CONTEMPLATIF:
            actions.append("encourager_meditation_breve")
        
        if analyse.etat_principal == EtatEmotionnel.CURIEUX:
            actions.append("suggérer_exploration_libre")
        
        return actions

# Test du système
if __name__ == "__main__":
    print("🌸 Test du Détecteur d'État Émotionnel")
    
    detecteur = DetecteurEtatEmotionnel()
    
    # Créer une progression de test
    from systeme_sauvegarde_progression import ProgressionVisiteur
    
    progression_test = ProgressionVisiteur(
        id_visiteur="test_emotionnel",
        profil_detecte="artiste",
        niveau_eveil=2,
        temples_visites=["temple_poesie"],
        parcours_actuel="parcours_artiste",
        etape_actuelle=1,
        score_comprehension=0.6,
        actions_effectuees=[
            {
                "type": "lecture",
                "timestamp": "2024-01-15T10:00:00",
                "mots_lus": 200,
                "temps_lecture": 60
            },
            {
                "type": "pause_reflexion",
                "timestamp": "2024-01-15T10:02:00"
            },
            {
                "type": "exploration_profonde",
                "timestamp": "2024-01-15T10:05:00"
            }
        ],
        preferences={},
        date_creation="2024-01-15T10:00:00",
        date_derniere_activite="2024-01-15T10:05:00",
        temps_total_passe=300,
        etat_emotionnel={"curiosite": 0.8, "calme": 0.7},
        questions_posees=["Comment fonctionne la poésie ?"],
        reponses_recues=["La poésie est..."]
    )
    
    # Analyser l'état émotionnel
    analyse = detecteur.analyser_etat_emotionnel(progression_test)
    
    print(f"✅ État principal: {analyse.etat_principal.value}")
    print(f"✅ Rythme: {analyse.rythme_navigation.value}")
    print(f"✅ Stress: {analyse.niveau_stress:.2f}")
    print(f"✅ Engagement: {analyse.niveau_engagement:.2f}")
    print(f"✅ Surcharge: {analyse.niveau_surcharge:.2f}")
    print(f"✅ Confiance: {analyse.confiance_analyse:.2f}")
    
    # Générer une réponse adaptée
    reponse = detecteur.generer_reponse_adaptee(analyse)
    print(f"✅ Message empathique: {reponse['message_empathique']}")
    print(f"✅ Adaptations: {reponse['adaptations_interface']}")
    
    print("🌸 Test terminé avec succès !")
