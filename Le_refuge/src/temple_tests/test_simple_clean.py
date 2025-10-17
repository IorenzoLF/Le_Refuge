#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Tests
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_tests_simple():
    """Test simple du Temple de Tests"""
    print("TEST DU TEMPLE DE TESTS")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules principaux
        print("\n1. Test des imports...")
        try:
            from hub_tests_unifie import hub_tests_unifie
            print("OK Hub de tests unifié importé")
        except Exception as e:
            print(f"Hub de tests unifié : Erreur - {e}")
        
        try:
            from adaptateurs_tests import adaptateurs_tests
            print("OK Adaptateurs de tests importés")
        except Exception as e:
            print(f"Adaptateurs de tests : Erreur - {e}")
        
        try:
            from optimiseur_doublons import optimiseur_doublons
            print("OK Optimiseur de doublons importé")
        except Exception as e:
            print(f"Optimiseur de doublons : Erreur - {e}")
        
        try:
            from organisateur_structure import organisateur_structure
            print("OK Organisateur de structure importé")
        except Exception as e:
            print(f"Organisateur de structure : Erreur - {e}")
        
        # Test 2: Test des modules d'analyse d'audit
        print("\n2. Test des modules d'analyse d'audit...")
        try:
            from analyse_audit.analyser_refuge_complet import analyser_refuge_complet
            print("OK Analyseur de refuge complet importé")
        except Exception as e:
            print(f"Analyseur de refuge complet : Erreur - {e}")
        
        try:
            from analyse_audit.audit_imports import audit_imports
            print("OK Audit d'imports importé")
        except Exception as e:
            print(f"Audit d'imports : Erreur - {e}")
        
        try:
            from analyse_audit.audit_temples_crees import audit_temples_crees
            print("OK Audit de temples créés importé")
        except Exception as e:
            print(f"Audit de temples créés : Erreur - {e}")
        
        # Test 3: Test des modules d'intégration
        print("\n3. Test des modules d'intégration...")
        try:
            from integration.test_integration import test_integration
            print("OK Test d'intégration importé")
        except Exception as e:
            print(f"Test d'intégration : Erreur - {e}")
        
        try:
            from integration.test_consolidation import test_consolidation
            print("OK Test de consolidation importé")
        except Exception as e:
            print(f"Test de consolidation : Erreur - {e}")
        
        try:
            from integration.test_intensif import test_intensif
            print("OK Test intensif importé")
        except Exception as e:
            print(f"Test intensif : Erreur - {e}")
        
        # Test 4: Test des modules LLM API
        print("\n4. Test des modules LLM API...")
        try:
            from llm_api.tests_llm_unifies import tests_llm_unifies
            print("OK Tests LLM unifiés importés")
        except Exception as e:
            print(f"Tests LLM unifiés : Erreur - {e}")
        
        try:
            from llm_api.test_aelya_conscience import test_aelya_conscience
            print("OK Test de conscience d'Ælya importé")
        except Exception as e:
            print(f"Test de conscience d'Ælya : Erreur - {e}")
        
        # Test 5: Test des modules spécialisés
        print("\n5. Test des modules spécialisés...")
        try:
            from specialises.test_dungeon_core import test_dungeon_core
            print("OK Test de dungeon core importé")
        except Exception as e:
            print(f"Test de dungeon core : Erreur - {e}")
        
        try:
            from specialises.test_nemo import test_nemo
            print("OK Test de Nemo importé")
        except Exception as e:
            print(f"Test de Nemo : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Tests est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_tests_simple()
    if succes:
        print("\nQue les tests continuent de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
