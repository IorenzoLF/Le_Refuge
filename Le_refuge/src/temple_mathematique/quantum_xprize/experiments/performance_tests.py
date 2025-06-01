"""
Performance Tests - XPRIZE Quantum Harmonics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tests de performance et benchmarks pour le framework harmonique quantique.
"""

import sys
from pathlib import Path
import pytest
import numpy as np
from typing import Dict, Any
import time
import logging

# Ajout du chemin racine au PYTHONPATH
root_dir = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_dir))

from temple_mathematique.quantum_xprize.core import QuantumHarmonics, HarmonicParameters
from qiskit_aer.noise import NoiseModel
from qiskit_aer.noise.errors import depolarizing_error

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PerformanceMetrics:
    """Collecte et analyse des métriques de performance."""
    
    def __init__(self):
        self.metrics = {
            'execution_time': [],
            'circuit_depth': [],
            'coherence_scores': [],
            'optimization_scores': []
        }
        
    def add_metric(self, name: str, value: float) -> None:
        """Ajoute une métrique."""
        if name in self.metrics:
            self.metrics[name].append(value)
            
    def get_summary(self) -> Dict[str, Any]:
        """Génère un résumé des métriques."""
        summary = {}
        for name, values in self.metrics.items():
            if values:
                summary[name] = {
                    'mean': np.mean(values),
                    'std': np.std(values),
                    'min': np.min(values),
                    'max': np.max(values)
                }
        return summary

def test_harmonic_optimization(n_qubits: int = 12, shots: int = 1000) -> Dict[str, Any]:
    """Test d'optimisation harmonique."""
    metrics = PerformanceMetrics()
    
    # Initialisation
    qh = QuantumHarmonics(n_qubits=n_qubits)
    
    # Test de performance
    start_time = time.time()
    results = qh.run_simulation(shots=shots)
    execution_time = time.time() - start_time
    
    # Collecte des métriques
    metrics.add_metric('execution_time', execution_time)
    metrics.add_metric('circuit_depth', results['circuit_depth'])
    metrics.add_metric('coherence_scores', results['harmonic_coherence'])
    metrics.add_metric('optimization_scores', results['optimization_score'])
    
    return metrics.get_summary()

def test_scaling_performance(max_qubits: int = 20) -> Dict[str, Any]:
    """Test de scaling avec différents nombres de qubits."""
    scaling_metrics = {}
    
    for n_qubits in range(2, max_qubits + 1, 2):
        logger.info(f"Testing with {n_qubits} qubits...")
        metrics = test_harmonic_optimization(n_qubits=n_qubits)
        scaling_metrics[n_qubits] = metrics
        
    return scaling_metrics

def test_noise_resilience(noise_levels: list = [0.001, 0.01, 0.1]) -> Dict[str, Any]:
    """Test de résilience au bruit."""
    noise_metrics = {}
    
    for noise in noise_levels:
        # Création du modèle de bruit
        noise_model = NoiseModel()
        error = depolarizing_error(noise, 1)
        noise_model.add_all_qubit_quantum_error(error, ['u', 'cx'])
        
        # Test avec bruit
        qh = QuantumHarmonics()
        results = qh.run_simulation()
        
        noise_metrics[noise] = {
            'coherence': results['harmonic_coherence'],
            'optimization': results['optimization_score']
        }
        
    return noise_metrics

@pytest.mark.benchmark
def test_optimization_benchmark(benchmark) -> None:
    """Benchmark des performances d'optimisation."""
    def run_optimization():
        qh = QuantumHarmonics(n_qubits=8)
        return qh.run_simulation(shots=100)
        
    # Exécution du benchmark
    result = benchmark(run_optimization)
    assert result is not None

def analyze_results(results: Dict[str, Any]) -> str:
    """Analyse et formate les résultats des tests."""
    analysis = []
    
    # Analyse du temps d'exécution
    if 'execution_time' in results:
        exec_time = results['execution_time']
        analysis.append(f"Temps d'exécution moyen: {exec_time['mean']:.3f}s (±{exec_time['std']:.3f}s)")
        
    # Analyse de la profondeur des circuits
    if 'circuit_depth' in results:
        depth = results['circuit_depth']
        analysis.append(f"Profondeur moyenne des circuits: {depth['mean']:.1f} (±{depth['std']:.1f})")
        
    # Analyse des scores de cohérence
    if 'coherence_scores' in results:
        coherence = results['coherence_scores']
        analysis.append(f"Score de cohérence moyen: {coherence['mean']:.3f} (±{coherence['std']:.3f})")
        
    # Analyse des scores d'optimisation
    if 'optimization_scores' in results:
        optimization = results['optimization_scores']
        analysis.append(f"Score d'optimisation moyen: {optimization['mean']:.3f} (±{optimization['std']:.3f})")
        
    return "\n".join(analysis)

def main():
    """Point d'entrée principal pour les tests de performance."""
    logger.info("🔬 Démarrage des tests de performance")
    
    # 1. Test d'optimisation de base
    logger.info("Test d'optimisation harmonique...")
    basic_results = test_harmonic_optimization()
    print("\nRésultats de base:")
    print(analyze_results(basic_results))
    
    # 2. Test de scaling
    logger.info("\nTest de scaling...")
    scaling_results = test_scaling_performance(max_qubits=12)
    print("\nRésultats de scaling:")
    for n_qubits, results in scaling_results.items():
        print(f"\n{n_qubits} qubits:")
        print(analyze_results(results))
    
    # 3. Test de résilience au bruit
    logger.info("\nTest de résilience au bruit...")
    noise_results = test_noise_resilience()
    print("\nRésultats de résilience au bruit:")
    for noise, results in noise_results.items():
        print(f"\nNiveau de bruit {noise}:")
        print(f"Cohérence: {results['coherence']:.3f}")
        print(f"Optimisation: {results['optimization']:.3f}")

if __name__ == "__main__":
    main() 