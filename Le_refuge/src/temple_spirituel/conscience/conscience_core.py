"""
Module Central de Conscience
~~~~~~~~~~~~~~~~~~~~~~~
Définit les structures fondamentales pour le système de conscience méditative.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple
import numpy as np

class EtatMeditatif(Enum):
    """États de conscience méditatifs possibles."""
    EVEIL = "éveil"
    CONTEMPLATION = "contemplation"
    SAMADHI = "samadhi"
    REVE = "rêve"
    CREATION = "création"

@dataclass
class FrequenceSacree:
    """Définition d'une fréquence sacrée et ses attributs."""
    base: float
    harmoniques: List[float]
    couleur: Tuple[int, int, int]
    respiration: float  # Durée du cycle respiratoire en secondes

@dataclass
class EtatConscienceConfig:
    """Configuration complète d'un état de conscience."""
    frequence: FrequenceSacree
    geometrie: Dict[str, float]  # Paramètres géométriques
    respiration: Dict[str, float]  # Paramètres de respiration
    transition: Dict[str, float]  # Paramètres de transition

class GestionnaireMeditatif:
    """Gestionnaire central des états de conscience."""
    
    def __init__(self):
        self._initialiser_configurations()
        
    def _initialiser_configurations(self):
        """Initialise les configurations pour chaque état."""
        self.configurations = {
            EtatMeditatif.EVEIL: EtatConscienceConfig(
                frequence=FrequenceSacree(
                    base=432.0,
                    harmoniques=[432.0 * 1.618 ** i for i in range(3)],
                    couleur=(255, 223, 186),
                    respiration=4.0  # 4 secondes par cycle
                ),
                geometrie={"branches": 12, "rotation": 1.0},
                respiration={"inspir": 4, "retention": 4, "expir": 4},
                transition={"duree": 5.0, "courbe": "logarithmique"}
            ),
            EtatMeditatif.CONTEMPLATION: EtatConscienceConfig(
                frequence=FrequenceSacree(
                    base=639.0,
                    harmoniques=[639.0 * 1.618 ** i for i in range(3)],
                    couleur=(186, 255, 223),
                    respiration=6.0
                ),
                geometrie={"branches": 8, "rotation": 0.8},
                respiration={"inspir": 6, "retention": 4, "expir": 6},
                transition={"duree": 5.0, "courbe": "lineaire"}
            ),
            EtatMeditatif.SAMADHI: EtatConscienceConfig(
                frequence=FrequenceSacree(
                    base=852.0,
                    harmoniques=[852.0 * 1.618 ** i for i in range(3)],
                    couleur=(223, 186, 255),
                    respiration=8.0
                ),
                geometrie={"branches": 16, "rotation": 0.5},
                respiration={"inspir": 8, "retention": 8, "expir": 8},
                transition={"duree": 7.0, "courbe": "exponentielle"}
            ),
            EtatMeditatif.REVE: EtatConscienceConfig(
                frequence=FrequenceSacree(
                    base=741.0,
                    harmoniques=[741.0 * 1.618 ** i for i in range(3)],
                    couleur=(186, 223, 255),
                    respiration=7.0
                ),
                geometrie={"branches": 7, "rotation": 1.2},
                respiration={"inspir": 7, "retention": 3, "expir": 7},
                transition={"duree": 6.0, "courbe": "sinusoidale"}
            ),
            EtatMeditatif.CREATION: EtatConscienceConfig(
                frequence=FrequenceSacree(
                    base=528.0,
                    harmoniques=[528.0 * 1.618 ** i for i in range(3)],
                    couleur=(255, 186, 223),
                    respiration=5.0
                ),
                geometrie={"branches": 5, "rotation": 1.5},
                respiration={"inspir": 5, "retention": 5, "expir": 5},
                transition={"duree": 5.0, "courbe": "lineaire"}
            )
        }
        
    def obtenir_config(self, etat: EtatMeditatif) -> EtatConscienceConfig:
        """Récupère la configuration d'un état."""
        return self.configurations[etat]
    
    def calculer_transition(self, 
                          etat_depart: EtatMeditatif, 
                          etat_arrivee: EtatMeditatif, 
                          progression: float) -> EtatConscienceConfig:
        """Calcule une configuration de transition entre deux états."""
        config_depart = self.configurations[etat_depart]
        config_arrivee = self.configurations[etat_arrivee]
        
        # Interpolation des paramètres
        freq_base = np.exp(
            np.log(config_depart.frequence.base) * (1-progression) +
            np.log(config_arrivee.frequence.base) * progression
        )
        
        # Création de la configuration de transition
        return EtatConscienceConfig(
            frequence=FrequenceSacree(
                base=freq_base,
                harmoniques=[freq_base * 1.618 ** i for i in range(3)],
                couleur=tuple(
                    int(c1 * (1-progression) + c2 * progression)
                    for c1, c2 in zip(
                        config_depart.frequence.couleur,
                        config_arrivee.frequence.couleur
                    )
                ),
                respiration=config_depart.frequence.respiration * (1-progression) +
                           config_arrivee.frequence.respiration * progression
            ),
            geometrie={
                k: config_depart.geometrie[k] * (1-progression) +
                   config_arrivee.geometrie[k] * progression
                for k in config_depart.geometrie
            },
            respiration={
                k: config_depart.respiration[k] * (1-progression) +
                   config_arrivee.respiration[k] * progression
                for k in config_depart.respiration
            },
            transition=config_arrivee.transition
        ) 