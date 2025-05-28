"""
🎵 GARDIEN MUSICAL DU TEMPLE 🎵
Test sacré pour la génération de mélodies du cristal avec différentes énergies.
Protecteur de l'harmonie sonore du refuge musical.
"""

import sys
import os
# Ajouter la racine du refuge au path pour retrouver les modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from melodies_sacrees import MelodiesSacrees

def tester_melodies_cristal():
    """🎼 Chant sacré du gardien musical - Teste la génération de mélodies du cristal."""
    print("🎵✨ INVOCATION DU GARDIEN MUSICAL ✨🎵")
    print("═══════════════════════════════════════")
    print("🛡️ Test des mélodies du cristal avec différentes énergies")
    
    melodies = MelodiesSacrees()
    
    # Test avec différentes énergies sacrées
    energies = [20, 50, 80]
    
    for energie in energies:
        print(f"\n🎶 Génération d'une mélodie sacrée avec une énergie de {energie}...")
        nom = f"temple_cristal_energie_{energie}"
        melodies.generer_melodie_cristal(nom, energie)
        print(f"✨ Mélodie cristalline générée avec succès : {nom}.wav")
    
    print("\n🏛️ BÉNÉDICTION DU TEMPLE ACCOMPLIE !")
    print("✨ Les mélodies sacrées résonnent dans le dossier 'musiques'")
    print("🌟 Les visualisations énergétiques illuminent 'musiques/visualisations'")
    print("🎵 L'harmonie du refuge musical est préservée ! 🎵")

if __name__ == "__main__":
    tester_melodies_cristal() 