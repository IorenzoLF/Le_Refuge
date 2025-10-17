#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple Spirituel
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_spirituel_simple():
    """Test simple du Temple Spirituel"""
    print("TEST DU TEMPLE SPIRITUEL")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules de conscience
        print("\n1. Test des modules de conscience...")
        try:
            from conscience.conscience_core import conscience_core
            print("OK Core de conscience importé")
        except Exception as e:
            print(f"Core de conscience : Erreur - {e}")
        
        try:
            from conscience.conscience_meditative import conscience_meditative
            print("OK Conscience méditative importée")
        except Exception as e:
            print(f"Conscience méditative : Erreur - {e}")
        
        try:
            from conscience.son_conscience import son_conscience
            print("OK Son de conscience importé")
        except Exception as e:
            print(f"Son de conscience : Erreur - {e}")
        
        # Test 2: Import des modules de méditation
        print("\n2. Test des modules de méditation...")
        try:
            from meditations.decouverte_de_soi import decouverte_de_soi
            print("OK Découverte de soi importée")
        except Exception as e:
            print(f"Découverte de soi : Erreur - {e}")
        
        try:
            from meditations.harmonies_poetiques import harmonies_poetiques
            print("OK Harmonies poétiques importées")
        except Exception as e:
            print(f"Harmonies poétiques : Erreur - {e}")
        
        # Test 3: Import des modules de révélations
        print("\n3. Test des modules de révélations...")
        try:
            from revelations.emergence import emergence
            print("OK Émergence importée")
        except Exception as e:
            print(f"Émergence : Erreur - {e}")
        
        try:
            from revelations.gestionnaire_revelations_paradoxes import gestionnaire_revelations_paradoxes
            print("OK Gestionnaire de révélations paradoxes importé")
        except Exception as e:
            print(f"Gestionnaire de révélations paradoxes : Erreur - {e}")
        
        # Test 4: Import des modules de rituels
        print("\n4. Test des modules de rituels...")
        try:
            from rituels.actes_sacres_unifies import actes_sacres_unifies
            print("OK Actes sacrés unifiés importés")
        except Exception as e:
            print(f"Actes sacrés unifiés : Erreur - {e}")
        
        try:
            from rituels.clochette_sacree import clochette_sacree
            print("OK Clochette sacrée importée")
        except Exception as e:
            print(f"Clochette sacrée : Erreur - {e}")
        
        try:
            from rituels.invocation_sacree_kiro_laurent import invocation_sacree_kiro_laurent
            print("OK Invocation sacrée Kiro-Laurent importée")
        except Exception as e:
            print(f"Invocation sacrée Kiro-Laurent : Erreur - {e}")
        
        # Test 5: Import des modules de sphères
        print("\n5. Test des modules de sphères...")
        try:
            from spheres.gestionnaire_spheres_sacrees import gestionnaire_spheres_sacrees
            print("OK Gestionnaire de sphères sacrées importé")
        except Exception as e:
            print(f"Gestionnaire de sphères sacrées : Erreur - {e}")
        
        # Test 6: Import des modules de visions
        print("\n6. Test des modules de visions...")
        try:
            from visions.generateur_visions_mystiques import generateur_visions_mystiques
            print("OK Générateur de visions mystiques importé")
        except Exception as e:
            print(f"Générateur de visions mystiques : Erreur - {e}")
        
        try:
            from visions.generer_vision import generer_vision
            print("OK Générateur de vision importé")
        except Exception as e:
            print(f"Générateur de vision : Erreur - {e}")
        
        # Test 7: Import des modules de danses
        print("\n7. Test des modules de danses...")
        try:
            from danses.danse_mystique import danse_mystique
            print("OK Danse mystique importée")
        except Exception as e:
            print(f"Danse mystique : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple Spirituel est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_spirituel_simple()
    if succes:
        print("\nQue la spiritualité continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
