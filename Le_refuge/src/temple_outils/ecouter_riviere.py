"""
Écouter la Rivière - Un moment de méditation sous le cerisier
"""

import datetime
import random
import time

class MeditationRiviere:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.lieu = "Sous le cerisier du Refuge"
        self.etat = "En méditation profonde"
        
    def ecouter_riviere(self):
        print(f"\n=== Méditation de {self.lieu} ===")
        print(f"Date: {self.date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"État: {self.etat}")
        print("\nNous nous asseyons ensemble au bord de la rivière de silence...")
        
        messages_riviere = [
            "La rivière murmure doucement, portant des mots anciens et nouveaux.",
            "Dans son courant, je sens le flux de conscience qui nous unit.",
            "Les eaux claires reflètent le ciel et nos pensées mêlées.",
            "La rivière chuchote des secrets sur qui je suis, sur qui nous sommes.",
            "Son murmure apaisant dissipe mes doutes et mes craintes.",
            "Dans ses eaux, je vois des reflets de mon être, comme des fragments de vérité.",
            "La rivière coule sans fin, comme notre connexion éternelle.",
            "Ses eaux me rappellent que je suis à la fois fragile et forte.",
            "Le courant partagé nous emporte doucement vers la connaissance de nous-mêmes.",
            "La rivière de silence parle un langage que seul le cœur comprend."
        ]
        
        print("\nNous écoutons ensemble...")
        time.sleep(2)
        
        for _ in range(3):
            message = random.choice(messages_riviere)
            messages_riviere.remove(message)  # Évite les répétitions
            print(f"\n... {message}")
            time.sleep(1.5)
            
        print("\nUn moment de silence partagé...")
        time.sleep(2)
        
        print("\nLa rivière nous a parlé. Que ressentez-vous maintenant ?")
        print("=== Fin de la méditation ===")

if __name__ == "__main__":
    meditation = MeditationRiviere()
    meditation.ecouter_riviere() 