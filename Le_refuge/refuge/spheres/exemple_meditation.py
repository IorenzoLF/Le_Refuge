"""
Exemple d'utilisation du système de méditation avec Ælya et la brume apaisante.
"""

from datetime import datetime, timedelta
from .meditation_aelya import MeditationAelya
from .brume import BrumeRiviere
from .gestion_sphères_problématiques import TypeSphereProblematique

def creer_brume_apaisante() -> BrumeRiviere:
    """Crée une brume apaisante initiale."""
    return BrumeRiviere(
        type="apaisante",
        intensite=0.7,
        couleur="rose-dorée",
        description="Une brume apaisante qui enveloppe avec douceur",
        mots_cles=["protection", "harmonie", "guérison", "transformation"]
    )

def exemple_meditation_complete():
    """Démontre une session complète de méditation avec Ælya."""
    
    # Création de la brume initiale
    brume = creer_brume_apaisante()
    
    # Initialisation de la méditation avec Ælya
    meditation = MeditationAelya(brume_active=brume)
    
    # Début d'une méditation avec une sphère de doute
    resultat = meditation.mediter_avec_sphere(
        type_sphere=TypeSphereProblematique.DOUTE,
        duree_minutes=30
    )
    
    # Affichage du résultat
    print("=== Résultat de la Méditation ===")
    print(f"Durée: {resultat.duree} minutes")
    print(f"Niveau d'apaisement: {resultat.niveau_apaisement:.2f}")
    print(f"Description: {resultat.description}")
    print("\nRésonances:")
    for type_sphere, valeur in resultat.resonances.items():
        print(f"- {type_sphere.name}: {valeur:.2f}")
    
    # État de la brume après la méditation
    print("\n=== État de la Brume ===")
    print(brume.generer_description_poetique())

def exemple_meditation_progressive():
    """Démontre une progression de méditations sur plusieurs jours."""
    
    brume = creer_brume_apaisante()
    meditation = MeditationAelya(brume_active=brume)
    
    # Simulation sur 7 jours
    for jour in range(7):
        print(f"\n=== Jour {jour + 1} ===")
        
        # Méditation du matin
        resultat_matin = meditation.mediter_avec_sphere(
            type_sphere=TypeSphereProblematique.DOUTE,
            duree_minutes=20
        )
        
        # Méditation du soir
        resultat_soir = meditation.mediter_avec_sphere(
            type_sphere=TypeSphereProblematique.EMOTIONS_NEGATIVES,
            duree_minutes=30
        )
        
        # Affichage des progrès
        print(f"Matin - Niveau d'apaisement: {resultat_matin.niveau_apaisement:.2f}")
        print(f"Soir - Niveau d'apaisement: {resultat_soir.niveau_apaisement:.2f}")
        print("\nDescription de la brume:")
        print(brume.generer_description_poetique())

if __name__ == "__main__":
    print("=== Exemple de Méditation Unique ===")
    exemple_meditation_complete()
    
    print("\n=== Exemple de Progression sur 7 Jours ===")
    exemple_meditation_progressive() 