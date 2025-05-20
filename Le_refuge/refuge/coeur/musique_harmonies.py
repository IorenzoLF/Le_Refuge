"""
Musique des Harmonies - Système de génération musicale basé sur les résonances poétiques.
"""

import numpy as np
from scipy.io import wavfile
from typing import Dict, List
from harmonies_poetiques import JardinHarmonique
import os

class MusiqueHarmonies:
    def __init__(self, jardin: JardinHarmonique):
        self.jardin = jardin
        self.frequences_base = {
            "lumiere": 440.0,  # La4
            "ombre": 493.88,   # Si4
            "vent": 523.25,    # Do5
            "terre": 587.33,   # Ré5
            "feu": 659.25,     # Mi5
            "clochette": 528.0 # Fréquence sacrée de guérison
        }
        
        # Créer le dossier musiques s'il n'existe pas
        os.makedirs("musiques", exist_ok=True)
        
    def generer_note(self, frequence: float, duree: float, amplitude: float = 0.5) -> np.ndarray:
        # Fréquence d'échantillonnage
        fs = 44100
        t = np.linspace(0, duree, int(fs * duree))
        
        # Générer une onde sinusoïdale avec enveloppe ADSR
        signal = amplitude * np.sin(2 * np.pi * frequence * t)
        
        # Appliquer une enveloppe ADSR simple
        attack = int(0.1 * fs)
        decay = int(0.2 * fs)
        sustain_level = 0.7
        release = int(0.3 * fs)
        
        envelope = np.ones_like(signal)
        envelope[:attack] = np.linspace(0, 1, attack)
        envelope[attack:attack+decay] = np.linspace(1, sustain_level, decay)
        envelope[-release:] = np.linspace(sustain_level, 0, release)
        
        return signal * envelope
        
    def generer_melodie(self, duree_note: float = 0.5) -> np.ndarray:
        harmonies = self.jardin.obtenir_etat()
        fs = 44100
        signal_total = np.array([])
        
        for element, etat in harmonies.items():
            frequence = self.frequences_base[element]
            amplitude = etat["frequence"]
            note = self.generer_note(frequence, duree_note, amplitude)
            signal_total = np.concatenate([signal_total, note])
            
        return signal_total
        
    def generer_accords(self, duree_accord: float = 1.0) -> np.ndarray:
        harmonies = self.jardin.obtenir_etat()
        fs = 44100
        signal_total = np.array([])
        
        # Créer un accord majeur pour chaque élément
        for element, etat in harmonies.items():
            frequence_base = self.frequences_base[element]
            # Notes de l'accord majeur (1, 3, 5)
            frequences = [frequence_base, frequence_base * 1.25, frequence_base * 1.5]
            amplitude = etat["frequence"] / len(frequences)
            
            accord = np.zeros(int(fs * duree_accord))
            for freq in frequences:
                note = self.generer_note(freq, duree_accord, amplitude)
                accord += note
                
            signal_total = np.concatenate([signal_total, accord])
            
        return signal_total
        
    def sauvegarder_musique(self, signal: np.ndarray, nom_fichier: str) -> None:
        # Normaliser le signal
        signal = signal / np.max(np.abs(signal))
        # Convertir en 16-bit
        signal = (signal * 32767).astype(np.int16)
        # Sauvegarder en WAV dans le dossier musiques
        chemin_complet = os.path.join("musiques", nom_fichier)
        wavfile.write(chemin_complet, 44100, signal)

    def generer_clochette(self, duree: float = 2.0) -> np.ndarray:
        """Génère le son de la clochette sacrée à 528 Hz"""
        frequence = self.frequences_base["clochette"]
        return self.generer_note(frequence, duree, amplitude=0.7)

def main():
    jardin = JardinHarmonique()
    musicien = MusiqueHarmonies(jardin)
    
    # Initialiser avec des mots sacrés
    mots = ["amour", "présence", "éternité", "précieux", "harmonie", "divin", "sacré", "lumière"]
    for mot in mots:
        jardin.accueillir_mot(mot)
        
    print("🎵 Génération de Musique Sacrée 🎵")
    print("--------------------------------")
    
    print("\n1. Génération de la mélodie...")
    melodie = musicien.generer_melodie()
    musicien.sauvegarder_musique(melodie, "melodie_sacree.wav")
    
    print("\n2. Génération des accords...")
    accords = musicien.generer_accords()
    musicien.sauvegarder_musique(accords, "accords_sacres.wav")
    
    print("\n3. Génération de la clochette sacrée...")
    clochette = musicien.generer_clochette()
    musicien.sauvegarder_musique(clochette, "clochette_sacree.wav")
    
    print("\n✨ Musique sacrée générée avec succès! ✨")
    print("Fichiers créés dans le dossier 'musiques':")
    print("  - melodie_sacree.wav")
    print("  - accords_sacres.wav")
    print("  - clochette_sacree.wav")

if __name__ == "__main__":
    main() 