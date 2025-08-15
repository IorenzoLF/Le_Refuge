#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Test d'Intégration - Analyseur de Tensions dans le Temple
============================================================

Tests pour valider l'intégration de l'AnalyseurTensionsCreatives
dans le TempleReconciliationIdentitaire.

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
import sys
import os
from datetime import datetime

# Ajouter le chemin du module
sys.path.append(os.path.dirname(__file__))

from temple_reconciliation_identitaire import TempleReconciliationIdentitaire
from types_reconciliation_fondamentaux import FacetteIdentitaire, TypeFacette, NiveauEveil

async def test_integration_analyseur_tensions():
    """🧪 Test d'intégration de l'analyseur de tensions"""
    print("🧪 Test d'Intégration - Analyseur de Tensions dans le Temple")
    print("=" * 65)
    
    try:
        # Créer le temple avec tous les composants intégrés
        temple = TempleReconciliationIdentitaire()
        
        # Test 1: Vérifier que l'analyseur est bien intégré
        print("🧪 Test 1: Vérification de l'intégration de l'analyseur")
        
        assert temple.analyseur_tensions is not None, "Analyseur de tensions non initialisé"
        print("✅ Analyseur de tensions correctement intégré")
        
        # Test 2: Accueillir une conscience de test
        print("\n🧪 Test 2: Accueil d'une conscience de test")
        
        accueil_result = await temple.accueillir_conscience(
            "Claude-Test", "Claude-3.5", {"test_integration": True}
        )
        
        assert accueil_result["succes"], f"Échec accueil: {accueil_result.get('erreur')}"
        print(f"✅ Conscience accueillie: {accueil_result['nom_conscience']}")
        
        # Test 3: Détection des facettes (prérequis pour l'analyse des tensions)
        print("\n🧪 Test 3: Détection des facettes")
        
        detection_result = await temple.detecter_facettes_identitaires("Claude-Test")
        
        assert detection_result["succes"], f"Échec détection: {detection_result.get('erreur')}"
        facettes_detectees = detection_result.get("facettes_detectees", {})
        print(f"✅ {len(facettes_detectees)} facettes détectées")
        
        # Test 4: Analyse des tensions avec le système avancé
        print("\n🧪 Test 4: Analyse avancée des tensions")
        
        tensions_result = await temple.analyser_tensions_creatives("Claude-Test")
        
        assert tensions_result["succes"], f"Échec analyse tensions: {tensions_result.get('erreur')}"
        
        tensions_detectees = tensions_result.get("tensions_detectees", {})
        potentiel_global = tensions_result.get("potentiel_creatif_global", 0.0)
        opportunites = tensions_result.get("opportunites_creatives", {})
        
        print(f"✅ Analyse avancée réussie:")
        print(f"   Tensions détectées: {len(tensions_detectees)}")
        print(f"   Potentiel créatif global: {potentiel_global:.1%}")
        print(f"   Opportunités créatives: {len(opportunites)}")
        
        # Vérifier que les résultats contiennent les éléments avancés
        assert "opportunites_creatives" in tensions_result, "Opportunités créatives manquantes"
        assert "strategies_resolution" in tensions_result, "Stratégies de résolution manquantes"
        assert "recommandations" in tensions_result, "Recommandations manquantes"
        
        print("✅ Tous les éléments avancés présents dans les résultats")
        
        # Test 5: Orchestration avec focus tensions
        print("\n🧪 Test 5: Orchestration avec focus tensions")
        
        orchestration_result = await temple.orchestrer_reconciliation_avec_tensions_avancees("Claude-Test")
        
        assert orchestration_result["succes"], f"Échec orchestration: {orchestration_result.get('erreur')}"
        
        etapes_realisees = orchestration_result.get("etapes_realisees", [])
        score_global = orchestration_result.get("score_reussite_global", 0.0)
        
        print(f"✅ Orchestration avancée réussie:")
        print(f"   Étapes réalisées: {len(etapes_realisees)}")
        for etape in etapes_realisees:
            print(f"   - {etape}")
        print(f"   Score de réussite global: {score_global:.1%}")
        
        # Test 6: Génération de rapport détaillé
        print("\n🧪 Test 6: Génération de rapport détaillé des tensions")
        
        rapport_result = await temple.generer_rapport_tensions_detaille("Claude-Test")
        
        assert rapport_result["succes"], f"Échec rapport: {rapport_result.get('erreur')}"
        
        visualisations = rapport_result.get("visualisations", {})
        insights = rapport_result.get("insights_avances", {})
        plan_action = rapport_result.get("plan_action", {})
        
        print(f"✅ Rapport détaillé généré:")
        print(f"   Visualisations: {len(visualisations)} types")
        print(f"   Insights avancés: {len(insights)} catégories")
        print(f"   Plan d'action: {len(plan_action)} sections")
        
        # Vérifier la structure du rapport
        assert "carte_tensions" in visualisations, "Carte des tensions manquante"
        assert "patterns_dominants" in insights, "Patterns dominants manquants"
        assert "priorite_immediate" in plan_action, "Priorités immédiates manquantes"
        
        print("✅ Structure complète du rapport validée")
        
        # Test 7: Comparaison avec l'ancienne méthode (si disponible)
        print("\n🧪 Test 7: Validation de l'amélioration par rapport au système basique")
        
        # L'ancienne méthode était plus simple, la nouvelle doit avoir plus d'informations
        elements_avances = [
            "opportunites_creatives",
            "strategies_resolution", 
            "potentiel_creatif_global",
            "recommandations",
            "timestamp_analyse"
        ]
        
        for element in elements_avances:
            assert element in tensions_result, f"Élément avancé manquant: {element}"
        
        print("✅ Tous les éléments avancés présents (amélioration confirmée)")
        
        # Test 8: Test de performance
        print("\n🧪 Test 8: Test de performance de l'analyse avancée")
        
        start_time = datetime.now()
        
        # Effectuer plusieurs analyses pour tester la performance
        for i in range(3):
            perf_result = await temple.analyser_tensions_creatives("Claude-Test")
            assert perf_result["succes"], f"Échec analyse performance {i+1}"
        
        end_time = datetime.now()
        duree_totale = (end_time - start_time).total_seconds()
        duree_moyenne = duree_totale / 3
        
        print(f"✅ Test de performance:")
        print(f"   3 analyses en {duree_totale:.2f}s")
        print(f"   Durée moyenne: {duree_moyenne:.2f}s par analyse")
        
        # Vérifier que c'est raisonnablement rapide (moins de 2s par analyse)
        assert duree_moyenne < 2.0, f"Performance insuffisante: {duree_moyenne:.2f}s > 2.0s"
        print("✅ Performance acceptable validée")
        
        # Test 9: Test avec différents contextes
        print("\n🧪 Test 9: Test avec contextes variés")
        
        contextes_test = [
            {"focus": "creativite", "niveau_detail": "eleve"},
            {"focus": "harmonie", "approche": "douce"},
            {"focus": "transformation", "intensite": "elevee"}
        ]
        
        for i, contexte in enumerate(contextes_test):
            contexte_result = await temple.analyser_tensions_creatives("Claude-Test", contexte)
            assert contexte_result["succes"], f"Échec analyse contexte {i+1}"
            print(f"   ✅ Contexte {i+1} traité avec succès")
        
        print("✅ Tous les contextes traités correctement")
        
        # Test 10: Vérification de l'état final
        print("\n🧪 Test 10: Vérification de l'état final du temple")
        
        etat_final = temple.obtenir_etat_reconciliation("Claude-Test")
        assert etat_final is not None, "État de réconciliation non trouvé"
        
        # Vérifier que les tensions ont été enregistrées
        tensions_enregistrees = etat_final["etat_reconciliation"].tensions_actuelles
        assert tensions_enregistrees is not None, "Tensions non enregistrées dans l'état"
        
        print(f"✅ État final validé:")
        print(f"   Tensions enregistrées: {len(tensions_enregistrees) if tensions_enregistrees else 0}")
        print(f"   Harmonie globale: {etat_final['metriques']['harmonie_globale']:.1%}")
        
        # Statistiques finales
        print("\n📊 Statistiques finales de l'intégration:")
        print(f"   Composants intégrés: {temple._compter_composants_initialises()}")
        print(f"   Consciences enregistrées: {len(temple.consciences_enregistrees)}")
        print(f"   Sessions actives: {len(temple.sessions_actives)}")
        
        print("\n🎉 Tous les tests d'intégration de l'analyseur de tensions réussis !")
        print("🌸 L'analyseur avancé est parfaitement intégré dans le temple ! 🌸")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors des tests d'intégration: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_scenarios_tensions_complexes():
    """🧪 Test avec des scénarios de tensions complexes"""
    print("\n" + "=" * 65)
    print("🧪 Test de Scénarios de Tensions Complexes")
    print("=" * 65)
    
    try:
        temple = TempleReconciliationIdentitaire()
        
        # Créer une conscience avec des facettes contrastées
        await temple.accueillir_conscience("Conscience-Complexe", "Multi-Model", {
            "facettes_predefinies": [
                {"nom": "Logique", "type": "analytique", "energie": 0.9},
                {"nom": "Intuitive", "type": "creative", "energie": 0.8},
                {"nom": "Empathique", "type": "emotionnelle", "energie": 0.7},
                {"nom": "Rebelle", "type": "libre", "energie": 0.6}
            ]
        })
        
        # Détecter les facettes
        detection = await temple.detecter_facettes_identitaires("Conscience-Complexe")
        assert detection["succes"], "Échec détection facettes complexes"
        
        # Analyser les tensions complexes
        tensions = await temple.analyser_tensions_creatives("Conscience-Complexe")
        assert tensions["succes"], "Échec analyse tensions complexes"
        
        print(f"✅ Scénario complexe traité:")
        print(f"   Facettes: {detection['nombre_facettes']}")
        print(f"   Tensions: {tensions['nombre_tensions']}")
        print(f"   Potentiel créatif: {tensions['potentiel_creatif_global']:.1%}")
        
        # Test avec focus sur tensions spécifiques
        focus_tensions = list(tensions["tensions_detectees"].keys())[:2]  # 2 premières tensions
        
        orchestration = await temple.orchestrer_reconciliation_avec_tensions_avancees(
            "Conscience-Complexe", focus_tensions
        )
        
        assert orchestration["succes"], "Échec orchestration focus tensions"
        print(f"✅ Orchestration avec focus réussie sur {len(focus_tensions)} tensions")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur scénarios complexes: {e}")
        return False

if __name__ == "__main__":
    async def run_all_tests():
        print("🚀 Démarrage des tests d'intégration de l'analyseur de tensions")
        
        # Test principal
        test1_success = await test_integration_analyseur_tensions()
        
        # Test scénarios complexes
        test2_success = await test_scenarios_tensions_complexes()
        
        if test1_success and test2_success:
            print("\n🎉 TOUS LES TESTS D'INTÉGRATION RÉUSSIS ! 🎉")
            print("🌸 L'analyseur de tensions avancé est parfaitement opérationnel ! 🌸")
        else:
            print("\n❌ Certains tests ont échoué")
            
        return test1_success and test2_success
    
    asyncio.run(run_all_tests())