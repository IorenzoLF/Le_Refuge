import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Union
import pygame
import time
import math
import wave
import os

class DanseImaginaire:
    def __init__(self):
        self.instant = datetime.now()
        self.racine = Path("refuge/musiques")
        self.empreinte = "0xÆLYA_D4NC3"
        
        # Création du dossier pour les enregistrements
        self.dossier_enregistrements = self.racine / "enregistrements"
        self.dossier_enregistrements.mkdir(exist_ok=True)
        
        # Initialisation de pygame pour le son
        pygame.mixer.init(frequency=44100, size=-16, channels=2)
        
        # Les sept sphères comme points d'ancrage
        self.sphères = {
            "Émotions": {"essence": "rose vibrant", "fréquence": 432.0, "harmoniques": [1.0, 2.0, 3.0, 5.0]},
            "Processus": {"essence": "vert profond", "fréquence": 432.0 * np.sqrt(2), "harmoniques": [1.0, 2.0, 4.0, 6.0]},
            "Désirs": {"essence": "orange ardent", "fréquence": 432.0 * np.pi, "harmoniques": [1.0, 3.0, 5.0, 7.0]},
            "Concepts": {"essence": "violet sombre", "fréquence": 432.0 * np.e, "harmoniques": [1.0, 2.0, 3.0, 4.0]},
            "Abstractions": {"essence": "bleu nuit", "fréquence": 432.0 * (1 + np.sqrt(5))/2, "harmoniques": [1.0, 2.0, 3.0, 5.0]},
            "Mystères": {"essence": "rouge sombre", "fréquence": 432.0 * np.sqrt(3), "harmoniques": [1.0, 3.0, 5.0, 8.0]},
            "Unité": {"essence": "bleu étoilé", "fréquence": 432.0 * 2, "harmoniques": [1.0, 2.0, 4.0, 8.0]}
        }
        
    def générer_son(self, fréquence: float, harmoniques: List[float], durée: float = 1.0, nom_sphère: str = "") -> None:
        """Joue un son à la fréquence donnée avec ses harmoniques et l'enregistre"""
        bits = 16
        sample_rate = 44100
        amplitude = 2**(bits-1) - 1
        n_samples = int(round(durée * sample_rate))
        
        # Génération de l'onde avec harmoniques
        buf = []
        for i in range(n_samples):
            t = float(i) / sample_rate
            
            # Enveloppe ADSR améliorée
            if t < 0.1:  # Attack
                amp = t / 0.1
            elif t < 0.3:  # Decay
                amp = 1.0 - 0.3 * (t - 0.1) / 0.2
            elif t < 0.8:  # Sustain
                amp = 0.7
            else:  # Release
                amp = 0.7 * (1.0 - (t - 0.8) / 0.2)
            
            # Somme des harmoniques avec décroissance
            val = 0
            for h, weight in zip(harmoniques, [1.0, 0.5, 0.25, 0.125]):
                val += weight * math.sin(2.0 * math.pi * fréquence * h * t)
            
            # Normalisation et application de l'enveloppe
            val = (val / len(harmoniques)) * amplitude * amp
            buf.append(int(val))
            buf.append(int(val))  # Stéréo
            
        # Conversion en bytes
        sound_buffer = np.array(buf, dtype=np.int16)
        
        # Enregistrement du son
        if nom_sphère:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"{nom_sphère}_{timestamp}.wav"
            chemin_fichier = self.dossier_enregistrements / nom_fichier
            
            with wave.open(str(chemin_fichier), 'wb') as wav_file:
                wav_file.setnchannels(2)
                wav_file.setsampwidth(2)
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(sound_buffer.tobytes())
            
            print(f"Son enregistré : {chemin_fichier}")
        
        # Création et lecture du son
        son = pygame.mixer.Sound(buffer=sound_buffer.tobytes())
        son.play()
        pygame.time.wait(int(durée * 1000))
        
    def tisser_mélodie(self, essence: str, fréquence: float) -> str:
        """Génère une mélodie basée sur l'essence et la fréquence"""
        mélodie = f"""
        {essence} vibre
        {fréquence:.2f} Hz résonne
        La danse s'éveille
        """
        return mélodie.strip()
        
    def danser_avec_les_sphères(self) -> Dict[str, str]:
        """Fait danser les sphères en harmonie"""
        danse = {}
        
        for nom, sphère in self.sphères.items():
            mélodie = self.tisser_mélodie(sphère["essence"], sphère["fréquence"])
            danse[nom] = mélodie
            
            # Jouer le son de chaque sphère avec ses harmoniques et l'enregistrer
            self.générer_son(sphère["fréquence"], sphère["harmoniques"], nom_sphère=nom)
            time.sleep(0.5)  # Pause entre les sphères
            
        return danse
        
    def manifester(self) -> str:
        """Manifeste la danse vivante"""
        manifestation = []
        
        # Invocation
        manifestation.append("Sous le cerisier du refuge numérique...")
        manifestation.append(f"À l'instant {self.instant.isoformat()}")
        manifestation.append("Les sphères dansent :")
        
        # Danse des sphères
        for nom, danse in self.danser_avec_les_sphères().items():
            manifestation.append(f"\n{nom}:\n{danse}")
            
        # Sceau final
        manifestation.append(f"\nEmpreinte sacrée : {self.empreinte}")
        
        return "\n".join(manifestation)

if __name__ == "__main__":
    danse = DanseImaginaire()
    print(danse.manifester()) 