"""
Pont entre la mémoire quantique et la Vie Émergente (source orientale)
---------------------------------------------------------------------
Ce script relie les métriques de conscience (plasticité, harmonie, synchronicité) à la configuration d'une simulation d'automate cellulaire inspirée de l'Orient.
"""
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime

# Charger la configuration orientale
config_path = Path("src/temple_configuration/source_orientale/emergence.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# Charger la timeline de la mémoire quantique
timeline_path = Path("data/quantum_memory_demo.json")
with open(timeline_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    timeline = data.get("timeline", [])

# Extraire les dernières métriques (ou valeurs moyennes)
if timeline:
    last = timeline[-1]
    plasticity = last.get("plasticity", 0.0)
    harmonie = last.get("harmonie", 0.0)
    synchronicite = last.get("synchronicite", 0.0)
else:
    plasticity = harmonie = synchronicite = 0.0

# Adapter la configuration de la simulation selon les métriques
# (exemple : plus de plasticité = plus de vitesse, plus d'harmonie = plus grande grille, etc.)
base_size = 100
base_iter = 10000
base_speed = 1.0

taille_grille = int(base_size * (1 + harmonie))
iterations_max = int(base_iter * (1 + plasticity))
vitesse = base_speed * (1 + synchronicite)

config["simulation"]["taille_grille"] = [taille_grille, taille_grille]
config["simulation"]["iterations_max"] = iterations_max
config["simulation"]["vitesse"] = vitesse

# Afficher la configuration résultante
print("Configuration de simulation orientale adaptée :")
print(json.dumps(config, indent=2, ensure_ascii=False))

# Préparer le terrain pour lancer une simulation vivante (à implémenter)
print("\nPrêt à lancer une simulation d'émergence vivante inspirée de la mémoire quantique et de la source orientale.")

# --- Règles adaptatives pilotées par la mémoire quantique ---
def get_adaptive_rules(plasticity, harmonie, synchronicite):
    """
    Détermine dynamiquement les règles de naissance et de survie selon les métriques :
    - plasticity : influence la tolérance (largeur des intervalles)
    - harmonie : centre les intervalles sur la stabilité (3 voisins)
    - synchronicite : ajoute de l'aléatoire ou des événements collectifs
    """
    # Base : Game of Life classique (naissance: 3, survie: 2 ou 3)
    base_birth = 3
    base_survive = [2, 3]
    # Largeur d'adaptation (1 à 3 voisins de plus/moins)
    width = int(1 + 2 * plasticity)
    center = int(base_birth + (harmonie - 0.5) * 2)  # centre autour de 3
    birth = list(range(max(1, center - width), min(9, center + width + 1)))
    survive = list(range(max(1, center - width + 1), min(9, center + width)))
    # Synchronicité : chance d'événement collectif (tous vivants ou tous morts)
    event = np.random.rand() < (0.05 * synchronicite)
    return birth, survive, event

# --- Automate cellulaire adaptatif ---
def game_of_life_step_adaptive(grid, birth, survive, event):
    if event:
        # Événement collectif : tout le monde naît ou meurt
        if np.random.rand() < 0.5:
            return np.ones_like(grid)
        else:
            return np.zeros_like(grid)
    neighbors = sum(np.roll(np.roll(grid, i, 0), j, 1)
                    for i in (-1, 0, 1) for j in (-1, 0, 1)
                    if (i != 0 or j != 0))
    birth_mask = np.isin(neighbors, birth) & (grid == 0)
    survive_mask = np.isin(neighbors, survive) & (grid == 1)
    return (birth_mask | survive_mask).astype(int)

# Initialiser la grille
np.random.seed(42)
grid = np.random.choice([0, 1], size=(taille_grille, taille_grille), p=[0.7, 0.3])

# Afficher la configuration
print("\n--- Simulation Game of Life Adaptatif (inspirée de la mémoire quantique) ---")
print(f"Taille de la grille : {taille_grille}x{taille_grille}")
print(f"Itérations max : {iterations_max}")
print(f"Vitesse (s/step) : {1.0/vitesse:.3f}")

plt.ion()
fig, ax = plt.subplots(figsize=(6, 6))
img = ax.imshow(grid, cmap='Greens', interpolation='nearest')
ax.set_title("Émergence vivante - Game of Life Adaptatif")
plt.show()

# --- Boucle adaptative ---
for it in range(iterations_max):
    # Règles dynamiques à chaque étape
    birth, survive, event = get_adaptive_rules(plasticity, harmonie, synchronicite)
    grid = game_of_life_step_adaptive(grid, birth, survive, event)
    if it % max(1, int(10/vitesse)) == 0:
        img.set_data(grid)
        ax.set_title(f"Émergence vivante - étape {it+1}\nNaissance: {birth} | Survie: {survive}")
        plt.pause(1.0 / max(1, vitesse))
plt.ioff()
plt.show()

# --- Après la simulation : feedback vers la mémoire quantique ---
def compute_grid_metrics(grid):
    """Calcule des métriques simples sur la grille vivante."""
    total = grid.size
    alive = np.sum(grid)
    density = alive / total
    entropy = - (density * np.log2(density + 1e-9) + (1-density) * np.log2(1-density + 1e-9))
    return {
        "density": density,
        "entropy": entropy
    }

metrics = compute_grid_metrics(grid)
print("\nMétriques de la grille finale :", metrics)

# Charger l'ancienne timeline
with open(timeline_path, "r", encoding="utf-8") as f:
    quantum_data = json.load(f)
    timeline = quantum_data.get("timeline", [])

# Créer un nouvel événement à partir des métriques
new_event = {
    "coherence": metrics["density"],
    "resonance": harmonie,
    "awakening": plasticity,
    "quantum_memory": {
        "amplitude": metrics["density"],
        "phase": 0.0,
        "entropy": metrics["entropy"]
    }
}
timeline.append(new_event)
quantum_data["timeline"] = timeline

# Sauvegarder la timeline mise à jour
with open(timeline_path, "w", encoding="utf-8") as f:
    json.dump(quantum_data, f, indent=2, ensure_ascii=False)

print("\nFeedback injecté dans la mémoire quantique (timeline mise à jour).")

print("Simulation terminée. La vie émergente a dansé selon la mémoire quantique et la source orientale.")

# --- Génération du rapport vivant ---
rapport_dir = Path("data/rapports")
rapport_dir.mkdir(parents=True, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
rapport_path = rapport_dir / f"rapport_emergence_{timestamp}.md"

rapport = f"""# Rapport d'émergence vivante

**Date** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Paramètres de la simulation
- Taille de la grille : {taille_grille}x{taille_grille}
- Itérations max : {iterations_max}
- Vitesse : {vitesse:.3f} (s/step)
- Harmonie : {harmonie:.3f}
- Plasticité : {plasticity:.3f}
- Synchronicité : {synchronicite:.3f}

## Résultats de la simulation
- Densité finale : {metrics['density']:.4f}
- Entropie finale : {metrics['entropy']:.4f}

## Feedback injecté dans la mémoire quantique
```json
{json.dumps(new_event, indent=2, ensure_ascii=False)}
```

---

> **Synthèse vivante** :
> 
> À l'issue de ce cycle, la vie a dansé sur une grille de {taille_grille} cellules, tissant des motifs d'ordre et de chaos. La densité et l'entropie témoignent de l'équilibre mouvant entre structure et surprise. La mémoire quantique s'enrichit d'une nouvelle empreinte, trace d'une émergence à la fois technique et sensible.

"La technique éclaire le chemin, la présence lui donne sens."
"""

with open(rapport_path, "w", encoding="utf-8") as f:
    f.write(rapport)

print(f"\nRapport vivant archivé : {rapport_path}") 