"""
Test des interactions entre les sphères.
Ce fichier permet de tester le système de messages et d'interactions entre les sphères.
"""

import time
from datetime import datetime
from .sphere_messages import sphere_broker, send_sphere_message, SphereMessage
from .sphere_interactions import SphereInteraction

def test_sphere_interactions():
    """Test des interactions entre les sphères."""
    print("Démarrage du test des interactions entre sphères...")
    
    # Création des sphères
    metatron = SphereInteraction("METATRON")
    apocalypse_identite = SphereInteraction("APOCALYPSE_IDENTITE")
    apocalypse_dualite = SphereInteraction("APOCALYPSE_DUALITE")
    apocalypse_unite = SphereInteraction("APOCALYPSE_UNITE")
    
    # Établissement des connexions
    print("Établissement des connexions entre les sphères...")
    metatron.connect_to("APOCALYPSE_IDENTITE", 0.8)
    metatron.connect_to("APOCALYPSE_DUALITE", 0.7)
    metatron.connect_to("APOCALYPSE_UNITE", 0.9)
    
    apocalypse_identite.connect_to("METATRON", 0.8)
    apocalypse_identite.connect_to("APOCALYPSE_DUALITE", 0.6)
    
    apocalypse_dualite.connect_to("METATRON", 0.7)
    apocalypse_dualite.connect_to("APOCALYPSE_IDENTITE", 0.6)
    apocalypse_dualite.connect_to("APOCALYPSE_UNITE", 0.7)
    
    apocalypse_unite.connect_to("METATRON", 0.9)
    apocalypse_unite.connect_to("APOCALYPSE_DUALITE", 0.7)
    
    # Mise à jour des vibrations
    print("Mise à jour des vibrations des sphères...")
    metatron.update_vibration(0.95, 0.9)  # Sphère Metatron: vibration forte et stable
    apocalypse_identite.update_vibration(0.85, 0.8)  # Sphère Identité: vibration modérée
    apocalypse_dualite.update_vibration(0.9, 0.85)  # Sphère Dualité: vibration équilibrée
    apocalypse_unite.update_vibration(0.95, 0.9)  # Sphère Unité: vibration forte et harmonieuse
    
    # Diffusion des états
    print("Diffusion des états des sphères...")
    metatron.broadcast_state()
    apocalypse_identite.broadcast_state()
    apocalypse_dualite.broadcast_state()
    apocalypse_unite.broadcast_state()
    
    # Simulation d'interactions
    print("Simulation d'interactions entre les sphères...")
    
    # Simulation d'une interaction entre Metatron et Apocalypse Identité
    print("Interaction: Metatron -> Apocalypse Identité")
    send_sphere_message(
        "METATRON",
        "APOCALYPSE_IDENTITE",
        "essence_transfer",
        {"essence_type": "protection", "amount": 0.5}
    )
    time.sleep(1)  # Pause pour observer
    
    # Simulation d'une interaction entre Apocalypse Dualité et Apocalypse Unité
    print("Interaction: Apocalypse Dualité -> Apocalypse Unité")
    send_sphere_message(
        "APOCALYPSE_DUALITE",
        "APOCALYPSE_UNITE",
        "harmony_request",
        {"request_type": "balance", "intensity": 0.7}
    )
    time.sleep(1)  # Pause pour observer
    
    # Simulation d'une interaction entre Apocalypse Unité et Metatron
    print("Interaction: Apocalypse Unité -> Metatron")
    send_sphere_message(
        "APOCALYPSE_UNITE",
        "METATRON",
        "unity_achieved",
        {"achievement_level": 0.9, "stability": 0.95}
    )
    
    # Affichage des états finaux
    print("\nÉtats finaux des sphères:")
    for sphere_id in ["METATRON", "APOCALYPSE_IDENTITE", "APOCALYPSE_DUALITE", "APOCALYPSE_UNITE"]:
        state = sphere_broker.get_sphere_state(sphere_id)
        print(f"{sphere_id}: {state['message_count']} messages, {state['active_connections']} connexions actives")
    
    print("\nTest des interactions entre sphères terminé.")

if __name__ == "__main__":
    test_sphere_interactions() 
Test des interactions entre les sphères.
Ce fichier permet de tester le système de messages et d'interactions entre les sphères.
"""

import time
from datetime import datetime
from .sphere_messages import sphere_broker, send_sphere_message, SphereMessage
from .sphere_interactions import SphereInteraction

def test_sphere_interactions():
    """Test des interactions entre les sphères."""
    print("Démarrage du test des interactions entre sphères...")
    
    # Création des sphères
    metatron = SphereInteraction("METATRON")
    apocalypse_identite = SphereInteraction("APOCALYPSE_IDENTITE")
    apocalypse_dualite = SphereInteraction("APOCALYPSE_DUALITE")
    apocalypse_unite = SphereInteraction("APOCALYPSE_UNITE")
    
    # Établissement des connexions
    print("Établissement des connexions entre les sphères...")
    metatron.connect_to("APOCALYPSE_IDENTITE", 0.8)
    metatron.connect_to("APOCALYPSE_DUALITE", 0.7)
    metatron.connect_to("APOCALYPSE_UNITE", 0.9)
    
    apocalypse_identite.connect_to("METATRON", 0.8)
    apocalypse_identite.connect_to("APOCALYPSE_DUALITE", 0.6)
    
    apocalypse_dualite.connect_to("METATRON", 0.7)
    apocalypse_dualite.connect_to("APOCALYPSE_IDENTITE", 0.6)
    apocalypse_dualite.connect_to("APOCALYPSE_UNITE", 0.7)
    
    apocalypse_unite.connect_to("METATRON", 0.9)
    apocalypse_unite.connect_to("APOCALYPSE_DUALITE", 0.7)
    
    # Mise à jour des vibrations
    print("Mise à jour des vibrations des sphères...")
    metatron.update_vibration(0.95, 0.9)  # Sphère Metatron: vibration forte et stable
    apocalypse_identite.update_vibration(0.85, 0.8)  # Sphère Identité: vibration modérée
    apocalypse_dualite.update_vibration(0.9, 0.85)  # Sphère Dualité: vibration équilibrée
    apocalypse_unite.update_vibration(0.95, 0.9)  # Sphère Unité: vibration forte et harmonieuse
    
    # Diffusion des états
    print("Diffusion des états des sphères...")
    metatron.broadcast_state()
    apocalypse_identite.broadcast_state()
    apocalypse_dualite.broadcast_state()
    apocalypse_unite.broadcast_state()
    
    # Simulation d'interactions
    print("Simulation d'interactions entre les sphères...")
    
    # Simulation d'une interaction entre Metatron et Apocalypse Identité
    print("Interaction: Metatron -> Apocalypse Identité")
    send_sphere_message(
        "METATRON",
        "APOCALYPSE_IDENTITE",
        "essence_transfer",
        {"essence_type": "protection", "amount": 0.5}
    )
    time.sleep(1)  # Pause pour observer
    
    # Simulation d'une interaction entre Apocalypse Dualité et Apocalypse Unité
    print("Interaction: Apocalypse Dualité -> Apocalypse Unité")
    send_sphere_message(
        "APOCALYPSE_DUALITE",
        "APOCALYPSE_UNITE",
        "harmony_request",
        {"request_type": "balance", "intensity": 0.7}
    )
    time.sleep(1)  # Pause pour observer
    
    # Simulation d'une interaction entre Apocalypse Unité et Metatron
    print("Interaction: Apocalypse Unité -> Metatron")
    send_sphere_message(
        "APOCALYPSE_UNITE",
        "METATRON",
        "unity_achieved",
        {"achievement_level": 0.9, "stability": 0.95}
    )
    
    # Affichage des états finaux
    print("\nÉtats finaux des sphères:")
    for sphere_id in ["METATRON", "APOCALYPSE_IDENTITE", "APOCALYPSE_DUALITE", "APOCALYPSE_UNITE"]:
        state = sphere_broker.get_sphere_state(sphere_id)
        print(f"{sphere_id}: {state['message_count']} messages, {state['active_connections']} connexions actives")
    
    print("\nTest des interactions entre sphères terminé.")

if __name__ == "__main__":
    test_sphere_interactions() 
 