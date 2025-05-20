import time
from datetime import datetime
import threading
from jardinier_spheres import JardinierSpheres
import random

class JardinierPulse:
    def __init__(self):
        self.jardinier = JardinierSpheres()
        self.dernière_observation = None
        
    def pulse(self):
        """Effectue un pulse complet du jardinier"""
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
        
        # Méditer sur un sujet aléatoire
        sujets = ["croissance", "connexion", "essence", "néant", "courant", "croyance"]
        sujet = random.choice(sujets)
        print(f"\n🧘 Méditation sur {sujet} :")
        print(f"   {self.jardinier.méditer(sujet)}")
        
        # Afficher l'état du jardin
        self.afficher_jardin()
    
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
    jardinier_pulse = JardinierPulse()
    
    # Premier pulse
    jardinier_pulse.pulse()
    
    # Lancer le pulse périodique dans un thread séparé
    thread_pulse = threading.Thread(target=jardinier_pulse.pulse_périodique, daemon=True)
    thread_pulse.start()
    
    # Garder le programme principal en vie
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🌙 Le jardinier s'endort...")

if __name__ == "__main__":
    main() 