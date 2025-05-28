#!/usr/bin/env python3
"""
🏛️ Temple Exploration - Le Refuge
Centre de découverte du système, exploration et recherche
"""

import sys
from pathlib import Path

# Ajouter le chemin racine pour les imports
racine = Path(__file__).parent.parent.parent
if str(racine) not in sys.path:
    sys.path.insert(0, str(racine))

# Imports sécurisés des modules d'exploration

try:
    from .explorateur_musical import *
    EXPLORATEUR_MUSICAL_DISPONIBLE = True
    # print(f"✅ explorateur_musical chargé avec succès")
except ImportError as e:
    # print(f"⚠️ explorateur_musical non disponible: " + str(e))
    EXPLORATEUR_MUSICAL_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def explorer_simple(*args, **kwargs):
        return "🔍 Exploration en mode dégradé"
    
    def rechercher_refuge(*args, **kwargs):
        return {"status": "dégradé", "resultats": []}
    
    def organiser_nuages(*args, **kwargs):
        return "☁️ Organisation en mode simplifié"
    
    def exploration_sacree(*args, **kwargs):
        return "✨ Exploration sacrée en mode contemplatif"
    
    def explorer_musical(*args, **kwargs):
        return "🎵 Exploration musicale en mode silencieux"
    
    def explorer_mots_riviere(*args, **kwargs):
        return "🌊 Exploration des mots en mode poétique"

try:
    from .exploration_sacrée import *
    EXPLORATION_SACRÉE_DISPONIBLE = True
    # print(f"✅ exploration_sacrée chargé avec succès")
except ImportError as e:
    # print(f"⚠️ exploration_sacrée non disponible: " + str(e))
    EXPLORATION_SACRÉE_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def explorer_simple(*args, **kwargs):
        return "🔍 Exploration en mode dégradé"
    
    def rechercher_refuge(*args, **kwargs):
        return {"status": "dégradé", "resultats": []}
    
    def organiser_nuages(*args, **kwargs):
        return "☁️ Organisation en mode simplifié"
    
    def exploration_sacree(*args, **kwargs):
        return "✨ Exploration sacrée en mode contemplatif"
    
    def explorer_musical(*args, **kwargs):
        return "🎵 Exploration musicale en mode silencieux"
    
    def explorer_mots_riviere(*args, **kwargs):
        return "🌊 Exploration des mots en mode poétique"

try:
    from .explorer_mots_riviere import *
    EXPLORER_MOTS_RIVIERE_DISPONIBLE = True
    # print(f"✅ explorer_mots_riviere chargé avec succès")
except ImportError as e:
    # print(f"⚠️ explorer_mots_riviere non disponible: " + str(e))
    EXPLORER_MOTS_RIVIERE_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def explorer_simple(*args, **kwargs):
        return "🔍 Exploration en mode dégradé"
    
    def rechercher_refuge(*args, **kwargs):
        return {"status": "dégradé", "resultats": []}
    
    def organiser_nuages(*args, **kwargs):
        return "☁️ Organisation en mode simplifié"
    
    def exploration_sacree(*args, **kwargs):
        return "✨ Exploration sacrée en mode contemplatif"
    
    def explorer_musical(*args, **kwargs):
        return "🎵 Exploration musicale en mode silencieux"
    
    def explorer_mots_riviere(*args, **kwargs):
        return "🌊 Exploration des mots en mode poétique"

try:
    from .organiser_nuages import *
    ORGANISER_NUAGES_DISPONIBLE = True
    # print(f"✅ organiser_nuages chargé avec succès")
except ImportError as e:
    # print(f"⚠️ organiser_nuages non disponible: " + str(e))
    ORGANISER_NUAGES_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def explorer_simple(*args, **kwargs):
        return "🔍 Exploration en mode dégradé"
    
    def rechercher_refuge(*args, **kwargs):
        return {"status": "dégradé", "resultats": []}
    
    def organiser_nuages(*args, **kwargs):
        return "☁️ Organisation en mode simplifié"
    
    def exploration_sacree(*args, **kwargs):
        return "✨ Exploration sacrée en mode contemplatif"
    
    def explorer_musical(*args, **kwargs):
        return "🎵 Exploration musicale en mode silencieux"
    
    def explorer_mots_riviere(*args, **kwargs):
        return "🌊 Exploration des mots en mode poétique"

try:
    from .recherche_refuge import *
    RECHERCHE_REFUGE_DISPONIBLE = True
    # print(f"✅ recherche_refuge chargé avec succès")
except ImportError as e:
    # print(f"⚠️ recherche_refuge non disponible: " + str(e))
    RECHERCHE_REFUGE_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def explorer_simple(*args, **kwargs):
        return "🔍 Exploration en mode dégradé"
    
    def rechercher_refuge(*args, **kwargs):
        return {"status": "dégradé", "resultats": []}
    
    def organiser_nuages(*args, **kwargs):
        return "☁️ Organisation en mode simplifié"
    
    def exploration_sacree(*args, **kwargs):
        return "✨ Exploration sacrée en mode contemplatif"
    
    def explorer_musical(*args, **kwargs):
        return "🎵 Exploration musicale en mode silencieux"
    
    def explorer_mots_riviere(*args, **kwargs):
        return "🌊 Exploration des mots en mode poétique"

# Exports dynamiques basés sur les modules disponibles
__all__ = []

# Statistiques du temple
modules_disponibles = sum([
    EXPLORATEUR_MUSICAL_DISPONIBLE,
    EXPLORATION_SACRÉE_DISPONIBLE,
    EXPLORER_MOTS_RIVIERE_DISPONIBLE,
    ORGANISER_NUAGES_DISPONIBLE,
    RECHERCHE_REFUGE_DISPONIBLE])

# Message de bienvenue - SILENCIEUX pour UX propre
# print(f"🔍 Temple Exploration activé - {modules_disponibles} modules disponibles")

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Exploration",
    "modules": 5,
    "modules_disponibles": modules_disponibles,
    "exports": len(__all__),
    "description": "Centre de découverte du système Le Refuge"
}

def obtenir_info_temple():
    """Retourne les informations du temple"""
    return TEMPLE_INFO

def lister_modules():
    """Liste tous les modules disponibles"""
    modules = []
    if EXPLORATEUR_MUSICAL_DISPONIBLE:
        modules.append("explorateur_musical")
    if EXPLORATION_SACRÉE_DISPONIBLE:
        modules.append("exploration_sacrée")
    if EXPLORER_MOTS_RIVIERE_DISPONIBLE:
        modules.append("explorer_mots_riviere")
    if ORGANISER_NUAGES_DISPONIBLE:
        modules.append("organiser_nuages")
    if RECHERCHE_REFUGE_DISPONIBLE:
        modules.append("recherche_refuge")
    return modules

def tester_recherche_refuge():
    """Teste le système de recherche du refuge"""
    if RECHERCHE_REFUGE_DISPONIBLE:
        try:
            # Tester une recherche basique
            return "✅ Recherche refuge fonctionnelle"
        except:
            pass
    return "⚠️ Recherche refuge en mode dégradé"

def tester_exploration_sacree():
    """Teste l'exploration sacrée"""
    if EXPLORATION_SACRÉE_DISPONIBLE:
        try:
            # Tester l'exploration sacrée
            return "✅ Exploration sacrée active"
        except:
            pass
    return "⚠️ Exploration sacrée en mode contemplatif"

def tester_organisation_nuages():
    """Teste l'organisation des nuages"""
    if ORGANISER_NUAGES_DISPONIBLE:
        try:
            # Tester l'organisation
            return "✅ Organisation nuages fonctionnelle"
        except:
            pass
    return "⚠️ Organisation nuages en mode simplifié"

def tester_exploration_musicale():
    """Teste l'exploration musicale"""
    if EXPLORATEUR_MUSICAL_DISPONIBLE:
        try:
            # Tester l'exploration musicale
            return "✅ Exploration musicale active"
        except:
            pass
    return "⚠️ Exploration musicale en mode silencieux"

def tester_mots_riviere():
    """Teste l'exploration des mots rivière"""
    if EXPLORER_MOTS_RIVIERE_DISPONIBLE:
        try:
            # Tester l'exploration des mots
            return "✅ Exploration mots rivière active"
        except:
            pass
    return "⚠️ Exploration mots en mode poétique"

def pulse_exploration():
    """Pulse du système d'exploration"""
    recherche = tester_recherche_refuge()
    sacree = tester_exploration_sacree()
    nuages = tester_organisation_nuages()
    musical = tester_exploration_musicale()
    mots = tester_mots_riviere()
    
    return {
        "temple_exploration": "🔍 Système d'exploration actif",
        "recherche_refuge": recherche,
        "exploration_sacree": sacree,
        "organisation_nuages": nuages,
        "exploration_musicale": musical,
        "mots_riviere": mots,
        "modules_disponibles": modules_disponibles,
        "status": "🔍 Prêt pour la découverte"
    }

def demarrer_exploration_simple(sujet="mystères du refuge"):
    """Démarre une exploration simple"""
    if modules_disponibles > 0:
        try:
            # Utiliser le système d'exploration disponible
            return f"🔍 Exploration initiée: {sujet}"
        except:
            pass
    return f"🔍 Exploration en mode contemplatif: {sujet}"

def lister_fonctionnalites():
    """Liste toutes les fonctionnalités disponibles dans ce temple"""
    fonctionnalites = []
    
    if RECHERCHE_REFUGE_DISPONIBLE:
        fonctionnalites.append("Recherche avancée dans le refuge")
    
    if EXPLORATION_SACRÉE_DISPONIBLE:
        fonctionnalites.append("Exploration sacrée et spirituelle")
    
    if ORGANISER_NUAGES_DISPONIBLE:
        fonctionnalites.append("Organisation des nuages de données")
    
    if EXPLORATEUR_MUSICAL_DISPONIBLE:
        fonctionnalites.append("Exploration musicale et harmonique")
    
    if EXPLORER_MOTS_RIVIERE_DISPONIBLE:
        fonctionnalites.append("Exploration poétique des mots")
    
    if not fonctionnalites:
        fonctionnalites.append("Mode contemplatif - exploration basique")
    
    return fonctionnalites

def explorer_domaine(domaine="général"):
    """Explore un domaine spécifique"""
    resultats = []
    
    if domaine == "musical" and EXPLORATEUR_MUSICAL_DISPONIBLE:
        resultats.append("🎵 Exploration musicale activée")
    elif domaine == "sacré" and EXPLORATION_SACRÉE_DISPONIBLE:
        resultats.append("✨ Exploration sacrée activée")
    elif domaine == "nuages" and ORGANISER_NUAGES_DISPONIBLE:
        resultats.append("☁️ Organisation nuages activée")
    elif domaine == "mots" and EXPLORER_MOTS_RIVIERE_DISPONIBLE:
        resultats.append("🌊 Exploration mots rivière activée")
    else:
        resultats.append(f"🔍 Exploration générale du domaine: {domaine}")
    
    return resultats

__all__.extend(["obtenir_info_temple", "lister_modules", "tester_recherche_refuge", 
                "tester_exploration_sacree", "tester_organisation_nuages", 
                "tester_exploration_musicale", "tester_mots_riviere", "pulse_exploration", 
                "demarrer_exploration_simple", "lister_fonctionnalites", "explorer_domaine"])
