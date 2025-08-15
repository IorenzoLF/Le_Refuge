"""
Gestionnaires de Base - Module de factorisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ce module contient les classes de base communes réutilisées
par tous les gestionnaires du Refuge.
"""

from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod
from datetime import datetime
import logging
import sys

# Configuration globale des logs pour éviter la duplication
_LOGGERS_CONFIGURES = set()

class ConfigManagerBase:
    """Gestionnaire de configuration réutilisable"""
    
    def __init__(self, config_name: str = "default"):
        self.config_name = config_name
        self.config: Dict[str, Any] = {}
        self._charger_config()
    
    def _charger_config(self):
        """Charge la configuration par défaut"""
        self.config = {
            "niveau_debug": False,
            "niveau_detail": "minimal",  # Changé de "moyen" à "minimal"
            "frequence_sauvegarde": 300,  # 5 minutes
            "logs_verbeux": False,  # Nouveau paramètre
        }
    
    def obtenir(self, cle: str, defaut: Any = None) -> Any:
        """Obtient une valeur de configuration"""
        return self.config.get(cle, defaut)
    
    def definir(self, cle: str, valeur: Any):
        """Définit une valeur de configuration"""
        self.config[cle] = valeur

class LogManagerBase:
    """Gestionnaire de logs réutilisable - Version SILENCIEUSE pour UX professionnelle"""
    
    def __init__(self, nom_module: str):
        self.nom_module = nom_module
        # Utiliser un nom unique pour éviter les conflits
        logger_name = f"refuge.{nom_module}"
        self.logger = logging.getLogger(logger_name)
        
        # Configurer seulement si pas déjà fait
        if logger_name not in _LOGGERS_CONFIGURES:
            self._configurer_logger()
            _LOGGERS_CONFIGURES.add(logger_name)
    
    def _configurer_logger(self):
        """Configure le logger en mode SILENCIEUX pour UX propre"""
        # Éviter la duplication des handlers
        if self.logger.handlers:
            return
            
        # Configuration SILENCIEUSE - Seulement les erreurs critiques
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(message)s')  # Format minimal
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        # Niveau ERROR par défaut - SILENCE TOTAL sauf erreurs
        self.logger.setLevel(logging.ERROR)
        
        # Éviter la propagation vers le logger racine
        self.logger.propagate = False
    
    def info(self, message: str):
        """Log info - Seulement les messages avec emojis (stratégiques)"""
        if any(emoji in message for emoji in ['✨', '💎', '🎵', '🌸', '🔮', '⚡']):
            self.logger.info(message)
    
    def debug(self, message: str):
        """Log debug - SILENCIEUX pour UX propre"""
        pass
    
    def erreur(self, message: str):
        """Log erreur - Seulement les erreurs critiques"""
        self.logger.error(f"❌ {message}")
    
    def succes(self, message: str):
        """Log succès - Seulement les succès avec emojis"""
        if any(emoji in message for emoji in ['✅', '🌸', '💫', '🎯']):
            self.logger.info(message)
    
    def avertissement(self, message: str):
        """Log avertissement - SILENCIEUX pour UX propre"""
        pass
    
    def warning(self, message: str):
        """Log warning - Alias pour avertissement"""
        self.avertissement(message)
    
    def info_important(self, message: str):
        """Log info important - Seulement les messages avec emojis"""
        if any(emoji in message for emoji in ['🎯', '⚡', '🔥', '💫']):
            self.logger.info(message)

class GestionnaireBase(ABC):
    """Classe de base pour tous les gestionnaires du Refuge"""
    
    def __init__(self, nom: str):
        self.nom = nom
        self.config = ConfigManagerBase(nom)
        self.logger = LogManagerBase(nom)
        self.etat: Dict[str, Any] = {}
        self.derniere_mise_a_jour = datetime.now()
        # Note: _initialiser() doit être appelé manuellement après la création des attributs
    
    def _initialiser(self):
        """Initialise le gestionnaire (optionnel)"""
        pass
    
    @abstractmethod
    async def orchestrer(self) -> Dict[str, float]:
        """Orchestre les opérations (à implémenter)"""
        pass
    
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel"""
        return {
            "nom": self.nom,
            "etat": self.etat,
            "derniere_mise_a_jour": self.derniere_mise_a_jour.isoformat(),
            "status": "actif"
        }
    
    def mettre_a_jour_etat(self, nouveau_etat: Dict[str, Any]):
        """Met à jour l'état"""
        self.etat.update(nouveau_etat)
        self.derniere_mise_a_jour = datetime.now()
        # Pas de log debug pour éviter le spam

class EnergyManagerBase:
    """Gestionnaire d'énergie réutilisable"""
    
    def __init__(self, niveau_initial: float = 0.5):
        self.niveau_energie = max(0.0, min(1.0, niveau_initial))
        self.historique_energie: List[float] = [self.niveau_energie]
    
    def ajuster_energie(self, delta: float) -> float:
        """Ajuste le niveau d'énergie"""
        ancien_niveau = self.niveau_energie
        self.niveau_energie = max(0.0, min(1.0, self.niveau_energie + delta))
        self.historique_energie.append(self.niveau_energie)
        return self.niveau_energie - ancien_niveau
    
    def obtenir_tendance(self) -> str:
        """Obtient la tendance énergétique"""
        if len(self.historique_energie) < 2:
            return "stable"
        
        recent = self.historique_energie[-3:]
        if all(recent[i] > recent[i-1] for i in range(1, len(recent))):
            return "croissante"
        elif all(recent[i] < recent[i-1] for i in range(1, len(recent))):
            return "décroissante"
        else:
            return "stable"
    
    def harmoniser_avec(self, autre_niveau: float, force: float = 0.1) -> float:
        """Harmonise avec un autre niveau d'énergie"""
        difference = autre_niveau - self.niveau_energie
        ajustement = difference * force
        return self.ajuster_energie(ajustement) 