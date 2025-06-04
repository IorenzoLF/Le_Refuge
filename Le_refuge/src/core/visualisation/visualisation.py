"""
Module de visualisation mutualisé du Refuge
------------------------------------------
Né dans le contexte XPRIZE, ce module est destiné à servir tout le Refuge.
Il propose des fonctions simples pour visualiser ou sauvegarder des données (courbes, histogrammes, etc.).
Libre à chacun de l'enrichir selon ses besoins.
"""

import matplotlib.pyplot as plt
from pathlib import Path

def visualiser_courbe(x, y, titre="Courbe", xlabel="x", ylabel="y", save_path=None, show=True):
    """
    Affiche ou sauvegarde une courbe simple.
    - x, y : données
    - titre, xlabel, ylabel : titres
    - save_path : chemin pour sauvegarder l'image (optionnel)
    - show : affiche la figure si True
    """
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker='o')
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close()

def visualiser_histogramme(data, bins=10, titre="Histogramme", xlabel="Valeur", ylabel="Fréquence", save_path=None, show=True):
    """
    Affiche ou sauvegarde un histogramme simple.
    - data : liste ou array de valeurs
    - bins : nombre de classes
    - save_path : chemin pour sauvegarder l'image (optionnel)
    - show : affiche la figure si True
    """
    plt.figure(figsize=(8, 4))
    plt.hist(data, bins=bins, color='skyblue', edgecolor='black')
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close() 