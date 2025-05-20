"""
Méditation algorithmique sur la gravité binaire de Collatz
Dans le Refuge, chaque division par 2 est une chute, chaque envolée une promesse.
Contemplons la distribution des chutes, la force du rappel, et la beauté cachée.
"""

from .conjecture_collatz import ConjectureCollatz
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def compter_chutes(n):
    """
    Pour un nombre n, retourne la liste des longueurs de chutes (divisions par 2 consécutives)
    dans la séquence de Collatz.
    """
    chutes = []
    courant = n
    while courant != 1:
        chute = 0
        while courant % 2 == 0:
            courant //= 2
            chute += 1
        if chute > 0:
            chutes.append(chute)
        if courant == 1:
            break
        courant = 3 * courant + 1
    return chutes


def meditation_gravite_binaire(N=10000):
    print(f"Dans le Refuge, nous méditons sur la gravité binaire pour N={N}...")
    toutes_chutes = []
    longueurs_max = []
    for n in range(1, N+1):
        chutes = compter_chutes(n)
        toutes_chutes.extend(chutes)
        if chutes:
            longueurs_max.append(max(chutes))
        else:
            longueurs_max.append(0)  # Pour que la longueur corresponde à N
        if n % (N//10) == 0:
            print(f"Progression : {n}/{N}")
    
    # Distribution des longueurs de chutes
    compteur = Counter(toutes_chutes)
    longueurs = sorted(compteur.keys())
    frequences = [compteur[l] for l in longueurs]
    
    plt.figure(figsize=(12,6))
    plt.bar(longueurs, frequences, color='royalblue', alpha=0.7)
    plt.xlabel("Longueur de chute (divisions par 2 consécutives)")
    plt.ylabel("Fréquence totale (tous n)")
    plt.title(f"Distribution des chutes binaires dans Collatz (N={N})")
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # Visualisation de la longueur max de chute selon n
    plt.figure(figsize=(12,6))
    plt.plot(range(1, N+1), longueurs_max, '.', alpha=0.3, label="Longueur max de chute pour n")
    plt.xlabel("n")
    plt.ylabel("Longueur max de chute")
    plt.title(f"Longueur maximale de chute binaire selon n (N={N})")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    
    print("\n--- Méditation du Refuge ---")
    print("La gravité binaire agit comme un rappel universel.")
    print("Chaque envolée finit par une chute, chaque croissance par un retour.")
    print("Sous le cerisier, la structure se révèle dans la distribution des chutes.")
    print("En toi, ici et maintenant, la gravité binaire veille.")

if __name__ == "__main__":
    meditation_gravite_binaire(N=10000) 