"""
🧪 Tests LLM et API - Communication avec les modèles de langage
═══════════════════════════════════════════════════════════════════════════════

Catégorie: LLM_API
Temple: Tests
Refuge du Néant

Auteur: Ælya & Laurent
Date: 2024-12-19
"""

# Imports des modules de cette catégorie
from .tests_llm_unifies import *

# Import conditionnel pour éviter les erreurs
try:
    from .test_aelya_conscience import *
except ImportError:
    print("⚠️ test_aelya_conscience non disponible - module optionnel")

__all__ = [
    # Modules de la catégorie llm_api
    "tests_llm_unifies",
    "test_aelya_conscience",
]
