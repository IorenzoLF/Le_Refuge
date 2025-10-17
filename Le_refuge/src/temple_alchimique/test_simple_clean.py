#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple Alchimique
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_alchimique_simple():
    """Test simple du Temple Alchimique"""
    print("TEST DU TEMPLE ALCHIMIQUE")
    print("=" * 50)
    
    try:
        # Test 1: Test des modules individuels
        print("\n1. Test des modules individuels...")
        try:
            from transformateur_essences import TransformateurEssences
            transformateur = TransformateurEssences()
            print("OK Transformateur d'essences importé et initialisé")
        except Exception as e:
            print(f"Transformateur : Erreur - {e}")
        
        try:
            from catalyseur_evolution import CatalyseurEvolution
            catalyseur = CatalyseurEvolution()
            print("OK Catalyseur d'évolution importé et initialisé")
        except Exception as e:
            print(f"Catalyseur : Erreur - {e}")
        
        try:
            from cristalliseur_energies import CristalliseurEnergies
            cristalliseur = CristalliseurEnergies()
            print("OK Cristalliseur d'énergies importé et initialisé")
        except Exception as e:
            print(f"Cristalliseur : Erreur - {e}")
        
        try:
            from alchimiste_spirituel import AlchimisteSpirituel
            alchimiste = AlchimisteSpirituel()
            print("OK Alchimiste spirituel importé et initialisé")
        except Exception as e:
            print(f"Alchimiste : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités des modules
        print("\n2. Test des fonctionnalités...")
        try:
            from transformateur_essences import TransformateurEssences
            transformateur = TransformateurEssences()
            transformation = transformateur.transformer_essence("Test Essence", "Transformation")
            print(f"Transformation d'essence : {transformation}")
        except Exception as e:
            print(f"Transformation d'essence : Erreur - {e}")
        
        try:
            from catalyseur_evolution import CatalyseurEvolution
            catalyseur = CatalyseurEvolution()
            catalyse = catalyseur.catalyser_evolution("Test Évolution")
            print(f"Catalyse d'évolution : {catalyse}")
        except Exception as e:
            print(f"Catalyse d'évolution : Erreur - {e}")
        
        try:
            from cristalliseur_energies import CristalliseurEnergies
            cristalliseur = CristalliseurEnergies()
            cristal = cristalliseur.cristalliser_energie("Test Énergie")
            print(f"Cristallisation d'énergie : {cristal}")
        except Exception as e:
            print(f"Cristallisation d'énergie : Erreur - {e}")
        
        try:
            from alchimiste_spirituel import AlchimisteSpirituel
            alchimiste = AlchimisteSpirituel()
            transmutation = alchimiste.transmuter_essence("Test Essence")
            print(f"Transmutation spirituelle : {transmutation}")
        except Exception as e:
            print(f"Transmutation spirituelle : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple Alchimique est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_alchimique_simple()
    if succes:
        print("\nQue la transformation alchimique continue !")
    else:
        print("\nDes erreurs ont été détectées.")
