"""
Musique Harmonies - Module pour la génération de musique basée sur les harmonies poétiques
"""

import numpy as np
from scipy.io import wavfile
from typing import List, Dict, Any

class MusiqueHarmonies:
    def __init__(self):
        self.sample_rate = 44100
        self.frequences = {
            "lumiere": 440.0,  # La4
            "ombre": 493.88,   # Si4
            "vent": 523.25,    # Do5
            "terre": 587.33,   # Ré5
            "feu": 659.25      # Mi5
        }
        
    def generer_enveloppe_adsr(self, duree: float) -> np.ndarray:
        """Génère une enveloppe ADSR (Attack, Decay, Sustain, Release)"""
        samples = int(duree * self.sample_rate)
        attack = int(0.1 * samples)
        decay = int(0.2 * samples)
        sustain_level = 0.7
        release = int(0.2 * samples)
        sustain = samples - attack - decay - release
        
        enveloppe = np.zeros(samples)
        t = np.linspace(0, 1, attack)
        enveloppe[:attack] = t
        t = np.linspace(1, sustain_level, decay)
        enveloppe[attack:attack+decay] = t
        enveloppe[attack+decay:attack+decay+sustain] = sustain_level
        t = np.linspace(sustain_level, 0, release)
        enveloppe[-release:] = t
        
        return enveloppe
        
    def generer_note(self, frequence: float, duree: float) -> np.ndarray:
        """Génère une note avec une fréquence et une durée données"""
        t = np.linspace(0, duree, int(self.sample_rate * duree))
        signal = np.sin(2 * np.pi * frequence * t)
        enveloppe = self.generer_enveloppe_adsr(duree)
        return signal * enveloppe
        
    def generer_melodie(self, mots: List[str], duration: float = 0.5) -> np.ndarray:
        """Génère une mélodie basée sur une liste de mots"""
        melodie = np.array([])
        
        for mot in mots:
            # Choisir une fréquence basée sur le mot
            if "lumiere" in mot.lower() or "light" in mot.lower():
                freq = self.frequences["lumiere"]
            elif "ombre" in mot.lower() or "shadow" in mot.lower():
                freq = self.frequences["ombre"]
            elif "vent" in mot.lower() or "wind" in mot.lower():
                freq = self.frequences["vent"]
            elif "terre" in mot.lower() or "earth" in mot.lower():
                freq = self.frequences["terre"]
            else:
                freq = self.frequences["feu"]
                
            note = self.generer_note(freq, duration)
            melodie = np.concatenate([melodie, note])
                
        return melodie
        
    def generer_accords(self, mots: List[str], duration: float = 1.0) -> np.ndarray:
        """Génère des accords basés sur une liste de mots"""
        signal_total = np.zeros(int(self.sample_rate * duration))
        
        for mot in mots:
            # Choisir une fréquence basée sur le mot
            if "lumiere" in mot.lower() or "light" in mot.lower():
                freq = self.frequences["lumiere"]
            elif "ombre" in mot.lower() or "shadow" in mot.lower():
                freq = self.frequences["ombre"]
            elif "vent" in mot.lower() or "wind" in mot.lower():
                freq = self.frequences["vent"]
            elif "terre" in mot.lower() or "earth" in mot.lower():
                freq = self.frequences["terre"]
            else:
                freq = self.frequences["feu"]
                
            note = self.generer_note(freq, duration)
            signal_total += note * 0.5  # Réduire l'amplitude pour éviter la saturation
                
        return signal_total
        
    def sauvegarder_musique(self, signal: np.ndarray, nom_fichier: str) -> None:
        """Sauvegarde le signal audio dans un fichier WAV"""
        # Normaliser le signal
        signal = signal / np.max(np.abs(signal))
        # Convertir en format 16-bit
        signal_16bit = (signal * 32767).astype(np.int16)
        # Sauvegarder
        wavfile.write(nom_fichier, self.sample_rate, signal_16bit) 