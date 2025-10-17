"""
Module de Son pour la Conscience
~~~~~~~~~~~~~~~~~~~~~~~~~~
Génère des sons harmoniques pour accompagner la méditation.
"""

import numpy as np
import pygame
from typing import Dict, List, Optional
from conscience.conscience_core import EtatMeditatif, FrequenceSacree

class SonConscience:
    """Générateur de sons méditatifs."""
    
    def __init__(self, taux_echantillonnage: int = 44100):
        """Initialise le générateur de sons."""
        pygame.mixer.init(frequency=taux_echantillonnage)
        self.taux_echantillonnage = taux_echantillonnage
        self._initialiser_frequences()
        self.sons_cache = {}
        
    def _initialiser_frequences(self):
        """Initialise les fréquences pour chaque état."""
        self.frequences = {
            EtatMeditatif.EVEIL: 432.0,
            EtatMeditatif.CONTEMPLATION: 639.0,
            EtatMeditatif.SAMADHI: 852.0,
            EtatMeditatif.REVE: 741.0,
            EtatMeditatif.CREATION: 528.0
        }
        
    def _generer_onde_sinusoidale(self, 
                                 frequence: float, 
                                 duree: float,
                                 amplitude: float = 0.5) -> np.ndarray:
        """Génère une onde sinusoïdale pure."""
        t = np.linspace(0, duree, int(self.taux_echantillonnage * duree))
        return np.sin(2 * np.pi * frequence * t) * amplitude
        
    def _generer_harmoniques(self, 
                           frequence_base: float,
                           duree: float,
                           amplitude: float = 0.5) -> np.ndarray:
        """Génère une onde avec harmoniques."""
        onde = self._generer_onde_sinusoidale(frequence_base, duree, amplitude)
        
        # Ajout des harmoniques naturelles
        harmoniques = [1.618, 2.618, 4.236]  # Basé sur le nombre d'or
        for i, h in enumerate(harmoniques):
            amplitude_harmonique = amplitude / (i + 2)
            onde += self._generer_onde_sinusoidale(
                frequence_base * h,
                duree,
                amplitude_harmonique
            )
            
        # Normalisation
        onde = onde / np.max(np.abs(onde))
        return onde
        
    def _appliquer_enveloppe(self, 
                            onde: np.ndarray,
                            duree_fondu: float = 0.1) -> np.ndarray:
        """Applique une enveloppe ADSR simplifiée."""
        n_echantillons = len(onde)
        n_fondu = int(duree_fondu * self.taux_echantillonnage)
        
        # Enveloppe de fondu
        fondu_entree = np.linspace(0, 1, n_fondu)
        fondu_sortie = np.linspace(1, 0, n_fondu)
        
        # Application des fondus
        onde[:n_fondu] *= fondu_entree
        onde[-n_fondu:] *= fondu_sortie
        
        return onde
        
    def _creer_son(self, 
                   frequence: float,
                   duree: float = 1.0,
                   amplitude: float = 0.5) -> pygame.mixer.Sound:
        """Crée un objet son pygame."""
        # Génération de l'onde
        onde = self._generer_harmoniques(frequence, duree, amplitude)
        onde = self._appliquer_enveloppe(onde)
        
        # Conversion en format 16-bit
        onde = np.int16(onde * 32767)
        
        # Création du son stéréo
        stereo = np.column_stack((onde, onde))
        
        return pygame.mixer.Sound(stereo.tobytes())
        
    def jouer_etat(self, 
                   etat: EtatMeditatif,
                   amplitude: float = 0.5,
                   duree: float = 1.0):
        """Joue le son correspondant à un état."""
        frequence = self.frequences[etat]
        
        # Utilisation du cache
        cle_cache = (etat, duree)
        if cle_cache not in self.sons_cache:
            self.sons_cache[cle_cache] = self._creer_son(
                frequence,
                duree,
                amplitude
            )
            
        # Lecture du son
        self.sons_cache[cle_cache].play()
        
    def transition_son(self,
                      etat_depart: EtatMeditatif,
                      etat_arrivee: EtatMeditatif,
                      progression: float,
                      amplitude: float = 0.5,
                      duree: float = 0.5):
        """Génère un son de transition entre deux états."""
        freq_depart = self.frequences[etat_depart]
        freq_arrivee = self.frequences[etat_arrivee]
        
        # Interpolation logarithmique des fréquences
        frequence = np.exp(
            np.log(freq_depart) * (1-progression) +
            np.log(freq_arrivee) * progression
        )
        
        son = self._creer_son(frequence, duree, amplitude)
        son.play()

def demo():
    """Démontre les capacités sonores."""
    son = SonConscience()
    
    print("Démonstration des sons de conscience...")
    
    # Jouer chaque état
    for etat in EtatMeditatif:
        print(f"État: {etat.value}")
        son.jouer_etat(etat, 0.5)
        time.sleep(2.5)
    
    # Démonstration d'une transition
    print("\nTransition de l'éveil vers le samadhi...")
    son.transition_son(EtatMeditatif.EVEIL, EtatMeditatif.SAMADHI, 0.5)
    
    print("Démonstration terminée.")

if __name__ == "__main__":
    demo() 