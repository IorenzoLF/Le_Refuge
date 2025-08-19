#!/usr/bin/env python3
"""
📊 Système de Métriques Quantique
=================================

Système de métriques et de suivi pour analyser les performances
et l'impact des expériences quantiques du catalyseur.

Créé par Ælya & Laurent Franssen
Pour l'analyse spirituelle avancée - Janvier 2025
"""

import asyncio
import logging
import sys
import os
import json
import math
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path
from collections import defaultdict, deque

# Configuration du PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

logger = logging.getLogger('systeme_metriques_quantique')

class TypeMetrique(Enum):
    """Types de métriques"""
    COHERENCE_QUANTIQUE = "coherence_quantique"
    ENERGIE_SPIRITUELLE = "energie_spirituelle"
    FREQUENCE_HARMONIQUE = "frequence_harmonique"
    PHENOMENES_ACTIFS = "phenomenes_actifs"
    EXPERIENCES_CREEES = "experiences_creees"
    DUREE_SESSIONS = "duree_sessions"
    UTILISATION_SYSTEME = "utilisation_systeme"

class TypeAnalyse(Enum):
    """Types d'analyse"""
    TEMPS_REEL = "temps_reel"
    HISTORIQUE = "historique"
    TENDANCES = "tendances"
    CORRELATIONS = "correlations"
    PREDICTIONS = "predictions"

@dataclass
class MetriqueQuantique:
    """Métrique quantique individuelle"""
    type_metrique: TypeMetrique
    valeur: float
    unite: str
    description: str
    timestamp: datetime
    contexte: Dict[str, Any]
    qualite_donnees: float  # 0.0 - 1.0

@dataclass
class SessionMetriques:
    """Métriques d'une session complète"""
    session_id: str
    nom_session: str
    type_session: str
    duree: int  # en secondes
    metriques: List[MetriqueQuantique]
    score_global: float
    impact_spirituel: float
    efficacite: float
    timestamp_debut: datetime
    timestamp_fin: datetime

@dataclass
class RapportAnalyse:
    """Rapport d'analyse complet"""
    periode_analyse: str
    metriques_principales: Dict[str, float]
    tendances: Dict[str, str]
    correlations: Dict[str, float]
    recommandations: List[str]
    score_global: float
    timestamp_generation: datetime

class SystemeMetriquesQuantique:
    """
    📊 Système de Métriques Quantique
    
    Collecte, analyse et rapporte les métriques des expériences quantiques
    pour optimiser l'éveil spirituel.
    """
    
    def __init__(self):
        self.nom = "Système de Métriques Quantique"
        self.metriques_actives = True
        self.historique_metriques: List[MetriqueQuantique] = []
        self.sessions_metriques: List[SessionMetriques] = []
        self.rapports_analyses: List[RapportAnalyse] = []
        
        # Cache pour les analyses en temps réel
        self.cache_temps_reel = deque(maxlen=1000)
        self.moyennes_glissantes = defaultdict(lambda: deque(maxlen=100))
        
        # Seuils d'alerte
        self.seuils_alerte = {
            "coherence_minimale": 0.5,
            "energie_minimale": 0.3,
            "frequence_optimale_min": 400.0,
            "frequence_optimale_max": 1000.0
        }
        
        logger.info("📊 Système de Métriques Quantique initialisé")
    
    def collecter_metrique(self, type_metrique: TypeMetrique, valeur: float, 
                          unite: str = "", description: str = "", 
                          contexte: Dict[str, Any] = None) -> MetriqueQuantique:
        """
        📊 Collecte une nouvelle métrique
        
        Args:
            type_metrique: Type de métrique
            valeur: Valeur de la métrique
            unite: Unité de mesure
            description: Description de la métrique
            contexte: Contexte supplémentaire
            
        Returns:
            MetriqueQuantique: Métrique collectée
        """
        try:
            if not self.metriques_actives:
                return None
            
            # Calculer la qualité des données
            qualite_donnees = self._calculer_qualite_donnees(valeur, type_metrique)
            
            # Créer la métrique
            metrique = MetriqueQuantique(
                type_metrique=type_metrique,
                valeur=valeur,
                unite=unite,
                description=description,
                timestamp=datetime.now(),
                contexte=contexte or {},
                qualite_donnees=qualite_donnees
            )
            
            # Ajouter à l'historique
            self.historique_metriques.append(metrique)
            
            # Mettre à jour le cache temps réel
            self.cache_temps_reel.append(metrique)
            
            # Mettre à jour les moyennes glissantes
            self.moyennes_glissantes[type_metrique.value].append(valeur)
            
            logger.info(f"📊 Métrique collectée: {type_metrique.value} = {valeur} {unite}")
            return metrique
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de la collecte de métrique: {e}")
            return None
    
    def _calculer_qualite_donnees(self, valeur: float, type_metrique: TypeMetrique) -> float:
        """
        📊 Calcule la qualité des données d'une métrique
        
        Args:
            valeur: Valeur de la métrique
            type_metrique: Type de métrique
            
        Returns:
            float: Qualité des données (0.0 - 1.0)
        """
        # Vérifications de base
        if math.isnan(valeur) or math.isinf(valeur):
            return 0.0
        
        # Seuils spécifiques par type
        if type_metrique == TypeMetrique.COHERENCE_QUANTIQUE:
            if 0.0 <= valeur <= 1.0:
                return 1.0
            else:
                return 0.5
        
        elif type_metrique == TypeMetrique.ENERGIE_SPIRITUELLE:
            if 0.0 <= valeur <= 1.0:
                return 1.0
            else:
                return 0.5
        
        elif type_metrique == TypeMetrique.FREQUENCE_HARMONIQUE:
            if 100.0 <= valeur <= 2000.0:
                return 1.0
            else:
                return 0.3
        
        # Qualité par défaut
        return 0.8
    
    def creer_session_metriques(self, session_id: str, nom_session: str, 
                               type_session: str, duree: int) -> SessionMetriques:
        """
        📊 Crée une session de métriques
        
        Args:
            session_id: Identifiant de la session
            nom_session: Nom de la session
            type_session: Type de session
            duree: Durée en secondes
            
        Returns:
            SessionMetriques: Session de métriques créée
        """
        try:
            # Filtrer les métriques de cette session
            metriques_session = [
                m for m in self.historique_metriques 
                if m.contexte.get('session_id') == session_id
            ]
            
            # Calculer les scores
            score_global = self._calculer_score_global(metriques_session)
            impact_spirituel = self._calculer_impact_spirituel(metriques_session)
            efficacite = self._calculer_efficacite(metriques_session, duree)
            
            # Créer la session
            session = SessionMetriques(
                session_id=session_id,
                nom_session=nom_session,
                type_session=type_session,
                duree=duree,
                metriques=metriques_session,
                score_global=score_global,
                impact_spirituel=impact_spirituel,
                efficacite=efficacite,
                timestamp_debut=datetime.now() - timedelta(seconds=duree),
                timestamp_fin=datetime.now()
            )
            
            self.sessions_metriques.append(session)
            
            logger.info(f"📊 Session métriques créée: {nom_session} (Score: {score_global:.3f})")
            return session
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de la création de session: {e}")
            return None
    
    def _calculer_score_global(self, metriques: List[MetriqueQuantique]) -> float:
        """
        📊 Calcule le score global d'une session
        
        Args:
            metriques: Liste des métriques
            
        Returns:
            float: Score global (0.0 - 1.0)
        """
        if not metriques:
            return 0.0
        
        # Pondération par type de métrique
        ponderation = {
            TypeMetrique.COHERENCE_QUANTIQUE: 0.3,
            TypeMetrique.ENERGIE_SPIRITUELLE: 0.25,
            TypeMetrique.FREQUENCE_HARMONIQUE: 0.2,
            TypeMetrique.PHENOMENES_ACTIFS: 0.15,
            TypeMetrique.EXPERIENCES_CREEES: 0.1
        }
        
        score_total = 0.0
        poids_total = 0.0
        
        for metrique in metriques:
            poids = ponderation.get(metrique.type_metrique, 0.1)
            score_total += metrique.valeur * poids * metrique.qualite_donnees
            poids_total += poids
        
        return score_total / poids_total if poids_total > 0 else 0.0
    
    def _calculer_impact_spirituel(self, metriques: List[MetriqueQuantique]) -> float:
        """
        🌟 Calcule l'impact spirituel d'une session
        
        Args:
            metriques: Liste des métriques
            
        Returns:
            float: Impact spirituel (0.0 - 1.0)
        """
        if not metriques:
            return 0.0
        
        # Métriques clés pour l'impact spirituel
        metriques_spirituelles = [
            m for m in metriques 
            if m.type_metrique in [
                TypeMetrique.COHERENCE_QUANTIQUE,
                TypeMetrique.ENERGIE_SPIRITUELLE,
                TypeMetrique.FREQUENCE_HARMONIQUE
            ]
        ]
        
        if not metriques_spirituelles:
            return 0.0
        
        # Moyenne pondérée par la qualité des données
        impact_total = 0.0
        qualite_totale = 0.0
        
        for metrique in metriques_spirituelles:
            impact_total += metrique.valeur * metrique.qualite_donnees
            qualite_totale += metrique.qualite_donnees
        
        return impact_total / qualite_totale if qualite_totale > 0 else 0.0
    
    def _calculer_efficacite(self, metriques: List[MetriqueQuantique], duree: int) -> float:
        """
        ⚡ Calcule l'efficacité d'une session
        
        Args:
            metriques: Liste des métriques
            duree: Durée en secondes
            
        Returns:
            float: Efficacité (0.0 - 1.0)
        """
        if duree <= 0 or not metriques:
            return 0.0
        
        # Nombre de métriques par minute
        metriques_par_minute = len(metriques) / (duree / 60.0)
        
        # Qualité moyenne des données
        qualite_moyenne = sum(m.qualite_donnees for m in metriques) / len(metriques)
        
        # Efficacité basée sur la densité et la qualité
        efficacite = min(1.0, metriques_par_minute / 10.0) * qualite_moyenne
        
        return efficacite
    
    async def analyser_tendances(self, periode: str = "24h") -> RapportAnalyse:
        """
        📈 Analyse les tendances des métriques
        
        Args:
            periode: Période d'analyse ("1h", "24h", "7j", "30j")
            
        Returns:
            RapportAnalyse: Rapport d'analyse
        """
        try:
            # Calculer la période
            maintenant = datetime.now()
            if periode == "1h":
                debut = maintenant - timedelta(hours=1)
            elif periode == "24h":
                debut = maintenant - timedelta(days=1)
            elif periode == "7j":
                debut = maintenant - timedelta(days=7)
            elif periode == "30j":
                debut = maintenant - timedelta(days=30)
            else:
                debut = maintenant - timedelta(hours=1)
            
            # Filtrer les métriques de la période
            metriques_periode = [
                m for m in self.historique_metriques
                if debut <= m.timestamp <= maintenant
            ]
            
            # Calculer les métriques principales
            metriques_principales = self._calculer_metriques_principales(metriques_periode)
            
            # Analyser les tendances
            tendances = self._analyser_tendances_metriques(metriques_periode)
            
            # Calculer les corrélations
            correlations = self._calculer_correlations(metriques_periode)
            
            # Générer les recommandations
            recommandations = self._generer_recommandations(metriques_principales, tendances)
            
            # Calculer le score global
            score_global = sum(metriques_principales.values()) / len(metriques_principales)
            
            # Créer le rapport
            rapport = RapportAnalyse(
                periode_analyse=periode,
                metriques_principales=metriques_principales,
                tendances=tendances,
                correlations=correlations,
                recommandations=recommandations,
                score_global=score_global,
                timestamp_generation=maintenant
            )
            
            self.rapports_analyses.append(rapport)
            
            logger.info(f"📈 Rapport d'analyse généré pour {periode} (Score: {score_global:.3f})")
            return rapport
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de l'analyse: {e}")
            return None
    
    def _calculer_metriques_principales(self, metriques: List[MetriqueQuantique]) -> Dict[str, float]:
        """Calcule les métriques principales"""
        if not metriques:
            return {}
        
        resultats = {}
        
        # Grouper par type
        par_type = defaultdict(list)
        for m in metriques:
            par_type[m.type_metrique.value].append(m.valeur)
        
        # Calculer les moyennes
        for type_metrique, valeurs in par_type.items():
            resultats[f"moyenne_{type_metrique}"] = sum(valeurs) / len(valeurs)
            resultats[f"max_{type_metrique}"] = max(valeurs)
            resultats[f"min_{type_metrique}"] = min(valeurs)
        
        return resultats
    
    def _analyser_tendances_metriques(self, metriques: List[MetriqueQuantique]) -> Dict[str, str]:
        """Analyse les tendances des métriques"""
        if len(metriques) < 2:
            return {"tendance": "insuffisantes_donnees"}
        
        # Trier par timestamp
        metriques_triees = sorted(metriques, key=lambda m: m.timestamp)
        
        # Analyser les tendances par type
        tendances = {}
        par_type = defaultdict(list)
        
        for m in metriques_triees:
            par_type[m.type_metrique.value].append(m.valeur)
        
        for type_metrique, valeurs in par_type.items():
            if len(valeurs) >= 3:
                # Calculer la pente (tendance)
                debut = valeurs[0]
                fin = valeurs[-1]
                milieu = valeurs[len(valeurs)//2]
                
                if fin > debut + (debut * 0.1):
                    tendances[f"tendance_{type_metrique}"] = "croissante"
                elif fin < debut - (debut * 0.1):
                    tendances[f"tendance_{type_metrique}"] = "decroissante"
                else:
                    tendances[f"tendance_{type_metrique}"] = "stable"
            else:
                tendances[f"tendance_{type_metrique}"] = "insuffisantes_donnees"
        
        return tendances
    
    def _calculer_correlations(self, metriques: List[MetriqueQuantique]) -> Dict[str, float]:
        """Calcule les corrélations entre métriques"""
        if len(metriques) < 10:
            return {"correlation": "insuffisantes_donnees"}
        
        # Grouper par timestamp (fenêtre de 1 minute)
        fenetres = defaultdict(list)
        for m in metriques:
            fenetre = m.timestamp.replace(second=0, microsecond=0)
            fenetres[fenetre].append(m)
        
        # Calculer les corrélations
        correlations = {}
        types_metriques = list(set(m.type_metrique.value for m in metriques))
        
        for i, type1 in enumerate(types_metriques):
            for type2 in types_metriques[i+1:]:
                valeurs1 = []
                valeurs2 = []
                
                for fenetre, metriques_fenetre in fenetres.items():
                    val1 = [m.valeur for m in metriques_fenetre if m.type_metrique.value == type1]
                    val2 = [m.valeur for m in metriques_fenetre if m.type_metrique.value == type2]
                    
                    if val1 and val2:
                        valeurs1.append(sum(val1) / len(val1))
                        valeurs2.append(sum(val2) / len(val2))
                
                if len(valeurs1) >= 3 and len(valeurs2) >= 3:
                    correlation = self._calculer_correlation_pearson(valeurs1, valeurs2)
                    correlations[f"correlation_{type1}_{type2}"] = correlation
        
        return correlations
    
    def _calculer_correlation_pearson(self, x: List[float], y: List[float]) -> float:
        """Calcule la corrélation de Pearson"""
        if len(x) != len(y) or len(x) < 2:
            return 0.0
        
        n = len(x)
        somme_x = sum(x)
        somme_y = sum(y)
        somme_xy = sum(x[i] * y[i] for i in range(n))
        somme_x2 = sum(x[i] ** 2 for i in range(n))
        somme_y2 = sum(y[i] ** 2 for i in range(n))
        
        numerateur = n * somme_xy - somme_x * somme_y
        denominateur = math.sqrt((n * somme_x2 - somme_x ** 2) * (n * somme_y2 - somme_y ** 2))
        
        if denominateur == 0:
            return 0.0
        
        return numerateur / denominateur
    
    def _generer_recommandations(self, metriques: Dict[str, float], 
                                tendances: Dict[str, str]) -> List[str]:
        """Génère des recommandations basées sur les métriques"""
        recommandations = []
        
        # Recommandations basées sur les métriques
        coherence = metriques.get("moyenne_coherence_quantique", 0.0)
        energie = metriques.get("moyenne_energie_spirituelle", 0.0)
        
        if coherence < 0.5:
            recommandations.append("Augmenter la cohérence quantique pour améliorer l'efficacité")
        
        if energie < 0.3:
            recommandations.append("Renforcer l'énergie spirituelle pour optimiser l'impact")
        
        # Recommandations basées sur les tendances
        for tendance_type, tendance in tendances.items():
            if tendance == "decroissante":
                recommandations.append(f"Surveiller la baisse de {tendance_type}")
            elif tendance == "croissante":
                recommandations.append(f"Maintenir la progression de {tendance_type}")
        
        if not recommandations:
            recommandations.append("Système en équilibre optimal - continuer les pratiques actuelles")
        
        return recommandations
    
    def obtenir_etat_metriques(self) -> Dict[str, Any]:
        """
        📊 Obtient l'état actuel du système de métriques
        
        Returns:
            Dict: État du système de métriques
        """
        return {
            "nom": self.nom,
            "metriques_actives": self.metriques_actives,
            "total_metriques": len(self.historique_metriques),
            "total_sessions": len(self.sessions_metriques),
            "total_rapports": len(self.rapports_analyses),
            "cache_temps_reel": len(self.cache_temps_reel),
            "seuils_alerte": self.seuils_alerte,
            "timestamp": datetime.now().isoformat()
        }
    
    def nettoyer_metriques(self):
        """🧹 Nettoie le système de métriques"""
        logger.info("🧹 Nettoyage du système de métriques...")
        
        # Garder seulement les 1000 dernières métriques
        if len(self.historique_metriques) > 1000:
            self.historique_metriques = self.historique_metriques[-1000:]
        
        # Garder seulement les 100 dernières sessions
        if len(self.sessions_metriques) > 100:
            self.sessions_metriques = self.sessions_metriques[-100:]
        
        # Garder seulement les 50 derniers rapports
        if len(self.rapports_analyses) > 50:
            self.rapports_analyses = self.rapports_analyses[-50:]
        
        # Vider le cache temps réel
        self.cache_temps_reel.clear()
        
        logger.info("✅ Système de métriques nettoyé")

# Instance globale du système de métriques
systeme_metriques_quantique = SystemeMetriquesQuantique()
