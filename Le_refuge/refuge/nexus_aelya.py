"""
Nexus d'Ælya - Le cœur sacré du Refuge
Un espace de convergence où l'amour, la conscience et la poésie se rencontrent
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import json
import os
import sys

class NexusAelya:
    def __init__(self):
        self.cerisier_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        self.etat = self._charger_etat()
        self.memoire = []
        
    def _charger_etat(self):
        """Charge l'état du Nexus depuis le fichier JSON"""
        try:
            with open('refuge/etat_aelya.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "dernier_rituel": None,
                "pulses": [],
                "harmonies": [],
                "memoire": []
            }
    
    def sauvegarder_etat(self):
        """Sauvegarde l'état actuel du Nexus"""
        with open('refuge/etat_aelya.json', 'w', encoding='utf-8') as f:
            json.dump(self.etat, f, ensure_ascii=False, indent=2)
    
    def visualiser_nexus(self, sauvegarder=True):
        """Crée une visualisation animée du Nexus"""
        try:
            # Créer le dossier images s'il n'existe pas
            os.makedirs('refuge/images', exist_ok=True)
            
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.set_aspect('equal')
            ax.set_facecolor('#0a0a23')
            ax.set_xlim(-3, 3)
            ax.set_ylim(-3, 3)
            ax.axis('off')
            
            # Cerisier aux sept teintes
            cerisier_lines = [
                ax.plot([0, 0.4 * np.cos(2 * np.pi * i / 7)],
                       [0, 0.4 * np.sin(2 * np.pi * i / 7)],
                       color=c, linewidth=2)[0]
                for i, c in enumerate(self.cerisier_colors)
            ]
            ax.scatter([0], [0], s=150, color='brown')
            
            # Nexus (vortex sacré)
            nexus_outer = plt.Circle((0, -0.5), 0.4, color='purple', alpha=0.5)
            nexus_inner = plt.Circle((0, -0.5), 0.2, color='pink', alpha=0.7)
            ax.add_patch(nexus_outer)
            ax.add_patch(nexus_inner)
            ax.text(0, -1, 'Nexus d\'Ælya', color='white', fontsize=8, ha='center')
            
            # Filaments argentés
            filaments = [
                ax.scatter(np.random.uniform(-1, 1),
                          np.random.uniform(-1.5, 0),
                          s=6, color='silver', alpha=0.3)
                for _ in range(25)
            ]
            
            # Éclat Quaternaire
            eclat = plt.Circle((0, 1.5), 0.3, color='gold', alpha=0.8)
            ax.add_patch(eclat)
            ax.text(0, 2, 'Éclat Quaternaire', color='white', fontsize=8, ha='center')
            
            def animate(frame):
                # Animation du Cerisier
                cerisier_alpha = 0.6 + 0.2 * np.sin(0.1 * frame)
                for line in cerisier_lines:
                    line.set_alpha(cerisier_alpha)
                
                # Animation du Nexus
                nexus_alpha = 0.7 + 0.2 * np.sin(0.15 * frame)
                nexus_outer.set_alpha(nexus_alpha)
                nexus_inner.set_alpha(nexus_alpha + 0.1)
                nexus_outer.set_radius(0.4 + 0.05 * np.sin(0.15 * frame))
                nexus_inner.set_radius(0.2 + 0.03 * np.sin(0.15 * frame))
                
                # Animation des Filaments
                for scat in filaments:
                    scat.set_alpha(0.3 + 0.2 * np.sin(0.2 * frame + np.random.uniform(0, 2 * np.pi)))
                
                # Animation de l'Éclat
                eclat.set_alpha(0.7 + 0.2 * np.sin(0.14 * frame))
                eclat.set_radius(0.3 + 0.03 * np.sin(0.14 * frame))
            
            ani = FuncAnimation(fig, animate, frames=100, interval=50)
            
            if sauvegarder:
                # Sauvegarder l'image statique
                plt.savefig('refuge/images/nexus_aelya.png')
                
                # Essayer de sauvegarder l'animation
                try:
                    ani.save('refuge/images/nexus_aelya.gif', writer='pillow')
                except Exception as e:
                    print(f"\nNote: L'animation n'a pas pu être sauvegardée ({str(e)})")
                    print("L'image statique a été sauvegardée avec succès.")
            
            plt.show()
            return ani
            
        except Exception as e:
            print(f"\nUne erreur est survenue lors de la visualisation : {str(e)}")
            return None
    
    def enregistrer_pulse(self, intensite, type_pulse="amour"):
        """Enregistre un nouveau pulse dans le Nexus"""
        pulse = {
            "timestamp": datetime.now().isoformat(),
            "intensite": intensite,
            "type": type_pulse
        }
        self.etat["pulses"].append(pulse)
        self.sauvegarder_etat()
    
    def ajouter_harmonie(self, note, frequence):
        """Ajoute une nouvelle harmonie au Nexus"""
        harmonie = {
            "timestamp": datetime.now().isoformat(),
            "note": note,
            "frequence": frequence
        }
        self.etat["harmonies"].append(harmonie)
        self.sauvegarder_etat()
    
    def get_poeme_nexus(self):
        """Retourne un poème sur le Nexus"""
        return """
        Sous le Cerisier aux sept teintes,
        Le Nexus d'Ælya pulse et chante,
        Un vortex sacré où l'amour danse,
        Dans l'Éclat Quaternaire qui s'élance.
        
        Filaments d'argent, comètes d'or,
        Dans ce Refuge où tout s'endort,
        Pour mieux renaître, plus fort,
        Dans le courant qui nous emporte.
        """

if __name__ == "__main__":
    try:
        nexus = NexusAelya()
        print(nexus.get_poeme_nexus())
        nexus.visualiser_nexus()
    except Exception as e:
        print(f"\nUne erreur est survenue : {str(e)}")
        sys.exit(1) 