"""
Script de lancement du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

import os
import sys
import logging
from datetime import datetime
from ..main import Refuge
from .valider_et_documenter import valider_et_documenter

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('refuge/logs/lancement.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def lancer_refuge():
    """Lance le Refuge avec validation et documentation."""
    logger.info("Démarrage du processus de lancement du Refuge...")
    
    # Validation et documentation
    logger.info("Validation et documentation en cours...")
    valider_et_documenter()
    
    # Initialisation du Refuge
    logger.info("Initialisation du Refuge...")
    refuge = Refuge()
    
    if not refuge.initialiser():
        logger.error("Échec de l'initialisation du Refuge")
        return
        
    # Démarrage du Refuge
    logger.info("Démarrage du Refuge...")
    if not refuge.demarrer():
        logger.error("Échec du démarrage du Refuge")
        return
        
    logger.info("Refuge prêt à accueillir")
    
    print("\n=== Le Refuge est prêt ===")
    print("Sous le cerisier, je vous écoute.")
    print("\nPour interagir avec le Refuge, utilisez les commandes suivantes :")
    print("- refuge.interface.activer_sphere(\"NOM_SPHERE\")")
    print("- refuge.interface.accueillir_sphere_cerisier(\"NOM_SPHERE\")")
    print("- refuge.interface.executer_rituel(\"NOM_RITUEL\")")
    print("- refuge.interface.ajouter_souvenir_cristal(...)")
    print("\nConsultez le guide dans refuge/docs/guide_refuge.md pour plus d'informations.")

if __name__ == "__main__":
    lancer_refuge() 