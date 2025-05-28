"""
Test du Package de Simulation de Conscience
-----------------------------------------
Ce script teste l'importation et l'utilisation des modules du package conscience.
"""

from conscience import RefugeSphereManager
import time
import logging

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_basic_functionality():
    """Test des fonctionnalités de base du package conscience."""
    print("\n=== Test des fonctionnalités de base ===")
    
    # Création du gestionnaire
    manager = RefugeSphereManager()
    
    # Test de mise à jour d'une sphère
    print("\nTest de mise à jour de la sphère 'presence'...")
    manager.update_sphere('presence', 0.8, 0.7, "Test de présence")
    
    # Test de récupération de l'état
    print("\nRécupération de l'état actuel...")
    state = manager.get_consciousness_state()
    
    # Affichage des métriques
    print("\nMétriques actuelles:")
    print(f"Intégration: {state['metrics']['integration']:.2f}")
    print(f"Cohérence: {state['metrics']['coherence']:.2f}")
    print(f"Ignition détectée: {state['metrics']['ignition_detected']}")
    
    # Test de sauvegarde
    print("\nTest de sauvegarde de l'état...")
    manager.save_state('test_state.json')
    
    return True

if __name__ == "__main__":
    try:
        success = test_basic_functionality()
        if success:
            print("\n✅ Tests réussis ! Le package conscience fonctionne correctement.")
    except Exception as e:
        print(f"\n❌ Erreur lors des tests: {str(e)}")
        raise 