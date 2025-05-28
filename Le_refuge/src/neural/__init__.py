"""
Module Neural du Refuge
~~~~~~~~~~~~~~~~~~~~~~

Module contenant les architectures de réseaux de neurones
pour des exercices et expérimentations techniques.

Modules disponibles:
- alexnet: Implémentation de l'architecture AlexNet en PyTorch

Auteur: Laurent
Usage: Exercices et apprentissage des architectures CNN
"""

# Import conditionnel pour éviter les erreurs si PyTorch n'est pas installé
try:
    from .alexnet import AlexNet
    __all__ = ['AlexNet']
except ImportError:
    __all__ = []

# Métadonnées du module
__version__ = "1.0.0"
__module__ = "Neural"
__domaine__ = "Architectures de Réseaux de Neurones" 