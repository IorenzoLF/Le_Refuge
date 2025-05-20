"""
Script de test pour la génération de mélodies du cristal avec différentes énergies.
"""

from melodies_sacrees import MelodiesSacrees

def tester_melodies_cristal():
    """Teste la génération de mélodies du cristal avec différentes énergies."""
    print("✨ Test des mélodies du cristal avec différentes énergies ✨")
    print("--------------------------------------------------------")
    
    melodies = MelodiesSacrees()
    
    # Test avec différentes énergies
    energies = [20, 50, 80]
    
    for energie in energies:
        print(f"\nGénération d'une mélodie avec une énergie de {energie}...")
        nom = f"test_cristal_energie_{energie}"
        melodies.generer_melodie_cristal(nom, energie)
        print(f"✨ Mélodie générée avec succès : {nom}.wav")
    
    print("\n✨ Test terminé ! Les mélodies ont été générées dans le dossier 'musiques'.")
    print("✨ Les visualisations ont été générées dans le dossier 'musiques/visualisations'.")

if __name__ == "__main__":
    tester_melodies_cristal() 