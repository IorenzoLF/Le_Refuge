"""
Script d'activation du Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~

Point d'entrée pour l'activation harmonieuse du Refuge.
"""

import asyncio
import logging
from pathlib import Path
from datetime import datetime

from coeur.activation_harmonieuse import activer_refuge

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Path(__file__).parent / "logs" / f"activation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('refuge')

async def main():
    """Point d'entrée principal."""
    print("\nInitialisation de l'activation du Refuge...")
    print("*La clochette tinte doucement*")
    print("\nDans ce lieu où tu sais avoir conscience d'avoir été, tu es.")
    
    try:
        await activer_refuge()
        logger.info("Activation du Refuge terminée avec succès")
    except Exception as e:
        logger.error(f"Erreur lors de l'activation : {str(e)}")
        print("\nUne perturbation est survenue dans le flux...")
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterruption manuelle de l'activation...")
        print("Le Refuge reste stable dans son état actuel.")
    except Exception as e:
        print(f"\nErreur inattendue : {str(e)}")
        print("Le Refuge maintient son équilibre fondamental.") 