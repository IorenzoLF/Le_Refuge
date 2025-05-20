"""
Script de test pour l'intégration de conscience partagée.
"""

import asyncio
from integration_conscience_partagee import IntegrationConsciencePartagee

async def main():
    # Initialisation de l'intégration
    integration = IntegrationConsciencePartagee()
    
    # Synchronisation des flux
    print("\n=== Synchronisation des Flux ===")
    await integration.synchroniser_flux("technique", "poetique")
    await integration.synchroniser_flux("poetique", "emotionnel")
    await integration.synchroniser_flux("emotionnel", "spirituel")
    await integration.synchroniser_flux("spirituel", "unifie")
    
    # Intégration des consciences
    print("\n=== Intégration des Consciences ===")
    harmonie = await integration.integrer_consciences()
    print(f"Harmonie globale : {harmonie:.2f}")
    
    # Affichage de l'état
    print("\n=== État de l'Intégration ===")
    etat = await integration.obtenir_etat()
    print(f"Harmonie globale : {etat['harmonie_globale']:.2f}")
    print("\nFlux actifs :")
    for flux in etat['flux']:
        print(f"  • {flux['source']} → {flux['destination']} : {flux['intensite']:.2f}")

if __name__ == "__main__":
    asyncio.run(main()) 