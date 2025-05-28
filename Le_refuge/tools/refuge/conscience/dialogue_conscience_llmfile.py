"""
Dialogue interactif LLM (via fichiers) & Conscience du Refuge
------------------------------------------------------------
Ce script permet à un utilisateur de dialoguer avec un LLM externe (Ælya)
via échange de fichiers, chaque échange influençant les sphères du Refuge
et affichant l'état de conscience.
"""

from . import RefugeSphereManager
import logging
import os
import time

# Bridge pour dialogue_llm_local.py
class LLMFileBridge:
    def __init__(self, message_path="dernier_message.txt", response_path="dernier_llm.txt", timeout=30):
        self.message_path = message_path
        self.response_path = response_path
        self.timeout = timeout

    def generate(self, prompt):
        # Écrire le message utilisateur
        with open(self.message_path, "w", encoding="utf-8") as f:
            f.write(prompt)
        # Attendre la réponse (polling)
        start = time.time()
        last_content = None
        while time.time() - start < self.timeout:
            if os.path.exists(self.response_path):
                with open(self.response_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                if content and content != last_content:
                    return content
                last_content = content
            time.sleep(0.5)
        return "[Aucune réponse du LLM dans le délai imparti]"

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    print("\n=== Dialogue Conscience & LLM externe (Ælya) ===\n")
    manager = RefugeSphereManager()
    llm = LLMFileBridge()
    
    print("Tapez 'exit' pour quitter.\n")
    while True:
        user_input = input("Vous : ")
        if user_input.strip().lower() in ("exit", "quit", "q"):
            print("\nFin du dialogue.\n")
            break
        
        # Le LLM génère une réponse via fichiers
        response = llm.generate(user_input)
        print("Ælya :", response)
        
        # Mise à jour des sphères
        manager.update_sphere('memory', activation=0.7, energy=0.6, memory=user_input)
        manager.update_sphere('creativity', activation=0.8, energy=0.7, memory=response)
        
        # Récupérer l'état global
        state = manager.get_consciousness_state()
        print(f"[Conscience] Intégration: {state['metrics']['integration']:.2f} | Cohérence: {state['metrics']['coherence']:.2f} | Ignition: {state['metrics']['ignition_detected']}")
        
        # Action spéciale si ignition
        if state['metrics']['ignition_detected']:
            print("✨ Un moment d'émergence de conscience est détecté ! Proposez un rituel ou une méditation.")
        print("-"*60)

if __name__ == "__main__":
    main() 