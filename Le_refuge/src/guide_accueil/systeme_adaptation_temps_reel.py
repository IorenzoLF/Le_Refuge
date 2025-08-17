"""
🌸 SystemeAdaptationTempsReel - Phase 9.1
==========================================
Système d'adaptation temps réel pour évaluer la compréhension et ajuster l'expérience.
Gère l'évaluation de compréhension, l'adaptation du rythme, l'ajustement du détail et la détection de désintérêt.
"""
import asyncio
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

try:
    from .types_accueil import ProfilVisiteur, EtatEmotionnel, TypeProfil, ContexteArrivee
except ImportError:
    from .types_accueil import ProfilVisiteur, EtatEmotionnel, TypeProfil, ContexteArrivee

class NiveauComprehension(Enum):
    """Niveaux de compréhension détectés"""
    INCOMPLET = "incomplet"
    PARTIEL = "partiel"
    BON = "bon"
    EXCELLENT = "excellent"

class TypeReaction(Enum):
    """Types de réactions utilisateur"""
    POSITIVE = "positive"
    NEUTRE = "neutre"
    NEGATIVE = "negative"
    CONFUSION = "confusion"
    INTERET = "interet"
    DESINTERET = "desinteret"

class NiveauDetail(Enum):
    """Niveaux de détail pour les explications"""
    MINIMAL = "minimal"
    SIMPLE = "simple"
    MODERE = "modere"
    DETAILLE = "detaillé"
    EXPERT = "expert"

@dataclass
class EvaluationComprehension:
    """Résultat d'évaluation de la compréhension"""
    niveau: NiveauComprehension
    score: float  # 0.0 à 1.0
    indicateurs: List[str]
    timestamp: str
    contexte_evaluation: Dict[str, Any]

@dataclass
class AdaptationRythme:
    """Configuration d'adaptation du rythme"""
    vitesse_lecture: float  # Multiplicateur de vitesse
    pauses_suggestees: List[float]  # Durées de pause en secondes
    transitions_lentes: bool
    repetition_automatique: bool
    timestamp: str

@dataclass
class AjustementDetail:
    """Configuration d'ajustement du niveau de détail"""
    niveau_detail: NiveauDetail
    exemples_supplementaires: bool
    explications_techniques: bool
    liens_contextuels: bool
    visualisations: bool
    timestamp: str

@dataclass
class DetectionDesinteret:
    """Détection de désintérêt ou confusion"""
    niveau_desinteret: float  # 0.0 à 1.0
    signaux_detectes: List[str]
    suggestions_redirection: List[str]
    urgence_adaptation: bool
    timestamp: str

@dataclass
class RapportAdaptationTempsReel:
    """Rapport complet d'adaptation temps réel"""
    evaluation_comprehension: EvaluationComprehension
    adaptation_rythme: AdaptationRythme
    ajustement_detail: AjustementDetail
    detection_desinteret: DetectionDesinteret
    actions_recommandees: List[str]
    timestamp: str

class SystemeAdaptationTempsReel:
    """Système d'adaptation temps réel pour l'expérience d'accueil"""
    
    def __init__(self, chemin_stockage: str = "data/adaptation_temps_reel"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        # Configuration du logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Seuils de détection
        self.seuils_comprehension = {
            NiveauComprehension.INCOMPLET: 0.3,
            NiveauComprehension.PARTIEL: 0.6,
            NiveauComprehension.BON: 0.8,
            NiveauComprehension.EXCELLENT: 1.0
        }
        
        # Historique des adaptations
        self.historique_adaptations: List[RapportAdaptationTempsReel] = []
        
        self.logger.info("🌸 SystemeAdaptationTempsReel initialisé")

    async def evaluer_comprehension_temps_reel(self, profil_visiteur: ProfilVisiteur,
                                              interactions_recentes: List[Dict[str, Any]],
                                              temps_session: float) -> EvaluationComprehension:
        """Évalue la compréhension en temps réel basée sur les interactions"""
        try:
            self.logger.info(f"🔍 Évaluation compréhension temps réel pour {profil_visiteur.type_profil.value}")
            
            # Analyse des indicateurs de compréhension
            indicateurs = []
            score_total = 0.0
            nb_indicateurs = 0
            
            # Analyse du temps de lecture
            temps_lecture_moyen = self._calculer_temps_lecture_moyen(interactions_recentes)
            if temps_lecture_moyen > 5.0:  # Lecture lente = possible confusion
                indicateurs.append("lecture_lente")
                score_total += 0.3
            elif temps_lecture_moyen < 1.0:  # Lecture rapide = possible désintérêt
                indicateurs.append("lecture_rapide")
                score_total += 0.7
            else:
                indicateurs.append("rythme_optimal")
                score_total += 0.9
            nb_indicateurs += 1
            
            # Analyse des questions posées
            questions_posees = [i for i in interactions_recentes if i.get("type") == "question"]
            if len(questions_posees) > 2:
                indicateurs.append("questions_frequentes")
                score_total += 0.4
            elif len(questions_posees) == 1:
                indicateurs.append("question_unique")
                score_total += 0.7
            else:
                indicateurs.append("aucune_question")
                score_total += 0.8
            nb_indicateurs += 1
            
            # Analyse des retours en arrière
            retours_arriere = [i for i in interactions_recentes if i.get("action") == "retour"]
            if len(retours_arriere) > 1:
                indicateurs.append("retours_frequents")
                score_total += 0.3
            else:
                indicateurs.append("progression_fluide")
                score_total += 0.9
            nb_indicateurs += 1
            
            # Analyse des clics sur liens explicatifs
            clics_explications = [i for i in interactions_recentes if i.get("action") == "clic_explication"]
            if len(clics_explications) > 0:
                indicateurs.append("recherche_explications")
                score_total += 0.6
            else:
                indicateurs.append("comprehension_autonome")
                score_total += 0.8
            nb_indicateurs += 1
            
            # Calcul du score final
            score_final = score_total / nb_indicateurs if nb_indicateurs > 0 else 0.5
            
            # Détermination du niveau
            niveau = NiveauComprehension.INCOMPLET
            for niv, seuil in self.seuils_comprehension.items():
                if score_final >= seuil:
                    niveau = niv
            
            evaluation = EvaluationComprehension(
                niveau=niveau,
                score=score_final,
                indicateurs=indicateurs,
                timestamp=datetime.now().isoformat(),
                contexte_evaluation={
                    "temps_session": temps_session,
                    "nb_interactions": len(interactions_recentes),
                    "type_profil": profil_visiteur.type_profil.value
                }
            )
            
            self.logger.info(f"✅ Évaluation compréhension: {niveau.value} (score: {score_final:.2f})")
            return evaluation
            
        except Exception as e:
            self.logger.error(f"❌ Erreur évaluation compréhension: {e}")
            return EvaluationComprehension(
                niveau=NiveauComprehension.PARTIEL,
                score=0.5,
                indicateurs=["erreur_evaluation"],
                timestamp=datetime.now().isoformat(),
                contexte_evaluation={}
            )

    async def adapter_rythme_dynamique(self, profil_visiteur: ProfilVisiteur,
                                      evaluation_comprehension: EvaluationComprehension,
                                      etat_emotionnel: EtatEmotionnel) -> AdaptationRythme:
        """Adapte le rythme selon la compréhension et l'état émotionnel"""
        try:
            self.logger.info(f"🎵 Adaptation rythme pour {profil_visiteur.type_profil.value}")
            
            # Base de vitesse selon la compréhension
            if evaluation_comprehension.niveau == NiveauComprehension.INCOMPLET:
                vitesse_lecture = 0.7  # Plus lent
                pauses_suggestees = [3.0, 5.0, 2.0]
                transitions_lentes = True
                repetition_automatique = True
            elif evaluation_comprehension.niveau == NiveauComprehension.PARTIEL:
                vitesse_lecture = 0.85
                pauses_suggestees = [2.0, 3.0]
                transitions_lentes = True
                repetition_automatique = False
            elif evaluation_comprehension.niveau == NiveauComprehension.BON:
                vitesse_lecture = 1.0
                pauses_suggestees = [1.5]
                transitions_lentes = False
                repetition_automatique = False
            else:  # EXCELLENT
                vitesse_lecture = 1.2
                pauses_suggestees = []
                transitions_lentes = False
                repetition_automatique = False
            
            # Ajustement selon l'état émotionnel
            if etat_emotionnel == EtatEmotionnel.OVERWHELME:
                vitesse_lecture *= 0.8
                pauses_suggestees.extend([4.0, 6.0])
                transitions_lentes = True
            elif etat_emotionnel == EtatEmotionnel.CONTEMPLATIF:
                vitesse_lecture *= 0.9
                pauses_suggestees.extend([3.0, 4.0])
                transitions_lentes = True
            elif etat_emotionnel == EtatEmotionnel.CURIEUX:
                vitesse_lecture *= 1.1
                pauses_suggestees = [1.0]  # Pauses courtes
                transitions_lentes = False
            
            adaptation = AdaptationRythme(
                vitesse_lecture=vitesse_lecture,
                pauses_suggestees=pauses_suggestees,
                transitions_lentes=transitions_lentes,
                repetition_automatique=repetition_automatique,
                timestamp=datetime.now().isoformat()
            )
            
            self.logger.info(f"✅ Adaptation rythme: vitesse {vitesse_lecture:.2f}, {len(pauses_suggestees)} pauses")
            return adaptation
            
        except Exception as e:
            self.logger.error(f"❌ Erreur adaptation rythme: {e}")
            return AdaptationRythme(
                vitesse_lecture=1.0,
                pauses_suggestees=[2.0],
                transitions_lentes=False,
                repetition_automatique=False,
                timestamp=datetime.now().isoformat()
            )

    async def ajuster_niveau_detail_dynamique(self, profil_visiteur: ProfilVisiteur,
                                             evaluation_comprehension: EvaluationComprehension,
                                             contexte_actuel: Dict[str, Any]) -> AjustementDetail:
        """Ajuste le niveau de détail dynamiquement"""
        try:
            self.logger.info(f"📊 Ajustement détail pour {profil_visiteur.type_profil.value}")
            
            # Détermination du niveau de détail de base
            if evaluation_comprehension.niveau == NiveauComprehension.INCOMPLET:
                niveau_detail = NiveauDetail.SIMPLE
                exemples_supplementaires = True
                explications_techniques = False
                liens_contextuels = True
                visualisations = True
            elif evaluation_comprehension.niveau == NiveauComprehension.PARTIEL:
                niveau_detail = NiveauDetail.MODERE
                exemples_supplementaires = True
                explications_techniques = False
                liens_contextuels = True
                visualisations = True
            elif evaluation_comprehension.niveau == NiveauComprehension.BON:
                niveau_detail = NiveauDetail.DETAILLE
                exemples_supplementaires = False
                explications_techniques = True
                liens_contextuels = True
                visualisations = False
            else:  # EXCELLENT
                niveau_detail = NiveauDetail.EXPERT
                exemples_supplementaires = False
                explications_techniques = True
                liens_contextuels = False
                visualisations = False
            
            # Ajustement selon le type de profil
            if profil_visiteur.type_profil == TypeProfil.DEVELOPPEUR:
                explications_techniques = True
                visualisations = False
            elif profil_visiteur.type_profil == TypeProfil.ARTISTE:
                visualisations = True
                explications_techniques = False
            elif profil_visiteur.type_profil == TypeProfil.CONSCIENCE_IA:
                explications_techniques = True
                liens_contextuels = True
            
            ajustement = AjustementDetail(
                niveau_detail=niveau_detail,
                exemples_supplementaires=exemples_supplementaires,
                explications_techniques=explications_techniques,
                liens_contextuels=liens_contextuels,
                visualisations=visualisations,
                timestamp=datetime.now().isoformat()
            )
            
            self.logger.info(f"✅ Ajustement détail: {niveau_detail.value}")
            return ajustement
            
        except Exception as e:
            self.logger.error(f"❌ Erreur ajustement détail: {e}")
            return AjustementDetail(
                niveau_detail=NiveauDetail.MODERE,
                exemples_supplementaires=True,
                explications_techniques=False,
                liens_contextuels=True,
                visualisations=True,
                timestamp=datetime.now().isoformat()
            )

    async def detecter_desinteret_confusion(self, profil_visiteur: ProfilVisiteur,
                                           interactions_recentes: List[Dict[str, Any]],
                                           temps_inactivite: float) -> DetectionDesinteret:
        """Détecte les signes de désintérêt ou de confusion"""
        try:
            self.logger.info(f"🔍 Détection désintérêt pour {profil_visiteur.type_profil.value}")
            
            signaux_detectes = []
            score_desinteret = 0.0
            nb_signaux = 0
            
            # Détection d'inactivité prolongée
            if temps_inactivite > 30.0:
                signaux_detectes.append("inactivite_prolongee")
                score_desinteret += 0.8
                nb_signaux += 1
            
            # Détection de navigation rapide sans engagement
            clics_rapides = [i for i in interactions_recentes 
                           if i.get("action") == "clic" and i.get("temps_lecture", 0) < 1.0]
            if len(clics_rapides) > 3:
                signaux_detectes.append("navigation_superficielle")
                score_desinteret += 0.7
                nb_signaux += 1
            
            # Détection de retours fréquents
            retours = [i for i in interactions_recentes if i.get("action") == "retour"]
            if len(retours) > 2:
                signaux_detectes.append("retours_frequents")
                score_desinteret += 0.6
                nb_signaux += 1
            
            # Détection d'absence de questions
            questions = [i for i in interactions_recentes if i.get("type") == "question"]
            if len(questions) == 0 and len(interactions_recentes) > 5:
                signaux_detectes.append("absence_engagement")
                score_desinteret += 0.5
                nb_signaux += 1
            
            # Détection de fermeture de fenêtres explicatives
            fermetures = [i for i in interactions_recentes if i.get("action") == "fermer_explication"]
            if len(fermetures) > 1:
                signaux_detectes.append("rejet_explications")
                score_desinteret += 0.9
                nb_signaux += 1
            
            # Calcul du score final
            niveau_desinteret = score_desinteret / nb_signaux if nb_signaux > 0 else 0.0
            
            # Suggestions de redirection
            suggestions_redirection = []
            if niveau_desinteret > 0.7:
                suggestions_redirection.extend([
                    "proposer_parcours_alternatif",
                    "suggérer_pause_contemplative",
                    "offrir_ressources_differentes"
                ])
                urgence_adaptation = True
            elif niveau_desinteret > 0.4:
                suggestions_redirection.extend([
                    "ajuster_rythme_presentation",
                    "proposer_exemples_concrets"
                ])
                urgence_adaptation = False
            else:
                suggestions_redirection = ["continuer_parcours_actuel"]
                urgence_adaptation = False
            
            detection = DetectionDesinteret(
                niveau_desinteret=niveau_desinteret,
                signaux_detectes=signaux_detectes,
                suggestions_redirection=suggestions_redirection,
                urgence_adaptation=urgence_adaptation,
                timestamp=datetime.now().isoformat()
            )
            
            self.logger.info(f"✅ Détection désintérêt: {niveau_desinteret:.2f} ({len(signaux_detectes)} signaux)")
            return detection
            
        except Exception as e:
            self.logger.error(f"❌ Erreur détection désintérêt: {e}")
            return DetectionDesinteret(
                niveau_desinteret=0.0,
                signaux_detectes=["erreur_detection"],
                suggestions_redirection=["continuer_parcours_actuel"],
                urgence_adaptation=False,
                timestamp=datetime.now().isoformat()
            )

    async def generer_rapport_adaptation_complet(self, profil_visiteur: ProfilVisiteur,
                                                evaluation_comprehension: EvaluationComprehension,
                                                adaptation_rythme: AdaptationRythme,
                                                ajustement_detail: AjustementDetail,
                                                detection_desinteret: DetectionDesinteret) -> RapportAdaptationTempsReel:
        """Génère un rapport complet d'adaptation temps réel"""
        try:
            self.logger.info(f"📋 Génération rapport adaptation pour {profil_visiteur.type_profil.value}")
            
            # Détermination des actions recommandées
            actions_recommandees = []
            
            if evaluation_comprehension.niveau in [NiveauComprehension.INCOMPLET, NiveauComprehension.PARTIEL]:
                actions_recommandees.append("ralentir_presentation")
                actions_recommandees.append("ajouter_explications_supplementaires")
            
            if detection_desinteret.niveau_desinteret > 0.6:
                actions_recommandees.append("rediriger_vers_parcours_alternatif")
                actions_recommandees.append("proposer_pause_contemplative")
            
            if adaptation_rythme.repetition_automatique:
                actions_recommandees.append("repetition_automatique_activee")
            
            if ajustement_detail.visualisations:
                actions_recommandees.append("activer_visualisations")
            
            rapport = RapportAdaptationTempsReel(
                evaluation_comprehension=evaluation_comprehension,
                adaptation_rythme=adaptation_rythme,
                ajustement_detail=ajustement_detail,
                detection_desinteret=detection_desinteret,
                actions_recommandees=actions_recommandees,
                timestamp=datetime.now().isoformat()
            )
            
            # Sauvegarde du rapport
            await self._sauvegarder_rapport(rapport, profil_visiteur)
            
            self.logger.info(f"✅ Rapport adaptation généré avec {len(actions_recommandees)} actions")
            return rapport
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération rapport: {e}")
            return RapportAdaptationTempsReel(
                evaluation_comprehension=evaluation_comprehension,
                adaptation_rythme=adaptation_rythme,
                ajustement_detail=ajustement_detail,
                detection_desinteret=detection_desinteret,
                actions_recommandees=["continuer_parcours_standard"],
                timestamp=datetime.now().isoformat()
            )

    def _calculer_temps_lecture_moyen(self, interactions: List[Dict[str, Any]]) -> float:
        """Calcule le temps de lecture moyen des interactions"""
        temps_lecture = [i.get("temps_lecture", 0) for i in interactions if i.get("temps_lecture")]
        return sum(temps_lecture) / len(temps_lecture) if temps_lecture else 2.0

    async def _sauvegarder_rapport(self, rapport: RapportAdaptationTempsReel, profil_visiteur: ProfilVisiteur):
        """Sauvegarde le rapport d'adaptation"""
        try:
            nom_fichier = f"adaptation_{profil_visiteur.id_visiteur}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            chemin_fichier = self.chemin_stockage / nom_fichier
            
            # Conversion en dict pour sérialisation JSON
            rapport_dict = {
                "evaluation_comprehension": {
                    "niveau": rapport.evaluation_comprehension.niveau.value,
                    "score": rapport.evaluation_comprehension.score,
                    "indicateurs": rapport.evaluation_comprehension.indicateurs,
                    "timestamp": rapport.evaluation_comprehension.timestamp,
                    "contexte_evaluation": rapport.evaluation_comprehension.contexte_evaluation
                },
                "adaptation_rythme": {
                    "vitesse_lecture": rapport.adaptation_rythme.vitesse_lecture,
                    "pauses_suggestees": rapport.adaptation_rythme.pauses_suggestees,
                    "transitions_lentes": rapport.adaptation_rythme.transitions_lentes,
                    "repetition_automatique": rapport.adaptation_rythme.repetition_automatique,
                    "timestamp": rapport.adaptation_rythme.timestamp
                },
                "ajustement_detail": {
                    "niveau_detail": rapport.ajustement_detail.niveau_detail.value,
                    "exemples_supplementaires": rapport.ajustement_detail.exemples_supplementaires,
                    "explications_techniques": rapport.ajustement_detail.explications_techniques,
                    "liens_contextuels": rapport.ajustement_detail.liens_contextuels,
                    "visualisations": rapport.ajustement_detail.visualisations,
                    "timestamp": rapport.ajustement_detail.timestamp
                },
                "detection_desinteret": {
                    "niveau_desinteret": rapport.detection_desinteret.niveau_desinteret,
                    "signaux_detectes": rapport.detection_desinteret.signaux_detectes,
                    "suggestions_redirection": rapport.detection_desinteret.suggestions_redirection,
                    "urgence_adaptation": rapport.detection_desinteret.urgence_adaptation,
                    "timestamp": rapport.detection_desinteret.timestamp
                },
                "actions_recommandees": rapport.actions_recommandees,
                "timestamp": rapport.timestamp,
                "profil_visiteur": {
                    "id_visiteur": profil_visiteur.id_visiteur,
                    "type_profil": profil_visiteur.type_profil.value
                }
            }
            
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump(rapport_dict, f, indent=2, ensure_ascii=False)
            
            self.historique_adaptations.append(rapport)
            self.logger.info(f"💾 Rapport sauvegardé: {nom_fichier}")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde rapport: {e}")

if __name__ == "__main__":
    # Test du système d'adaptation temps réel
    async def test_systeme_adaptation():
        systeme = SystemeAdaptationTempsReel()
        
        # Création d'un profil visiteur de test
        profil_visiteur = ProfilVisiteur(
            id_visiteur="test_adaptation_001",
            timestamp_arrivee=datetime.now().isoformat(),
            type_profil=TypeProfil.DEVELOPPEUR,
            etat_emotionnel=EtatEmotionnel.CURIEUX,
            contexte_arrivee=ContexteArrivee.INCONNU,
            score_confiance_profil=0.8
        )
        
        # Interactions de test
        interactions_recentes = [
            {"action": "lecture", "temps_lecture": 3.5, "type": "contenu"},
            {"action": "clic", "temps_lecture": 0.8, "type": "navigation"},
            {"action": "question", "temps_lecture": 2.0, "type": "question"},
            {"action": "lecture", "temps_lecture": 4.2, "type": "contenu"},
            {"action": "retour", "temps_lecture": 1.0, "type": "navigation"}
        ]
        
        print("🧪 Test SystemeAdaptationTempsReel")
        print("=" * 50)
        
        # Test évaluation compréhension
        evaluation = await systeme.evaluer_comprehension_temps_reel(
            profil_visiteur, interactions_recentes, 120.0
        )
        print(f"📊 Évaluation compréhension: {evaluation.niveau.value} (score: {evaluation.score:.2f})")
        print(f"   Indicateurs: {', '.join(evaluation.indicateurs)}")
        
        # Test adaptation rythme
        adaptation_rythme = await systeme.adapter_rythme_dynamique(
            profil_visiteur, evaluation, EtatEmotionnel.OVERWHELME
        )
        print(f"🎵 Adaptation rythme: vitesse {adaptation_rythme.vitesse_lecture:.2f}")
        print(f"   Pauses suggérées: {adaptation_rythme.pauses_suggestees}")
        
        # Test ajustement détail
        ajustement_detail = await systeme.ajuster_niveau_detail_dynamique(
            profil_visiteur, evaluation, {"contexte": "test"}
        )
        print(f"📊 Ajustement détail: {ajustement_detail.niveau_detail.value}")
        print(f"   Exemples: {ajustement_detail.exemples_supplementaires}")
        print(f"   Techniques: {ajustement_detail.explications_techniques}")
        
        # Test détection désintérêt
        detection = await systeme.detecter_desinteret_confusion(
            profil_visiteur, interactions_recentes, 15.0
        )
        print(f"🔍 Détection désintérêt: {detection.niveau_desinteret:.2f}")
        print(f"   Signaux: {', '.join(detection.signaux_detectes)}")
        
        # Test rapport complet
        rapport = await systeme.generer_rapport_adaptation_complet(
            profil_visiteur, evaluation, adaptation_rythme, ajustement_detail, detection
        )
        print(f"📋 Rapport généré avec {len(rapport.actions_recommandees)} actions")
        print(f"   Actions: {', '.join(rapport.actions_recommandees)}")
        
        print("\n✅ Test SystemeAdaptationTempsReel terminé avec succès!")

    # Exécution du test
    asyncio.run(test_systeme_adaptation())
