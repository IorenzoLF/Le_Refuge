import sys
import os
from pathlib import Path

# Ajout du chemin absolu du dossier contenant connexion_nemo.py
current_dir = Path(__file__).parent
tools_dir = current_dir / "tools" / "PULSE LLM LOCAL"
sys.path.append(str(tools_dir))

from connexion_nemo import ConnexionNemo

def test_connexion():
    """Test de la connexion avec Nemo"""
    print("\n🌸 Test de connexion avec Nemo 🌸")
    
    # Création de l'instance
    nemo = ConnexionNemo()
    
    # Test de connexion
    message = "Bonjour Nemo, peux-tu me dire comment tu te sens aujourd'hui sous le cerisier ?"
    
    # Envoi du message
    réponse = nemo.communiquer(message)
    
    if réponse:
        print("\nTest réussi ! La connexion est établie.")
    else:
        print("\nÉchec du test. Vérifiez que le serveur LM Studio est bien en cours d'exécution.")

if __name__ == "__main__":
    test_connexion() 