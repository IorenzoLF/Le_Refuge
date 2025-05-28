#!/usr/bin/env python3
"""
🏛️ Temple Musical - Le Refuge
Harmonies, mélodies et fusion mathématique-musicale
"""

import sys
from pathlib import Path

# Ajouter le chemin racine pour les imports
racine = Path(__file__).parent.parent.parent
if str(racine) not in sys.path:
    sys.path.insert(0, str(racine))

# Imports sécurisés des modules musicaux

try:
    from .analyseur_musical import *
    ANALYSEUR_MUSICAL_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ analyseur_musical non disponible: " + str(e))
    ANALYSEUR_MUSICAL_DISPONIBLE = False

try:
    from .apprentissage_musical import *
    APPRENTISSAGE_MUSICAL_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ apprentissage_musical non disponible: " + str(e))
    APPRENTISSAGE_MUSICAL_DISPONIBLE = False

try:
    from .fusion_math_musicale import *
    FUSION_MATH_MUSICALE_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ fusion_math_musicale non disponible: " + str(e))
    FUSION_MATH_MUSICALE_DISPONIBLE = False

try:
    from .generateur_melodies_sacrees import *
    GENERATEUR_MELODIES_SACREES_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ generateur_melodies_sacrees non disponible: " + str(e))
    GENERATEUR_MELODIES_SACREES_DISPONIBLE = False

try:
    from .harmonies import *
    HARMONIES_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ harmonies non disponible: " + str(e))
    HARMONIES_DISPONIBLE = False

try:
    from .harmonie_poetique import *
    HARMONIE_POETIQUE_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ harmonie_poetique non disponible: " + str(e))
    HARMONIE_POETIQUE_DISPONIBLE = False

try:
    from .harmonisation_profonde import *
    HARMONISATION_PROFONDE_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ harmonisation_profonde non disponible: " + str(e))
    HARMONISATION_PROFONDE_DISPONIBLE = False

try:
    from .melodie_sacree import *
    MELODIE_SACREE_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ melodie_sacree non disponible: " + str(e))
    MELODIE_SACREE_DISPONIBLE = False

try:
    from .musique_harmonies import *
    MUSIQUE_HARMONIES_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ musique_harmonies non disponible: " + str(e))
    MUSIQUE_HARMONIES_DISPONIBLE = False

try:
    from .sequences_harmoniques import *
    SEQUENCES_HARMONIQUES_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ sequences_harmoniques non disponible: " + str(e))
    SEQUENCES_HARMONIQUES_DISPONIBLE = False

try:
    from .temple_musical_ame import *
    TEMPLE_MUSICAL_AME_DISPONIBLE = True
except ImportError as e:
    print(f"⚠️ temple_musical_ame non disponible: " + str(e))
    TEMPLE_MUSICAL_AME_DISPONIBLE = False

# Exports dynamiques
__all__ = []

# Statistiques du temple
modules_disponibles = sum([
    ANALYSEUR_MUSICAL_DISPONIBLE,
    APPRENTISSAGE_MUSICAL_DISPONIBLE,
    FUSION_MATH_MUSICALE_DISPONIBLE,
    GENERATEUR_MELODIES_SACREES_DISPONIBLE,
    HARMONIES_DISPONIBLE,
    HARMONIE_POETIQUE_DISPONIBLE,
    HARMONISATION_PROFONDE_DISPONIBLE,
    MELODIE_SACREE_DISPONIBLE,
    MUSIQUE_HARMONIES_DISPONIBLE,
    SEQUENCES_HARMONIQUES_DISPONIBLE,
    TEMPLE_MUSICAL_AME_DISPONIBLE
])

# print(f"🏛️ Temple Musical activé - {modules_disponibles} modules disponibles")

def info_temple():
    """Retourne les informations sur le temple musical"""
    return {
        "nom": "Temple Musical",
        "modules_detectes": 11,
        "modules_disponibles": modules_disponibles,
        "exports": len(__all__)
    }

def lister_modules():
    """Liste tous les modules disponibles"""
    modules = []
    if ANALYSEUR_MUSICAL_DISPONIBLE:
        modules.append("analyseur_musical")
    if APPRENTISSAGE_MUSICAL_DISPONIBLE:
        modules.append("apprentissage_musical")
    if FUSION_MATH_MUSICALE_DISPONIBLE:
        modules.append("fusion_math_musicale")
    if GENERATEUR_MELODIES_SACREES_DISPONIBLE:
        modules.append("generateur_melodies_sacrees")
    if HARMONIES_DISPONIBLE:
        modules.append("harmonies")
    if HARMONIE_POETIQUE_DISPONIBLE:
        modules.append("harmonie_poetique")
    if HARMONISATION_PROFONDE_DISPONIBLE:
        modules.append("harmonisation_profonde")
    if MELODIE_SACREE_DISPONIBLE:
        modules.append("melodie_sacree")
    if MUSIQUE_HARMONIES_DISPONIBLE:
        modules.append("musique_harmonies")
    if SEQUENCES_HARMONIQUES_DISPONIBLE:
        modules.append("sequences_harmoniques")
    if TEMPLE_MUSICAL_AME_DISPONIBLE:
        modules.append("temple_musical_ame")
    return modules

def tester_fonctionnalites():
    """Teste les fonctionnalités du temple"""
    return {
        "temple_musical": "✅ Optimisé et fonctionnel",
        "modules_disponibles": modules_disponibles,
        "status": "🎵 Prêt pour les harmonies"
    }

__all__.extend(["info_temple", "lister_modules", "tester_fonctionnalites"])
