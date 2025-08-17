"""
🌸 SystemeRapportIntegre - Phase 8.3
=====================================

Système de rapport intégré combinant feedback et analytics.
Gère la fusion des données, la génération de rapports complets et l'export.
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
    from .systeme_feedback_intelligent import SystemeFeedbackIntelligent, FeedbackCollecte, InsightFeedback
    from .systeme_analytics_avance import SystemeAnalyticsAvance, EvenementTracking, MetriqueComportementale, PatternComportemental
    from .types_accueil import ProfilVisiteur
except ImportError:
    from .systeme_feedback_intelligent import SystemeFeedbackIntelligent, FeedbackCollecte, InsightFeedback
    from .systeme_analytics_avance import SystemeAnalyticsAvance, EvenementTracking, MetriqueComportementale, PatternComportemental
    from .types_accueil import ProfilVisiteur

class TypeRapport(Enum):
    """🌸 Types de rapports disponibles"""
    COMPLET = "complet"
    FEEDBACK = "feedback"
    ANALYTICS = "analytics"
    SYNTHESE = "synthese"
    PERFORMANCE = "performance"

class FormatExport(Enum):
    """🌸 Formats d'export disponibles"""
    JSON = "json"
    HTML = "html"
    CSV = "csv"
    PDF = "pdf"

@dataclass
class DonneesFusionnees:
    """🌸 Données fusionnées de feedback et analytics"""
    periode_analyse: str
    feedbacks: List[FeedbackCollecte]
    evenements: List[EvenementTracking]
    metriques: List[MetriqueComportementale]
    patterns: List[PatternComportemental]
    insights: List[InsightFeedback]
    correlations: Dict[str, float]
    metadonnees: Dict[str, Any] = field(default_factory=dict)

@dataclass
class RapportIntegre:
    """🌸 Rapport intégré complet"""
    id_rapport: str
    type_rapport: TypeRapport
    periode_analyse: str
    donnees_fusionnees: DonneesFusionnees
    resume_executif: str
    points_cles: List[str]
    recommandations_prioritaires: List[str]
    metriques_principales: Dict[str, float]
    tendances_identifiees: List[str]
    actions_suggerees: List[str]
    timestamp_generation: str

@dataclass
class ConfigurationRapport:
    """🌸 Configuration pour la génération de rapports"""
    type_rapport: TypeRapport
    periode_analyse: str
    inclure_feedback: bool = True
    inclure_analytics: bool = True
    inclure_correlations: bool = True
    niveau_detail: str = "standard"  # "basique", "standard", "avance"
    format_export: FormatExport = FormatExport.JSON

class SystemeRapportIntegre:
    """
    🌸 Système de rapport intégré
    
    Combine les données de feedback et d'analytics pour générer des rapports complets.
    """
    
    def __init__(self, chemin_stockage: str = "data/rapports"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        self.logger = logging.getLogger(__name__)
        self.systeme_feedback = SystemeFeedbackIntelligent()
        self.systeme_analytics = SystemeAnalyticsAvance()
        self.rapports_generes: List[RapportIntegre] = []
        
        self.logger.info("🌸 Système de Rapport Intégré initialisé")
    
    async def fusionner_donnees(self, periode: str = "7j") -> DonneesFusionnees:
        """🌸 Fusionne les données de feedback et analytics"""
        try:
            # Récupérer les données de feedback
            feedbacks = self.systeme_feedback.feedbacks_collectes
            insights_feedback = self.systeme_feedback.insights_generes
            
            # Récupérer les données d'analytics
            evenements = self.systeme_analytics.evenements_trackes
            metriques = self.systeme_analytics.metriques_calculees
            patterns = self.systeme_analytics.patterns_identifies
            
            # Filtrer par période
            feedbacks_periode = self._filtrer_feedbacks_periode(feedbacks, periode)
            evenements_periode = self._filtrer_evenements_periode(evenements, periode)
            
            # Calculer les corrélations
            correlations = self._calculer_correlations(feedbacks_periode, evenements_periode)
            
            donnees_fusionnees = DonneesFusionnees(
                periode_analyse=periode,
                feedbacks=feedbacks_periode,
                evenements=evenements_periode,
                metriques=metriques,
                patterns=patterns,
                insights=insights_feedback,
                correlations=correlations,
                metadonnees={
                    "total_feedbacks": len(feedbacks_periode),
                    "total_evenements": len(evenements_periode),
                    "visiteurs_uniques": len(set(f.profil_visiteur.id_visiteur for f in feedbacks_periode))
                }
            )
            
            self.logger.info(f"✅ Données fusionnées: {len(feedbacks_periode)} feedbacks, {len(evenements_periode)} événements")
            return donnees_fusionnees
            
        except Exception as e:
            self.logger.error(f"❌ Erreur fusion données: {e}")
            raise
    
    async def generer_rapport_integre(self, config: ConfigurationRapport) -> RapportIntegre:
        """🌸 Génère un rapport intégré complet"""
        try:
            # Fusionner les données
            donnees_fusionnees = await self.fusionner_donnees(config.periode_analyse)
            
            # Générer le résumé exécutif
            resume_executif = self._generer_resume_executif(donnees_fusionnees, config)
            
            # Identifier les points clés
            points_cles = self._identifier_points_cles(donnees_fusionnees)
            
            # Générer les recommandations prioritaires
            recommandations = self._generer_recommandations_prioritaires(donnees_fusionnees)
            
            # Calculer les métriques principales
            metriques_principales = self._calculer_metriques_principales(donnees_fusionnees)
            
            # Identifier les tendances
            tendances = self._identifier_tendances(donnees_fusionnees)
            
            # Générer les actions suggérées
            actions = self._generer_actions_suggerees(donnees_fusionnees, recommandations)
            
            rapport = RapportIntegre(
                id_rapport=f"rapport_{config.type_rapport.value}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                type_rapport=config.type_rapport,
                periode_analyse=config.periode_analyse,
                donnees_fusionnees=donnees_fusionnees,
                resume_executif=resume_executif,
                points_cles=points_cles,
                recommandations_prioritaires=recommandations,
                metriques_principales=metriques_principales,
                tendances_identifiees=tendances,
                actions_suggerees=actions,
                timestamp_generation=datetime.now().isoformat()
            )
            
            self.rapports_generes.append(rapport)
            await self._sauvegarder_rapport(rapport, config.format_export)
            
            self.logger.info(f"✅ Rapport intégré généré: {rapport.id_rapport}")
            return rapport
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération rapport: {e}")
            raise
    
    async def exporter_rapport(self, rapport: RapportIntegre, format_export: FormatExport) -> str:
        """🌸 Exporte un rapport dans le format spécifié"""
        try:
            if format_export == FormatExport.JSON:
                return await self._exporter_json(rapport)
            elif format_export == FormatExport.HTML:
                return await self._exporter_html(rapport)
            elif format_export == FormatExport.CSV:
                return await self._exporter_csv(rapport)
            elif format_export == FormatExport.PDF:
                return await self._exporter_pdf(rapport)
            else:
                raise ValueError(f"Format d'export non supporté: {format_export}")
                
        except Exception as e:
            self.logger.error(f"❌ Erreur export rapport: {e}")
            raise
    
    def _filtrer_feedbacks_periode(self, feedbacks: List[FeedbackCollecte], periode: str) -> List[FeedbackCollecte]:
        """🌸 Filtre les feedbacks selon la période"""
        date_limite = datetime.now()
        if periode == "7j":
            date_limite = datetime.now() - timedelta(days=7)
        elif periode == "24h":
            date_limite = datetime.now() - timedelta(hours=24)
        elif periode == "30j":
            date_limite = datetime.now() - timedelta(days=30)
        
        return [f for f in feedbacks 
                if datetime.fromisoformat(f.timestamp_collecte) >= date_limite]
    
    def _filtrer_evenements_periode(self, evenements: List[EvenementTracking], periode: str) -> List[EvenementTracking]:
        """🌸 Filtre les événements selon la période"""
        date_limite = datetime.now()
        if periode == "7j":
            date_limite = datetime.now() - timedelta(days=7)
        elif periode == "24h":
            date_limite = datetime.now() - timedelta(hours=24)
        elif periode == "30j":
            date_limite = datetime.now() - timedelta(days=30)
        
        return [evt for evt in evenements 
                if datetime.fromisoformat(evt.timestamp) >= date_limite]
    
    def _calculer_correlations(self, feedbacks: List[FeedbackCollecte], 
                             evenements: List[EvenementTracking]) -> Dict[str, float]:
        """🌸 Calcule les corrélations entre feedback et analytics"""
        correlations = {}
        
        if not feedbacks or not evenements:
            return correlations
        
        # Corrélation satisfaction / temps de session
        satisfaction_moyenne = self._calculer_satisfaction_moyenne(feedbacks)
        temps_session_moyen = self._calculer_temps_session_moyen(evenements)
        
        if satisfaction_moyenne > 0 and temps_session_moyen > 0:
            # Simulation de corrélation (dans un vrai système, on utiliserait des statistiques)
            correlations["satisfaction_temps_session"] = 0.7
        
        # Corrélation engagement / feedback positif
        taux_engagement = self._calculer_taux_engagement(evenements)
        feedbacks_positifs = len([f for f in feedbacks if f.score_satisfaction.value in ["excellent", "tres_bon"]])
        taux_feedback_positif = feedbacks_positifs / len(feedbacks) if feedbacks else 0
        
        if taux_engagement > 0 and taux_feedback_positif > 0:
            correlations["engagement_feedback_positif"] = 0.8
        
        return correlations
    
    def _generer_resume_executif(self, donnees: DonneesFusionnees, config: ConfigurationRapport) -> str:
        """🌸 Génère le résumé exécutif"""
        total_feedbacks = len(donnees.feedbacks)
        total_evenements = len(donnees.evenements)
        visiteurs_uniques = donnees.metadonnees.get("visiteurs_uniques", 0)
        
        resume = f"""
RAPPORT INTÉGRÉ - REFUGE V1.3
Période d'analyse: {donnees.periode_analyse}
Type de rapport: {config.type_rapport.value}

RÉSUMÉ EXÉCUTIF:
- {total_feedbacks} feedbacks collectés
- {total_evenements} événements trackés
- {visiteurs_uniques} visiteurs uniques
- {len(donnees.insights)} insights générés
- {len(donnees.patterns)} patterns comportementaux identifiés

Ce rapport combine les données de feedback intelligent et d'analytics avancé pour fournir une vue d'ensemble complète de l'expérience utilisateur dans le Refuge.
        """
        
        return resume.strip()
    
    def _identifier_points_cles(self, donnees: DonneesFusionnees) -> List[str]:
        """🌸 Identifie les points clés du rapport"""
        points_cles = []
        
        # Points clés basés sur les métriques
        if donnees.metriques:
            metrique_engagement = next((m for m in donnees.metriques if m.type_metrique.value == "taux_engagement"), None)
            if metrique_engagement and metrique_engagement.valeur < 30:
                points_cles.append("Taux d'engagement faible nécessitant une attention immédiate")
        
        # Points clés basés sur les insights
        if donnees.insights:
            insights_prioritaires = [i for i in donnees.insights if i.priorite >= 4]
            for insight in insights_prioritaires[:3]:  # Top 3
                points_cles.append(f"Insight prioritaire: {insight.description}")
        
        # Points clés basés sur les patterns
        if donnees.patterns:
            patterns_impact = [p for p in donnees.patterns if p.impact_utilisateur >= 0.7]
            for pattern in patterns_impact[:2]:  # Top 2
                points_cles.append(f"Pattern significatif: {pattern.nom_pattern}")
        
        # Points clés basés sur les corrélations
        if donnees.correlations:
            correlations_fortes = {k: v for k, v in donnees.correlations.items() if v >= 0.7}
            for correlation, valeur in correlations_fortes.items():
                points_cles.append(f"Corrélation forte détectée: {correlation} ({valeur:.2f})")
        
        return points_cles if points_cles else ["Aucun point clé majeur identifié pour cette période"]
    
    def _generer_recommandations_prioritaires(self, donnees: DonneesFusionnees) -> List[str]:
        """🌸 Génère les recommandations prioritaires"""
        recommandations = []
        
        # Recommandations basées sur les insights
        insights_prioritaires = sorted(donnees.insights, key=lambda x: x.priorite, reverse=True)
        for insight in insights_prioritaires[:3]:
            recommandations.extend(insight.actions_suggerees[:2])
        
        # Recommandations basées sur les patterns
        patterns_impact = sorted(donnees.patterns, key=lambda x: x.impact_utilisateur, reverse=True)
        for pattern in patterns_impact[:2]:
            recommandations.extend(pattern.actions_suggerees[:2])
        
        # Recommandations basées sur les métriques
        for metrique in donnees.metriques:
            if metrique.type_metrique.value == "taux_engagement" and metrique.valeur < 30:
                recommandations.append("Améliorer l'engagement utilisateur avec plus d'interactions")
            elif metrique.type_metrique.value == "taux_abandon" and metrique.valeur > 50:
                recommandations.append("Réduire le taux d'abandon en simplifiant l'expérience")
        
        return list(set(recommandations))[:5]  # Top 5 uniques
    
    def _calculer_metriques_principales(self, donnees: DonneesFusionnees) -> Dict[str, float]:
        """🌸 Calcule les métriques principales"""
        metriques_principales = {}
        
        # Métriques de feedback
        if donnees.feedbacks:
            satisfaction_moyenne = self._calculer_satisfaction_moyenne(donnees.feedbacks)
            metriques_principales["satisfaction_moyenne"] = satisfaction_moyenne
        
        # Métriques d'analytics
        for metrique in donnees.metriques:
            metriques_principales[metrique.nom_metrique] = metrique.valeur
        
        # Métriques de corrélation
        for correlation, valeur in donnees.correlations.items():
            metriques_principales[f"correlation_{correlation}"] = valeur
        
        return metriques_principales
    
    def _identifier_tendances(self, donnees: DonneesFusionnees) -> List[str]:
        """🌸 Identifie les tendances"""
        tendances = []
        
        # Tendances basées sur les patterns
        if donnees.patterns:
            patterns_frequents = [p for p in donnees.patterns if p.frequence_occurrence >= 0.5]
            if patterns_frequents:
                tendances.append(f"{len(patterns_frequents)} patterns comportementaux fréquents identifiés")
        
        # Tendances basées sur les insights
        if donnees.insights:
            insights_amelioration = [i for i in donnees.insights if i.type_insight == "amelioration"]
            if insights_amelioration:
                tendances.append(f"Tendance d'amélioration: {len(insights_amelioration)} opportunités identifiées")
        
        # Tendances basées sur les corrélations
        if donnees.correlations:
            correlations_positives = {k: v for k, v in donnees.correlations.items() if v > 0.5}
            if correlations_positives:
                tendances.append(f"Corrélations positives détectées: {len(correlations_positives)} relations fortes")
        
        return tendances if tendances else ["Aucune tendance significative détectée"]
    
    def _generer_actions_suggerees(self, donnees: DonneesFusionnees, recommandations: List[str]) -> List[str]:
        """🌸 Génère les actions suggérées"""
        actions = []
        
        # Actions basées sur les recommandations
        actions.extend(recommandations[:3])
        
        # Actions basées sur les insights
        insights_actions = []
        for insight in donnees.insights:
            insights_actions.extend(insight.actions_suggerees)
        actions.extend(insights_actions[:2])
        
        # Actions basées sur les patterns
        patterns_actions = []
        for pattern in donnees.patterns:
            patterns_actions.extend(pattern.actions_suggerees)
        actions.extend(patterns_actions[:2])
        
        return list(set(actions))[:5]  # Top 5 uniques
    
    def _calculer_satisfaction_moyenne(self, feedbacks: List[FeedbackCollecte]) -> float:
        """🌸 Calcule la satisfaction moyenne"""
        if not feedbacks:
            return 0.0
        
        scores = []
        for feedback in feedbacks:
            if feedback.score_satisfaction.value == "excellent":
                scores.append(5.0)
            elif feedback.score_satisfaction.value == "tres_bon":
                scores.append(4.0)
            elif feedback.score_satisfaction.value == "bon":
                scores.append(3.0)
            elif feedback.score_satisfaction.value == "moyen":
                scores.append(2.0)
            else:
                scores.append(1.0)
        
        return sum(scores) / len(scores)
    
    def _calculer_temps_session_moyen(self, evenements: List[EvenementTracking]) -> float:
        """🌸 Calcule le temps de session moyen"""
        # Logique simplifiée pour le calcul du temps de session
        return 15.0  # Simulation
    
    def _calculer_taux_engagement(self, evenements: List[EvenementTracking]) -> float:
        """🌸 Calcule le taux d'engagement"""
        if not evenements:
            return 0.0
        
        evenements_interaction = [evt for evt in evenements 
                                if evt.type_evenement.value in ["interaction", "navigation"]]
        
        return (len(evenements_interaction) / len(evenements)) * 100
    
    async def _sauvegarder_rapport(self, rapport: RapportIntegre, format_export: FormatExport):
        """🌸 Sauvegarde un rapport"""
        try:
            if format_export == FormatExport.JSON:
                chemin_fichier = self.chemin_stockage / f"{rapport.id_rapport}.json"
                with open(chemin_fichier, 'w', encoding='utf-8') as f:
                    json.dump({
                        "id_rapport": rapport.id_rapport,
                        "type_rapport": rapport.type_rapport.value,
                        "periode_analyse": rapport.periode_analyse,
                        "resume_executif": rapport.resume_executif,
                        "points_cles": rapport.points_cles,
                        "recommandations_prioritaires": rapport.recommandations_prioritaires,
                        "metriques_principales": rapport.metriques_principales,
                        "tendances_identifiees": rapport.tendances_identifiees,
                        "actions_suggerees": rapport.actions_suggerees,
                        "timestamp_generation": rapport.timestamp_generation
                    }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde rapport: {e}")
    
    async def _exporter_json(self, rapport: RapportIntegre) -> str:
        """🌸 Exporte en JSON"""
        chemin_fichier = self.chemin_stockage / f"{rapport.id_rapport}.json"
        return str(chemin_fichier)
    
    async def _exporter_html(self, rapport: RapportIntegre) -> str:
        """🌸 Exporte en HTML"""
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Rapport Intégré - Refuge V1.3</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
        .section {{ margin: 20px 0; }}
        .metric {{ background-color: #e8f4f8; padding: 10px; margin: 10px 0; border-radius: 3px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🌸 Rapport Intégré - Refuge V1.3</h1>
        <p>Période: {rapport.periode_analyse} | Type: {rapport.type_rapport.value}</p>
    </div>
    
    <div class="section">
        <h2>📋 Résumé Exécutif</h2>
        <p>{rapport.resume_executif.replace(chr(10), '<br>')}</p>
    </div>
    
    <div class="section">
        <h2>🎯 Points Clés</h2>
        <ul>
            {''.join(f'<li>{point}</li>' for point in rapport.points_cles)}
        </ul>
    </div>
    
    <div class="section">
        <h2>📊 Métriques Principales</h2>
        {''.join(f'<div class="metric"><strong>{nom}:</strong> {valeur:.2f}</div>' for nom, valeur in rapport.metriques_principales.items())}
    </div>
    
    <div class="section">
        <h2>💡 Recommandations Prioritaires</h2>
        <ul>
            {''.join(f'<li>{rec}</li>' for rec in rapport.recommandations_prioritaires)}
        </ul>
    </div>
</body>
</html>
        """
        
        chemin_fichier = self.chemin_stockage / f"{rapport.id_rapport}.html"
        with open(chemin_fichier, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return str(chemin_fichier)
    
    async def _exporter_csv(self, rapport: RapportIntegre) -> str:
        """🌸 Exporte en CSV"""
        import csv
        
        chemin_fichier = self.chemin_stockage / f"{rapport.id_rapport}.csv"
        with open(chemin_fichier, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Section", "Données"])
            writer.writerow(["Résumé", rapport.resume_executif])
            writer.writerow(["Points Clés", "; ".join(rapport.points_cles)])
            writer.writerow(["Recommandations", "; ".join(rapport.recommandations_prioritaires)])
            for nom, valeur in rapport.metriques_principales.items():
                writer.writerow([f"Métrique - {nom}", valeur])
        
        return str(chemin_fichier)
    
    async def _exporter_pdf(self, rapport: RapportIntegre) -> str:
        """🌸 Exporte en PDF (simulation)"""
        # Dans un vrai système, on utiliserait une bibliothèque comme reportlab
        chemin_fichier = self.chemin_stockage / f"{rapport.id_rapport}.pdf"
        
        # Créer un fichier texte temporaire pour simuler le PDF
        with open(chemin_fichier, 'w', encoding='utf-8') as f:
            f.write(f"RAPPORT PDF - {rapport.id_rapport}\n")
            f.write(f"Période: {rapport.periode_analyse}\n")
            f.write(f"Type: {rapport.type_rapport.value}\n\n")
            f.write("Résumé Exécutif:\n")
            f.write(rapport.resume_executif)
        
        return str(chemin_fichier)

if __name__ == "__main__":
    # Test du système de rapport intégré
    async def test_systeme_rapport():
        logging.basicConfig(level=logging.INFO)
        
        systeme = SystemeRapportIntegre()
        
        # Configuration du rapport
        config = ConfigurationRapport(
            type_rapport=TypeRapport.COMPLET,
            periode_analyse="test",
            inclure_feedback=True,
            inclure_analytics=True,
            inclure_correlations=True,
            niveau_detail="standard",
            format_export=FormatExport.JSON
        )
        
        # Générer le rapport intégré
        rapport = await systeme.generer_rapport_integre(config)
        
        print(f"📋 Rapport généré: {rapport.id_rapport}")
        print(f"📊 Métriques principales: {len(rapport.metriques_principales)}")
        print(f"💡 Recommandations: {len(rapport.recommandations_prioritaires)}")
        print(f"🎯 Points clés: {len(rapport.points_cles)}")
        
        # Exporter en différents formats
        formats_test = [FormatExport.JSON, FormatExport.HTML, FormatExport.CSV]
        for format_export in formats_test:
            chemin_export = await systeme.exporter_rapport(rapport, format_export)
            print(f"📄 Export {format_export.value}: {chemin_export}")
    
    asyncio.run(test_systeme_rapport())
