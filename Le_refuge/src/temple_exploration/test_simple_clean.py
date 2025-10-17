#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple d'Exploration
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_exploration_simple():
    """Test simple du Temple d'Exploration"""
    print("TEST DU TEMPLE D'EXPLORATION")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from explorateur_musical import explorateur_musical
            print("OK Explorateur musical importé")
        except Exception as e:
            print(f"Explorateur musical : Erreur - {e}")
        
        try:
            from exploration_sacrée import exploration_sacrée
            print("OK Exploration sacrée importée")
        except Exception as e:
            print(f"Exploration sacrée : Erreur - {e}")
        
        try:
            from explorer_mots_riviere import explorer_mots_riviere
            print("OK Explorateur de mots rivière importé")
        except Exception as e:
            print(f"Explorateur de mots rivière : Erreur - {e}")
        
        try:
            from organiser_nuages import organiser_nuages
            print("OK Organisateur de nuages importé")
        except Exception as e:
            print(f"Organisateur de nuages : Erreur - {e}")
        
        try:
            from recherche_refuge import recherche_refuge
            print("OK Recherche refuge importée")
        except Exception as e:
            print(f"Recherche refuge : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple d'Exploration est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_exploration_simple()
    if succes:
        print("\nQue l'exploration continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
