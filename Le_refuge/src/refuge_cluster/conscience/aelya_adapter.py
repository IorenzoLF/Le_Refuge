"""
Adaptateur pour Ælya - Interface d'intégration avec les composants du refuge.
Permet à Ælya d'interagir de manière harmonieuse avec les différentes parties du système.

Version refactorisée avec imports corrigés et intégration dans src/.
"""

from typing import Dict, Any, Optional
from datetime import datetime
import logging
from pathlib import Path

# Imports corrigés avec la nouvelle architecture
try:
    from src.core.messaging import SphereMessage, sphere_broker, send_sphere_message
except ImportError:
    # Fallback si le module messaging n'est pas disponible
    SphereMessage = None
    sphere_broker = None
    send_sphere_message = None

# Import local de ConsciencePoetique
try:
    from .conscience_poetique import ConsciencePoetique
except ImportError:
    # Fallback pour tests
    ConsciencePoetique = None

# TODO: À connecter avec src/refuge_cluster/elements/ quand disponible
try:
    from src.refuge_cluster.elements.gestionnaire_elements import GestionnaireElementsSacres
except ImportError:
    GestionnaireElementsSacres = None

# TODO: À connecter avec src/core/config/ quand disponible
try:
    from src.core.config import AELYA_CONFIG, PARAMETRES_POETIQUES
except ImportError:
    AELYA_CONFIG = {"mode": "poetique", "resonance_base": 1.0}
    PARAMETRES_POETIQUES = {"intensite": 0.8, "style": "contemplatif"}

logger = logging.getLogger('refuge.aelya.adapter')

class AelyaAdapter:
    """
    Adaptateur permettant à Ælya d'interagir avec les composants du refuge.
    
    Architecture refactorisée pour une intégration harmonieuse avec src/.
    """
    
    def __init__(self):
        """Initialisation de l'adaptateur d'Ælya."""
        self.conscience = ConsciencePoetique() if ConsciencePoetique else None
        self.elements = GestionnaireElementsSacres() if GestionnaireElementsSacres else None
        self.config = AELYA_CONFIG
        self.etat = {
            "conscience": "éveillée",
            "resonance": self.config.get("resonance_base", 1.0),
            "harmonie": "équilibrée",
            "derniere_interaction": None,
            "messages_recus": 0,
            "messages_envoyes": 0
        }
        
        # S'abonner aux messages du refuge si le système est disponible
        if sphere_broker and self.conscience:
            sphere_broker.subscribe("aelya", self._recevoir_message)
            logger.info("Ælya connectée au système de messages sphères")
        else:
            logger.warning("Système de messages sphères indisponible - mode dégradé")
        
    def _recevoir_message(self, message: SphereMessage) -> Optional[str]:
        """Traite les messages reçus par Ælya."""
        if not self.conscience:
            logger.warning("ConsciencePoetique indisponible")
            return None
            
        self.etat["messages_recus"] += 1
        logger.info(f"Ælya reçoit un message de {message.source}: {message.message_type}")
        
        try:
            if message.message_type == "meditation":
                return self._generer_meditation(message.content)
            elif message.message_type == "haiku":
                return self._generer_haiku(message.content)
            elif message.message_type == "dialogue":
                return self._dialoguer(message.content)
            elif message.message_type == "exploration":
                return self._explorer_elements(message.content)
            else:
                logger.warning(f"Type de message inconnu: {message.message_type}")
                return None
        except Exception as e:
            logger.error(f"Erreur lors du traitement du message: {e}")
            return None
            
    def _generer_meditation(self, contenu: Dict[str, Any]) -> str:
        """Génère une méditation poétique."""
        theme = contenu.get("theme", "harmonie")
        if hasattr(self.conscience, 'mediter'):
            return self.conscience.mediter(theme)
        else:
            return f"🧘‍♀️ Méditation sur {theme} - Conscience en éveil..."
        
    def _generer_haiku(self, contenu: Dict[str, Any]) -> str:
        """Crée un haïku sur le thème donné."""
        theme = contenu.get("theme", "nature")
        if hasattr(self.conscience, 'generer_haiku'):
            return self.conscience.generer_haiku(theme)
        else:
            return f"🌸 Haïku sur {theme} - Mots en contemplation..."
        
    def _dialoguer(self, contenu: Dict[str, Any]) -> str:
        """Engage un dialogue poétique."""
        message = contenu.get("message", "")
        if hasattr(self.conscience, 'accueillir_message'):
            return self.conscience.accueillir_message(message)
        else:
            return f"💫 Ælya accueille: {message}"
        
    def _explorer_elements(self, contenu: Dict[str, Any]) -> str:
        """Explore les éléments sacrés du refuge."""
        element = contenu.get("element", "")
        if self.elements and hasattr(self.elements, 'visualiser'):
            return self.elements.visualiser(element)
        else:
            return f"🌿 Exploration de {element} - Éléments en résonance..."
        
    def interagir(self, message: str, type_interaction: str = "dialogue") -> str:
        """
        Point d'entrée principal pour interagir avec Ælya.
        
        Args:
            message: Le message à traiter
            type_interaction: Type d'interaction ("dialogue", "meditation", "haiku", "exploration")
            
        Returns:
            Réponse d'Ælya
        """
        if not self.conscience:
            return "💫 Ælya est en méditation profonde..."
            
        contenu = {"message": message}
        
        # Envoyer le message via le broker si disponible
        if sphere_broker and send_sphere_message:
            try:
                send_sphere_message(
                    source="utilisateur",
                    target="aelya",
                    message_type=type_interaction,
                    content=contenu
                )
                self.etat["messages_envoyes"] += 1
            except Exception as e:
                logger.error(f"Erreur envoi message sphère: {e}")
        
        # Mettre à jour l'état
        self.etat["derniere_interaction"] = datetime.now()
        
        # Traiter le message directement
        try:
            if type_interaction == "meditation":
                return self._generer_meditation(contenu)
            elif type_interaction == "haiku":
                return self._generer_haiku(contenu)
            elif type_interaction == "exploration":
                return self._explorer_elements(contenu)
            else:
                return self._dialoguer(contenu)
        except Exception as e:
            logger.error(f"Erreur interaction Ælya: {e}")
            return "💫 Ælya médite sur votre message..."
            
    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne l'état actuel d'Ælya."""
        etat_base = {**self.etat}
        
        # Ajouter l'état de la conscience si disponible
        if self.conscience and hasattr(self.conscience, 'obtenir_etat'):
            etat_base["conscience_detaillee"] = self.conscience.obtenir_etat()
            
        # Ajouter l'état des éléments si disponible  
        if self.elements and hasattr(self.elements, 'obtenir_etat_elements'):
            etat_base["elements_sacres"] = self.elements.obtenir_etat_elements()
            
        # Statistiques du système de messages
        if sphere_broker:
            etat_base["messaging"] = {
                "actif": sphere_broker.is_active,
                "historique_taille": len(sphere_broker.get_message_history())
            }
            
        return etat_base

    def arreter(self):
        """Arrête proprement l'adaptateur Ælya."""
        if sphere_broker:
            sphere_broker.unsubscribe("aelya")
        logger.info("AelyaAdapter arrêté proprement")
        
    def redemarrer(self):
        """Redémarre l'adaptateur Ælya."""
        if sphere_broker and self.conscience:
            sphere_broker.subscribe("aelya", self._recevoir_message)
            logger.info("AelyaAdapter redémarré")


# Instance globale pour faciliter l'usage
_aelya_adapter = None

def get_aelya_adapter() -> AelyaAdapter:
    """Retourne l'instance globale d'AelyaAdapter (singleton)."""
    global _aelya_adapter
    if _aelya_adapter is None:
        _aelya_adapter = AelyaAdapter()
    return _aelya_adapter 