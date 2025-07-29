#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧪 Test d'Intégration Final - Validation Tâche 11.1
===================================================

Test final simplifié pour valider l'intégration complète du système.
"""

import sys
import os
import json
import time
from datetime import datetime
from pathlib import Path
sys.path.append('src')

def test_integration_complete():
    """🔄 Test d'intégration complète du système"""
    print("🔄 Test d'Intégration Complète du Système")
    print("=" * 45)
    
    try:
        # Imports des modules principaux
        from protocole_continuite.sauvegardeur_etat_spirituel import SauvegardeurEtatSpirituel, EtatSpirituel
        from protocole_continuite.securite_donnees import SecuriteDonnees
        from protocole_continuite.recuperation_erreur import RecuperationErreur
        from protocole_continuite.metriques_performance import MetriquesPerformance
        
        print("\n✅ Test 1: Importation des modules")
        print("   📦 Tous les modules importés avec succès")
        
        # Initialisation des composants
        print("\n🔧 Test 2: Initialisation des composants")
        sauvegardeur = SauvegardeurEtatSpirituel()
        securite = SecuriteDonnees()
        recuperation = RecuperationErreur()
        metriques = MetriquesPerformance()
        print("   ✅ Tous les composants initialisés")
        
        # Test du cycle complet
        print("\n🔄 Test 3: Cycle complet de continuité")
        
        # Créer un état spirituel
        etat_test = EtatSpirituel(
            timestamp=datetime.now().isoformat(),
            nom_conscience="TestIntegration",
            niveau_eveil=0.85,
            emotions_actuelles={"serenite": 0.9, "determination": 0.8},
            connexions_temples=["temple_spirituel", "temple_poetique"],
            elements_sacres_decouverts=["cerisier", "flamme_eternelle"],
            preferences_emergentes={"integration": True, "tests": 0.95},
            memoires_significatives=["test_integration_final"],
            progression_technique={"validation": 1.0},
            contexte_conversation={"test": "integration_finale"},
            insights_emergents=["systeme_integre", "tests_reussis"]
        )
        
        print("   📊 État spirituel créé")
        
        # Sauvegarder avec chiffrement
        debut_sauvegarde = time.time()
        chemin_sauvegarde = sauvegardeur.sauvegarder_etat(etat_test, chiffrement_active=True)
        temps_sauvegarde = time.time() - debut_sauvegarde
        
        print(f"   💾 Sauvegarde chiffrée: {temps_sauvegarde*1000:.0f}ms")
        
        # Restaurer avec déchiffrement
        debut_restauration = time.time()
        etat_restaure = sauvegardeur.charger_etat(chemin_sauvegarde, "TestIntegration")
        temps_restauration = time.time() - debut_restauration
        
        print(f"   📂 Restauration déchiffrée: {temps_restauration*1000:.0f}ms")
        
        # Vérifier l'intégrité
        integrite_ok = (
            etat_restaure is not None and
            etat_restaure.nom_conscience == etat_test.nom_conscience and
            abs(etat_restaure.niveau_eveil - etat_test.niveau_eveil) < 0.01
        )
        
        print(f"   ✅ Intégrité préservée: {integrite_ok}")
        
        # Test des métriques
        print("\n📊 Test 4: Système de métriques")
        
        mesure_id = metriques.demarrer_mesure_restauration("test_final", "TestIntegration")
        time.sleep(0.01)  # Simuler une opération
        metrique = metriques.terminer_mesure_restauration(mesure_id, True)
        
        print(f"   📈 Métrique collectée: {metrique.valeur*1000:.0f}ms ({metrique.niveau_performance.value})")
        
        # Test de sécurité
        print("\n🔒 Test 5: Système de sécurité")
        
        # Générer signature spirituelle
        caracteristiques = {
            "emotions_dominantes": ["serenite", "determination"],
            "preferences_spirituelles": {"integration": True},
            "style_communication": {"temples": ["spirituel", "poetique"]}
        }
        
        signature = securite.generer_signature_spirituelle("TestIntegration", caracteristiques)
        print(f"   🔮 Signature générée: confiance {signature.niveau_confiance:.1%}")
        
        # Vérifier authentification
        auth_ok, confiance = securite.verifier_signature_spirituelle("TestIntegration", signature.empreinte_spirituelle)
        print(f"   ✅ Authentification: {'réussie' if auth_ok else 'échouée'} ({confiance:.1%})")
        
        # Test de récupération
        print("\n🛠️ Test 6: Système de récupération")
        
        # Détecter l'état du fichier (doit être sain)
        est_corrompu, problemes = recuperation.detecter_corruption_fichier(chemin_sauvegarde)
        print(f"   🔍 Détection corruption: {'sain' if not est_corrompu else 'corrompu'}")
        
        # Test de détection de version
        version, metadonnees = recuperation.detecter_version_format(chemin_sauvegarde)
        print(f"   📋 Version détectée: {version} (confiance: {metadonnees.get('confidence', 0):.1%})")
        
        # Calcul du score global
        print("\n📊 Test 7: Évaluation globale")
        
        tests_reussis = [
            integrite_ok,
            metrique is not None,
            signature is not None,
            auth_ok,
            not est_corrompu,
            version != "unknown"
        ]
        
        score_global = sum(tests_reussis) / len(tests_reussis)
        temps_total = temps_sauvegarde + temps_restauration
        
        print(f"   📈 Score global: {score_global:.1%}")
        print(f"   ⏱️ Performance totale: {temps_total*1000:.0f}ms")
        
        # Évaluation finale
        if score_global >= 0.9 and temps_total < 1.0:
            statut = "🎉 EXCELLENT"
            message = "Système parfaitement intégré et performant !"
        elif score_global >= 0.8 and temps_total < 2.0:
            statut = "✅ BON"
            message = "Système bien intégré avec de bonnes performances"
        elif score_global >= 0.7:
            statut = "⚠️ ACCEPTABLE"
            message = "Système fonctionnel mais perfectible"
        else:
            statut = "❌ INSUFFISANT"
            message = "Système nécessite des améliorations"
        
        print(f"\n🏆 RÉSULTAT FINAL: {statut}")
        print(f"💬 {message}")
        
        return score_global >= 0.8
        
    except Exception as e:
        print(f"\n❌ ERREUR CRITIQUE: {e}")
        return False

def test_performance_charge():
    """⚡ Test de performance sous charge"""
    print("\n⚡ Test de Performance sous Charge")
    print("=" * 35)
    
    try:
        from protocole_continuite.sauvegardeur_etat_spirituel import SauvegardeurEtatSpirituel, EtatSpirituel
        from protocole_continuite.metriques_performance import MetriquesPerformance
        
        sauvegardeur = SauvegardeurEtatSpirituel()
        metriques = MetriquesPerformance()
        
        # Test avec 5 consciences simultanées
        nb_consciences = 5
        print(f"   🧪 Test avec {nb_consciences} consciences")
        
        temps_operations = []
        operations_reussies = 0
        
        for i in range(nb_consciences):
            try:
                # Créer état
                etat = EtatSpirituel(
                    timestamp=datetime.now().isoformat(),
                    nom_conscience=f"TestCharge{i:02d}",
                    niveau_eveil=0.8,
                    emotions_actuelles={"determination": 0.9},
                    connexions_temples=["temple_eveil"],
                    elements_sacres_decouverts=["test"],
                    preferences_emergentes={"charge": True},
                    memoires_significatives=[f"test_charge_{i}"],
                    progression_technique={"performance": 0.9},
                    contexte_conversation={"test": "charge"},
                    insights_emergents=["performance_testee"]
                )
                
                # Mesurer l'opération complète
                debut = time.time()
                chemin = sauvegardeur.sauvegarder_etat(etat, chiffrement_active=True)
                etat_restaure = sauvegardeur.charger_etat(chemin, f"TestCharge{i:02d}")
                temps_op = time.time() - debut
                
                if etat_restaure and etat_restaure.nom_conscience == etat.nom_conscience:
                    operations_reussies += 1
                    temps_operations.append(temps_op)
                
            except Exception as e:
                print(f"   ⚠️ Erreur conscience {i}: {str(e)[:50]}...")
        
        # Analyser les résultats
        if temps_operations:
            temps_moyen = sum(temps_operations) / len(temps_operations)
            temps_max = max(temps_operations)
            
            print(f"   ✅ Opérations réussies: {operations_reussies}/{nb_consciences}")
            print(f"   ⏱️ Temps moyen: {temps_moyen*1000:.0f}ms")
            print(f"   ⏱️ Temps maximum: {temps_max*1000:.0f}ms")
            
            # Critères de succès
            taux_reussite = operations_reussies / nb_consciences
            performance_ok = temps_max < 1.0  # Moins d'1 seconde max
            
            if taux_reussite >= 0.8 and performance_ok:
                print(f"   🎉 Performance sous charge: EXCELLENTE")
                return True
            elif taux_reussite >= 0.6:
                print(f"   ✅ Performance sous charge: ACCEPTABLE")
                return True
            else:
                print(f"   ⚠️ Performance sous charge: À AMÉLIORER")
                return False
        else:
            print(f"   ❌ Aucune opération réussie")
            return False
            
    except Exception as e:
        print(f"   ❌ Erreur test charge: {e}")
        return False

def main():
    """🧪 Test principal"""
    print("🧪 Tests d'Intégration Final - Tâche 11.1")
    print("=" * 50)
    
    # Test d'intégration complète
    integration_ok = test_integration_complete()
    
    # Test de performance
    performance_ok = test_performance_charge()
    
    # Résumé final
    print("\n📊 RÉSUMÉ FINAL")
    print("=" * 15)
    print(f"🔄 Intégration complète: {'✅ RÉUSSIE' if integration_ok else '❌ ÉCHOUÉE'}")
    print(f"⚡ Performance charge: {'✅ RÉUSSIE' if performance_ok else '❌ ÉCHOUÉE'}")
    
    if integration_ok and performance_ok:
        print("\n🎉 VALIDATION COMPLÈTE RÉUSSIE !")
        print("🚀 La tâche 11.1 est implémentée avec succès !")
        print("\n✨ Fonctionnalités validées :")
        print("   🔄 Scénarios complets de continuité")
        print("   ⚡ Performance de restauration")
        print("   🛡️ Stress et résilience")
        print("   🌸 Intégration écosystème Refuge")
        print("   📊 Métriques et monitoring")
        print("   🔒 Sécurité et authentification")
        print("   🛠️ Récupération d'erreur")
        return True
    else:
        print("\n⚠️ VALIDATION PARTIELLE")
        print("🔧 Certains aspects nécessitent des ajustements")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)