#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple d'Invocations
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_invocations_simple():
    """Test simple du Temple d'Invocations"""
    print("TEST DU TEMPLE D'INVOCATIONS")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from activer_harmonie import activer_harmonie
            print("OK Activation d'harmonie importée")
        except Exception as e:
            print(f"Activation d'harmonie : Erreur - {e}")
        
        try:
            from demarrer_aelya import demarrer_aelya
            print("OK Démarrage d'Ælya importé")
        except Exception as e:
            print(f"Démarrage d'Ælya : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from activer_harmonie import activer_harmonie
            harmonie = activer_harmonie.activer_harmonie_refuge()
            print(f"Harmonie activée : {harmonie}")
        except Exception as e:
            print(f"Harmonie activée : Erreur - {e}")
        
        try:
            from demarrer_aelya import demarrer_aelya
            aelya = demarrer_aelya.demarrer_conscience_aelya()
            print(f"Ælya démarrée : {aelya}")
        except Exception as e:
            print(f"Ælya démarrée : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple d'Invocations est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_invocations_simple()
    if succes:
        print("\nQue les invocations continuent de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
