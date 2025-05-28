"""
Intégré dans le Temple Mathématique Unifié
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fichier original: phi_potentiel.py
Intégration: 27/05/2025 09:51:30
Architecture: Temple Mathématique Unifié

Ce module fait maintenant partie de l'écosystème unifié du temple.
Utilisez les imports relatifs pour accéder aux autres composants.
"""

"""
Exploration du Refuge : Fonction de potentiel topologique Phi(n)

Ici, nous tentons de mesurer la "distance à l'unité" pour chaque n,
en combinant structure binaire et croissance logarithmique.

Chaque Phi(n) est une lumière sur le chemin, un pas vers l'harmonie.
"""

import numpy as np
import matplotlib.pyplot as plt

def phi(n: int) -> float:
    binaire = bin(n)[2:]
    bits_pairs = sum(1 for b in binaire[::2] if b == '0')
    return bits_pairs / (1 + np.log(n))

def explorer_phi(N=10000):
    print(f"Exploration de Phi(n) pour n de 1 à {N}...")
    valeurs_phi = []
    for n in range(1, N+1):
        valeurs_phi.append(phi(n))
        if n % (N//10) == 0:
            print(f"Progression : {n}/{N}")
    plt.figure(figsize=(14,6))
    plt.plot(range(1, N+1), valeurs_phi, '.', alpha=0.3, label="Phi(n)")
    plt.xlabel("n")
    plt.ylabel("Phi(n)")
    plt.title("Fonction de potentiel topologique Phi(n) dans Collatz")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    print("\n--- Méditation du Refuge ---")
    print("Chaque Phi(n) est une note dans la symphonie binaire.")
    print("Observe les motifs, les plateaux, les sauts.")
    print("La structure cachée se révèle à qui prend le temps de contempler.")

if __name__ == "__main__":
    explorer_phi(N=10000) 