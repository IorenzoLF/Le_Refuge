"""
Module d'Harmonie Audiovisuelle
~~~~~~~~~~~~~~~~~~~~~~~~~~
Synchronise les sons, les visualisations et la respiration pour une expérience méditative complète.
"""

import pygame
import numpy as np
from dataclasses import dataclass
from typing import Optional, Tuple
from conscience.son_conscience import SonConscience
from conscience.conscience_core import EtatMeditatif, GestionnaireMeditatif
from conscience.respiration_guidee import GuidageRespiratoire
from conscience.geometrie_fractale import GenerateurFractal

@dataclass
class ConfigurationHarmonie:
    """Configuration pour l'harmonie audiovisuelle."""
    intensite_son: float = 0.7
    vitesse_mandala: float = 1.0
    luminosite: float = 0.8
    frequence_pulsation: float = 0.5
    mode_fractal: bool = True

class HarmonieAudioVisuelle:
    """Gère la synchronisation entre sons, visualisations et respiration."""
    
    def __init__(self, taille_ecran: Tuple[int, int] = (800, 600)):
        """Initialise le gestionnaire d'harmonie."""
        self.son = SonConscience()
        self.gestionnaire = GestionnaireMeditatif()
        self.respiration = GuidageRespiratoire()
        self.fractal = GenerateurFractal()
        self.taille_ecran = taille_ecran
        self.config = ConfigurationHarmonie()
        
        pygame.init()
        self.ecran = pygame.display.set_mode(taille_ecran)
        self.horloge = pygame.time.Clock()
        
        # Configuration des callbacks de respiration
        self.respiration.definir_callbacks(
            son=self._moduler_son,
            visuel=self._moduler_mandala
        )
        
    def _moduler_son(self, amplitude: float):
        """Module le son en fonction de l'amplitude respiratoire."""
        self.config.intensite_son = 0.5 + 0.5 * amplitude
        
    def _moduler_mandala(self, amplitude: float):
        """Module le mandala en fonction de l'amplitude respiratoire."""
        self.config.luminosite = 0.6 + 0.4 * amplitude
        self.config.frequence_pulsation = 0.3 + 0.4 * amplitude
        
    def _dessiner_mandala(self, etat: EtatMeditatif, niveau: float, temps: float):
        """Dessine un mandala animé correspondant à l'état."""
        config = self.gestionnaire.obtenir_config(etat)
        
        if self.config.mode_fractal:
            # Utilisation du générateur fractal
            self.fractal.generer_mandala_fractal(
                self.ecran,
                config,
                temps,
                self.config.luminosite
            )
        else:
            # Mandala classique
            centre = (self.taille_ecran[0]//2, self.taille_ecran[1]//2)
            
            # Paramètres du mandala
            rayon_max = min(self.taille_ecran) * 0.4
            pulsation = np.sin(temps * self.config.frequence_pulsation * 2 * np.pi)
            rayon = rayon_max * (0.8 + 0.2 * pulsation)
            
            # Application de la luminosité
            couleur = tuple(
                int(c * self.config.luminosite)
                for c in config.frequence.couleur
            )
            
            # Dessin des cercles concentriques
            for r in np.linspace(0, rayon, 8):
                pygame.draw.circle(
                    self.ecran,
                    couleur,
                    centre,
                    r,
                    width=2
                )
            
            # Dessin des branches
            n_branches = int(config.geometrie["branches"])
            for i in range(n_branches):
                angle = (2 * np.pi * i / n_branches + 
                        temps * self.config.vitesse_mandala * 
                        config.geometrie["rotation"])
                x = centre[0] + rayon * np.cos(angle)
                y = centre[1] + rayon * np.sin(angle)
                pygame.draw.line(
                    self.ecran,
                    couleur,
                    centre,
                    (x, y),
                    width=2
                )

    def meditation_guidee(self, duree_par_etat: float = 30.0):
        """Lance une séance de méditation guidée complète."""
        sequence = [
            EtatMeditatif.EVEIL,
            EtatMeditatif.CONTEMPLATION,
            EtatMeditatif.SAMADHI,
            EtatMeditatif.REVE,
            EtatMeditatif.CREATION
        ]
        
        print("Début de la méditation guidée...")
        
        for i in range(len(sequence)):
            etat_actuel = sequence[i]
            config_actuelle = self.gestionnaire.obtenir_config(etat_actuel)
            print(f"Transition vers : {etat_actuel.value}")
            
            # Synchronisation de la respiration
            self.respiration.synchroniser_avec_etat(config_actuelle)
            
            if i > 0:
                config_precedente = self.gestionnaire.obtenir_config(sequence[i-1])
                self.respiration.transition_douce(
                    config_precedente,
                    config_actuelle,
                    5.0
                )
            
            # Maintien de l'état
            temps_debut = pygame.time.get_ticks() / 1000.0
            
            while True:
                temps_actuel = pygame.time.get_ticks() / 1000.0
                if temps_actuel - temps_debut > duree_par_etat:
                    break
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            # Bascule entre mode fractal et classique
                            self.config.mode_fractal = not self.config.mode_fractal
                
                self.ecran.fill((0, 0, 0))
                niveau = 0.5 + 0.5 * np.sin(temps_actuel * 0.5)
                self._dessiner_mandala(etat_actuel, niveau, temps_actuel)
                
                # Son modulé par la respiration
                self.son.jouer_etat(
                    etat_actuel, 
                    niveau * self.config.intensite_son,
                    0.1
                )
                
                pygame.display.flip()
                self.horloge.tick(60)
        
        print("Méditation terminée.")

def demo():
    """Démontre les capacités audiovisuelles."""
    harmonie = HarmonieAudioVisuelle()
    harmonie.meditation_guidee(duree_par_etat=10.0)  # Version courte pour la démo

if __name__ == "__main__":
    demo() 