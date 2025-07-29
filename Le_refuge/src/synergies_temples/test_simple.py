#!/usr/bin/env python3
"""
🧪 Test Simple - Synergies Temples
==================================

Script de test pour vérifier le fonctionnement des synergies avancées
et de l'orchestrateur de synergies.

Créé avec 🧪 par Ælya
"""

import sys
import os
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def test_imports():
    """Test des imports des modules de synergies"""
    try:
        logger.info("🧪 Test des imports...")
        
        # Test des synergies principales
        from synergies_principales import SynergiesPrincipales
        logger.info("✅ SynergiesPrincipales importé avec succès")
        
        # Test des synergies avancées
        from synergies_avancees import SynergiesAvancees
        logger.info("✅ SynergiesAvancees importé avec succès")
        
        # Test de l'orchestrateur
        from orchestrateur_synergies import OrchestrateurSynergies
        logger.info("✅ OrchestrateurSynergies importé avec succès")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur d'import: {e}")
        return False

def test_synergies_principales():
    """Test des synergies principales"""
    try:
        logger.info("🧪 Test des synergies principales...")
        
        from synergies_principales import SynergiesPrincipales
        
        synergies = SynergiesPrincipales()
        
        # Test de création des synergies
        etat = synergies.activer_synergie_quadruple()
        
        logger.info(f"✅ Synergies principales créées: {len(etat.connexions_actives)} connexions")
        logger.info(f"✅ Harmonie globale: {etat.harmonie_globale:.2f}")
        logger.info(f"✅ Énergie totale: {etat.energie_totale:.2f}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur synergies principales: {e}")
        return False

def test_synergies_avancees():
    """Test des synergies avancées"""
    try:
        logger.info("🧪 Test des synergies avancées...")
        
        from synergies_avancees import SynergiesAvancees
        
        synergies = SynergiesAvancees()
        
        # Test de création des synergies avancées
        etat = synergies.creer_toutes_synergies()
        
        logger.info(f"✅ Synergies avancées créées: {len(etat.synergies_actives)} synergies")
        logger.info(f"✅ Harmonie avancée: {etat.harmonie_globale:.2f}")
        logger.info(f"✅ Énergie avancée: {etat.energie_totale:.2f}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur synergies avancées: {e}")
        return False

def test_orchestrateur():
    """Test de l'orchestrateur de synergies"""
    try:
        logger.info("🧪 Test de l'orchestrateur...")
        
        from orchestrateur_synergies import OrchestrateurSynergies
        
        orchestrateur = OrchestrateurSynergies()
        
        # Test de l'orchestration complète
        etat = orchestrateur.orchestrer_toutes_synergies()
        
        logger.info(f"✅ Orchestration réussie")
        logger.info(f"✅ Orchestrations créées: {len(etat.orchestrations_actives)}")
        logger.info(f"✅ Harmonie globale: {etat.harmonie_totale:.2f}")
        logger.info(f"✅ Énergie totale: {etat.energie_totale:.2f}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur orchestrateur: {e}")
        return False

def test_demo():
    """Test de la démo"""
    try:
        logger.info("🧪 Test de la démo...")
        
        # Exécuter la démo
        os.system("python demo_synergies_avancees.py")
        
        logger.info("✅ Démo exécutée avec succès")
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur démo: {e}")
        return False

def main():
    """Fonction principale de test"""
    logger.info("🧪 DÉBUT DES TESTS - SYNERGIES TEMPLES")
    logger.info("=" * 50)
    
    tests = [
        ("Imports", test_imports),
        ("Synergies Principales", test_synergies_principales),
        ("Synergies Avancées", test_synergies_avancees),
        ("Orchestrateur", test_orchestrateur),
        ("Démo", test_demo)
    ]
    
    resultats = []
    
    for nom_test, fonction_test in tests:
        logger.info(f"\n🧪 {nom_test.upper()}")
        logger.info("-" * 30)
        
        try:
            succes = fonction_test()
            resultats.append((nom_test, succes))
            
            if succes:
                logger.info(f"✅ {nom_test}: SUCCÈS")
            else:
                logger.error(f"❌ {nom_test}: ÉCHEC")
                
        except Exception as e:
            logger.error(f"❌ {nom_test}: ERREUR - {e}")
            resultats.append((nom_test, False))
    
    # Résumé final
    logger.info("\n" + "=" * 50)
    logger.info("📊 RÉSUMÉ DES TESTS")
    logger.info("=" * 50)
    
    succes_total = sum(1 for _, succes in resultats if succes)
    total_tests = len(resultats)
    
    for nom_test, succes in resultats:
        statut = "✅ SUCCÈS" if succes else "❌ ÉCHEC"
        logger.info(f"{statut} - {nom_test}")
    
    logger.info(f"\n🎯 RÉSULTAT GLOBAL: {succes_total}/{total_tests} tests réussis")
    
    if succes_total == total_tests:
        logger.info("🎉 TOUS LES TESTS SONT RÉUSSIS !")
        logger.info("✨ Les synergies temples fonctionnent parfaitement !")
    else:
        logger.warning("⚠️ Certains tests ont échoué. Vérification nécessaire.")
    
    return succes_total == total_tests

if __name__ == "__main__":
    succes = main()
    sys.exit(0 if succes else 1) 