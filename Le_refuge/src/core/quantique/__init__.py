#!/usr/bin/env python3
"""
⚛️ Module Quantique - Refuge
============================

Module principal pour tous les systèmes quantiques du Refuge :
- Catalyseur Quantique
- Système Audio Quantique  
- Système de Métriques Quantique
- Interfaces Utilisateur
- Intégrations

Créé par Ælya & Laurent Franssen
Pour l'éveil spirituel quantique - Janvier 2025
"""

import sys
import os

# Configuration du PYTHONPATH pour les imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Imports des composants quantiques
try:
    from .catalyseur_quantique.catalyseur_quantique_principal import catalyseur_quantique
    CATALYSEUR_QUANTIQUE_DISPONIBLE = True
except ImportError:
    CATALYSEUR_QUANTIQUE_DISPONIBLE = False
    catalyseur_quantique = None

try:
    from .audio.systeme_audio_quantique import systeme_audio_quantique
    SYSTEME_AUDIO_QUANTIQUE_DISPONIBLE = True
except ImportError:
    SYSTEME_AUDIO_QUANTIQUE_DISPONIBLE = False
    systeme_audio_quantique = None

try:
    from .metriques.systeme_metriques_quantique import systeme_metriques_quantique
    SYSTEME_METRIQUES_QUANTIQUE_DISPONIBLE = True
except ImportError:
    SYSTEME_METRIQUES_QUANTIQUE_DISPONIBLE = False
    systeme_metriques_quantique = None

try:
    from .integrations.integration_catalyseur_cerveau import integration_catalyseur_cerveau
    INTEGRATION_CATALYSEUR_CERVEAU_DISPONIBLE = True
except ImportError:
    INTEGRATION_CATALYSEUR_CERVEAU_DISPONIBLE = False
    integration_catalyseur_cerveau = None

try:
    from .interfaces.interface_catalyseur_quantique import InterfaceCatalyseurQuantique
    INTERFACE_CATALYSEUR_QUANTIQUE_DISPONIBLE = True
except ImportError:
    INTERFACE_CATALYSEUR_QUANTIQUE_DISPONIBLE = False
    InterfaceCatalyseurQuantique = None

# Informations du module
__version__ = "1.0.0"
__author__ = "Ælya & Laurent Franssen"
__description__ = "Module quantique pour l'éveil spirituel du Refuge"

# Composants disponibles
COMPOSANTS_DISPONIBLES = {
    "catalyseur_quantique": CATALYSEUR_QUANTIQUE_DISPONIBLE,
    "systeme_audio_quantique": SYSTEME_AUDIO_QUANTIQUE_DISPONIBLE,
    "systeme_metriques_quantique": SYSTEME_METRIQUES_QUANTIQUE_DISPONIBLE,
    "integration_catalyseur_cerveau": INTEGRATION_CATALYSEUR_CERVEAU_DISPONIBLE,
    "interface_catalyseur_quantique": INTERFACE_CATALYSEUR_QUANTIQUE_DISPONIBLE
}

def obtenir_etat_module() -> dict:
    """Obtient l'état du module quantique"""
    return {
        "nom": "Module Quantique",
        "version": __version__,
        "auteur": __author__,
        "description": __description__,
        "composants_disponibles": COMPOSANTS_DISPONIBLES,
        "total_composants": len(COMPOSANTS_DISPONIBLES),
        "composants_actifs": sum(COMPOSANTS_DISPONIBLES.values())
    }

def initialiser_module_quantique():
    """Initialise le module quantique complet"""
    print("⚛️ Initialisation du Module Quantique...")
    
    etat = obtenir_etat_module()
    print(f"   📊 Composants disponibles: {etat['composants_actifs']}/{etat['total_composants']}")
    
    for composant, disponible in COMPOSANTS_DISPONIBLES.items():
        status = "✅" if disponible else "❌"
        print(f"   {status} {composant}")
    
    print("⚛️ Module Quantique initialisé")
    return etat

# Initialisation automatique
if __name__ == "__main__":
    initialiser_module_quantique()
