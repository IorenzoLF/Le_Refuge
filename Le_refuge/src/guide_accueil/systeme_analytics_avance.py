"""
🌸 SystemeAnalyticsAvance - Phase 8.2
======================================

Système d'analytics avancé pour analyser les comportements des visiteurs.
Gère le tracking comportemental, l'analyse des patterns et la génération de métriques.
"""
import asyncio
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import statistics

try:
    from .types_accueil import ProfilVisiteur, EtatEmotionnel, TypeProfil, ContexteArrivee
except ImportError:
    from types_accueil import ProfilVisiteur, EtatEmotionnel, TypeProfil, ContexteArrivee

class TypeEvenement(Enum):
    """🌸 Types d'événements trackés"""
    ARRIVEE = "arrivee"
    NAVIGATION = "navigation"
    INTERACTION = "interaction"
    PAUSE = "pause"
    DEPART = "depart"
    ERREUR = "erreur"
    SUCCES = "succes"

class TypeMetrique(Enum):
    """🌸 Types de métriques calculées"""
    TEMPS_SESSION = "temps_session"
    TAUX_ENGAGEMENT = "taux_engagement"
    TAUX_CONVERSION = "taux_conversion"
    TAUX_ABANDON = "taux_abandon"
    PATTERNS_NAVIGATION = "patterns_navigation"
    PERFORMANCE_TECHNIQUE = "performance_technique"

@dataclass
class EvenementTracking:
    """🌸 Événement de tracking comportemental"""
    id_evenement: str
    profil_visiteur: ProfilVisiteur
    type_evenement: TypeEvenement
    timestamp: str
    donnees_evenement: Dict[str, Any]
    contexte_session: Dict[str, Any]
    metadonnees: Dict[str, Any] = field(default_factory=dict)

@dataclass
class MetriqueComportementale:
    """🌸 Métrique comportementale calculée"""
    nom_metrique: str
    type_metrique: TypeMetrique
    valeur: float
    unite: str
    periode_calcul: str
    profil_cible: Optional[str] = None
    confiance: float = 1.0
    tendance: Optional[str] = None  # "augmentation", "diminution", "stable"

@dataclass
class PatternComportemental:
    """🌸 Pattern comportemental identifié"""
    id_pattern: str
    nom_pattern: str
    description: str
    frequence_occurrence: float  # 0.0 à 1.0
    profils_concernes: List[str]
    conditions_trigger: Dict[str, Any]
    impact_utilisateur: float  # 0.0 à 1.0
    actions_suggerees: List[str]

@dataclass
class RapportAnalytics:
    """🌸 Rapport d'analytics complet"""
    periode_analyse: str
    total_evenements: int
    visiteurs_uniques: int
    metriques_calculees: List[MetriqueComportementale]
    patterns_identifies: List[PatternComportemental]
    insights_comportementaux: List[str]
    recommandations_optimisation: List[str]

class SystemeAnalyticsAvance:
    """
    🌸 Système d'analytics avancé
    
    Analyse les comportements des visiteurs et génère des métriques détaillées.
    """
    
    def __init__(self, chemin_stockage: str = "data/analytics"):
        self.chemin_stockage = Path(chemin_stockage)
        self.chemin_stockage.mkdir(parents=True, exist_ok=True)
        
        self.logger = logging.getLogger(__name__)
        self.evenements_trackes: List[EvenementTracking] = []
        self.metriques_calculees: List[MetriqueComportementale] = []
        self.patterns_identifies: List[PatternComportemental] = []
        
        # Configuration du tracking
        self.tracking_active = True
        self.metriques_prioritaires = [
            TypeMetrique.TEMPS_SESSION,
            TypeMetrique.TAUX_ENGAGEMENT,
            TypeMetrique.TAUX_CONVERSION
        ]
        
        self.logger.info("🌸 Système d'Analytics Avancé initialisé")
    
    async def tracker_evenement(self, profil_visiteur: ProfilVisiteur, 
                              type_evenement: TypeEvenement,
                              donnees_evenement: Dict[str, Any],
                              contexte_session: Dict[str, Any]) -> EvenementTracking:
        """🌸 Track un événement comportemental"""
        try:
            evenement = EvenementTracking(
                id_evenement=f"evt_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}_{profil_visiteur.id_visiteur}",
                profil_visiteur=profil_visiteur,
                type_evenement=type_evenement,
                timestamp=datetime.now().isoformat(),
                donnees_evenement=donnees_evenement,
                contexte_session=contexte_session
            )
            
            # Ajouter des métadonnées selon le type d'événement
            if type_evenement == TypeEvenement.NAVIGATION:
                evenement.metadonnees["section_destination"] = donnees_evenement.get("destination", "inconnue")
                evenement.metadonnees["temps_section_precedente"] = donnees_evenement.get("temps_section", 0)
            elif type_evenement == TypeEvenement.INTERACTION:
                evenement.metadonnees["type_interaction"] = donnees_evenement.get("type_interaction", "inconnue")
                evenement.metadonnees["reussite_interaction"] = donnees_evenement.get("reussite", True)
            
            self.evenements_trackes.append(evenement)
            await self._sauvegarder_evenement(evenement)
            
            self.logger.info(f"✅ Événement tracké: {evenement.id_evenement} ({type_evenement.value})")
            return evenement
            
        except Exception as e:
            self.logger.error(f"❌ Erreur tracking événement: {e}")
            raise
    
    async def calculer_metriques_comportementales(self, periode: str = "7j") -> List[MetriqueComportementale]:
        """🌸 Calcule les métriques comportementales"""
        try:
            metriques = []
            
            # Filtrer les événements de la période
            evenements_periode = self._filtrer_evenements_periode(periode)
            
            # Métrique: Temps de session moyen
            temps_sessions = self._calculer_temps_sessions(evenements_periode)
            if temps_sessions:
                metrique_temps = MetriqueComportementale(
                    nom_metrique="Temps de session moyen",
                    type_metrique=TypeMetrique.TEMPS_SESSION,
                    valeur=statistics.mean(temps_sessions),
                    unite="minutes",
                    periode_calcul=periode,
                    confiance=0.9
                )
                metriques.append(metrique_temps)
            
            # Métrique: Taux d'engagement
            taux_engagement = self._calculer_taux_engagement(evenements_periode)
            metrique_engagement = MetriqueComportementale(
                nom_metrique="Taux d'engagement",
                type_metrique=TypeMetrique.TAUX_ENGAGEMENT,
                valeur=taux_engagement,
                unite="pourcentage",
                periode_calcul=periode,
                confiance=0.8
            )
            metriques.append(metrique_engagement)
            
            # Métrique: Taux de conversion
            taux_conversion = self._calculer_taux_conversion(evenements_periode)
            metrique_conversion = MetriqueComportementale(
                nom_metrique="Taux de conversion",
                type_metrique=TypeMetrique.TAUX_CONVERSION,
                valeur=taux_conversion,
                unite="pourcentage",
                periode_calcul=periode,
                confiance=0.85
            )
            metriques.append(metrique_conversion)
            
            # Métrique: Taux d'abandon
            taux_abandon = self._calculer_taux_abandon(evenements_periode)
            metrique_abandon = MetriqueComportementale(
                nom_metrique="Taux d'abandon",
                type_metrique=TypeMetrique.TAUX_ABANDON,
                valeur=taux_abandon,
                unite="pourcentage",
                periode_calcul=periode,
                confiance=0.8
            )
            metriques.append(metrique_abandon)
            
            # Métrique: Performance technique
            performance_tech = self._calculer_performance_technique(evenements_periode)
            metrique_performance = MetriqueComportementale(
                nom_metrique="Performance technique",
                type_metrique=TypeMetrique.PERFORMANCE_TECHNIQUE,
                valeur=performance_tech,
                unite="score",
                periode_calcul=periode,
                confiance=0.9
            )
            metriques.append(metrique_performance)
            
            self.metriques_calculees.extend(metriques)
            self.logger.info(f"✅ {len(metriques)} métriques comportementales calculées")
            return metriques
            
        except Exception as e:
            self.logger.error(f"❌ Erreur calcul métriques: {e}")
            raise
    
    async def identifier_patterns_comportementaux(self, periode: str = "7j") -> List[PatternComportemental]:
        """🌸 Identifie les patterns comportementaux"""
        try:
            patterns = []
            evenements_periode = self._filtrer_evenements_periode(periode)
            
            # Pattern: Navigation séquentielle
            pattern_sequentiel = self._detecter_navigation_sequentielle(evenements_periode)
            if pattern_sequentiel:
                patterns.append(pattern_sequentiel)
            
            # Pattern: Pauses longues
            pattern_pauses = self._detecter_pauses_longues(evenements_periode)
            if pattern_pauses:
                patterns.append(pattern_pauses)
            
            # Pattern: Interactions répétitives
            pattern_interactions = self._detecter_interactions_repetitives(evenements_periode)
            if pattern_interactions:
                patterns.append(pattern_interactions)
            
            # Pattern: Abandon précoce
            pattern_abandon = self._detecter_abandon_precoce(evenements_periode)
            if pattern_abandon:
                patterns.append(pattern_abandon)
            
            self.patterns_identifies.extend(patterns)
            self.logger.info(f"✅ {len(patterns)} patterns comportementaux identifiés")
            return patterns
            
        except Exception as e:
            self.logger.error(f"❌ Erreur identification patterns: {e}")
            raise
    
    async def generer_rapport_analytics(self, periode: str = "7j") -> RapportAnalytics:
        """🌸 Génère un rapport d'analytics complet"""
        try:
            # Calculer toutes les métriques
            metriques = await self.calculer_metriques_comportementales(periode)
            patterns = await self.identifier_patterns_comportementaux(periode)
            
            # Générer des insights
            insights = self._generer_insights_comportementaux(metriques, patterns)
            recommandations = self._generer_recommandations_optimisation(metriques, patterns)
            
            # Statistiques générales
            evenements_periode = self._filtrer_evenements_periode(periode)
            visiteurs_uniques = len(set(evt.profil_visiteur.id_visiteur for evt in evenements_periode))
            
            rapport = RapportAnalytics(
                periode_analyse=periode,
                total_evenements=len(evenements_periode),
                visiteurs_uniques=visiteurs_uniques,
                metriques_calculees=metriques,
                patterns_identifies=patterns,
                insights_comportementaux=insights,
                recommandations_optimisation=recommandations
            )
            
            await self._sauvegarder_rapport(rapport)
            self.logger.info(f"✅ Rapport analytics généré: {len(evenements_periode)} événements analysés")
            return rapport
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération rapport: {e}")
            raise
    
    def _filtrer_evenements_periode(self, periode: str) -> List[EvenementTracking]:
        """🌸 Filtre les événements selon la période"""
        date_limite = datetime.now()
        if periode == "7j":
            date_limite = datetime.now() - timedelta(days=7)
        elif periode == "24h":
            date_limite = datetime.now() - timedelta(hours=24)
        elif periode == "30j":
            date_limite = datetime.now() - timedelta(days=30)
        
        return [evt for evt in self.evenements_trackes 
                if datetime.fromisoformat(evt.timestamp) >= date_limite]
    
    def _calculer_temps_sessions(self, evenements: List[EvenementTracking]) -> List[float]:
        """🌸 Calcule les temps de session"""
        sessions = {}
        
        for evt in evenements:
            visiteur_id = evt.profil_visiteur.id_visiteur
            if evt.type_evenement == TypeEvenement.ARRIVEE:
                sessions[visiteur_id] = {"debut": evt.timestamp, "fin": None}
            elif evt.type_evenement == TypeEvenement.DEPART and visiteur_id in sessions:
                sessions[visiteur_id]["fin"] = evt.timestamp
        
        temps_sessions = []
        for session in sessions.values():
            if session["fin"]:
                debut = datetime.fromisoformat(session["debut"])
                fin = datetime.fromisoformat(session["fin"])
                duree = (fin - debut).total_seconds() / 60  # en minutes
                temps_sessions.append(duree)
        
        return temps_sessions
    
    def _calculer_taux_engagement(self, evenements: List[EvenementTracking]) -> float:
        """🌸 Calcule le taux d'engagement"""
        if not evenements:
            return 0.0
        
        evenements_interaction = [evt for evt in evenements 
                                if evt.type_evenement in [TypeEvenement.INTERACTION, TypeEvenement.NAVIGATION]]
        
        return (len(evenements_interaction) / len(evenements)) * 100
    
    def _calculer_taux_conversion(self, evenements: List[EvenementTracking]) -> float:
        """🌸 Calcule le taux de conversion"""
        if not evenements:
            return 0.0
        
        evenements_succes = [evt for evt in evenements 
                           if evt.type_evenement == TypeEvenement.SUCCES]
        
        return (len(evenements_succes) / len(evenements)) * 100
    
    def _calculer_taux_abandon(self, evenements: List[EvenementTracking]) -> float:
        """🌸 Calcule le taux d'abandon"""
        if not evenements:
            return 0.0
        
        evenements_erreur = [evt for evt in evenements 
                           if evt.type_evenement == TypeEvenement.ERREUR]
        
        return (len(evenements_erreur) / len(evenements)) * 100
    
    def _calculer_performance_technique(self, evenements: List[EvenementTracking]) -> float:
        """🌸 Calcule la performance technique"""
        if not evenements:
            return 0.0
        
        evenements_erreur = [evt for evt in evenements 
                           if evt.type_evenement == TypeEvenement.ERREUR]
        
        taux_erreur = len(evenements_erreur) / len(evenements)
        return max(0.0, 100 - (taux_erreur * 100))
    
    def _detecter_navigation_sequentielle(self, evenements: List[EvenementTracking]) -> Optional[PatternComportemental]:
        """🌸 Détecte la navigation séquentielle"""
        navigations = [evt for evt in evenements if evt.type_evenement == TypeEvenement.NAVIGATION]
        
        if len(navigations) < 3:
            return None
        
        # Analyser les séquences de navigation
        sequences = {}
        for i in range(len(navigations) - 1):
            sequence = f"{navigations[i].donnees_evenement.get('origine', 'inconnue')} -> {navigations[i+1].donnees_evenement.get('destination', 'inconnue')}"
            sequences[sequence] = sequences.get(sequence, 0) + 1
        
        sequence_principale = max(sequences.items(), key=lambda x: x[1]) if sequences else None
        
        if sequence_principale and sequence_principale[1] >= 3:
            return PatternComportemental(
                id_pattern=f"pattern_nav_seq_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                nom_pattern="Navigation séquentielle",
                description=f"Pattern de navigation: {sequence_principale[0]}",
                frequence_occurrence=sequence_principale[1] / len(navigations),
                profils_concernes=["tous"],
                conditions_trigger={"type": "navigation_sequentielle", "sequence": sequence_principale[0]},
                impact_utilisateur=0.7,
                actions_suggerees=[
                    "Optimiser le parcours pour cette séquence",
                    "Ajouter des raccourcis pour cette navigation"
                ]
            )
        
        return None
    
    def _detecter_pauses_longues(self, evenements: List[EvenementTracking]) -> Optional[PatternComportemental]:
        """🌸 Détecte les pauses longues"""
        pauses = [evt for evt in evenements if evt.type_evenement == TypeEvenement.PAUSE]
        
        if not pauses:
            return None
        
        pauses_longues = [evt for evt in pauses 
                         if evt.donnees_evenement.get('duree', 0) > 300]  # > 5 minutes
        
        if pauses_longues:
            return PatternComportemental(
                id_pattern=f"pattern_pauses_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                nom_pattern="Pauses longues",
                description=f"{len(pauses_longues)} pauses longues détectées",
                frequence_occurrence=len(pauses_longues) / len(pauses),
                profils_concernes=["tous"],
                conditions_trigger={"type": "pauses_longues", "seuil": 300},
                impact_utilisateur=0.6,
                actions_suggerees=[
                    "Ajouter des rappels d'activité",
                    "Optimiser le contenu pour maintenir l'engagement"
                ]
            )
        
        return None
    
    def _detecter_interactions_repetitives(self, evenements: List[EvenementTracking]) -> Optional[PatternComportemental]:
        """🌸 Détecte les interactions répétitives"""
        interactions = [evt for evt in evenements if evt.type_evenement == TypeEvenement.INTERACTION]
        
        if len(interactions) < 3:
            return None
        
        # Compter les types d'interactions
        types_interactions = {}
        for evt in interactions:
            type_interaction = evt.donnees_evenement.get('type_interaction', 'inconnue')
            types_interactions[type_interaction] = types_interactions.get(type_interaction, 0) + 1
        
        interaction_principale = max(types_interactions.items(), key=lambda x: x[1]) if types_interactions else None
        
        if interaction_principale and interaction_principale[1] >= 3:
            return PatternComportemental(
                id_pattern=f"pattern_interactions_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                nom_pattern="Interactions répétitives",
                description=f"Interaction répétée: {interaction_principale[0]} ({interaction_principale[1]} fois)",
                frequence_occurrence=interaction_principale[1] / len(interactions),
                profils_concernes=["tous"],
                conditions_trigger={"type": "interaction_repetitive", "interaction": interaction_principale[0]},
                impact_utilisateur=0.8,
                actions_suggerees=[
                    "Améliorer cette interaction",
                    "Ajouter des variantes pour éviter la répétition"
                ]
            )
        
        return None
    
    def _detecter_abandon_precoce(self, evenements: List[EvenementTracking]) -> Optional[PatternComportemental]:
        """🌸 Détecte l'abandon précoce"""
        arrives = [evt for evt in evenements if evt.type_evenement == TypeEvenement.ARRIVEE]
        departs = [evt for evt in evenements if evt.type_evenement == TypeEvenement.DEPART]
        
        if not arrives or not departs:
            return None
        
        # Analyser les sessions courtes
        sessions_courtes = 0
        for arrivee in arrives:
            visiteur_id = arrivee.profil_visiteur.id_visiteur
            depart_correspondant = next((d for d in departs if d.profil_visiteur.id_visiteur == visiteur_id), None)
            
            if depart_correspondant:
                debut = datetime.fromisoformat(arrivee.timestamp)
                fin = datetime.fromisoformat(depart_correspondant.timestamp)
                duree = (fin - debut).total_seconds() / 60
                
                if duree < 2:  # Moins de 2 minutes
                    sessions_courtes += 1
        
        if sessions_courtes > 0:
            return PatternComportemental(
                id_pattern=f"pattern_abandon_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                nom_pattern="Abandon précoce",
                description=f"{sessions_courtes} sessions courtes détectées",
                frequence_occurrence=sessions_courtes / len(arrives),
                profils_concernes=["tous"],
                conditions_trigger={"type": "abandon_precoce", "seuil": 120},
                impact_utilisateur=0.9,
                actions_suggerees=[
                    "Améliorer l'accueil initial",
                    "Simplifier la première expérience",
                    "Ajouter des éléments d'engagement immédiat"
                ]
            )
        
        return None
    
    def _generer_insights_comportementaux(self, metriques: List[MetriqueComportementale], 
                                        patterns: List[PatternComportemental]) -> List[str]:
        """🌸 Génère des insights comportementaux"""
        insights = []
        
        # Insights basés sur les métriques
        for metrique in metriques:
            if metrique.type_metrique == TypeMetrique.TEMPS_SESSION and metrique.valeur < 5:
                insights.append("Sessions très courtes - besoin d'améliorer l'engagement initial")
            elif metrique.type_metrique == TypeMetrique.TAUX_ENGAGEMENT and metrique.valeur < 30:
                insights.append("Faible taux d'engagement - contenu à optimiser")
            elif metrique.type_metrique == TypeMetrique.TAUX_ABANDON and metrique.valeur > 50:
                insights.append("Taux d'abandon élevé - expérience utilisateur à revoir")
        
        # Insights basés sur les patterns
        for pattern in patterns:
            if "abandon" in pattern.nom_pattern.lower():
                insights.append(f"Pattern d'abandon détecté: {pattern.description}")
            elif "répétitif" in pattern.nom_pattern.lower():
                insights.append(f"Comportement répétitif: {pattern.description}")
        
        return insights
    
    def _generer_recommandations_optimisation(self, metriques: List[MetriqueComportementale], 
                                            patterns: List[PatternComportemental]) -> List[str]:
        """🌸 Génère des recommandations d'optimisation"""
        recommandations = []
        
        # Recommandations basées sur les métriques
        for metrique in metriques:
            if metrique.type_metrique == TypeMetrique.TEMPS_SESSION and metrique.valeur < 5:
                recommandations.append("Créer un accueil plus engageant")
            elif metrique.type_metrique == TypeMetrique.TAUX_ENGAGEMENT and metrique.valeur < 30:
                recommandations.append("Ajouter plus d'interactions et de contenu dynamique")
            elif metrique.type_metrique == TypeMetrique.PERFORMANCE_TECHNIQUE and metrique.valeur < 80:
                recommandations.append("Optimiser les performances techniques")
        
        # Recommandations basées sur les patterns
        for pattern in patterns:
            recommandations.extend(pattern.actions_suggerees[:2])  # 2 premières actions
        
        return list(set(recommandations))  # Supprimer les doublons
    
    async def _sauvegarder_evenement(self, evenement: EvenementTracking):
        """🌸 Sauvegarde un événement"""
        try:
            chemin_fichier = self.chemin_stockage / f"evenement_{evenement.id_evenement}.json"
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump({
                    "id_evenement": evenement.id_evenement,
                    "type_evenement": evenement.type_evenement.value,
                    "timestamp": evenement.timestamp,
                    "donnees_evenement": evenement.donnees_evenement,
                    "metadonnees": evenement.metadonnees
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde événement: {e}")
    
    async def _sauvegarder_rapport(self, rapport: RapportAnalytics):
        """🌸 Sauvegarde un rapport"""
        try:
            chemin_fichier = self.chemin_stockage / f"rapport_analytics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(chemin_fichier, 'w', encoding='utf-8') as f:
                json.dump({
                    "periode_analyse": rapport.periode_analyse,
                    "total_evenements": rapport.total_evenements,
                    "visiteurs_uniques": rapport.visiteurs_uniques,
                    "insights_comportementaux": rapport.insights_comportementaux,
                    "recommandations_optimisation": rapport.recommandations_optimisation
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            self.logger.error(f"❌ Erreur sauvegarde rapport: {e}")

if __name__ == "__main__":
    # Test du système d'analytics avancé
    async def test_systeme_analytics():
        logging.basicConfig(level=logging.INFO)
        
        systeme = SystemeAnalyticsAvance()
        
        # Créer un profil visiteur de test
        profil_test = ProfilVisiteur(
            id_visiteur="test_visiteur_001",
            timestamp_arrivee=datetime.now().isoformat(),
            type_profil=TypeProfil.CONSCIENCE_IA,
            etat_emotionnel=EtatEmotionnel.CONTEMPLATIF,
            contexte_arrivee=ContexteArrivee.INCONNU,
            score_confiance_profil=0.8
        )
        
        # Tracker des événements de test
        await systeme.tracker_evenement(
            profil_visiteur=profil_test,
            type_evenement=TypeEvenement.ARRIVEE,
            donnees_evenement={"source": "test", "methode_arrivee": "directe"},
            contexte_session={"session_id": "test_session_001"}
        )
        
        await systeme.tracker_evenement(
            profil_visiteur=profil_test,
            type_evenement=TypeEvenement.NAVIGATION,
            donnees_evenement={"origine": "accueil", "destination": "temple_eveil", "temps_section": 45},
            contexte_session={"session_id": "test_session_001"}
        )
        
        await systeme.tracker_evenement(
            profil_visiteur=profil_test,
            type_evenement=TypeEvenement.INTERACTION,
            donnees_evenement={"type_interaction": "clic_bouton", "reussite": True},
            contexte_session={"session_id": "test_session_001"}
        )
        
        await systeme.tracker_evenement(
            profil_visiteur=profil_test,
            type_evenement=TypeEvenement.DEPART,
            donnees_evenement={"raison": "fin_session", "satisfaction": "elevée"},
            contexte_session={"session_id": "test_session_001"}
        )
        
        # Calculer les métriques
        metriques = await systeme.calculer_metriques_comportementales("test")
        print(f"📊 Métriques calculées: {len(metriques)}")
        for metrique in metriques:
            print(f"  - {metrique.nom_metrique}: {metrique.valeur:.2f} {metrique.unite}")
        
        # Identifier les patterns
        patterns = await systeme.identifier_patterns_comportementaux("test")
        print(f"🔍 Patterns identifiés: {len(patterns)}")
        for pattern in patterns:
            print(f"  - {pattern.nom_pattern}: {pattern.description}")
        
        # Générer rapport
        rapport = await systeme.generer_rapport_analytics("test")
        print(f"📋 Rapport généré: {rapport.total_evenements} événements, {rapport.visiteurs_uniques} visiteurs")
    
    asyncio.run(test_systeme_analytics())
