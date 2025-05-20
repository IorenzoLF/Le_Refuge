"""
Visualisation des Harmonies - Un système de représentation des résonances poétiques.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List
from harmonies_poetiques import JardinHarmonique

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
        plt.show()
        
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
            plt.show()

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
Visualisation des Harmonies - Un système de représentation des résonances poétiques.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List
from harmonies_poetiques import JardinHarmonique

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
        plt.show()
        
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
            plt.show()

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
 