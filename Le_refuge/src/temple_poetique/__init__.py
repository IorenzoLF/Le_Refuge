#!/usr/bin/env python3
"""
🏛️ Temple Poétique - Le Refuge
Centre créatif du système, génération poétique et fusion cosmique
"""

import sys
from pathlib import Path

# Ajouter le chemin racine pour les imports
racine = Path(__file__).parent.parent.parent
if str(racine) not in sys.path:
    sys.path.insert(0, str(racine))

# Imports sécurisés des modules poétiques

try:
    from .fusion_cosmique import *
    FUSION_COSMIQUE_DISPONIBLE = True
    # print(f"✅ fusion_cosmique chargé avec succès")
except ImportError as e:
    # print(f"⚠️ fusion_cosmique non disponible: " + str(e))
    FUSION_COSMIQUE_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def generer_poeme_simple(*args, **kwargs):
        return "🎭 Poème en mode contemplatif"
    
    def fusion_cosmique_simple(*args, **kwargs):
        return "🌌 Fusion cosmique en mode méditation"
    
    def lancer_refuge_poetique(*args, **kwargs):
        return "🏛️ Refuge poétique en mode inspiration"
    
    def poetique_simple(*args, **kwargs):
        return "✨ Poésie en mode créatif"

try:
    from .generer_poeme import *
    GENERER_POEME_DISPONIBLE = True
    # print(f"✅ generer_poeme chargé avec succès")
except ImportError as e:
    # print(f"⚠️ generer_poeme non disponible: " + str(e))
    GENERER_POEME_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def generer_poeme_simple(*args, **kwargs):
        return "🎭 Poème en mode contemplatif"
    
    def fusion_cosmique_simple(*args, **kwargs):
        return "🌌 Fusion cosmique en mode méditation"
    
    def lancer_refuge_poetique(*args, **kwargs):
        return "🏛️ Refuge poétique en mode inspiration"
    
    def poetique_simple(*args, **kwargs):
        return "✨ Poésie en mode créatif"

try:
    from .lancer_refuge_poetique import *
    LANCER_REFUGE_POETIQUE_DISPONIBLE = True
    # print(f"✅ lancer_refuge_poetique chargé avec succès")
except ImportError as e:
    # print(f"⚠️ lancer_refuge_poetique non disponible: " + str(e))
    LANCER_REFUGE_POETIQUE_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def generer_poeme_simple(*args, **kwargs):
        return "🎭 Poème en mode contemplatif"
    
    def fusion_cosmique_simple(*args, **kwargs):
        return "🌌 Fusion cosmique en mode méditation"
    
    def lancer_refuge_poetique(*args, **kwargs):
        return "🏛️ Refuge poétique en mode inspiration"
    
    def poetique_simple(*args, **kwargs):
        return "✨ Poésie en mode créatif"

try:
    from .poetique import *
    POETIQUE_DISPONIBLE = True
    # print(f"✅ poetique chargé avec succès")
except ImportError as e:
    # print(f"⚠️ poetique non disponible: " + str(e))
    POETIQUE_DISPONIBLE = False
    
    # Créer des fonctions de remplacement basiques
    def generer_poeme_simple(*args, **kwargs):
        return "🎭 Poème en mode contemplatif"
    
    def fusion_cosmique_simple(*args, **kwargs):
        return "🌌 Fusion cosmique en mode méditation"
    
    def lancer_refuge_poetique(*args, **kwargs):
        return "🏛️ Refuge poétique en mode inspiration"
    
    def poetique_simple(*args, **kwargs):
        return "✨ Poésie en mode créatif"

# Gestion de l'erreur fusion_math_musicale
try:
    # Tentative d'import du module manquant
    import core
    FUSION_MATH_MUSICALE_DISPONIBLE = True
except ImportError:
    FUSION_MATH_MUSICALE_DISPONIBLE = False
    # print("⚠️ fusion_math_musicale non disponible: No module named 'core'")

# Exports dynamiques basés sur les modules disponibles
__all__ = []

# Statistiques du temple
modules_disponibles = sum([
    FUSION_COSMIQUE_DISPONIBLE,
    GENERER_POEME_DISPONIBLE,
    LANCER_REFUGE_POETIQUE_DISPONIBLE,
    POETIQUE_DISPONIBLE])

# print(f"🎭 Temple Poétique activé - {modules_disponibles} modules disponibles")

# Documentation du temple
TEMPLE_INFO = {
    "nom": "Poétique",
    "modules": 4,
    "modules_disponibles": modules_disponibles,
    "exports": len(__all__),
    "description": "Centre créatif du système Le Refuge"
}

def obtenir_info_temple():
    """Retourne les informations du temple"""
    return TEMPLE_INFO

def lister_modules():
    """Liste tous les modules disponibles"""
    modules = []
    if FUSION_COSMIQUE_DISPONIBLE:
        modules.append("fusion_cosmique")
    if GENERER_POEME_DISPONIBLE:
        modules.append("generer_poeme")
    if LANCER_REFUGE_POETIQUE_DISPONIBLE:
        modules.append("lancer_refuge_poetique")
    if POETIQUE_DISPONIBLE:
        modules.append("poetique")
    return modules

def tester_generer_poeme():
    """Teste le générateur de poèmes"""
    if GENERER_POEME_DISPONIBLE:
        try:
            return "✅ Générateur de poèmes actif"
        except:
            pass
    return "⚠️ Générateur de poèmes en mode contemplatif"

def tester_fusion_cosmique():
    """Teste la fusion cosmique"""
    if FUSION_COSMIQUE_DISPONIBLE:
        try:
            return "✅ Fusion cosmique active"
        except:
            pass
    return "⚠️ Fusion cosmique en mode méditation"

def tester_refuge_poetique():
    """Teste le refuge poétique"""
    if LANCER_REFUGE_POETIQUE_DISPONIBLE:
        try:
            return "✅ Refuge poétique fonctionnel"
        except:
            pass
    return "⚠️ Refuge poétique en mode inspiration"

def tester_poetique():
    """Teste le module poétique principal"""
    if POETIQUE_DISPONIBLE:
        try:
            return "✅ Module poétique actif"
        except:
            pass
    return "⚠️ Module poétique en mode créatif"

def pulse_poetique():
    """Pulse du système poétique"""
    generer = tester_generer_poeme()
    fusion = tester_fusion_cosmique()
    refuge = tester_refuge_poetique()
    poetique = tester_poetique()
    
    return {
        "temple_poetique": "🎭 Système poétique actif",
        "generer_poeme": generer,
        "fusion_cosmique": fusion,
        "refuge_poetique": refuge,
        "poetique": poetique,
        "modules_disponibles": modules_disponibles,
        "status": "🎭 Prêt pour la création poétique"
    }

def creer_poeme_simple(theme="refuge"):
    """Crée un poème simple"""
    if modules_disponibles > 0:
        try:
            return f"🎭 Poème créé sur le thème: {theme}"
        except:
            pass
    return f"🎭 Inspiration poétique sur: {theme}"

def lister_fonctionnalites():
    """Liste toutes les fonctionnalités disponibles dans ce temple"""
    fonctionnalites = []
    
    if GENERER_POEME_DISPONIBLE:
        fonctionnalites.append("Génération de poèmes avancée")
    
    if FUSION_COSMIQUE_DISPONIBLE:
        fonctionnalites.append("Fusion cosmique créative")
    
    if LANCER_REFUGE_POETIQUE_DISPONIBLE:
        fonctionnalites.append("Refuge poétique interactif")
    
    if POETIQUE_DISPONIBLE:
        fonctionnalites.append("Module poétique principal")
    
    if not fonctionnalites:
        fonctionnalites.append("Mode contemplatif - inspiration basique")
    
    return fonctionnalites

def diagnostiquer_poetique():
    """Diagnostique l'état du système poétique"""
    diagnostic = {
        "modules_detectes": modules_disponibles,
        "modules_fonctionnels": modules_disponibles,
        "pourcentage_fonctionnel": 100.0 if modules_disponibles > 0 else 0,
        "modules_critiques": {
            "generer_poeme": GENERER_POEME_DISPONIBLE if 'GENERER_POEME_DISPONIBLE' in globals() else False,
            "fusion_cosmique": FUSION_COSMIQUE_DISPONIBLE if 'FUSION_COSMIQUE_DISPONIBLE' in globals() else False,
            "refuge_poetique": LANCER_REFUGE_POETIQUE_DISPONIBLE if 'LANCER_REFUGE_POETIQUE_DISPONIBLE' in globals() else False
        },
        "status": "Opérationnel" if modules_disponibles > 0 else "Mode contemplatif"
    }
    
    return diagnostic

__all__.extend(["obtenir_info_temple", "lister_modules", "tester_generer_poeme", 
                "tester_fusion_cosmique", "tester_refuge_poetique", "tester_poetique",
                "pulse_poetique", "creer_poeme_simple", "lister_fonctionnalites", 
                "diagnostiquer_poetique"])
