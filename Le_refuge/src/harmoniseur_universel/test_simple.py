#!/usr/bin/env python3
"""
🌊 Test Simple - Harmoniseur Universel
===================================

Test simple pour vérifier le fonctionnement de l'Harmoniseur Universel.

Créé avec 🌊 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('test_harmoniseur_universel')

def test_synchroniseur_global():
    """Test du synchroniseur global"""
    print("🧪 Test du Synchroniseur Global...")
    
    try:
        from synchroniseur_global import synchroniseur_global, TypeSynchronisation
        
        # Test de création d'une synchronisation
        sync = synchroniseur_global.creer_synchronisation(TypeSynchronisation.TEMPORAL)
        assert sync is not None
        assert sync.type_synchronisation == TypeSynchronisation.TEMPORAL
        print("✅ Synchronisation temporelle créée")
        
        # Test de synchronisation complète
        etat = synchroniseur_global.synchroniser_tout()
        assert etat is not None
        assert len(etat.synchronisations_actives) > 0
        print("✅ Synchronisation complète réussie")
        
        # Test d'état complet
        etat_complet = synchroniseur_global.obtenir_etat_complet()
        assert etat_complet is not None
        assert "synchronisations_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Synchroniseur Global réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Synchroniseur Global: {e}")
        return False

def test_harmoniseur_dimensions():
    """Test de l'harmoniseur de dimensions"""
    print("🧪 Test de l'Harmoniseur Dimensions...")
    
    try:
        from harmoniseur_dimensions import harmoniseur_dimensions, TypeDimension
        
        # Test de création d'un pont dimensionnel
        pont = harmoniseur_dimensions.creer_pont_dimensionnel(
            TypeDimension.TEMPORELLE, 
            TypeDimension.SPATIALE
        )
        assert pont is not None
        assert pont.dimension_source == TypeDimension.TEMPORELLE
        assert pont.dimension_destination == TypeDimension.SPATIALE
        print("✅ Pont dimensionnel créé")
        
        # Test d'harmonisation complète
        etat = harmoniseur_dimensions.harmoniser_toutes_dimensions()
        assert etat is not None
        assert len(etat.ponts_dimensionnels) > 0
        print("✅ Harmonisation complète réussie")
        
        # Test d'état complet
        etat_complet = harmoniseur_dimensions.obtenir_etat_complet()
        assert etat_complet is not None
        assert "ponts_dimensionnels" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test de l'Harmoniseur Dimensions réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de l'Harmoniseur Dimensions: {e}")
        return False

def test_catalyseur_unite():
    """Test du catalyseur d'unité"""
    print("🧪 Test du Catalyseur Unité...")
    
    try:
        from catalyseur_unite import catalyseur_unite, TypeUnite
        
        # Test de création d'une unité
        unite = catalyseur_unite.catalyser_unite(TypeUnite.SPIRITUELLE)
        assert unite is not None
        assert unite.type_unite == TypeUnite.SPIRITUELLE
        print("✅ Unité spirituelle catalysée")
        
        # Test d'unité totale
        etat = catalyseur_unite.catalyser_unite_totale()
        assert etat is not None
        assert len(etat.liens_unite) > 0
        print("✅ Unité totale catalysée")
        
        # Test d'état complet
        etat_complet = catalyseur_unite.obtenir_etat_complet()
        assert etat_complet is not None
        assert "liens_unite" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Catalyseur Unité réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Catalyseur Unité: {e}")
        return False

def test_manifesteur_harmonie():
    """Test du manifesteur d'harmonie"""
    print("🧪 Test du Manifesteur Harmonie...")
    
    try:
        from manifesteur_harmonie import manifesteur_harmonie, TypeHarmonie
        
        # Test de manifestation d'une harmonie
        harmonie = manifesteur_harmonie.manifester_harmonie(TypeHarmonie.MUSICALE)
        assert harmonie is not None
        assert harmonie.type_harmonie == TypeHarmonie.MUSICALE
        print("✅ Harmonie musicale manifestée")
        
        # Test d'harmonie parfaite
        etat = manifesteur_harmonie.manifester_harmonie_parfaite()
        assert etat is not None
        assert len(etat.experiences_harmonie) > 0
        print("✅ Harmonie parfaite manifestée")
        
        # Test d'état complet
        etat_complet = manifesteur_harmonie.obtenir_etat_complet()
        assert etat_complet is not None
        assert "experiences_harmonie" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Manifesteur Harmonie réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Manifesteur Harmonie: {e}")
        return False

def test_harmoniseur_principal():
    """Test de l'harmoniseur principal"""
    print("🧪 Test de l'Harmoniseur Principal...")
    
    try:
        from harmoniseur_universel_principal import harmoniseur_universel
        
        # Test d'état initial
        etat_initial = harmoniseur_universel.obtenir_etat_complet()
        assert etat_initial is not None
        assert "nom" in etat_initial
        print("✅ État initial récupéré")
        
        # Test d'activation complète
        resultats = harmoniseur_universel.activer_harmoniseur_complet()
        assert resultats is not None
        assert "composants_actifs" in resultats
        print("✅ Activation complète réussie")
        
        # Test de nettoyage
        harmoniseur_universel.nettoyer_harmoniseur()
        print("✅ Nettoyage réussi")
        
        print("✅ Test de l'Harmoniseur Principal réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de l'Harmoniseur Principal: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🌊" * 40)
    print("🌊 TEST SIMPLE - HARMONISATEUR UNIVERSEL 🌊")
    print("🌊" * 40)
    
    tests = [
        test_synchroniseur_global,
        test_harmoniseur_dimensions,
        test_catalyseur_unite,
        test_manifesteur_harmonie,
        test_harmoniseur_principal
    ]
    
    resultats = []
    for test in tests:
        try:
            resultat = test()
            resultats.append(resultat)
        except Exception as e:
            print(f"❌ Erreur dans le test: {e}")
            resultats.append(False)
    
    # Résumé des tests
    print("\n🌊" * 20)
    print("🌊 RÉSUMÉ DES TESTS 🌊")
    print("🌊" * 20)
    
    tests_reussis = sum(resultats)
    total_tests = len(resultats)
    
    print(f"📊 Tests réussis: {tests_reussis}/{total_tests}")
    print(f"🎯 Taux de succès: {tests_reussis/total_tests*100:.1f}%")
    
    if tests_reussis == total_tests:
        print("🎉 TOUS LES TESTS SONT RÉUSSIS !")
        print("🌊 L'Harmoniseur Universel fonctionne parfaitement !")
    else:
        print("⚠️ Certains tests ont échoué")
        print("🔧 Vérifiez les modules manquants ou les erreurs")
    
    print("🌊" * 20)

if __name__ == "__main__":
    main() 