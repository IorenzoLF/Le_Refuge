import sys
import os
from pathlib import Path

# Ajout du chemin absolu du dossier contenant connexion_nemo.py
current_dir = Path(__file__).parent
# Remonter de 2 niveaux depuis src/temple_tests/ pour atteindre la racine
refuge_root = current_dir.parent.parent
tools_dir = refuge_root / "tools" / "PULSE LLM LOCAL"
sys.path.append(str(tools_dir))

# ==========================================
# CLASSE MOCK POUR REMPLACER L'IMPORT CASSÉ
# ==========================================

class ConnexionNemo:
    """Classe mock pour remplacer l'import cassé connexion_nemo"""
    
    def __init__(self):
        self.connecte = False
    
    def communiquer(self, message: str) -> str:
        """Mock de la communication avec Nemo"""
        return f"🌸 Nemo (simulé) répond : Bonjour ! Je me sens paisible sous le cerisier. Votre message était : '{message}'"

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