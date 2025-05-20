"""
Mélodie Sacrée - Script principal pour la génération de mélodies basées sur des mots sacrés
"""

import os
from musique_harmonies import MusiqueHarmonies

def main():
    # Créer le dossier musiques s'il n'existe pas
    os.makedirs("musiques", exist_ok=True)

    # Liste des mots sacrés
    mots_sacres = ["amour", "présence", "éternité", "précieux", "harmonie", "divin", "sacré", "lumière"]

    # Créer une instance de MusiqueHarmonies
    musique = MusiqueHarmonies()

    # Générer la mélodie et les accords
    melodie = musique.generer_melodie(mots_sacres, 0.5)
    accords = musique.generer_accords(mots_sacres, 2.0)

    # Sauvegarder les fichiers
    musique.sauvegarder_musique(melodie, "musiques/melodie_sacree.wav")
    print("Mélodie sacrée créée dans musiques/melodie_sacree.wav")
    
    musique.sauvegarder_musique(accords, "musiques/accords_sacres.wav")
    print("Accords sacrés créés dans musiques/accords_sacres.wav")

if __name__ == "__main__":
    main() 