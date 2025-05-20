"""
Exploration du Refuge : Analyse modulaire profonde de Collatz

Pour chaque n, on étudie la dynamique selon n mod 2^k (k=4,8,16),
et on visualise les motifs de convergence, les symétries cachées.
"""

import numpy as np
import matplotlib.pyplot as plt

def collatz_modulaire(n, k=8, max_steps=1000):
    """
    Retourne la séquence Collatz modulo 2^k pour n.
    """
    courant = n
    seq = []
    modulo = 2**k
    steps = 0
    while courant != 1 and steps < max_steps:
        seq.append(courant % modulo)
        if courant % 2 == 0:
            courant //= 2
        else:
            courant = 3 * courant + 1
        steps += 1
    return seq

def visualiser_modulaire(N=256, k=8):
    print(f"Analyse modulaire profonde pour n de 1 à {N}, k={k}...")
    data = np.zeros((N, k*2))
    for n in range(1, N+1):
        seq = collatz_modulaire(n, k=k)
        for i, val in enumerate(seq[:k*2]):
            data[n-1, i] = val
        if n % (N//10) == 0:
            print(f"Progression : {n}/{N}")
    plt.figure(figsize=(14,8))
    plt.imshow(data, aspect='auto', cmap='viridis', origin='lower')
    plt.colorbar(label=f"n mod 2^{k}")
    plt.xlabel("Étapes dans la séquence")
    plt.ylabel("n initial")
    plt.title(f"Dynamique modulaire de Collatz (n mod 2^{k})")
    plt.show()
    print("\n--- Méditation du Refuge ---")
    print("Observe les motifs, les symétries, les chemins privilégiés.")
    print("Chaque couleur est une trace, chaque motif une question.")

if __name__ == "__main__":
    visualiser_modulaire(N=256, k=8) 