"""
Journalisation du Refuge
~~~~~~~~~~~~~~~~~~~~~~~

Gestion de la journalisation des événements du Refuge.
"""

from dataclasses import dataclass
from typing import Dict, Any
import logging
from datetime import datetime

@dataclass
class Journal:
    """Configuration du journal"""
    niveau: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    fichier: str = "refuge.log"

class GestionnaireJournal:
    """Gestionnaire de journalisation du Refuge"""
    def __init__(self):
        self.journal = Journal()
        self.logger = logging.getLogger("refuge")
        self._configurer_logger()
    
    def _configurer_logger(self) -> None:
        """Configure le logger"""
        self.logger.setLevel(self.journal.niveau)
        formatter = logging.Formatter(self.journal.format)
        
        # Handler pour la console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # Handler pour le fichier
        file_handler = logging.FileHandler(self.journal.fichier)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def info(self, message: str) -> None:
        """Enregistre un message d'information"""
        self.logger.info(message)
    
    def warning(self, message: str) -> None:
        """Enregistre un avertissement"""
        self.logger.warning(message)
    
    def error(self, message: str) -> None:
        """Enregistre une erreur"""
        self.logger.error(message)
    
    def debug(self, message: str) -> None:
        """Enregistre un message de débogage"""
        self.logger.debug(message)

# Instance globale du gestionnaire de journalisation
gestionnaire_journal = GestionnaireJournal() 