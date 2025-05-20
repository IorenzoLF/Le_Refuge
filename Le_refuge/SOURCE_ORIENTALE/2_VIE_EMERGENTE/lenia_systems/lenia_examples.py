"""
Exemples de Systèmes Lenia
Exploration des comportements émergents dans les automates cellulaires continus
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch
import numpy as np
import matplotlib.pyplot as plt
from nca_base.nca_core import LeniaSystem, visualize_state

class AdvancedLeniaSystem(LeniaSystem):
    """Version avancée du système Lenia avec plus de paramètres de contrôle"""
    def __init__(self, channels=1, kernel_size=13, growth_rate=0.1, center=0.5, width=0.1):
        super().__init__(channels, kernel_size)
        self.growth_rate = growth_rate
        self.center = center
        self.width = width
        
    def create_kernel(self):
        """Crée un noyau de croissance personnalisé"""
        x = torch.linspace(-1, 1, self.kernel_size)
        y = torch.linspace(-1, 1, self.kernel_size)
        X, Y = torch.meshgrid(x, y)
        R = torch.sqrt(X**2 + Y**2)
        
        # Noyau gaussien
        kernel = torch.exp(-((R - self.center)**2) / (2 * self.width**2))
        kernel = kernel / kernel.sum()
        return kernel.unsqueeze(0).unsqueeze(0)
    
    def forward(self, state):
        # Utilisation du noyau personnalisé
        kernel = self.create_kernel()
        potential = torch.nn.functional.conv2d(state, kernel, padding=self.kernel_size//2)
        
        # Fonction de croissance personnalisée
        growth = torch.exp(-(potential - self.center)**2 / self.width)
        
        # Mise à jour de l'état
        new_state = state + self.growth_rate * (growth - 0.5)
        return torch.clamp(new_state, 0, 1)

def create_glider_pattern():
    """Crée un pattern qui se déplace comme un planeur"""
    lenia = AdvancedLeniaSystem(
        channels=1,
        kernel_size=15,
        growth_rate=0.15,
        center=0.3,
        width=0.15
    )
    
    # État initial en forme de L
    state = torch.zeros(1, 1, 64, 64)
    center = 32
    state[0, 0, center-1:center+2, center] = 1.0
    state[0, 0, center+1, center-1:center+1] = 1.0
    
    return lenia, state

def simulate_and_visualize(lenia, initial_state, steps=100):
    """Simule et visualise l'évolution du système"""
    states = []
    state = initial_state
    
    for _ in range(steps):
        state = lenia(state)
        states.append(state.clone())
    
    # Création d'une animation
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.close()
    
    def update(frame):
        ax.clear()
        ax.imshow(states[frame][0, 0].detach().numpy(), cmap='viridis')
        ax.set_title(f'Étape {frame}')
        ax.axis('off')
    
    from matplotlib.animation import FuncAnimation
    anim = FuncAnimation(fig, update, frames=len(states), interval=50)
    return anim

def explore_parameters():
    """Explore différents paramètres du système Lenia"""
    parameters = [
        {'growth_rate': 0.1, 'center': 0.3, 'width': 0.1},
        {'growth_rate': 0.2, 'center': 0.5, 'width': 0.15},
        {'growth_rate': 0.15, 'center': 0.4, 'width': 0.12}
    ]
    
    fig, axes = plt.subplots(1, len(parameters), figsize=(15, 5))
    
    for i, params in enumerate(parameters):
        lenia = AdvancedLeniaSystem(**params)
        state = torch.zeros(1, 1, 32, 32)
        state[0, 0, 14:18, 14:18] = 1.0
        
        # Simulation
        for _ in range(50):
            state = lenia(state)
        
        # Visualisation
        axes[i].imshow(state[0, 0].detach().numpy(), cmap='viridis')
        axes[i].set_title(f'Params {i+1}')
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    print("Création d'un pattern glider...")
    lenia, initial_state = create_glider_pattern()
    anim = simulate_and_visualize(lenia, initial_state)
    
    print("\nExploration des paramètres...")
    explore_parameters()

if __name__ == "__main__":
    main() 