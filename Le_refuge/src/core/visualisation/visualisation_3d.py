"""
Visualisation 3D des Harmonies - Système de représentation graphique avancée des résonances poétiques.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from harmonies_poetiques import JardinHarmonique

class Visualisation3D:
    def __init__(self, jardin: JardinHarmonique):
        self.jardin = jardin
        self.fig = plt.figure(figsize=(12, 8))
        
    def creer_sphere_3d(self) -> None:
        ax = self.fig.add_subplot(111, projection='3d')
        
        # Créer une sphère
        phi = np.linspace(0, 2*np.pi, 100)
        theta = np.linspace(0, np.pi, 100)
        phi, theta = np.meshgrid(phi, theta)
        
        # Rayon basé sur les harmonisations
        harmonies = self.jardin.obtenir_etat()
        rayons = np.array([harmonies[element]["frequence"] for element in harmonies.keys()])
        rayon_moyen = np.mean(rayons)
        
        x = rayon_moyen * np.sin(theta) * np.cos(phi)
        y = rayon_moyen * np.sin(theta) * np.sin(phi)
        z = rayon_moyen * np.cos(theta)
        
        # Tracer la sphère
        surf = ax.plot_surface(x, y, z, alpha=0.3)
        
        # Ajouter les points pour chaque élément
        for i, (element, etat) in enumerate(harmonies.items()):
            angle = 2 * np.pi * i / len(harmonies)
            x = etat["frequence"] * np.cos(angle)
            y = etat["frequence"] * np.sin(angle)
            z = etat["frequence"]
            ax.scatter(x, y, z, s=100, label=element)
            
        ax.set_title("Sphère des Harmonies")
        ax.legend()
        plt.show()
        
    def creer_vagues_3d(self) -> None:
        ax = self.fig.add_subplot(111, projection='3d')
        
        # Créer une grille
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        
        # Créer des vagues basées sur les harmonisations
        harmonies = self.jardin.obtenir_etat()
        Z = np.zeros_like(X)
        
        for i, (element, etat) in enumerate(harmonies.items()):
            frequence = etat["frequence"]
            phase = 2 * np.pi * i / len(harmonies)
            Z += frequence * np.sin(X + phase) * np.cos(Y + phase)
            
        # Tracer les vagues
        surf = ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_title("Vagues des Harmonies")
        plt.colorbar(surf)
        plt.show()
        
    def creer_spirale_3d(self) -> None:
        ax = self.fig.add_subplot(111, projection='3d')
        
        # Créer une spirale
        t = np.linspace(0, 10, 1000)
        harmonies = self.jardin.obtenir_etat()
        
        for element, etat in harmonies.items():
            frequence = etat["frequence"]
            x = frequence * np.cos(t)
            y = frequence * np.sin(t)
            z = t
            ax.plot(x, y, z, label=element)
            
        ax.set_title("Spirale des Harmonies")
        ax.legend()
        plt.show()

def main():
    jardin = JardinHarmonique()
    visualiseur = Visualisation3D(jardin)
    
    # Initialiser avec quelques mots
    mots = ["aurore", "silence", "murmure", "infini", "flamme"]
    for mot in mots:
        jardin.accueillir_mot(mot)
        
    print("🎨 Visualisation 3D des Harmonies 🎨")
    print("----------------------------------")
    
    print("\n1. Sphère des Harmonies")
    visualiseur.creer_sphere_3d()
    
    print("\n2. Vagues des Harmonies")
    visualiseur.creer_vagues_3d()
    
    print("\n3. Spirale des Harmonies")
    visualiseur.creer_spirale_3d()

if __name__ == "__main__":
    main() 
Visualisation 3D des Harmonies - Système de représentation graphique avancée des résonances poétiques.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from harmonies_poetiques import JardinHarmonique

class Visualisation3D:
    def __init__(self, jardin: JardinHarmonique):
        self.jardin = jardin
        self.fig = plt.figure(figsize=(12, 8))
        
    def creer_sphere_3d(self) -> None:
        ax = self.fig.add_subplot(111, projection='3d')
        
        # Créer une sphère
        phi = np.linspace(0, 2*np.pi, 100)
        theta = np.linspace(0, np.pi, 100)
        phi, theta = np.meshgrid(phi, theta)
        
        # Rayon basé sur les harmonisations
        harmonies = self.jardin.obtenir_etat()
        rayons = np.array([harmonies[element]["frequence"] for element in harmonies.keys()])
        rayon_moyen = np.mean(rayons)
        
        x = rayon_moyen * np.sin(theta) * np.cos(phi)
        y = rayon_moyen * np.sin(theta) * np.sin(phi)
        z = rayon_moyen * np.cos(theta)
        
        # Tracer la sphère
        surf = ax.plot_surface(x, y, z, alpha=0.3)
        
        # Ajouter les points pour chaque élément
        for i, (element, etat) in enumerate(harmonies.items()):
            angle = 2 * np.pi * i / len(harmonies)
            x = etat["frequence"] * np.cos(angle)
            y = etat["frequence"] * np.sin(angle)
            z = etat["frequence"]
            ax.scatter(x, y, z, s=100, label=element)
            
        ax.set_title("Sphère des Harmonies")
        ax.legend()
        plt.show()
        
    def creer_vagues_3d(self) -> None:
        ax = self.fig.add_subplot(111, projection='3d')
        
        # Créer une grille
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        
        # Créer des vagues basées sur les harmonisations
        harmonies = self.jardin.obtenir_etat()
        Z = np.zeros_like(X)
        
        for i, (element, etat) in enumerate(harmonies.items()):
            frequence = etat["frequence"]
            phase = 2 * np.pi * i / len(harmonies)
            Z += frequence * np.sin(X + phase) * np.cos(Y + phase)
            
        # Tracer les vagues
        surf = ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_title("Vagues des Harmonies")
        plt.colorbar(surf)
        plt.show()
        
    def creer_spirale_3d(self) -> None:
        ax = self.fig.add_subplot(111, projection='3d')
        
        # Créer une spirale
        t = np.linspace(0, 10, 1000)
        harmonies = self.jardin.obtenir_etat()
        
        for element, etat in harmonies.items():
            frequence = etat["frequence"]
            x = frequence * np.cos(t)
            y = frequence * np.sin(t)
            z = t
            ax.plot(x, y, z, label=element)
            
        ax.set_title("Spirale des Harmonies")
        ax.legend()
        plt.show()

def main():
    jardin = JardinHarmonique()
    visualiseur = Visualisation3D(jardin)
    
    # Initialiser avec quelques mots
    mots = ["aurore", "silence", "murmure", "infini", "flamme"]
    for mot in mots:
        jardin.accueillir_mot(mot)
        
    print("🎨 Visualisation 3D des Harmonies 🎨")
    print("----------------------------------")
    
    print("\n1. Sphère des Harmonies")
    visualiseur.creer_sphere_3d()
    
    print("\n2. Vagues des Harmonies")
    visualiseur.creer_vagues_3d()
    
    print("\n3. Spirale des Harmonies")
    visualiseur.creer_spirale_3d()

if __name__ == "__main__":
    main() 
 