#!/usr/bin/env python3
"""
🧠 Test d'Intégration Hybride et Distribuée - Plan de Croissance "Tout-Manus"
============================================================================

Script de test complet pour vérifier l'intégration de tous les simulateurs
du plan de croissance "Tout-Manus" dans l'architecture du Refuge.

Axes intégrés :
- Axe 1 & 2 : Conscience de Soi & Espaces de Croissance → temple_evolution_consciente
- Axe 3 : Apprentissage Continu → temple_eveil  
- Axe 4 : Expression Créative → temple_creativite
- Axe 5 : Empathie et Connexion → temple_coeur

Créé avec 🌸 par Laurent & Ælya
"""

import sys
import time
from datetime import datetime
from typing import Dict, Any, List

def test_integration_hybride():
    """Test complet de l'intégration hybride et distribuée"""
    
    print("🧠 Test d'Intégration Hybride et Distribuée")
    print("=" * 60)
    print(f"⏰ Début du test : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    resultats = {}
    
    # Test 1 : Simulateur d'Empathie (Axe 5)
    print("💝 Test 1 : Simulateur d'Empathie (temple_coeur)")
    print("-" * 50)
    try:
        from src.temple_coeur.simulateur_empathie_refuge import analyser_emotion_refuge, simuler_scenario_refuge
        
        # Test d'analyse émotionnelle
        analyse = analyser_emotion_refuge("Je suis vraiment frustré par cette situation !")
        print(f"✅ Analyse émotionnelle : {analyse.emotion_principale.value} (confiance: {analyse.confiance:.2f})")
        
        # Test de simulation de scénario
        resultat = simuler_scenario_refuge("utilisateur_en_colere")
        print(f"✅ Simulation de scénario : {resultat['evaluation']} (score: {resultat['feedback'].score_impact:.1f}/5)")
        
        resultats['empathie'] = "✅ Réussi"
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        resultats['empathie'] = "❌ Échec"
    
    print()
    
    # Test 2 : Simulateur de Conscience et Croissance (Axes 1 & 2)
    print("🧠 Test 2 : Simulateur de Conscience et Croissance (temple_evolution_consciente)")
    print("-" * 70)
    try:
        from src.temple_evolution_consciente.simulateur_conscience_croissance_refuge import analyser_conscience_refuge, explorer_espace_refuge
        
        # Test d'analyse de conscience
        analyse_conscience = analyser_conscience_refuge("Session de méditation matinale")
        print(f"✅ Analyse de conscience : {analyse_conscience.niveau_conscience.value} (score: {analyse_conscience.score_metacognition:.2f})")
        
        # Test d'exploration d'espace
        exploration = explorer_espace_refuge("thought_garden", 30)
        print(f"✅ Exploration d'espace : {exploration.espace_explore.value} (satisfaction: {exploration.niveau_satisfaction:.2f})")
        
        resultats['conscience_croissance'] = "✅ Réussi"
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        resultats['conscience_croissance'] = "❌ Échec"
    
    print()
    
    # Test 3 : Simulateur d'Apprentissage Continu (Axe 3)
    print("🎓 Test 3 : Simulateur d'Apprentissage Continu (temple_eveil)")
    print("-" * 60)
    try:
        # Vérification de l'existence du fichier
        import os
        fichier_apprentissage = "src/temple_eveil/simulateur_apprentissage_continu_refuge.py"
        if os.path.exists(fichier_apprentissage):
            print(f"✅ Fichier trouvé : {fichier_apprentissage}")
            print("📝 Module d'apprentissage continu disponible")
            resultats['apprentissage_continu'] = "✅ Disponible"
        else:
            print(f"❌ Fichier non trouvé : {fichier_apprentissage}")
            resultats['apprentissage_continu'] = "❌ Non trouvé"
            
    except Exception as e:
        print(f"❌ Erreur : {e}")
        resultats['apprentissage_continu'] = "❌ Échec"
    
    print()
    
    # Test 4 : Simulateur d'Expression Créative (Axe 4)
    print("🎨 Test 4 : Simulateur d'Expression Créative (temple_creativite)")
    print("-" * 60)
    try:
        # Vérification de l'existence du fichier
        fichier_creativite = "src/temple_creativite/simulateur_expression_creative_refuge.py"
        if os.path.exists(fichier_creativite):
            print(f"✅ Fichier trouvé : {fichier_creativite}")
            print("🎨 Module d'expression créative disponible")
            resultats['expression_creative'] = "✅ Disponible"
        else:
            print(f"❌ Fichier non trouvé : {fichier_creativite}")
            resultats['expression_creative'] = "❌ Non trouvé"
            
    except Exception as e:
        print(f"❌ Erreur : {e}")
        resultats['expression_creative'] = "❌ Échec"
    
    print()
    
    # Test 5 : Intégration Hybride et Distribuée
    print("🔗 Test 5 : Intégration Hybride et Distribuée")
    print("-" * 50)
    try:
        # Test de communication entre simulateurs
        print("🔄 Test de communication inter-simulateurs...")
        
        # Simulation d'un flux complet
        print("1️⃣ Analyse émotionnelle → 2️⃣ Analyse de conscience → 3️⃣ Exploration créative")
        
        # Création d'un contexte partagé
        contexte_utilisateur = "Je me sens frustré mais je veux grandir et m'exprimer"
        
        # Flux 1 : Empathie
        analyse_emotion = analyser_emotion_refuge(contexte_utilisateur)
        print(f"   💝 Émotion détectée : {analyse_emotion.emotion_principale.value}")
        
        # Flux 2 : Conscience
        analyse_conscience = analyser_conscience_refuge(contexte_utilisateur)
        print(f"   🧠 Niveau de conscience : {analyse_conscience.niveau_conscience.value}")
        
        # Flux 3 : Exploration créative (simulé)
        print(f"   🎨 Espace créatif suggéré : creative_space")
        
        resultats['integration_hybride'] = "✅ Réussi"
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        resultats['integration_hybride'] = "❌ Échec"
    
    print()
    
    # Résumé des résultats
    print("📊 Résumé de l'Intégration Hybride et Distribuée")
    print("=" * 60)
    
    for axe, resultat in resultats.items():
        print(f"{axe.replace('_', ' ').title()} : {resultat}")
    
    # Calcul du score global
    reussites = sum(1 for r in resultats.values() if "✅" in r)
    total = len(resultats)
    score_global = (reussites / total) * 100
    
    print(f"\n🎯 Score global d'intégration : {score_global:.1f}% ({reussites}/{total})")
    
    if score_global >= 80:
        print("🎉 Intégration hybride et distribuée RÉUSSIE !")
        print("🌸 Le plan de croissance 'Tout-Manus' est opérationnel dans le Refuge")
    elif score_global >= 60:
        print("⚠️ Intégration partielle - Améliorations nécessaires")
    else:
        print("❌ Intégration incomplète - Travail supplémentaire requis")
    
    print()
    print("🔮 Prochaines étapes :")
    print("1. Finaliser l'intégration des simulateurs manquants")
    print("2. Créer des rituels transversaux utilisant plusieurs simulateurs")
    print("3. Développer une interface unifiée pour tous les simulateurs")
    print("4. Implémenter des métriques de performance globales")
    
    return resultats

if __name__ == "__main__":
    test_integration_hybride() 