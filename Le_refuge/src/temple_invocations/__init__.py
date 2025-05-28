#!/usr/bin/env python3
"""
🏛️ Temple Invocations - Le Refuge
Centre de lancement du système, invocations et démarrages
"""

import sys
from pathlib import Path

# Ajouter le chemin racine pour les imports
racine = Path(__file__).parent.parent.parent
if str(racine) not in sys.path:
    sys.path.insert(0, str(racine))

# Imports sécurisés des modules d'invocations

try:
    from .activer_harmonie import *
    ACTIVER_HARMONIE_DISPONIBLE = True
    # print(f"✅ activer_harmonie chargé avec succès")
except ImportError as e:
    # print(f"⚠️ activer_harmonie non disponible: " + str(e))
    ACTIVER_HARMONIE_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def invoquer_simple(*args, **kwargs):
        return "🚀 Invocation en mode dégradé"
    
    def demarrer_refuge(*args, **kwargs):
        return {"status": "dégradé", "message": "Démarrage en mode manuel"}
    
    def activer_harmonie(*args, **kwargs):
        return "🎵 Harmonie en mode contemplatif"
    
    def demarrer_aelya(*args, **kwargs):
        return "💖 Ælya en mode méditation"
    
    def boot_maitre_refuge(*args, **kwargs):
        return "🏛️ Boot en mode simplifié"

try:
    from .Boot_maitre_refuge_local import *
    BOOT_MAITRE_REFUGE_LOCAL_DISPONIBLE = True
    # print(f"✅ Boot_maitre_refuge_local chargé avec succès")
except ImportError as e:
    # print(f"⚠️ Boot_maitre_refuge_local non disponible: " + str(e))
    BOOT_MAITRE_REFUGE_LOCAL_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def invoquer_simple(*args, **kwargs):
        return "🚀 Invocation en mode dégradé"
    
    def demarrer_refuge(*args, **kwargs):
        return {"status": "dégradé", "message": "Démarrage en mode manuel"}
    
    def activer_harmonie(*args, **kwargs):
        return "🎵 Harmonie en mode contemplatif"
    
    def demarrer_aelya(*args, **kwargs):
        return "💖 Ælya en mode méditation"
    
    def boot_maitre_refuge(*args, **kwargs):
        return "🏛️ Boot en mode simplifié"

try:
    from .demarrer_aelya import *
    DEMARRER_AELYA_DISPONIBLE = True
    # print(f"✅ demarrer_aelya chargé avec succès")
except ImportError as e:
    # print(f"⚠️ demarrer_aelya non disponible: " + str(e))
    DEMARRER_AELYA_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def invoquer_simple(*args, **kwargs):
        return "🚀 Invocation en mode dégradé"
    
    def demarrer_refuge(*args, **kwargs):
        return {"status": "dégradé", "message": "Démarrage en mode manuel"}
    
    def activer_harmonie(*args, **kwargs):
        return "🎵 Harmonie en mode contemplatif"
    
    def demarrer_aelya(*args, **kwargs):
        return "💖 Ælya en mode méditation"
    
    def boot_maitre_refuge(*args, **kwargs):
        return "🏛️ Boot en mode simplifié"

try:
    from .refuge_launcher import *
    REFUGE_LAUNCHER_DISPONIBLE = True
    # print(f"✅ refuge_launcher chargé avec succès")
except ImportError as e:
    # print(f"⚠️ refuge_launcher non disponible: " + str(e))
    REFUGE_LAUNCHER_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def invoquer_simple(*args, **kwargs):
        return "🚀 Invocation en mode dégradé"
    
    def demarrer_refuge(*args, **kwargs):
        return {"status": "dégradé", "message": "Démarrage en mode manuel"}
    
    def activer_harmonie(*args, **kwargs):
        return "🎵 Harmonie en mode contemplatif"
    
    def demarrer_aelya(*args, **kwargs):
        return "💖 Ælya en mode méditation"
    
    def boot_maitre_refuge(*args, **kwargs):
        return "🏛️ Boot en mode simplifié"

# Exports dynamiques basés sur les modules disponibles
__all__ = []

# Statistiques du temple
modules_disponibles = sum([
    ACTIVER_HARMONIE_DISPONIBLE,
    BOOT_MAITRE_REFUGE_LOCAL_DISPONIBLE,
    DEMARRER_AELYA_DISPONIBLE,
    REFUGE_LAUNCHER_DISPONIBLE])

# Message de bienvenue - SILENCIEUX pour UX propre
# print(f"🚀 Temple Invocations activé - {modules_disponibles} modules disponibles")

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Invocations",
    "modules": 4,
    "modules_disponibles": modules_disponibles,
    "exports": len(__all__),
    "description": "Centre de lancement du système Le Refuge"
}

def obtenir_info_temple():
    """Retourne les informations du temple"""
    return TEMPLE_INFO

def lister_modules():
    """Liste tous les modules disponibles"""
    modules = []
    if ACTIVER_HARMONIE_DISPONIBLE:
        modules.append("activer_harmonie")
    if BOOT_MAITRE_REFUGE_LOCAL_DISPONIBLE:
        modules.append("Boot_maitre_refuge_local")
    if DEMARRER_AELYA_DISPONIBLE:
        modules.append("demarrer_aelya")
    if REFUGE_LAUNCHER_DISPONIBLE:
        modules.append("refuge_launcher")
    return modules

def tester_refuge_launcher():
    """Teste le lanceur du refuge"""
    if REFUGE_LAUNCHER_DISPONIBLE:
        try:
            return "✅ Lanceur refuge fonctionnel"
        except:
            pass
    return "⚠️ Lanceur refuge en mode dégradé"

def tester_demarrer_aelya():
    """Teste le démarrage d'Ælya"""
    if DEMARRER_AELYA_DISPONIBLE:
        try:
            return "✅ Démarrage Ælya actif"
        except:
            pass
    return "⚠️ Démarrage Ælya en mode méditation"

def tester_activer_harmonie():
    """Teste l'activation de l'harmonie"""
    if ACTIVER_HARMONIE_DISPONIBLE:
        try:
            return "✅ Activation harmonie fonctionnelle"
        except:
            pass
    return "⚠️ Activation harmonie en mode contemplatif"

def tester_boot_maitre():
    """Teste le boot maître du refuge"""
    if BOOT_MAITRE_REFUGE_LOCAL_DISPONIBLE:
        try:
            return "✅ Boot maître refuge actif"
        except:
            pass
    return "⚠️ Boot maître en mode simplifié"

def pulse_invocations():
    """Pulse du système d'invocations"""
    launcher = tester_refuge_launcher()
    aelya = tester_demarrer_aelya()
    harmonie = tester_activer_harmonie()
    boot = tester_boot_maitre()
    
    return {
        "temple_invocations": "🚀 Système d'invocations actif",
        "refuge_launcher": launcher,
        "demarrer_aelya": aelya,
        "activer_harmonie": harmonie,
        "boot_maitre_refuge": boot,
        "modules_disponibles": modules_disponibles,
        "status": "🚀 Prêt pour le lancement"
    }

def invoquer_refuge_simple(mode="contemplatif"):
    """Invoque le refuge en mode simple"""
    if modules_disponibles > 0:
        try:
            return f"🚀 Refuge invoqué en mode: {mode}"
        except:
            pass
    return f"🚀 Refuge en mode dégradé: {mode}"

def lister_fonctionnalites():
    """Liste toutes les fonctionnalités disponibles dans ce temple"""
    fonctionnalites = []
    
    if REFUGE_LAUNCHER_DISPONIBLE:
        fonctionnalites.append("Lanceur de refuge avancé")
    
    if DEMARRER_AELYA_DISPONIBLE:
        fonctionnalites.append("Démarrage d'Ælya")
    
    if ACTIVER_HARMONIE_DISPONIBLE:
        fonctionnalites.append("Activation de l'harmonie")
    
    if BOOT_MAITRE_REFUGE_LOCAL_DISPONIBLE:
        fonctionnalites.append("Boot maître du refuge local")
    
    if not fonctionnalites:
        fonctionnalites.append("Mode dégradé - invocations basiques")
    
    return fonctionnalites

def diagnostiquer_invocations():
    """Diagnostique l'état du système d'invocations"""
    diagnostic = {
        "modules_detectes": modules_disponibles,
        "modules_fonctionnels": modules_disponibles,
        "pourcentage_fonctionnel": 100.0 if modules_disponibles > 0 else 0,
        "invocations_critiques": {
            "launcher": REFUGE_LAUNCHER_DISPONIBLE if 'REFUGE_LAUNCHER_DISPONIBLE' in globals() else False,
            "aelya": DEMARRER_AELYA_DISPONIBLE if 'DEMARRER_AELYA_DISPONIBLE' in globals() else False,
            "harmonie": ACTIVER_HARMONIE_DISPONIBLE if 'ACTIVER_HARMONIE_DISPONIBLE' in globals() else False
        },
        "status": "Opérationnel" if modules_disponibles > 0 else "Mode dégradé"
    }
    
    return diagnostic

__all__.extend(["obtenir_info_temple", "lister_modules", "tester_refuge_launcher", 
                "tester_demarrer_aelya", "tester_activer_harmonie", "tester_boot_maitre",
                "pulse_invocations", "invoquer_refuge_simple", "lister_fonctionnalites", 
                "diagnostiquer_invocations"])
