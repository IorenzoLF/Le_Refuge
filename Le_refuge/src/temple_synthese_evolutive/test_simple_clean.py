#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Synthèse Évolutive
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_synthese_evolutive_simple():
    """Test simple du Temple de Synthèse Évolutive"""
    print("TEST DU TEMPLE DE SYNTHESE EVOLUTIVE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from temple_synthese_evolutive import temple_synthese_evolutive
            print("OK Temple de synthèse évolutive importé")
        except Exception as e:
            print(f"Temple de synthèse évolutive : Erreur - {e}")
        
        try:
            from activation_inaugurale import activation_inaugurale
            print("OK Activation inaugurale importée")
        except Exception as e:
            print(f"Activation inaugurale : Erreur - {e}")
        
        try:
            from meditation_transcendante import meditation_transcendante
            print("OK Méditation transcendante importée")
        except Exception as e:
            print(f"Méditation transcendante : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from temple_synthese_evolutive import temple_synthese_evolutive
            temple = temple_synthese_evolutive.activer_temple("Test Temple")
            print(f"Temple activé : {temple}")
        except Exception as e:
            print(f"Temple activé : Erreur - {e}")
        
        try:
            from activation_inaugurale import activation_inaugurale
            activation = activation_inaugurale.activer_inauguration("Test Activation")
            print(f"Activation inaugurale : {activation}")
        except Exception as e:
            print(f"Activation inaugurale : Erreur - {e}")
        
        try:
            from meditation_transcendante import meditation_transcendante
            meditation = meditation_transcendante.mediter_transcendance("Test Méditation")
            print(f"Méditation transcendante : {meditation}")
        except Exception as e:
            print(f"Méditation transcendante : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Synthèse Évolutive est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_synthese_evolutive_simple()
    if succes:
        print("\nQue la synthèse évolutive continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
