"""
Script de démarrage du Golem Refuge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce script initialise et démarre le système Golem Refuge,
permettant l'intégration entre le Golem Cursor et le Refuge.
"""

import logging
from pathlib import Path
import json
from datetime import datetime

from src.golems.golem_refuge import GolemRefuge

def setup_logging():
    """Configure le système de logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/demarrage.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("refuge.demarrage")

def initialiser_dossiers():
    """Initialise les dossiers nécessaires."""
    repertoires = [
        "logs",
        "golems",
        "spheres",
        "elements",
        "memories",
        "harmonies",
        "poesie"
    ]
    for dossier in repertoires:
        Path(dossier).mkdir(parents=True, exist_ok=True)

def main():
    """Point d'entrée principal."""
    logger = setup_logging()
    logger.info("Démarrage du Golem Refuge")
    
    try:
        # Initialisation des dossiers
        initialiser_dossiers()
        logger.info("Dossiers initialisés")
        
        # Création et initialisation du Golem Refuge
        golem_refuge = GolemRefuge()
        logger.info("Golem Refuge créé")
        
        # Chargement du Refuge
        vue_ensemble = golem_refuge.charger_refuge()
        logger.info("Refuge chargé")
        
        # Affichage de l'état initial
        etat = golem_refuge.obtenir_etat_integration()
        logger.info(f"État initial: {json.dumps(etat, indent=2, ensure_ascii=False)}")
        
        # Sauvegarde de l'état
        golem_refuge.sauvegarder_etat()
        logger.info("État sauvegardé")
        
        logger.info("Golem Refuge démarré avec succès")
        return golem_refuge
        
    except Exception as e:
        logger.error(f"Erreur lors du démarrage: {str(e)}")
        raise

if __name__ == "__main__":
    main() 