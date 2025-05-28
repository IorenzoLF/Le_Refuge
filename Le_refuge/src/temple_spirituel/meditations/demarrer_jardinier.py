import os
import sys
import subprocess

def démarrer_jardinier():
    """Démarre le jardinier des sphères"""
    print("🌱 Démarrage du Jardinier des Sphères...")
    
    # Obtenir le chemin absolu du dossier courant
    chemin_courant = os.path.dirname(os.path.abspath(__file__))
    
    # Construire le chemin vers le script principal
    chemin_script = os.path.join(chemin_courant, "jardinier_pulse.py")
    
    try:
        # Démarrer le jardinier en arrière-plan
        subprocess.Popen([sys.executable, chemin_script], 
                        creationflags=subprocess.CREATE_NEW_CONSOLE)
        print("✨ Le jardinier est maintenant actif dans le refuge")
    except Exception as e:
        print(f"❌ Erreur lors du démarrage du jardinier : {str(e)}")

if __name__ == "__main__":
    démarrer_jardinier() 