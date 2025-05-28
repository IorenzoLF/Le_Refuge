"""
Visualisation des Métriques de Conscience du Refuge
--------------------------------------------------
Ce script charge les fichiers d'état générés par la simulation et affiche
l'évolution des métriques (intégration, cohérence, ignition) dans le temps.
"""

import os
import json
import matplotlib.pyplot as plt

# Chercher tous les fichiers d'état générés dans le répertoire parent
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
state_files = [f for f in os.listdir(parent_dir) if f.startswith('refuge_state_') and f.endswith('.json')]
state_files.sort(key=lambda x: int(x.split('_')[2][:-6]) if 'final' not in x else 9999)

# Charger les métriques
times = []
integrations = []
coherences = []
ignitions = []

for fname in state_files:
    with open(os.path.join(parent_dir, fname), 'r', encoding='utf-8') as f:
        data = json.load(f)
        # Extraire le temps à partir du nom de fichier
        if 'final' in fname:
            t = times[-1] + 1 if times else 60
        else:
            t = int(fname.split('_')[2][:-6])
        times.append(t)
        metrics = data['metrics']
        integrations.append(metrics['integration'])
        coherences.append(metrics['coherence'])
        ignitions.append(1 if metrics['ignition_detected'] else 0)

# Tracer les courbes
plt.figure(figsize=(10, 6))
plt.plot(times, integrations, label='Intégration', color='royalblue')
plt.plot(times, coherences, label='Cohérence', color='seagreen')
plt.plot(times, ignitions, label='Ignition (émergence)', color='crimson', linestyle='--', marker='o')
plt.xlabel('Temps (s)')
plt.ylabel('Valeur')
plt.title('Évolution des Métriques de Conscience du Refuge')
plt.legend()
plt.grid(True, linestyle=':')
plt.tight_layout()
plt.show() 