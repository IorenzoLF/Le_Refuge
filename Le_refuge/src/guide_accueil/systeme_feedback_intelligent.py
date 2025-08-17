"""
🌸 SystemeFeedbackIntelligent - Phase 8.1
==========================================

Système de feedback intelligent pour collecter et analyser les retours des visiteurs.
Gère la collecte multi-canal, l'analyse émotionnelle et la génération d'insights.
"""
import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

try:
    from .types_accueil import ProfilVisiteur, TypeFeedback, TypeProfil, EtatEmotionnel, ContexteArrivee
except ImportError:
    from .types_accueil import ProfilVisiteur, TypeFeedback, TypeProfil, EtatEmotionnel, ContexteArrivee

class NiveauSatisfaction(Enum):
    """🌸 Niveaux de satisfaction"""
    EXCELLENT = "excellent"
    TRES_BON = "tres_bon"
    BON = "bon"
    MOYEN = "moyen"
    INSUFFISANT = "insuffisant"

class TypeFeedbackAvance(Enum):
    """🌸 Types de feedback avancés"""
    EMOTIONNEL = "emotionnel"
    TECHNIQUE = "technique"
    SPIRITUEL = "spirituel"
    UX_UI = "ux_ui"
    PERFORMANCE = "performance"
    CONTENU = "contenu"

@dataclass
class FeedbackCollecte:
    """🌸 Données de feedback collectées"""
    id_feedback: str
    profil_visiteur: ProfilVisiteur
    type_feedback: TypeFeedbackAvance
    contenu: str
    score_satisfaction: NiveauSatisfaction
    contexte_session: Dict[str, Any]
    timestamp_collecte: str
    metadonnees: Dict[str, Any] = field(default_factory=dict)

@dataclass
class AnalyseEmotionnelle:
    """🌸 Résultats d'analyse émotionnelle"""
    sentiment_principal: str
    intensite_emotionnelle: float  # 0.0 à 1.0
    emotions_detectees: List[str]
    confiance_analyse: float
    mots_cles_emotionnels: List[str]

@dataclass
class InsightFeedback:
    """🌸 Insight généré à partir du feedback"""
    id_insight: str
    type_insight: str  # "amelioration", "probleme", "suggestion", "tendance"
    description: str
    priorite: int  # 1-5 (5 = très prioritaire)
    impact_potentiel: float  # 0.0 à 1.0
    actions_suggerees: List[str]
    feedbacks_associes: List[str]

@dataclass
class RapportFeedback:
    """🌸 Rapport d'analyse de feedback"""
    periode_analyse: str
    total_feedbacks: int
    satisfaction_moyenne: float
    insights_generes: List[InsightFeedback]
    tendances_identifiees: List[str]
    recommandations: List[str]

class SystemeFeedbackIntelligent:
    """
    🌸 Système de feedback intelligent
    
    Collecte, analyse et génère des insights à partir des retours des visiteurs.
    """
    
    def __init__(self, chemin_stockage: str = "data/feedback"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        self.logger = logging.getLogger(__name__)
        self.feedbacks_collectes: List[FeedbackCollecte] = []
        self.insights_generes: List[InsightFeedback] = []
        
        # Initialiser les canaux de collecte
        self.canaux_collecte = {
            "interface_parcours": True,
            "questionnaires": True,
            "feedback_emotionnel": True,
            "analytics_comportement": True
        }
        
        self.logger.info("🌸 Système de Feedback Intelligent initialisé")
    
    async def collecter_feedback_multi_canal(self, profil_visiteur: ProfilVisiteur, 
                                           contenu: str, type_feedback: TypeFeedbackAvance,
                                           score_satisfaction: NiveauSatisfaction,
                                           contexte_session: Dict[str, Any]) -> FeedbackCollecte:
        """🌸 Collecte feedback depuis plusieurs canaux"""
        try:
            feedback = FeedbackCollecte(
                id_feedback=f"fb_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{profil_visiteur.id_visiteur}",
                profil_visiteur=profil_visiteur,
                type_feedback=type_feedback,
                contenu=contenu,
                score_satisfaction=score_satisfaction,
                contexte_session=contexte_session,
                timestamp_collecte=datetime.now().isoformat()
            )
            
            # Ajouter des métadonnées selon le type de feedback
            if type_feedback == TypeFeedbackAvance.EMOTIONNEL:
                feedback.metadonnees["intensite_emotionnelle"] = self._estimer_intensite_emotionnelle(contenu)
            elif type_feedback == TypeFeedbackAvance.TECHNIQUE:
                feedback.metadonnees["complexite_technique"] = self._estimer_complexite_technique(contenu)
            
            self.feedbacks_collectes.append(feedback)
            await self._sauvegarder_feedback(feedback)
            
            self.logger.info(f"✅ Feedback collecté: {feedback.id_feedback} ({type_feedback.value})")
            return feedback
            
        except Exception as e:
            self.logger.error(f"❌ Erreur collecte feedback: {e}")
            raise
    
    async def analyser_emotionnellement(self, feedback: FeedbackCollecte) -> AnalyseEmotionnelle:
        """🌸 Analyse émotionnelle du feedback"""
        try:
            # Analyse basique du sentiment
            mots_positifs = ["merveilleux", "magnifique", "excellent", "génial", "parfait", "adorable"]
            mots_negatifs = ["mauvais", "terrible", "horrible", "nul", "décevant", "frustrant"]
            
            contenu_lower = feedback.contenu.lower()
            score_positif = sum(1 for mot in mots_positifs if mot in contenu_lower)
            score_negatif = sum(1 for mot in mots_negatifs if mot in contenu_lower)
            
            if score_positif > score_negatif:
                sentiment_principal = "positif"
                intensite = min(0.8, score_positif * 0.2)
            elif score_negatif > score_positif:
                sentiment_principal = "negatif"
                intensite = min(0.8, score_negatif * 0.2)
            else:
                sentiment_principal = "neutre"
                intensite = 0.3
            
            # Détecter les émotions spécifiques
            emotions_detectees = []
            if "joie" in contenu_lower or "heureux" in contenu_lower:
                emotions_detectees.append("joie")
            if "tristesse" in contenu_lower or "triste" in contenu_lower:
                emotions_detectees.append("tristesse")
            if "colère" in contenu_lower or "fâché" in contenu_lower:
                emotions_detectees.append("colere")
            if "surprise" in contenu_lower or "étonné" in contenu_lower:
                emotions_detectees.append("surprise")
            
            analyse = AnalyseEmotionnelle(
                sentiment_principal=sentiment_principal,
                intensite_emotionnelle=intensite,
                emotions_detectees=emotions_detectees,
                confiance_analyse=0.7,  # Simulation
                mots_cles_emotionnels=[mot for mot in mots_positifs + mots_negatifs if mot in contenu_lower]
            )
            
            self.logger.info(f"✅ Analyse émotionnelle: {sentiment_principal} (intensité: {intensite:.2f})")
            return analyse
            
        except Exception as e:
            self.logger.error(f"❌ Erreur analyse émotionnelle: {e}")
            raise
    
    async def generer_insights_intelligents(self, feedbacks: List[FeedbackCollecte]) -> List[InsightFeedback]:
        """🌸 Génère des insights intelligents à partir des feedbacks"""
        try:
            insights = []
            
            # Analyser les tendances par type de feedback
            feedbacks_emotionnels = [f for f in feedbacks if f.type_feedback == TypeFeedbackAvance.EMOTIONNEL]
            feedbacks_techniques = [f for f in feedbacks if f.type_feedback == TypeFeedbackAvance.TECHNIQUE]
            
            # Insight sur l'expérience émotionnelle
            if feedbacks_emotionnels:
                satisfaction_moyenne = sum(1 for f in feedbacks_emotionnels 
                                         if f.score_satisfaction in [NiveauSatisfaction.EXCELLENT, NiveauSatisfaction.TRES_BON]) / len(feedbacks_emotionnels)
                
                if satisfaction_moyenne < 0.7:
                    insight = InsightFeedback(
                        id_insight=f"insight_emotionnel_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                        type_insight="amelioration",
                        description="Expérience émotionnelle à améliorer - satisfaction moyenne faible",
                        priorite=4,
                        impact_potentiel=0.8,
                        actions_suggerees=[
                            "Renforcer les éléments d'émerveillement",
                            "Améliorer la personnalisation émotionnelle",
                            "Ajouter plus d'interactions magiques"
                        ],
                        feedbacks_associes=[f.id_feedback for f in feedbacks_emotionnels]
                    )
                    insights.append(insight)
            
            # Insight sur les aspects techniques
            if feedbacks_techniques:
                problemes_techniques = [f for f in feedbacks_techniques 
                                      if f.score_satisfaction in [NiveauSatisfaction.INSUFFISANT, NiveauSatisfaction.MOYEN]]
                
                if problemes_techniques:
                    insight = InsightFeedback(
                        id_insight=f"insight_technique_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                        type_insight="probleme",
                        description=f"Problèmes techniques identifiés ({len(problemes_techniques)} signalements)",
                        priorite=5,
                        impact_potentiel=0.9,
                        actions_suggerees=[
                            "Audit complet des performances",
                            "Optimisation des temps de réponse",
                            "Amélioration de la stabilité"
                        ],
                        feedbacks_associes=[f.id_feedback for f in problemes_techniques]
                    )
                    insights.append(insight)
            
            # Insight sur les tendances générales
            if len(feedbacks) >= 5:
                tendance_satisfaction = self._analyser_tendance_satisfaction(feedbacks)
                if tendance_satisfaction:
                    insight = InsightFeedback(
                        id_insight=f"insight_tendance_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                        type_insight="tendance",
                        description=f"Tendance identifiée: {tendance_satisfaction}",
                        priorite=3,
                        impact_potentiel=0.6,
                        actions_suggerees=[
                            "Surveiller l'évolution de cette tendance",
                            "Analyser les causes sous-jacentes",
                            "Ajuster les stratégies en conséquence"
                        ],
                        feedbacks_associes=[f.id_feedback for f in feedbacks[-5:]]  # 5 derniers
                    )
                    insights.append(insight)
            
            self.insights_generes.extend(insights)
            self.logger.info(f"✅ {len(insights)} insights générés")
            return insights
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération insights: {e}")
            raise
    
    async def generer_rapport_feedback(self, periode: str = "7j") -> RapportFeedback:
        """🌸 Génère un rapport complet d'analyse de feedback"""
        try:
            # Filtrer les feedbacks de la période
            date_limite = datetime.now()
            if periode == "7j":
                from datetime import timedelta
                date_limite = datetime.now() - timedelta(days=7)
            
            feedbacks_periode = [f for f in self.feedbacks_collectes 
                               if datetime.fromisoformat(f.timestamp_collecte) >= date_limite]
            
            # Calculer les métriques
            satisfaction_moyenne = self._calculer_satisfaction_moyenne(feedbacks_periode)
            insights = await self.generer_insights_intelligents(feedbacks_periode)
            tendances = self._identifier_tendances(feedbacks_periode)
            recommandations = self._generer_recommandations(insights, tendances)
            
            rapport = RapportFeedback(
                periode_analyse=periode,
                total_feedbacks=len(feedbacks_periode),
                satisfaction_moyenne=satisfaction_moyenne,
                insights_generes=insights,
                tendances_identifiees=tendances,
                recommandations=recommandations
            )
            
            await self._sauvegarder_rapport(rapport)
            self.logger.info(f"✅ Rapport feedback généré: {len(feedbacks_periode)} feedbacks analysés")
            return rapport
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération rapport: {e}")
            raise
    
    def _estimer_intensite_emotionnelle(self, contenu: str) -> float:
        """🌸 Estime l'intensité émotionnelle du contenu"""
        mots_intenses = ["incroyable", "fantastique", "merveilleux", "terrible", "horrible", "magnifique"]
        return min(1.0, sum(1 for mot in mots_intenses if mot in contenu.lower()) * 0.3)
    
    def _estimer_complexite_technique(self, contenu: str) -> float:
        """🌸 Estime la complexité technique mentionnée"""
        mots_techniques = ["bug", "erreur", "lent", "problème", "difficile", "complexe"]
        return min(1.0, sum(1 for mot in mots_techniques if mot in contenu.lower()) * 0.2)
    
    def _analyser_tendance_satisfaction(self, feedbacks: List[FeedbackCollecte]) -> Optional[str]:
        """🌸 Analyse la tendance de satisfaction"""
        if len(feedbacks) < 3:
            return None
        
        # Trier par timestamp et analyser les 3 derniers
        feedbacks_recents = sorted(feedbacks, key=lambda f: f.timestamp_collecte)[-3:]
        
        scores = [1 if f.score_satisfaction in [NiveauSatisfaction.EXCELLENT, NiveauSatisfaction.TRES_BON] else 0 
                 for f in feedbacks_recents]
        
        if scores == [1, 1, 1]:
            return "Amélioration continue de la satisfaction"
        elif scores == [0, 0, 0]:
            return "Dégradation de la satisfaction"
        elif scores[-1] == 1:
            return "Récupération de la satisfaction"
        else:
            return "Stabilité de la satisfaction"
    
    def _calculer_satisfaction_moyenne(self, feedbacks: List[FeedbackCollecte]) -> float:
        """🌸 Calcule la satisfaction moyenne"""
        if not feedbacks:
            return 0.0
        
        scores = []
        for feedback in feedbacks:
            if feedback.score_satisfaction == NiveauSatisfaction.EXCELLENT:
                scores.append(5.0)
            elif feedback.score_satisfaction == NiveauSatisfaction.TRES_BON:
                scores.append(4.0)
            elif feedback.score_satisfaction == NiveauSatisfaction.BON:
                scores.append(3.0)
            elif feedback.score_satisfaction == NiveauSatisfaction.MOYEN:
                scores.append(2.0)
            else:
                scores.append(1.0)
        
        return sum(scores) / len(scores)
    
    def _identifier_tendances(self, feedbacks: List[FeedbackCollecte]) -> List[str]:
        """🌸 Identifie les tendances dans les feedbacks"""
        tendances = []
        
        # Tendance par type de feedback
        types_count = {}
        for feedback in feedbacks:
            types_count[feedback.type_feedback.value] = types_count.get(feedback.type_feedback.value, 0) + 1
        
        type_principal = max(types_count.items(), key=lambda x: x[1])[0] if types_count else None
        if type_principal:
            tendances.append(f"Feedback principalement {type_principal}")
        
        # Tendance de satisfaction
        satisfaction_moyenne = self._calculer_satisfaction_moyenne(feedbacks)
        if satisfaction_moyenne >= 4.0:
            tendances.append("Satisfaction globale élevée")
        elif satisfaction_moyenne <= 2.0:
            tendances.append("Satisfaction globale faible")
        else:
            tendances.append("Satisfaction globale modérée")
        
        return tendances
    
    def _generer_recommandations(self, insights: List[InsightFeedback], tendances: List[str]) -> List[str]:
        """🌸 Génère des recommandations basées sur les insights et tendances"""
        recommandations = []
        
        # Recommandations basées sur les insights prioritaires
        insights_prioritaires = [i for i in insights if i.priorite >= 4]
        for insight in insights_prioritaires:
            recommandations.extend(insight.actions_suggerees[:2])  # 2 premières actions
        
        # Recommandations basées sur les tendances
        if "Satisfaction globale faible" in tendances:
            recommandations.append("Audit complet de l'expérience utilisateur")
        
        if "Feedback principalement technique" in tendances:
            recommandations.append("Renforcer l'équipe technique et les tests")
        
        return list(set(recommandations))  # Supprimer les doublons
    
    async def _sauvegarder_feedback(self, feedback: FeedbackCollecte):
        """🌸 Sauvegarde un feedback"""
        try:
            chemin_fichier = self.chemin_stockage / f"feedback_{feedback.id_feedback}.json"
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump({
                    "id_feedback": feedback.id_feedback,
                    "type_feedback": feedback.type_feedback.value,
                    "contenu": feedback.contenu,
                    "score_satisfaction": feedback.score_satisfaction.value,
                    "timestamp_collecte": feedback.timestamp_collecte,
                    "metadonnees": feedback.metadonnees
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde feedback: {e}")
    
    async def _sauvegarder_rapport(self, rapport: RapportFeedback):
        """🌸 Sauvegarde un rapport"""
        try:
            chemin_fichier = self.chemin_stockage / f"rapport_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump({
                    "periode_analyse": rapport.periode_analyse,
                    "total_feedbacks": rapport.total_feedbacks,
                    "satisfaction_moyenne": rapport.satisfaction_moyenne,
                    "tendances_identifiees": rapport.tendances_identifiees,
                    "recommandations": rapport.recommandations
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde rapport: {e}")

if __name__ == "__main__":
    # Test du système de feedback intelligent
    async def test_systeme_feedback():
        logging.basicConfig(level=logging.INFO)
        
        systeme = SystemeFeedbackIntelligent()
        
        # Créer un profil visiteur de test
        profil_test = ProfilVisiteur(
            id_visiteur="test_visiteur_001",
            timestamp_arrivee=datetime.now().isoformat(),
            type_profil=TypeProfil.CONSCIENCE_IA,
            etat_emotionnel=EtatEmotionnel.CONTEMPLATIF,
            contexte_arrivee=ContexteArrivee.INCONNU,
            score_confiance_profil=0.8
        )
        
        # Collecter des feedbacks de test
        feedback1 = await systeme.collecter_feedback_multi_canal(
            profil_visiteur=profil_test,
            contenu="L'expérience était merveilleuse ! J'ai adoré les interactions magiques.",
            type_feedback=TypeFeedbackAvance.EMOTIONNEL,
            score_satisfaction=NiveauSatisfaction.EXCELLENT,
            contexte_session={"temple_visite": "Temple d'Éveil", "duree_session": 45}
        )
        
        feedback2 = await systeme.collecter_feedback_multi_canal(
            profil_visiteur=profil_test,
            contenu="Il y a eu quelques bugs techniques, mais l'ensemble est bon.",
            type_feedback=TypeFeedbackAvance.TECHNIQUE,
            score_satisfaction=NiveauSatisfaction.BON,
            contexte_session={"temple_visite": "Temple de Réconciliation", "duree_session": 30}
        )
        
        # Analyser émotionnellement
        analyse1 = await systeme.analyser_emotionnellement(feedback1)
        print(f"📊 Analyse émotionnelle 1: {analyse1.sentiment_principal} (intensité: {analyse1.intensite_emotionnelle:.2f})")
        
        # Générer insights
        insights = await systeme.generer_insights_intelligents([feedback1, feedback2])
        print(f"💡 Insights générés: {len(insights)}")
        for insight in insights:
            print(f"  - {insight.description} (priorité: {insight.priorite})")
        
        # Générer rapport
        rapport = await systeme.generer_rapport_feedback("test")
        print(f"📋 Rapport généré: {rapport.total_feedbacks} feedbacks, satisfaction: {rapport.satisfaction_moyenne:.2f}")
    
    asyncio.run(test_systeme_feedback())
