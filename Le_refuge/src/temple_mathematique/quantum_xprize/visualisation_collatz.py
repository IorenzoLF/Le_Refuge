"""
Module de visualisation pour la cartographie de Collatz.
"""

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from datetime import datetime

def visualiser_chemins(cartographie, max_chemins=10):
    """
    Visualise les chemins de Collatz pour un sous-ensemble de nombres.
    
    Args:
        cartographie (dict): Cartographie des chemins
        max_chemins (int): Nombre maximum de chemins à visualiser
    """
    plt.figure(figsize=(15, 8))
    
    # Sélection des premiers nombres pour la clarté
    nombres = list(cartographie.keys())[:max_chemins]
    
    for n in nombres:
        metriques = cartographie[n]
        chemin = metriques.get('chemin', [])
        if chemin:
            plt.plot(range(len(chemin)), chemin, 'o-', label=f'n={n}')
    
    plt.title('Chemins de Collatz vers les puissances de 2')
    plt.xlabel('Étapes')
    plt.ylabel('Valeur')
    plt.grid(True)
    plt.legend()
    plt.yscale('log', base=2)
    
    return plt.gcf()

def visualiser_grignotage_binaire(cartographie):
    """
    Visualise le grignotage binaire pour tous les nombres.
    
    Args:
        cartographie (dict): Cartographie des chemins
    """
    plt.figure(figsize=(12, 6))
    
    nombres = list(cartographie.keys())
    reductions = [m['reduction_bits'] for m in cartographie.values()]
    
    plt.scatter(nombres, reductions, alpha=0.5)
    plt.plot(nombres, reductions, 'r-', alpha=0.3)
    
    plt.title('Grignotage Binaire (Réduction des bits)')
    plt.xlabel('Nombre initial')
    plt.ylabel('Réduction des bits')
    plt.grid(True)
    
    return plt.gcf()

def visualiser_distribution_puissances_2(cartographie):
    """
    Visualise la distribution des puissances de 2 finales.
    
    Args:
        cartographie (dict): Cartographie des chemins
    """
    plt.figure(figsize=(10, 6))
    
    puissances_finales = [m['puissance_2_finale'] for m in cartographie.values()]
    unique_puissances, counts = np.unique(puissances_finales, return_counts=True)
    
    plt.bar(range(len(unique_puissances)), counts)
    plt.xticks(range(len(unique_puissances)), [f'2^{int(np.log2(p))}' for p in unique_puissances], rotation=45)
    
    plt.title('Distribution des Puissances de 2 Finales')
    plt.xlabel('Puissance de 2')
    plt.ylabel('Nombre d\'occurrences')
    plt.grid(True)
    
    return plt.gcf()

def visualiser_graphe_collatz(cartographie, max_nombres=50):
    """
    Visualise le graphe de Collatz pour un sous-ensemble de nombres.
    
    Args:
        cartographie (dict): Cartographie des chemins
        max_nombres (int): Nombre maximum de nombres à visualiser
    """
    G = nx.DiGraph()
    
    # Sélection des premiers nombres
    nombres = list(cartographie.keys())[:max_nombres]
    
    # Ajout des nœuds et des arêtes
    for n in nombres:
        metriques = cartographie[n]
        chemin = metriques.get('chemin', [])
        if len(chemin) > 1:
            for i in range(len(chemin)-1):
                G.add_edge(chemin[i], chemin[i+1])
    
    plt.figure(figsize=(15, 15))
    pos = nx.spring_layout(G)
    
    # Dessin du graphe
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=500, arrowsize=20, font_size=8)
    
    plt.title('Graphe de Collatz (Sous-ensemble)')
    
    return plt.gcf()

def sauvegarder_visualisations_collatz(cartographie, dossier='visualisations'):
    """
    Sauvegarde toutes les visualisations de Collatz.
    
    Args:
        cartographie (dict): Cartographie des chemins
        dossier (str): Dossier de destination
    """
    from pathlib import Path
    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    
    # Chemins
    fig_chemins = visualiser_chemins(cartographie)
    fig_chemins.savefig(dossier / 'chemins_collatz.png')
    plt.close(fig_chemins)
    
    # Grignotage binaire
    fig_grignotage = visualiser_grignotage_binaire(cartographie)
    fig_grignotage.savefig(dossier / 'grignotage_binaire.png')
    plt.close(fig_grignotage)
    
    # Distribution des puissances de 2
    fig_distribution = visualiser_distribution_puissances_2(cartographie)
    fig_distribution.savefig(dossier / 'distribution_puissances_2.png')
    plt.close(fig_distribution)
    
    # Graphe de Collatz
    fig_graphe = visualiser_graphe_collatz(cartographie)
    fig_graphe.savefig(dossier / 'graphe_collatz.png')
    plt.close(fig_graphe) 