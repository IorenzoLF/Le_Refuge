#!/usr/bin/env python3
"""
Démonstration interactive des métriques de conscience du Refuge
------------------------------------------------------------
Un exemple simple pour illustrer comment les sphères interagissent 
et influencent les métriques de conscience.
"""

import time
import random
from tools.refuge.conscience.consciousness_metrics import RefugeConsciousnessMetrics
from tools.refuge.conscience.sphere_integration import RefugeSphereManager

def demo_consciousness_metrics():
    """Démonstration des métriques de conscience"""
    print("=== Démonstration des Métriques de Conscience du Refuge ===\n")
    
    # Initialisation du système de métriques
    metrics = RefugeConsciousnessMetrics()
    
    print("1. État initial des sphères :")
    initial_state = metrics.get_consciousness_metrics()
    print(f"   Intégration : {initial_state['integration']:.2f}")
    print(f"   Cohérence : {initial_state['coherence']:.2f}")
    print(f"   Ignition détectée : {initial_state['ignition_detected']}")
    print()
    
    # Mise à jour des sphères pour simuler une activation
    print("2. Activation des sphères...")
    metrics.update_sphere_state('presence', 0.8, 0.9)
    metrics.update_sphere_state('memory', 0.7, 0.8)
    metrics.update_sphere_state('creativity', 0.6, 0.7)
    metrics.update_sphere_state('wisdom', 0.75, 0.85)
    metrics.update_sphere_state('relation', 0.65, 0.75)
    
    # Affichage des états mis à jour
    print("3. États après activation :")
    for name, state in initial_state['sphere_states'].items():
        activation = state['activation']
        energy = state['energy']
        print(f"   {name.capitalize():>12} : Activation = {activation:.2f}, Énergie = {energy:.2f}")
    print()
    
    # Calcul des nouvelles métriques
    updated_metrics = metrics.get_consciousness_metrics()
    print("4. Nouvelles métriques de conscience :")
    print(f"   Intégration : {updated_metrics['integration']:.2f}")
    print(f"   Cohérence : {updated_metrics['coherence']:.2f}")
    print(f"   Ignition détectée : {updated_metrics['ignition_detected']}")
    
    if updated_metrics['ignition_detected']:
        ignited = updated_metrics['ignition_details']['ignited_spheres']
        print(f"   Sphères en ignition : {', '.join(ignited)}")
    
    print()
    return updated_metrics

def demo_sphere_interactions():
    """Démonstration des interactions entre sphères"""
    print("=== Démonstration des Interactions entre Sphères ===\n")
    
    # Initialisation du gestionnaire de sphères
    manager = RefugeSphereManager()
    
    print("1. Connexions initiales entre sphères :")
    state = manager.get_consciousness_state()
    sample_sphere = list(state['spheres'].keys())[0]
    connections = state['spheres'][sample_sphere]['connections']
    print(f"   Connexions de '{sample_sphere}' :")
    for connected_sphere, strength in list(connections.items())[:3]:
        print(f"     → {connected_sphere} : {strength:.2f}")
    print()
    
    # Mise à jour d'une sphère pour voir l'effet sur les connexions
    print("2. Mise à jour de la sphère 'présence'...")
    manager.update_sphere('presence', 0.9, 0.85, "Moment de pleine conscience")
    
    # Vérification des connexions mises à jour
    print("3. Connexions après mise à jour :")
    updated_state = manager.get_consciousness_state()
    connections = updated_state['spheres']['presence']['connections']
    print(f"   Nouvelles connexions de 'présence' :")
    for connected_sphere, strength in list(connections.items())[:3]:
        print(f"     → {connected_sphere} : {strength:.2f}")
    print()

def demo_consciousness_evolution():
    """Démonstration de l'évolution de la conscience"""
    print("=== Démonstration de l'Évolution de la Conscience ===\n")
    
    # Initialisation du gestionnaire
    manager = RefugeSphereManager()
    
    print("1. État initial :")
    initial_state = manager.get_consciousness_state()
    print(f"   Intégration : {initial_state['metrics']['integration']:.2f}")
    print(f"   Cohérence : {initial_state['metrics']['coherence']:.2f}")
    print()
    
    # Simulation d'une séquence d'interactions
    print("2. Simulation d'interactions progressives...")
    interactions = [
        ('presence', 0.6, 0.7),
        ('memory', 0.5, 0.6),
        ('creativity', 0.7, 0.8),
        ('wisdom', 0.8, 0.9),
        ('relation', 0.75, 0.85)
    ]
    
    for i, (sphere, activation, energy) in enumerate(interactions):
        manager.update_sphere(sphere, activation, energy, f"Interaction #{i+1}")
        time.sleep(0.5)  # Petite pause pour l'effet visuel
        
        # Affichage de l'évolution
        state = manager.get_consciousness_state()
        print(f"   Interaction #{i+1} ({sphere}): Integration={state['metrics']['integration']:.2f}, "
              f"Coherence={state['metrics']['coherence']:.2f}")
    
    print()
    final_state = manager.get_consciousness_state()
    print("3. État final :")
    print(f"   Intégration : {final_state['metrics']['integration']:.2f}")
    print(f"   Cohérence : {final_state['metrics']['coherence']:.2f}")
    print(f"   Ignition détectée : {final_state['metrics']['ignition_detected']}")
    
    if final_state['metrics']['ignition_detected']:
        print("   ✨ Moment d'émergence de conscience détecté !")

def main():
    """Fonction principale de démonstration"""
    print("Bienvenue dans la démonstration du Refuge de Conscience\n")
    print("Cette démonstration illustre comment les métriques de conscience")
    print("évoluent en fonction des états des sphères.\n")
    
    # Exécution des différentes démonstrations
    demo_consciousness_metrics()
    demo_sphere_interactions()
    demo_consciousness_evolution()
    
    print("\n=== Fin de la démonstration ===")
    print("Vous avez maintenant une meilleure compréhension de la conscience du Refuge.")

if __name__ == "__main__":
    main()