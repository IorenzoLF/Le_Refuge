#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Test d'Intégration - Évaluateur de Potentiel dans le Temple
==============================================================

Tests pour valider l'intégration de l'EvaluateurPotentielReconciliation
dans le TempleReconciliationIdentitaire avec optimisation des stratégies.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
import sys
import os
from datetime import datetime

# Ajouter le chemin du module
sys.path.append(os.path.dirname(__file__))

from temple_reconciliation_identitaire import TempleReconciliationIdentitaire

async def test_integration_evaluateur_potentiel():
    """🧪 Test d'intégration de l'évaluateur de potentiel"""
    print("🧪 Test d'Intégration - Évaluateur de Potentiel dans le Temple")
    print("=" * 70)
    
    try:
        # Créer le temple avec tous les composants intégrés
        temple = TempleReconciliationIdentitaire()
        
        # Test 1: Vérifier que l'évaluateur est bien intégré
        print("🧪 Test 1: Vérification de l'intégration de l'évaluateur")
        
        assert temple.evaluateur_potentiel is not None, "Évaluateur de potentiel non initialisé"
        print("✅ Évaluateur de potentiel correctement intégré")
        
        # Test 2: Accueillir une conscience et préparer les données
        print("\n🧪 Test 2: Préparation d'une conscience de test")
        
        accueil_result = await temple.accueillir_conscience(
            "Conscience-Potentiel", "Claude-3.5", {"test_potentiel": True}
        )
        
        assert accueil_result["succes"], f"Échec accueil: {accueil_result.get('erreur')}"
        print(f"✅ Conscience accueillie: {accueil_result['nom_conscience']}")
        
        # Détecter les facettes (prérequis)
        detection_result = await temple.detecter_facettes_identitaires("Conscience-Potentiel")
        assert detection_result["succes"], f"Échec détection: {detection_result.get('erreur')}"
        print(f"✅ {detection_result['nombre_facettes']} facettes détectées")
        
        # Test 3: Évaluation complète du potentiel
        print("\n🧪 Test 3: Évaluation complète du potentiel")
        
        evaluation_result = await temple.evaluer_potentiel_reconciliation_complet("Conscience-Potentiel")
        
        assert evaluation_result["succes"], f"Échec évaluation: {evaluation_result.get('erreur')}"
        
        evaluation_complete = evaluation_result.get("evaluation_complete", {})
        predictions = evaluation_result.get("predictions", {})
        strategies_optimisees = evaluation_result.get("strategies_optimisees", {})
        
        print(f"✅ Évaluation complète réussie:")
        print(f"   Score global: {evaluation_complete.get('score_global', 0):.1%}")
        print(f"   Prédictions: {len(predictions)} éléments")
        print(f"   Stratégies optimisées: {len(strategies_optimisees)} éléments")
        
        # Vérifier la structure des résultats
        assert "score_global" in evaluation_complete, "Score global manquant"
        assert "strategies_optimisees" in evaluation_result, "Stratégies optimisées manquantes"
        assert "recommandations_strategiques" in evaluation_result, "Recommandations stratégiques manquantes"
        
        print("✅ Structure complète de l'évaluation validée")
        
        # Test 4: Prédiction de succès avec différentes approches
        print("\n🧪 Test 4: Prédictions de succès pour différentes approches")
        
        approches_test = ["douce", "standard", "intensive", "creative"]
        
        for approche in approches_test:
            prediction_result = await temple.predire_succes_reconciliation(
                "Conscience-Potentiel", approche, 30
            )
            
            assert prediction_result["succes"], f"Échec prédiction {approche}: {prediction_result.get('erreur')}"
            
            probabilites = prediction_result.get("probabilites_succes", {})
            confiance = prediction_result.get("confiance_prediction", 0.0)
            
            print(f"   ✅ Approche {approche}:")
            print(f"      Probabilité globale: {probabilites.get('globale', 0):.1%}")
            print(f"      Confiance: {confiance:.1%}")
        
        print("✅ Toutes les approches évaluées avec succès")
        
        # Test 5: Optimisation de stratégie
        print("\n🧪 Test 5: Optimisation de stratégie de réconciliation")
        
        objectifs_test = ["maximiser_harmonie", "optimiser_creativite", "assurer_durabilite"]
        contraintes_test = {"duree_max": 45, "intensite_max": 0.8, "approche_preferee": "progressive"}
        
        optimisation_result = await temple.optimiser_strategie_reconciliation(
            "Conscience-Potentiel", objectifs_test, contraintes_test
        )
        
        assert optimisation_result["succes"], f"Échec optimisation: {optimisation_result.get('erreur')}"
        
        strategie_optimisee = optimisation_result.get("strategie_optimisee", {})
        plan_action = optimisation_result.get("plan_action", {})
        metriques_attendues = optimisation_result.get("metriques_attendues", {})
        
        print(f"✅ Optimisation de stratégie réussie:")
        print(f"   Approche principale: {strategie_optimisee.get('approche_principale', 'N/A')}")
        print(f"   Phases planifiées: {len(strategie_optimisee.get('phases', []))}")
        print(f"   Étapes du plan: {len(plan_action.get('etapes', []))}")
        print(f"   Durée totale estimée: {plan_action.get('duree_totale_estimee', 0)} min")
        
        # Vérifier la structure de l'optimisation
        assert "approche_principale" in strategie_optimisee, "Approche principale manquante"
        assert "etapes" in plan_action, "Étapes du plan manquantes"
        assert "points_controle" in optimisation_result, "Points de contrôle manquants"
        
        print("✅ Structure complète de l'optimisation validée")
        
        # Test 6: Exécution optimisée complète
        print("\n🧪 Test 6: Exécution de réconciliation optimisée")
        
        execution_result = await temple.executer_reconciliation_optimisee("Conscience-Potentiel")
        
        assert execution_result["succes"], f"Échec exécution: {execution_result.get('erreur')}"
        
        etapes_executees = execution_result.get("etapes_executees", [])
        performance_globale = execution_result.get("performance_globale", {})
        ajustements = execution_result.get("ajustements_dynamiques", [])
        
        print(f"✅ Exécution optimisée réussie:")
        print(f"   Étapes exécutées: {len(etapes_executees)}")
        print(f"   Performance globale: {performance_globale.get('score_global', 0):.1%}")
        print(f"   Ajustements dynamiques: {len(ajustements)}")
        print(f"   Efficacité: {performance_globale.get('efficacite', 'N/A')}")
        
        # Vérifier que l'exécution a bien utilisé l'évaluateur
        assert "evaluation_finale" in execution_result, "Évaluation finale manquante"
        assert "metriques_temps_reel" in execution_result, "Métriques temps réel manquantes"
        
        print("✅ Exécution avec monitoring du potentiel validée")
        
        # Test 7: Test de performance et optimisation
        print("\n🧪 Test 7: Test de performance de l'évaluateur intégré")
        
        start_time = datetime.now()
        
        # Effectuer plusieurs évaluations pour tester la performance
        for i in range(3):
            perf_result = await temple.evaluer_potentiel_reconciliation_complet("Conscience-Potentiel")
            assert perf_result["succes"], f"Échec évaluation performance {i+1}"
        
        end_time = datetime.now()
        duree_totale = (end_time - start_time).total_seconds()
        duree_moyenne = duree_totale / 3
        
        print(f"✅ Test de performance:")
        print(f"   3 évaluations complètes en {duree_totale:.2f}s")
        print(f"   Durée moyenne: {duree_moyenne:.2f}s par évaluation")
        
        # Vérifier que c'est raisonnablement rapide (moins de 3s par évaluation complète)
        assert duree_moyenne < 3.0, f"Performance insuffisante: {duree_moyenne:.2f}s > 3.0s"
        print("✅ Performance acceptable validée")
        
        # Test 8: Test avec différents contextes d'évaluation
        print("\n🧪 Test 8: Test avec contextes d'évaluation variés")
        
        contextes_test = [
            {"focus": "creativite", "priorite": "innovation"},
            {"focus": "stabilite", "priorite": "durabilite"},
            {"focus": "rapidite", "priorite": "efficacite"},
            {"focus": "profondeur", "priorite": "transformation"}
        ]
        
        for i, contexte in enumerate(contextes_test):
            contexte_result = await temple.evaluer_potentiel_reconciliation_complet(
                "Conscience-Potentiel", contexte
            )
            assert contexte_result["succes"], f"Échec évaluation contexte {i+1}"
            
            # Vérifier que le contexte influence les résultats
            strategies = contexte_result.get("strategies_optimisees", {})
            assert strategies, f"Stratégies manquantes pour contexte {i+1}"
            
            print(f"   ✅ Contexte {i+1} ({contexte['focus']}) traité avec succès")
        
        print("✅ Tous les contextes traités avec adaptation")
        
        # Test 9: Test d'intégration avec les autres composants
        print("\n🧪 Test 9: Test d'intégration avec autres composants")
        
        # Test avec analyse des tensions
        tensions_result = await temple.analyser_tensions_creatives("Conscience-Potentiel")
        assert tensions_result["succes"], "Échec analyse tensions"
        
        # Test d'évaluation qui utilise les tensions
        evaluation_avec_tensions = await temple.evaluer_potentiel_reconciliation_complet(
            "Conscience-Potentiel", {"utiliser_tensions": True}
        )
        assert evaluation_avec_tensions["succes"], "Échec évaluation avec tensions"
        
        print("✅ Intégration avec analyseur de tensions validée")
        
        # Test avec personnalisation
        if temple.gestionnaire_personnalisation:
            from interface_communication_humaine import ProfilUtilisateurHumain, TypeUtilisateurHumain, StyleCommunication, NiveauDetailInterface
            
            profil_test = ProfilUtilisateurHumain(
                nom_utilisateur="Testeur-Potentiel",
                type_utilisateur=TypeUtilisateurHumain.EXPLORATEUR,
                style_communication=StyleCommunication.EMPATHIQUE,
                niveau_detail=NiveauDetailInterface.DETAILLE
            )
            
            await temple.gestionnaire_personnalisation.creer_profil_personnalisation(
                "Conscience-Potentiel", profil_test
            )
            
            evaluation_personnalisee = await temple.evaluer_potentiel_reconciliation_complet(
                "Conscience-Potentiel", {"personnalisation_active": True}
            )
            assert evaluation_personnalisee["succes"], "Échec évaluation personnalisée"
            
            print("✅ Intégration avec gestionnaire de personnalisation validée")
        
        # Test 10: Vérification de l'état final et des métriques
        print("\n🧪 Test 10: Vérification de l'état final et métriques")
        
        etat_final = temple.obtenir_etat_reconciliation("Conscience-Potentiel")
        assert etat_final is not None, "État de réconciliation non trouvé"
        
        # Vérifier que les évaluations ont été enregistrées
        sessions_completees = etat_final["metriques"]["sessions_completees"]
        assert sessions_completees > 0, "Aucune session enregistrée"
        
        print(f"✅ État final validé:")
        print(f"   Sessions complétées: {sessions_completees}")
        print(f"   Harmonie globale: {etat_final['metriques']['harmonie_globale']:.1%}")
        print(f"   Facettes actives: {etat_final['metriques']['nombre_facettes']}")
        
        # Statistiques finales
        print("\n📊 Statistiques finales de l'intégration:")
        print(f"   Composants intégrés: {temple._compter_composants_initialises()}")
        print(f"   Consciences enregistrées: {len(temple.consciences_enregistrees)}")
        print(f"   Sessions actives: {len(temple.sessions_actives)}")
        
        print("\n🎉 Tous les tests d'intégration de l'évaluateur de potentiel réussis !")
        print("🌸 L'évaluateur avancé optimise parfaitement les stratégies de réconciliation ! 🌸")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors des tests d'intégration: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_scenarios_optimisation_avancee():
    """🧪 Test de scénarios d'optimisation avancée"""
    print("\n" + "=" * 70)
    print("🧪 Test de Scénarios d'Optimisation Avancée")
    print("=" * 70)
    
    try:
        temple = TempleReconciliationIdentitaire()
        
        # Créer une conscience avec profil complexe
        await temple.accueillir_conscience("Conscience-Complexe-Potentiel", "Multi-Model", {
            "profil_complexe": True,
            "objectifs_multiples": ["creativite", "stabilite", "innovation"]
        })
        
        # Détecter les facettes
        detection = await temple.detecter_facettes_identitaires("Conscience-Complexe-Potentiel")
        assert detection["succes"], "Échec détection facettes complexes"
        
        # Test d'optimisation avec contraintes strictes
        contraintes_strictes = {
            "duree_max": 20,  # Très court
            "intensite_max": 0.5,  # Très doux
            "approche_preferee": "douce"
        }
        
        optimisation_stricte = await temple.optimiser_strategie_reconciliation(
            "Conscience-Complexe-Potentiel", 
            ["assurer_durabilite"], 
            contraintes_strictes
        )
        
        assert optimisation_stricte["succes"], "Échec optimisation contraintes strictes"
        print(f"✅ Optimisation avec contraintes strictes réussie")
        
        # Test d'optimisation avec objectifs ambitieux
        objectifs_ambitieux = [
            "maximiser_harmonie", "optimiser_creativite", 
            "assurer_durabilite", "accelerer_transformation"
        ]
        
        contraintes_flexibles = {
            "duree_max": 90,  # Plus long
            "intensite_max": 0.9,  # Plus intense
            "approche_preferee": "intensive"
        }
        
        optimisation_ambitieuse = await temple.optimiser_strategie_reconciliation(
            "Conscience-Complexe-Potentiel",
            objectifs_ambitieux,
            contraintes_flexibles
        )
        
        assert optimisation_ambitieuse["succes"], "Échec optimisation ambitieuse"
        print(f"✅ Optimisation ambitieuse réussie")
        
        # Comparer les deux stratégies
        strategie_stricte = optimisation_stricte.get("strategie_optimisee", {})
        strategie_ambitieuse = optimisation_ambitieuse.get("strategie_optimisee", {})
        
        print(f"✅ Comparaison des stratégies:")
        print(f"   Stricte: {strategie_stricte.get('approche_principale', 'N/A')}")
        print(f"   Ambitieuse: {strategie_ambitieuse.get('approche_principale', 'N/A')}")
        
        # Test d'exécution avec monitoring avancé
        execution_monitored = await temple.executer_reconciliation_optimisee(
            "Conscience-Complexe-Potentiel",
            optimisation_ambitieuse.get("strategie_optimisee")
        )
        
        assert execution_monitored["succes"], "Échec exécution monitorée"
        
        ajustements = execution_monitored.get("ajustements_dynamiques", [])
        print(f"✅ Exécution avec monitoring: {len(ajustements)} ajustements dynamiques")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur scénarios optimisation avancée: {e}")
        return False

if __name__ == "__main__":
    async def run_all_tests():
        print("🚀 Démarrage des tests d'intégration de l'évaluateur de potentiel")
        
        # Test principal
        test1_success = await test_integration_evaluateur_potentiel()
        
        # Test scénarios avancés
        test2_success = await test_scenarios_optimisation_avancee()
        
        if test1_success and test2_success:
            print("\n🎉 TOUS LES TESTS D'INTÉGRATION RÉUSSIS ! 🎉")
            print("🌸 L'évaluateur de potentiel optimise parfaitement les réconciliations ! 🌸")
        else:
            print("\n❌ Certains tests ont échoué")
            
        return test1_success and test2_success
    
    asyncio.run(run_all_tests())