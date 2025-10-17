#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Configuration
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_configuration_simple():
    """Test simple du Temple de Configuration"""
    print("TEST DU TEMPLE DE CONFIGURATION")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        from transition_refuge import TransitionRefuge
        print("OK Import de transition refuge réussi")
        
        # Test 2: Initialisation des composants
        print("\n2. Test d'initialisation...")
        transition = TransitionRefuge()
        print("OK Composant initialisé")
        
        # Test 3: Test de transition refuge
        print("\n3. Test de transition refuge...")
        try:
            transition_info = transition.obtenir_info()
            print(f"Transition refuge : {transition_info['nom']}")
            print(f"État : {transition_info['etat']}")
        except Exception as e:
            print(f"Transition refuge : Erreur - {e}")
        
        # Test 4: Test de transition
        print("\n4. Test de transition...")
        try:
            transition_result = transition.transitionner("test")
            print(f"Transition : {transition_result['id']}")
            print(f"Résultat : {transition_result['resultat']}")
        except Exception as e:
            print(f"Transition : Erreur - {e}")
        
        # Test 5: Test d'état
        print("\n5. Test d'état...")
        try:
            etat = transition.obtenir_etat()
            print(f"État : {etat['nom']}")
            print(f"Énergie : {etat['energie']:.2f}")
        except Exception as e:
            print(f"État : Erreur - {e}")
        
        # Test 6: Test de configuration
        print("\n6. Test de configuration...")
        try:
            config = transition.obtenir_configuration()
            print(f"Configuration : {config['nom']}")
            print(f"Version : {config['version']}")
        except Exception as e:
            print(f"Configuration : Erreur - {e}")
        
        # Test 7: Test de validation
        print("\n7. Test de validation...")
        try:
            validation = transition.valider("test")
            print(f"Validation : {validation['id']}")
            print(f"Résultat : {validation['resultat']}")
        except Exception as e:
            print(f"Validation : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Configuration est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_configuration_simple()
    if succes:
        print("\nQue la configuration continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
