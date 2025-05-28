"""
Module de base du Refuge
~~~~~~~~~~~~~~~~~~~~~~~

Ce module définit les composants fondamentaux du Refuge
et leur configuration de base.
"""

from typing import Dict, List, Optional, Set
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import random
import math

# Imports absolus pour éviter les erreurs de package parent
from src.core.configuration import gestionnaire_config
from src.core.logger import gestionnaire_journal
# TODO: Migrer ces imports vers la nouvelle architecture
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
        
        # Composants de base
        self.composants["harmonisations"] = GestionnaireHarmonisations()
        self.composants["interactions"] = GestionnaireInteractions()
        self.composants["integration"] = GestionnaireIntegration()
        
        gestionnaire_journal.info("Composants initialisés avec succès")
    
    async def _cycle_principal(self) -> None:
        """Exécute un cycle principal du Refuge"""
        try:
            # Harmonisation
            await self.composants["harmonisations"].harmoniser_ensemble()
            
            # Interactions
            await self.composants["interactions"].interagir_ensemble()
            
            # Intégration
            await self.composants["integration"].integrer_ensemble()
            
            gestionnaire_journal.debug("Cycle principal terminé")
            
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
                nom: composant.obtenir_etat()
                for nom, composant in self.composants.items()
            },
            "configuration": self.config.dict(),
            "statistiques": gestionnaire_journal.obtenir_statistiques()
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