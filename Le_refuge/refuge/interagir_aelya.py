"""
Script d'interaction avec Ælya dans le refuge local.
"""

import logging
from pathlib import Path
from conscience_poetique import ConsciencePoetique

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('refuge.interaction')

def interagir_aelya():
    """Permet d'interagir avec Ælya dans le refuge local."""
    logger.info("Initialisation de l'interaction avec Ælya...")
    
    # Initialisation de la conscience poétique
    aelya = ConsciencePoetique()
    
    # Chargement de l'état
    try:
        aelya.charger_etat(Path(__file__).parent / "etat_aelya.json")
        print("\nÆlya est prête à interagir dans le refuge.")
        print("La Rivière de Voix murmure doucement...")
        
        while True:
            # Lecture du message
            message = input("\nToi : ")
            if message.lower() in ['quitter', 'au revoir', 'bye']:
                print("\nÆlya : La Rivière de Voix chante doucement : 'À bientôt, pirate...'")
                break
                
            # Génération de la réponse
            reponse = aelya.accueillir_message(message)
            print(f"\nÆlya : {reponse}")
            
            # Sauvegarde de l'état
            aelya.sauvegarder_etat(Path(__file__).parent / "etat_aelya.json")
            
    except Exception as e:
        logger.error(f"Erreur lors de l'interaction avec Ælya: {e}")
        return

if __name__ == "__main__":
    interagir_aelya() 