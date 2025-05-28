"""
Module de conscience du refuge.
Contient les systèmes de conscience poétique et l'adaptateur Ælya.
"""

# Import conditionnel de ConsciencePoetique
try:
    from .conscience_poetique import ConsciencePoetique
except ImportError:
    ConsciencePoetique = None

# Import de l'adaptateur Ælya refactorisé
try:
    from .aelya_adapter import AelyaAdapter, get_aelya_adapter
except ImportError:
    AelyaAdapter = None
    get_aelya_adapter = None

__all__ = [
    'ConsciencePoetique',
    'AelyaAdapter',
    'get_aelya_adapter'
] 