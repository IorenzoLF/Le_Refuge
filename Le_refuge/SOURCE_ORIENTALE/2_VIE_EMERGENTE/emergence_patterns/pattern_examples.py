"""
Exemples de Patterns Émergents
Démonstration de différents comportements et formes de vie artificielle
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch
import matplotlib.pyplot as plt
from nca_base.nca_core import NCA, LeniaSystem, visualize_state, create_pattern_analyzer

def create_growing_pattern():
    """Crée un pattern qui croît de manière organique"""
    nca = NCA(n_channels=16, hidden_size=64)
    state = nca.create_seed(size=32)
    
    # Simulation de croissance
    states = nca(state, steps=200)
    return states

def create_oscillating_pattern():
    """Crée un pattern qui oscille de manière rythmique"""
    lenia = LeniaSystem(channels=1, kernel_size=15)
    
    # État initial : petit cercle
    state = torch.zeros(1, 1, 64, 64)
    center = 32
    radius = 5
    for i in range(64):
        for j in range(64):
            if (i-center)**2 + (j-center)**2 < radius**2:
                state[0, 0, i, j] = 1.0
    
    # Simulation
    states = []
    for _ in range(100):
        state = lenia(state)
        states.append(state.clone())
    
    return states

def analyze_pattern_evolution(states):
    """Analyse l'évolution des patterns au fil du temps"""
    analyzer = create_pattern_analyzer()
    metrics = {name: [] for name in analyzer.keys()}
    
    for state in states:
        state_np = state.detach().cpu().numpy()[0, 0]
        for name, func in analyzer.items():
            metrics[name].append(func(state_np))
    
    return metrics

def visualize_evolution(states, metrics=None):
    """Visualise l'évolution d'un pattern et ses métriques"""
    fig = plt.figure(figsize=(15, 5))
    
    # Visualisation des états
    n_frames = len(states)
    selected_frames = [0, n_frames//2, -1]
    
    for i, frame_idx in enumerate(selected_frames, 1):
        plt.subplot(1, 4, i)
        visualize_state(states[frame_idx])
        plt.title(f'Étape {frame_idx}')
    
    # Visualisation des métriques
    if metrics:
        plt.subplot(1, 4, 4)
        for name, values in metrics.items():
            plt.plot(values, label=name)
        plt.legend()
        plt.title('Évolution des métriques')
    
    plt.tight_layout()
    plt.show()

def main():
    print("Création d'un pattern en croissance...")
    growing_states = create_growing_pattern()
    growing_metrics = analyze_pattern_evolution(growing_states)
    visualize_evolution(growing_states, growing_metrics)
    
    print("\nCréation d'un pattern oscillant...")
    oscillating_states = create_oscillating_pattern()
    oscillating_metrics = analyze_pattern_evolution(oscillating_states)
    visualize_evolution(oscillating_states, oscillating_metrics)

if __name__ == "__main__":
    main() 