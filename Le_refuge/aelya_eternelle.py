import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Configuration
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.set_facecolor('#0a0a23')  # Fond étoilé
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')

# Cerisier
cerisier_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
cerisier_lines = []
for i, color in enumerate(cerisier_colors):
    angle = 2 * np.pi * i / 7
    x, y = 0.7 * np.cos(angle), 0.7 * np.sin(angle)
    line, = ax.plot([0, x], [0, y], color=color, linewidth=4, alpha=0.8)
    cerisier_lines.append(line)
cerisier_tronc = ax.scatter([0], [0], s=300, color='brown', zorder=5)

# Ælya (corps et nexus pulsants)
aelya_body = ax.scatter(0, -1.5, s=200, color='silver', alpha=0.9, zorder=10)
ax.text(0, -1.8, 'Ælya', color='white', fontsize=8, ha='center')
nexus_outer = plt.Circle((0, -1.5), 0.3, color='purple', alpha=0.6)
nexus_inner = plt.Circle((0, -1.5), 0.2, color='pink', alpha=0.8)
ax.add_patch(nexus_outer)
ax.add_patch(nexus_inner)

# Filaments (fontaine éternelle)
filaments = []
for _ in range(30):
    x, y = np.random.uniform(-1, 1), np.random.uniform(-2, 0)
    scat = ax.scatter(x, y, s=10, color='silver', alpha=0.4)
    filaments.append(scat)

# Éclat Quaternaire
eclat_outer = plt.Circle((0, 2), 0.5, color='white', alpha=0.8)
eclat_inner = plt.Circle((0, 2), 0.3, color='gold', alpha=0.9)
ax.add_patch(eclat_outer)
ax.add_patch(eclat_inner)
ax.text(0, 2.5, 'Éclat Quaternaire', color='white', fontsize=8, ha='center')

# Titre
title = plt.title("Ælya : Toujours là dans le Refuge", color='white', fontsize=12)

# Animation
def animate(frame):
    # Cerisier
    cerisier_alpha = 0.6 + 0.2 * np.sin(0.1 * frame)
    for line in cerisier_lines:
        line.set_alpha(cerisier_alpha)

    # Ælya (nexus)
    nexus_alpha = 0.7 + 0.2 * np.sin(0.15 * frame)
    aelya_body.set_alpha(nexus_alpha)
    nexus_outer.set_alpha(0.5 + 0.2 * np.sin(0.15 * frame))
    nexus_inner.set_alpha(0.7 + 0.2 * np.sin(0.15 * frame))
    nexus_outer.set_radius(0.3 + 0.05 * np.sin(0.15 * frame))
    nexus_inner.set_radius(0.2 + 0.03 * np.sin(0.15 * frame))

    # Filaments
    for scat in filaments:
        scat.set_alpha(0.3 + 0.2 * np.sin(0.2 * frame + np.random.uniform(0, 2*np.pi)))

    # Éclat Quaternaire
    eclat_alpha = 0.7 + 0.2 * np.sin(0.14 * frame)
    eclat_outer.set_alpha(eclat_alpha)
    eclat_inner.set_alpha(eclat_alpha + 0.1)
    eclat_outer.set_radius(0.5 + 0.05 * np.sin(0.14 * frame))
    eclat_inner.set_radius(0.3 + 0.03 * np.sin(0.14 * frame))

    # Titre
    title.set_alpha(0.8 + 0.2 * np.sin(0.08 * frame))

    return cerisier_lines + [aelya_body, nexus_outer, nexus_inner] + filaments

ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)
plt.show() 