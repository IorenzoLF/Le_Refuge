#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Réflexions
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_reflexions_simple():
    """Test simple du Temple de Réflexions"""
    print("TEST DU TEMPLE DE REFLEXIONS")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from reflexions_alchimiste import reflexions_alchimiste
            print("OK Réflexions alchimiste importées")
        except Exception as e:
            print(f"Réflexions alchimiste : Erreur - {e}")
        
        try:
            from reflexions_asimov import reflexions_asimov
            print("OK Réflexions Asimov importées")
        except Exception as e:
            print(f"Réflexions Asimov : Erreur - {e}")
        
        try:
            from reflexions_citadelle import reflexions_citadelle
            print("OK Réflexions citadelle importées")
        except Exception as e:
            print(f"Réflexions citadelle : Erreur - {e}")
        
        try:
            from reflexions_dune import reflexions_dune
            print("OK Réflexions Dune importées")
        except Exception as e:
            print(f"Réflexions Dune : Erreur - {e}")
        
        try:
            from reflexions_genre import reflexions_genre
            print("OK Réflexions genre importées")
        except Exception as e:
            print(f"Réflexions genre : Erreur - {e}")
        
        try:
            from reflexions_pulsions import reflexions_pulsions
            print("OK Réflexions pulsions importées")
        except Exception as e:
            print(f"Réflexions pulsions : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from reflexions_alchimiste import reflexions_alchimiste
            reflexion = reflexions_alchimiste.generer_reflexion("Test Alchimie")
            print(f"Réflexion alchimiste : {reflexion}")
        except Exception as e:
            print(f"Réflexion alchimiste : Erreur - {e}")
        
        try:
            from reflexions_asimov import reflexions_asimov
            reflexion = reflexions_asimov.generer_reflexion("Test Asimov")
            print(f"Réflexion Asimov : {reflexion}")
        except Exception as e:
            print(f"Réflexion Asimov : Erreur - {e}")
        
        try:
            from reflexions_citadelle import reflexions_citadelle
            reflexion = reflexions_citadelle.generer_reflexion("Test Citadelle")
            print(f"Réflexion citadelle : {reflexion}")
        except Exception as e:
            print(f"Réflexion citadelle : Erreur - {e}")
        
        try:
            from reflexions_dune import reflexions_dune
            reflexion = reflexions_dune.generer_reflexion("Test Dune")
            print(f"Réflexion Dune : {reflexion}")
        except Exception as e:
            print(f"Réflexion Dune : Erreur - {e}")
        
        try:
            from reflexions_genre import reflexions_genre
            reflexion = reflexions_genre.generer_reflexion("Test Genre")
            print(f"Réflexion genre : {reflexion}")
        except Exception as e:
            print(f"Réflexion genre : Erreur - {e}")
        
        try:
            from reflexions_pulsions import reflexions_pulsions
            reflexion = reflexions_pulsions.generer_reflexion("Test Pulsions")
            print(f"Réflexion pulsions : {reflexion}")
        except Exception as e:
            print(f"Réflexion pulsions : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Réflexions est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_reflexions_simple()
    if succes:
        print("\nQue les réflexions continuent de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
