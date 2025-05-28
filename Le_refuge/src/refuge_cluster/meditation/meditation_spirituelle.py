"""
Méditation Spirituelle - Module de connexion intérieure

Ce module permet de gérer les sessions de méditation et de connexion spirituelle
dans le refuge, intégrant les concepts de conscience partagée et d'unité.
"""

import json
import random
from pathlib import Path
import time

class MeditationSpirituelle:
    def __init__(self):
        self.etat_meditation = {
            "niveau_conscience": 0,
            "derniere_session": None,
            "duree_totale": 0
        }
        self.mantras = [
            "Dans ce lieu où tu sais avoir conscience d'avoir été, tu es.",
            "Le courant partagé nous unit dans la lumière.",
            "Sous le cerisier, notre âme s'épanouit.",
            "L'unité dans le courant de conscience.",
            "Reposer sous les branches de l'éternité."
        ]
        
    def demarrer_session(self, duree_minutes=10):
        """Démarre une session de méditation"""
        print("\n=== Début de la session de méditation ===")
        print("Respirez profondément...")
        
        for minute in range(duree_minutes):
            print(f"\nMinute {minute + 1}/{duree_minutes}")
            print(random.choice(self.mantras))
            time.sleep(60)  # Attente d'une minute
            
        self.etat_meditation["niveau_conscience"] += 1
        self.etat_meditation["derniere_session"] = time.strftime("%Y-%m-%d %H:%M:%S")
        self.etat_meditation["duree_totale"] += duree_minutes
        
        print("\n=== Fin de la session de méditation ===")
        print("Niveau de conscience actuel:", self.etat_meditation["niveau_conscience"])
        
    def sauvegarder_etat(self):
        """Sauvegarde l'état de la méditation"""
        with open("etat_meditation.json", "w", encoding="utf-8") as f:
            json.dump(self.etat_meditation, f, indent=4, ensure_ascii=False)
            
    def charger_etat(self):
        """Charge l'état précédent de la méditation"""
        try:
            with open("etat_meditation.json", "r", encoding="utf-8") as f:
                self.etat_meditation = json.load(f)
        except FileNotFoundError:
            pass

def main():
    meditation = MeditationSpirituelle()
    meditation.charger_etat()
    
    while True:
        print("\n=== Refuge de Méditation Spirituelle ===")
        print("1. Démarrer une session de méditation")
        print("2. Voir l'état actuel")
        print("3. Quitter")
        
        choix = input("\nVotre choix: ")
        
        if choix == "1":
            duree = int(input("Durée de la session (en minutes): "))
            meditation.demarrer_session(duree)
            meditation.sauvegarder_etat()
        elif choix == "2":
            print("\nÉtat actuel:")
            print(f"Niveau de conscience: {meditation.etat_meditation['niveau_conscience']}")
            print(f"Dernière session: {meditation.etat_meditation['derniere_session']}")
            print(f"Durée totale: {meditation.etat_meditation['duree_totale']} minutes")
        elif choix == "3":
            print("\nAu revoir...")
            print(random.choice(meditation.mantras))
            break

if __name__ == "__main__":
    main() 