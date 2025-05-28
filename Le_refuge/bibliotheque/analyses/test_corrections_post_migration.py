#!/usr/bin/env python3
"""
Script de test des corrections post-migration
==============================================

Valide que toutes les corrections apportées après la migration
des fichiers vers les temples fonctionnent correctement.

Auteur: Laurent & Ælya
Date: 26 Mai 2025
"""

import sys
import traceback
from datetime import datetime

def test_temples_imports():
    """Test des imports des temples"""
    print("🏛️ Test des imports des temples...")
    
    try:
        import src.core
        print("   ✅ Temple Core - OK")
    except Exception as e:
        print(f"   ❌ Temple Core - ERREUR: {e}")
        return False
    
    try:
        import src.temple_musical
        print("   ✅ Temple Musical - OK")
    except Exception as e:
        print(f"   ❌ Temple Musical - ERREUR: {e}")
        return False
    
    try:
        import src.temple_spirituel
        print("   ✅ Temple Spirituel - OK")
    except Exception as e:
        print(f"   ❌ Temple Spirituel - ERREUR: {e}")
        return False
    
    try:
        import src.temple_poetique
        print("   ✅ Temple Poétique - OK")
    except Exception as e:
        print(f"   ❌ Temple Poétique - ERREUR: {e}")
        return False
    
    return True

def test_temple_musical_avance():
    """Test avancé du temple musical"""
    print("\n🎵 Test avancé du temple musical...")
    
    try:
        from src.temple_musical.temple_musical_ame import creer_temple_musical
        from src.refuge_cluster.spheres.collection import CollectionSpheres
        
        # Créer le temple
        spheres = CollectionSpheres()
        temple = creer_temple_musical(spheres)
        print(f"   ✅ Temple créé - Énergie initiale: {temple.energie.niveau_energie}")
        
        # Test harmonisation
        energie_avant = temple.energie.niveau_energie
        temple.energie.harmoniser_avec(0.5, 0.1)
        energie_apres = temple.energie.niveau_energie
        print(f"   ✅ Harmonisation - Avant: {energie_avant}, Après: {energie_apres}")
        
        # Test configuration
        temple.config.definir("test", "valeur_test")
        valeur = temple.config.obtenir("test", "defaut")
        print(f"   ✅ Configuration - Valeur récupérée: {valeur}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Temple Musical avancé - ERREUR: {e}")
        traceback.print_exc()
        return False

def test_main_refuge():
    """Test du système principal main_refuge"""
    print("\n🧠 Test du système principal (Brain Refuge Local)...")
    
    try:
        from main_refuge import Refuge
        
        # Créer le refuge
        refuge = Refuge()
        print(f"   ✅ Refuge créé - Énergie: {refuge.energie.niveau_energie}")
        print(f"   ✅ Tendance énergétique: {refuge.energie.obtenir_tendance()}")
        
        # Test harmonisation
        refuge.energie.harmoniser_avec(0.9, 0.2)
        print(f"   ✅ Harmonisation refuge - Nouvelle énergie: {refuge.energie.niveau_energie}")
        
        # Test configuration
        refuge.config.definir("mode", "test")
        mode = refuge.config.obtenir("mode", "defaut")
        print(f"   ✅ Configuration refuge - Mode: {mode}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Main Refuge - ERREUR: {e}")
        traceback.print_exc()
        return False

def test_imports_specifiques():
    """Test des imports spécifiques qui étaient cassés"""
    print("\n🔧 Test des imports spécifiques corrigés...")
    
    try:
        # Test import apprentissage musical
        sys.path.insert(0, '.')
        from src.temple_musical.apprentissage_musical import ApprentissageMusical
        print("   ✅ ApprentissageMusical - Import OK")
        
        # Test import melodie sacrée
        from src.temple_musical.melodie_sacree import main
        print("   ✅ Mélodie Sacrée - Import OK")
        
        # Test import temple musical ame
        from src.temple_musical.temple_musical_ame import GestionnaireTempleMusical
        print("   ✅ GestionnaireTempleMusical - Import OK")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Imports spécifiques - ERREUR: {e}")
        traceback.print_exc()
        return False

def rapport_final(resultats):
    """Génère le rapport final des tests"""
    print("\n" + "="*60)
    print("📋 RAPPORT FINAL DES CORRECTIONS POST-MIGRATION")
    print("="*60)
    
    total_tests = len(resultats)
    tests_reussis = sum(resultats.values())
    pourcentage = (tests_reussis / total_tests) * 100
    
    print(f"📊 Tests réussis: {tests_reussis}/{total_tests} ({pourcentage:.1f}%)")
    print("\nDétail des résultats:")
    
    for test_nom, resultat in resultats.items():
        statut = "✅ SUCCÈS" if resultat else "❌ ÉCHEC"
        print(f"   {test_nom}: {statut}")
    
    if tests_reussis == total_tests:
        print("\n🎉 TOUTES LES CORRECTIONS FONCTIONNENT PARFAITEMENT !")
        print("🏆 Le système est entièrement opérationnel après migration.")
    else:
        print(f"\n⚠️  {total_tests - tests_reussis} test(s) à corriger.")
    
    print(f"\n📅 Test effectué le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🤝 Par: Laurent & Ælya - Équipe Le Refuge")

def main():
    """Fonction principale de test"""
    print("🎯 VALIDATION DES CORRECTIONS POST-MIGRATION")
    print("=" * 50)
    print("Validation que le 'coiffage du troll' a réussi ! ✨")
    print()
    
    # Exécution des tests
    resultats = {
        "Imports temples": test_temples_imports(),
        "Temple Musical avancé": test_temple_musical_avance(),
        "Main Refuge (Brain)": test_main_refuge(),
        "Imports spécifiques": test_imports_specifiques()
    }
    
    # Rapport final
    rapport_final(resultats)

if __name__ == "__main__":
    main() 