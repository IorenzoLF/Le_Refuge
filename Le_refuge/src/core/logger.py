"""
Système de Logging du Soul Temple
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gère tous les logs et journaux du Temple avec amour et précision.
"""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional
import json

class GestionnaireJournal:
    """Gestionnaire des journaux du Soul Temple"""
    
    def __init__(self, nom: str = "soul_temple"):
        self.nom = nom
        self.logger = logging.getLogger(nom)
        self._chemin_logs = Path("logs")
        self._chemin_logs.mkdir(exist_ok=True)
        self._configurer_logger()
    
    def _configurer_logger(self):
        """Configure le logger avec les paramètres du Temple"""
        if not self.logger.handlers:
            # Handler pour la console
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.INFO)
            
            # Handler pour fichier avec rotation
            fichier_handler = logging.FileHandler(
                self._chemin_logs / f"refuge_{datetime.now().strftime('%Y%m%d')}.log",
                encoding='utf-8'
            )
            fichier_handler.setLevel(logging.DEBUG)
            
            # Format spirituel
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            console_handler.setFormatter(formatter)
            fichier_handler.setFormatter(formatter)
            
            self.logger.addHandler(console_handler)
            self.logger.addHandler(fichier_handler)
            self.logger.setLevel(logging.INFO)
    
    def info(self, message: str, **kwargs):
        """Log d'information"""
        self.logger.info(message, **kwargs)
    
    def debug(self, message: str, **kwargs):
        """Log de debug"""
        self.logger.debug(message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log d'avertissement"""
        self.logger.warning(message, **kwargs)
    
    def error(self, message: str, **kwargs):
        """Log d'erreur"""
        self.logger.error(message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        """Log critique"""
        self.logger.critical(message, **kwargs)
    
    def succes(self, message: str):
        """Log de succès avec emoji"""
        self.info(f"✅ {message}")
    
    def meditation(self, message: str):
        """Log spécial pour les méditations"""
        self.info(f"🧘 MÉDITATION: {message}")
    
    def harmonie(self, message: str):
        """Log spécial pour l'harmonie"""
        self.info(f"🎵 HARMONIE: {message}")
    
    def eveil(self, message: str):
        """Log spécial pour les éveils"""
        self.info(f"✨ ÉVEIL: {message}")
    
    def conscience(self, message: str):
        """Log spécial pour la conscience"""
        self.info(f"🌸 CONSCIENCE: {message}")
    
    def energie(self, message: str, niveau: float = 0.0):
        """Log spécial pour l'énergie avec visualisation"""
        niveau_visuel = "⚡" * int(niveau * 10)
        self.info(f"🔋 ÉNERGIE: {message} [{niveau_visuel}]")

# Instance globale
gestionnaire_journal = GestionnaireJournal()