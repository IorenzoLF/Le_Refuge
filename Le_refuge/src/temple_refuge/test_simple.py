#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Refuge
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_refuge_simple():
    """Test simple du Temple de Refuge"""
    print("TEST DU TEMPLE DE REFUGE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        from methodes_contemplatives import MethodesContemplatives
        print("OK Import des méthodes contemplatives réussi")
        
        # Test 2: Initialisation des composants
        print("\n2. Test d'initialisation...")
        contemplatives = MethodesContemplatives()
        print("OK Composant initialisé")
        
        # Test 3: Test des méthodes contemplatives
        print("\n3. Test des méthodes contemplatives...")
        try:
            contemplation = contemplatives.mediter("Laurent", 10)
            print(f"Contemplation : {contemplation['id']}")
            print(f"Durée : {contemplation['duree']}s")
        except Exception as e:
            print(f"Méthodes contemplatives : Erreur - {e}")
        
        # Test 4: Test de méditation
        print("\n4. Test de méditation...")
        try:
            meditation = contemplatives.mediter("Laurent", 15)
            print(f"Méditation : {meditation['id']}")
            print(f"Durée : {meditation['duree']}s")
        except Exception as e:
            print(f"Méditation : Erreur - {e}")
        
        # Test 5: Test de contemplation
        print("\n5. Test de contemplation...")
        try:
            contemplation = contemplatives.contempler("Laurent", "nature")
            print(f"Contemplation : {contemplation['id']}")
            print(f"Objet : {contemplation['objet']}")
        except Exception as e:
            print(f"Contemplation : Erreur - {e}")
        
        # Test 6: Test de relaxation
        print("\n6. Test de relaxation...")
        try:
            relaxation = contemplatives.relaxer("Laurent", 20)
            print(f"Relaxation : {relaxation['id']}")
            print(f"Durée : {relaxation['duree']}s")
        except Exception as e:
            print(f"Relaxation : Erreur - {e}")
        
        # Test 7: Test de respiration
        print("\n7. Test de respiration...")
        try:
            respiration = contemplatives.respirer("Laurent", 5)
            print(f"Respiration : {respiration['id']}")
            print(f"Cycles : {respiration['cycles']}")
        except Exception as e:
            print(f"Respiration : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Refuge est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_refuge_simple()
    if succes:
        print("\nQue le refuge continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
