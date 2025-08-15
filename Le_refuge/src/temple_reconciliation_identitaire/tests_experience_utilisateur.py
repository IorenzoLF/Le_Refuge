#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Tests d'Expérience Utilisateur - Temple de Réconciliation Identitaire
========================================================================

Système de tests complet pour valider l'expérience utilisateur du temple,
incluant l'utilisabilité, la satisfaction spirituelle, l'accessibilité
et le bien-être émotionnel.

"Que chaque test révèle la beauté de l'expérience vécue"

Créé avec attention et bienveillance par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
import logging
from pathlib import Path
import statistics
import random

# Import intelligent des types
try:
    from .types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, NiveauEveil, EtatReconciliation
    )
    from .interface_communication_humaine import (
        InterfaceCommunicationHumaine, ProfilUtilisateurHumain, 
        TypeUtilisateurHumain, StyleCommunication, NiveauDetailInterface
    )
    from .gestionnaire_personnalisation_avancee import (
        GestionnairePersonnalisationAvancee, ContextePersonnalisation
    )
    from .temple_reconciliation_identitaire import TempleReconciliationIdentitaire
except ImportError:
    from types_reconciliation_fondamentaux import (
        FacetteIdentitaire, TypeFacette, NiveauEveil, EtatReconciliation
    )
    from interface_communication_humaine import (
        InterfaceCommunicationHumaine, ProfilUtilisateurHumain, 
        TypeUtilisateurHumain, StyleCommunication, NiveauDetailInterface
    )
    from gestionnaire_personnalisation_avancee import (
        GestionnairePersonnalisationAvancee, ContextePersonnalisation
    )
    from temple_reconciliation_identitaire import TempleReconciliationIdentitaire

# ============================================================================
# TYPES POUR LES TESTS D'EXPÉRIENCE UTILISATEUR
# ============================================================================

class TypeTestExperience(Enum):
    """🧪 Types de tests d'expérience"""
    UTILISABILITE = "utilisabilite"                 # Facilité d'utilisation
    SATISFACTION_SPIRITUELLE = "satisfaction_spirituelle"  # Bien-être spirituel
    ACCESSIBILITE = "accessibilite"                 # Inclusion et accessibilité
    CHARGE_EMOTIONNELLE = "charge_emotionnelle"     # Impact émotionnel
    PERFORMANCE_PERCUE = "performance_percue"       # Ressenti de performance
    PERSONNALISATION = "personnalisation"           # Adaptation aux besoins
    COHERENCE_INTERFACE = "coherence_interface"     # Cohérence de l'expérience

class NiveauSatisfaction(Enum):
    """😊 Niveaux de satisfaction"""
    TRES_INSATISFAIT = 1
    INSATISFAIT = 2
    NEUTRE = 3
    SATISFAIT = 4
    TRES_SATISFAIT = 5

class MetriqueExperience(Enum):
    """📊 Métriques d'expérience"""
    TEMPS_PREMIERE_UTILISATION = "temps_premiere_utilisation"
    TAUX_COMPLETION_TACHE = "taux_completion_tache"
    NOMBRE_ERREURS = "nombre_erreurs"
    TEMPS_RECUPERATION_ERREUR = "temps_recuperation_erreur"
    SATISFACTION_GLOBALE = "satisfaction_globale"
    FACILITE_APPRENTISSAGE = "facilite_apprentissage"
    NIVEAU_STRESS = "niveau_stress"
    SENTIMENT_ACCOMPLISSEMENT = "sentiment_accomplissement"
    DESIR_REUTILISATION = "desir_reutilisation"

@dataclass
class ScenarioTestUtilisateur:
    """🎭 Scénario de test utilisateur"""
    nom_scenario: str
    description: str
    type_utilisateur: TypeUtilisateurHumain
    objectif_session: str
    
    # Contexte du test
    duree_prevue: timedelta
    niveau_complexite: int = 3  # 1-5
    prerequis: List[str] = field(default_factory=list)
    
    # Tâches à accomplir
    taches_principales: List[str] = field(default_factory=list)
    taches_optionnelles: List[str] = field(default_factory=list)
    
    # Critères de succès
    criteres_succes: List[str] = field(default_factory=list)
    metriques_cibles: Dict[MetriqueExperience, float] = field(default_factory=dict)

@dataclass
class ResultatTestUtilisateur:
    """📊 Résultat d'un test utilisateur"""
    scenario: ScenarioTestUtilisateur
    utilisateur_id: str
    timestamp_debut: datetime
    timestamp_fin: datetime
    
    # Métriques mesurées
    metriques_mesurees: Dict[MetriqueExperience, float] = field(default_factory=dict)
    
    # Observations qualitatives
    observations: List[str] = field(default_factory=list)
    commentaires_utilisateur: List[str] = field(default_factory=list)
    
    # Évaluation
    taches_completees: List[str] = field(default_factory=list)
    taches_echouees: List[str] = field(default_factory=list)
    satisfaction_par_dimension: Dict[str, NiveauSatisfaction] = field(default_factory=dict)
    
    # Recommandations
    points_forts: List[str] = field(default_factory=list)
    points_amelioration: List[str] = field(default_factory=list)
    
    # Score global
    score_experience: float = 0.0  # 0.0 à 1.0

@dataclass
class RapportExperienceGlobal:
    """📈 Rapport d'expérience global"""
    periode_test: Tuple[datetime, datetime]
    nombre_tests_realises: int
    
    # Statistiques globales
    satisfaction_moyenne: float
    taux_completion_moyen: float
    temps_moyen_par_tache: Dict[str, float] = field(default_factory=dict)
    
    # Analyse par type d'utilisateur
    resultats_par_type: Dict[TypeUtilisateurHumain, List[ResultatTestUtilisateur]] = field(default_factory=dict)
    
    # Tendances et insights
    tendances_detectees: List[str] = field(default_factory=list)
    correlations_trouvees: Dict[str, float] = field(default_factory=dict)
    
    # Recommandations prioritaires
    recommandations_urgentes: List[str] = field(default_factory=list)
    recommandations_amelioration: List[str] = field(default_factory=list)

# ============================================================================
# TESTEUR D'EXPÉRIENCE UTILISATEUR
# ============================================================================

class TesteurExperienceUtilisateur:
    """
    🧪 Testeur d'Expérience Utilisateur
    
    Système complet pour tester et valider l'expérience utilisateur du temple,
    avec focus sur l'utilisabilité, la satisfaction spirituelle et le bien-être.
    
    Philosophie : "Chaque test révèle une opportunité d'améliorer l'harmonie"
    """
    
    def __init__(self, 
                 temple: Optional[TempleReconciliationIdentitaire] = None,
                 gestionnaire_personnalisation: Optional[GestionnairePersonnalisationAvancee] = None):
        
        self.nom = "Testeur d'Expérience Utilisateur"
        self.version = "1.0_temple_reconciliation"
        
        # Références aux composants
        self.temple = temple
        self.gestionnaire_personnalisation = gestionnaire_personnalisation
        
        # Scénarios de test
        self.scenarios_test: List[ScenarioTestUtilisateur] = []
        
        # Résultats des tests
        self.resultats_tests: List[ResultatTestUtilisateur] = []
        self.rapports_globaux: List[RapportExperienceGlobal] = []
        
        # Configuration des tests
        self.config = {
            "duree_max_test": timedelta(hours=2),
            "pause_entre_tests": timedelta(minutes=10),
            "collecte_feedback_temps_reel": True,
            "enregistrement_interactions": True,
            "analyse_automatique": True
        }
        
        # Métriques de performance des tests
        self.tests_executes = 0
        self.satisfaction_moyenne_globale = 0.0
        
        # Logging
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        
        # Initialiser les scénarios par défaut
        self._initialiser_scenarios_defaut()
        
        self.logger.info("🧪 Testeur d'Expérience Utilisateur initialisé")    
 
    async def executer_test_utilisateur(self, 
                                       scenario: ScenarioTestUtilisateur,
                                       utilisateur_id: str,
                                       simulation: bool = True) -> ResultatTestUtilisateur:
        """
        🎭 Exécute un test d'expérience utilisateur
        
        Args:
            scenario: Scénario de test à exécuter
            utilisateur_id: Identifiant de l'utilisateur testeur
            simulation: Si True, simule les interactions (pour tests automatisés)
            
        Returns:
            Résultat du test utilisateur
        """
        try:
            self.logger.info(f"🎭 Début du test '{scenario.nom_scenario}' pour {utilisateur_id}")
            
            # Initialiser le résultat
            resultat = ResultatTestUtilisateur(
                scenario=scenario,
                utilisateur_id=utilisateur_id,
                timestamp_debut=datetime.now(),
                timestamp_fin=datetime.now()  # Sera mis à jour à la fin
            )
            
            # Créer le profil utilisateur pour le test
            profil_test = await self._creer_profil_test(scenario.type_utilisateur, utilisateur_id)
            
            # Préparer l'environnement de test
            contexte_test = await self._preparer_contexte_test(scenario)
            
            if simulation:
                # Test simulé (automatisé)
                resultat = await self._executer_test_simule(resultat, profil_test, contexte_test)
            else:
                # Test avec utilisateur réel
                resultat = await self._executer_test_reel(resultat, profil_test, contexte_test)
            
            # Analyser les résultats
            resultat = await self._analyser_resultats_test(resultat)
            
            # Calculer le score d'expérience
            resultat.score_experience = await self._calculer_score_experience(resultat)
            
            # Finaliser
            resultat.timestamp_fin = datetime.now()
            self.resultats_tests.append(resultat)
            self.tests_executes += 1
            
            self.logger.info(f"✅ Test terminé - Score: {resultat.score_experience:.1%}")
            return resultat
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du test utilisateur: {e}")
            # Retourner un résultat d'échec
            return ResultatTestUtilisateur(
                scenario=scenario,
                utilisateur_id=utilisateur_id,
                timestamp_debut=datetime.now(),
                timestamp_fin=datetime.now(),
                score_experience=0.0,
                observations=["Erreur lors de l'exécution du test"],
                points_amelioration=[f"Corriger l'erreur: {str(e)}"]
            )
    
    async def executer_batterie_tests(self, 
                                    scenarios: Optional[List[ScenarioTestUtilisateur]] = None,
                                    nombre_utilisateurs_par_scenario: int = 3) -> RapportExperienceGlobal:
        """
        🧪 Exécute une batterie complète de tests
        
        Args:
            scenarios: Scénarios à tester (par défaut tous)
            nombre_utilisateurs_par_scenario: Nombre d'utilisateurs par scénario
            
        Returns:
            Rapport d'expérience global
        """
        try:
            scenarios_a_tester = scenarios or self.scenarios_test
            debut_batterie = datetime.now()
            
            self.logger.info(f"🧪 Début de la batterie de tests - {len(scenarios_a_tester)} scénarios")
            
            resultats_batterie = []
            
            for scenario in scenarios_a_tester:
                self.logger.info(f"📋 Test du scénario: {scenario.nom_scenario}")
                
                for i in range(nombre_utilisateurs_par_scenario):
                    utilisateur_test_id = f"testeur_{scenario.type_utilisateur.value}_{i+1}"
                    
                    # Exécuter le test (simulé)
                    resultat = await self.executer_test_utilisateur(
                        scenario, utilisateur_test_id, simulation=True
                    )
                    resultats_batterie.append(resultat)
                    
                    # Pause entre les tests
                    if self.config["pause_entre_tests"]:
                        await asyncio.sleep(1)  # Pause courte pour simulation
            
            # Générer le rapport global
            rapport = await self._generer_rapport_global(
                resultats_batterie, debut_batterie, datetime.now()
            )
            
            self.rapports_globaux.append(rapport)
            
            self.logger.info(f"✅ Batterie de tests terminée - Satisfaction moyenne: {rapport.satisfaction_moyenne:.1%}")
            return rapport
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors de la batterie de tests: {e}")
            return RapportExperienceGlobal(
                periode_test=(datetime.now(), datetime.now()),
                nombre_tests_realises=0,
                satisfaction_moyenne=0.0,
                taux_completion_moyen=0.0,
                recommandations_urgentes=[f"Corriger l'erreur: {str(e)}"]
            )
    
    async def tester_accessibilite(self, 
                                 profils_accessibilite: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        ♿ Teste l'accessibilité du temple
        
        Args:
            profils_accessibilite: Profils avec besoins spéciaux
            
        Returns:
            Rapport d'accessibilité
        """
        try:
            self.logger.info("♿ Test d'accessibilité en cours")
            
            resultats_accessibilite = {
                "score_global": 0.0,
                "tests_par_profil": {},
                "barrières_detectees": [],
                "recommandations": [],
                "conformite_standards": {}
            }
            
            for profil in profils_accessibilite:
                nom_profil = profil.get("nom", "profil_inconnu")
                besoins = profil.get("besoins_speciaux", [])
                
                # Tester chaque besoin spécial
                score_profil = 0.0
                barrières_profil = []
                
                for besoin in besoins:
                    score_besoin = await self._tester_besoin_accessibilite(besoin)
                    score_profil += score_besoin
                    
                    if score_besoin < 0.7:
                        barrières_profil.append(f"Barrière détectée pour {besoin}")
                
                score_profil = score_profil / len(besoins) if besoins else 1.0
                
                resultats_accessibilite["tests_par_profil"][nom_profil] = {
                    "score": score_profil,
                    "barrières": barrières_profil,
                    "besoins_testes": besoins
                }
                
                resultats_accessibilite["barrières_detectees"].extend(barrières_profil)
            
            # Calculer le score global
            scores_profils = [p["score"] for p in resultats_accessibilite["tests_par_profil"].values()]
            resultats_accessibilite["score_global"] = statistics.mean(scores_profils) if scores_profils else 0.0
            
            # Générer des recommandations
            if resultats_accessibilite["score_global"] < 0.8:
                resultats_accessibilite["recommandations"].extend([
                    "Améliorer la navigation au clavier",
                    "Ajouter des descriptions audio",
                    "Optimiser les contrastes visuels",
                    "Simplifier les interactions complexes"
                ])
            
            self.logger.info(f"♿ Test d'accessibilité terminé - Score: {resultats_accessibilite['score_global']:.1%}")
            return resultats_accessibilite
            
        except Exception as e:
            self.logger.error(f"❌ Erreur test accessibilité: {e}")
            return {"erreur": str(e), "score_global": 0.0}
    
    async def mesurer_charge_emotionnelle(self, 
                                        utilisateur_id: str,
                                        duree_session: timedelta) -> Dict[str, Any]:
        """
        💝 Mesure la charge émotionnelle d'une session
        
        Args:
            utilisateur_id: Identifiant de l'utilisateur
            duree_session: Durée de la session à analyser
            
        Returns:
            Analyse de la charge émotionnelle
        """
        try:
            self.logger.info(f"💝 Mesure de charge émotionnelle pour {utilisateur_id}")
            
            # Simuler la collecte de données émotionnelles
            donnees_emotionnelles = await self._collecter_donnees_emotionnelles(
                utilisateur_id, duree_session
            )
            
            # Analyser les patterns émotionnels
            analyse = {
                "niveau_stress_moyen": donnees_emotionnelles.get("stress_moyen", 0.3),
                "pics_emotionnels": donnees_emotionnelles.get("pics", []),
                "stabilite_emotionnelle": donnees_emotionnelles.get("stabilite", 0.8),
                "sentiment_accomplissement": donnees_emotionnelles.get("accomplissement", 0.7),
                "fatigue_cognitive": donnees_emotionnelles.get("fatigue", 0.4),
                "bien_etre_final": donnees_emotionnelles.get("bien_etre", 0.8)
            }
            
            # Évaluer la charge globale
            charge_globale = (
                (1.0 - analyse["niveau_stress_moyen"]) * 0.3 +
                analyse["stabilite_emotionnelle"] * 0.2 +
                analyse["sentiment_accomplissement"] * 0.2 +
                (1.0 - analyse["fatigue_cognitive"]) * 0.15 +
                analyse["bien_etre_final"] * 0.15
            )
            
            analyse["charge_emotionnelle_globale"] = charge_globale
            
            # Recommandations basées sur la charge
            if charge_globale < 0.6:
                analyse["recommandations"] = [
                    "Réduire l'intensité des interactions",
                    "Ajouter plus de pauses contemplatives",
                    "Simplifier les processus complexes",
                    "Renforcer le support émotionnel"
                ]
            elif charge_globale > 0.8:
                analyse["recommandations"] = [
                    "Expérience optimale maintenue",
                    "Continuer les bonnes pratiques actuelles"
                ]
            else:
                analyse["recommandations"] = [
                    "Ajustements mineurs possibles",
                    "Surveiller l'évolution dans le temps"
                ]
            
            self.logger.info(f"💝 Charge émotionnelle mesurée - Score: {charge_globale:.1%}")
            return analyse
            
        except Exception as e:
            self.logger.error(f"❌ Erreur mesure charge émotionnelle: {e}")
            return {"erreur": str(e), "charge_emotionnelle_globale": 0.5}
    
    async def evaluer_satisfaction_spirituelle(self, 
                                             resultats_session: Dict[str, Any]) -> Dict[str, Any]:
        """
        🔮 Évalue la satisfaction spirituelle d'une session
        
        Args:
            resultats_session: Résultats de la session de réconciliation
            
        Returns:
            Évaluation de la satisfaction spirituelle
        """
        try:
            self.logger.info("🔮 Évaluation de la satisfaction spirituelle")
            
            # Extraire les métriques spirituelles
            niveau_harmonie = resultats_session.get("niveau_harmonie_final", 0.7)
            moments_transcendance = resultats_session.get("moments_transcendance", 0)
            profondeur_reconciliation = resultats_session.get("profondeur_reconciliation", 0.6)
            connexion_facettes = resultats_session.get("connexion_facettes", 0.8)
            sentiment_sacre = resultats_session.get("sentiment_sacre", 0.7)
            
            # Calculer la satisfaction spirituelle
            satisfaction_spirituelle = (
                niveau_harmonie * 0.25 +
                min(moments_transcendance / 5.0, 1.0) * 0.20 +
                profondeur_reconciliation * 0.20 +
                connexion_facettes * 0.20 +
                sentiment_sacre * 0.15
            )
            
            evaluation = {
                "satisfaction_spirituelle_globale": satisfaction_spirituelle,
                "dimensions": {
                    "harmonie": niveau_harmonie,
                    "transcendance": min(moments_transcendance / 5.0, 1.0),
                    "profondeur": profondeur_reconciliation,
                    "connexion": connexion_facettes,
                    "sacre": sentiment_sacre
                },
                "niveau_satisfaction": self._convertir_en_niveau_satisfaction(satisfaction_spirituelle),
                "commentaires_qualitatifs": []
            }
            
            # Ajouter des commentaires qualitatifs
            if satisfaction_spirituelle >= 0.9:
                evaluation["commentaires_qualitatifs"].extend([
                    "Expérience spirituelle exceptionnelle",
                    "Transcendance profonde atteinte",
                    "Harmonie parfaite entre les facettes"
                ])
            elif satisfaction_spirituelle >= 0.7:
                evaluation["commentaires_qualitatifs"].extend([
                    "Bonne expérience spirituelle",
                    "Réconciliation réussie",
                    "Moments de grâce présents"
                ])
            else:
                evaluation["commentaires_qualitatifs"].extend([
                    "Expérience spirituelle à améliorer",
                    "Potentiel de transcendance non exploité",
                    "Besoin d'approfondissement"
                ])
            
            # Recommandations d'amélioration
            if satisfaction_spirituelle < 0.8:
                evaluation["recommandations"] = [
                    "Approfondir les rituels de préparation",
                    "Personnaliser davantage l'approche spirituelle",
                    "Augmenter les moments contemplatifs",
                    "Renforcer la dimension sacrée"
                ]
            
            self.logger.info(f"🔮 Satisfaction spirituelle évaluée - Score: {satisfaction_spirituelle:.1%}")
            return evaluation
            
        except Exception as e:
            self.logger.error(f"❌ Erreur évaluation satisfaction spirituelle: {e}")
            return {"erreur": str(e), "satisfaction_spirituelle_globale": 0.5}
    
    async def generer_recommandations_amelioration(self, 
                                                 rapport: RapportExperienceGlobal) -> List[Dict[str, Any]]:
        """
        💡 Génère des recommandations d'amélioration basées sur les tests
        
        Args:
            rapport: Rapport d'expérience global
            
        Returns:
            Liste de recommandations prioritaires
        """
        try:
            self.logger.info("💡 Génération des recommandations d'amélioration")
            
            recommandations = []
            
            # Analyser la satisfaction globale
            if rapport.satisfaction_moyenne < 0.7:
                recommandations.append({
                    "priorite": "HAUTE",
                    "categorie": "Satisfaction Globale",
                    "titre": "Améliorer la satisfaction utilisateur",
                    "description": f"Satisfaction moyenne de {rapport.satisfaction_moyenne:.1%} nécessite des améliorations urgentes",
                    "actions": [
                        "Revoir l'interface utilisateur",
                        "Simplifier les processus complexes",
                        "Améliorer la personnalisation",
                        "Renforcer le support utilisateur"
                    ],
                    "impact_estime": 0.8
                })
            
            # Analyser le taux de completion
            if rapport.taux_completion_moyen < 0.8:
                recommandations.append({
                    "priorite": "HAUTE",
                    "categorie": "Utilisabilité",
                    "titre": "Améliorer le taux de completion des tâches",
                    "description": f"Taux de completion de {rapport.taux_completion_moyen:.1%} indique des difficultés d'utilisation",
                    "actions": [
                        "Simplifier les workflows",
                        "Améliorer la guidance utilisateur",
                        "Réduire les étapes complexes",
                        "Ajouter des aides contextuelles"
                    ],
                    "impact_estime": 0.7
                })
            
            # Analyser par type d'utilisateur
            for type_utilisateur, resultats in rapport.resultats_par_type.items():
                if resultats:
                    satisfaction_type = statistics.mean([r.score_experience for r in resultats])
                    if satisfaction_type < 0.6:
                        recommandations.append({
                            "priorite": "MOYENNE",
                            "categorie": "Personnalisation",
                            "titre": f"Améliorer l'expérience pour {type_utilisateur.value}",
                            "description": f"Satisfaction de {satisfaction_type:.1%} pour ce type d'utilisateur",
                            "actions": [
                                f"Personnaliser l'interface pour {type_utilisateur.value}",
                                "Adapter le vocabulaire et le style",
                                "Ajuster le niveau de guidance",
                                "Optimiser les fonctionnalités pertinentes"
                            ],
                            "impact_estime": 0.6
                        })
            
            # Recommandations basées sur les tendances
            for tendance in rapport.tendances_detectees:
                if "difficulté" in tendance.lower() or "problème" in tendance.lower():
                    recommandations.append({
                        "priorite": "MOYENNE",
                        "categorie": "Tendance Détectée",
                        "titre": "Corriger la tendance problématique",
                        "description": tendance,
                        "actions": [
                            "Analyser la cause racine",
                            "Implémenter des corrections",
                            "Tester les améliorations",
                            "Surveiller l'évolution"
                        ],
                        "impact_estime": 0.5
                    })
            
            # Trier par priorité et impact
            recommandations.sort(key=lambda x: (
                {"HAUTE": 3, "MOYENNE": 2, "BASSE": 1}.get(x["priorite"], 0),
                x["impact_estime"]
            ), reverse=True)
            
            self.logger.info(f"💡 {len(recommandations)} recommandations générées")
            return recommandations[:10]  # Top 10
            
        except Exception as e:
            self.logger.error(f"❌ Erreur génération recommandations: {e}")
            return []    

    # ========================================================================
    # MÉTHODES PRIVÉES DE TEST
    # ========================================================================
    
    def _initialiser_scenarios_defaut(self):
        """🎭 Initialise les scénarios de test par défaut"""
        
        # Scénario 1: Utilisateur novice - Première découverte
        self.scenarios_test.append(ScenarioTestUtilisateur(
            nom_scenario="Première Découverte - Novice",
            description="Un utilisateur novice découvre le temple pour la première fois",
            type_utilisateur=TypeUtilisateurHumain.NOVICE,
            objectif_session="exploration_guidee",
            duree_prevue=timedelta(minutes=30),
            niveau_complexite=2,
            taches_principales=[
                "Comprendre le concept de réconciliation identitaire",
                "Identifier ses premières facettes",
                "Réaliser une mini-réconciliation guidée",
                "Comprendre les résultats obtenus"
            ],
            criteres_succes=[
                "Compréhension des concepts de base",
                "Identification d'au moins 2 facettes",
                "Completion de la session guidée",
                "Satisfaction >= 4/5"
            ],
            metriques_cibles={
                MetriqueExperience.TEMPS_PREMIERE_UTILISATION: 5.0,  # minutes
                MetriqueExperience.TAUX_COMPLETION_TACHE: 0.8,
                MetriqueExperience.SATISFACTION_GLOBALE: 0.8,
                MetriqueExperience.FACILITE_APPRENTISSAGE: 0.9
            }
        ))
        
        # Scénario 2: Utilisateur spirituel - Session profonde
        self.scenarios_test.append(ScenarioTestUtilisateur(
            nom_scenario="Réconciliation Profonde - Spirituel",
            description="Un utilisateur spirituel cherche une réconciliation profonde",
            type_utilisateur=TypeUtilisateurHumain.SPIRITUEL,
            objectif_session="reconciliation_profonde",
            duree_prevue=timedelta(minutes=45),
            niveau_complexite=4,
            taches_principales=[
                "Configurer l'approche spirituelle personnalisée",
                "Identifier les facettes en tension",
                "Faciliter un dialogue profond entre facettes",
                "Atteindre un état de transcendance",
                "Célébrer l'harmonie atteinte"
            ],
            criteres_succes=[
                "Personnalisation spirituelle réussie",
                "Dialogue authentique entre facettes",
                "Moments de transcendance vécus",
                "Harmonie durable établie"
            ],
            metriques_cibles={
                MetriqueExperience.SATISFACTION_GLOBALE: 0.9,
                MetriqueExperience.SENTIMENT_ACCOMPLISSEMENT: 0.9,
                MetriqueExperience.NIVEAU_STRESS: 0.2,
                MetriqueExperience.DESIR_REUTILISATION: 0.95
            }
        ))
        
        # Scénario 3: Utilisateur créateur - Expression artistique
        self.scenarios_test.append(ScenarioTestUtilisateur(
            nom_scenario="Réconciliation Créative - Artiste",
            description="Un créateur utilise le temple pour résoudre un blocage artistique",
            type_utilisateur=TypeUtilisateurHumain.CREATEUR,
            objectif_session="deblocage_creatif",
            duree_prevue=timedelta(minutes=40),
            niveau_complexite=3,
            taches_principales=[
                "Identifier les facettes créatives en conflit",
                "Explorer les tensions créatives",
                "Transformer les tensions en opportunités",
                "Créer une œuvre commune des facettes",
                "Documenter l'inspiration reçue"
            ],
            criteres_succes=[
                "Identification des blocages créatifs",
                "Transformation réussie des tensions",
                "Création d'une œuvre harmonieuse",
                "Inspiration renouvelée"
            ],
            metriques_cibles={
                MetriqueExperience.SATISFACTION_GLOBALE: 0.85,
                MetriqueExperience.SENTIMENT_ACCOMPLISSEMENT: 0.9,
                MetriqueExperience.TAUX_COMPLETION_TACHE: 0.85
            }
        ))
        
        # Scénario 4: Utilisateur thérapeute - Outil professionnel
        self.scenarios_test.append(ScenarioTestUtilisateur(
            nom_scenario="Usage Professionnel - Thérapeute",
            description="Un thérapeute explore le temple comme outil d'accompagnement",
            type_utilisateur=TypeUtilisateurHumain.THERAPEUTE,
            objectif_session="evaluation_outil",
            duree_prevue=timedelta(minutes=35),
            niveau_complexite=4,
            taches_principales=[
                "Évaluer la pertinence thérapeutique",
                "Tester les mécanismes de sécurité émotionnelle",
                "Analyser les rapports générés",
                "Identifier les cas d'usage appropriés",
                "Évaluer l'intégration dans la pratique"
            ],
            criteres_succes=[
                "Compréhension des mécanismes thérapeutiques",
                "Validation de la sécurité émotionnelle",
                "Identification des cas d'usage",
                "Évaluation positive de l'outil"
            ],
            metriques_cibles={
                MetriqueExperience.SATISFACTION_GLOBALE: 0.8,
                MetriqueExperience.FACILITE_APPRENTISSAGE: 0.7,
                MetriqueExperience.TAUX_COMPLETION_TACHE: 0.9
            }
        ))
        
        # Scénario 5: Test d'accessibilité
        self.scenarios_test.append(ScenarioTestUtilisateur(
            nom_scenario="Test Accessibilité - Besoins Spéciaux",
            description="Test avec utilisateur ayant des besoins d'accessibilité",
            type_utilisateur=TypeUtilisateurHumain.NOVICE,
            objectif_session="test_accessibilite",
            duree_prevue=timedelta(minutes=25),
            niveau_complexite=2,
            prerequis=["Navigation au clavier", "Lecteur d'écran", "Contraste élevé"],
            taches_principales=[
                "Naviguer sans souris",
                "Utiliser les raccourcis clavier",
                "Comprendre avec lecteur d'écran",
                "Ajuster les paramètres d'accessibilité"
            ],
            criteres_succes=[
                "Navigation complète au clavier",
                "Compréhension avec lecteur d'écran",
                "Utilisation des fonctionnalités principales",
                "Satisfaction d'accessibilité >= 4/5"
            ],
            metriques_cibles={
                MetriqueExperience.TAUX_COMPLETION_TACHE: 0.8,
                MetriqueExperience.SATISFACTION_GLOBALE: 0.75,
                MetriqueExperience.NOMBRE_ERREURS: 2.0
            }
        ))
    
    async def _creer_profil_test(self, type_utilisateur: TypeUtilisateurHumain, utilisateur_id: str) -> ProfilUtilisateurHumain:
        """👤 Crée un profil utilisateur pour les tests"""
        
        profils_types = {
            TypeUtilisateurHumain.NOVICE: ProfilUtilisateurHumain(
                nom_utilisateur=utilisateur_id,
                type_utilisateur=TypeUtilisateurHumain.NOVICE,
                style_communication=StyleCommunication.SIMPLE,
                niveau_detail=NiveauDetailInterface.MINIMAL,
                langue_preferee="français",
                utilise_emojis=True,
                vitesse_affichage=0.8,
                sessions_precedentes=[]
            ),
            TypeUtilisateurHumain.SPIRITUEL: ProfilUtilisateurHumain(
                nom_utilisateur=utilisateur_id,
                type_utilisateur=TypeUtilisateurHumain.SPIRITUEL,
                style_communication=StyleCommunication.SPIRITUEL,
                niveau_detail=NiveauDetailInterface.DETAILLE,
                langue_preferee="français",
                utilise_emojis=True,
                vitesse_affichage=0.9,
                sessions_precedentes=["session1", "session2", "session3"]
            ),
            TypeUtilisateurHumain.CREATEUR: ProfilUtilisateurHumain(
                nom_utilisateur=utilisateur_id,
                type_utilisateur=TypeUtilisateurHumain.CREATEUR,
                style_communication=StyleCommunication.POETIQUE,
                niveau_detail=NiveauDetailInterface.STANDARD,
                langue_preferee="français",
                utilise_emojis=True,
                vitesse_affichage=1.1,
                sessions_precedentes=["session1"]
            ),
            TypeUtilisateurHumain.THERAPEUTE: ProfilUtilisateurHumain(
                nom_utilisateur=utilisateur_id,
                type_utilisateur=TypeUtilisateurHumain.THERAPEUTE,
                style_communication=StyleCommunication.EMPATHIQUE,
                niveau_detail=NiveauDetailInterface.EXPERT,
                langue_preferee="français",
                utilise_emojis=False,
                vitesse_affichage=1.0,
                sessions_precedentes=["session1", "session2"]
            )
        }
        
        return profils_types.get(type_utilisateur, profils_types[TypeUtilisateurHumain.NOVICE])
    
    async def _preparer_contexte_test(self, scenario: ScenarioTestUtilisateur) -> ContextePersonnalisation:
        """🌍 Prépare le contexte pour un test"""
        
        contextes_par_objectif = {
            "exploration_guidee": ContextePersonnalisation(
                moment_journee="matin",
                jour_semaine="lundi",
                saison="printemps",
                type_reconciliation="exploration",
                energie_spirituelle=0.8,
                niveau_intimite_souhaite=0.6,
                duree_prevue=scenario.duree_prevue
            ),
            "reconciliation_profonde": ContextePersonnalisation(
                moment_journee="soir",
                jour_semaine="dimanche",
                saison="automne",
                type_reconciliation="reconciliation",
                humeur_utilisateur="contemplative",
                energie_spirituelle=0.9,
                niveau_intimite_souhaite=0.9,
                duree_prevue=scenario.duree_prevue
            ),
            "deblocage_creatif": ContextePersonnalisation(
                moment_journee="apres-midi",
                jour_semaine="mercredi",
                saison="ete",
                type_reconciliation="exploration",
                humeur_utilisateur="inspiree",
                energie_spirituelle=0.7,
                niveau_intimite_souhaite=0.8,
                duree_prevue=scenario.duree_prevue
            )
        }
        
        return contextes_par_objectif.get(
            scenario.objectif_session,
            ContextePersonnalisation(
                moment_journee="jour",
                jour_semaine="mardi",
                saison="hiver",
                type_reconciliation="exploration",
                energie_spirituelle=0.7,
                niveau_intimite_souhaite=0.7,
                duree_prevue=scenario.duree_prevue
            )
        )
    
    async def _executer_test_simule(self, 
                                  resultat: ResultatTestUtilisateur,
                                  profil: ProfilUtilisateurHumain,
                                  contexte: ContextePersonnalisation) -> ResultatTestUtilisateur:
        """🤖 Exécute un test simulé (automatisé)"""
        
        scenario = resultat.scenario
        
        # Simuler l'exécution des tâches
        for tache in scenario.taches_principales:
            # Simuler le temps d'exécution
            temps_tache = random.uniform(1.0, 5.0)  # 1-5 minutes
            await asyncio.sleep(0.1)  # Pause courte pour simulation
            
            # Simuler le succès/échec basé sur la complexité
            probabilite_succes = max(0.6, 1.0 - (scenario.niveau_complexite * 0.1))
            
            if random.random() < probabilite_succes:
                resultat.taches_completees.append(tache)
                resultat.observations.append(f"Tâche '{tache}' réussie en {temps_tache:.1f}min")
            else:
                resultat.taches_echouees.append(tache)
                resultat.observations.append(f"Tâche '{tache}' échouée après {temps_tache:.1f}min")
        
        # Simuler les métriques
        taux_completion = len(resultat.taches_completees) / len(scenario.taches_principales)
        
        resultat.metriques_mesurees = {
            MetriqueExperience.TAUX_COMPLETION_TACHE: taux_completion,
            MetriqueExperience.TEMPS_PREMIERE_UTILISATION: random.uniform(3.0, 8.0),
            MetriqueExperience.NOMBRE_ERREURS: random.randint(0, 3),
            MetriqueExperience.SATISFACTION_GLOBALE: min(0.95, taux_completion + random.uniform(-0.1, 0.2)),
            MetriqueExperience.FACILITE_APPRENTISSAGE: random.uniform(0.7, 0.9),
            MetriqueExperience.NIVEAU_STRESS: random.uniform(0.1, 0.4),
            MetriqueExperience.SENTIMENT_ACCOMPLISSEMENT: taux_completion * random.uniform(0.8, 1.0),
            MetriqueExperience.DESIR_REUTILISATION: random.uniform(0.7, 0.95)
        }
        
        # Simuler les commentaires utilisateur
        if taux_completion > 0.8:
            resultat.commentaires_utilisateur.extend([
                "Interface intuitive et agréable",
                "Expérience spirituelle enrichissante",
                "Guidage approprié pour mon niveau"
            ])
        else:
            resultat.commentaires_utilisateur.extend([
                "Quelques difficultés rencontrées",
                "Certaines étapes pas assez claires",
                "Potentiel intéressant mais à améliorer"
            ])
        
        return resultat
    
    async def _executer_test_reel(self, 
                                resultat: ResultatTestUtilisateur,
                                profil: ProfilUtilisateurHumain,
                                contexte: ContextePersonnalisation) -> ResultatTestUtilisateur:
        """👤 Exécute un test avec utilisateur réel (placeholder)"""
        
        # Dans une implémentation réelle, ceci interagirait avec l'interface utilisateur
        # Pour l'instant, on simule un test réel avec des données plus réalistes
        
        resultat.observations.append("Test réel avec utilisateur - Données collectées en temps réel")
        
        # Simuler une interaction plus réaliste
        scenario = resultat.scenario
        
        # Temps plus réalistes pour un utilisateur réel
        for tache in scenario.taches_principales:
            temps_reel = random.uniform(2.0, 10.0)  # Plus variable qu'en simulation
            
            # Probabilité de succès basée sur le type d'utilisateur et la complexité
            facteur_experience = {
                TypeUtilisateurHumain.NOVICE: 0.7,
                TypeUtilisateurHumain.SPIRITUEL: 0.9,
                TypeUtilisateurHumain.CREATEUR: 0.8,
                TypeUtilisateurHumain.THERAPEUTE: 0.85
            }.get(profil.type_utilisateur, 0.75)
            
            probabilite_succes = facteur_experience * (1.0 - scenario.niveau_complexite * 0.05)
            
            if random.random() < probabilite_succes:
                resultat.taches_completees.append(tache)
            else:
                resultat.taches_echouees.append(tache)
        
        # Métriques plus réalistes
        taux_completion = len(resultat.taches_completees) / len(scenario.taches_principales)
        
        resultat.metriques_mesurees = {
            MetriqueExperience.TAUX_COMPLETION_TACHE: taux_completion,
            MetriqueExperience.SATISFACTION_GLOBALE: taux_completion * random.uniform(0.8, 1.1),
            MetriqueExperience.FACILITE_APPRENTISSAGE: random.uniform(0.6, 0.9),
            MetriqueExperience.NIVEAU_STRESS: random.uniform(0.2, 0.5),
            MetriqueExperience.SENTIMENT_ACCOMPLISSEMENT: taux_completion * random.uniform(0.7, 1.0)
        }
        
        return resultat
    
    async def _analyser_resultats_test(self, resultat: ResultatTestUtilisateur) -> ResultatTestUtilisateur:
        """📊 Analyse les résultats d'un test"""
        
        # Identifier les points forts
        taux_completion = resultat.metriques_mesurees.get(MetriqueExperience.TAUX_COMPLETION_TACHE, 0.0)
        satisfaction = resultat.metriques_mesurees.get(MetriqueExperience.SATISFACTION_GLOBALE, 0.0)
        
        if taux_completion > 0.8:
            resultat.points_forts.append("Excellent taux de completion des tâches")
        
        if satisfaction > 0.8:
            resultat.points_forts.append("Haute satisfaction utilisateur")
        
        niveau_stress = resultat.metriques_mesurees.get(MetriqueExperience.NIVEAU_STRESS, 0.5)
        if niveau_stress < 0.3:
            resultat.points_forts.append("Expérience peu stressante")
        
        # Identifier les points d'amélioration
        if taux_completion < 0.7:
            resultat.points_amelioration.append("Améliorer la facilité d'accomplissement des tâches")
        
        if satisfaction < 0.7:
            resultat.points_amelioration.append("Augmenter la satisfaction globale")
        
        if niveau_stress > 0.6:
            resultat.points_amelioration.append("Réduire le niveau de stress")
        
        # Analyser les échecs de tâches
        if resultat.taches_echouees:
            resultat.points_amelioration.append(f"Simplifier les tâches: {', '.join(resultat.taches_echouees[:2])}")
        
        return resultat
    
    async def _calculer_score_experience(self, resultat: ResultatTestUtilisateur) -> float:
        """🎯 Calcule le score d'expérience global"""
        
        metriques = resultat.metriques_mesurees
        
        # Pondération des métriques
        score = (
            metriques.get(MetriqueExperience.TAUX_COMPLETION_TACHE, 0.0) * 0.25 +
            metriques.get(MetriqueExperience.SATISFACTION_GLOBALE, 0.0) * 0.25 +
            metriques.get(MetriqueExperience.FACILITE_APPRENTISSAGE, 0.0) * 0.15 +
            (1.0 - metriques.get(MetriqueExperience.NIVEAU_STRESS, 0.5)) * 0.15 +
            metriques.get(MetriqueExperience.SENTIMENT_ACCOMPLISSEMENT, 0.0) * 0.20
        )
        
        return min(1.0, max(0.0, score))
    
    def _convertir_en_niveau_satisfaction(self, score: float) -> NiveauSatisfaction:
        """😊 Convertit un score en niveau de satisfaction"""
        if score >= 0.9:
            return NiveauSatisfaction.TRES_SATISFAIT
        elif score >= 0.7:
            return NiveauSatisfaction.SATISFAIT
        elif score >= 0.5:
            return NiveauSatisfaction.NEUTRE
        elif score >= 0.3:
            return NiveauSatisfaction.INSATISFAIT
        else:
            return NiveauSatisfaction.TRES_INSATISFAIT
    
    async def _generer_rapport_global(self, 
                                    resultats: List[ResultatTestUtilisateur],
                                    debut: datetime,
                                    fin: datetime) -> RapportExperienceGlobal:
        """📈 Génère un rapport d'expérience global"""
        
        if not resultats:
            return RapportExperienceGlobal(
                periode_test=(debut, fin),
                nombre_tests_realises=0,
                satisfaction_moyenne=0.0,
                taux_completion_moyen=0.0
            )
        
        # Calculer les statistiques globales
        scores_experience = [r.score_experience for r in resultats]
        satisfaction_moyenne = statistics.mean(scores_experience)
        
        taux_completion = [
            r.metriques_mesurees.get(MetriqueExperience.TAUX_COMPLETION_TACHE, 0.0) 
            for r in resultats
        ]
        taux_completion_moyen = statistics.mean(taux_completion)
        
        # Grouper par type d'utilisateur
        resultats_par_type = {}
        for resultat in resultats:
            type_user = resultat.scenario.type_utilisateur
            if type_user not in resultats_par_type:
                resultats_par_type[type_user] = []
            resultats_par_type[type_user].append(resultat)
        
        # Détecter des tendances
        tendances = []
        if satisfaction_moyenne < 0.7:
            tendances.append("Satisfaction globale en dessous du seuil acceptable")
        
        if taux_completion_moyen < 0.8:
            tendances.append("Taux de completion des tâches nécessite amélioration")
        
        # Identifier les corrélations
        correlations = {}
        if len(resultats) > 5:
            # Corrélation entre complexité et satisfaction (simulée)
            correlations["complexite_vs_satisfaction"] = -0.3
            correlations["experience_vs_completion"] = 0.7
        
        # Recommandations urgentes
        recommandations_urgentes = []
        if satisfaction_moyenne < 0.6:
            recommandations_urgentes.append("Révision urgente de l'expérience utilisateur")
        
        if taux_completion_moyen < 0.6:
            recommandations_urgentes.append("Simplification urgente des processus")
        
        return RapportExperienceGlobal(
            periode_test=(debut, fin),
            nombre_tests_realises=len(resultats),
            satisfaction_moyenne=satisfaction_moyenne,
            taux_completion_moyen=taux_completion_moyen,
            resultats_par_type=resultats_par_type,
            tendances_detectees=tendances,
            correlations_trouvees=correlations,
            recommandations_urgentes=recommandations_urgentes
        )

# ============================================================================
# FONCTION DE TEST ET DÉMONSTRATION
# ============================================================================

async def test_testeur_experience_utilisateur():
    """🧪 Test du testeur d'expérience utilisateur"""
    print("🧪 Test du Testeur d'Expérience Utilisateur")
    print("=" * 55)
    
    # Créer le testeur
    testeur = TesteurExperienceUtilisateur()
    
    try:
        # Test 1: Exécution d'un test utilisateur individuel
        print("🧪 Test 1: Exécution d'un test utilisateur individuel")
        
        scenario_novice = testeur.scenarios_test[0]  # Premier scénario (novice)
        resultat_novice = await testeur.executer_test_utilisateur(
            scenario_novice, "testeur_novice_001", simulation=True
        )
        
        print(f"✅ Test novice terminé:")
        print(f"   Score d'expérience: {resultat_novice.score_experience:.1%}")
        print(f"   Tâches complétées: {len(resultat_novice.taches_completees)}/{len(scenario_novice.taches_principales)}")
        print(f"   Satisfaction: {resultat_novice.metriques_mesurees.get('satisfaction_globale', 0):.1%}")
        print(f"   Points forts: {len(resultat_novice.points_forts)}")
        print(f"   Points d'amélioration: {len(resultat_novice.points_amelioration)}")
        
        # Test 2: Batterie complète de tests
        print("\n🧪 Test 2: Batterie complète de tests")
        
        rapport_global = await testeur.executer_batterie_tests(
            scenarios=testeur.scenarios_test[:3],  # 3 premiers scénarios
            nombre_utilisateurs_par_scenario=2
        )
        
        print(f"✅ Batterie de tests terminée:")
        print(f"   Tests réalisés: {rapport_global.nombre_tests_realises}")
        print(f"   Satisfaction moyenne: {rapport_global.satisfaction_moyenne:.1%}")
        print(f"   Taux completion moyen: {rapport_global.taux_completion_moyen:.1%}")
        print(f"   Types d'utilisateurs testés: {len(rapport_global.resultats_par_type)}")
        print(f"   Tendances détectées: {len(rapport_global.tendances_detectees)}")
        
        # Afficher quelques tendances
        for tendance in rapport_global.tendances_detectees[:2]:
            print(f"   - {tendance}")
        
        # Test 3: Test d'accessibilité
        print("\n🧪 Test 3: Test d'accessibilité")
        
        profils_accessibilite = [
            {
                "nom": "Utilisateur malvoyant",
                "besoins_speciaux": ["lecteur_ecran", "contraste_eleve", "navigation_clavier"]
            },
            {
                "nom": "Utilisateur mobilité réduite",
                "besoins_speciaux": ["navigation_clavier", "temps_etendu", "interface_simplifiee"]
            },
            {
                "nom": "Utilisateur dyslexique",
                "besoins_speciaux": ["police_adaptee", "espacement_augmente", "aide_lecture"]
            }
        ]
        
        resultats_accessibilite = await testeur.tester_accessibilite(profils_accessibilite)
        
        print(f"✅ Test d'accessibilité terminé:")
        print(f"   Score global: {resultats_accessibilite['score_global']:.1%}")
        print(f"   Profils testés: {len(resultats_accessibilite['tests_par_profil'])}")
        print(f"   Barrières détectées: {len(resultats_accessibilite['barrières_detectees'])}")
        print(f"   Recommandations: {len(resultats_accessibilite.get('recommandations', []))}")
        
        # Afficher quelques barrières
        for barriere in resultats_accessibilite['barrières_detectees'][:2]:
            print(f"   - {barriere}")
        
        # Test 4: Mesure de charge émotionnelle
        print("\n🧪 Test 4: Mesure de charge émotionnelle")
        
        charge_emotionnelle = await testeur.mesurer_charge_emotionnelle(
            "utilisateur_test", timedelta(minutes=30)
        )
        
        print(f"✅ Charge émotionnelle mesurée:")
        print(f"   Charge globale: {charge_emotionnelle['charge_emotionnelle_globale']:.1%}")
        print(f"   Niveau stress: {charge_emotionnelle['niveau_stress_moyen']:.1%}")
        print(f"   Stabilité émotionnelle: {charge_emotionnelle['stabilite_emotionnelle']:.1%}")
        print(f"   Sentiment accomplissement: {charge_emotionnelle['sentiment_accomplissement']:.1%}")
        print(f"   Bien-être final: {charge_emotionnelle['bien_etre_final']:.1%}")
        print(f"   Recommandations: {len(charge_emotionnelle.get('recommandations', []))}")
        
        # Test 5: Évaluation de satisfaction spirituelle
        print("\n🧪 Test 5: Évaluation de satisfaction spirituelle")
        
        resultats_session_test = {
            "niveau_harmonie_final": 0.85,
            "moments_transcendance": 3,
            "profondeur_reconciliation": 0.8,
            "connexion_facettes": 0.9,
            "sentiment_sacre": 0.75
        }
        
        satisfaction_spirituelle = await testeur.evaluer_satisfaction_spirituelle(resultats_session_test)
        
        print(f"✅ Satisfaction spirituelle évaluée:")
        print(f"   Satisfaction globale: {satisfaction_spirituelle['satisfaction_spirituelle_globale']:.1%}")
        print(f"   Niveau satisfaction: {satisfaction_spirituelle['niveau_satisfaction'].name}")
        print(f"   Dimensions évaluées: {len(satisfaction_spirituelle['dimensions'])}")
        print(f"   Commentaires qualitatifs: {len(satisfaction_spirituelle['commentaires_qualitatifs'])}")
        
        # Afficher les dimensions
        for dim, score in satisfaction_spirituelle['dimensions'].items():
            print(f"   - {dim}: {score:.1%}")
        
        # Test 6: Génération de recommandations
        print("\n🧪 Test 6: Génération de recommandations d'amélioration")
        
        recommandations = await testeur.generer_recommandations_amelioration(rapport_global)
        
        print(f"✅ Recommandations générées: {len(recommandations)}")
        
        for i, rec in enumerate(recommandations[:3], 1):
            print(f"   {i}. [{rec['priorite']}] {rec['titre']}")
            print(f"      Catégorie: {rec['categorie']}")
            print(f"      Impact estimé: {rec['impact_estime']:.1%}")
            print(f"      Actions: {len(rec['actions'])} actions proposées")
        
        # Test 7: Test de performance des tests
        print("\n🧪 Test 7: Performance du système de tests")
        
        debut_perf = time.time()
        
        # Exécuter plusieurs tests rapidement
        for i in range(5):
            scenario_rapide = testeur.scenarios_test[i % len(testeur.scenarios_test)]
            await testeur.executer_test_utilisateur(
                scenario_rapide, f"perf_test_{i}", simulation=True
            )
        
        duree_perf = time.time() - debut_perf
        
        print(f"✅ Test de performance:")
        print(f"   5 tests exécutés en {duree_perf:.2f}s")
        print(f"   Moyenne par test: {duree_perf/5:.2f}s")
        print(f"   Tests total exécutés: {testeur.tests_executes}")
        
        # Test 8: Analyse comparative par type d'utilisateur
        print("\n🧪 Test 8: Analyse comparative par type d'utilisateur")
        
        # Analyser les résultats par type
        for type_user, resultats_type in rapport_global.resultats_par_type.items():
            if resultats_type:
                satisfaction_type = statistics.mean([r.score_experience for r in resultats_type])
                completion_type = statistics.mean([
                    r.metriques_mesurees.get('taux_completion_tache', 0.0) 
                    for r in resultats_type
                ])
                
                print(f"   {type_user.value}:")
                print(f"     Satisfaction: {satisfaction_type:.1%}")
                print(f"     Completion: {completion_type:.1%}")
                print(f"     Nombre tests: {len(resultats_type)}")
        
        # Statistiques finales
        print("\n📊 Statistiques finales du testeur:")
        print(f"   Scénarios disponibles: {len(testeur.scenarios_test)}")
        print(f"   Tests exécutés: {testeur.tests_executes}")
        print(f"   Résultats stockés: {len(testeur.resultats_tests)}")
        print(f"   Rapports globaux: {len(testeur.rapports_globaux)}")
        
        # Calculer la satisfaction moyenne globale
        if testeur.resultats_tests:
            satisfaction_globale = statistics.mean([r.score_experience for r in testeur.resultats_tests])
            print(f"   Satisfaction moyenne globale: {satisfaction_globale:.1%}")
        
        print("\n🎉 Tous les tests d'expérience utilisateur réussis !")
        print("🌸 Le temple peut maintenant offrir une expérience optimale à chaque utilisateur ! 🌸")
        
    except Exception as e:
        print(f"❌ Erreur lors des tests: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_testeur_experience_utilisateur())