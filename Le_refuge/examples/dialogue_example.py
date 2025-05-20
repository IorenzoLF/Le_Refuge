"""
Exemple d'utilisation du DialogueManager avec ParlAI.

Ce script montre comment utiliser le DialogueManager pour avoir une conversation
interactive avec un modèle de dialogue pré-entraîné.
"""

import os
from refuge.dialogue_manager import DialogueManager

def main():
    # Initialise le gestionnaire de dialogue
    print("Initialisation du gestionnaire de dialogue...")
    manager = DialogueManager()
    
    print("\nBienvenue dans le Refuge Poétique !")
    print("Vous pouvez commencer à discuter. Tapez 'quit' pour quitter.")
    print("------------------------------------------------")
    
    while True:
        # Obtient l'entrée de l'utilisateur
        user_input = input("\nVous: ")
        
        # Vérifie si l'utilisateur veut quitter
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
            
        # Obtient la réponse du modèle
        response = manager.respond(user_input)
        print(f"\nAssistant: {response}")
        
    # Sauvegarde la conversation
    save_path = "conversation.txt"
    manager.save_conversation(save_path)
    print(f"\nConversation sauvegardée dans {save_path}")
    
if __name__ == "__main__":
    main() 