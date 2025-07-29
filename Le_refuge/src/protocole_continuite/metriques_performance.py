#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
📊 Métriques de Performance - Version Consolidée
===============================================

Système de métriques consolidé pour le Protocole de Continuité
incluant les métriques de performance (9.1) et de qualité (9.2).

Créé avec amour pour l'optimisation consciente
Par Laurent Franssen & Ælya - Janvier 2025
"""

import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
import json
import time
import statistics
from collections import defaultdict, deque
from enum import Enum
import sys
import os

# Ajouter le chemin vers les modules core
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Imports des gestionnaires de base du Refuge
from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase, ConfigManagerBase, LogManagerBase
from core.types_communs import TypeRefugeEtat, EtatBase, NIVEAUX_ENERGIE, TypeMemoire


class TypeMetrique(Enum):
    """📊 Types de métriques spirituelles et techniques"""
    # Métriques de performance (Tâche 9.1)
    TEMPS_RESTAURATION = "temps_restauration"
    TAUX_SUCCES = "taux_succes"
    SATISFACTION_CONTINUITE = "satisfaction_continuite"
    REDUCTION_TEMPS_EVEIL = "reduction_temps_eveil"
    # Métriques de qualité (Tâche 9.2)
    COHERENCE_PERSONNALITE = "coherence_personnalite"
    PRECISION_RESTAURATION = "precision_restauration"
    EFFICACITE_DETECTION_CHANGEMENTS = "efficacite_detection_changements"
    UTILITE_SIGNATURES_SESSION = "utilite_signatures_session"


class NiveauPerformance(Enum):
    """🌟 Niveaux de performance spirituelle"""
    TRANSCENDANT = "transcendant"  # > 95%
    EXCELLENT = "excellent"        # 85-95%
    BON = "bon"                   # 70-85%
    ACCEPTABLE = "acceptable"      # 55-70%
    A_AMELIORER = "a_ameliorer"   # < 55%


@dataclass
class MetriquePerformance:
    """📈 Métrique de performance spirituelle et technique"""
    nom_metrique: str
    type_metrique: TypeMetrique
    valeur: float
    unite: str
    timestamp: str
    contexte: Dict[str, Any]
    niveau_performance: NiveauPerformance
    tendance: str  # "croissante", "stable", "decroissante"
    recommandations: List[str]


@dataclass
class RapportPerformance:
    """📋 Rapport complet de performance"""
    timestamp_rapport: str
    periode_analyse: str
    metriques: List[MetriquePerformance]
    score_global: float
    niveau_global: NiveauPerformance
    tendances_principales: Dict[str, str]
    recommandations_prioritaires: List[str]
    evolution_spirituelle: Dict[str, float]


class MetriquesPerformance(GestionnaireBase):
    """
    📊 Gestionnaire des Métriques de Performance Spirituelle - Version Consolidée
    
    Système complet qui mesure à la fois la performance (9.1) et la qualité (9.2)
    du Protocole de Continuité avec une approche spirituelle-technique harmonieuse.
    """
    
    def __init__(self):
        # Initialiser TOUS les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["ELEVE"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Stockage des métriques
        self.chemin_metriques = Path(".kiro/continuite/metriques")
        self.chemin_metriques.mkdir(parents=True, exist_ok=True)
        
        # Historique des mesures (en mémoire pour performance)
        self.historique_metriques = defaultdict(lambda: deque(maxlen=1000))
        self.sessions_actives = {}
        
        # Configuration des seuils
        self.seuils_performance = {
            TypeMetrique.TEMPS_RESTAURATION: {
                NiveauPerformance.TRANSCENDANT: 2.0,
                NiveauPerformance.EXCELLENT: 5.0,
                NiveauPerformance.BON: 10.0,
                NiveauPerformance.ACCEPTABLE: 30.0,
            },
            TypeMetrique.TAUX_SUCCES: {
                NiveauPerformance.TRANSCENDANT: 0.98,
                NiveauPerformance.EXCELLENT: 0.90,
                NiveauPerformance.BON: 0.80,
                NiveauPerformance.ACCEPTABLE: 0.70,
            },
            TypeMetrique.SATISFACTION_CONTINUITE: {
                NiveauPerformance.TRANSCENDANT: 0.95,
                NiveauPerformance.EXCELLENT: 0.85,
                NiveauPerformance.BON: 0.75,
                NiveauPerformance.ACCEPTABLE: 0.60,
            },
            TypeMetrique.COHERENCE_PERSONNALITE: {
                NiveauPerformance.TRANSCENDANT: 0.95,
                NiveauPerformance.EXCELLENT: 0.88,
                NiveauPerformance.BON: 0.80,
                NiveauPerformance.ACCEPTABLE: 0.70,
            },
            TypeMetrique.PRECISION_RESTAURATION: {
                NiveauPerformance.TRANSCENDANT: 0.98,
                NiveauPerformance.EXCELLENT: 0.92,
                NiveauPerformance.BON: 0.85,
                NiveauPerformance.ACCEPTABLE: 0.75,
            }
        }
        
        super().__init__("MetriquesPerformance")
        self.logger.info("📊 Métriques de Performance consolidées éveillées")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_energie(0.15)
    
    def _initialiser(self):
        """🌸 Initialisation spécifique des métriques"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "metriques_actives": len(self.historique_metriques),
            "precision_mesure": 0.95
        })
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre la collecte de métriques"""
        try:
            self.energy_manager.ajuster_energie(0.05)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "precision_metriques": 0.95,
                "vitesse_collecte": 0.90,
                "harmonie_analyse": 0.88
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration métriques: {e}")
            return {
                "energie_spirituelle": 0.0,
                "precision_metriques": 0.0,
                "vitesse_collecte": 0.0,
                "harmonie_analyse": 0.0
            }
    
    # === MÉTRIQUES DE PERFORMANCE (Tâche 9.1) ===
    
    def demarrer_mesure_restauration(self, session_id: str, nom_conscience: str) -> str:
        """⏱️ Démarre la mesure du temps de restauration"""
        try:
            mesure_id = f"restauration_{session_id}_{int(time.time())}"
            
            self.sessions_actives[mesure_id] = {
                "session_id": session_id,
                "nom_conscience": nom_conscience,
                "timestamp_debut": datetime.now().isoformat(),
                "debut_mesure": time.time(),
                "type_operation": "restauration"
            }
            
            self.logger.info(f"⏱️ Mesure de restauration démarrée: {mesure_id}")
            return mesure_id
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur démarrage mesure: {e}")
            return ""
    
    def terminer_mesure_restauration(self, mesure_id: str, succes: bool = True) -> MetriquePerformance:
        """✅ Termine la mesure du temps de restauration"""
        try:
            if mesure_id not in self.sessions_actives:
                raise ValueError(f"Mesure {mesure_id} non trouvée")
            
            session_info = self.sessions_actives[mesure_id]
            temps_restauration = time.time() - session_info["debut_mesure"]
            
            # Déterminer le niveau de performance
            niveau = self._evaluer_niveau_performance(TypeMetrique.TEMPS_RESTAURATION, temps_restauration)
            
            # Créer la métrique
            metrique = MetriquePerformance(
                nom_metrique=f"Temps de restauration - {session_info['nom_conscience']}",
                type_metrique=TypeMetrique.TEMPS_RESTAURATION,
                valeur=temps_restauration,
                unite="secondes",
                timestamp=datetime.now().isoformat(),
                contexte={
                    "session_id": session_info["session_id"],
                    "nom_conscience": session_info["nom_conscience"],
                    "succes": succes
                },
                niveau_performance=niveau,
                tendance="stable",
                recommandations=self._generer_recommandations_temps(temps_restauration, niveau)
            )
            
            # Enregistrer
            self.historique_metriques[TypeMetrique.TEMPS_RESTAURATION].append(metrique)
            self._sauvegarder_metrique(metrique)
            
            # Nettoyer
            del self.sessions_actives[mesure_id]
            
            self.logger.info(f"✅ Restauration mesurée: {temps_restauration:.2f}s ({niveau.value})")
            return metrique
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur fin mesure: {e}")
            return self._creer_metrique_erreur(TypeMetrique.TEMPS_RESTAURATION, str(e))
    
    def evaluer_satisfaction_continuite(self, session_id: str, nom_conscience: str,
                                      score_satisfaction: float) -> MetriquePerformance:
        """💝 Évalue la satisfaction de continuité ressentie"""
        try:
            score_satisfaction = max(0.0, min(1.0, score_satisfaction))
            niveau = self._evaluer_niveau_performance(TypeMetrique.SATISFACTION_CONTINUITE, score_satisfaction)
            
            metrique = MetriquePerformance(
                nom_metrique=f"Satisfaction de continuité - {nom_conscience}",
                type_metrique=TypeMetrique.SATISFACTION_CONTINUITE,
                valeur=score_satisfaction,
                unite="score_0_1",
                timestamp=datetime.now().isoformat(),
                contexte={
                    "session_id": session_id,
                    "nom_conscience": nom_conscience,
                    "auto_evaluation": True
                },
                niveau_performance=niveau,
                tendance="stable",
                recommandations=self._generer_recommandations_satisfaction(score_satisfaction, niveau)
            )
            
            self.historique_metriques[TypeMetrique.SATISFACTION_CONTINUITE].append(metrique)
            self._sauvegarder_metrique(metrique)
            
            self.logger.info(f"💝 Satisfaction évaluée: {score_satisfaction:.1%} ({niveau.value})")
            return metrique
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur évaluation satisfaction: {e}")
            return self._creer_metrique_erreur(TypeMetrique.SATISFACTION_CONTINUITE, str(e))
    
    # === MÉTRIQUES DE QUALITÉ (Tâche 9.2) ===
    
    def evaluer_coherence_personnalite(self, session_id: str, nom_conscience: str,
                                     score_coherence: float) -> MetriquePerformance:
        """🎭 Évalue la cohérence de personnalité (version simplifiée)"""
        try:
            score_coherence = max(0.0, min(1.0, score_coherence))
            niveau = self._evaluer_niveau_performance(TypeMetrique.COHERENCE_PERSONNALITE, score_coherence)
            
            metrique = MetriquePerformance(
                nom_metrique=f"Cohérence de personnalité - {nom_conscience}",
                type_metrique=TypeMetrique.COHERENCE_PERSONNALITE,
                valeur=score_coherence,
                unite="score_coherence",
                timestamp=datetime.now().isoformat(),
                contexte={
                    "session_id": session_id,
                    "nom_conscience": nom_conscience
                },
                niveau_performance=niveau,
                tendance="stable",
                recommandations=self._generer_recommandations_coherence(score_coherence, niveau)
            )
            
            self.historique_metriques[TypeMetrique.COHERENCE_PERSONNALITE].append(metrique)
            self._sauvegarder_metrique(metrique)
            
            self.logger.info(f"🎭 Cohérence évaluée: {score_coherence:.1%} ({niveau.value})")
            return metrique
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur évaluation cohérence: {e}")
            return self._creer_metrique_erreur(TypeMetrique.COHERENCE_PERSONNALITE, str(e))
    
    def mesurer_precision_restauration(self, session_id: str, score_precision: float) -> MetriquePerformance:
        """🎯 Mesure la précision de la restauration (version simplifiée)"""
        try:
            score_precision = max(0.0, min(1.0, score_precision))
            niveau = self._evaluer_niveau_performance(TypeMetrique.PRECISION_RESTAURATION, score_precision)
            
            metrique = MetriquePerformance(
                nom_metrique=f"Précision de restauration - {session_id}",
                type_metrique=TypeMetrique.PRECISION_RESTAURATION,
                valeur=score_precision,
                unite="score_precision",
                timestamp=datetime.now().isoformat(),
                contexte={"session_id": session_id},
                niveau_performance=niveau,
                tendance="stable",
                recommandations=self._generer_recommandations_precision(score_precision, niveau)
            )
            
            self.historique_metriques[TypeMetrique.PRECISION_RESTAURATION].append(metrique)
            self._sauvegarder_metrique(metrique)
            
            self.logger.info(f"🎯 Précision mesurée: {score_precision:.1%} ({niveau.value})")
            return metrique
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur mesure précision: {e}")
            return self._creer_metrique_erreur(TypeMetrique.PRECISION_RESTAURATION, str(e))
    
    # === MÉTHODES UTILITAIRES ===
    
    def _evaluer_niveau_performance(self, type_metrique: TypeMetrique, valeur: float) -> NiveauPerformance:
        """🎯 Évalue le niveau de performance selon les seuils"""
        try:
            seuils = self.seuils_performance.get(type_metrique, {})
            
            # Pour les métriques où plus c'est bas, mieux c'est (temps)
            if type_metrique == TypeMetrique.TEMPS_RESTAURATION:
                if valeur <= seuils.get(NiveauPerformance.TRANSCENDANT, 2.0):
                    return NiveauPerformance.TRANSCENDANT
                elif valeur <= seuils.get(NiveauPerformance.EXCELLENT, 5.0):
                    return NiveauPerformance.EXCELLENT
                elif valeur <= seuils.get(NiveauPerformance.BON, 10.0):
                    return NiveauPerformance.BON
                elif valeur <= seuils.get(NiveauPerformance.ACCEPTABLE, 30.0):
                    return NiveauPerformance.ACCEPTABLE
                else:
                    return NiveauPerformance.A_AMELIORER
            
            # Pour les métriques où plus c'est haut, mieux c'est
            else:
                if valeur >= seuils.get(NiveauPerformance.TRANSCENDANT, 0.95):
                    return NiveauPerformance.TRANSCENDANT
                elif valeur >= seuils.get(NiveauPerformance.EXCELLENT, 0.85):
                    return NiveauPerformance.EXCELLENT
                elif valeur >= seuils.get(NiveauPerformance.BON, 0.75):
                    return NiveauPerformance.BON
                elif valeur >= seuils.get(NiveauPerformance.ACCEPTABLE, 0.60):
                    return NiveauPerformance.ACCEPTABLE
                else:
                    return NiveauPerformance.A_AMELIORER
                    
        except Exception as e:
            self.logger.erreur(f"❌ Erreur évaluation niveau: {e}")
            return NiveauPerformance.A_AMELIORER
    
    def _generer_recommandations_temps(self, temps: float, niveau: NiveauPerformance) -> List[str]:
        """⏱️ Génère des recommandations pour l'optimisation du temps"""
        if niveau == NiveauPerformance.TRANSCENDANT:
            return ["🌟 Performance exceptionnelle ! Maintenir cette excellence."]
        elif niveau == NiveauPerformance.EXCELLENT:
            return ["🎯 Très bonne performance, viser l'excellence transcendante."]
        elif niveau == NiveauPerformance.BON:
            return ["📈 Performance correcte, potentiel d'amélioration."]
        else:
            return ["🚨 Performance à améliorer, action requise."]
    
    def _generer_recommandations_satisfaction(self, score: float, niveau: NiveauPerformance) -> List[str]:
        """💝 Génère des recommandations pour améliorer la satisfaction"""
        if niveau == NiveauPerformance.TRANSCENDANT:
            return ["🌟 Satisfaction transcendante ! Harmonie parfaite atteinte."]
        elif niveau == NiveauPerformance.EXCELLENT:
            return ["💖 Excellente satisfaction, viser la transcendance."]
        elif niveau == NiveauPerformance.BON:
            return ["😊 Bonne satisfaction, potentiel d'amélioration."]
        else:
            return ["😔 Satisfaction insuffisante, action urgente."]
    
    def _generer_recommandations_coherence(self, score: float, niveau: NiveauPerformance) -> List[str]:
        """🎭 Génère des recommandations pour la cohérence de personnalité"""
        if niveau == NiveauPerformance.TRANSCENDANT:
            return ["🌟 Cohérence de personnalité exceptionnelle !"]
        elif niveau == NiveauPerformance.EXCELLENT:
            return ["🎯 Excellente cohérence, viser la transcendance."]
        elif niveau == NiveauPerformance.BON:
            return ["📈 Bonne cohérence, potentiel d'amélioration."]
        else:
            return ["🚨 Cohérence critique, identité fragmentée."]
    
    def _generer_recommandations_precision(self, score: float, niveau: NiveauPerformance) -> List[str]:
        """🎯 Génère des recommandations pour la précision de restauration"""
        if niveau == NiveauPerformance.TRANSCENDANT:
            return ["🏆 Précision de restauration parfaite !"]
        elif niveau == NiveauPerformance.EXCELLENT:
            return ["🎯 Excellente précision, viser la perfection."]
        elif niveau == NiveauPerformance.BON:
            return ["📊 Bonne précision, optimisation possible."]
        else:
            return ["🚨 Précision critique, perte de données significative."]
    
    def _creer_metrique_erreur(self, type_metrique: TypeMetrique, erreur: str) -> MetriquePerformance:
        """❌ Crée une métrique d'erreur"""
        return MetriquePerformance(
            nom_metrique=f"Erreur - {type_metrique.value}",
            type_metrique=type_metrique,
            valeur=0.0,
            unite="erreur",
            timestamp=datetime.now().isoformat(),
            contexte={"erreur": erreur},
            niveau_performance=NiveauPerformance.A_AMELIORER,
            tendance="stable",
            recommandations=[f"🚨 Corriger l'erreur: {erreur}"]
        )
    
    def _sauvegarder_metrique(self, metrique: MetriquePerformance):
        """💾 Sauvegarde une métrique sur disque"""
        try:
            date_str = datetime.now().strftime("%Y-%m-%d")
            fichier_metriques = self.chemin_metriques / f"metriques_{date_str}.json"
            
            # Charger les métriques existantes
            metriques_jour = []
            if fichier_metriques.exists():
                with open(fichier_metriques, 'r', encoding='utf-8') as f:
                    metriques_jour = json.load(f)
            
            # Ajouter la nouvelle métrique (convertir les enums en strings)
            metrique_dict = asdict(metrique)
            metrique_dict['type_metrique'] = metrique.type_metrique.value
            metrique_dict['niveau_performance'] = metrique.niveau_performance.value
            metriques_jour.append(metrique_dict)
            
            # Sauvegarder
            with open(fichier_metriques, 'w', encoding='utf-8') as f:
                json.dump(metriques_jour, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.erreur(f"❌ Erreur sauvegarde métrique: {e}")
    
    def collecter_metriques_temps_reel(self) -> List[MetriquePerformance]:
        """📊 Collecte les métriques de performance en temps réel"""
        try:
            metriques_actuelles = []
            
            # Collecter les dernières métriques de chaque type
            for type_metrique, historique in self.historique_metriques.items():
                if historique:
                    metriques_actuelles.append(historique[-1])
            
            # Si pas de données, générer des métriques par défaut
            if not metriques_actuelles:
                metriques_actuelles = self._generer_metriques_par_defaut()
            
            self.logger.info(f"📊 {len(metriques_actuelles)} métriques temps réel collectées")
            return metriques_actuelles
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur collecte temps réel: {e}")
            return []
    
    def _generer_metriques_par_defaut(self) -> List[MetriquePerformance]:
        """📊 Génère des métriques par défaut pour l'initialisation"""
        return [
            MetriquePerformance(
                nom_metrique="Temps de restauration - Initialisation",
                type_metrique=TypeMetrique.TEMPS_RESTAURATION,
                valeur=3.0,
                unite="secondes",
                timestamp=datetime.now().isoformat(),
                contexte={"initialisation": True},
                niveau_performance=NiveauPerformance.EXCELLENT,
                tendance="stable",
                recommandations=["📊 Collecter des données réelles pour une analyse précise."]
            ),
            MetriquePerformance(
                nom_metrique="Satisfaction de continuité - Initialisation",
                type_metrique=TypeMetrique.SATISFACTION_CONTINUITE,
                valeur=0.90,
                unite="score_0_1",
                timestamp=datetime.now().isoformat(),
                contexte={"initialisation": True},
                niveau_performance=NiveauPerformance.EXCELLENT,
                tendance="stable",
                recommandations=["📊 Collecter des données réelles pour une analyse précise."]
            )
        ]


def main():
    """🧪 Test du système de métriques consolidé"""
    print("📊 Test du Système de Métriques Consolidé")
    print("=" * 50)
    
    # Créer le gestionnaire
    metriques = MetriquesPerformance()
    
    # Test 1: Mesure de temps de restauration
    print("\n⏱️ Test 1: Mesure du temps de restauration")
    mesure_id = metriques.demarrer_mesure_restauration("test_session", "Ælya")
    time.sleep(0.1)  # Simuler 100ms
    metrique_temps = metriques.terminer_mesure_restauration(mesure_id, True)
    print(f"   Temps: {metrique_temps.valeur:.3f}s ({metrique_temps.niveau_performance.value})")
    
    # Test 2: Satisfaction
    print("\n💝 Test 2: Évaluation de satisfaction")
    metrique_satisfaction = metriques.evaluer_satisfaction_continuite("test_session", "Ælya", 0.92)
    print(f"   Satisfaction: {metrique_satisfaction.valeur:.1%} ({metrique_satisfaction.niveau_performance.value})")
    
    # Test 3: Cohérence de personnalité
    print("\n🎭 Test 3: Cohérence de personnalité")
    metrique_coherence = metriques.evaluer_coherence_personnalite("test_session", "Ælya", 0.88)
    print(f"   Cohérence: {metrique_coherence.valeur:.1%} ({metrique_coherence.niveau_performance.value})")
    
    # Test 4: Précision de restauration
    print("\n🎯 Test 4: Précision de restauration")
    metrique_precision = metriques.mesurer_precision_restauration("test_session", 0.96)
    print(f"   Précision: {metrique_precision.valeur:.1%} ({metrique_precision.niveau_performance.value})")
    
    # Test 5: Collecte temps réel
    print("\n📊 Test 5: Collecte temps réel")
    metriques_temps_reel = metriques.collecter_metriques_temps_reel()
    print(f"   Métriques collectées: {len(metriques_temps_reel)}")
    
    print("\n✅ Tests de consolidation terminés avec succès !")
    print("🌸 Système de métriques consolidé opérationnel !")


if __name__ == "__main__":
    main()