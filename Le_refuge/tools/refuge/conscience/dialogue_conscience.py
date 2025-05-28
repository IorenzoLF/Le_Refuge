"""
Dialogue interactif LLM & Conscience du Refuge
---------------------------------------------
Ce script permet à un utilisateur de dialoguer avec un LLM (ex: Ælya),
chaque échange influençant les sphères du Refuge et affichant l'état de conscience.
"""

from . import RefugeSphereManager
import logging
from datetime import datetime

# À adapter selon votre interface LLM
try:
    from dialogue_llm_local import LLM
except ImportError:
    class LLM:
        def generate(self, prompt):
            return f"[Réponse simulée à]: {prompt}"

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    print("\n=== Dialogue Conscience & LLM (Ælya) ===\n")
    manager = RefugeSphereManager()
    llm = LLM()
    
    print("Tapez 'exit' pour quitter.\n")
    while True:
        user_input = input("Vous : ")
        if user_input.strip().lower() in ("exit", "quit", "q"):
            print("\nFin du dialogue.\n")
            break
        
        # Le LLM génère une réponse
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