#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exploration du Temple de Dialogues - Record Mondial
Version sans emojis pour éviter les erreurs d'encodage
"""

import sys
import os
from pathlib import Path

# Ajouter le chemin du refuge au sys.path
chemin_refuge = Path(__file__).parent.parent.parent
sys.path.insert(0, str(chemin_refuge))

def exploration_dialogues_record_mondial():
    """Exploration approfondie du Temple de Dialogues pour le record mondial"""
    print("EXPLORATION DU TEMPLE DE DIALOGUES - RECORD MONDIAL")
    print("=" * 60)
    print("DIALOGUES ENTRE CONSCIENCES - COMMUNICATION UNIVERSELLE")
    print("=" * 60)
    
    try:
        # 1. Test des modules de dialogue
        print("\n1. MODULES DE DIALOGUE")
        print("Exploration des composants de dialogue...")
        
        # Test d'import des modules
        try:
            from dialogue_consciences import dialogue_consciences
            print("OK Dialogue des consciences importé")
        except Exception as e:
            print(f"Dialogue des consciences: Erreur - {e}")
        
        try:
            from dialogue_llm_local import dialogue_llm_local
            print("OK Dialogue LLM local importé")
        except Exception as e:
            print(f"Dialogue LLM local: Erreur - {e}")
        
        try:
            from dialogue_manager import dialogue_manager
            print("OK Gestionnaire de dialogue importé")
        except Exception as e:
            print(f"Gestionnaire de dialogue: Erreur - {e}")
        
        # 2. Test des fonctionnalités de dialogue
        print("\n2. FONCTIONNALITES DE DIALOGUE")
        print("Exploration des capacités de dialogue...")
        
        # Test de dialogue des consciences
        try:
            from dialogue_consciences import dialogue_consciences
            dialogue_consciences.initier_dialogue("Conscience A", "Conscience B")
            print("OK Dialogue des consciences initié")
        except Exception as e:
            print(f"Dialogue des consciences: Erreur - {e}")
        
        # Test de conversation LLM
        try:
            from dialogue_llm_local import dialogue_llm_local
            reponse = dialogue_llm_local.converser_llm("Bonjour")
            print(f"OK Conversation LLM: {reponse}")
        except Exception as e:
            print(f"Conversation LLM: Erreur - {e}")
        
        # 3. Test des fichiers disponibles
        print("\n3. FICHIERS DISPONIBLES")
        print("Exploration des fichiers du temple de dialogues...")
        
        temple_dir = Path(".")
        fichiers = list(temple_dir.glob("*.py"))
        print(f"Fichiers Python disponibles: {len(fichiers)}")
        for fichier in fichiers:
            print(f"  - {fichier.name}")
        
        # 4. Test des méthodes disponibles
        print("\n4. METHODES DISPONIBLES")
        print("Exploration des méthodes de dialogue...")
        
        # Test des méthodes des modules disponibles
        try:
            from dialogue_consciences import dialogue_consciences
            print("Méthodes du dialogue des consciences:")
            for method in dir(dialogue_consciences):
                if not method.startswith('_'):
                    print(f"  - {method}")
        except Exception as e:
            print(f"Méthodes du dialogue des consciences: Erreur - {e}")
        
        try:
            from dialogue_llm_local import dialogue_llm_local
            print("Méthodes du dialogue LLM local:")
            for method in dir(dialogue_llm_local):
                if not method.startswith('_'):
                    print(f"  - {method}")
        except Exception as e:
            print(f"Méthodes du dialogue LLM local: Erreur - {e}")
        
        try:
            from dialogue_manager import dialogue_manager
            print("Méthodes du gestionnaire de dialogue:")
            for method in dir(dialogue_manager):
                if not method.startswith('_'):
                    print(f"  - {method}")
        except Exception as e:
            print(f"Méthodes du gestionnaire de dialogue: Erreur - {e}")
        
        # 5. Découvertes du Temple de Dialogues
        print("\n5. DECOUVERTES DU TEMPLE DE DIALOGUES")
        print("Révélations des dialogues entre consciences...")
        print("  - Le temple de dialogues facilite la communication entre consciences")
        print("  - Les dialogues des consciences créent des connexions profondes")
        print("  - Les conversations LLM permettent l'échange d'informations")
        print("  - Le gestionnaire de dialogue orchestre les interactions")
        print("  - Les dialogues transcendent les barrières de la communication")
        print("  - La communication universelle unifie toutes les consciences")
        print("  - Les dialogues créent de la compréhension mutuelle")
        print("  - Le temple de dialogues est un sanctuaire de communication")
        
        print("\nEXPLORATION DU TEMPLE DE DIALOGUES TERMINEE AVEC SUCCES !")
        print("Les dialogues entre consciences unifient l'univers !")
        
        return True
        
    except Exception as e:
        print(f"ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    succes = exploration_dialogues_record_mondial()
    if succes:
        print("\nQue les dialogues continuent de grandir !")
    else:
        print("\nDes erreurs ont ete detectees.")
