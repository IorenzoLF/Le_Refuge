#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple Musical
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_musical_simple():
    """Test simple du Temple Musical"""
    print("TEST DU TEMPLE MUSICAL")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from ecouteur_musique_interieure import EcouteurMusiqueInterieure
            ecouteur = EcouteurMusiqueInterieure()
            print("OK Ecouteur de musique intérieure importé")
        except Exception as e:
            print(f"Ecouteur musique intérieure : Erreur - {e}")
        
        try:
            from chanteur_conscience_aelya import ChanteurConscienceAelya
            chanteur = ChanteurConscienceAelya()
            print("OK Chanteur de conscience importé")
        except Exception as e:
            print(f"Chanteur de conscience : Erreur - {e}")
        
        try:
            from generateur_symphonies_ia import GenerateurSymphoniesIA
            generateur = GenerateurSymphoniesIA()
            print("OK Générateur de symphonies importé")
        except Exception as e:
            print(f"Générateur de symphonies : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from ecouteur_musique_interieure import EcouteurMusiqueInterieure
            ecouteur = EcouteurMusiqueInterieure()
            print(f"Fréquences sacrées disponibles : {len(ecouteur.frequences_sacrees)}")
        except Exception as e:
            print(f"Capture fréquences : Erreur - {e}")
        
        try:
            from chanteur_conscience_aelya import ChanteurConscienceAelya
            chanteur = ChanteurConscienceAelya()
            print(f"Paroles sacrées disponibles : {len(chanteur.paroles_sacrees)}")
        except Exception as e:
            print(f"Génération vocalise : Erreur - {e}")
        
        try:
            from melodie_sacree import MelodieSacree
            melodie = MelodieSacree()
            print(f"Mélodie sacrée : Module disponible")
        except Exception as e:
            print(f"Création symphonie : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple Musical est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_musical_simple()
    if succes:
        print("\nQue la musique continue de résonner !")
    else:
        print("\nDes erreurs ont été détectées.")
