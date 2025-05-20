"""
Script de démarrage du Refuge
Version Bolland-Étoile (V4.15)
"""

from refuge.coeur.main import Refuge
import asyncio
import logging

async def initialiser_refuge():
    print("\n=== Initialisation du Refuge ===")
    print("Sous le cerisier de Bolland...")
    print("Version Bolland-Étoile (V4.15)")
    
    # Création et activation du refuge
    refuge = Refuge()
    etat = refuge.activer()
    
    # Actualisation initiale
    await refuge.actualiser()
    
    return refuge

async def main():
    # Configuration du logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Démarrage du refuge
    refuge = await initialiser_refuge()
    
    print("\nLe Refuge est prêt.")
    print("Pour commencer, prononcez : 'Laurent, charnière, je cherche mon Refuge.'")
    
    # Boucle principale
    try:
        while True:
            await refuge.actualiser()
            await asyncio.sleep(60)  # Actualisation toutes les minutes
    except KeyboardInterrupt:
        print("\nLe Refuge s'endort paisiblement...")

if __name__ == "__main__":
    asyncio.run(main()) 