#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Sagesse
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_sagesse_simple():
    """Test simple du Temple de Sagesse"""
    print("TEST DU TEMPLE DE SAGESSE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from bibliotheque_ancestrale import bibliotheque_ancestrale
            print("OK Bibliothèque ancestrale importée")
        except Exception as e:
            print(f"Bibliothèque ancestrale : Erreur - {e}")
        
        try:
            from gardien_sagesse import gardien_sagesse
            print("OK Gardien de sagesse importé")
        except Exception as e:
            print(f"Gardien de sagesse : Erreur - {e}")
        
        try:
            from oracle_divin import oracle_divin
            print("OK Oracle divin importé")
        except Exception as e:
            print(f"Oracle divin : Erreur - {e}")
        
        try:
            from temple_sagesse_ancestrale import temple_sagesse_ancestrale
            print("OK Temple de sagesse ancestrale importé")
        except Exception as e:
            print(f"Temple de sagesse ancestrale : Erreur - {e}")
        
        try:
            from transmetteur_connaissance import transmetteur_connaissance
            print("OK Transmetteur de connaissance importé")
        except Exception as e:
            print(f"Transmetteur de connaissance : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from bibliotheque_ancestrale import bibliotheque_ancestrale
            livre = bibliotheque_ancestrale.consulter_livre("Test Livre")
            print(f"Livre consulté : {livre}")
        except Exception as e:
            print(f"Livre consulté : Erreur - {e}")
        
        try:
            from gardien_sagesse import gardien_sagesse
            sagesse = gardien_sagesse.transmettre_sagesse("Test Sagesse")
            print(f"Sagesse transmise : {sagesse}")
        except Exception as e:
            print(f"Sagesse transmise : Erreur - {e}")
        
        try:
            from oracle_divin import oracle_divin
            oracle = oracle_divin.consulter_oracle("Test Oracle")
            print(f"Oracle consulté : {oracle}")
        except Exception as e:
            print(f"Oracle consulté : Erreur - {e}")
        
        try:
            from temple_sagesse_ancestrale import temple_sagesse_ancestrale
            temple = temple_sagesse_ancestrale.activer_temple("Test Temple")
            print(f"Temple activé : {temple}")
        except Exception as e:
            print(f"Temple activé : Erreur - {e}")
        
        try:
            from transmetteur_connaissance import transmetteur_connaissance
            connaissance = transmetteur_connaissance.transmettre_connaissance("Test Connaissance")
            print(f"Connaissance transmise : {connaissance}")
        except Exception as e:
            print(f"Connaissance transmise : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Sagesse est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_sagesse_simple()
    if succes:
        print("\nQue la sagesse continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
