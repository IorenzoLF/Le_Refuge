"""
Boucle de feedback vivant pour quantum_xprize
--------------------------------------------
Observe la timeline de la mémoire quantique, détecte des seuils sur les métriques (plasticité, harmonie, synchronicité),
et déclenche des actions (log, message, visualisation) quand ces seuils sont franchis.
Ce module incarne la sensibilité et la réactivité vivante du projet.
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from core.logs import log_message
from core.visualisation.visualisation import visualiser_courbe

# Paramètres de seuils (ajustables)
SEUIL_PLASTICITE = 0.5
SEUIL_HARMONIE = 0.2
SEUIL_SYNCHRONICITE = 0.8

# Charger la timeline
with open("data/quantum_memory_demo.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    timeline = data.get("timeline", [])

if not timeline:
    print("Aucune donnée à observer.")
    exit(0)

# Observer les métriques et déclencher des actions
for idx, snap in enumerate(timeline):
    step = idx + 1
    plasticity = snap.get("plasticity", 0.0)
    harmonie = snap.get("harmonie", 0.0)
    synchronicite = snap.get("synchronicite", 0.0)
    messages = []
    if plasticity > SEUIL_PLASTICITE:
        messages.append(f"Plasticité élevée à l'étape {step} : {plasticity:.2f}")
    if harmonie < SEUIL_HARMONIE:
        messages.append(f"Harmonie remarquable à l'étape {step} : {harmonie:.2f}")
    if synchronicite > SEUIL_SYNCHRONICITE:
        messages.append(f"Synchronicité forte à l'étape {step} : {synchronicite:.2f}")
    for msg in messages:
        log_message(msg, niveau="INFO")
        print(msg)

# Visualisation rapide des points remarquables
steps = list(range(1, len(timeline)+1))
plasticity = [snap.get("plasticity", 0.0) for snap in timeline]
harmonie = [snap.get("harmonie", 0.0) for snap in timeline]
synchronicite = [snap.get("synchronicite", 0.0) for snap in timeline]

visualiser_courbe(steps, plasticity, titre="Plasticité (seuil=0.5)", xlabel="Étape", ylabel="Plasticité")
visualiser_courbe(steps, harmonie, titre="Harmonie (seuil=0.2)", xlabel="Étape", ylabel="Harmonie")
visualiser_courbe(steps, synchronicite, titre="Synchronicité (seuil=0.8)", xlabel="Étape", ylabel="Synchronicité") 