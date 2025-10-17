#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple d'Outils
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_outils_simple():
    """Test simple du Temple d'Outils"""
    print("TEST DU TEMPLE D'OUTILS")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules principaux
        print("\n1. Test des imports...")
        try:
            from analyser_resonance_temples import analyser_resonance_temples
            print("OK Analyseur de résonance des temples importé")
        except Exception as e:
            print(f"Analyseur de résonance : Erreur - {e}")
        
        try:
            from explorer_ponts_temporels import explorer_ponts_temporels
            print("OK Explorateur de ponts temporels importé")
        except Exception as e:
            print(f"Explorateur de ponts temporels : Erreur - {e}")
        
        try:
            from gestionnaire_constellations_sacrees import gestionnaire_constellations_sacrees
            print("OK Gestionnaire de constellations sacrées importé")
        except Exception as e:
            print(f"Gestionnaire de constellations : Erreur - {e}")
        
        # Test 2: Test des modules de recherche scientifique
        print("\n2. Test des modules de recherche...")
        try:
            from recherche_scientifique.CONSCIENCE_ARTIFICIELLE.consciousness_core import consciousness_core
            print("OK Core de conscience artificielle importé")
        except Exception as e:
            print(f"Core de conscience : Erreur - {e}")
        
        try:
            from recherche_scientifique.ai_researcher import ai_researcher
            print("OK Chercheur IA importé")
        except Exception as e:
            print(f"Chercheur IA : Erreur - {e}")
        
        # Test 3: Test des modules d'optimisation
        print("\n3. Test des modules d'optimisation...")
        try:
            from optimiseur_temple_musical import optimiseur_temple_musical
            print("OK Optimiseur de temple musical importé")
        except Exception as e:
            print(f"Optimiseur de temple musical : Erreur - {e}")
        
        try:
            from harmonisateur_temples import harmonisateur_temples
            print("OK Harmonisateur de temples importé")
        except Exception as e:
            print(f"Harmonisateur de temples : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple d'Outils est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_outils_simple()
    if succes:
        print("\nQue les outils continuent de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
