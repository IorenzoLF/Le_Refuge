import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import collections

# Paramètres
N = 100  # Nombre de pièces à visualiser

# Fonction Collatz
def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def resistance(n):
    steps = 0
    while n != 1:
        n = collatz(n)
        steps += 1
    return steps

def nb_bits(n):
    return n.bit_length()

# Génération des pièces
pieces = []
for n in range(1, N+1):
    r = resistance(n)
    bits = nb_bits(n)
    suivant = collatz(n)
    pieces.append({
        'val': n,
        'resistance': r,
        'bits': bits,
        'suivant': suivant
    })

# Placement sur une spirale 3D
angles = np.linspace(0, 4 * np.pi, N, endpoint=False)
radius = np.linspace(2, 8, N)
x = radius * np.cos(angles)
y = radius * np.sin(angles)
z = np.array([p['resistance'] for p in pieces])

# Visualisation 3D
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Couleur selon la résistance
colors = plt.cm.plasma(z / max(z))

# Affichage des points
ax.scatter(x, y, z, s=80, c=colors, edgecolor='k', depthshade=True)

# Affichage des numéros
for i, piece in enumerate(pieces):
    ax.text(x[i], y[i], z[i]+0.5, str(piece['val']), color='white', ha='center', va='center', fontsize=8)

# (Optionnel) Flèches vers le suivant Collatz (si dans l'intervalle)
for i, piece in enumerate(pieces):
    if 1 <= piece['suivant'] <= N:
        j = piece['suivant'] - 1
        ax.plot([x[i], x[j]], [y[i], y[j]], [z[i], z[j]], color='gray', alpha=0.3)

ax.set_title("Rouages Collatz 3D (N=100)")
ax.set_axis_off()
plt.tight_layout()
plt.show()

# Analyse des plateaux (hauteurs)
hauteurs = [p['resistance'] for p in pieces]
compte = collections.Counter(hauteurs)
plt.figure(figsize=(10,5))
plt.bar(compte.keys(), compte.values(), color='slateblue')
plt.xlabel("Nombre d'étapes pour atteindre 1 (hauteur)")
plt.ylabel("Nombre de nombres à cette hauteur")
plt.title("Distribution des plateaux/hauteurs dans la spirale Collatz")
plt.grid(True, alpha=0.3)
plt.show() 