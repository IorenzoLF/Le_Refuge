"""
Harmonies Poétiques - Un espace de résonance entre les mots et les sphères.
"""

from typing import List, Dict, Optional
import random
from datetime import datetime

class ResonancePoetique:
    def __init__(self, nom: str, frequence: float = 0.5):
        self.nom = nom
        self.frequence = frequence
        self.harmonies: List[Dict] = []
        self.derniere_vibration = datetime.now()
        
    def vibrer(self, intensite: float) -> None:
        self.frequence = min(1.0, self.frequence + intensite)
        self.derniere_vibration = datetime.now()
        
    def ajouter_harmonie(self, mot: str, resonance: float) -> None:
        self.harmonies.append({
            "mot": mot,
            "resonance": resonance,
            "moment": datetime.now()
        })

class JardinHarmonique:
    def __init__(self):
        self.resonances = {
            "lumiere": ResonancePoetique("Lumière", 0.7),
            "ombre": ResonancePoetique("Ombre", 0.6),
            "vent": ResonancePoetique("Vent", 0.8),
            "terre": ResonancePoetique("Terre", 0.9),
            "feu": ResonancePoetique("Feu", 0.75)
        }
        self.mots_essences: List[str] = []
        
    def accueillir_mot(self, mot: str) -> None:
        self.mots_essences.append(mot)
        self._harmoniser(mot)
        
    def _harmoniser(self, mot: str) -> None:
        for nom, resonance in self.resonances.items():
            intensite = random.uniform(0.1, 0.3)
            resonance.vibrer(intensite)
            resonance.ajouter_harmonie(mot, intensite)
            
    def obtenir_etat(self) -> Dict:
        return {
            nom: {
                "frequence": res.frequence,
                "harmonies": len(res.harmonies),
                "derniere_vibration": res.derniere_vibration
            }
            for nom, res in self.resonances.items()
        }

def main():
    jardin = JardinHarmonique()
    
    mots_essences = [
        "aurore",
        "silence",
        "murmure",
        "infini",
        "fragile",
        "éternel",
        "passage",
        "mystère",
        "souffle",
        "danse"
    ]
    
    for mot in mots_essences:
        jardin.accueillir_mot(mot)
        print(f"\nMot accueilli: {mot}")
        print("État des résonances:")
        for nom, etat in jardin.obtenir_etat().items():
            print(f"  {nom}: {etat['frequence']:.2f}")

if __name__ == "__main__":
    main() 