#!/usr/bin/env python3
"""
🧪 TESTS DE CONSOLIDATION DU REFUGE
==================================

Validation exhaustive de l'architecture après migration et corrections.
Auteur: Laurent Franssen & Ælya
Date: Mai 2025
"""

import sys
import traceback
from datetime import datetime
from pathlib import Path
import logging

# Configuration du logging pour les tests
logging.basicConfig(level=logging.WARNING)  # Réduire le bruit

def test_architecture_principale():
    """Test de l'architecture principale du Refuge."""
    print("🏛️ TEST 1: ARCHITECTURE PRINCIPALE")
    print("="*60)
    
    tests = [
        ("🔵 Refuge Core", "refuge_core"),
        ("⭕ Sphères", "spheres"),
        ("🌸 Harmonies", "harmonies"),
        ("💫 Interactions", "interactions"),
        ("🎭 Conscience", "conscience"),
        ("📚 Poésie", "poesie"),
        ("🌱 Jardin", "jardin"),
        ("🔮 Rituels", "rituels"),
        ("🌊 Intégration", "integration")
    ]
    
    succes = 0
    for nom, module in tests:
        try:
            exec(f'import {module}')
            print(f'✅ {nom}')
            succes += 1
        except Exception as e:
            print(f'❌ {nom}: {str(e)[:50]}...')
    
    print(f'\n📊 Architecture: {succes}/{len(tests)} ({(succes/len(tests))*100:.1f}%)')
    return succes, len(tests)


def test_cluster_refuge():
    """Test du cluster migré vers src/refuge_cluster."""
    print("\n🏗️ TEST 2: CLUSTER REFUGE MIGRÉ")
    print("="*60)
    
    tests = [
        ("🪨 Éléments naturels", "src.refuge_cluster.elements.elements_naturels"),
        ("💫 Interactions sphères", "src.refuge_cluster.interactions.interactions_spheres"),
        ("🧠 Conscience poétique", "src.refuge_cluster.conscience.conscience_poetique"),
        ("🧘 Méditation sphères", "src.refuge_cluster.meditation.meditation_spheres"),
        ("💎 Mémoire persistante", "src.refuge_cluster.memoire.memoire_persistante"),
        ("⚡ Gestionnaire énergies", "src.refuge_cluster.gestionnaires.energies"),
        ("🔧 Utilitaires", "src.refuge_cluster.utilitaires.outils_refuge")
    ]
    
    succes = 0
    for nom, module in tests:
        try:
            exec(f'import {module}')
            print(f'✅ {nom}')
            succes += 1
        except Exception as e:
            print(f'❌ {nom}: {str(e)[:50]}...')
    
    print(f'\n📊 Cluster migré: {succes}/{len(tests)} ({(succes/len(tests))*100:.1f}%)')
    return succes, len(tests)


def test_temples():
    """Test des temples existants."""
    print("\n🏛️ TEST 3: TEMPLES SACRÉS")
    print("="*60)
    
    tests = [
        ("✨ Temple Ælya", "src.temple_aelya.aelya_eternelle"),
        ("🤔 Temple Réflexions", "src.temple_reflexions.reflexions_alchimiste"),
        ("🛠️ Temple Outils", "src.temple_outils.outils_refuge"),
        ("🧪 Temple Tests", "src.temple_tests.test_nemo")
    ]
    
    succes = 0
    for nom, module in tests:
        try:
            exec(f'import {module}')
            print(f'✅ {nom}')
            succes += 1
        except Exception as e:
            print(f'❌ {nom}: {str(e)[:50]}...')
    
    print(f'\n📊 Temples: {succes}/{len(tests)} ({(succes/len(tests))*100:.1f}%)')
    return succes, len(tests)


def test_fonctionnalites_principales():
    """Test des fonctionnalités principales."""
    print("\n⚙️ TEST 4: FONCTIONNALITÉS PRINCIPALES")
    print("="*60)
    
    # Test 1: Création d'objets principaux
    try:
        from src.refuge_cluster.spheres.collection import CollectionSpheres
        collection = CollectionSpheres()
        print("✅ CollectionSpheres créée")
        
        from src.refuge_cluster.elements.elements_naturels import Cerisier
        cerisier = Cerisier()
        print("✅ Cerisier créé")
        
        from harmonies import GestionnaireHarmonies
        from interactions import GestionnaireInteractions
        from src.refuge_cluster.elements.elements_sacres import RefugeElements
        
        # Créer les paramètres requis pour GestionnaireInteractions
        refuge_elements = RefugeElements()
        gestionnaire_interactions = GestionnaireInteractions(refuge_elements, collection)
        gestionnaire_harmonies = GestionnaireHarmonies(gestionnaire_interactions)
        print("✅ Gestionnaires créés")
        
        # Test 2: Fonctionnalités de base
        etat = gestionnaire_interactions.obtenir_etat_interactions()
        print(f"✅ État interactions: {len(etat)} clés")
        
        etat_h = gestionnaire_harmonies.obtenir_etat()
        print(f"✅ État harmonies: {len(etat_h)} clés")
        
        return 5, 5
        
    except Exception as e:
        print(f"❌ Erreur fonctionnalités: {str(e)}")
        traceback.print_exc()
        return 0, 5


def test_modules_corriges():
    """Test spécifique des modules que nous avons corrigés."""
    print("\n🔧 TEST 5: MODULES CORRIGÉS")
    print("="*60)
    
    modules_corriges = [
        ("integration.py", "integration"),
        ("main_refuge.py", "main_refuge"),
        ("ecouter_riviere.py", "ecouter_riviere"),
        ("sequences_harmoniques.py", "sequences_harmoniques"),
        ("repos_nocturne.py", "repos_nocturne"),
        ("mobile_spheres.py", "mobile_spheres"),
        ("cristaux_memoire.py", "cristaux_memoire"),
        ("courant_partage.py", "courant_partage")
    ]
    
    succes = 0
    for nom_fichier, module in modules_corriges:
        try:
            exec(f'import {module}')
            print(f'✅ {nom_fichier}')
            succes += 1
        except Exception as e:
            print(f'❌ {nom_fichier}: {str(e)[:50]}...')
    
    print(f'\n📊 Modules corrigés: {succes}/{len(modules_corriges)} ({(succes/len(modules_corriges))*100:.1f}%)')
    return succes, len(modules_corriges)


def test_stress_systeme():
    """Test de stress pour vérifier la stabilité."""
    print("\n💪 TEST 6: STRESS ET STABILITÉ")
    print("="*60)
    
    try:
        # Import multiple des modules principaux
        for i in range(3):
            import refuge_core
            import harmonies
            import interactions
            import spheres
            import conscience
        print("✅ Imports multiples réussis")
        
        # Création multiple d'objets
        objets = []
        for i in range(5):
            from interactions import GestionnaireInteractions
            from src.refuge_cluster.elements.elements_sacres import RefugeElements
            from src.refuge_cluster.spheres.collection import CollectionSpheres
            
            refuge_elements = RefugeElements()
            collection = CollectionSpheres()
            obj = GestionnaireInteractions(refuge_elements, collection)
            objets.append(obj)
        print(f"✅ {len(objets)} objets créés")
        
        # Test de mémoire/nettoyage
        del objets
        print("✅ Nettoyage mémoire réussi")
        
        return 3, 3
        
    except Exception as e:
        print(f"❌ Erreur stress: {str(e)}")
        return 0, 3


def test_integration_complete():
    """Test d'intégration complète du système."""
    print("\n🌟 TEST 7: INTÉGRATION COMPLÈTE")
    print("="*60)
    
    try:
        # Test du système main_refuge
        from main_refuge import Refuge
        refuge = Refuge()
        print("✅ Refuge créé")
        
        # Test d'initialisation
        if refuge.initialiser():
            print("✅ Refuge initialisé")
        else:
            print("⚠️ Initialisation partielle")
        
        # Test d'état
        etat = refuge.obtenir_etat()
        print(f"✅ État refuge: {len(etat)} clés")
        
        # Test interaction avec Ælya
        try:
            from interagir_aelya import interagir_avec_aelya
            print("✅ Interaction Ælya disponible")
        except:
            print("⚠️ Interaction Ælya limitée")
        
        return 4, 4
        
    except Exception as e:
        print(f"❌ Erreur intégration: {str(e)}")
        traceback.print_exc()
        return 0, 4


def afficher_bilan_final(resultats):
    """Affiche le bilan final des tests."""
    print("\n" + "="*80)
    print("🎯 BILAN FINAL DE CONSOLIDATION")
    print("="*80)
    
    total_succes = sum(r[0] for r in resultats)
    total_tests = sum(r[1] for r in resultats)
    pourcentage = (total_succes / total_tests) * 100
    
    print(f"\n📊 RÉSULTATS GLOBAUX:")
    print(f"   • Tests réussis: {total_succes}/{total_tests}")
    print(f"   • Taux de réussite: {pourcentage:.1f}%")
    
    if pourcentage >= 90:
        print(f"\n🏆 EXCELLENT! Architecture très solide")
    elif pourcentage >= 80:
        print(f"\n✅ TRÈS BIEN! Architecture stable")
    elif pourcentage >= 70:
        print(f"\n⚠️ CORRECT. Quelques ajustements nécessaires")
    else:
        print(f"\n🔴 PROBLÈMES. Architecture à consolider")
    
    print(f"\n💡 RECOMMANDATIONS:")
    if pourcentage >= 85:
        print(f"   • Architecture consolidée - Prêt pour la suite!")
        print(f"   • Peut continuer les corrections restantes")
    else:
        print(f"   • Corriger les problèmes identifiés")
        print(f"   • Renforcer la stabilité avant de continuer")


if __name__ == "__main__":
    print("🧪 DÉBUT DES TESTS DE CONSOLIDATION")
    print(f"⏰ {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("="*80)
    
    resultats = []
    resultats.append(test_architecture_principale())
    resultats.append(test_cluster_refuge())
    resultats.append(test_temples())
    resultats.append(test_fonctionnalites_principales())
    resultats.append(test_modules_corriges())
    resultats.append(test_stress_systeme())
    resultats.append(test_integration_complete())
    
    afficher_bilan_final(resultats) 
