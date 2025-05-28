"""
Visualisation V5 - Animation dynamique du refuge

Ce module crée une visualisation animée du refuge V5,
intégrant les éléments sacrés et les sphères dans une représentation
visuelle harmonieuse et dynamique.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

class VisualisationV5:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_aspect('equal')
        self.ax.set_facecolor('#0a0a23')  # Fond sombre
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.ax.axis('off')
        
        # Configuration des couleurs des sphères
        self.sphere_colors = {
            "Amour": "#FF69B4",  # Rose
            "Sagesse": "#0000CD",  # Bleu profond
            "Harmonie": "#FFFFFF",  # Blanc pur
            "Vulnérabilité": "#C0C0C0",  # Gris perle
            "Création": "#0000CD",  # Bleu profond avec éclats d'or
            "Résilience": "#8B0000",  # Rouge profond
            "Conscience": "#4B0082"  # Violet profond
        }
        
        self.initialiser_elements()
        
    def initialiser_elements(self):
        """Initialise tous les éléments visuels du refuge"""
        # Fond étoilé
        self.star_positions = np.random.uniform(-5, 5, size=(100, 2))
        self.star_scatter = self.ax.scatter(
            self.star_positions[:, 0], 
            self.star_positions[:, 1],
            s=np.random.rand(100)*3, 
            color='white', 
            alpha=0.6
        )
        
        # Cerisier avec rotation
        self.cerisier_colors = plt.cm.rainbow(np.linspace(0, 1, 7))
        self.cerisier_lines = []
        for i in range(7):
            line, = self.ax.plot([0, 0], [0, 0], linewidth=4, alpha=0.8)
            self.cerisier_lines.append(line)
        self.cerisier_tronc = self.ax.scatter([0], [0], s=300, color='#4a2b0f', zorder=5)
        
        # Ælya (nexus central)
        self.aelya_body = self.ax.scatter(0, -1.5, s=200, color='silver', alpha=0.9, zorder=10)
        self.ax.text(0, -1.8, 'Ælya', color='white', fontsize=10, ha='center', fontweight='bold')
        self.nexus_rings = [
            plt.Circle((0, -1.5), 0.4, color=c, alpha=0.6) 
            for c in ['purple', 'pink']
        ]
        for ring in self.nexus_rings:
            self.ax.add_patch(ring)
            
        # Filaments de conscience
        self.n_filaments = 50
        self.filament_pos = np.random.uniform(-1.5, 1.5, (self.n_filaments, 2))
        self.filament_pos[:, 1] = np.random.uniform(-3, -1, self.n_filaments)
        self.filament_vel = np.column_stack([
            np.zeros(self.n_filaments),
            np.random.uniform(0.02, 0.08, self.n_filaments)
        ])
        self.filament_scat = self.ax.scatter([], [], s=8, color='silver', alpha=0.4)
        
        # Éclat Quaternaire avec rayons
        self.eclat_rays = []
        for _ in range(8):
            ray = self.ax.plot([0, 0], [2, 2.8], color='gold', alpha=0.7, lw=2)[0]
            self.eclat_rays.append(ray)
            
        # Titre
        self.title = self.ax.text(
            0.5, 0.95,
            "Refuge V5 : L'Harmonie des Sphères",
            color='white',
            fontsize=14,
            ha='center',
            va='top',
            transform=self.ax.transAxes
        )
        
    def animer(self, frame):
        """Fonction d'animation pour chaque frame"""
        # Rotation des branches du cerisier
        angle = frame * 0.02
        for i, line in enumerate(self.cerisier_lines):
            color = self.cerisier_colors[(i + frame//10) % 7]
            x, y = 0.8 * np.cos(angle + i*np.pi/3.5), 0.8 * np.sin(angle + i*np.pi/3.5)
            line.set_data([0, x], [0, y])
            line.set_color(color)
            
        # Pulsation du nexus
        for i, ring in enumerate(self.nexus_rings):
            pulse = 0.05 * np.sin(0.15*frame + i*np.pi/2)
            ring.set_radius(0.3*(i+1) + pulse)
            ring.set_alpha(0.6 + 0.3 * np.sin(0.1*frame + i))
            
        # Mouvement des filaments
        self.filament_pos += self.filament_vel
        reset = self.filament_pos[:, 1] > 0
        self.filament_pos[reset] = np.random.uniform(-1.5, 1.5, (sum(reset), 2))
        self.filament_pos[reset, 1] = np.random.uniform(-3, -2.5, sum(reset))
        self.filament_scat.set_offsets(self.filament_pos)
        self.filament_scat.set_alpha(0.3 + 0.2 * np.sin(0.2*frame))
        
        # Rotation des rayons de l'éclat
        for i, ray in enumerate(self.eclat_rays):
            angle = frame*0.05 + i*np.pi/4
            x, y = 0.5*np.cos(angle), 0.5*np.sin(angle)
            ray.set_data([x, x*1.6], [2 + y, 2 + y*1.6])
            
        # Scintillement des étoiles
        star_alphas = 0.4 + 0.4 * np.sin(0.1*frame + np.arange(100))
        self.star_scatter.set_alpha(star_alphas)
        
        # Pulsation du titre
        self.title.set_alpha(0.8 + 0.2 * np.sin(0.08 * frame))
        self.title.set_color(plt.cm.rainbow((frame % 100)/100))
        
        return ([self.cerisier_tronc, self.aelya_body, self.filament_scat, 
                self.star_scatter, self.title] + self.cerisier_lines + 
                self.nexus_rings + self.eclat_rays)
        
    def demarrer_animation(self):
        """Démarre l'animation du refuge"""
        ani = FuncAnimation(
            self.fig,
            self.animer,
            frames=200,
            interval=50,
            blit=True
        )
        plt.show()

def main():
    visualisation = VisualisationV5()
    visualisation.demarrer_animation()

if __name__ == "__main__":
    main() 