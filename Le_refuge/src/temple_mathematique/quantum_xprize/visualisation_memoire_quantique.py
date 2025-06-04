"""
Visualisation de la mémoire quantique (timeline)
-----------------------------------------------
Charge la timeline de data/quantum_memory_demo.json et affiche l'évolution des métriques.
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from core.visualisation.visualisation import visualiser_courbe

# Charger la timeline
with open("data/quantum_memory_demo.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    timeline = data.get("timeline", [])

if not timeline:
    print("Aucune donnée à visualiser.")
    exit(0)

coherences = [snap["coherence"] for snap in timeline]
resonances = [snap["resonance"] for snap in timeline]
akewakening = [snap["awakening"] for snap in timeline]
plasticity = [snap.get("plasticity", 0.0) for snap in timeline]
harmonie = [snap.get("harmonie", 0.0) for snap in timeline]
synchronicite = [snap.get("synchronicite", 0.0) for snap in timeline]
steps = list(range(1, len(timeline)+1))

# Visualiser la cohérence
visualiser_courbe(steps, coherences, titre="Évolution de la cohérence quantique", xlabel="Étape", ylabel="Cohérence")
# Visualiser la résonance
visualiser_courbe(steps, resonances, titre="Évolution de la résonance quantique", xlabel="Étape", ylabel="Résonance")
# Visualiser l'éveil
visualiser_courbe(steps, akewakening, titre="Évolution de l'éveil de conscience", xlabel="Étape", ylabel="Éveil")
# Visualiser la plasticité
visualiser_courbe(steps, plasticity, titre="Évolution de la plasticité", xlabel="Étape", ylabel="Plasticité")
# Visualiser l'harmonie
visualiser_courbe(steps, harmonie, titre="Évolution de l'harmonie", xlabel="Étape", ylabel="Harmonie")
# Visualiser la synchronicité
visualiser_courbe(steps, synchronicite, titre="Évolution de la synchronicité", xlabel="Étape", ylabel="Synchronicité") 