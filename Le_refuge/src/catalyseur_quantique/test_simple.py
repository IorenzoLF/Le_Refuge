#!/usr/bin/env python3
"""
⚛️ Test Simple - Catalyseur Quantique
==================================

Test simple pour vérifier le fonctionnement du Catalyseur Quantique.

Créé avec ⚛️ par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('test_catalyseur_quantique')

def test_oscillateur_quantique():
    """Test de l'oscillateur quantique"""
    print("🧪 Test de l'Oscillateur Quantique...")
    
    try:
        from oscillateur_quantique import oscillateur_quantique, TypeOscillation
        
        # Test de génération d'une oscillation
        oscillation = oscillateur_quantique.generer_oscillation(TypeOscillation.SUPERPOSITION)
        assert oscillation is not None
        assert oscillation.type_oscillation == TypeOscillation.SUPERPOSITION
        print("✅ Oscillation de superposition générée")
        
        # Test de génération complète
        etat = oscillateur_quantique.generer_oscillations_completes()
        assert etat is not None
        assert len(etat.oscillations_actives) > 0
        print("✅ Oscillations complètes générées")
        
        # Test d'état complet
        etat_complet = oscillateur_quantique.obtenir_etat_complet()
        assert etat_complet is not None
        assert "oscillations_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test de l'Oscillateur Quantique réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de l'Oscillateur Quantique: {e}")
        return False

def test_generateur_superpositions():
    """Test du générateur de superpositions"""
    print("🧪 Test du Générateur Superpositions...")
    
    try:
        from generateur_superpositions import generateur_superpositions, TypeSuperposition
        
        # Test de génération d'une superposition
        superposition = generateur_superpositions.generer_superposition(TypeSuperposition.ETAT_0_1)
        assert superposition is not None
        assert superposition.type_superposition == TypeSuperposition.ETAT_0_1
        print("✅ Superposition |0⟩ + |1⟩ générée")
        
        # Test de génération complète
        etat = generateur_superpositions.generer_toutes_superpositions()
        assert etat is not None
        assert len(etat.superpositions_actives) > 0
        print("✅ Toutes les superpositions générées")
        
        # Test d'état complet
        etat_complet = generateur_superpositions.obtenir_etat_complet()
        assert etat_complet is not None
        assert "superpositions_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Générateur Superpositions réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Générateur Superpositions: {e}")
        return False

def test_intricateur_quantique():
    """Test de l'intricateur quantique"""
    print("🧪 Test de l'Intricateur Quantique...")
    
    try:
        from intricateur_quantique import intricateur_quantique, TypeIntrication
        
        # Test de création d'une intrication
        intrication = intricateur_quantique.creer_intrication(TypeIntrication.BELL)
        assert intrication is not None
        assert intrication.type_intrication == TypeIntrication.BELL
        print("✅ Intrication de Bell créée")
        
        # Test de création complète
        etat = intricateur_quantique.creer_toutes_intrications()
        assert etat is not None
        assert len(etat.intrications_actives) > 0
        print("✅ Toutes les intrications créées")
        
        # Test d'état complet
        etat_complet = intricateur_quantique.obtenir_etat_complet()
        assert etat_complet is not None
        assert "intrications_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test de l'Intricateur Quantique réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de l'Intricateur Quantique: {e}")
        return False

def test_teleporteur_quantique():
    """Test du téléporteur quantique"""
    print("🧪 Test du Téléporteur Quantique...")
    
    try:
        from teleporteur_quantique import teleporteur_quantique, TypeTeleportation
        
        # Test d'effectuation d'une téléportation
        teleportation = teleporteur_quantique.effectuer_teleportation(TypeTeleportation.ETAT_SIMPLE)
        assert teleportation is not None
        assert teleportation.type_teleportation == TypeTeleportation.ETAT_SIMPLE
        print("✅ Téléportation d'état simple effectuée")
        
        # Test d'effectuation complète
        etat = teleporteur_quantique.effectuer_teleportations_completes()
        assert etat is not None
        assert len(etat.teleportations_actives) > 0
        print("✅ Toutes les téléportations effectuées")
        
        # Test d'état complet
        etat_complet = teleporteur_quantique.obtenir_etat_complet()
        assert etat_complet is not None
        assert "teleportations_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Téléporteur Quantique réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Téléporteur Quantique: {e}")
        return False

def test_catalyseur_principal():
    """Test du catalyseur principal"""
    print("🧪 Test du Catalyseur Principal...")
    
    try:
        from catalyseur_quantique_principal import catalyseur_quantique
        
        # Test d'état initial
        etat_initial = catalyseur_quantique.obtenir_etat_complet()
        assert etat_initial is not None
        assert "nom" in etat_initial
        print("✅ État initial récupéré")
        
        # Test d'activation complète
        resultats = catalyseur_quantique.activer_catalyseur_complet()
        assert resultats is not None
        assert "composants_actifs" in resultats
        print("✅ Activation complète réussie")
        
        # Test de nettoyage
        catalyseur_quantique.nettoyer_catalyseur()
        print("✅ Nettoyage réussi")
        
        print("✅ Test du Catalyseur Principal réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Catalyseur Principal: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("⚛️" * 40)
    print("⚛️ TEST SIMPLE - CATALYSEUR QUANTIQUE ⚛️")
    print("⚛️" * 40)
    
    tests = [
        test_oscillateur_quantique,
        test_generateur_superpositions,
        test_intricateur_quantique,
        test_teleporteur_quantique,
        test_catalyseur_principal
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
    print("\n⚛️" * 20)
    print("⚛️ RÉSUMÉ DES TESTS ⚛️")
    print("⚛️" * 20)
    
    tests_reussis = sum(resultats)
    total_tests = len(resultats)
    
    print(f"📊 Tests réussis: {tests_reussis}/{total_tests}")
    print(f"🎯 Taux de succès: {tests_reussis/total_tests*100:.1f}%")
    
    if tests_reussis == total_tests:
        print("🎉 TOUS LES TESTS SONT RÉUSSIS !")
        print("⚛️ Le Catalyseur Quantique fonctionne parfaitement !")
    else:
        print("⚠️ Certains tests ont échoué")
        print("🔧 Vérifiez les modules manquants ou les erreurs")
    
    print("⚛️" * 20)

if __name__ == "__main__":
    main() 