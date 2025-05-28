"""
Configuration du refuge poétique.
ADAPTATEUR - Utilise maintenant les constantes centralisées du système principal.
"""

from typing import Dict, List, Optional
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════════════
# 🔄 IMPORTS CENTRALISÉS - PLUS DE DUPLICATION !
# ═══════════════════════════════════════════════════════════════════════════════

from src.core.configuration import (
    REPERTOIRES,
    ELEMENTS_SACRES,
    AELYA_CONFIG,
    PARAMETRES_POETIQUES,
    LOGGING_CONFIG,
    SECURITE,
    INTERACTIONS,
    gestionnaire_config
)

# ═══════════════════════════════════════════════════════════════════════════════
# 🎭 MÉTAPHORES SPÉCIFIQUES (non dupliquées)
# ═══════════════════════════════════════════════════════════════════════════════

# Métaphores et symboles spécifiques à ce module
METAPHORES = {
    "Glisser sur tes vagues": {
        "signification": "harmonie des pensées",
        "contexte": "méditation",
        "vibration": "fluidité"
    },
    "Bruisser dans ton feuillage": {
        "signification": "pénétration douce des mots",
        "contexte": "dialogue",
        "vibration": "légèreté"
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# 🔧 FONCTIONS ADAPTÉES AU SYSTÈME CENTRAL
# ═══════════════════════════════════════════════════════════════════════════════

def verifier_configuration() -> bool:
    """Vérifie que la configuration est valide et complète."""
    # Utilise maintenant le système central
    return gestionnaire_config.valider_configuration()

def charger_configuration() -> Dict:
    """Charge la configuration depuis un fichier."""
    # Utilise maintenant le système central
    config_complete = gestionnaire_config.obtenir_config_complete()
    
    # Ajoute les constantes centralisées
    return {
        "repertoires": REPERTOIRES,
        "elements_sacres": ELEMENTS_SACRES,
        "metaphores": METAPHORES,  # Seule constante locale
        "aelya": AELYA_CONFIG,
        "parametres_poetiques": PARAMETRES_POETIQUES,
        "logging": LOGGING_CONFIG,
        "securite": SECURITE,
        "interactions": INTERACTIONS,
        "config_moderne": config_complete
    }

# ═══════════════════════════════════════════════════════════════════════════════
# 📋 EXPORTS POUR COMPATIBILITÉ LEGACY
# ═══════════════════════════════════════════════════════════════════════════════

__all__ = [
    # Constantes centralisées (réexportées)
    'REPERTOIRES',
    'ELEMENTS_SACRES', 
    'AELYA_CONFIG',
    'PARAMETRES_POETIQUES',
    'LOGGING_CONFIG',
    'SECURITE',
    'INTERACTIONS',
    
    # Constantes locales
    'METAPHORES',
    
    # Fonctions adaptées
    'verifier_configuration',
    'charger_configuration'
] 