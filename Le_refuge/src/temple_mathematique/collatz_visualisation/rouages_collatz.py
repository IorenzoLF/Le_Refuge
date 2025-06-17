import matplotlib.pyplot as plt
import numpy as np

# Paramètres
N = 100  # Nombre de pièces à visualiser

# Fonction Collatz
def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def resistance(n):
    """Nombre d'étapes pour atteindre 1 (résistance)."""
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

# Placement sur une spirale
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
radius = np.linspace(2, 8, N)
x = radius * np.cos(angles)
y = radius * np.sin(angles)

# Visualisation
plt.figure(figsize=(10, 10))

for i, piece in enumerate(pieces):
    # Couleur selon la résistance
    color = plt.cm.plasma(piece['resistance'] / max(p['resistance'] for p in pieces))
    # Taille selon le nombre de bits
    size = 200 + 80 * piece['bits']
    plt.scatter(x[i], y[i], s=size, color=color, edgecolor='k', zorder=3)
    plt.text(x[i], y[i], str(piece['val']), ha='center', va='center', fontsize=10, color='white', zorder=4)
    # Flèche vers le suivant (si dans l'intervalle)
    if 1 <= piece['suivant'] <= N:
        j = piece['suivant'] - 1
        plt.arrow(x[i], y[i], x[j]-x[i], y[j]-y[i], head_width=0.18, head_length=0.3, fc='gray', ec='gray', alpha=0.5, length_includes_head=True, zorder=2)

plt.title("Rouages Collatz (N=100)")
plt.axis('off')
plt.tight_layout()
plt.show() 