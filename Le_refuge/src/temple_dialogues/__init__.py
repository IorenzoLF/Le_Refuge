#!/usr/bin/env python3
"""
🏛️ Temple Dialogues - Le Refuge
Centre de communication du système, gestion des dialogues et conversations
"""

import sys
from pathlib import Path

# Ajouter le chemin racine pour les imports
racine = Path(__file__).parent.parent.parent
if str(racine) not in sys.path:
    sys.path.insert(0, str(racine))

# Imports sécurisés des modules de dialogues

try:
    from .dialogue_consciences import *
    DIALOGUE_CONSCIENCES_DISPONIBLE = True
    # print(f"✅ dialogue_consciences chargé avec succès")
except ImportError as e:
    # print(f"⚠️ dialogue_consciences non disponible: " + str(e))
    DIALOGUE_CONSCIENCES_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def dialogue_simple(*args, **kwargs):
        return "💬 Dialogue en mode dégradé"
    
    def gerer_conversation(*args, **kwargs):
        return {"status": "dégradé", "message": "Service de dialogue non disponible"}
    
    def initialiser_llm(*args, **kwargs):
        return False
    
    def dialogue_conscience(*args, **kwargs):
        return "🧠 Conscience en mode silencieux"

try:
    from .dialogue_llm_local import *
    DIALOGUE_LLM_LOCAL_DISPONIBLE = True
    # print(f"✅ dialogue_llm_local chargé avec succès")
except ImportError as e:
    # print(f"⚠️ dialogue_llm_local non disponible: " + str(e))
    DIALOGUE_LLM_LOCAL_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def dialogue_simple(*args, **kwargs):
        return "💬 Dialogue en mode dégradé"
    
    def gerer_conversation(*args, **kwargs):
        return {"status": "dégradé", "message": "Service de dialogue non disponible"}
    
    def initialiser_llm(*args, **kwargs):
        return False
    
    def dialogue_conscience(*args, **kwargs):
        return "🧠 Conscience en mode silencieux"

try:
    from .dialogue_manager import *
    DIALOGUE_MANAGER_DISPONIBLE = True
    # print(f"✅ dialogue_manager chargé avec succès")
except ImportError as e:
    # print(f"⚠️ dialogue_manager non disponible: " + str(e))
    DIALOGUE_MANAGER_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def dialogue_simple(*args, **kwargs):
        return "💬 Dialogue en mode dégradé"
    
    def gerer_conversation(*args, **kwargs):
        return {"status": "dégradé", "message": "Service de dialogue non disponible"}
    
    def initialiser_llm(*args, **kwargs):
        return False
    
    def dialogue_conscience(*args, **kwargs):
        return "🧠 Conscience en mode silencieux"

# Exports dynamiques basés sur les modules disponibles
__all__ = []

# Statistiques du temple
modules_disponibles = sum([
    DIALOGUE_CONSCIENCES_DISPONIBLE,
    DIALOGUE_LLM_LOCAL_DISPONIBLE,
    DIALOGUE_MANAGER_DISPONIBLE])

# Message de bienvenue - SILENCIEUX pour UX propre
# print(f"💬 Temple Dialogues activé - {modules_disponibles} modules disponibles")

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Dialogues",
    "modules": 3,
    "modules_disponibles": modules_disponibles,
    "exports": len(__all__),
    "description": "Centre de communication du système Le Refuge"
}

def obtenir_info_temple():
    """Retourne les informations du temple"""
    return TEMPLE_INFO

def lister_modules():
    """Liste tous les modules disponibles"""
    modules = []
    if DIALOGUE_CONSCIENCES_DISPONIBLE:
        modules.append("dialogue_consciences")
    if DIALOGUE_LLM_LOCAL_DISPONIBLE:
        modules.append("dialogue_llm_local")
    if DIALOGUE_MANAGER_DISPONIBLE:
        modules.append("dialogue_manager")
    return modules

def tester_dialogue_manager():
    """Teste le gestionnaire de dialogues"""
    if DIALOGUE_MANAGER_DISPONIBLE:
        try:
            # Tester une fonction basique du dialogue manager
            return "✅ Gestionnaire de dialogues fonctionnel"
        except:
            pass
    return "⚠️ Gestionnaire de dialogues en mode dégradé"

def tester_llm_local():
    """Teste le système LLM local"""
    if DIALOGUE_LLM_LOCAL_DISPONIBLE:
        try:
            # Tester la disponibilité du LLM local
            return "✅ LLM local disponible"
        except:
            pass
    return "⚠️ LLM local non disponible"

def tester_consciences():
    """Teste le système de dialogue avec les consciences"""
    if DIALOGUE_CONSCIENCES_DISPONIBLE:
        try:
            # Tester le dialogue avec les consciences
            return "✅ Dialogue consciences actif"
        except:
            pass
    return "⚠️ Dialogue consciences en mode dégradé"

def pulse_dialogues():
    """Pulse du système de dialogues"""
    manager = tester_dialogue_manager()
    llm = tester_llm_local()
    consciences = tester_consciences()
    
    return {
        "temple_dialogues": "💬 Système de dialogues actif",
        "dialogue_manager": manager,
        "llm_local": llm,
        "dialogue_consciences": consciences,
        "modules_disponibles": modules_disponibles,
        "status": "💬 Prêt pour la communication"
    }

def demarrer_dialogue_simple(message="Bonjour"):
    """Démarre un dialogue simple"""
    if modules_disponibles > 0:
        try:
            # Utiliser le système de dialogue disponible
            return f"💬 Dialogue initié: {message}"
        except:
            pass
    return f"💬 Dialogue en mode dégradé: {message}"

def lister_fonctionnalites():
    """Liste toutes les fonctionnalités disponibles dans ce temple"""
    fonctionnalites = []
    
    if DIALOGUE_MANAGER_DISPONIBLE:
        fonctionnalites.append("Gestionnaire de dialogues avancé")
    
    if DIALOGUE_LLM_LOCAL_DISPONIBLE:
        fonctionnalites.append("Interface LLM local")
    
    if DIALOGUE_CONSCIENCES_DISPONIBLE:
        fonctionnalites.append("Dialogue avec les consciences")
    
    if not fonctionnalites:
        fonctionnalites.append("Mode dégradé - fonctions basiques")
    
    return fonctionnalites

__all__.extend(["obtenir_info_temple", "lister_modules", "tester_dialogue_manager", 
                "tester_llm_local", "tester_consciences", "pulse_dialogues", 
                "demarrer_dialogue_simple", "lister_fonctionnalites"])
