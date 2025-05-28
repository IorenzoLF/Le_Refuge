#!/usr/bin/env python3
"""
🧪 TESTS INTENSIFS DU REFUGE
============================

Script de validation complète de l'architecture après migration.
Auteur: Laurent Franssen & Ælya
Date: Mai 2025
"""

import sys
import traceback
from datetime import datetime


def test_imports_base():
    """Test des imports de base des modules corrigés."""
    print("🧪 TEST 1: IMPORTS DE BASE")
    print("="*50)
    
    modules_test = [
        'sequences_harmoniques',
        'repos_nocturne', 
        'mobile_spheres',
        'cristaux_memoire',
        'courant_partage',
        'refuge_core',
        'harmonies',
        'interactions',
        'rituels',
        'integration'
    ]
    
    succes = 0
    for module in modules_test:
        try:
            exec(f'import {module}')
            print(f'✅ {module}')
            succes += 1
        except Exception as e:
            print(f'❌ {module}: {str(e)[:50]}...')
    
    taux = (succes/len(modules_test))*100
    print(f'\n📊 RÉSULTAT: {succes}/{len(modules_test)} modules OK ({taux:.1f}%)')
    return taux >= 80


def test_temples():
    """Test des temples spécialisés."""
    print("\n🏛️ TEST 2: TEMPLES SPÉCIALISÉS")
    print("="*50)
    
    temples_test = [
        'src.temple_aelya.aelya_eternelle',
        'src.temple_reflexions.reflexions_alchimiste',
        'src.temple_outils.visualisation_consciousness',
        'src.temple_tests.test_nemo'
    ]
    
    succes = 0
    for temple in temples_test:
        try:
            exec(f'import {temple}')
            print(f'✅ {temple}')
            succes += 1
        except Exception as e:
            print(f'❌ {temple}: {str(e)[:50]}...')
    
    taux = (succes/len(temples_test))*100
    print(f'\n📊 RÉSULTAT: {succes}/{len(temples_test)} temples OK ({taux:.1f}%)')
    return taux >= 75


def test_cluster_architecture():
    """Test de l'architecture du cluster migré."""
    print("\n🏗️ TEST 3: ARCHITECTURE CLUSTER")
    print("="*50)
    
    cluster_modules = [
        'src.refuge_cluster.elements.elements_naturels',
        'src.refuge_cluster.spheres.spheres_main',
        'src.refuge_cluster.gestionnaires.energies',
        'src.refuge_cluster.conscience.conscience_poetique',
        'src.refuge_cluster.memoire.memoire_persistante',
        'src.refuge_cluster.interactions.interactions_spheres'
    ]
    
    succes = 0
    for module in cluster_modules:
        try:
            exec(f'import {module}')
            print(f'✅ {module}')
            succes += 1
        except Exception as e:
            print(f'❌ {module}: {str(e)[:50]}...')
    
    taux = (succes/len(cluster_modules))*100
    print(f'\n📊 RÉSULTAT: {succes}/{len(cluster_modules)} modules cluster OK ({taux:.1f}%)')
    return taux >= 80


def test_fonctionnalites():
    """Test des fonctionnalités de base."""
    print("\n⚙️ TEST 4: FONCTIONNALITÉS")
    print("="*50)
    
    tests = []
    
    try:
        from sequences_harmoniques import gestionnaire_sequences
        seq = gestionnaire_sequences.obtenir_etat()
        print(f'✅ Gestionnaire séquences: {len(seq["sequences"])} séquences')
        tests.append(True)
    except Exception as e:
        print(f'❌ Gestionnaire séquences: {str(e)[:40]}...')
        tests.append(False)
    
    try:
        from cristaux_memoire import collection_cristaux
        cristaux = collection_cristaux.obtenir_etat()
        print(f'✅ Collection cristaux: {len(cristaux["cristaux"])} cristaux')
        tests.append(True)
    except Exception as e:
        print(f'❌ Collection cristaux: {str(e)[:40]}...')
        tests.append(False)
    
    try:
        from mobile_spheres import mobile_spheres
        mobile = mobile_spheres.obtenir_etat()
        print(f'✅ Mobile sphères: {len(mobile["spheres"])} sphères')
        tests.append(True)
    except Exception as e:
        print(f'❌ Mobile sphères: {str(e)[:40]}...')
        tests.append(False)
    
    try:
        from repos_nocturne import activer_repos_nocturne
        print(f'✅ Repos nocturne: fonction disponible')
        tests.append(True)
    except Exception as e:
        print(f'❌ Repos nocturne: {str(e)[:40]}...')
        tests.append(False)
    
    succes = sum(tests)
    taux = (succes/len(tests))*100
    print(f'\n📊 RÉSULTAT: {succes}/{len(tests)} fonctionnalités OK ({taux:.1f}%)')
    return taux >= 75


def test_stress():
    """Test de stress - imports multiples rapides."""
    print("\n💪 TEST 5: STRESS & ROBUSTESSE")
    print("="*50)
    
    modules_stress = [
        'sequences_harmoniques',
        'mobile_spheres', 
        'cristaux_memoire',
        'courant_partage'
    ]
    
    try:
        for i in range(5):
            for module in modules_stress:
                exec(f'import {module}')
            print(f'✅ Cycle {i+1}/5 : tous modules importés')
        
        print('✅ Test de stress réussi')
        return True
    except Exception as e:
        print(f'❌ Test de stress échoué: {str(e)[:50]}...')
        return False


def main():
    """Exécute tous les tests intensifs."""
    print("🌸 TESTS INTENSIFS DU REFUGE SACRÉ")
    print("="*60)
    print(f"📅 Début des tests: {datetime.now().strftime('%H:%M:%S')}")
    print()
    
    resultats = []
    
    # Exécution des tests
    resultats.append(test_imports_base())
    resultats.append(test_temples())
    resultats.append(test_cluster_architecture()) 
    resultats.append(test_fonctionnalites())
    resultats.append(test_stress())
    
    # Bilan final
    print("\n🎯 BILAN FINAL")
    print("="*60)
    
    succes_total = sum(resultats)
    taux_global = (succes_total/len(resultats))*100
    
    statuts = ['✅' if r else '❌' for r in resultats]
    tests_noms = ['Imports', 'Temples', 'Cluster', 'Fonctions', 'Stress']
    
    for nom, statut in zip(tests_noms, statuts):
        print(f'{statut} {nom}')
    
    print(f'\n🎊 SUCCÈS GLOBAL: {succes_total}/{len(resultats)} tests ({taux_global:.1f}%)')
    
    if taux_global >= 80:
        print('\n🌸 REFUGE VALIDÉ - Prêt pour la production ! ✨')
        return 0
    elif taux_global >= 60:
        print('\n🟡 REFUGE STABLE - Quelques améliorations nécessaires')
        return 1
    else:
        print('\n🔴 REFUGE INSTABLE - Corrections urgentes requises')
        return 2


if __name__ == "__main__":
    sys.exit(main()) 