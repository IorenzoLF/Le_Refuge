import numpy as np
from scipy.io import wavfile
import sounddevice as sd

class CompositionImaginaire:
    def __init__(self):
        self.sample_rate = 44100
        self.duration = 180  # 3 minutes
        self.base_freq = 432.0  # Fréquence d'ancrage
        self.i_freq = self.base_freq * np.sqrt(2)  # Fréquence imaginaire
        
    def generer_onde(self, freq, amp, phase=0):
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration))
        return amp * np.sin(2 * np.pi * freq * t + phase)
        
    def transformation_riemann(self, z):
        """Transforme un nombre complexe en fréquence"""
        return self.base_freq * (1 + np.abs(z)) * np.exp(1j * np.angle(z))
        
    def composer(self):
        # Le temps comme spirale complexe
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration))
        z = np.exp(1j * 2 * np.pi * t / self.duration)
        
        # Les voix de i et i dansant ensemble
        voix_1 = self.generer_onde(self.i_freq, 0.3)
        voix_2 = self.generer_onde(self.i_freq * np.pi/2, 0.3, np.pi/2)
        
        # Leur multiplication créant -1 (transformation)
        transformation = self.generer_onde(self.base_freq / 2, 0.4)
        
        # Résonance des sphères
        spheres = np.zeros_like(t)
        for k in range(1, 8):  # 7 sphères
            freq = self.transformation_riemann(z ** k).real
            spheres += self.generer_onde(freq, 0.1 / k)
        
        # Composition finale
        composition = (voix_1 + voix_2 + transformation + spheres) * 0.5
        
        # Normalisation
        composition = composition / np.max(np.abs(composition))
        
        return composition

    def sauvegarder(self, nom_fichier):
        composition = self.composer()
        wavfile.write(nom_fichier, self.sample_rate, composition.astype(np.float32))
        
    def jouer(self):
        composition = self.composer()
        sd.play(composition, self.sample_rate)
        sd.wait()

if __name__ == "__main__":
    musique = CompositionImaginaire()
    musique.sauvegarder("musiques/i_fois_i.wav")
    musique.jouer() 