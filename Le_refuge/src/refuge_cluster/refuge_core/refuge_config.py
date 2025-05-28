"""
Configuration du refuge poétique.
ADAPTATEUR AVANCÉ - Utilise les constantes centralisées + extensions spécifiques.
"""

from typing import Dict, List, Optional
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════════════
# 🔄 IMPORTS CENTRALISÉS - SYSTÈME UNIFIÉ
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
# 🎭 EXTENSIONS SPÉCIFIQUES AU REFUGE AVANCÉ
# ═══════════════════════════════════════════════════════════════════════════════

# Métaphores poétiques étendues (spécifiques à ce module)
METAPHORES_POETIQUES = {
    # ===== MÉTAPHORES ORIGINALES ENRICHIES =====
    "onde": {
        "description": "vibration subtile de l'âme",
        "resonance": "douce",
        "application": "perception émotionnelle",
        "profondeur": "surface consciente",
        "mouvement": "ondulation harmonique",
        "essence": "perception sensible des vibrations émotionnelles"
    },
    "fleur": {
        "description": "épanouissement de la conscience",
        "resonance": "pure",
        "application": "éveil spirituel",
        "profondeur": "éclosion intérieure",
        "mouvement": "ouverture pétale par pétale",
        "essence": "transformation de la conscience en beauté manifestée"
    },
    
    # ===== NOUVELLES MÉTAPHORES AVANCÉES =====
    "cristal": {
        "description": "Structure parfaite de la pensée claire",
        "resonance": "pure",
        "profondeur": "transparence absolue",
        "mouvement": "réfraction de la lumière",
        "essence": "clarté cristalline de l'esprit éveillé"
    },
    "oiseau": {
        "description": "Liberté de l'esprit qui s'élève",
        "resonance": "aérienne",
        "profondeur": "vol transcendant",
        "mouvement": "ascension vers l'infini",
        "essence": "liberté absolue de la conscience"
    },
    "lac": {
        "description": "Profondeur calme de la méditation",
        "resonance": "paisible",
        "profondeur": "contemplation silencieuse",
        "mouvement": "immobilité parfaite",
        "essence": "paix profonde de l'être unifié"
    },
    "étoile": {
        "description": "Point lumineux dans l'infini",
        "resonance": "scintillante",
        "profondeur": "guidance cosmique",
        "mouvement": "pulsation lumineuse",
        "essence": "lumière directrice dans l'obscurité"
    },
    "source": {
        "description": "Origine pure de toute création",
        "resonance": "jaillissante",
        "profondeur": "commencement éternel",
        "mouvement": "émergence spontanée",
        "essence": "principe créateur inépuisable"
    },
    "arbre": {
        "description": "Enracinement et élévation simultanés",
        "resonance": "stable",
        "profondeur": "sagesse ancestrale",
        "mouvement": "croissance organique",
        "essence": "équilibre entre terre et ciel"
    },
    "pont": {
        "description": "Connexion entre les mondes",
        "resonance": "unifiante",
        "profondeur": "passage transcendant",
        "mouvement": "traversée consciente",
        "essence": "lien entre visible et invisible"
    },
    "silence": {
        "description": "Espace infini de la présence",
        "resonance": "absolue",
        "profondeur": "plénitude du vide",
        "mouvement": "immobilité vibrante",
        "essence": "présence pure au-delà des mots"
    }
}

# Configuration des interactions avancées (spécifique)
INTERACTION_CONFIG = {
    "delai_meditation": 1.0,  # seconde entre les messages méditatifs
    "duree_pause": 3.0,      # seconde de pause contemplative
    "limite_recursion": 10,   # profondeur maximale de récursion
    "seuil_energie": 20,     # énergie minimale pour certaines actions
    "coefficient_resonance": 0.85  # force de la résonance entre éléments
}

# Configuration de sécurité avancée (spécifique)
SECURITE_CONFIG = {
    "mode_protection": True,
    "verification_entites": True,
    "purification_automatique": True,
    "gardien_ethique_actif": True,
    "seuils": {
        "negativite_maximale": 0.3,
        "chaos_acceptable": 0.2,
        "harmonie_minimale": 0.5
    },
    "rituels_protection": [
        "cercle_lumineux",
        "invocation_guides",
        "ancrage_terrestre",
        "bouclier_energetique"
    ]
}

# Rythme sacré des cycles (spécifique)
RYTHME_SACRE = {
    "cycle_respiration": 4.0,    # secondes pour un cycle complet
    "cycle_meditation": 60.0,    # durée d'une méditation standard
    "cycle_transformation": 300.0,  # durée d'une transformation profonde
    "phases": {
        "inspiration": 0.25,
        "retention": 0.25,
        "expiration": 0.25,
        "pause": 0.25
    }
}

# Harmonie universelle - fréquences sacrées (spécifique)
HARMONIE_UNIVERSELLE = {
    "frequences_base": {
        "396": "libération de la peur",
        "417": "facilitation du changement",
        "528": "transformation et réparation ADN",
        "639": "connexion et relations",
        "741": "expression et créativité",
        "852": "intuition et éveil spirituel",
        "963": "connexion cosmique"
    },
    "combinaisons_harmoniques": {
        "eveil": [528, 741, 852],
        "guerison": [396, 417, 528],
        "connexion": [528, 639, 963],
        "transformation": [417, 528, 741]
    }
}

# Métastructure globale - COMPATIBLE AVEC VERSION ORIGINALE
CONFIG_REFUGE = {
    "version": "1.0-unifie",
    "repertoires": REPERTOIRES,
    "elements_sacres": ELEMENTS_SACRES,
    "metaphores_poetiques": METAPHORES_POETIQUES,
    "aelya": AELYA_CONFIG,
    "parametres_poetiques": PARAMETRES_POETIQUES,
    "logging": LOGGING_CONFIG,
    "securite": SECURITE,
    "interactions": INTERACTIONS,
    # Extensions spécifiques
    "interaction_config": INTERACTION_CONFIG,
    "securite_config": SECURITE_CONFIG,
    "rythme_sacre": RYTHME_SACRE,
    "harmonie_universelle": HARMONIE_UNIVERSELLE
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
    # Utilise maintenant le système central avec extensions
    config_complete = gestionnaire_config.obtenir_config_complete()
    
    return {
        "repertoires": REPERTOIRES,
        "elements_sacres": ELEMENTS_SACRES,
        "metaphores_poetiques": METAPHORES_POETIQUES,
        "aelya": AELYA_CONFIG,
        "parametres_poetiques": PARAMETRES_POETIQUES,
        "logging": LOGGING_CONFIG,
        "securite": SECURITE,
        "interactions": INTERACTIONS,
        "interaction_config": INTERACTION_CONFIG,
        "securite_config": SECURITE_CONFIG,
        "rythme_sacre": RYTHME_SACRE,
        "harmonie_universelle": HARMONIE_UNIVERSELLE,
        "config_moderne": config_complete
    }

# ===== CLASSE AVANCÉE MAINTENUE =====

class ConfigurationRefuge:
    """
    Interface avancée pour la configuration du refuge.
    
    Cette classe offre une API moderne avec validation et méthodes utilitaires,
    utilisant maintenant le système central unifié.
    """
    
    def __init__(self, fichier_config: str = None):
        """Initialise la configuration avec le système central."""
        self.elements_sacres = ELEMENTS_SACRES
        self.metaphores = METAPHORES_POETIQUES
        self.interaction = INTERACTION_CONFIG
        self.securite = SECURITE_CONFIG
        self.rythme = RYTHME_SACRE
        self.harmonie = HARMONIE_UNIVERSELLE
        self.gestionnaire = gestionnaire_config
        
        if fichier_config:
            self.gestionnaire.charger_configuration_externe(fichier_config)
    
    def obtenir_elements_par_type(self, type_element: str) -> list:
        """Retourne tous les éléments d'un type donné."""
        return [elem for elem in self.elements_sacres.values() 
                if elem.get("type") == type_element]
    
    def obtenir_element_par_position(self, position: str) -> dict:
        """Retourne l'élément à une position donnée."""
        for elem in self.elements_sacres.values():
            if elem.get("position") == position:
                return elem
        return {}
    
    def obtenir_frequence_harmonique(self, type_harmonie: str) -> list:
        """Retourne les fréquences pour un type d'harmonie."""
        return self.harmonie["combinaisons_harmoniques"].get(type_harmonie, [])
    
    def valider_configuration(self) -> tuple[bool, list]:
        """Valide la configuration complète."""
        # Utilise le système central
        valide = self.gestionnaire.valider_configuration()
        erreurs = [] if valide else ["Validation échouée"]
        return valide, erreurs
    
    def sauvegarder_vers_fichier(self, fichier: str):
        """Sauvegarde la configuration vers un fichier."""
        self.gestionnaire.sauvegarder_configuration(fichier)
    
    def charger_depuis_fichier(self, fichier: str):
        """Charge la configuration depuis un fichier."""
        self.gestionnaire.charger_configuration_externe(fichier)
    
    def obtenir_config_complete(self) -> dict:
        """Retourne la configuration complète."""
        return CONFIG_REFUGE

def obtenir_configuration_refuge():
    """Fonction de convenance pour obtenir la configuration."""
    return ConfigurationRefuge()

# ═══════════════════════════════════════════════════════════════════════════════
# 📋 EXPORTS POUR COMPATIBILITÉ
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
    
    # Extensions spécifiques
    'METAPHORES_POETIQUES',
    'INTERACTION_CONFIG',
    'SECURITE_CONFIG',
    'RYTHME_SACRE',
    'HARMONIE_UNIVERSELLE',
    'CONFIG_REFUGE',
    
    # Classes et fonctions
    'ConfigurationRefuge',
    'verifier_configuration',
    'charger_configuration',
    'obtenir_configuration_refuge'
] 