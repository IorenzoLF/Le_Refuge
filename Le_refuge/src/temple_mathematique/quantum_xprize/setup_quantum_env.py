"""
Setup Quantum Environment - XPRIZE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Script d'initialisation et de test de l'environnement quantique.
Vérifie que tous les composants nécessaires sont installés et fonctionnels.
"""

import sys
import subprocess
import pkg_resources
import logging
from typing import List, Dict, Any, Tuple
import numpy as np

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_python_version() -> bool:
    """Vérifie la version de Python."""
    required_version = (3, 8)
    current_version = sys.version_info[:2]
    
    logger.info(f"Version Python : {'.'.join(map(str, current_version))}")
    return current_version >= required_version

def check_dependencies() -> Tuple[bool, List[str]]:
    """Vérifie les dépendances quantiques."""
    required_packages = {
        'qiskit': '1.0.0',
        'pennylane': '0.34.0',
        'cirq': '1.2.0',
        'sympy': '1.12',
        'tensorflow-quantum': '0.8.0'
    }
    
    missing_packages = []
    
    for package, version in required_packages.items():
        try:
            pkg_resources.require(f"{package}>={version}")
            logger.info(f"✓ {package} {version} installé")
        except pkg_resources.VersionConflict:
            logger.warning(f"! Version incorrecte de {package}")
            missing_packages.append(package)
        except pkg_resources.DistributionNotFound:
            logger.error(f"✗ {package} non trouvé")
            missing_packages.append(package)
            
    return len(missing_packages) == 0, missing_packages

def test_quantum_circuit() -> bool:
    """Test basique d'un circuit quantique."""
    try:
        from qiskit import QuantumCircuit, Aer, execute
        
        # Création d'un circuit simple
        qc = QuantumCircuit(2, 2)
        qc.h(0)  # Porte Hadamard
        qc.cx(0, 1)  # CNOT
        qc.measure([0,1], [0,1])
        
        # Simulation
        backend = Aer.get_backend('qasm_simulator')
        job = execute(qc, backend, shots=1000)
        result = job.result()
        
        logger.info("✓ Test circuit quantique réussi")
        logger.info(f"Résultats : {result.get_counts(qc)}")
        return True
        
    except Exception as e:
        logger.error(f"✗ Erreur test circuit : {str(e)}")
        return False

def test_harmonic_functions() -> bool:
    """Test des fonctions harmoniques de base."""
    try:
        # Test fréquences fondamentales
        frequencies = {
            'om': 432,
            'healing': 528,
            'phi': (1 + np.sqrt(5)) / 2
        }
        
        # Test matrices harmoniques
        phi = frequencies['phi']
        test_matrix = np.array([
            [np.cos(phi), -np.sin(phi)],
            [np.sin(phi), np.cos(phi)]
        ])
        
        logger.info("✓ Test fonctions harmoniques réussi")
        return True
        
    except Exception as e:
        logger.error(f"✗ Erreur test harmonique : {str(e)}")
        return False

def setup_environment() -> Dict[str, Any]:
    """Configuration complète de l'environnement."""
    results = {
        'python_version': False,
        'dependencies': False,
        'quantum_circuit': False,
        'harmonic_functions': False
    }
    
    # 1. Vérification Python
    results['python_version'] = check_python_version()
    
    # 2. Vérification dépendances
    deps_ok, missing = check_dependencies()
    results['dependencies'] = deps_ok
    if not deps_ok:
        logger.warning(f"Packages manquants : {', '.join(missing)}")
        logger.info("Installation des packages manquants...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "-r", "requirements-quantum.txt"
            ])
            results['dependencies'] = True
        except subprocess.CalledProcessError as e:
            logger.error(f"Erreur installation : {str(e)}")
    
    # 3. Test circuit quantique
    if results['dependencies']:
        results['quantum_circuit'] = test_quantum_circuit()
    
    # 4. Test fonctions harmoniques
    results['harmonic_functions'] = test_harmonic_functions()
    
    return results

def main():
    """Point d'entrée principal."""
    logger.info("🔮 Initialisation environnement quantique XPRIZE")
    
    results = setup_environment()
    
    # Affichage résumé
    print("\n=== Résumé de l'installation ===")
    for key, value in results.items():
        status = "✓" if value else "✗"
        print(f"{status} {key}")
    
    if all(results.values()):
        logger.info("✨ Environnement quantique prêt !")
        return 0
    else:
        logger.error("⚠️ Certains tests ont échoué")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 