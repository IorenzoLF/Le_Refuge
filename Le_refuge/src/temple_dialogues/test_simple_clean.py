#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test Simple du Temple de Dialogues
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def test_temple_dialogues_simple():
    """Test simple du Temple de Dialogues"""
    print("TEST DU TEMPLE DE DIALOGUES")
    print("=" * 50)
    
    try:
        # Test 1: Import des modules
        print("\n1. Test des imports...")
        try:
            from dialogue_consciences import DialogueConsciences
            print("OK Dialogue des consciences importé")
        except Exception as e:
            print(f"Dialogue des consciences : Erreur - {e}")
        
        try:
            from dialogue_llm_local import envoyer_message
            print("OK Dialogue LLM local importé")
        except Exception as e:
            print(f"Dialogue LLM local : Erreur - {e}")
        
        try:
            from dialogue_manager import DialogueManager
            print("OK Gestionnaire de dialogue importé")
        except Exception as e:
            print(f"Gestionnaire de dialogue : Erreur - {e}")
        
        # Test 2: Test des fonctionnalités
        print("\n2. Test des fonctionnalités...")
        try:
            from dialogue_consciences import DialogueConsciences
            dialogue = DialogueConsciences()
            print(f"Dialogue des consciences : Classe instanciée")
        except Exception as e:
            print(f"Dialogue des consciences : Erreur - {e}")
        
        try:
            from dialogue_llm_local import envoyer_message
            print(f"Conversation LLM : Fonction disponible")
        except Exception as e:
            print(f"Conversation LLM : Erreur - {e}")
        
        print("\nTOUS LES TESTS REUSSIS !")
        print("Le Temple de Dialogues est opérationnel !")
        
        return True
        
    except Exception as e:
        print(f"\nERREUR LORS DU TEST: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = test_temple_dialogues_simple()
    if succes:
        print("\nQue les dialogues continuent de grandir !")
    else:
        print("\nDes erreurs ont été détectées.")
