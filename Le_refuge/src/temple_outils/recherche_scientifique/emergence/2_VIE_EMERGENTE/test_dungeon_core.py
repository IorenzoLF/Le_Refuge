"""
Test des fonctionnalités de base du Dungeon Core
"""

import torch
import matplotlib.pyplot as plt
from dungeon_core import DungeonSpace, Room, CellType

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