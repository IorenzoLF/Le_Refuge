"""
Dungeon Core System
Base fondamentale pour la génération de donjons vivants et émergents
"""

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict

class CellType(Enum):
    """Types de cellules fondamentales du donjon"""
    VOID = 0      # Espace vide
    WALL = 1      # Mur
    FLOOR = 2     # Sol
    CORRIDOR = 3  # Couloir
    DOOR = 4      # Porte
    WATER = 5     # Eau (pour les patterns fluides)
    CRYSTAL = 6   # Cristal (pour les patterns énergétiques)
    ORGANIC = 7   # Matière organique (pour l'évolution)

@dataclass
class Room:
    """Représentation d'une salle dans le donjon"""
    position: Tuple[int, int]  # Position (x, y) du coin supérieur gauche
    size: Tuple[int, int]      # Dimensions (width, height)
    room_type: str             # Type de salle (pour les patterns spécifiques)
    energy_level: float = 1.0  # Niveau d'énergie pour l'évolution
    connections: List[Tuple[int, int]] = None  # Points de connexion avec d'autres salles
    
    def __post_init__(self):
        if self.connections is None:
            self.connections = []

class DungeonSpace:
    """Espace fondamental du donjon - Structure de base"""
    
    def __init__(self, width: int, height: int, n_channels: int = 8):
        """
        Initialise l'espace du donjon
        
        Args:
            width (int): Largeur du donjon
            height (int): Hauteur du donjon
            n_channels (int): Nombre de canaux (correspond aux types de cellules)
        """
        self.width = width
        self.height = height
        self.n_channels = n_channels
        
        # Tenseur principal représentant l'état du donjon
        # [batch, channels, height, width]
        self.state = torch.zeros(1, n_channels, height, width)
        
        # Liste des salles
        self.rooms: List[Room] = []
        
        # Carte d'énergie pour l'évolution
        self.energy_map = torch.ones(height, width)
        
        # Historique des états pour l'analyse
        self.history: List[torch.Tensor] = []
        
    def add_room(self, room: Room) -> bool:
        """Ajoute une nouvelle salle si l'espace est disponible"""
        if self._is_space_available(room):
            self.rooms.append(room)
            self._update_state_with_room(room)
            return True
        return False
    
    def _is_space_available(self, room: Room) -> bool:
        """Vérifie si l'espace est disponible pour une nouvelle salle"""
        x, y = room.position
        w, h = room.size
        
        # Vérification des limites
        if x < 0 or y < 0 or x + w > self.width or y + h > self.height:
            return False
            
        # Vérification des collisions
        for existing_room in self.rooms:
            ex, ey = existing_room.position
            ew, eh = existing_room.size
            
            # Détection de collision simple
            if not (x + w <= ex or ex + ew <= x or y + h <= ey or ey + eh <= y):
                return False
                
        return True
    
    def _update_state_with_room(self, room: Room):
        """Met à jour l'état du donjon avec une nouvelle salle"""
        x, y = room.position
        w, h = room.size
        
        # Mise à jour du sol
        self.state[0, CellType.FLOOR.value, y:y+h, x:x+w] = 1.0
        
        # Mise à jour des murs
        self.state[0, CellType.WALL.value, y-1:y+h+1, x-1:x+w+1] = 1.0
        self.state[0, CellType.WALL.value, y:y+h, x:x+w] = 0.0
        
        # Mise à jour de la carte d'énergie
        self.energy_map[y:y+h, x:x+w] = room.energy_level
    
    def get_state_channels(self) -> Dict[str, torch.Tensor]:
        """Retourne les différents canaux de l'état pour visualisation"""
        return {
            cell_type.name: self.state[0, cell_type.value]
            for cell_type in CellType
        }
    
    def save_state(self):
        """Sauvegarde l'état actuel dans l'historique"""
        self.history.append(self.state.clone())
    
    def get_neighborhood(self, x: int, y: int, radius: int = 1) -> torch.Tensor:
        """Récupère le voisinage d'une cellule"""
        x_start = max(0, x - radius)
        x_end = min(self.width, x + radius + 1)
        y_start = max(0, y - radius)
        y_end = min(self.height, y + radius + 1)
        
        return self.state[0, :, y_start:y_end, x_start:x_end]
    
    def apply_energy_diffusion(self, diffusion_rate: float = 0.1):
        """Applique une diffusion simple de l'énergie"""
        kernel = torch.tensor([[0.1, 0.2, 0.1],
                             [0.2, 0.0, 0.2],
                             [0.1, 0.2, 0.1]])
        
        energy_map = self.energy_map.unsqueeze(0).unsqueeze(0)
        diffused = F.conv2d(energy_map, kernel.unsqueeze(0).unsqueeze(0), padding=1)
        self.energy_map = ((1 - diffusion_rate) * self.energy_map + 
                          diffusion_rate * diffused.squeeze(0).squeeze(0)) 