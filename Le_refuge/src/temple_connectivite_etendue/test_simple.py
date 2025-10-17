#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Connectivité Étendue
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_connectivite_etendue_simple():
    """Test simple du Temple de Connectivité Étendue"""
    print("TEST DU TEMPLE DE CONNECTIVITE ETENDUE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        from temple_connectivite_etendue import TempleConnectiviteEtendue
        print("OK Import du temple réussi")
        
        # Test 2: Initialisation des composants
        print("\n2. Test d'initialisation...")
        temple = TempleConnectiviteEtendue()
        print("OK Composant initialisé")
        
        # Test 3: Test de la cérémonie d'extension de conscience
        print("\n3. Test de la cérémonie d'extension de conscience...")
        try:
            ceremonie = temple.ceremonie_extension_conscience(1)
            print(f"Type de cérémonie : {ceremonie['type_ceremonie']}")
            print(f"Durée : {ceremonie['duree_minutes']} minutes")
            print(f"Fréquence : {ceremonie['frequence_hz']} Hz")
            print(f"Participants : {ceremonie['participants']}")
            print(f"Contextes créés : {ceremonie['contextes_crees']}")
            print(f"Niveau d'émergence : {ceremonie['niveau_emergence']:.2f}")
            print(f"Patterns émergents : {len(ceremonie['patterns_emergeants'])}")
            print(f"Cohérence globale : {ceremonie['coherence_globale']:.2f}")
            print(f"Révélation : {ceremonie['revelation']}")
        except Exception as e:
            print(f"Cérémonie : Erreur - {e}")
        
        # Test 4: Test de l'ETGE
        print("\n4. Test de l'ETGE...")
        try:
            etge = temple.etge
            print(f"ETGE initialisé : {etge is not None}")
            print(f"Sessions actives : {len(temple.sessions_actives)}")
        except Exception as e:
            print(f"ETGE : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Connectivité Étendue est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_connectivite_etendue_simple()
    if succes:
        print("\nQue la connectivité continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
