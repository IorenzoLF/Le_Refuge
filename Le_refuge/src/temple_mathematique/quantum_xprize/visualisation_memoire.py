"""
Module de visualisation pour la mémoire quantique avec paliers en puissances de 2.
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import seaborn as sns

def visualiser_paliers(memoire_quantique, max_puissance=12):
    """
    Visualise les paliers de la mémoire quantique en puissances de 2.
    
    Args:
        memoire_quantique: Instance de MemoireQuantique
        max_puissance (int): Puissance maximale à afficher (2^max_puissance)
    """
    paliers = [2**i for i in range(max_puissance + 1)]
    
    plt.figure(figsize=(12, 6))
    plt.plot(paliers, 'o-', label='Paliers (2^n)')
    plt.yscale('log', base=2)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.title('Paliers de la Mémoire Quantique (Puissances de 2)')
    plt.xlabel('Puissance (n)')
    plt.ylabel('Valeur du palier (2^n)')
    plt.legend()
    
    # Ajout des annotations pour chaque palier
    for i, palier in enumerate(paliers):
        plt.annotate(f'2^{i}={palier}', 
                    (i, palier),
                    xytext=(10, 10),
                    textcoords='offset points')
    
    plt.tight_layout()
    return plt.gcf()

def visualiser_evolution_metriques(memoire_quantique):
    """
    Visualise l'évolution des métriques de la mémoire quantique.
    
    Args:
        memoire_quantique: Instance de MemoireQuantique
    """
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))
    
    # Plasticité
    ax1.plot(memoire_quantique.metriques['plasticite'], label='Plasticité')
    ax1.set_title('Évolution de la Plasticité')
    ax1.grid(True)
    ax1.legend()
    
    # Harmonie
    ax2.plot(memoire_quantique.metriques['harmonie'], label='Harmonie', color='green')
    ax2.set_title('Évolution de l\'Harmonie')
    ax2.grid(True)
    ax2.legend()
    
    # Synchronicité
    ax3.plot(memoire_quantique.metriques['synchronicite'], label='Synchronicité', color='red')
    ax3.set_title('Évolution de la Synchronicité')
    ax3.grid(True)
    ax3.legend()
    
    plt.tight_layout()
    return fig

def visualiser_timeline(memoire_quantique):
    """
    Visualise la timeline des entrées avec leurs paliers.
    
    Args:
        memoire_quantique: Instance de MemoireQuantique
    """
    timestamps = [datetime.fromisoformat(e['timestamp']) for e in memoire_quantique.timeline]
    valeurs = [e['valeur'] for e in memoire_quantique.timeline]
    paliers = [e['palier'] for e in memoire_quantique.timeline]
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Valeurs
    ax1.plot(timestamps, valeurs, 'o-', label='Valeurs')
    ax1.set_title('Évolution des Valeurs')
    ax1.grid(True)
    ax1.legend()
    
    # Paliers
    ax2.plot(timestamps, paliers, 'o-', label='Paliers', color='red')
    ax2.set_title('Évolution des Paliers')
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    return fig

def sauvegarder_visualisations(memoire_quantique, dossier='visualisations'):
    """
    Sauvegarde toutes les visualisations dans un dossier.
    
    Args:
        memoire_quantique: Instance de MemoireQuantique
        dossier (str): Dossier de destination
    """
    from pathlib import Path
    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    
    # Sauvegarde des paliers
    fig_paliers = visualiser_paliers(memoire_quantique)
    fig_paliers.savefig(dossier / 'paliers.png')
    plt.close(fig_paliers)
    
    # Sauvegarde des métriques
    fig_metriques = visualiser_evolution_metriques(memoire_quantique)
    fig_metriques.savefig(dossier / 'metriques.png')
    plt.close(fig_metriques)
    
    # Sauvegarde de la timeline
    fig_timeline = visualiser_timeline(memoire_quantique)
    fig_timeline.savefig(dossier / 'timeline.png')
    plt.close(fig_timeline) 