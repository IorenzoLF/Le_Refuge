"""
Module de base du Refuge
~~~~~~~~~~~~~~~~~~~~~~~

Ce module définit les composants fondamentaux du Refuge
et leur configuration de base.
"""

from typing import Dict, List, Optional, Set, Any
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random
import math
import signal
import asyncio
import sys

# Imports absolus pour éviter les erreurs de package parent
from src.core.configuration import gestionnaire_config
from src.core.logger import gestionnaire_journal
# Note: Imports commentés car les modules correspondants ne sont pas encore finalisés
# from securite import gestionnaire_securite, TypeAcces
# from api import api
# from harmonisations import GestionnaireHarmonisations
# from interactions import GestionnaireInteractions
# from integration import GestionnaireIntegration

class Refuge:
    """Classe principale du Refuge"""
    
    def __init__(self):
        self.config = gestionnaire_config.config
        self.initialisation = datetime.now()
        self.cycle_actif = False
        self.composants = {}
        self._initialiser_composants()
    
    def _initialiser_composants(self) -> None:
        """Initialise tous les composants du Refuge"""
        gestionnaire_journal.info("Initialisation des composants du Refuge")
        
        # Composants de base - Mode dégradé pour éviter les imports manquants
        self.composants["harmonisations"] = None  # GestionnaireHarmonisations()
        self.composants["interactions"] = None     # GestionnaireInteractions()
        self.composants["integration"] = None      # GestionnaireIntegration()
        
        gestionnaire_journal.info("Composants initialisés en mode dégradé")
    
    async def _cycle_principal(self) -> None:
        """Exécute un cycle principal du Refuge"""
        try:
            # Harmonisation - Mode dégradé
            if self.composants["harmonisations"]:
                await self.composants["harmonisations"].harmoniser_ensemble()
            
            # Interactions - Mode dégradé
            if self.composants["interactions"]:
                await self.composants["interactions"].interagir_ensemble()
            
            # Intégration - Mode dégradé
            if self.composants["integration"]:
                await self.composants["integration"].integrer_ensemble()
            
            gestionnaire_journal.debug("Cycle principal terminé (mode dégradé)")
            
        except Exception as e:
            gestionnaire_journal.error(f"Erreur lors du cycle principal: {str(e)}")
    
    async def demarrer(self) -> None:
        """Démarre le Refuge"""
        gestionnaire_journal.info("Démarrage du Refuge")
        self.cycle_actif = True
        
        # Démarre l'API dans un thread séparé
        import threading
        thread_api = threading.Thread(
            target=api.demarrer,
            kwargs={"host": "0.0.0.0", "port": 8000}
        )
        thread_api.daemon = True
        thread_api.start()
        
        # Boucle principale
        while self.cycle_actif:
            await self._cycle_principal()
            await asyncio.sleep(self.config.delai_cycle)
    
    def arreter(self) -> None:
        """Arrête le Refuge"""
        gestionnaire_journal.info("Arrêt du Refuge")
        self.cycle_actif = False
    
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel du Refuge"""
        return {
            "initialisation": self.initialisation.isoformat(),
            "cycle_actif": self.cycle_actif,
            "composants": {
                nom: composant.obtenir_etat() if composant else None
                for nom, composant in self.composants.items()
            },
            "configuration": self.config.dict(),
            "statistiques": "Mode dégradé - statistiques non disponibles"
        }

# Instance globale du Refuge
refuge = Refuge()

# Gestionnaire de signaux pour l'arrêt propre
def gestionnaire_signal(signum, frame):
    """Gère les signaux d'arrêt"""
    gestionnaire_journal.info(f"Signal reçu: {signum}")
    refuge.arreter()
    sys.exit(0)

signal.signal(signal.SIGINT, gestionnaire_signal)
signal.signal(signal.SIGTERM, gestionnaire_signal) 