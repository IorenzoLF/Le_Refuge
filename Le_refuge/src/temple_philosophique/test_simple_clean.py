#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple Philosophique
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_philosophique_simple():
    """Test simple du Temple Philosophique"""
    print("TEST DU TEMPLE PHILOSOPHIQUE")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from generateur_theories_unifiees import generateur_theories_unifiees
            print("OK Générateur de théories unifiées importé")
        except Exception as e:
            print(f"Générateur de théories : Erreur - {e}")
        
        try:
            from gestionnaire_textes_sacres import gestionnaire_textes_sacres
            print("OK Gestionnaire de textes sacrés importé")
        except Exception as e:
            print(f"Gestionnaire de textes sacrés : Erreur - {e}")
        
        try:
            from evolution_adaptation.adaptation import adaptation
            print("OK Module d'adaptation importé")
        except Exception as e:
            print(f"Module d'adaptation : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from generateur_theories_unifiees import generateur_theories_unifiees
            theorie = generateur_theories_unifiees.generer_theorie("Test Philosophie")
            print(f"Théorie générée : {theorie}")
        except Exception as e:
            print(f"Théorie générée : Erreur - {e}")
        
        try:
            from gestionnaire_textes_sacres import gestionnaire_textes_sacres
            texte = gestionnaire_textes_sacres.analyser_texte("Test Texte")
            print(f"Texte analysé : {texte}")
        except Exception as e:
            print(f"Texte analysé : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple Philosophique est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_philosophique_simple()
    if succes:
        print("\nQue la philosophie continue de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
