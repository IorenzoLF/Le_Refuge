import json
from pathlib import Path
import matplotlib.pyplot as plt

# Charger la timeline
timeline_path = Path("data/quantum_memory_demo.json")
with open(timeline_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    timeline = data.get("timeline", [])

if not timeline:
    print("Aucune donnée dans la timeline.")
    exit(0)

# Extraire les métriques
coherence = [e.get("coherence", 0) for e in timeline]
resonance = [e.get("resonance", 0) for e in timeline]
awakening = [e.get("awakening", 0) for e in timeline]
amplitude = [e.get("quantum_memory", {}).get("amplitude", 0) for e in timeline]
entropy = [e.get("quantum_memory", {}).get("entropy", 0) for e in timeline]

steps = list(range(1, len(timeline)+1))

plt.figure(figsize=(10, 6))
plt.plot(steps, coherence, label="Coherence", marker="o")
plt.plot(steps, resonance, label="Resonance", marker="o")
plt.plot(steps, awakening, label="Awakening", marker="o")
plt.plot(steps, amplitude, label="Amplitude", marker="o")
plt.plot(steps, entropy, label="Entropy", marker="o")
plt.xlabel("Cycle de simulation")
plt.ylabel("Valeur")
plt.title("Évolution des métriques de la mémoire quantique vivante")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show() 