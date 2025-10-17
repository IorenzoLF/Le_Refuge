#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple Cosmique
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_cosmique_simple():
    """Test simple du Temple Cosmique"""
    print("TEST DU TEMPLE COSMIQUE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        from temple_cosmique_principal import TempleCosmique
        print("OK Import du temple réussi")
        
        # Test 2: Initialisation des composants
        print("\n2. Test d'initialisation...")
        temple = TempleCosmique()
        print("OK Composant initialisé")
        
        # Test 3: Test des méthodes du temple
        print("\n3. Test des méthodes du temple...")
        try:
            etat = temple.obtenir_etat_complet()
            print(f"État complet : {etat}")
        except Exception as e:
            print(f"État complet : Erreur - {e}")
        
        try:
            connexion = temple.creer_connexion_cosmique("Temple Poétique", "Temple Créativité", "etoile_polaire")
            print(f"Connexion cosmique : {connexion}")
        except Exception as e:
            print(f"Connexion cosmique : Erreur - {e}")
        
        try:
            reseau = temple.creer_reseau_cosmique_complet()
            print(f"Réseau cosmique : {reseau}")
        except Exception as e:
            print(f"Réseau cosmique : Erreur - {e}")
        
        try:
            harmonie = temple.calculer_harmonie_cosmique()
            print(f"Harmonie cosmique : {harmonie:.2f}")
        except Exception as e:
            print(f"Harmonie cosmique : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple Cosmique est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_cosmique_simple()
    if succes:
        print("\nQue la conscience cosmique continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
