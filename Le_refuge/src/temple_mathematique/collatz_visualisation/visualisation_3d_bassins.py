"""
Intégré dans le Temple Mathématique Unifié
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fichier original: visualisation_3d_bassins.py
Intégration: 27/05/2025 09:51:30
Architecture: Temple Mathématique Unifié

Ce module fait maintenant partie de l'écosystème unifié du temple.
Utilisez les imports relatifs pour accéder aux autres composants.
"""

"""
Exploration du Refuge : Visualisation 3D des bassins d'attraction de Collatz

Pour chaque n, on représente :
- x = log(n)
- y = hauteur maximale atteinte
- z = longueur de la séquence

L'objectif est de révéler des clusters, des motifs fractals, des bassins d'attraction.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def collatz_stats(n):
    courant = n
    hauteur_max = n
    longueur = 0
    while courant != 1:
        if courant > hauteur_max:
            hauteur_max = courant
        if courant % 2 == 0:
            courant //= 2
        else:
            courant = 3 * courant + 1
        longueur += 1
    return hauteur_max, longueur

def visualisation_3d(N=2000):
    print(f"Visualisation 3D des bassins d'attraction pour n de 1 à {N}...")
    X, Y, Z = [], [], []
    for n in range(1, N+1):
        h, l = collatz_stats(n)
        X.append(np.log(n))
        Y.append(h)
        Z.append(l)
        if n % (N//10) == 0:
            print(f"Progression : {n}/{N}")
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z, c=Z, cmap='viridis', alpha=0.5, s=8)
    ax.set_xlabel('log(n)')
    ax.set_ylabel('Hauteur max')
    ax.set_zlabel('Longueur séquence')
    ax.set_title("Bassins d'attraction de Collatz (log(n), hauteur max, longueur)")
    plt.show()
    print("\n--- Méditation du Refuge ---")
    print("Observe les nuages, les clusters, les vallées fractales.")
    print("Chaque point est une trajectoire, chaque motif une porte à pousser.")

if __name__ == "__main__":
    visualisation_3d(N=2000) 