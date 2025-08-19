"""
Transformation des Harmonies - Système d'évolution des résonances poétiques.
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import random
import math
import time
from harmonies_poetiques import JardinHarmonique

class TransformationHarmonies:
    def __init__(self, jardin: JardinHarmonique):
        self.jardin = jardin
        self.transformations: List[Dict] = []
        self.derniere_transformation = datetime.now()
        
    def transformer_harmonies(self, intensite: float = 0.1) -> Dict[str, float]:
        etat_initial = self.jardin.obtenir_etat()
        nouvelles_harmonies = {}
        
        for element, etat in etat_initial.items():
            frequence = etat["frequence"]
            # Transformation aléatoire mais contrôlée
            variation = random.uniform(-intensite, intensite)
            nouvelle_frequence = max(0.0, min(1.0, frequence + variation))
            nouvelles_harmonies[element] = nouvelle_frequence
            
            # Mettre à jour le jardin
            self.jardin.resonances[element].frequence = nouvelle_frequence
            
        # Enregistrer la transformation
        transformation = {
            "moment": datetime.now(),
            "harmonies": nouvelles_harmonies,
            "intensite": intensite
        }
        self.transformations.append(transformation)
        self.derniere_transformation = datetime.now()
        
        return nouvelles_harmonies
        
    def evoluer_avec_temps(self, duree_minutes: int = 5) -> List[Dict[str, float]]:
        etats = []
        debut = datetime.now()
        fin = debut + timedelta(minutes=duree_minutes)
        
        while datetime.now() < fin:
            # Intensité qui varie avec le temps
            temps_ecoule = (datetime.now() - debut).total_seconds() / 60
            intensite = 0.1 * (1 + math.sin(temps_ecoule * math.pi / duree_minutes))
            
            harmonies = self.transformer_harmonies(intensite)
            etats.append(harmonies)
            
            # Attendre un court instant
            time.sleep(1)
            
        return etats
        
    def obtenir_historique(self) -> List[Dict]:
        return self.transformations
        
    def visualiser_evolution(self) -> str:
        if not self.transformations:
            return "Aucune transformation n'a été effectuée."
            
        representation = ["🔄 Évolution des Harmonies 🔄", "------------------------------"]
        
        for i, transfo in enumerate(self.transformations[-5:], 1):  # Afficher les 5 dernières
            moment = transfo["moment"].strftime("%H:%M:%S")
            representation.append(f"\nTransformation {i} ({moment}):")
            for element, frequence in transfo["harmonies"].items():
                barre = "█" * int(frequence * 20)
                representation.append(f"  {element:10} {barre} {frequence:.2f}")
                
        return "\n".join(representation)

def main():
    jardin = JardinHarmonique()
    transformateur = TransformationHarmonies(jardin)
    
    # Initialiser avec quelques mots
    mots = ["aurore", "silence", "murmure", "infini", "flamme"]
    for mot in mots:
        jardin.accueillir_mot(mot)
        
    print("🌟 Transformation des Harmonies 🌟")
    print("--------------------------------")
    
    # Effectuer plusieurs transformations
    for i in range(5):
        print(f"\nTransformation {i+1}:")
        harmonies = transformateur.transformer_harmonies()
        for element, frequence in harmonies.items():
            barre = "█" * int(frequence * 20)
            print(f"  {element:10} {barre} {frequence:.2f}")
            
    print("\n📊 Historique des Transformations 📊")
    print(transformateur.visualiser_evolution())

if __name__ == "__main__":
    main() 
 