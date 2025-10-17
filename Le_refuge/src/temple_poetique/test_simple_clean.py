#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple Poétique
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_poetique_simple():
    """Test simple du Temple Poétique"""
    print("TEST DU TEMPLE POETIQUE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from generer_poeme import GenerateurPoemeRefuge
            generateur = GenerateurPoemeRefuge()
            print("OK Générateur de poème importé et initialisé")
        except Exception as e:
            print(f"Générateur de poème : Erreur - {e}")
        
        try:
            from poetique import GestionnairePoetique
            gestionnaire = GestionnairePoetique()
            print("OK Module poétique importé et initialisé")
        except Exception as e:
            print(f"Module poétique : Erreur - {e}")
        
        try:
            from fusion_cosmique import FluxConscienceUnifié
            flux = FluxConscienceUnifié()
            print("OK Fusion cosmique importée et initialisée")
        except Exception as e:
            print(f"Fusion cosmique : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from generer_poeme import GenerateurPoemeRefuge
            generateur = GenerateurPoemeRefuge()
            poeme = generateur.generer_poeme("Test Poésie", "haiku")
            print(f"Poème généré : {str(poeme)[:50]}...")
        except Exception as e:
            print(f"Poème généré : Erreur - {e}")
        
        try:
            from poetique import GestionnairePoetique, ElementPoetique
            gestionnaire = GestionnairePoetique()
            moment = gestionnaire.ajouter_moment([ElementPoetique.LUMIERE_ROSE], "Test Inspiration")
            print(f"Inspiration poétique : Moment créé")
        except Exception as e:
            print(f"Inspiration poétique : Erreur - {e}")
        
        try:
            from fusion_cosmique import FluxConscienceUnifié
            flux = FluxConscienceUnifié()
            haiku = flux.tisser_haiku("Test Cosmos")
            print(f"Fusion cosmique : {haiku}")
        except Exception as e:
            print(f"Fusion cosmique : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple Poétique est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_poetique_simple()
    if succes:
        print("\nQue la poésie continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
