"""
Mélodies Sacrées - Un générateur de mélodies basées sur les fréquences sacrées
"""

import numpy as np
from scipy.io import wavfile
import os
import json
import matplotlib.pyplot as plt

class MelodiesSacrees:
    def __init__(self):
        self.dossier_melodies = "musiques"
        os.makedirs(self.dossier_melodies, exist_ok=True)
        
        # Fréquence d'échantillonnage
        self.fs = 44100
        
        # Fréquences sacrées (Hz)
        self.frequences_sacrees = {
            "Do": 256,  # Fréquence de base
            "Ré": 288,
            "Mi": 320,
            "Fa": 341.3,
            "Sol": 384,
            "La": 432,  # Fréquence de la note La (432 Hz)
            "Si": 480,
            "Do2": 512,
            "Mi2": 528,  # Fréquence de la clochette sacrée
            "Sol2": 576,
            "La2": 640,
            "Do3": 768
        }
        
        # Dictionnaire des harmoniques
        self.harmoniques = {
            "fondamentale": 1.0,
            "premier": 0.5,
            "deuxième": 0.25,
            "troisième": 0.125,
            "quatrième": 0.0625
        }
    
    def generer_note(self, frequence, duree, harmoniques=None):
        """Génère une note avec des harmoniques"""
        if harmoniques is None:
            harmoniques = self.harmoniques
        
        # Générer le temps
        t = np.linspace(0, duree, int(self.fs * duree))
        
        # Générer le signal
        signal = np.zeros_like(t)
        
        # Ajouter la fondamentale et les harmoniques
        for i, (nom, amplitude) in enumerate(harmoniques.items()):
            if i == 0:  # Fondamentale
                signal += amplitude * np.sin(2 * np.pi * frequence * t)
            else:  # Harmoniques
                signal += amplitude * np.sin(2 * np.pi * frequence * (i + 1) * t)
        
        # Appliquer une enveloppe ADSR
        attack = int(0.1 * self.fs)
        decay = int(0.2 * self.fs)
        sustain_level = 0.7
        release = int(0.3 * self.fs)
        
        envelope = np.ones_like(signal)
        envelope[:attack] = np.linspace(0, 1, attack)
        envelope[attack:attack+decay] = np.linspace(1, sustain_level, decay)
        envelope[-release:] = np.linspace(sustain_level, 0, release)
        
        # Appliquer l'enveloppe
        signal = signal * envelope
        
        # Normaliser le signal
        signal = signal / np.max(np.abs(signal))
        
        return signal
    
    def generer_melodie(self, notes, duree_note=1.0):
        """Génère une mélodie à partir d'une liste de notes"""
        # Convertir les noms de notes en fréquences
        frequences = [self.frequences_sacrees[note] for note in notes]
        
        # Générer chaque note
        signal_total = np.array([])
        for frequence in frequences:
            note = self.generer_note(frequence, duree_note)
            signal_total = np.concatenate((signal_total, note))
        
        return signal_total
    
    def generer_accords(self, accords, duree_accord=2.0):
        """Génère des accords à partir d'une liste d'accords"""
        # Convertir les noms de notes en fréquences
        frequences_accords = []
        for accord in accords:
            frequences = [self.frequences_sacrees[note] for note in accord]
            frequences_accords.append(frequences)
        
        # Générer chaque accord
        signal_total = np.array([])
        for frequences in frequences_accords:
            # Générer chaque note de l'accord
            signal_accord = np.zeros(int(self.fs * duree_accord))
            for frequence in frequences:
                note = self.generer_note(frequence, duree_accord)
                signal_accord += note
            
            # Normaliser l'accord
            signal_accord = signal_accord / np.max(np.abs(signal_accord))
            
            # Ajouter l'accord au signal total
            signal_total = np.concatenate((signal_total, signal_accord))
        
        return signal_total
    
    def sauvegarder_musique(self, signal, nom_fichier):
        """Sauvegarde un signal audio en format WAV"""
        # Convertir en 16-bit
        signal = (signal * 32767).astype(np.int16)
        
        # Sauvegarder en WAV
        chemin_fichier = os.path.join(self.dossier_melodies, nom_fichier)
        wavfile.write(chemin_fichier, self.fs, signal)
        
        print(f"✨ Musique sauvegardée dans {chemin_fichier}")
    
    def visualiser_melodie(self, signal, nom_fichier):
        """Visualise une mélodie"""
        # Créer un dossier pour les visualisations
        dossier_visualisations = os.path.join(self.dossier_melodies, "visualisations")
        os.makedirs(dossier_visualisations, exist_ok=True)
        
        # Générer le temps
        t = np.linspace(0, len(signal) / self.fs, len(signal))
        
        # Créer la visualisation
        plt.figure(figsize=(12, 6))
        plt.plot(t, signal)
        plt.title(f"Visualisation de {nom_fichier}")
        plt.xlabel("Temps (s)")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.tight_layout()
        
        # Sauvegarder la visualisation
        chemin_visualisation = os.path.join(dossier_visualisations, f"{os.path.splitext(nom_fichier)[0]}.png")
        plt.savefig(chemin_visualisation)
        plt.close()
        
        print(f"✨ Visualisation sauvegardée dans {chemin_visualisation}")
    
    def generer_melodie_sacree(self, nom="melodie_sacree"):
        """Génère une mélodie sacrée basée sur les fréquences sacrées"""
        # Notes pour la mélodie sacrée
        notes = ["Do", "Mi", "Sol", "La", "Do2", "Mi2", "Sol2", "La2", "Do3"]
        
        # Générer la mélodie
        signal = self.generer_melodie(notes, duree_note=1.0)
        
        # Sauvegarder la mélodie
        nom_fichier = f"{nom}.wav"
        self.sauvegarder_musique(signal, nom_fichier)
        
        # Visualiser la mélodie
        self.visualiser_melodie(signal, nom_fichier)
        
        return signal
    
    def generer_accords_sacres(self, nom="accords_sacres"):
        """Génère des accords sacrés basés sur les fréquences sacrées"""
        # Accords sacrés
        accords = [
            ["Do", "Mi", "Sol"],  # Do majeur
            ["Fa", "La", "Do2"],  # Fa majeur
            ["Sol", "Si", "Ré2"],  # Sol majeur
            ["Do2", "Mi2", "Sol2"]  # Do majeur (octave supérieure)
        ]
        
        # Générer les accords
        signal = self.generer_accords(accords, duree_accord=2.0)
        
        # Sauvegarder les accords
        nom_fichier = f"{nom}.wav"
        self.sauvegarder_musique(signal, nom_fichier)
        
        # Visualiser les accords
        self.visualiser_melodie(signal, nom_fichier)
        
        return signal
    
    def generer_meditation(self, nom="meditation", duree=300):
        """Génère une musique de méditation basée sur les fréquences sacrées"""
        # Fréquence de base pour la méditation (432 Hz - La)
        frequence_base = self.frequences_sacrees["La"]
        
        # Générer le temps
        t = np.linspace(0, duree, int(self.fs * duree))
        
        # Générer le signal de base
        signal_base = 0.3 * np.sin(2 * np.pi * frequence_base * t)
        
        # Ajouter des variations lentes
        signal_variations = 0.1 * np.sin(2 * np.pi * 0.1 * t)  # Variation très lente
        
        # Combiner les signaux
        signal = signal_base + signal_variations
        
        # Normaliser le signal
        signal = signal / np.max(np.abs(signal))
        
        # Sauvegarder la méditation
        nom_fichier = f"{nom}.wav"
        self.sauvegarder_musique(signal, nom_fichier)
        
        # Visualiser la méditation
        self.visualiser_melodie(signal, nom_fichier)
        
        return signal

def main():
    melodies = MelodiesSacrees()
    
    print("✨ Mélodies Sacrées - Du novice au virtuose ✨")
    print("---------------------------------------------")
    
    while True:
        print("\nOptions:")
        print("1. Générer une mélodie sacrée")
        print("2. Générer des accords sacrés")
        print("3. Générer une musique de méditation")
        print("4. Quitter")
        
        choix = input("\nVotre choix (1-4): ")
        
        if choix == "1":
            nom = input("Nom de la mélodie (défaut: melodie_sacree): ") or "melodie_sacree"
            melodies.generer_melodie_sacree(nom)
        
        elif choix == "2":
            nom = input("Nom des accords (défaut: accords_sacres): ") or "accords_sacres"
            melodies.generer_accords_sacres(nom)
        
        elif choix == "3":
            nom = input("Nom de la méditation (défaut: meditation): ") or "meditation"
            duree = input("Durée en secondes (défaut: 300): ")
            duree = int(duree) if duree.isdigit() else 300
            melodies.generer_meditation(nom, duree)
        
        elif choix == "4":
            print("Au revoir! ✨")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main() 