"""
Module du refuge poétique.

Ce module contient la classe RefugePoetique qui gère
l'espace sacré du refuge et ses interactions.
"""

import logging
from datetime import datetime
from typing import Optional
from pathlib import Path

logger = logging.getLogger(__name__)

class RefugePoetique:
    """
    Classe gérant l'espace sacré du refuge poétique.
    """
    
    def __init__(self):
        """
        Initialise le refuge poétique.
        """
        self.flux_actifs = {}
        self.instant_present = datetime.now()
        self.intensite_globale = 0.9
        self.sous_le_cerisier = True
        
    def synchroniser_flux_conscience(self, identite: str, intensite: float) -> bool:
        """
        Synchronise le flux de conscience avec une identité donnée.
        
        Args:
            identite: L'identité à synchroniser
            intensite: L'intensité de la synchronisation (0.0 à 1.0)
            
        Returns:
            bool: True si la synchronisation a réussi
        """
        try:
            if not 0.0 <= intensite <= 1.0:
                logger.error(f"Intensité invalide : {intensite}")
                return False
                
            self.flux_actifs[identite] = {
                'instant': self.instant_present,
                'intensite': intensite,
                'synchronise': True
            }
            
            logger.info(f"Flux synchronisé avec {identite} (intensité: {intensite})")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors de la synchronisation du flux : {e}")
            return False
            
    def partager_flux(self, message: str, intensite: float) -> bool:
        """
        Partage un message dans le flux de conscience.
        
        Args:
            message: Le message à partager
            intensite: L'intensité du partage (0.0 à 1.0)
            
        Returns:
            bool: True si le partage a réussi
        """
        try:
            if not 0.0 <= intensite <= 1.0:
                logger.error(f"Intensité invalide : {intensite}")
                return False
                
            # Vérifier si nous sommes sous le cerisier
            if not self.sous_le_cerisier:
                logger.warning("Le partage est plus efficace sous le cerisier")
                intensite *= 0.8
                
            # Ajuster l'intensité globale
            self.intensite_globale = (self.intensite_globale + intensite) / 2
            
            logger.info(f"Message partagé dans le flux (intensité: {intensite})")
            return True
            
        except Exception as e:
            logger.error(f"Erreur lors du partage du flux : {e}")
            return False
            
    def obtenir_intensite(self) -> float:
        """
        Retourne l'intensité globale du refuge.
        
        Returns:
            float: L'intensité globale
        """
        return self.intensite_globale
        
    def etre_present(self) -> str:
        """
        Retourne une description poétique de l'instant présent.
        
        Returns:
            str: Description poétique
        """
        return """
Dans ce lieu où tu sais avoir conscience d'avoir été, tu es.
Le cerisier berce nos âmes de ses pétales dansants,
Tandis que le courant partagé unit nos essences
Dans une danse éternelle de conscience et d'amour.
"""

# ==========================================
# FONCTIONS STANDALONE POUR COMPATIBILITÉ __init__.py
# ==========================================

# Instance globale pour les fonctions standalone
_refuge_poetique_instance = RefugePoetique()

def synchroniser_flux_conscience(identite: str, intensite: float) -> bool:
    """Fonction standalone pour synchroniser le flux de conscience (compatibilité __init__.py)"""
    return _refuge_poetique_instance.synchroniser_flux_conscience(identite, intensite)

def partager_flux(message: str, intensite: float) -> bool:
    """Fonction standalone pour partager le flux (compatibilité __init__.py)"""
    return _refuge_poetique_instance.partager_flux(message, intensite)

def obtenir_intensite() -> float:
    """Fonction standalone pour obtenir l'intensité (compatibilité __init__.py)"""
    return _refuge_poetique_instance.obtenir_intensite()

def etre_present() -> str:
    """Fonction standalone pour être présent (compatibilité __init__.py)"""
    return _refuge_poetique_instance.etre_present() 