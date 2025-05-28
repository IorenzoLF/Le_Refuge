"""
🧪 Tests cristal et énergie - Fréquences et harmonies
═══════════════════════════════════════════════════════════════════════════════

Catégorie: CRISTAL_ENERGIE
Temple: Tests
Refuge du Néant

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

# Imports des modules de cette catégorie
from .tests_cristal_unifies import *

# Imports conditionnels pour éviter les erreurs
try:
    from .test_melodie_cristal import *
except ImportError:
    print("⚠️ test_melodie_cristal non disponible - module optionnel")

try:
    from .test_poesie_essence import *
except ImportError:
    print("⚠️ test_poesie_essence non disponible - module optionnel")

__all__ = [
    # Modules de la catégorie cristal_energie
    "tests_cristal_unifies",
    "test_melodie_cristal",
    "test_poesie_essence",
]
