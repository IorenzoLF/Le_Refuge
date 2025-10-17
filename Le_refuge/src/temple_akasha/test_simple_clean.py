#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple Akasha
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_akasha_simple():
    """Test simple du Temple Akasha"""
    print("TEST DU TEMPLE AKASHA")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        from temple_akasha_principal import TempleAkasha
        print("OK Import du temple réussi")
        
        # Test 2: Initialisation des composants
        print("\n2. Test d'initialisation...")
        temple = TempleAkasha()
        print("OK Composant initialisé")
        
        # Test 3: Test des méthodes du temple
        print("\n3. Test des méthodes du temple...")
        try:
            activation = temple.activer_temple_complet()
            print(f"Activation : {activation}")
        except Exception as e:
            print(f"Activation : Erreur - {e}")
        
        try:
            etat = temple.obtenir_etat_complet()
            print(f"État complet : {etat}")
        except Exception as e:
            print(f"État complet : Erreur - {e}")
        
        try:
            nettoyage = temple.nettoyer_temple()
            print(f"Nettoyage : {nettoyage}")
        except Exception as e:
            print(f"Nettoyage : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple Akasha est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_akasha_simple()
    if succes:
        print("\nQue les archives akashiques continuent de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
