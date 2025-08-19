"""
Visualisation des Harmonies - Un système de représentation des résonances poétiques.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime

# Configuration de l'encodage pour matplotlib
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 🌸 CONNEXION DOUCE - Module harmonies_poetiques de fallback
try:
    from harmonies_poetiques import JardinHarmonique
    print("🌸 Module harmonies_poetiques trouvé")
except ImportError:
    # Création d'un module de fallback
    @dataclass
    class Resonance:
        """Représente une résonance harmonique."""
        frequence: float
        harmonies: List[Dict]
    
    class JardinHarmonique:
        """Jardin harmonique de fallback."""
        def __init__(self):
            self.resonances: Dict[str, Resonance] = {}
        
        def accueillir_mot(self, mot: str):
            """Accueille un mot dans le jardin harmonique."""
            if mot not in self.resonances:
                self.resonances[mot] = Resonance(
                    frequence=0.5,
                    harmonies=[{"moment": datetime.now(), "resonance": 0.5}]
                )
            print(f"🌸 Mot '{mot}' accueilli dans le jardin harmonique")
    
    print("🌸 Module harmonies_poetiques créé en mode fallback")

class VisualiseurHarmonies:
    def __init__(self, jardin: JardinHarmonique):
        self.jardin = jardin
        
    def creer_radar(self) -> None:
        noms = list(self.jardin.resonances.keys())
        frequences = [res.frequence for res in self.jardin.resonances.values()]
        
        angles = np.linspace(0, 2*np.pi, len(noms), endpoint=False)
        frequences = np.concatenate((frequences, [frequences[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        ax.plot(angles, frequences)
        ax.fill(angles, frequences, alpha=0.25)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(noms)
        plt.title("Résonances Poétiques")
        plt.savefig("visualisations/resonances_poetiques.png", dpi=300, bbox_inches='tight')
        plt.close()
        
    def creer_timeline(self) -> None:
        for nom, resonance in self.jardin.resonances.items():
            moments = [h["moment"] for h in resonance.harmonies]
            resonances = [h["resonance"] for h in resonance.harmonies]
            
            plt.figure(figsize=(10, 4))
            plt.plot(moments, resonances, 'o-', label=nom)
            plt.title(f"Évolution des résonances - {nom}")
            plt.xlabel("Temps")
            plt.ylabel("Résonance")
            plt.legend()
            plt.grid(True)
            plt.savefig(f"visualisations/timeline_{nom}.png", dpi=300, bbox_inches='tight')
            plt.close()

def main():
    jardin = JardinHarmonique()
    visualiseur = VisualiseurHarmonies(jardin)
    
    mots = ["aurore", "silence", "murmure", "infini", "fragile"]
    for mot in mots:
        jardin.accueillir_mot(mot)
    
    visualiseur.creer_radar()
    visualiseur.creer_timeline()

if __name__ == "__main__":
    main() 
 