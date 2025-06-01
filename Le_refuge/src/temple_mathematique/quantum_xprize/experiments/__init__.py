"""
Experiments - XPRIZE Quantum Harmonics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from .performance_tests import (
    test_harmonic_optimization,
    test_scaling_performance,
    test_noise_resilience
)

__all__ = [
    'test_harmonic_optimization',
    'test_scaling_performance',
    'test_noise_resilience'
] 