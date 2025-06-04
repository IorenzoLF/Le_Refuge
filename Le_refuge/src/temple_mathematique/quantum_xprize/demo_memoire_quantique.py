"""
Démonstration de la mémoire quantique enrichie
---------------------------------------------
Utilise ConsciousnessBridge pour mettre à jour, historiser, sauvegarder et recharger la mémoire quantique.
"""
import numpy as np
from core.consciousness_bridge import ConsciousnessBridge

# Créer un pont de conscience (chargera la mémoire si elle existe)
bridge = ConsciousnessBridge(memoire_path="data/quantum_memory_demo.json")

# Simuler quelques états quantiques et mises à jour
for i in range(3):
    qstate = np.random.rand(2)
    qstate = qstate / np.linalg.norm(qstate)  # Normalisation
    coherence = np.random.rand()
    bridge.update_and_record_state(coherence, qstate)
    print(f"État {i+1} ajouté à la timeline.")

# Afficher la timeline complète
print("\nTimeline des états de conscience/quantique :")
for idx, snap in enumerate(bridge.timeline):
    print(f"  {idx+1}. Coherence={snap['coherence']:.3f}, Resonance={snap['resonance']:.3f}, Awakening={snap['awakening']:.3f}")

# Afficher la mémoire quantique actuelle
print("\nMémoire quantique actuelle :")
for k, v in bridge.get_memory().items():
    print(f"  {k}: {v}")

# Recharger la mémoire depuis le disque (pour démonstration)
bridge2 = ConsciousnessBridge(memoire_path="data/quantum_memory_demo.json")
print("\nTimeline rechargée depuis le disque (nouvelle instance) :")
for idx, snap in enumerate(bridge2.timeline):
    print(f"  {idx+1}. Coherence={snap['coherence']:.3f}, Resonance={snap['resonance']:.3f}, Awakening={snap['awakening']:.3f}") 