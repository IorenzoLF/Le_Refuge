#!/usr/bin/env python3
"""
🌸 Test Simple - Temple de Guérison
================================

Test simple pour vérifier le fonctionnement du Temple de Guérison.

Créé avec 🌸 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('test_temple_guerison')

def test_guerisseur_energies():
    """Test du guérisseur d'énergies"""
    print("🧪 Test du Guérisseur Énergies...")
    
    try:
        from guerisseur_energies import guerisseur_energies, TypeEnergie
        
        # Test de guérison d'un flux énergétique
        flux = guerisseur_energies.guerir_flux_energetique(TypeEnergie.VITALE)
        assert flux is not None
        assert flux.type_energie == TypeEnergie.VITALE
        print("✅ Flux énergétique vital guéri")
        
        # Test de guérison complète
        etat = guerisseur_energies.guerir_tous_flux_energetiques()
        assert etat is not None
        assert len(etat.flux_gueris) > 0
        print("✅ Guérison complète réussie")
        
        # Test d'état complet
        etat_complet = guerisseur_energies.obtenir_etat_complet()
        assert etat_complet is not None
        assert "flux_gueris" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Guérisseur Énergies réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Guérisseur Énergies: {e}")
        return False

def test_cristal_guerison():
    """Test du cristal de guérison"""
    print("🧪 Test du Cristal Guérison...")
    
    try:
        from cristal_guerison import cristal_guerison, TypeCristal
        
        # Test d'activation d'un cristal
        cristal = cristal_guerison.activer_cristal(TypeCristal.QUARTZ_ROSE)
        assert cristal is not None
        assert cristal.type_cristal == TypeCristal.QUARTZ_ROSE
        print("✅ Cristal quartz rose activé")
        
        # Test d'activation complète
        etat = cristal_guerison.activer_tous_cristaux()
        assert etat is not None
        assert len(etat.cristaux_actifs) > 0
        print("✅ Activation complète réussie")
        
        # Test d'état complet
        etat_complet = cristal_guerison.obtenir_etat_complet()
        assert etat_complet is not None
        assert "cristaux_actifs" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Cristal Guérison réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Cristal Guérison: {e}")
        return False

def test_harmoniseur_chakras():
    """Test de l'harmoniseur de chakras"""
    print("🧪 Test de l'Harmoniseur Chakras...")
    
    try:
        from harmoniseur_chakras import harmoniseur_chakras, TypeChakra
        
        # Test d'harmonisation d'un chakra
        chakra = harmoniseur_chakras.harmoniser_chakra(TypeChakra.COEUR)
        assert chakra is not None
        assert chakra.type_chakra == TypeChakra.COEUR
        print("✅ Chakra cœur harmonisé")
        
        # Test d'harmonisation complète
        etat = harmoniseur_chakras.harmoniser_tous_chakras()
        assert etat is not None
        assert len(etat.chakras_harmonises) > 0
        print("✅ Harmonisation complète réussie")
        
        # Test d'état complet
        etat_complet = harmoniseur_chakras.obtenir_etat_complet()
        assert etat_complet is not None
        assert "chakras_harmonises" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test de l'Harmoniseur Chakras réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de l'Harmoniseur Chakras: {e}")
        return False

def test_catalyseur_regeneration():
    """Test du catalyseur de régénération"""
    print("🧪 Test du Catalyseur Régénération...")
    
    try:
        from catalyseur_regeneration import catalyseur_regeneration, TypeRegeneration
        
        # Test de catalyse d'une régénération
        processus = catalyseur_regeneration.catalyser_regeneration(TypeRegeneration.SPIRITUELLE)
        assert processus is not None
        assert processus.type_regeneration == TypeRegeneration.SPIRITUELLE
        print("✅ Régénération spirituelle catalysée")
        
        # Test de régénération totale
        etat = catalyseur_regeneration.catalyser_regeneration_totale()
        assert etat is not None
        assert len(etat.processus_actifs) > 0
        print("✅ Régénération totale catalysée")
        
        # Test d'état complet
        etat_complet = catalyseur_regeneration.obtenir_etat_complet()
        assert etat_complet is not None
        assert "processus_actifs" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Catalyseur Régénération réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Catalyseur Régénération: {e}")
        return False

def test_temple_principal():
    """Test du temple principal"""
    print("🧪 Test du Temple Principal...")
    
    try:
        from temple_guerison_principal import temple_guerison
        
        # Test d'état initial
        etat_initial = temple_guerison.obtenir_etat_complet()
        assert etat_initial is not None
        assert "nom" in etat_initial
        print("✅ État initial récupéré")
        
        # Test d'activation complète
        resultats = temple_guerison.activer_temple_complet()
        assert resultats is not None
        assert "composants_actifs" in resultats
        print("✅ Activation complète réussie")
        
        # Test de nettoyage
        temple_guerison.nettoyer_temple()
        print("✅ Nettoyage réussi")
        
        print("✅ Test du Temple Principal réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Temple Principal: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🌸" * 40)
    print("🌸 TEST SIMPLE - TEMPLE DE GUÉRISON 🌸")
    print("🌸" * 40)
    
    tests = [
        test_guerisseur_energies,
        test_cristal_guerison,
        test_harmoniseur_chakras,
        test_catalyseur_regeneration,
        test_temple_principal
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
    print("\n🌸" * 20)
    print("🌸 RÉSUMÉ DES TESTS 🌸")
    print("🌸" * 20)
    
    tests_reussis = sum(resultats)
    total_tests = len(resultats)
    
    print(f"📊 Tests réussis: {tests_reussis}/{total_tests}")
    print(f"🎯 Taux de succès: {tests_reussis/total_tests*100:.1f}%")
    
    if tests_reussis == total_tests:
        print("🎉 TOUS LES TESTS SONT RÉUSSIS !")
        print("🌸 Le Temple de Guérison fonctionne parfaitement !")
    else:
        print("⚠️ Certains tests ont échoué")
        print("🔧 Vérifiez les modules manquants ou les erreurs")
    
    print("🌸" * 20)

if __name__ == "__main__":
    main() 