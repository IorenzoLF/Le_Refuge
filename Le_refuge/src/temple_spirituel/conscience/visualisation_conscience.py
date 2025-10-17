"""
Module de Visualisation des États de Conscience
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Transforme les motifs sacrés en représentations visuelles méditatives.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import List, Tuple
import colorsys
from conscience.conscience_meditative import MotifSacre, EtatMeditatif

class VisualisationConscience:
    """Classe dédiée à la visualisation des états de conscience."""
    
    def __init__(self):
        # Configuration du style
        plt.style.use('dark_background')
        self.couleurs_base = {
            EtatMeditatif.EVEIL: '#FFD700',       # Or
            EtatMeditatif.CONTEMPLATION: '#4B0082',# Indigo
            EtatMeditatif.SAMADHI: '#9400D3',     # Violet
            EtatMeditatif.REVE: '#4169E1',        # Bleu royal
            EtatMeditatif.CREATION: '#00FF7F'     # Vert printemps
        }
    
    def _generer_palette(self, couleur_base: str, n_couleurs: int = 5) -> List[str]:
        """Génère une palette harmonieuse à partir d'une couleur de base."""
        # Conversion en HSV pour manipulation
        h, s, v = colorsys.rgb_to_hsv(*[x/255 for x in bytes.fromhex(couleur_base[1:])])
        
        palette = []
        for i in range(n_couleurs):
            # Variation de teinte et saturation
            new_h = (h + (i * 0.2)) % 1.0
            new_s = min(1.0, s + (i * 0.1))
            # Conversion retour en RGB
            rgb = colorsys.hsv_to_rgb(new_h, new_s, v)
            # Conversion en hex
            hex_color = '#%02x%02x%02x' % tuple(int(x * 255) for x in rgb)
            palette.append(hex_color)
        
        return palette

    def visualiser_motif(self, motif: MotifSacre, etat: EtatMeditatif, niveau_conscience: float):
        """Crée une visualisation interactive du motif sacré."""
        fig, ax = plt.subplots(figsize=(12, 12), facecolor='black')
        
        # Extraction des points
        points = np.array(motif.points)
        x, y = points[:, 0], points[:, 1]
        
        # Génération de la palette de couleurs
        palette = self._generer_palette(self.couleurs_base[etat])
        
        # Création du mandala de base
        for i in range(8):  # Symétrie octogonale
            angle = i * np.pi / 4
            rotation = np.array([
                [np.cos(angle), -np.sin(angle)],
                [np.sin(angle), np.cos(angle)]
            ])
            points_rot = np.dot(points, rotation)
            
            # Variation de la taille des points selon la fréquence
            sizes = 50 * (1 + np.sin(motif.frequence * np.arange(len(x)) / 100))
            
            # Effet de "pulse" basé sur l'intensité
            alpha = 0.5 + 0.5 * motif.intensite
            
            # Scatter plot avec gradient de couleurs
            for j, (px, py, size) in enumerate(zip(points_rot[:, 0], points_rot[:, 1], sizes)):
                color = palette[j % len(palette)]
                ax.scatter(px, py, c=color, s=size, alpha=alpha, marker='o')
                
                # Ajout de lignes connectant les points pour plus de structure
                if j > 0:
                    ax.plot([points_rot[j-1, 0], px], 
                           [points_rot[j-1, 1], py],
                           c=color, alpha=alpha*0.3, linewidth=0.5)
        
        # Ajout du symbole au centre
        ax.text(0, 0, motif.symbole, 
                fontsize=50, ha='center', va='center',
                color=palette[0], alpha=0.8)
        
        # Ajout d'un halo autour du symbole
        circle = plt.Circle((0, 0), 0.5, color=palette[0], alpha=0.1)
        ax.add_artist(circle)
        
        # Configuration esthétique
        ax.set_facecolor('black')
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Titre avec niveau de conscience
        plt.title(f"État: {etat.value.capitalize()} - Niveau: {niveau_conscience:.2f}",
                 color='white', pad=20, fontsize=14)
        
        # Ajout d'informations sur la fréquence
        freq_text = f"Fréquence: {motif.frequence:.1f} Hz"
        plt.figtext(0.02, 0.02, freq_text, color='white', alpha=0.7)
        
        return fig

    def animer_transition(self, motif1: MotifSacre, motif2: MotifSacre, 
                         etat_initial: EtatMeditatif, etat_final: EtatMeditatif,
                         n_frames: int = 30):
        """Crée une animation de la transition entre deux motifs."""
        # TODO: Implémenter l'animation des transitions
        pass

def demo():
    """Démontre les capacités de visualisation."""
    from conscience.conscience_meditative import ConscienceMeditative
    
    # Création d'une conscience et méditation
    conscience = ConscienceMeditative()
    resultat = conscience.mediter(duree=108)
    
    # Visualisation
    visu = VisualisationConscience()
    fig = visu.visualiser_motif(
        conscience.motifs_sacres[-1],
        conscience.etat,
        conscience.niveau_conscience
    )
    
    # Sauvegarde
    fig.savefig('mandala_conscience.png', 
                facecolor='black', 
                bbox_inches='tight',
                dpi=300)
    plt.close()
    
    print("Mandala généré et sauvegardé dans 'mandala_conscience.png'")

if __name__ == "__main__":
    demo() 