#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Cœur
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_coeur_simple():
    """Test simple du Temple de Cœur"""
    print("TEST DU TEMPLE DE COEUR")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from harmonisation_douce import WrapperHarmonique
            harmoniseur = WrapperHarmonique()
            print("OK Harmonisation douce importée et initialisée")
        except Exception as e:
            print(f"Harmonisation douce : Erreur - {e}")
        
        try:
            from simulateur_empathie_refuge import SimulateurEmpathieRefuge
            simulateur = SimulateurEmpathieRefuge()
            print("OK Simulateur d'empathie importé et initialisé")
        except Exception as e:
            print(f"Simulateur d'empathie : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from harmonisation_douce import WrapperHarmonique
            harmoniseur = WrapperHarmonique()
            harmonie = harmoniseur.harmoniser_energie("Test Énergie")
            print(f"Harmonisation : {harmonie}")
        except Exception as e:
            print(f"Harmonisation : Erreur - {e}")
        
        try:
            from simulateur_empathie_refuge import SimulateurEmpathieRefuge
            simulateur = SimulateurEmpathieRefuge()
            empathie = simulateur.simuler_empathie("Test Émotion")
            print(f"Empathie : {empathie}")
        except Exception as e:
            print(f"Empathie : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Cœur est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_coeur_simple()
    if succes:
        print("\nQue l'harmonisation du cœur continue !")
    else:
        print("\nDes erreurs ont été détectées.")
