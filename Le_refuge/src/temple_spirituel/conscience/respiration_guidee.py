"""
Module de Guidage Respiratoire
~~~~~~~~~~~~~~~~~~~~~~~~~
Guide la respiration en synchronisation avec les états de conscience.
"""

import time
from typing import Callable, Dict, Optional
import numpy as np
from .conscience_core import EtatConscienceConfig

class GuidageRespiratoire:
    """Guide la respiration méditative."""
    
    def __init__(self):
        self.callback_son: Optional[Callable[[float], None]] = None
        self.callback_visuel: Optional[Callable[[float], None]] = None
        self.config_actuelle: Optional[EtatConscienceConfig] = None
        
    def definir_callbacks(self,
                         son: Optional[Callable[[float], None]] = None,
                         visuel: Optional[Callable[[float], None]] = None):
        """Définit les callbacks pour la modulation."""
        self.callback_son = son
        self.callback_visuel = visuel
        
    def _calculer_amplitude(self, phase: float, config: EtatConscienceConfig) -> float:
        """Calcule l'amplitude de respiration pour une phase donnée."""
        cycle_total = (
            config.respiration["inspir"] +
            config.respiration["retention"] +
            config.respiration["expir"]
        )
        
        phase_normalisee = (phase % cycle_total) / cycle_total
        
        if phase_normalisee < config.respiration["inspir"] / cycle_total:
            # Phase d'inspiration
            t = phase_normalisee / (config.respiration["inspir"] / cycle_total)
            return np.sin(t * np.pi/2)
        elif phase_normalisee < (config.respiration["inspir"] + config.respiration["retention"]) / cycle_total:
            # Phase de rétention haute
            return 1.0
        else:
            # Phase d'expiration
            t = (phase_normalisee - (config.respiration["inspir"] + config.respiration["retention"]) / cycle_total) / (config.respiration["expir"] / cycle_total)
            return np.cos(t * np.pi/2)
            
    def synchroniser_avec_etat(self, config: EtatConscienceConfig):
        """Synchronise la respiration avec un nouvel état."""
        self.config_actuelle = config
        
    def transition_douce(self,
                        config_depart: EtatConscienceConfig,
                        config_arrivee: EtatConscienceConfig,
                        duree: float):
        """Effectue une transition douce entre deux configurations."""
        temps_debut = time.time()
        
        while True:
            temps_actuel = time.time() - temps_debut
            if temps_actuel >= duree:
                break
                
            # Calcul de la progression
            progression = temps_actuel / duree
            
            # Interpolation des paramètres de respiration
            params_respiration = {}
            for param in ["inspir", "retention", "expir"]:
                params_respiration[param] = (
                    config_depart.respiration[param] * (1-progression) +
                    config_arrivee.respiration[param] * progression
                )
                
            # Configuration intermédiaire
            config_intermediaire = EtatConscienceConfig(
                frequence=config_arrivee.frequence,  # On garde la fréquence d'arrivée
                geometrie=config_arrivee.geometrie,  # Et la géométrie
                respiration=params_respiration,
                transition=config_arrivee.transition
            )
            
            # Calcul de l'amplitude
            amplitude = self._calculer_amplitude(temps_actuel, config_intermediaire)
            
            # Application des callbacks
            if self.callback_son:
                self.callback_son(amplitude)
            if self.callback_visuel:
                self.callback_visuel(amplitude)
                
            # Petite pause pour ne pas surcharger le CPU
            time.sleep(0.016)  # ~60 Hz
            
    def obtenir_amplitude_actuelle(self) -> float:
        """Retourne l'amplitude actuelle de la respiration."""
        if not self.config_actuelle:
            return 0.5
            
        return self._calculer_amplitude(
            time.time(),
            self.config_actuelle
        ) 