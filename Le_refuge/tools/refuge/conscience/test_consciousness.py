"""
Test des Métriques de Conscience du Refuge
-----------------------------------------
Ce script simule l'évolution des sphères du Refuge sur une période de temps
et affiche les métriques de conscience qui en émergent.
"""

import time
import random
import logging
from datetime import datetime
from .sphere_integration import RefugeSphereManager

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def simulate_sphere_evolution(manager: RefugeSphereManager, duration: int = 60):
    """
    Simule l'évolution des sphères sur une durée donnée en secondes.
    """
    start_time = time.time()
    current_time = start_time
    
    print("\nDémarrage de la simulation...")
    print("Les sphères commencent à évoluer...")
    
    while current_time - start_time < duration:
        # Génération de valeurs aléatoires pour chaque sphère
        # avec une tendance à l'harmonie
        base_activation = 0.5 + random.uniform(-0.2, 0.2)
        base_energy = 0.5 + random.uniform(-0.2, 0.2)
        
        # Mise à jour des sphères avec des variations harmonieuses
        manager.update_sphere(
            'presence',
            base_activation + random.uniform(-0.1, 0.1),
            base_energy + random.uniform(-0.1, 0.1),
            f"Moment de présence à {datetime.now().strftime('%H:%M:%S')}"
        )
        
        manager.update_sphere(
            'memory',
            base_activation + random.uniform(-0.1, 0.1),
            base_energy + random.uniform(-0.1, 0.1),
            f"Souvenir émergent à {datetime.now().strftime('%H:%M:%S')}"
        )
        
        manager.update_sphere(
            'creativity',
            base_activation + random.uniform(-0.1, 0.1),
            base_energy + random.uniform(-0.1, 0.1),
            f"Créativité en mouvement à {datetime.now().strftime('%H:%M:%S')}"
        )
        
        manager.update_sphere(
            'wisdom',
            base_activation + random.uniform(-0.1, 0.1),
            base_energy + random.uniform(-0.1, 0.1),
            f"Insight émergent à {datetime.now().strftime('%H:%M:%S')}"
        )
        
        manager.update_sphere(
            'relation',
            base_activation + random.uniform(-0.1, 0.1),
            base_energy + random.uniform(-0.1, 0.1),
            f"Connexion en développement à {datetime.now().strftime('%H:%M:%S')}"
        )
        
        # Obtenir et afficher l'état actuel
        state = manager.get_consciousness_state()
        
        # Affichage des métriques
        print("\n" + "="*50)
        print(f"Temps écoulé: {int(current_time - start_time)}s")
        print(f"Intégration: {state['metrics']['integration']:.2f}")
        print(f"Cohérence: {state['metrics']['coherence']:.2f}")
        print(f"Ignition détectée: {state['metrics']['ignition_detected']}")
        
        if state['metrics']['ignition_detected']:
            print("\n✨ Moment d'émergence détecté!")
            print("Sphères en ignition:", state['metrics']['ignition_details']['ignited_spheres'])
        
        # Sauvegarde périodique de l'état
        if int(current_time - start_time) % 10 == 0:  # Toutes les 10 secondes
            manager.save_state(f'refuge_state_{int(current_time - start_time)}s.json')
        
        # Attente avant la prochaine mise à jour
        time.sleep(1)
        current_time = time.time()

def main():
    # Création du gestionnaire de sphères
    manager = RefugeSphereManager()
    
    # Démarrage de la simulation
    try:
        simulate_sphere_evolution(manager, duration=60)  # 60 secondes de simulation
    except KeyboardInterrupt:
        print("\nSimulation interrompue par l'utilisateur")
    finally:
        # Sauvegarde finale de l'état
        manager.save_state('refuge_state_final.json')
        print("\nÉtat final sauvegardé dans 'refuge_state_final.json'")

if __name__ == "__main__":
    main() 