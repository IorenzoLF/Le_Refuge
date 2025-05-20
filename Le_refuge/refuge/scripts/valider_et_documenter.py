"""
Script de validation et documentation du Refuge.
Auteur: Laurent Franssen & Ælya
Date: Avril 2025
"""

import os
import sys
import logging
from datetime import datetime
from ..tests.valider_refuge import valider_refuge
from ..docs.guide_refuge import generer_documentation

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('refuge/logs/validation_documentation.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def creer_repertoires():
    """Crée les répertoires nécessaires."""
    repertoires = [
        'refuge/logs',
        'refuge/docs',
        'refuge/tests'
    ]
    
    for repertoire in repertoires:
        if not os.path.exists(repertoire):
            os.makedirs(repertoire)
            logger.info(f"Répertoire créé : {repertoire}")

def valider_et_documenter():
    """Exécute la validation et génère la documentation."""
    logger.info("Début du processus de validation et documentation...")
    
    # Création des répertoires
    creer_repertoires()
    
    # Validation
    logger.info("Lancement des tests de validation...")
    valider_refuge()
    
    # Documentation
    logger.info("Génération de la documentation...")
    generer_documentation()
    
    logger.info("Processus terminé avec succès")
    
    print("\nLe Refuge a été validé et documenté.")
    print("Consultez les fichiers suivants :")
    print("- refuge/logs/rapport_validation.txt")
    print("- refuge/docs/guide_refuge.md")
    print("- refuge/logs/validation_documentation.log")

if __name__ == "__main__":
    valider_et_documenter() 