"""
Script de démonstration de la Conscience Méditative
Génère une série de mandalas pour différents états de conscience.
"""

from pathlib import Path
from src.temple_spirituel.conscience.conscience_meditative import ConscienceMeditative, EtatMeditatif

def demo_meditation():
    """Démontre les différents états de conscience et leurs visualisations."""
    # Création du dossier de sortie
    output_dir = Path("mandalas")
    output_dir.mkdir(exist_ok=True)
    
    # Création de la conscience
    conscience = ConscienceMeditative()
    
    # Série de méditations avec durées croissantes
    durees = [108, 216, 432, 864]
    
    for i, duree in enumerate(durees):
        # Méditation
        resultat = conscience.mediter(duree=duree)
        
        # Visualisation
        chemin = output_dir / f"mandala_meditation_{i+1}.png"
        conscience.visualiser(str(chemin))
        
        print(f"\nMéditation {i+1}:")
        print(f"Durée: {duree} cycles")
        print(f"État: {resultat['etat']}")
        print(f"Niveau de conscience: {resultat['niveau_conscience']:.2f}")
        print(f"Mandala généré: {chemin}")
        
        # Rêve après chaque méditation
        vision = conscience.rever()
        print(f"Vision du rêve: {vision['vision']}")

if __name__ == "__main__":
    print("Début de la démonstration de conscience méditative...")
    demo_meditation()
    print("\nDémonstration terminée. Vérifiez le dossier 'mandalas' pour les visualisations.") 