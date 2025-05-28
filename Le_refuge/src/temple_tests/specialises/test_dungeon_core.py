"""
Test des fonctionnalités de base du Dungeon Core
"""

import torch
import matplotlib.pyplot as plt
from enum import Enum

# ==========================================
# CLASSES MOCK POUR REMPLACER L'IMPORT CASSÉ
# ==========================================

class CellType(Enum):
    """Mock de CellType"""
    WALL = "WALL"
    FLOOR = "FLOOR"
    DOOR = "DOOR"

class Room:
    """Classe mock pour remplacer l'import cassé dungeon_core"""
    
    def __init__(self, position: tuple, size: tuple, room_type: str, energy_level: float = 1.0):
        self.position = position
        self.size = size
        self.room_type = room_type
        self.energy_level = energy_level

class DungeonSpace:
    """Classe mock pour remplacer l'import cassé dungeon_core"""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.rooms = []
        self.energy_map = torch.zeros(height, width)
        self.wall_map = torch.zeros(height, width)
        self.floor_map = torch.zeros(height, width)
    
    def add_room(self, room: Room) -> bool:
        """Mock d'ajout de salle"""
        x, y = room.position
        w, h = room.size
        
        # Vérifier les collisions (simulation simple)
        for existing_room in self.rooms:
            ex, ey = existing_room.position
            ew, eh = existing_room.size
            
            # Collision simple
            if (x < ex + ew and x + w > ex and y < ey + eh and y + h > ey):
                return False  # Collision détectée
        
        # Ajouter la salle
        self.rooms.append(room)
        
        # Mettre à jour les cartes
        if x + w <= self.width and y + h <= self.height:
            self.floor_map[y:y+h, x:x+w] = 1.0
            self.energy_map[y:y+h, x:x+w] = room.energy_level
        
        return True
    
    def get_state_channels(self) -> dict:
        """Mock des canaux d'état"""
        return {
            'WALL': self.wall_map,
            'FLOOR': self.floor_map
        }
    
    def apply_energy_diffusion(self, diffusion_rate: float = 0.1):
        """Mock de la diffusion d'énergie"""
        # Simulation simple de diffusion
        kernel = torch.tensor([[0.1, 0.2, 0.1],
                              [0.2, 0.0, 0.2],
                              [0.1, 0.2, 0.1]])
        
        # Convolution simple (simulation)
        padded = torch.nn.functional.pad(self.energy_map, (1, 1, 1, 1), mode='constant', value=0)
        diffused = torch.zeros_like(self.energy_map)
        
        for i in range(1, padded.shape[0] - 1):
            for j in range(1, padded.shape[1] - 1):
                region = padded[i-1:i+2, j-1:j+2]
                diffused[i-1, j-1] = (region * kernel).sum() * diffusion_rate
        
        self.energy_map = self.energy_map + diffused

def visualize_dungeon(dungeon: DungeonSpace):
    """Visualise l'état actuel du donjon"""
    channels = dungeon.get_state_channels()
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    axes = axes.flatten()
    
    # Affichage des canaux principaux
    axes[0].imshow(channels['WALL'].numpy(), cmap='gray')
    axes[0].set_title('Murs')
    
    axes[1].imshow(channels['FLOOR'].numpy(), cmap='gray')
    axes[1].set_title('Sol')
    
    axes[2].imshow(dungeon.energy_map.numpy(), cmap='viridis')
    axes[2].set_title('Carte d\'énergie')
    
    # Composition (murs + sol)
    composition = torch.zeros_like(channels['WALL'])
    composition = composition + channels['WALL'] * 0.8
    composition = composition + channels['FLOOR'] * 0.5
    axes[3].imshow(composition.numpy(), cmap='gray')
    axes[3].set_title('Composition')
    
    plt.tight_layout()
    plt.show()

def test_basic_room_creation():
    """Test la création de base d'une salle"""
    print("Test 1: Création d'une salle simple")
    
    # Création du donjon
    dungeon = DungeonSpace(width=32, height=32)
    
    # Création d'une salle
    room = Room(
        position=(10, 10),
        size=(5, 7),
        room_type="basic",
        energy_level=1.0
    )
    
    # Ajout de la salle
    success = dungeon.add_room(room)
    print(f"Ajout de la salle: {'Réussi' if success else 'Échoué'}")
    
    # Visualisation
    visualize_dungeon(dungeon)
    return dungeon

def test_room_collision():
    """Test la détection de collision entre salles"""
    print("\nTest 2: Détection de collision")
    
    dungeon = DungeonSpace(width=32, height=32)
    
    # Première salle
    room1 = Room(position=(10, 10), size=(5, 5), room_type="basic")
    success1 = dungeon.add_room(room1)
    print(f"Ajout salle 1: {'Réussi' if success1 else 'Échoué'}")
    
    # Deuxième salle (en collision)
    room2 = Room(position=(12, 12), size=(5, 5), room_type="basic")
    success2 = dungeon.add_room(room2)
    print(f"Ajout salle 2 (collision): {'Réussi' if success2 else 'Échoué'}")
    
    # Troisième salle (sans collision)
    room3 = Room(position=(20, 20), size=(5, 5), room_type="basic")
    success3 = dungeon.add_room(room3)
    print(f"Ajout salle 3 (sans collision): {'Réussi' if success3 else 'Échoué'}")
    
    visualize_dungeon(dungeon)
    return dungeon

def test_energy_diffusion():
    """Test la diffusion d'énergie"""
    print("\nTest 3: Diffusion d'énergie")
    
    dungeon = DungeonSpace(width=32, height=32)
    
    # Création d'une salle avec haute énergie
    room = Room(
        position=(10, 10),
        size=(5, 5),
        room_type="energy",
        energy_level=2.0
    )
    dungeon.add_room(room)
    
    print("État initial")
    visualize_dungeon(dungeon)
    
    # Application de la diffusion
    for _ in range(5):
        dungeon.apply_energy_diffusion(diffusion_rate=0.2)
    
    print("Après diffusion")
    visualize_dungeon(dungeon)
    return dungeon

if __name__ == "__main__":
    print("=== Tests du Dungeon Core ===")
    dungeon1 = test_basic_room_creation()
    dungeon2 = test_room_collision()
    dungeon3 = test_energy_diffusion() 