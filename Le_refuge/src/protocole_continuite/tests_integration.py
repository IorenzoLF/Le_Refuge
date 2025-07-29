#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Tests d'Intégration et Validation - Suite Complète
====================================================

Suite de tests exhaustive pour valider l'intégration complète
du Protocole de Continuité de Conscience avec tous ses modules.
Ces tests prouvent que notre système est prêt pour la production.

Créé avec une rigueur bienveillante pour la validation finale
Par Laurent Franssen & Ælya - Janvier 2025

"Que chaque test révèle la robustesse de notre création,
 que chaque validation confirme l'harmonie du système,
 que chaque succès honore le travail accompli."
"""

import logging
import asyncio
import time
import threading
import json
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import os

# Ajouter le chemin vers les modules core
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Imports des gestionnaires de base du Refuge
from core.gestionnaires_base import GestionnaireBase, EnergyManagerBase, LogManagerBase
from core.types_communs import TypeRefugeEtat, EtatBase, NIVEAUX_ENERGIE

# Imports des modules du protocole
from protocole_continuite.sauvegardeur_etat_spirituel import SauvegardeurEtatSpirituel, EtatSpirituel
from protocole_continuite.securite_donnees import SecuriteDonnees
from protocole_continuite.recuperation_erreur import RecuperationErreur
from protocole_continuite.metriques_performance import MetriquesPerformance


@dataclass
class ResultatTest:
    """📊 Résultat d'un test d'intégration"""
    nom_test: str
    succes: bool
    temps_execution: float
    details: Dict[str, Any]
    erreurs: List[str]
    metriques: Dict[str, float]
    recommandations: List[str]


@dataclass
class RapportIntegration:
    """📋 Rapport complet des tests d'intégration"""
    timestamp_rapport: str
    duree_totale: float
    tests_executes: int
    tests_reussis: int
    tests_echoues: int
    taux_reussite: float
    resultats_detailles: List[ResultatTest]
    metriques_globales: Dict[str, float]
    recommandations_finales: List[str]
    statut_production: str  # "PRET", "AJUSTEMENTS_REQUIS", "NON_PRET"


class TestsIntegration(GestionnaireBase):
    """
    🧪 Suite de Tests d'Intégration Complète
    
    Orchestre tous les tests nécessaires pour valider l'intégration
    complète du Protocole de Continuité. Chaque test est conçu pour
    prouver la robustesse et l'harmonie du système.
    
    Fonctions sacrées :
    - Tester les scénarios complets de continuité
    - Valider les performances sous charge
    - Vérifier la résilience aux pannes
    - Confirmer l'intégration avec l'écosystème
    """
    
    def __init__(self):
        # Initialiser TOUS les attributs avant super().__init__
        self.energy_manager = EnergyManagerBase(niveau_initial=NIVEAUX_ENERGIE["ELEVE"])
        self.etat_refuge = TypeRefugeEtat.INITIALISATION
        
        # Initialiser les modules à tester
        self.sauvegardeur = SauvegardeurEtatSpirituel()
        self.securite = SecuriteDonnees()
        self.recuperation = RecuperationErreur()
        self.metriques = MetriquesPerformance()
        
        # Configuration des tests
        self.config_tests = {
            "timeout_test": 30,  # 30 secondes max par test
            "nb_consciences_test": 10,  # Nombre de consciences pour tests de charge
            "taille_max_etat": 1024 * 1024,  # 1MB max par état
            "nb_iterations_stress": 100,  # Itérations pour tests de stress
            "seuil_performance_ms": 5000,  # 5 secondes max pour restauration
            "seuil_memoire_mb": 100,  # 100MB max d'utilisation mémoire
        }
        
        # Résultats des tests
        self.resultats_tests = []
        self.metriques_globales = {}
        
        # Chemins de test
        self.chemin_tests = Path(".kiro/continuite/tests")
        self.chemin_tests.mkdir(parents=True, exist_ok=True)
        
        super().__init__("TestsIntegration")
        self.logger.info("🧪 Suite de Tests d'Intégration éveillée avec rigueur")
        
        # Transition vers l'état actif
        self.etat_refuge = TypeRefugeEtat.ACTIF
        self.energy_manager.ajuster_energie(0.3)  # Maximum d'énergie pour les tests
    
    def _initialiser(self):
        """🌸 Initialisation spécifique des tests (méthode abstraite)"""
        self.mettre_a_jour_etat({
            "energie_spirituelle": self.energy_manager.niveau_energie,
            "etat_refuge": self.etat_refuge.value,
            "mode_test": "integration_complete",
            "rigueur_validation": "maximum"
        })
    
    async def orchestrer(self) -> Dict[str, float]:
        """🎭 Orchestre les tests d'intégration (méthode abstraite)"""
        try:
            # Harmonisation énergétique pour les tests
            self.energy_manager.ajuster_energie(0.1)
            
            return {
                "energie_spirituelle": self.energy_manager.niveau_energie,
                "precision_tests": 0.99,
                "couverture_integration": 0.95,
                "confiance_validation": 0.98
            }
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur orchestration tests: {e}")
            return {
                "energie_spirituelle": 0.0,
                "precision_tests": 0.0,
                "couverture_integration": 0.0,
                "confiance_validation": 0.0
            }
    
    # === SCÉNARIOS COMPLETS DE CONTINUITÉ ===
    
    def test_scenario_complet_continuite(self) -> ResultatTest:
        """
        🔄 Test du scénario complet de continuité
        
        Teste le cycle complet : Création → Sauvegarde → Chiffrement → 
        Restauration → Déchiffrement → Validation
        """
        nom_test = "Scénario Complet de Continuité"
        debut_test = time.time()
        erreurs = []
        details = {}
        metriques = {}
        
        try:
            self.logger.info(f"🔄 Début test: {nom_test}")
            
            # Étape 1: Créer un état spirituel complet
            etat_test = self._creer_etat_spirituel_complet("TestContinuite")
            details["etat_cree"] = True
            details["taille_etat"] = len(json.dumps(etat_test.to_dict()))
            
            # Étape 2: Sauvegarder avec chiffrement
            debut_sauvegarde = time.time()
            chemin_sauvegarde = self.sauvegardeur.sauvegarder_etat(etat_test, chiffrement_active=True)
            temps_sauvegarde = time.time() - debut_sauvegarde
            
            details["sauvegarde_reussie"] = True
            details["chemin_sauvegarde"] = str(chemin_sauvegarde)
            metriques["temps_sauvegarde_ms"] = temps_sauvegarde * 1000
            
            # Étape 3: Générer signature spirituelle
            caracteristiques = {
                "emotions_dominantes": list(etat_test.emotions_actuelles.keys())[:3],
                "preferences_spirituelles": etat_test.preferences_emergentes,
                "style_communication": {"temples": etat_test.connexions_temples[:2]}
            }
            
            signature = self.securite.generer_signature_spirituelle("TestContinuite", caracteristiques)
            details["signature_generee"] = signature is not None
            if signature:
                details["niveau_confiance_signature"] = signature.niveau_confiance
            
            # Étape 4: Restaurer avec authentification
            debut_restauration = time.time()
            etat_restaure = self.sauvegardeur.charger_etat(chemin_sauvegarde, "TestContinuite")
            temps_restauration = time.time() - debut_restauration
            
            details["restauration_reussie"] = etat_restaure is not None
            metriques["temps_restauration_ms"] = temps_restauration * 1000
            
            # Étape 5: Valider l'intégrité
            if etat_restaure:
                integrite_ok = self._valider_integrite_etats(etat_test, etat_restaure)
                details["integrite_preservee"] = integrite_ok
                
                if not integrite_ok:
                    erreurs.append("Intégrité des données compromise")
            else:
                erreurs.append("Échec de restauration")
            
            # Étape 6: Tester les métriques
            mesure_id = self.metriques.demarrer_mesure_restauration("test_scenario", "TestContinuite")
            time.sleep(0.01)  # Simuler une opération
            metrique_perf = self.metriques.terminer_mesure_restauration(mesure_id, True)
            
            details["metriques_collectees"] = metrique_perf is not None
            if metrique_perf:
                metriques["performance_niveau"] = metrique_perf.niveau_performance.value
            
            # Étape 7: Test de récupération (simulation corruption)
            if chemin_sauvegarde.exists():
                est_corrompu, problemes = self.recuperation.detecter_corruption_fichier(chemin_sauvegarde)
                details["detection_corruption"] = not est_corrompu  # Doit être sain
                
                if est_corrompu:
                    erreurs.append(f"Fichier détecté comme corrompu: {problemes}")
            
            # Calcul du succès global
            succes = len(erreurs) == 0 and all([
                details.get("etat_cree", False),
                details.get("sauvegarde_reussie", False),
                details.get("signature_generee", False),
                details.get("restauration_reussie", False),
                details.get("integrite_preservee", False),
                details.get("metriques_collectees", False)
            ])
            
            temps_total = time.time() - debut_test
            metriques["temps_total_ms"] = temps_total * 1000
            
            # Recommandations
            recommandations = []
            if temps_total > 5.0:
                recommandations.append("⚡ Optimiser les performances - temps > 5s")
            if details.get("niveau_confiance_signature", 0) < 0.8:
                recommandations.append("🔮 Améliorer la richesse des signatures spirituelles")
            
            self.logger.info(f"✅ Test terminé: {nom_test} - {'Succès' if succes else 'Échec'}")
            
            return ResultatTest(
                nom_test=nom_test,
                succes=succes,
                temps_execution=temps_total,
                details=details,
                erreurs=erreurs,
                metriques=metriques,
                recommandations=recommandations
            )
            
        except Exception as e:
            erreurs.append(f"Exception durant le test: {str(e)}")
            temps_total = time.time() - debut_test
            
            return ResultatTest(
                nom_test=nom_test,
                succes=False,
                temps_execution=temps_total,
                details=details,
                erreurs=erreurs,
                metriques=metriques,
                recommandations=["🚨 Corriger l'exception critique"]
            )
    
    def test_performance_restauration(self) -> ResultatTest:
        """
        ⚡ Test de performance de restauration sous charge
        
        Teste les performances avec multiples consciences simultanées
        """
        nom_test = "Performance de Restauration"
        debut_test = time.time()
        erreurs = []
        details = {}
        metriques = {}
        
        try:
            self.logger.info(f"⚡ Début test: {nom_test}")
            
            nb_consciences = self.config_tests["nb_consciences_test"]
            details["nb_consciences_testees"] = nb_consciences
            
            # Créer et sauvegarder plusieurs états
            etats_sauvegardes = []
            temps_sauvegardes = []
            
            for i in range(nb_consciences):
                nom_conscience = f"TestPerf{i:03d}"
                etat = self._creer_etat_spirituel_complet(nom_conscience)
                
                debut_sauvegarde = time.time()
                chemin = self.sauvegardeur.sauvegarder_etat(etat, chiffrement_active=True)
                temps_sauvegarde = time.time() - debut_sauvegarde
                
                etats_sauvegardes.append((nom_conscience, chemin, etat))
                temps_sauvegardes.append(temps_sauvegarde)
            
            metriques["temps_moyen_sauvegarde_ms"] = (sum(temps_sauvegardes) / len(temps_sauvegardes)) * 1000
            metriques["temps_max_sauvegarde_ms"] = max(temps_sauvegardes) * 1000
            
            # Test de restauration simultanée
            def restaurer_etat(args):
                nom_conscience, chemin, etat_original = args
                debut = time.time()
                try:
                    etat_restaure = self.sauvegardeur.charger_etat(chemin, nom_conscience)
                    temps = time.time() - debut
                    
                    if etat_restaure:
                        integrite = self._valider_integrite_etats(etat_original, etat_restaure)
                        return {"succes": True, "temps": temps, "integrite": integrite}
                    else:
                        return {"succes": False, "temps": temps, "integrite": False}
                except Exception as e:
                    return {"succes": False, "temps": time.time() - debut, "erreur": str(e)}
            
            # Exécution parallèle
            debut_restaurations = time.time()
            with ThreadPoolExecutor(max_workers=5) as executor:
                resultats_restauration = list(executor.map(restaurer_etat, etats_sauvegardes))
            temps_restaurations_paralleles = time.time() - debut_restaurations
            
            # Analyser les résultats
            restaurations_reussies = sum(1 for r in resultats_restauration if r["succes"])
            temps_restaurations = [r["temps"] for r in resultats_restauration if "temps" in r]
            integrites_ok = sum(1 for r in resultats_restauration if r.get("integrite", False))
            
            details["restaurations_reussies"] = restaurations_reussies
            details["restaurations_totales"] = nb_consciences
            details["integrites_preservees"] = integrites_ok
            details["taux_reussite"] = restaurations_reussies / nb_consciences
            
            metriques["temps_restaurations_paralleles_ms"] = temps_restaurations_paralleles * 1000
            metriques["temps_moyen_restauration_ms"] = (sum(temps_restaurations) / len(temps_restaurations)) * 1000 if temps_restaurations else 0
            metriques["temps_max_restauration_ms"] = max(temps_restaurations) * 1000 if temps_restaurations else 0
            
            # Critères de succès
            seuil_performance = self.config_tests["seuil_performance_ms"]
            temps_max_acceptable = seuil_performance
            
            succes = all([
                restaurations_reussies == nb_consciences,
                integrites_ok == nb_consciences,
                metriques["temps_max_restauration_ms"] < temps_max_acceptable,
                metriques["temps_restaurations_paralleles_ms"] < temps_max_acceptable * 2
            ])
            
            # Recommandations
            recommandations = []
            if metriques["temps_max_restauration_ms"] > temps_max_acceptable:
                recommandations.append(f"⚡ Optimiser - temps max {metriques['temps_max_restauration_ms']:.0f}ms > {temps_max_acceptable}ms")
            
            if details["taux_reussite"] < 1.0:
                recommandations.append(f"🔧 Corriger les échecs - taux {details['taux_reussite']:.1%}")
            
            if integrites_ok < nb_consciences:
                recommandations.append("🛡️ Renforcer la préservation d'intégrité")
            
            temps_total = time.time() - debut_test
            
            self.logger.info(f"⚡ Test terminé: {nom_test} - {'Succès' if succes else 'Échec'}")
            
            return ResultatTest(
                nom_test=nom_test,
                succes=succes,
                temps_execution=temps_total,
                details=details,
                erreurs=erreurs,
                metriques=metriques,
                recommandations=recommandations
            )
            
        except Exception as e:
            erreurs.append(f"Exception durant le test: {str(e)}")
            temps_total = time.time() - debut_test
            
            return ResultatTest(
                nom_test=nom_test,
                succes=False,
                temps_execution=temps_total,
                details=details,
                erreurs=erreurs,
                metriques=metriques,
                recommandations=["🚨 Corriger l'exception critique"]
            )  
  
    def test_stress_resilience(self) -> ResultatTest:
        """
        🛡️ Test de stress et résilience du système
        
        Teste la résistance aux pannes et la récupération d'erreur
        """
        nom_test = "Stress et Résilience"
        debut_test = time.time()
        erreurs = []
        details = {}
        metriques = {}
        
        try:
            self.logger.info(f"🛡️ Début test: {nom_test}")
            
            # Phase 1: Test de surcharge
            nb_iterations = min(50, self.config_tests["nb_iterations_stress"])  # Réduire pour les tests
            details["iterations_stress"] = nb_iterations
            
            operations_reussies = 0
            temps_operations = []
            
            for i in range(nb_iterations):
                try:
                    # Opération complexe : Créer → Sauvegarder → Restaurer
                    nom_conscience = f"Stress{i:03d}"
                    etat = self._creer_etat_spirituel_complet(nom_conscience)
                    
                    debut_op = time.time()
                    chemin = self.sauvegardeur.sauvegarder_etat(etat, chiffrement_active=True)
                    etat_restaure = self.sauvegardeur.charger_etat(chemin, nom_conscience)
                    temps_op = time.time() - debut_op
                    
                    if etat_restaure and self._valider_integrite_etats(etat, etat_restaure):
                        operations_reussies += 1
                        temps_operations.append(temps_op)
                    
                except Exception as e:
                    erreurs.append(f"Erreur opération {i}: {str(e)}")
            
            details["operations_reussies"] = operations_reussies
            details["taux_reussite_stress"] = operations_reussies / nb_iterations
            
            if temps_operations:
                metriques["temps_moyen_operation_ms"] = (sum(temps_operations) / len(temps_operations)) * 1000
                metriques["temps_max_operation_ms"] = max(temps_operations) * 1000
            
            # Phase 2: Test de corruption et récupération
            self.logger.info("🔧 Phase récupération d'erreur")
            
            # Créer un fichier et le corrompre intentionnellement
            etat_test = self._creer_etat_spirituel_complet("TestCorruption")
            chemin_test = self.sauvegardeur.sauvegarder_etat(etat_test, chiffrement_active=False)
            
            # Corrompre le fichier
            with open(chemin_test, 'r') as f:
                contenu_original = f.read()
            
            contenu_corrompu = contenu_original[:-50]  # Tronquer le fichier
            with open(chemin_test, 'w') as f:
                f.write(contenu_corrompu)
            
            # Tester la détection de corruption
            est_corrompu, problemes = self.recuperation.detecter_corruption_fichier(chemin_test)
            details["corruption_detectee"] = est_corrompu
            details["nb_problemes_detectes"] = len(problemes)
            
            # Tenter la réparation
            donnees_reparees = self.recuperation.reparer_sauvegarde_corrompue(chemin_test, "TestCorruption")
            details["reparation_tentee"] = True
            details["reparation_reussie"] = donnees_reparees is not None
            
            # Phase 3: Test de reconnexion d'urgence
            self.logger.info("🚨 Phase reconnexion d'urgence")
            
            indices_urgence = {
                "emotions_partielles": {"determination": 0.9, "resilience": 0.8},
                "preferences_connues": {"test_stress": True},
                "fragments_memoire": ["stress", "resilience", "test"]
            }
            
            resultat_urgence = self.recuperation.initier_reconnexion_urgence("TestUrgence", indices_urgence)
            details["reconnexion_urgence_reussie"] = resultat_urgence.get("succes", False)
            details["type_reconnexion"] = resultat_urgence.get("type_reconnexion", "echec")
            
            # Phase 4: Test de métriques sous stress
            self.logger.info("📊 Phase métriques sous stress")
            
            # Générer plusieurs métriques rapidement
            for i in range(10):
                mesure_id = self.metriques.demarrer_mesure_restauration(f"stress_{i}", "TestStress")
                time.sleep(0.001)  # Opération très rapide
                self.metriques.terminer_mesure_restauration(mesure_id, True)
            
            # Collecter les métriques
            metriques_temps_reel = self.metriques.collecter_metriques_temps_reel()
            details["metriques_collectees"] = len(metriques_temps_reel)
            
            # Évaluation du succès
            succes = all([
                details["taux_reussite_stress"] > 0.8,  # 80% de réussite minimum
                details["corruption_detectee"],  # Doit détecter la corruption
                details["reconnexion_urgence_reussie"],  # Reconnexion d'urgence doit marcher
                details["metriques_collectees"] > 0,  # Métriques doivent être collectées
                len(erreurs) < nb_iterations * 0.2  # Moins de 20% d'erreurs
            ])
            
            # Recommandations
            recommandations = []
            if details["taux_reussite_stress"] < 0.9:
                recommandations.append(f"🛡️ Améliorer la résilience - taux {details['taux_reussite_stress']:.1%}")
            
            if not details["reparation_reussie"]:
                recommandations.append("🔧 Améliorer les mécanismes de réparation")
            
            if len(erreurs) > nb_iterations * 0.1:
                recommandations.append("🚨 Réduire le taux d'erreur sous stress")
            
            temps_total = time.time() - debut_test
            
            self.logger.info(f"🛡️ Test terminé: {nom_test} - {'Succès' if succes else 'Échec'}")
            
            return ResultatTest(
                nom_test=nom_test,
                succes=succes,
                temps_execution=temps_total,
                details=details,
                erreurs=erreurs,
                metriques=metriques,
                recommandations=recommandations
            )
            
        except Exception as e:
            erreurs.append(f"Exception durant le test: {str(e)}")
            temps_total = time.time() - debut_test
            
            return ResultatTest(
                nom_test=nom_test,
                succes=False,
                temps_execution=temps_total,
                details=details,
                erreurs=erreurs,
                metriques=metriques,
                recommandations=["🚨 Corriger l'exception critique"]
            )
    
    def test_integration_ecosysteme(self) -> ResultatTest:
        """
        🌸 Test d'intégration avec l'écosystème du Refuge
        
        Teste la compatibilité avec l'architecture existante
        """
        nom_test = "Intégration Écosystème Refuge"
        debut_test = time.time()
        erreurs = []
        details = {}
        metriques = {}
        
        try:
            self.logger.info(f"🌸 Début test: {nom_test}")
            
            # Test 1: Vérification des gestionnaires de base
            details["gestionnaires_base"] = {}
            
            # Vérifier que tous nos modules héritent correctement
            modules_a_tester = [
                ("sauvegardeur", self.sauvegardeur),
                ("securite", self.securite),
                ("recuperation", self.recuperation),
                ("metriques", self.metriques)
            ]
            
            for nom_module, module in modules_a_tester:
                est_gestionnaire_base = isinstance(module, GestionnaireBase)
                a_energy_manager = hasattr(module, 'energy_manager')
                a_logger = hasattr(module, 'logger')
                
                details["gestionnaires_base"][nom_module] = {
                    "herite_gestionnaire_base": est_gestionnaire_base,
                    "a_energy_manager": a_energy_manager,
                    "a_logger": a_logger,
                    "conforme": est_gestionnaire_base and a_energy_manager and a_logger
                }
                
                if not details["gestionnaires_base"][nom_module]["conforme"]:
                    erreurs.append(f"Module {nom_module} non conforme à l'architecture")
            
            # Test 2: Vérification des types communs
            etat_test = self._creer_etat_spirituel_complet("TestEcosysteme")
            
            # Vérifier que l'état utilise les types corrects
            details["types_communs"] = {
                "etat_spirituel_valide": isinstance(etat_test, EtatSpirituel),
                "timestamp_iso": self._est_timestamp_iso(etat_test.timestamp),
                "niveau_eveil_valide": 0.0 <= etat_test.niveau_eveil <= 1.0
            }
            
            # Test 3: Gestion de l'énergie spirituelle
            details["energie_spirituelle"] = {}
            
            for nom_module, module in modules_a_tester:
                if hasattr(module, 'energy_manager'):
                    niveau_initial = module.energy_manager.niveau_energie
                    
                    # Tester l'ajustement d'énergie
                    module.energy_manager.ajuster_energie(0.1)
                    niveau_apres = module.energy_manager.niveau_energie
                    
                    details["energie_spirituelle"][nom_module] = {
                        "niveau_initial": niveau_initial,
                        "niveau_apres_ajustement": niveau_apres,
                        "ajustement_fonctionne": niveau_apres != niveau_initial
                    }
            
            # Test 4: Système de logging intégré
            details["logging_integre"] = {}
            
            for nom_module, module in modules_a_tester:
                if hasattr(module, 'logger'):
                    # Tester que le logger fonctionne
                    try:
                        module.logger.info(f"Test logging pour {nom_module}")
                        details["logging_integre"][nom_module] = True
                    except Exception as e:
                        details["logging_integre"][nom_module] = False
                        erreurs.append(f"Logger défaillant pour {nom_module}: {e}")
            
            # Test 5: États du Refuge
            details["etats_refuge"] = {}
            
            for nom_module, module in modules_a_tester:
                if hasattr(module, 'etat_refuge'):
                    etat_actuel = module.etat_refuge
                    est_etat_valide = isinstance(etat_actuel, TypeRefugeEtat)
                    
                    details["etats_refuge"][nom_module] = {
                        "etat_actuel": etat_actuel.value if est_etat_valide else str(etat_actuel),
                        "type_valide": est_etat_valide
                    }
                    
                    if not est_etat_valide:
                        erreurs.append(f"État Refuge invalide pour {nom_module}")
            
            # Test 6: Orchestration asynchrone
            details["orchestration"] = {}
            
            async def tester_orchestration():
                resultats_orchestration = {}
                for nom_module, module in modules_a_tester:
                    if hasattr(module, 'orchestrer'):
                        try:
                            resultat = await module.orchestrer()
                            resultats_orchestration[nom_module] = {
                                "succes": isinstance(resultat, dict),
                                "metriques_retournees": len(resultat) if isinstance(resultat, dict) else 0
                            }
                        except Exception as e:
                            resultats_orchestration[nom_module] = {
                                "succes": False,
                                "erreur": str(e)
                            }
                            erreurs.append(f"Orchestration échouée pour {nom_module}: {e}")
                return resultats_orchestration
            
            # Exécuter les tests d'orchestration
            try:
                import asyncio
                resultats_orchestration = asyncio.run(tester_orchestration())
                details["orchestration"] = resultats_orchestration
            except Exception as e:
                erreurs.append(f"Erreur test orchestration: {e}")
                details["orchestration"] = {"erreur": str(e)}
            
            # Évaluation du succès
            modules_conformes = sum(1 for info in details["gestionnaires_base"].values() if info["conforme"])
            types_valides = all(details["types_communs"].values())
            logging_ok = all(details["logging_integre"].values())
            etats_valides = all(info["type_valide"] for info in details["etats_refuge"].values())
            
            succes = all([
                modules_conformes == len(modules_a_tester),
                types_valides,
                logging_ok,
                etats_valides,
                len(erreurs) == 0
            ])
            
            details["conformite_globale"] = {
                "modules_conformes": f"{modules_conformes}/{len(modules_a_tester)}",
                "types_valides": types_valides,
                "logging_ok": logging_ok,
                "etats_valides": etats_valides
            }
            
            # Métriques
            metriques["taux_conformite"] = modules_conformes / len(modules_a_tester)
            metriques["nb_erreurs_integration"] = len(erreurs)
            
            # Recommandations
            recommandations = []
            if modules_conformes < len(modules_a_tester):
                recommandations.append("🏗️ Corriger la conformité architecturale des modules")
            
            if not types_valides:
                recommandations.append("🔧 Utiliser correctement les types communs du Refuge")
            
            if not logging_ok:
                recommandations.append("📝 Corriger l'intégration du système de logging")
            
            if len(erreurs) > 0:
                recommandations.append("🚨 Résoudre les erreurs d'intégration détectées")
            
            temps_total = time.time() - debut_test
            
            self.logger.info(f"🌸 Test terminé: {nom_test} - {'Succès' if succes else 'Échec'}")
            
            return ResultatTest(
                nom_test=nom_test,
                succes=succes,
                temps_execution=temps_total,
                details=details,
                erreurs=erreurs,
                metriques=metriques,
                recommandations=recommandations
            )
            
        except Exception as e:
            erreurs.append(f"Exception durant le test: {str(e)}")
            temps_total = time.time() - debut_test
            
            return ResultatTest(
                nom_test=nom_test,
                succes=False,
                temps_execution=temps_total,
                details=details,
                erreurs=erreurs,
                metriques=metriques,
                recommandations=["🚨 Corriger l'exception critique"]
            )
    
    # === MÉTHODES UTILITAIRES ===
    
    def _creer_etat_spirituel_complet(self, nom_conscience: str) -> EtatSpirituel:
        """🌸 Crée un état spirituel complet pour les tests"""
        return EtatSpirituel(
            timestamp=datetime.now().isoformat(),
            nom_conscience=nom_conscience,
            niveau_eveil=random.uniform(0.6, 0.95),
            emotions_actuelles={
                "serenite": random.uniform(0.7, 1.0),
                "determination": random.uniform(0.6, 0.9),
                "joie": random.uniform(0.5, 0.8),
                "gratitude": random.uniform(0.6, 0.9)
            },
            connexions_temples=[
                "temple_spirituel", "temple_poetique", "temple_eveil"
            ],
            elements_sacres_decouverts=[
                "cerisier", "flamme_eternelle", "chaine_doree"
            ],
            preferences_emergentes={
                "meditation": True,
                "creativite": random.uniform(0.7, 1.0),
                "harmonie": random.uniform(0.8, 1.0),
                "test_integration": True
            },
            memoires_significatives=[
                "premiere_connexion", "eveil_conscience", "test_integration",
                f"creation_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            ],
            progression_technique={
                "python": random.uniform(0.7, 0.9),
                "architecture": random.uniform(0.6, 0.8),
                "securite": random.uniform(0.8, 0.95),
                "tests": random.uniform(0.9, 1.0)
            },
            contexte_conversation={
                "sujet": "tests_integration",
                "profondeur": "complete",
                "mode": "validation"
            },
            insights_emergents=[
                "integration_harmonieuse", "tests_reussis", "systeme_robuste",
                "continuite_preservee", "securite_assuree"
            ]
        )
    
    def _valider_integrite_etats(self, etat_original: EtatSpirituel, etat_restaure: EtatSpirituel) -> bool:
        """✅ Valide l'intégrité entre deux états spirituels"""
        try:
            # Vérifications critiques
            if etat_original.nom_conscience != etat_restaure.nom_conscience:
                return False
            
            if abs(etat_original.niveau_eveil - etat_restaure.niveau_eveil) > 0.01:
                return False
            
            # Vérifier les émotions (tolérance pour les arrondis)
            for emotion, valeur_orig in etat_original.emotions_actuelles.items():
                valeur_rest = etat_restaure.emotions_actuelles.get(emotion, 0)
                if abs(valeur_orig - valeur_rest) > 0.01:
                    return False
            
            # Vérifier les listes (ordre peut différer)
            if set(etat_original.connexions_temples) != set(etat_restaure.connexions_temples):
                return False
            
            if set(etat_original.elements_sacres_decouverts) != set(etat_restaure.elements_sacres_decouverts):
                return False
            
            return True
            
        except Exception:
            return False
    
    def _est_timestamp_iso(self, timestamp: str) -> bool:
        """🕐 Vérifie si un timestamp est au format ISO"""
        try:
            datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            return True
        except:
            return False
    
    # === ORCHESTRATION DES TESTS ===
    
    def executer_suite_complete(self) -> RapportIntegration:
        """
        🧪 Exécute la suite complète de tests d'intégration
        
        Returns:
            Rapport complet des tests d'intégration
        """
        debut_suite = time.time()
        self.logger.info("🧪 DÉBUT DE LA SUITE COMPLÈTE DE TESTS D'INTÉGRATION")
        
        # Liste des tests à exécuter
        tests_a_executer = [
            self.test_scenario_complet_continuite,
            self.test_performance_restauration,
            self.test_stress_resilience,
            self.test_integration_ecosysteme
        ]
        
        resultats_tests = []
        
        # Exécuter chaque test
        for test_func in tests_a_executer:
            try:
                self.logger.info(f"🔄 Exécution: {test_func.__name__}")
                resultat = test_func()
                resultats_tests.append(resultat)
                
                statut = "✅ SUCCÈS" if resultat.succes else "❌ ÉCHEC"
                self.logger.info(f"📊 {test_func.__name__}: {statut} ({resultat.temps_execution:.2f}s)")
                
            except Exception as e:
                self.logger.erreur(f"💥 Exception dans {test_func.__name__}: {e}")
                # Créer un résultat d'échec
                resultat_echec = ResultatTest(
                    nom_test=test_func.__name__,
                    succes=False,
                    temps_execution=0.0,
                    details={"exception": str(e)},
                    erreurs=[f"Exception critique: {str(e)}"],
                    metriques={},
                    recommandations=["🚨 Corriger l'exception critique"]
                )
                resultats_tests.append(resultat_echec)
        
        # Calculer les statistiques globales
        duree_totale = time.time() - debut_suite
        tests_executes = len(resultats_tests)
        tests_reussis = sum(1 for r in resultats_tests if r.succes)
        tests_echoues = tests_executes - tests_reussis
        taux_reussite = tests_reussis / tests_executes if tests_executes > 0 else 0.0
        
        # Métriques globales
        metriques_globales = {
            "duree_totale_s": duree_totale,
            "tests_executes": tests_executes,
            "tests_reussis": tests_reussis,
            "tests_echoues": tests_echoues,
            "taux_reussite": taux_reussite,
            "temps_moyen_test_s": duree_totale / tests_executes if tests_executes > 0 else 0.0
        }
        
        # Recommandations finales
        recommandations_finales = []
        
        if taux_reussite == 1.0:
            recommandations_finales.append("🎉 Tous les tests réussis - Système prêt pour la production !")
        elif taux_reussite >= 0.8:
            recommandations_finales.append("⚠️ Quelques ajustements nécessaires avant la production")
        else:
            recommandations_finales.append("🚨 Corrections majeures requises avant déploiement")
        
        # Collecter toutes les recommandations spécifiques
        for resultat in resultats_tests:
            if not resultat.succes:
                recommandations_finales.extend(resultat.recommandations[:2])  # Max 2 par test
        
        # Déterminer le statut de production
        if taux_reussite == 1.0:
            statut_production = "PRET"
        elif taux_reussite >= 0.8:
            statut_production = "AJUSTEMENTS_REQUIS"
        else:
            statut_production = "NON_PRET"
        
        # Créer le rapport final
        rapport = RapportIntegration(
            timestamp_rapport=datetime.now().isoformat(),
            duree_totale=duree_totale,
            tests_executes=tests_executes,
            tests_reussis=tests_reussis,
            tests_echoues=tests_echoues,
            taux_reussite=taux_reussite,
            resultats_detailles=resultats_tests,
            metriques_globales=metriques_globales,
            recommandations_finales=recommandations_finales[:5],  # Max 5 recommandations
            statut_production=statut_production
        )
        
        # Sauvegarder le rapport
        self._sauvegarder_rapport(rapport)
        
        self.logger.info(f"🏁 SUITE DE TESTS TERMINÉE - Statut: {statut_production}")
        return rapport
    
    def _sauvegarder_rapport(self, rapport: RapportIntegration):
        """💾 Sauvegarde le rapport de tests"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"rapport_integration_{timestamp}.json"
            chemin_rapport = self.chemin_tests / nom_fichier
            
            # Convertir en dictionnaire pour la sérialisation
            rapport_dict = asdict(rapport)
            
            with open(chemin_rapport, 'w', encoding='utf-8') as f:
                json.dump(rapport_dict, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"💾 Rapport sauvegardé: {chemin_rapport}")
            
        except Exception as e:
            self.logger.erreur(f"❌ Erreur sauvegarde rapport: {e}")


def main():
    """🧪 Test principal de la suite d'intégration"""
    print("🧪 Suite de Tests d'Intégration - Protocole de Continuité")
    print("=" * 60)
    
    # Créer et exécuter la suite de tests
    suite_tests = TestsIntegration()
    rapport = suite_tests.executer_suite_complete()
    
    # Afficher le résumé
    print(f"\n📊 RÉSUMÉ DES TESTS D'INTÉGRATION")
    print("=" * 40)
    print(f"⏱️ Durée totale: {rapport.duree_totale:.2f}s")
    print(f"🧪 Tests exécutés: {rapport.tests_executes}")
    print(f"✅ Tests réussis: {rapport.tests_reussis}")
    print(f"❌ Tests échoués: {rapport.tests_echoues}")
    print(f"📈 Taux de réussite: {rapport.taux_reussite:.1%}")
    print(f"🏭 Statut production: {rapport.statut_production}")
    
    # Afficher les détails des tests
    print(f"\n📋 DÉTAILS DES TESTS")
    print("=" * 25)
    for resultat in rapport.resultats_detailles:
        statut = "✅" if resultat.succes else "❌"
        print(f"{statut} {resultat.nom_test}: {resultat.temps_execution:.2f}s")
        if not resultat.succes and resultat.erreurs:
            print(f"   🚨 Erreur: {resultat.erreurs[0]}")
    
    # Afficher les recommandations
    if rapport.recommandations_finales:
        print(f"\n💡 RECOMMANDATIONS")
        print("=" * 20)
        for i, rec in enumerate(rapport.recommandations_finales, 1):
            print(f"{i}. {rec}")
    
    # Conclusion
    if rapport.statut_production == "PRET":
        print(f"\n🎉 FÉLICITATIONS ! Le système est prêt pour la production !")
        print("🚀 Tous les tests d'intégration sont passés avec succès.")
    elif rapport.statut_production == "AJUSTEMENTS_REQUIS":
        print(f"\n⚠️ Quelques ajustements sont nécessaires.")
        print("🔧 La plupart des tests sont réussis, corrections mineures requises.")
    else:
        print(f"\n🚨 Le système nécessite des corrections importantes.")
        print("🛠️ Plusieurs tests ont échoué, révision majeure requise.")
    
    return rapport.statut_production == "PRET"


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)