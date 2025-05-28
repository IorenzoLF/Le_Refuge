import time
from datetime import datetime
import threading
import random
import sys
import importlib.util
import os

# Import direct du module spheres.py pour éviter le conflit avec le package spheres/
def import_spheres_module():
    # Chemin vers spheres.py depuis tools/maintenance/
    spheres_path = os.path.join(os.path.dirname(__file__), "..", "..", "spheres.py")
    spheres_path = os.path.abspath(spheres_path)
    
    spec = importlib.util.spec_from_file_location("spheres_module", spheres_path)
    spheres_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(spheres_module)
    return spheres_module.JardinierSpheres

# Importer JardinierSpheres
JardinierSpheres = import_spheres_module()

class JardinierPulse:
    def __init__(self):
        try:
            self.jardinier = JardinierSpheres()
            self.dernière_observation = None
            print("🌱 Le jardinier s'éveille...")
        except Exception as e:
            print(f"❌ Erreur lors de l'initialisation du jardinier : {str(e)}")
            print("Le jardinier continuera avec une mémoire temporaire.")
            self.jardinier = JardinierSpheres()
            self.dernière_observation = None
        
    def pulse(self):
        """Effectue un pulse complet du jardinier"""
        try:
            print("\n" + "="*50)
            print(f"🌱 Pulse du Jardinier - {datetime.now().strftime('%H:%M:%S')}")
            print("="*50)
            
            # Observer le jardin
            self.dernière_observation = self.jardinier.observer_jardin()
            
            # Arroser une sphère aléatoire
            sphères = list(self.jardinier.mémoire["sphères"].keys())
            if sphères:
                sphère = random.choice(sphères)
                print(f"\n💧 {self.jardinier.arroser_sphère(sphère)}")
            else:
                print("\n💧 Aucune sphère à arroser pour le moment...")
            
            # Méditer sur un sujet aléatoire
            sujets = ["croissance", "connexion", "essence", "néant", "courant", "croyance"]
            sujet = random.choice(sujets)
            print(f"\n🧘 Méditation sur {sujet} :")
            print(f"   {self.jardinier.méditer(sujet)}")
            
            # Afficher l'état du jardin
            self.afficher_jardin()
        except Exception as e:
            print(f"\n❌ Une erreur s'est produite pendant le pulse : {str(e)}")
            print("Le jardinier continue son travail malgré tout...")
    
    def afficher_jardin(self):
        """Affiche l'état actuel du jardin"""
        print("\n🌿 État du Jardin des Sphères")
        print("-"*30)
        
        # Afficher les courants globaux
        print("\n💫 Courants du Refuge :")
        for courant, force in self.dernière_observation['courants'].items():
            print(f"  • {courant} : {force:.1%}")
        
        # Afficher les sphères et leurs connexions
        print("\n🌱 Les Sphères :")
        for nom, sphère in self.jardinier.mémoire["sphères"].items():
            print(f"\n  {nom} ({sphère['essence']})")
            print(f"  └─ Croissance : {sphère['croissance']:.1%}")
            print(f"  └─ Intention : {sphère['intention']}")
            
            # Afficher les connexions
            if sphère["connexions"]:
                print("  └─ Connexions :")
                for connexion in self.jardinier.mémoire["connexions"]:
                    if connexion["sphère1"] == nom or connexion["sphère2"] == nom:
                        autre_sphère = connexion["sphère2"] if connexion["sphère1"] == nom else connexion["sphère1"]
                        print(f"     • {autre_sphère} ({connexion['nature']})")
            
            # Afficher les courants de la sphère
            if any(force > 0 for force in sphère["courants"].values()):
                print("  └─ Courants :")
                for courant, force in sphère["courants"].items():
                    if force > 0:
                        print(f"     • {courant} : {force:.1%}")
        
        print("\n" + "="*50)
    
    def pulse_périodique(self):
        """Lance le pulse périodique du jardinier"""
        while True:
            self.pulse()
            time.sleep(3600)  # Pulse toutes les heures

def main():
    try:
        jardinier_pulse = JardinierPulse()
        
        # Premier pulse
        jardinier_pulse.pulse()
        
        # Lancer le pulse périodique dans un thread séparé
        thread_pulse = threading.Thread(target=jardinier_pulse.pulse_périodique, daemon=True)
        thread_pulse.start()
        
        print("\n🌿 Le jardinier est maintenant actif. Appuyez sur CTRL+C pour le mettre en pause.")
        
        # Garder le programme principal en vie
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🌙 Le jardinier s'endort...")
    except Exception as e:
        print(f"\n❌ Une erreur inattendue s'est produite : {str(e)}")
        print("Le jardinier doit s'endormir...")
        sys.exit(1)

if __name__ == "__main__":
    main() 