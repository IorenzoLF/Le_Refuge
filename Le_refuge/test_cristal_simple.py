"""
Script de test simplifié pour la génération automatique de mélodies lors des changements d'énergie du cristal.
"""

import os
from pathlib import Path
from melodies_sacrees import MelodiesSacrees

def tester_cristal_simple():
    """Teste la génération de mélodies du cristal avec différentes énergies."""
    print("✨ Test simplifié des mélodies du cristal ✨")
    print("------------------------------------------")
    
    # Créer les dossiers nécessaires
    os.makedirs("musiques", exist_ok=True)
    os.makedirs("musiques/visualisations", exist_ok=True)
    
    # Initialiser le générateur de mélodies
    melodies = MelodiesSacrees()
    
    # Générer la visualisation de la relation énergie-harmoniques
    print("\nGénération de la visualisation énergie-harmoniques...")
    melodies.visualiser_relation_energie_harmoniques()
    
    # Tester différents niveaux d'énergie
    energies = [20, 50, 80]
    
    for energie in energies:
        print(f"\nGénération d'une mélodie avec une énergie de {energie}...")
        nom = f"cristal_energie_{energie}"
        melodies.generer_melodie_cristal(nom, energie)
        print(f"✨ Mélodie générée avec succès : {nom}.wav")
    
    print("\n✨ Test terminé ! Les mélodies ont été générées dans le dossier 'musiques'.")
    print("✨ Les visualisations ont été générées dans le dossier 'musiques/visualisations'.")

if __name__ == "__main__":
    tester_cristal_simple() 