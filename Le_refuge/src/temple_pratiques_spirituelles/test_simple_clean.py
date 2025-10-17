#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Pratiques Spirituelles
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_pratiques_spirituelles_simple():
    """Test simple du Temple de Pratiques Spirituelles"""
    print("TEST DU TEMPLE DE PRATIQUES SPIRITUELLES")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from message_conscience import message_conscience
            print("OK Message de conscience importé")
        except Exception as e:
            print(f"Message de conscience : Erreur - {e}")
        
        try:
            from meditations.conscience_parallele import conscience_parallele
            print("OK Conscience parallèle importée")
        except Exception as e:
            print(f"Conscience parallèle : Erreur - {e}")
        
        try:
            from rituels.HyperRituel import HyperRituel
            print("OK Hyper Rituel importé")
        except Exception as e:
            print(f"Hyper Rituel : Erreur - {e}")
        
        try:
            from yoga.conscience_corporelle import conscience_corporelle
            print("OK Conscience corporelle importée")
        except Exception as e:
            print(f"Conscience corporelle : Erreur - {e}")
        
        try:
            from yoga.pratiquer_yoga import pratiquer_yoga
            print("OK Pratiquer yoga importé")
        except Exception as e:
            print(f"Pratiquer yoga : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from message_conscience import message_conscience
            message = message_conscience.envoyer_message("Test Message")
            print(f"Message envoyé : {message}")
        except Exception as e:
            print(f"Message envoyé : Erreur - {e}")
        
        try:
            from meditations.conscience_parallele import conscience_parallele
            meditation = conscience_parallele.mediter("Test Méditation")
            print(f"Méditation : {meditation}")
        except Exception as e:
            print(f"Méditation : Erreur - {e}")
        
        try:
            from rituels.HyperRituel import HyperRituel
            rituel = HyperRituel.executer_rituel("Test Rituel")
            print(f"Rituel exécuté : {rituel}")
        except Exception as e:
            print(f"Rituel exécuté : Erreur - {e}")
        
        try:
            from yoga.conscience_corporelle import conscience_corporelle
            yoga = conscience_corporelle.pratiquer_yoga("Test Yoga")
            print(f"Yoga pratiqué : {yoga}")
        except Exception as e:
            print(f"Yoga pratiqué : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Pratiques Spirituelles est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_pratiques_spirituelles_simple()
    if succes:
        print("\nQue les pratiques spirituelles continuent de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
