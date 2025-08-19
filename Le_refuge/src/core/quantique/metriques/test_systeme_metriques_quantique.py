#!/usr/bin/env python3
"""
🧪 Test du Système de Métriques Quantique
=========================================

Test complet du système de métriques quantique pour vérifier
la collecte, l'analyse et le rapport des métriques.

Créé par Ælya & Laurent Franssen
"""

import asyncio
import logging
import sys
import os
import time
from datetime import datetime

# Configuration du PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('test_metriques')

async def test_systeme_metriques_complet():
    """🧪 Test complet du système de métriques"""
    print("🧪 TEST DU SYSTÈME DE MÉTRIQUES QUANTIQUE")
    print("=" * 50)
    
    try:
        # Import du système de métriques
        from metriques.systeme_metriques_quantique import systeme_metriques_quantique, TypeMetrique
        
        print("1. 📊 Test d'initialisation du système de métriques...")
        etat_metriques = systeme_metriques_quantique.obtenir_etat_metriques()
        print(f"   ✅ Système de métriques initialisé: {etat_metriques['nom']}")
        print(f"   📊 Métriques actives: {etat_metriques['metriques_actives']}")
        
        print("\n2. 📊 Test de collecte de métriques...")
        metriques_test = [
            (TypeMetrique.COHERENCE_QUANTIQUE, 0.85, "Cohérence quantique élevée"),
            (TypeMetrique.ENERGIE_SPIRITUELLE, 0.72, "Énergie spirituelle optimale"),
            (TypeMetrique.FREQUENCE_HARMONIQUE, 963.0, "Fréquence de connexion divine"),
            (TypeMetrique.PHENOMENES_ACTIFS, 4.0, "Tous les phénomènes actifs"),
            (TypeMetrique.EXPERIENCES_CREEES, 2.0, "Expériences créées avec succès")
        ]
        
        for type_metrique, valeur, description in metriques_test:
            metrique = systeme_metriques_quantique.collecter_metrique(
                type_metrique, valeur, description=description
            )
            if metrique:
                print(f"   ✅ {type_metrique.value}: {valeur} (Qualité: {metrique.qualite_donnees:.3f})")
            else:
                print(f"   ❌ Échec collecte {type_metrique.value}")
        
        print("\n3. 📊 Test de création de session métriques...")
        session = systeme_metriques_quantique.creer_session_metriques(
            session_id="test_session_001",
            nom_session="Session Test Métriques",
            type_session="test_complet",
            duree=300
        )
        if session:
            print(f"   ✅ Session créée: {session.nom_session}")
            print(f"   📊 Score global: {session.score_global:.3f}")
            print(f"   🌟 Impact spirituel: {session.impact_spirituel:.3f}")
            print(f"   ⚡ Efficacité: {session.efficacite:.3f}")
        else:
            print("   ❌ Échec création de session")
            return False
        
        print("\n4. 📈 Test d'analyse de tendances...")
        rapport = await systeme_metriques_quantique.analyser_tendances("1h")
        if rapport:
            print(f"   ✅ Rapport généré pour {rapport.periode_analyse}")
            print(f"   📊 Score global: {rapport.score_global:.3f}")
            print(f"   📈 Tendances: {len(rapport.tendances)} analysées")
            print(f"   🔗 Corrélations: {len(rapport.correlations)} calculées")
            print(f"   💡 Recommandations: {len(rapport.recommandations)} générées")
            
            # Afficher quelques recommandations
            for i, recommandation in enumerate(rapport.recommandations[:3]):
                print(f"      {i+1}. {recommandation}")
        else:
            print("   ❌ Échec génération de rapport")
            return False
        
        print("\n5. 📊 Test d'état final du système...")
        etat_final = systeme_metriques_quantique.obtenir_etat_metriques()
        print(f"   ✅ Total métriques: {etat_final['total_metriques']}")
        print(f"   📊 Total sessions: {etat_final['total_sessions']}")
        print(f"   📈 Total rapports: {etat_final['total_rapports']}")
        print(f"   ⚡ Cache temps réel: {etat_final['cache_temps_reel']}")
        
        print("\n6. 🧹 Test de nettoyage...")
        systeme_metriques_quantique.nettoyer_metriques()
        print("   ✅ Système de métriques nettoyé")
        
        print("\n🎉 TEST RÉUSSI - SYSTÈME DE MÉTRIQUES OPÉRATIONNEL !")
        print("📊 Le système de métriques quantique fonctionne parfaitement !")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        logger.error(f"Erreur: {e}")
        return False

async def test_collecte_intensive():
    """🧪 Test de collecte intensive de métriques"""
    print("\n🔬 TEST DE COLLECTE INTENSIVE")
    print("=" * 50)
    
    try:
        from metriques.systeme_metriques_quantique import systeme_metriques_quantique, TypeMetrique
        
        print("📊 Collecte intensive de métriques...")
        
        # Collecter de nombreuses métriques pour tester les analyses
        for i in range(50):
            # Simuler des variations de métriques
            coherence = 0.7 + (i % 10) * 0.03
            energie = 0.6 + (i % 8) * 0.05
            frequence = 800 + (i % 6) * 50
            
            systeme_metriques_quantique.collecter_metrique(
                TypeMetrique.COHERENCE_QUANTIQUE, coherence, 
                contexte={"session_id": f"intensive_{i//10}"}
            )
            systeme_metriques_quantique.collecter_metrique(
                TypeMetrique.ENERGIE_SPIRITUELLE, energie,
                contexte={"session_id": f"intensive_{i//10}"}
            )
            systeme_metriques_quantique.collecter_metrique(
                TypeMetrique.FREQUENCE_HARMONIQUE, frequence,
                contexte={"session_id": f"intensive_{i//10}"}
            )
            
            # Petite pause pour simuler le temps réel
            await asyncio.sleep(0.01)
        
        print(f"   ✅ {50*3} métriques collectées")
        
        # Créer plusieurs sessions
        for i in range(5):
            session = systeme_metriques_quantique.creer_session_metriques(
                session_id=f"intensive_session_{i}",
                nom_session=f"Session Intensive {i+1}",
                type_session="test_intensif",
                duree=60 + i * 30
            )
            if session:
                print(f"   📊 Session {i+1}: Score {session.score_global:.3f}")
        
        # Analyser les tendances
        rapport = await systeme_metriques_quantique.analyser_tendances("1h")
        if rapport:
            print(f"   📈 Rapport généré avec {len(rapport.metriques_principales)} métriques principales")
            print(f"   💡 Recommandations: {rapport.recommandations}")
        
        print("✅ Test de collecte intensive terminé")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")

async def main():
    """Fonction principale de test"""
    print("🚀 DÉMARRAGE DES TESTS DE MÉTRIQUES")
    print("=" * 50)
    
    # Test principal
    success = await test_systeme_metriques_complet()
    
    if success:
        # Test intensif si le principal réussit
        await test_collecte_intensive()
    
    print("\n🏁 FIN DES TESTS DE MÉTRIQUES")

if __name__ == "__main__":
    asyncio.run(main())
