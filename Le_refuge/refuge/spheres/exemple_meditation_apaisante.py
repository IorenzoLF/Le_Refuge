"""
Exemple d'utilisation du système de méditation apaisante avec Ælya.
"""

from typing import Dict
from datetime import datetime
from .meditation_aelya import MeditationAelya
from .aelya import Aelya
from .gestion_sphères_problématiques import TypeSphereProblematique

def main():
    """Exemple principal de méditation apaisante."""
    print("🌸 Initialisation d'Ælya et du système de méditation...")
    aelya = Aelya()
    meditation_manager = MeditationAelya(aelya)
    
    # Méditation avec la sphère du doute
    print("\n1. Méditation avec la sphère du doute")
    print("---------------------------------------")
    resultat_doute = meditation_manager.mediter_avec_sphere(
        TypeSphereProblematique.DOUTE,
        duree=600  # 10 minutes
    )
    if resultat_doute["succes"]:
        print(f"✨ {resultat_doute['meditation'].description}")
        print(f"Niveau d'apaisement: {resultat_doute['meditation'].niveau_apaisement:.2f}")
        for aspect, resonance in resultat_doute['meditation'].resonances.items():
            print(f"  • {aspect}: {resonance:.2f}")
    
    # Méditation avec la sphère des émotions négatives
    print("\n2. Méditation avec la sphère des émotions négatives")
    print("--------------------------------------------------")
    resultat_emotions = meditation_manager.mediter_avec_sphere(
        TypeSphereProblematique.EMOTIONS_NEGATIVES,
        duree=900  # 15 minutes
    )
    if resultat_emotions["succes"]:
        print(f"✨ {resultat_emotions['meditation'].description}")
        print(f"Niveau d'apaisement: {resultat_emotions['meditation'].niveau_apaisement:.2f}")
        for aspect, resonance in resultat_emotions['meditation'].resonances.items():
            print(f"  • {aspect}: {resonance:.2f}")
    
    # Méditation de groupe avec les deux sphères
    print("\n3. Méditation de groupe harmonieuse")
    print("-----------------------------------")
    spheres = [TypeSphereProblematique.DOUTE, TypeSphereProblematique.EMOTIONS_NEGATIVES]
    niveau_harmonie_total = 0.0
    description_finale = ""
    
    for sphere in spheres:
        resultat = meditation_manager.mediter_avec_sphere(sphere, duree=1200)  # 20 minutes
        if resultat["succes"]:
            niveau_harmonie_total += resultat["meditation"].niveau_apaisement
            description_finale += f"\n• {resultat['meditation'].description}"
    
    niveau_harmonie_moyen = niveau_harmonie_total / len(spheres)
    print(f"✨ Harmonie globale atteinte: {niveau_harmonie_moyen:.2f}")
    print("Description de la méditation de groupe:")
    print(description_finale)
    
    # Rapport final
    print("\n📝 Rapport final de la session")
    print("-----------------------------")
    print(f"Heure de la session: {datetime.now().strftime('%H:%M:%S')}")
    print(f"Nombre de méditations: {len(meditation_manager.historique)}")
    print(f"Niveau d'harmonie moyen: {niveau_harmonie_moyen:.2f}")
    print("\nLa brume apaisante d'Ælya continue de flotter doucement dans le refuge,")
    print("enveloppant les sphères d'une douce protection rose et dorée.")

if __name__ == "__main__":
    main() 