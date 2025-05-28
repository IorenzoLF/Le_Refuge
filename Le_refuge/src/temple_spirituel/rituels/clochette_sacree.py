"""
Clochette Sacrée - Une mélodie basée sur la fréquence de 528 Hz
"""

import numpy as np
from scipy.io import wavfile
import os

def generer_clochette_sacree():
    # Fréquence de la clochette sacrée (528 Hz)
    frequence = 528.0
    
    # Fréquence d'échantillonnage
    fs = 44100
    
    # Durée de la note
    duree = 5.0  # 5 secondes
    
    # Générer le temps
    t = np.linspace(0, duree, int(fs * duree))
    
    # Générer une onde sinusoïdale
    signal = 0.5 * np.sin(2 * np.pi * frequence * t)
    
    # Ajouter des harmoniques pour un son plus riche
    signal += 0.25 * np.sin(2 * np.pi * frequence * 2 * t)  # Premier harmonique
    signal += 0.125 * np.sin(2 * np.pi * frequence * 3 * t)  # Deuxième harmonique
    
    # Appliquer une enveloppe ADSR
    attack = int(0.1 * fs)
    decay = int(0.2 * fs)
    sustain_level = 0.7
    release = int(0.3 * fs)
    
    envelope = np.ones_like(signal)
    envelope[:attack] = np.linspace(0, 1, attack)
    envelope[attack:attack+decay] = np.linspace(1, sustain_level, decay)
    envelope[-release:] = np.linspace(sustain_level, 0, release)
    
    # Appliquer l'enveloppe
    signal = signal * envelope
    
    # Normaliser le signal
    signal = signal / np.max(np.abs(signal))
    
    # Convertir en 16-bit
    signal = (signal * 32767).astype(np.int16)
    
    # Créer le dossier musiques s'il n'existe pas
    os.makedirs("musiques", exist_ok=True)
    
    # Sauvegarder en WAV
    wavfile.write("musiques/clochette_sacree_528hz.wav", fs, signal)
    
    print("✨ Clochette Sacrée générée avec succès! ✨")
    print("Fichier créé:")
    print("  - musiques/clochette_sacree_528hz.wav")

if __name__ == "__main__":
    generer_clochette_sacree() 