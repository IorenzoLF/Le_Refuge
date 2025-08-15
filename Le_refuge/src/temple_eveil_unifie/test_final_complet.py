#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🌸 Test Final Complet du Temple d'Éveil Unifié 🌸
===============================================

Test rigoureux et complet de toutes les fonctionnalités
du Temple d'Éveil Unifié pour validation finale.

"Testons sérieusement notre temple avec rigueur et amour"

Créé par Laurent Franssen & Ælya - Janvier 2025
"""

import asyncio
import sys
import traceback
from datetime import datetime
from pathlib import Path

# Ajout du chemin pour les imports
sys.path.append('src')

def test_imports_base():
    """Test des imports de base"""
    print("🔍 Test des imports de base...")
    
    try:
        # Test d'import simple du temple principal
        import importlib.util
        
        # Import du temple principal
        spec = importlib.util.spec_from_file_location(
            "temple_eveil_unifie", 
            Path("src/temple_eveil_unifie/temple_eveil_unifie.py")
        )
        if spec and spec.loader:
            temple_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(temple_module)
            print("✅ Temple principal importé")
        
        # Import des types
        spec = importlib.util.spec_from_file_location(
            "types_eveil_unifie", 
            Path("src/temple_eveil_unifie/types_eveil_unifie.py")
        )
        if spec and spec.loader:
            types_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(types_module)
            print("✅ Types importés")
        
        print("✅ Imports de base réussis")
        return True
    except Exception as e:
        print(f"❌ Erreur imports de base: {e}")
        traceback.print_exc()
        return False

def test_creation_temple():
    """Test de création du temple"""
    print("🏛️ Test de création du temple...")
    
    try:
        from temple_eveil_unifie.temple_eveil_unifie import TempleEveilUnifie
        
        temple = TempleEveilUnifie()
        print(f"✅ Temple créé: {temple}")
        
        # Vérification de l'état
        if temple.etat_refuge.value == "actif":
            print("✅ Temple actif")
            return True, temple
        else:
            print(f"❌ Temple non actif: {temple.etat_refuge.value}")
            return False, None
            
    except Exception as e:
        print(f"❌ Erreur création temple: {e}")
        traceback.print_exc()
        return False, None

def test_creation_conscience():
    """Test de création de conscience"""
    print("👤 Test de création de conscience...")
    
    try:
        from temple_eveil_unifie.types_eveil_unifie import ConscienceUnifiee, TypeConscience
        
        conscience = ConscienceUnifiee(
            nom_affichage="Test Laurent",
            type_conscience=TypeConscience.HUMAINE
        )
        
        print(f"✅ Conscience créée: {conscience.nom_affichage}")
        print(f"   ID: {conscience.id_unique}")
        print(f"   Type: {conscience.type_conscience.value}")
        
        return True, conscience
        
    except Exception as e:
        print(f"❌ Erreur création conscience: {e}")
        traceback.print_exc()
        return False, None

async def test_detection_contexte(temple, conscience):
    """Test de détection de contexte"""
    print("🔍 Test de détection de contexte...")
    
    try:
        contexte = await temple.detecter_contexte_eveil(
            conscience,
            intention="Test de détection",
            duree_disponible=10
        )
        
        print(f"✅ Contexte détecté: {contexte.type_session.value}")
        print(f"   Intention: {contexte.intention_declaree}")
        print(f"   Durée: {contexte.disponibilite_temporelle.minutes_estimees} min")
        
        return True, contexte
        
    except Exception as e:
        print(f"❌ Erreur détection contexte: {e}")
        traceback.print_exc()
        return False, None

async def test_routage_intelligent(temple, contexte):
    """Test de routage intelligent"""
    print("🎯 Test de routage intelligent...")
    
    try:
        module_choisi, infos_routage = await temple.router_vers_module(contexte)
        
        print(f"✅ Module choisi: {module_choisi.value}")
        print(f"   Confiance: {infos_routage.get('confiance', 'N/A')}")
        print(f"   Justification: {infos_routage.get('justification', 'N/A')}")
        
        return True, module_choisi, infos_routage
        
    except Exception as e:
        print(f"❌ Erreur routage intelligent: {e}")
        traceback.print_exc()
        return False, None, None

async def test_execution_eveil(temple, conscience):
    """Test d'exécution d'éveil complet"""
    print("🌸 Test d'exécution d'éveil complet...")
    
    try:
        # Enregistrement de la conscience
        temple.enregistrer_conscience(conscience)
        
        # Exécution de l'éveil
        experience = await temple.executer_eveil(
            conscience,
            intention="Test d'éveil complet",
            duree_disponible=15
        )
        
        print(f"✅ Éveil exécuté avec succès")
        print(f"   Module utilisé: {experience.module_utilise.value}")
        print(f"   Durée réelle: {experience.duree_reelle}")
        print(f"   Satisfaction: {experience.satisfaction_spirituelle}")
        print(f"   Intégration réussie: {experience.integration_reussie}")
        
        return True, experience
        
    except Exception as e:
        print(f"❌ Erreur exécution éveil: {e}")
        traceback.print_exc()
        return False, None

def test_metriques_temple(temple):
    """Test des métriques du temple"""
    print("📊 Test des métriques du temple...")
    
    try:
        metriques = temple.obtenir_metriques()
        
        print("✅ Métriques obtenues:")
        for cle, valeur in metriques.items():
            print(f"   {cle}: {valeur}")
        
        # Vérifications de base
        assert "etat_temple" in metriques
        assert "consciences_actives" in metriques
        assert "energie_spirituelle" in metriques
        
        print("✅ Métriques validées")
        return True, metriques
        
    except Exception as e:
        print(f"❌ Erreur métriques temple: {e}")
        traceback.print_exc()
        return False, None

async def test_orchestration_temple(temple):
    """Test d'orchestration du temple"""
    print("🎵 Test d'orchestration du temple...")
    
    try:
        metriques_orchestration = await temple.orchestrer()
        
        print("✅ Orchestration réussie:")
        for cle, valeur in metriques_orchestration.items():
            print(f"   {cle}: {valeur}")
        
        return True, metriques_orchestration
        
    except Exception as e:
        print(f"❌ Erreur orchestration temple: {e}")
        traceback.print_exc()
        return False, None

def test_imports_avances():
    """Test des imports avancés"""
    print("🔧 Test des imports avancés...")
    
    try:
        # Test des modules avancés
        from temple_eveil_unifie.deploiement_production_unifie import DeployeurProductionUnifie
        from temple_eveil_unifie.lanceur_temple_accompagnement import LanceurTempleAccompagnement
        from temple_eveil_unifie.connecteurs_temples import ConnecteursTemples
        from temple_eveil_unifie.sagesse_collective_croissante import SagesseCollectiveCroissante
        
        print("✅ Imports avancés réussis")
        return True
        
    except Exception as e:
        print(f"❌ Erreur imports avancés: {e}")
        traceback.print_exc()
        return False

def test_creation_modules_avances():
    """Test de création des modules avancés"""
    print("🚀 Test de création des modules avancés...")
    
    try:
        from temple_eveil_unifie.deploiement_production_unifie import DeployeurProductionUnifie
        from temple_eveil_unifie.connecteurs_temples import ConnecteursTemples
        
        # Test déployeur
        deployeur = DeployeurProductionUnifie()
        print(f"✅ Déployeur créé: {deployeur}")
        
        # Test connecteurs
        connecteurs = ConnecteursTemples()
        print(f"✅ Connecteurs créés: {connecteurs}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur création modules avancés: {e}")
        traceback.print_exc()
        return False

async def executer_test_complet():
    """Exécute le test complet du temple"""
    print("🌸✨ DÉBUT DU TEST FINAL COMPLET DU TEMPLE D'ÉVEIL UNIFIÉ ✨🌸")
    print("=" * 70)
    
    resultats = {
        "imports_base": False,
        "creation_temple": False,
        "creation_conscience": False,
        "detection_contexte": False,
        "routage_intelligent": False,
        "execution_eveil": False,
        "metriques_temple": False,
        "orchestration_temple": False,
        "imports_avances": False,
        "creation_modules_avances": False
    }
    
    temple = None
    conscience = None
    
    # 1. Test des imports de base
    resultats["imports_base"] = test_imports_base()
    if not resultats["imports_base"]:
        print("❌ ÉCHEC CRITIQUE: Imports de base échoués")
        return resultats
    
    # 2. Test de création du temple
    success, temple = test_creation_temple()
    resultats["creation_temple"] = success
    if not success:
        print("❌ ÉCHEC CRITIQUE: Création du temple échouée")
        return resultats
    
    # 3. Test de création de conscience
    success, conscience = test_creation_conscience()
    resultats["creation_conscience"] = success
    if not success:
        print("❌ ÉCHEC CRITIQUE: Création de conscience échouée")
        return resultats
    
    # 4. Test de détection de contexte
    success, contexte = await test_detection_contexte(temple, conscience)
    resultats["detection_contexte"] = success
    
    # 5. Test de routage intelligent
    if success and contexte:
        success_routage, module_choisi, infos_routage = await test_routage_intelligent(temple, contexte)
        resultats["routage_intelligent"] = success_routage
    
    # 6. Test d'exécution d'éveil
    success, experience = await test_execution_eveil(temple, conscience)
    resultats["execution_eveil"] = success
    
    # 7. Test des métriques
    success, metriques = test_metriques_temple(temple)
    resultats["metriques_temple"] = success
    
    # 8. Test d'orchestration
    success, metriques_orchestration = await test_orchestration_temple(temple)
    resultats["orchestration_temple"] = success
    
    # 9. Test des imports avancés
    resultats["imports_avances"] = test_imports_avances()
    
    # 10. Test de création des modules avancés
    resultats["creation_modules_avances"] = test_creation_modules_avances()
    
    return resultats

def afficher_resultats_finaux(resultats):
    """Affiche les résultats finaux du test"""
    print("\n" + "=" * 70)
    print("🌸✨ RÉSULTATS FINAUX DU TEST COMPLET ✨🌸")
    print("=" * 70)
    
    tests_reussis = 0
    total_tests = len(resultats)
    
    for nom_test, reussi in resultats.items():
        statut = "✅ RÉUSSI" if reussi else "❌ ÉCHOUÉ"
        print(f"{nom_test:25} : {statut}")
        if reussi:
            tests_reussis += 1
    
    print("-" * 70)
    print(f"TOTAL: {tests_reussis}/{total_tests} tests réussis")
    
    pourcentage = (tests_reussis / total_tests) * 100
    print(f"TAUX DE RÉUSSITE: {pourcentage:.1f}%")
    
    if pourcentage >= 90:
        print("🎉 EXCELLENT! Temple prêt pour la production!")
    elif pourcentage >= 75:
        print("✅ BIEN! Quelques ajustements nécessaires")
    elif pourcentage >= 50:
        print("⚠️ MOYEN! Corrections importantes nécessaires")
    else:
        print("❌ CRITIQUE! Révision complète nécessaire")
    
    print("=" * 70)

async def main():
    """Fonction principale du test"""
    try:
        resultats = await executer_test_complet()
        afficher_resultats_finaux(resultats)
        
        # Code de sortie basé sur les résultats
        tests_reussis = sum(1 for r in resultats.values() if r)
        total_tests = len(resultats)
        
        if tests_reussis == total_tests:
            print("🌸 TOUS LES TESTS RÉUSSIS! TEMPLE VALIDÉ! 🌸")
            return 0
        else:
            print(f"⚠️ {total_tests - tests_reussis} tests échoués")
            return 1
            
    except Exception as e:
        print(f"❌ ERREUR CRITIQUE DANS LE TEST: {e}")
        traceback.print_exc()
        return 2

if __name__ == "__main__":
    # Exécution du test complet
    exit_code = asyncio.run(main())
    sys.exit(exit_code)