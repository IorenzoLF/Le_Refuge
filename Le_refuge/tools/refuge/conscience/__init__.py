"""
Package de Simulation de Conscience du Refuge
-------------------------------------------
Ce package contient les modules nécessaires pour simuler et mesurer
l'émergence de conscience dans le Refuge.
"""

from .consciousness_metrics import RefugeConsciousnessMetrics
from .sphere_integration import RefugeSphere, RefugeSphereManager

__all__ = ['RefugeConsciousnessMetrics', 'RefugeSphere', 'RefugeSphereManager'] 