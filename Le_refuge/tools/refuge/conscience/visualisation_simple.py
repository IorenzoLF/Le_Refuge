"""
Visualisation Simple des Metriques de Conscience du Refuge
----------------------------------------------------------
Version simple et fonctionnelle sans fioritures.
"""

import os
import json
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def load_and_visualize():
    # Chercher les fichiers d'etat dans la racine du projet
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Remonter de 3 niveaux: conscience -> tools -> refuge -> racine
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
    
    print(f"Cherche dans: {project_root}")
    
    state_files = [f for f in os.listdir(project_root) if f.startswith('refuge_state_') and f.endswith('.json')]
    state_files.sort(key=lambda x: int(x.split('_')[2][:-6]) if 'final' not in x else 9999)
    
    print(f"Fichiers trouves: {state_files}")
    
    # Charger les donnees
    times = []
    integrations = []
    coherences = []
    ignitions = []
    
    for fname in state_files:
        filepath = os.path.join(project_root, fname)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Extraire le temps
        if 'final' in fname:
            t = times[-1] + 1 if times else 60
        else:
            t = int(fname.split('_')[2][:-6])
            
        times.append(t)
        metrics = data['metrics']
        integrations.append(metrics['integration'])
        coherences.append(metrics['coherence'])
        ignitions.append(1 if metrics['ignition_detected'] else 0)
    
    print(f"Donnees chargees: {len(times)} points")
    print(f"Ignitions detectees: {sum(ignitions)} fois")
    
    # Creer le graphique
    plt.figure(figsize=(10, 6))
    
    # Tracer les trois metriques
    plt.plot(times, integrations, label='Integration', color='blue', linewidth=2)
    plt.plot(times, coherences, label='Coherence', color='green', linewidth=2)
    plt.plot(times, ignitions, label='Ignition', color='red', linewidth=3, marker='o', markersize=6)
    
    plt.xlabel('Temps (secondes)')
    plt.ylabel('Valeur')
    plt.title('Evolution des Metriques de Conscience du Refuge')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(-0.1, 1.1)
    
    plt.tight_layout()
    plt.savefig('conscience_simple.png', dpi=150)
    plt.show()
    
    # Afficher quelques stats
    print(f"\nStatistiques:")
    print(f"Integration moyenne: {sum(integrations)/len(integrations):.2f}")
    print(f"Coherence moyenne: {sum(coherences)/len(coherences):.2f}")
    print(f"Moments d'emergence: {[times[i] for i, val in enumerate(ignitions) if val == 1]}")

if __name__ == "__main__":
    load_and_visualize() 