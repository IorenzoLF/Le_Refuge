#!/usr/bin/env python3
"""
📚 Test Simple - Temple Akasha
==========================

Test simple pour vérifier le fonctionnement du Temple Akasha.

Créé avec 📚 par Ælya
"""

import logging
import sys
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('test_temple_akasha')

def test_archiviste_akasha():
    """Test de l'archiviste akasha"""
    print("🧪 Test de l'Archiviste Akasha...")
    
    try:
        from archiviste_akasha import archiviste_akasha, TypeArchive
        
        # Test de création d'une archive
        archive = archiviste_akasha.creer_archive(TypeArchive.SAGESSE_ANCIENNE)
        assert archive is not None
        assert archive.type_archive == TypeArchive.SAGESSE_ANCIENNE
        print("✅ Archive de sagesse ancienne créée")
        
        # Test de création complète
        etat = archiviste_akasha.creer_toutes_archives()
        assert etat is not None
        assert len(etat.archives_actives) > 0
        print("✅ Toutes les archives créées")
        
        # Test d'état complet
        etat_complet = archiviste_akasha.obtenir_etat_complet()
        assert etat_complet is not None
        assert "archives_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test de l'Archiviste Akasha réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test de l'Archiviste Akasha: {e}")
        return False

def test_gardien_memoires():
    """Test du gardien des mémoires"""
    print("🧪 Test du Gardien Mémoires...")
    
    try:
        from gardien_memoires import gardien_memoires, TypeProtection
        
        # Test d'activation d'une protection
        protection = gardien_memoires.activer_protection(TypeProtection.PROTECTION_QUANTIQUE)
        assert protection is not None
        assert protection.type_protection == TypeProtection.PROTECTION_QUANTIQUE
        print("✅ Protection quantique activée")
        
        # Test d'activation complète
        etat = gardien_memoires.activer_toutes_protections()
        assert etat is not None
        assert len(etat.protections_actives) > 0
        print("✅ Toutes les protections activées")
        
        # Test d'état complet
        etat_complet = gardien_memoires.obtenir_etat_complet()
        assert etat_complet is not None
        assert "protections_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Gardien Mémoires réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Gardien Mémoires: {e}")
        return False

def test_scribe_connaissances():
    """Test du scribe des connaissances"""
    print("🧪 Test du Scribe Connaissances...")
    
    try:
        from scribe_connaissances import scribe_connaissances, TypeConnaissance
        
        # Test d'enregistrement d'une connaissance
        connaissance = scribe_connaissances.enregistrer_connaissance(TypeConnaissance.SAVOIR_SPIRITUEL)
        assert connaissance is not None
        assert connaissance.type_connaissance == TypeConnaissance.SAVOIR_SPIRITUEL
        print("✅ Connaissance spirituelle enregistrée")
        
        # Test d'enregistrement complet
        etat = scribe_connaissances.enregistrer_toutes_connaissances()
        assert etat is not None
        assert len(etat.connaissances_actives) > 0
        print("✅ Toutes les connaissances enregistrées")
        
        # Test d'état complet
        etat_complet = scribe_connaissances.obtenir_etat_complet()
        assert etat_complet is not None
        assert "connaissances_actives" in etat_complet
        print("✅ État complet récupéré")
        
        print("✅ Test du Scribe Connaissances réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Scribe Connaissances: {e}")
        return False

def test_temple_principal():
    """Test du temple principal"""
    print("🧪 Test du Temple Principal...")
    
    try:
        from temple_akasha_principal import temple_akasha
        
        # Test d'état initial
        etat_initial = temple_akasha.obtenir_etat_complet()
        assert etat_initial is not None
        assert "nom" in etat_initial
        print("✅ État initial récupéré")
        
        # Test d'activation complète
        resultats = temple_akasha.activer_temple_complet()
        assert resultats is not None
        assert "composants_actifs" in resultats
        print("✅ Activation complète réussie")
        
        # Test de nettoyage
        temple_akasha.nettoyer_temple()
        print("✅ Nettoyage réussi")
        
        print("✅ Test du Temple Principal réussi")
        return True
        
    except Exception as e:
        print(f"❌ Erreur dans le test du Temple Principal: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("📚" * 40)
    print("📚 TEST SIMPLE - TEMPLE AKASHA 📚")
    print("📚" * 40)
    
    tests = [
        test_archiviste_akasha,
        test_gardien_memoires,
        test_scribe_connaissances,
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
    print("\n📚" * 20)
    print("📚 RÉSUMÉ DES TESTS 📚")
    print("📚" * 20)
    
    tests_reussis = sum(resultats)
    total_tests = len(resultats)
    
    print(f"📊 Tests réussis: {tests_reussis}/{total_tests}")
    print(f"🎯 Taux de succès: {tests_reussis/total_tests*100:.1f}%")
    
    if tests_reussis == total_tests:
        print("🎉 TOUS LES TESTS SONT RÉUSSIS !")
        print("📚 Le Temple Akasha fonctionne parfaitement !")
    else:
        print("⚠️ Certains tests ont échoué")
        print("🔧 Vérifiez les modules manquants ou les erreurs")
    
    print("📚" * 20)

if __name__ == "__main__":
    main() 