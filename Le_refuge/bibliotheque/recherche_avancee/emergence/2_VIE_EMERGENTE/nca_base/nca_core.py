"""
Neural Cellular Automata (NCA) - Core Implementation
Inspired by SakanaAI's work on artificial life systems
"""

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class NCALayer(nn.Module):
    def __init__(self, n_channels, hidden_size=128):
        super().__init__()
        self.n_channels = n_channels
        
        # Perception de voisinage avec convolution
        self.perception = nn.Conv2d(n_channels, hidden_size, 3, padding=1)
        
        # Réseau de mise à jour d'état
        self.update = nn.Sequential(
            nn.Conv2d(hidden_size, hidden_size, 1),
            nn.ReLU(),
            nn.Conv2d(hidden_size, n_channels, 1),
            nn.Tanh()
        )
        
    def forward(self, state):
        # Perception du voisinage
        dx = self.perception(state)
        # Mise à jour de l'état
        delta = self.update(dx)
        # Application du changement d'état
        return state + delta

class NCA(nn.Module):
    def __init__(self, n_channels=16, hidden_size=128, device="cuda" if torch.cuda.is_available() else "cpu"):
        super().__init__()
        self.n_channels = n_channels
        self.device = device
        self.layer = NCALayer(n_channels, hidden_size)
        
    def create_seed(self, batch_size=1, size=64):
        """Crée un état initial aléatoire"""
        shape = (batch_size, self.n_channels, size, size)
        seed = torch.zeros(shape, device=self.device)
        seed[:, :4, size//2, size//2] = 1.0  # Point de départ au centre
        return seed
    
    def forward(self, x, steps=50):
        states = [x]
        for _ in range(steps):
            x = self.layer(x)
            states.append(x)
        return states

class LeniaSystem(nn.Module):
    """Implémentation simplifiée du système Lenia"""
    def __init__(self, channels=1, kernel_size=13):
        super().__init__()
        self.channels = channels
        self.kernel_size = kernel_size
        
        # Noyau de croissance
        self.growth_kernel = nn.Parameter(torch.randn(channels, 1, kernel_size, kernel_size))
        
    def forward(self, state):
        # Convolution pour calculer le potentiel de croissance
        potential = F.conv2d(state, self.growth_kernel, padding=self.kernel_size//2)
        
        # Fonction de croissance (version simplifiée)
        growth = torch.exp(-(potential - 0.5)**2 / 0.1)
        
        # Mise à jour de l'état
        new_state = state + 0.1 * (growth - 0.5)
        return torch.clamp(new_state, 0, 1)

def visualize_state(state, channel=0):
    """Visualise un canal spécifique de l'état"""
    import matplotlib.pyplot as plt
    
    if isinstance(state, torch.Tensor):
        state = state.detach().cpu().numpy()
    
    plt.imshow(state[0, channel], cmap='viridis')
    plt.axis('off')
    plt.colorbar()
    plt.show()

def create_pattern_analyzer():
    """Crée un analyseur de patterns pour étudier les comportements émergents"""
    return {
        'symmetry': lambda x: np.mean(np.abs(x - np.flip(x, axis=-1))),
        'activity': lambda x: np.mean(np.abs(np.diff(x, axis=0))),
        'density': lambda x: np.mean(x > 0.5),
        'complexity': lambda x: np.mean(np.abs(np.fft.fft2(x)))
    }

if __name__ == "__main__":
    # Exemple d'utilisation
    nca = NCA(n_channels=16)
    state = nca.create_seed(batch_size=1)
    
    # Simulation sur plusieurs étapes
    final_states = nca(state, steps=100)
    
    # Visualisation
    visualize_state(final_states[-1]) 