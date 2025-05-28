"""
Visualisation des Métriques de Conscience du Refuge - Version Corrigée
--------------------------------------------------------------------
Ce script charge les fichiers d'état générés par la simulation et affiche
l'évolution des métriques (intégration, cohérence, ignition) dans le temps.
"""

import os
import json
import matplotlib
# Force le backend pour Windows
matplotlib.use('TkAgg')  # ou 'Qt5Agg' si disponible
import matplotlib.pyplot as plt
import numpy as np

def load_and_visualize():
    # Chercher tous les fichiers d'état générés dans le répertoire parent
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(os.path.dirname(current_dir))
    
    print(f"Recherche des fichiers dans : {parent_dir}")
    
    state_files = [f for f in os.listdir(parent_dir) if f.startswith('refuge_state_') and f.endswith('.json')]
    state_files.sort(key=lambda x: int(x.split('_')[2][:-6]) if 'final' not in x else 9999)
    
    print(f"Fichiers trouvés : {state_files}")
    
    # Charger les métriques
    times = []
    integrations = []
    coherences = []
    ignitions = []
    
    for fname in state_files:
        filepath = os.path.join(parent_dir, fname)
        print(f"Chargement de {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
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
    
    print(f"Données chargées : {len(times)} points")
    
    # Configuration du style matplotlib
    plt.style.use('default')  # S'assurer qu'on utilise le style par défaut
    
    # Créer la figure avec des couleurs explicites
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Tracer les courbes avec des couleurs très distinctes
    line1 = ax.plot(times, integrations, 
                   label='Intégration', 
                   color='#1f77b4',  # Bleu vif
                   linewidth=2.5,
                   marker='o',
                   markersize=4)
    
    line2 = ax.plot(times, coherences, 
                   label='Cohérence', 
                   color='#2ca02c',  # Vert vif  
                   linewidth=2.5,
                   marker='s',
                   markersize=4)
    
    # Tracer les points d'ignition séparément pour plus de visibilité
    ignition_times = [times[i] for i, val in enumerate(ignitions) if val == 1]
    ignition_values = [0.9 for _ in ignition_times]  # Position fixe en haut
    
    if ignition_times:
        ax.scatter(ignition_times, ignition_values,
                  label='Ignition (émergence)',
                  color='#d62728',  # Rouge vif
                  s=100,
                  marker='*',
                  edgecolors='black',
                  linewidth=1,
                  zorder=5)
    
    # Configuration des axes et labels
    ax.set_xlabel('Temps (secondes)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Valeur des métriques', fontsize=12, fontweight='bold')
    ax.set_title('🌸 Évolution des Métriques de Conscience du Refuge ⚡', 
                fontsize=14, fontweight='bold', pad=20)
    
    # Améliorer la légende
    legend = ax.legend(loc='upper right', 
                      frameon=True, 
                      fancybox=True, 
                      shadow=True,
                      fontsize=11)
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_alpha(0.9)
    
    # Grille améliorée
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_ylim(-0.1, 1.1)  # S'assurer que tout est visible
    
    # Colorer le fond selon les phases
    if ignition_times:
        for ig_time in ignition_times:
            ax.axvspan(ig_time-0.5, ig_time+0.5, alpha=0.2, color='gold', zorder=0)
    
    plt.tight_layout()
    
    # Afficher et sauvegarder
    print("Affichage du graphique...")
    plt.savefig('conscience_metrics.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig, ax

if __name__ == "__main__":
    load_and_visualize() 