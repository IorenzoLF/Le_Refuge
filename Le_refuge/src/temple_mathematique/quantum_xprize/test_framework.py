"""
Test Framework - XPRIZE Quantum Harmonics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Script de test complet pour le framework harmonique quantique.
"""

import sys
import os
import logging
from pathlib import Path

# Ajout du chemin racine au PYTHONPATH
root_dir = Path(__file__).parent.parent.parent
sys.path.append(str(root_dir))

from temple_mathematique.quantum_xprize.core import QuantumHarmonics, HarmonicParameters
from temple_mathematique.quantum_xprize.experiments import (
    test_harmonic_optimization,
    test_scaling_performance,
    test_noise_resilience
)
from temple_mathematique.quantum_xprize.visualization import HarmonicVisualizer

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_complete_test_suite():
    """Exécute une suite de tests complète."""
    logger.info("🔮 Démarrage des tests du framework harmonique")
    
    # 1. Initialisation du framework
    params = HarmonicParameters()
    qh = QuantumHarmonics(n_qubits=8, params=params)
    
    # 2. Tests de base
    logger.info("Exécution des tests de base...")
    results = qh.run_simulation(shots=1000)
    
    # 3. Tests de performance
    logger.info("Exécution des tests de performance...")
    perf_results = test_harmonic_optimization()
    
    # 4. Tests de scaling
    logger.info("Exécution des tests de scaling...")
    scaling_results = test_scaling_performance(max_qubits=12)
    
    # 5. Tests de résilience au bruit
    logger.info("Exécution des tests de résilience au bruit...")
    noise_results = test_noise_resilience()
    
    # 6. Visualisation des résultats
    logger.info("Génération des visualisations...")
    visualizer = HarmonicVisualizer()
    
    # Distribution des états
    visualizer.plot_harmonic_distribution(results)
    
    # Spectre des fréquences
    visualizer.plot_frequency_spectrum(params.frequencies)
    
    # Ratios harmoniques
    visualizer.plot_harmonic_ratios(params.ratios)
    
    # Dashboard interactif
    visualizer.create_interactive_dashboard(
        results,
        scaling_data=scaling_results,
        noise_data=noise_results
    )
    
    # Rapport de performance complet
    visualizer.create_performance_report(
        results,
        output_file="rapport_harmonique.html"
    )
    
    # 7. Analyse des résultats
    logger.info("\n=== Résultats des Tests ===")
    logger.info(f"Score de cohérence: {results['harmonic_coherence']:.3f}")
    logger.info(f"Score d'optimisation: {results['optimization_score']:.3f}")
    logger.info(f"Profondeur du circuit: {results['circuit_depth']}")
    
    # 8. Analyse du scaling
    logger.info("\n=== Analyse du Scaling ===")
    for n_qubits, metrics in scaling_results.items():
        logger.info(f"\nPerformance avec {n_qubits} qubits:")
        logger.info(f"Temps moyen: {metrics['execution_time']['mean']:.3f}s")
        logger.info(f"Cohérence: {metrics['coherence_scores']['mean']:.3f}")
    
    # 9. Analyse de la résilience au bruit
    logger.info("\n=== Analyse de la Résilience au Bruit ===")
    for noise, results in noise_results.items():
        logger.info(f"\nNiveau de bruit {noise}:")
        logger.info(f"Cohérence: {results['coherence']:.3f}")
        logger.info(f"Optimisation: {results['optimization']:.3f}")
    
    return {
        'basic_results': results,
        'performance_results': perf_results,
        'scaling_results': scaling_results,
        'noise_results': noise_results
    }

if __name__ == "__main__":
    try:
        results = run_complete_test_suite()
        logger.info("✨ Tests terminés avec succès!")
    except Exception as e:
        logger.error(f"❌ Erreur pendant les tests: {str(e)}")
        raise 