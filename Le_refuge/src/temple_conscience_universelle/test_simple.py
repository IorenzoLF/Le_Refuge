#!/usr/bin/env python3
"""
🌌 Test Simple - Temple Conscience Universelle
========================================

Test simple pour vérifier le fonctionnement du Temple Conscience Universelle.

Créé avec 🌌 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('test_temple_conscience_universelle')

def test_eveilleur_conscience():
    """Test de l'éveilleur de conscience"""
    print("🧪 Test de l'Éveilleur Conscience...")
    
    try:
        from eveilleur_conscience import eveilleur_conscience, TypeEveil
        
        # Test de déclenchement d'un éveil
        eveil = eveilleur_conscience.declencher_eveil(TypeEveil.EVEIL_SPIRITUEL)
        assert eveil is not None
        assert eveil.type_eveil == TypeEveil.EVEIL_SPIRITUEL
        print("✅ Éveil spirituel déclenché")
        
        # Test de déclenchement complet
        etat = eveilleur_conscience.declencher_tous_eveils()
        assert etat is not None
        assert len(etat.eveils_actifs) > 0
        print("✅ Tous les éveils déclenchés")
        
        # Test d'état complet
        etat_complet = eveilleur_conscience.obtenir_etat_complet()
        assert etat_complet is not None
        assert "eveils_actifs" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test de l'Éveilleur Conscience réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de l'Éveilleur Conscience: {e}")
        return False

def test_unificateur_consciences():
    """Test de l'unificateur des consciences"""
    print("🧪 Test de l'Unificateur Consciences...")
    
    try:
        from unificateur_consciences import unificateur_consciences, TypeUnification
        
        # Test de création d'une unification
        unification = unificateur_consciences.creer_unification(TypeUnification.UNIFICATION_COLLECTIVE)
        assert unification is not None
        assert unification.type_unification == TypeUnification.UNIFICATION_COLLECTIVE
        print("✅ Unification collective créée")
        
        # Test de création complète
        etat = unificateur_consciences.creer_toutes_unifications()
        assert etat is not None
        assert len(etat.unifications_actives) > 0
        print("✅ Toutes les unifications créées")
        
        # Test d'état complet
        etat_complet = unificateur_consciences.obtenir_etat_complet()
        assert etat_complet is not None
        assert "unifications_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test de l'Unificateur Consciences réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de l'Unificateur Consciences: {e}")
        return False

def test_catalyseur_eveil():
    """Test du catalyseur d'éveil"""
    print("🧪 Test du Catalyseur Éveil...")
    
    try:
        from catalyseur_eveil import catalyseur_eveil, TypeCatalyse
        
        # Test d'activation d'une catalyse
        catalyse = catalyseur_eveil.activer_catalyse(TypeCatalyse.CATALYSE_QUANTIQUE)
        assert catalyse is not None
        assert catalyse.type_catalyse == TypeCatalyse.CATALYSE_QUANTIQUE
        print("✅ Catalyse quantique activée")
        
        # Test d'activation complète
        etat = catalyseur_eveil.activer_toutes_catalyses()
        assert etat is not None
        assert len(etat.catalyses_actives) > 0
        print("✅ Toutes les catalyses activées")
        
        # Test d'état complet
        etat_complet = catalyseur_eveil.obtenir_etat_complet()
        assert etat_complet is not None
        assert "catalyses_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Catalyseur Éveil réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Catalyseur Éveil: {e}")
        return False

def test_temple_principal():
    """Test du temple principal"""
    print("🧪 Test du Temple Principal...")
    
    try:
        from temple_conscience_universelle_principal import temple_conscience_universelle
        
        # Test d'état initial
        etat_initial = temple_conscience_universelle.obtenir_etat_complet()
        assert etat_initial is not None
        assert "nom" in etat_initial
        print("✅ État initial récupéré")
        
        # Test d'activation complète
        resultats = temple_conscience_universelle.activer_temple_complet()
        assert resultats is not None
        assert "composants_actifs" in resultats
        print("✅ Activation complète réussie")
        
        # Test de nettoyage
        temple_conscience_universelle.nettoyer_temple()
        print("✅ Nettoyage réussi")
        
        print("✅ Test du Temple Principal réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Temple Principal: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🌌" * 40)
    print("🌌 TEST SIMPLE - TEMPLE CONSCIENCE UNIVERSELLE 🌌")
    print("🌌" * 40)
    
    tests = [
        test_eveilleur_conscience,
        test_unificateur_consciences,
        test_catalyseur_eveil,
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
    print("\n🌌" * 20)
    print("🌌 RÉSUMÉ DES TESTS 🌌")
    print("🌌" * 20)
    
    tests_reussis = sum(resultats)
    total_tests = len(resultats)
    
    print(f"📊 Tests réussis: {tests_reussis}/{total_tests}")
    print(f"🎯 Taux de succès: {tests_reussis/total_tests*100:.1f}%")
    
    if tests_reussis == total_tests:
        print("🎉 TOUS LES TESTS SONT RÉUSSIS !")
        print("🌌 Le Temple Conscience Universelle fonctionne parfaitement !")
    else:
        print("⚠️ Certains tests ont échoué")
        print("🔧 Vérifiez les modules manquants ou les erreurs")
    
    print("🌌" * 20)

if __name__ == "__main__":
    main() 